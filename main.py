from pyautogui import *
import pygetwindow as gw
import pyautogui
import time
import keyboard
import random
import os
from pynput.mouse import Button, Controller

os.system('title telegram: @kryyaasoft')

mouse = Controller()
time.sleep(0.5)

window_input = "\nВведите название окна (1 - TelegramDesktop | 2 - iMe): "
window_not_found = "[❌] | Окно - {} не найдено!"
window_found = "[✅] | Окно найдено - {}\nНажмите 'q' для паузы."
pause_message = "Пауза \nНажмите снова 'q' что бы продолжить"
continue_message = 'Продолжение работы.'

def click(x, y):
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)


window_name = input(window_input)

if window_name == '1':
    window_name = "TelegramDesktop"

if window_name == '2':
    window_name = "iMe"


check = gw.getWindowsWithTitle(window_name)
if not check:
    print(window_not_found.format(window_name))
else:
    print(window_found.format(window_name))

telegram_window = check[0]
paused = False

while True:
    if keyboard.is_pressed('q'):
        paused = not paused
        if paused:
            print(pause_message)
        else:
            print(continue_message)
        time.sleep(0.2)

    if paused:
        continue

    window_rect = (
        telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height
    )

    if telegram_window != []:
        try:
            telegram_window.activate()
        except:
            telegram_window.minimize()
            telegram_window.restore()

    scrn = pyautogui.screenshot(region=(window_rect[0], window_rect[1], window_rect[2], window_rect[3]))

    width, height = scrn.size
    pixel_found = False
    if pixel_found == True:
        break

    for x in range(0, width, 20):
        for y in range(0, height, 20):
            r, g, b = scrn.getpixel((x, y))
            if (b in range(0, 125)) and (r in range(102, 220)) and (g in range(200, 255)):
                screen_x = window_rect[0] + x
                screen_y = window_rect[1] + y
                click(screen_x + 4, screen_y)
                time.sleep(0.001)
                pixel_found = True
                break
