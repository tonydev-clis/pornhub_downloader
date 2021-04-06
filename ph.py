import json
import requests

def read_json(filename='data.json'):
    with open(filename, 'r+', encoding='utf-8') as file:
        data = json.loads(file.read())
    return data

def collect(data):
    new_links = []
    while True:
        new_link = input('Insert new links: ').lower()
        if new_link == 'q' or new_link == 'b' or len(new_link) == 0:
            break
        if new_link == 'd':
            delete_link(data)
        if new_link in data:
            print('Duplicate links')
            continue
        else:
            new_links.append(new_link)
    return new_links

def write_json(data, new_links, filename='data.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(data+new_links))

def collect_links():
    data = read_json()
    new_links = collect(data)
    write_json(data,new_links)

def delete_link(data):
    while True:
        links_to_delete = input('Links to delete: ').lower()
        if links_to_delete == 'b' or links_to_delete == 'q' or len(links_to_delete) == 0:
            break
        else:
            data.remove(links_to_delete)


if __name__ == '__main__':
    collect_links()