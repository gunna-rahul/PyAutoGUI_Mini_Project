import pyautogui as pg
import time
import random
import keyboard as key

time.sleep(3)
print(pg.position())

pg.leftClick(643, 103)
time.sleep(1)
key.write("#python") #typewrite doesnt support #symbol
time.sleep(2)

pg.leftClick(650, 164)
time.sleep(3)

list = ['thats awesome','great one','perfect']

for i in range(10):
    pg.doubleClick(418,388)
    time.sleep(1)
    pg.leftClick(888, 680, 1)
    msg = random.choice(list)
    pg.typewrite(msg)
    time.sleep(1)
    pg.press('enter')
    time.sleep(5)
    
    pg.leftClick(1322, 391)
    time.sleep(3)
    