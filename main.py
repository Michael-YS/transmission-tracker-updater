import requests
from transmission_rpc import Client, Torrent, Status
import logging

import config

logging.basicConfig(
    level=config.LOG_LEVEL,
    format=config.LOG_FORMAT,
    filename=config.LOG_FILE,
)


def fetch_tracker(tracker_url: str) -> list[str]:
    try:
        response = requests.get(tracker_url, timeout=config.TIMEOUT)
        response.raise_for_status()
        trackers = [line.strip() for line in response.text.splitlines() if line.strip()]
        logging.info(f"Fetched {len(trackers)} trackers from {tracker_url}")
        return trackers
    except requests.RequestException as e:
        logging.error(f"Failed to fetch tracker from {tracker_url}: {e}")
        return []


def fetch_all_trackers(tracker_list: list[str]) -> list[str]:
    all_trackers = []
    for tracker_url in tracker_list:
        trackers = fetch_tracker(tracker_url)
        all_trackers.extend(trackers)
    unique_trackers = list(dict.fromkeys(all_trackers))
    logging.info(f"Total unique trackers fetched: {len(unique_trackers)}")
    return unique_trackers


def get_active_torrents(client: Client) -> list[Torrent]:
    try:
        torrents = list(filter(lambda x: x.status != Status.STOPPED, client.get_torrents()))
        logging.info(f"Retrieved {len(torrents)} active torrents")
        return torrents
    except Exception as e:
        logging.error(f"Failed to retrieve torrents: {e}")
        return []


def update_a_torrent_tracker(client: Client, torrent: Torrent, trackers: list[str]) -> int:
    exist_trackers = [t.announce for t in torrent.trackers]
    merged_trackers = list(dict.fromkeys(exist_trackers + trackers))
    valid_trackers = [t for t in merged_trackers if t.startswith(("http://", "https://", "udp://", "wss://"))]
    invalid_trackers = [t for t in merged_trackers if t not in valid_trackers]
    if invalid_trackers:
        logging.warning(f"Filtered out {len(invalid_trackers)} invalid trackers: {invalid_trackers}")
    tier_list = [[t] for t in valid_trackers]
    client.change_torrent(
        ids=torrent.id,
        tracker_list=tier_list
    )
    logging.info(f"Updated torrent {torrent.name} with {len(valid_trackers)} trackers")
    return torrent.id


def update_all_torrents_tracker(client: Client, torrents: list[Torrent], trackers: list[str]) -> list[int | str]:
    updated_ids = []
    for torrent in torrents:
        torrent_id = update_a_torrent_tracker(client, torrent, trackers)
        updated_ids.append(torrent_id)
    logging.info(f"Updated {len(updated_ids)} torrents with new trackers")
    return updated_ids


def main():
    try:
        client = Client(
            protocol="https" if config.USE_HTTPS else "http",
            username=config.TRANSMISSION_RPC_USERNAME,
            password=config.TRANSMISSION_RPC_PASSWORD,
            host=config.TRANSMISSION_RPC_HOST,
            port=config.TRANSMISSION_RPC_PORT,
            path=config.TRANSMISSION_RPC_PATH,
            timeout=config.TIMEOUT,
            logger=logging.getLogger()
        )
    except Exception as e:
        logging.error(f"Failed to connect to Transmission: {e}")
        return

    trackers = fetch_all_trackers(config.TRACKER_LIST)
    torrents = get_active_torrents(client)
    ids = update_all_torrents_tracker(client, torrents, trackers)
    client.reannounce_torrent(ids=ids)
    logging.info("Reannounced all updated torrents")
    logging.info(f"Tracker update process completed. Processed {len(torrents)} torrents.")


if __name__ == "__main__":
    main()