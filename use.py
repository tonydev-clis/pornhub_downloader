import json
import pyperclip
with open('./data.json', 'r') as file:
    links = json.load(file)['links']
    for x, y in enumerate(links):
        print(x, y)
    while True:
        index = input('Which link that you want to watch?: ')
        if index == 'q' or index == '':
            break
        index = int(index)
        check = input('Delete link or nah?: ').lower()
        print(links[index] + ' it is')
        pyperclip.copy(links[index])
        if check == 'n' or check == 'no':
            continue
        elif check == 'y' or check == 'yes':
            links.pop(index)
with open('./data.json', 'w') as file:
    json.dump({'links': links}, file)
