import youtube_dl
import json
from time import sleep as s
from twilio.rest import Client
from logger import pornhub_logger
from collect import get_storage_links


def start_download(new_links):
    options = {
        'noplaylist': True,
        'format': 'best[ext=mp4]/best',
        'ignoreerrors': True
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        for new_link in new_links:
            try:
                info_dict = ydl.extract_info(new_link)

            # ydl.start_download(links)
            except Exception as e:
                pornhub_logger.warning(f"{new_link}\n{e}")
                continue


def organize_links(downloaded_links, new_links):
    downloaded_links += new_links
    return downloaded_links


def write_downloaded_json(filename, downloaded_links):
    with open(filename, 'w') as file:
        json.dump({
            'downloaded_links': downloaded_links,
            'new_links': []
        },
                  file,
                  indent=4)


def download(filename='./data/data.json'):
    downloaded_links, new_links = get_storage_links(filename)
    start_download(new_links)
    organized_links = organize_links(downloaded_links, new_links)
    write_downloaded_json(filename, organized_links)


if __name__ == '__main__':
    download()