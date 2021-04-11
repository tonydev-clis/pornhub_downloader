import youtube_dl
import json
from time import sleep as s

def get_links(filename='data.json'):
    with open(filename, 'r') as file:
        return json.load(file)['links']

def download(links):
    options = {'noplaylist': True, 'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', 'continue_dl': True }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([links[0]])

def main():
    links = get_links()
    download(links)

if __name__ == '__main__':
    main()