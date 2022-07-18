from selenium import webdriver
from selenium_stealth import stealth
import time
import mouse
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

 # options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r"C:\Program Files (x86)\chromedriver.exe")

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

driver.get("https://www.fidelity.com/")
time.sleep(3)
username = driver.find_element(By.ID, 'userId-input')
# input username here  -> username.send_keys('')
time.sleep(1)
pw = driver.find_element(By.ID, 'password')
# input password here  -> pw.send_keys('')
time.sleep(1)
login_button = driver.find_element(By.ID, 'fs-login-button')
login_button.click()
time.sleep(4)

pos = driver.find_element(By.XPATH, '/html/body/ap143528-portsum-dashboard-root/dashboard-root/div/div[3]/accounts-selector/nav/div[2]/div[3]/div/pvd3-link/s-root/span/a')
pos.click()
time.sleep(4)

contrib_button = driver.find_element(By.XPATH, '/html/body/ap143528-portsum-dashboard-root/dashboard-root/div/div[3]/div/div/div[2]/div/new-tab-group/new-tab-group-ui/div[2]/summary-panel/div/div[2]/div/div[2]/ira-contribution-container/ira-contribution/div/div[2]/pvd3-link/s-root/span/a')
contrib_button.click()
time.sleep(3)

keyboard = Controller()
def press(button):
    keyboard.press(button)
    keyboard.release(button)
    
c = 0
while c < 3:
    press(Key.tab)
    c = c+1
press(Key.enter)

d = 0
while d < 3:
    press(Key.down)
    d = d+1
press(Key.enter)
time.sleep(1)

e = 0
while e < 3:
    press(Key.tab)
    e = e+1
    
press(Key.enter)
press(Key.down)
press(Key.enter)
time.sleep(2)

g = 0
while g < 4:
    press(Key.tab)
    g = g+1

time.sleep(2)
keyboard.press('1')
keyboard.press('0')
press(Key.tab)
press(Key.enter)
time.sleep(2)

press(Key.tab)
press(Key.tab)
press(Key.enter)
time.sleep(6)

### funds are now sent for account to invest with

driver.get("https://www.fidelity.com/")

f = 0
while f < 10:
    press(Key.tab)
    f = f+1
press(Key.enter)
time.sleep(1)

press(Key.tab)
press(Key.tab)
press(Key.enter)
time.sleep(4)

mouse.move('343', '965')
time.sleep(2)
mouse.click()
mouse.move('359', '1017')
time.sleep(1)
mouse.click()
time.sleep(2)

k = 0
while k < 6:
    press(Key.tab)
    k = k+1
press(Key.enter)
press(Key.enter)
press(Key.tab)
keyboard.press('1')
keyboard.press('0')
time.sleep(2)

mouse.move('193', '607')
mouse.click()
mouse.move('195', '711')
mouse.click()
## fzrox fund has now been bought

time.sleep(6)
driver.quit()


