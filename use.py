import os
import subprocess
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from time import sleep as s
username = os.getenv('USERPROFILE')
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('start-maximized')
options.add_argument('log-level=3')
options.add_argument(fr'user-data-dir={username}\AppData\Local\Google\Chrome\User Data\Default')
options.add_argument(r'--load-extension=C:\Users\owenw\Downloads\build-chrome')
options.add_extension(r'C:\Users\owenw\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.31.0_0.crx')
driver = webdriver.Chrome(executable_path=r'C:\Users\owenw\vscode\chromedriver.exe', options=options)
