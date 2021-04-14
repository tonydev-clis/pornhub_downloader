import youtube_dl
import json
from time import sleep as s
from twilio.rest import Client
from logger import pornhub_logger
def get_links(filename='./data/data.json'):
    with open(filename, 'r') as file:
        return json.load(file)['links']


def download(links):
    options = {
        'noplaylist': True,
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        for link in links:
            try:
                info_dict = ydl.extract_info(link)
                video_url = info_dict.get('url', None)
                video_id = info_dict.get('id', None)
                video_title = info_dict.get('title', None)

            # ydl.download(links)
            except Exception as e:
                # account_sid = "AC67d1437cea8593339dce6ec20c4eeeb3"
                # auth_token = "60e2616f01b750c78efd6d44022a8210"
                # client = Client(account_sid, auth_token)
                # client = Client(account_sid, auth_token)
                # message = client.messages.create(
                #     body={'ph download error'}, from_="+18592953746", to="+62816300111")
                pornhub_logger.warning(f"{link}\n{e}")
                continue


def main():
    links = get_links()
    download(links)


if __name__ == '__main__':
    main()