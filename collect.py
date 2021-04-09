import json
import requests
import re
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(lineno)s: %(message)s')
def read_json(filename='data.json'):
    with open(filename, 'r+', encoding='utf-8') as file:
        data = json.load(file)['links']
    return data

def collect(data):
    new_links = []
    while True:
        new_link = input('Insert new links: ').lower()
        if new_link == 'q' or new_link == 'b' or len(new_link) == 0:
            logging.info('Program has ended')
            break
        if new_link in data:
            logging.warning('Duplicate links in storage')
            continue
        if new_link in new_links:
            logging.warning('Duplicate links in recent entered link')
            continue
        if 'https://www.pornhub.com/view_video.php?viewkey' not in new_link:
            logging.warning('Not a valid pornhub link!')
            continue
        else:
            new_links.append(new_link)
    return new_links

def write_json(data, new_links, filename='data.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(({'links':data+new_links}),file)

def collect_links():
    data = read_json()
    new_links = collect(data)
    write_json(data,new_links)

if __name__ == '__main__':
    collect_links()