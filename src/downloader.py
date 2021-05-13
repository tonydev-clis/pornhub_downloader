import youtube_dl
import json
from time import sleep as s
from twilio.rest import Client
from logger import pornhub_logger
def get_storage_links(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        downloaded_links = data['downloaded_links']
        new_links = data['new_links']
        return downloaded_links, new_links


def download(new_links):
    options = {
        'noplaylist': True,
        'format': 'best[ext=mp4]/best',
        'ignoreerrors': True
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        for new_link in new_links:
            try:
                info_dict = ydl.extract_info(new_link)

            # ydl.download(links)
            except Exception as e:
                pornhub_logger.warning(f"{new_link}\n{e}")
                continue
def organize_links(downloaded_links, new_links):
    downloaded_links += new_links
    return downloaded_links

def write_json(filename, downloaded_links):
    with open(filename, 'w') as file:
        json.dump({'downloaded_links': downloaded_links, 'new_links': []}, file)
    

def main(filename):
    downloaded_links, new_links = get_storage_links(filename)
    download(new_links)
    organized_links = organize_links(downloaded_links, new_links)
    write_json(filename, organized_links)


if __name__ == '__main__':
    main('./data/data.json')