import json
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s: %(lineno)s: %(message)s')


def get_storage_links(filename):
    with open(filename, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        downloaded_links = data['downloaded_links']
        new_data = data['new_links']
    return downloaded_links, new_data


def check(downloaded_links, new_data):
    while True:
        new_link = input('Insert new links: ').lower()
        if new_link == 'q' or new_link == 'b' or len(new_link) == 0:
            logging.info('Program has ended')
            break
        if new_link in downloaded_links:
            logging.warning('Duplicate links in storage')
            continue
        if new_link in new_data:
            logging.warning('Duplicate links in recent entered link')
            continue
        if 'https://www.pornhub.com/view_video.php?viewkey' not in new_link:
            logging.warning('Not a valid pornhub link!')
            continue
        else:
            new_data.append(new_link)
    return new_data


def write_json(downloaded_links, checked_new_data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump({
            'downloaded_links': downloaded_links,
            'new_links': checked_new_data
        },
                  file,
                  indent=4)


def collect_links(filename='./data/data.json'):
    downloaded_links, new_data = get_storage_links(filename)
    checked_new_data = check(downloaded_links, new_data)
    write_json(downloaded_links, checked_new_data, filename)


if __name__ == '__main__':
    collect_links()