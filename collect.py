import json
import requests
import re
def read_json(filename='data.json'):
    with open(filename, 'r+', encoding='utf-8') as file:
        data = json.load(file)['links']
    return data

def collect(data):
    new_links = []
    while True:
        new_link = input('Insert new links: ').lower()
        if new_link == 'q' or new_link == 'b' or len(new_link) == 0:
            break
        if new_link in data:
            print('Duplicate links in storage')
            continue
        if new_link in new_links:
            print('Duplicate links in recent entered link')
            continue
        if 'https://www.pornhub.com/view_video.php?viewkey' not in new_link:
            print('Not a valid pornhub link!')
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