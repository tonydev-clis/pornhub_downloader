import webbrowser
import json
chrome_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe %s --incognito'
with open('data.json', 'r+', encoding='utf-8') as file:
    links = json.load(file)['links']
    
def open():
    webbrowser.get(chrome_path).open_new(url)