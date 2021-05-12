import youtube_dl
import json
from time import sleep as s
from twilio.rest import Client
from logger import pornhub_logger
def get_links(filename=r'C:\Users\owenw\vscode\projects\Pornhub\data\data.json'):
    with open(filename, 'r') as file:
        return json.load(file)['links']


def download(links):
    options = {
        'noplaylist': True,
        'format': 'best[ext=mp4]/best'
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        for link in links:
            try:
                info_dict = ydl.extract_info(link)

            # ydl.download(links)
            except Exception as e:
                pornhub_logger.warning(f"{link}\n{e}")
                continue


def main():
    links = get_links()
    download(links)


if __name__ == '__main__':
    main()