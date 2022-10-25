from pyautogui import *
import os
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

# Tile 2 Position: X:  682 Y:  400 RGB: (  0,   0,   0)
# Tile 3 Position: X:  770 Y:  400 RGB: ( 79,  82, 116)
# Tile 4 Position: X:  869 Y:  400 RGB: ( 80,  83, 116)
time.sleep(2)


def iniciar(x=520, y=649):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)  # This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)  # This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.01)


iniciar()

time.sleep(.5)

while keyboard.is_pressed('q') == False:

    if (pyautogui.pixel(265, 527))[0] == 0:
        click(265, 527)
    if pyautogui.pixel(265, 326)[0] == 0:
        click(265, 326)
    if pyautogui.pixel(339, 326)[0] == 0:
        click(339, 326)
    if pyautogui.pixel(417, 326)[0] == 0:
        click(417, 326)
    if pyautogui.pixel(512, 326)[0] == 0:
        click(512, 326)
    if pyautogui.pixel(339, 518)[0] == 0:
        click(339, 518)
    if pyautogui.pixel(417, 518)[0] == 0:
        click(417, 518)
    if pyautogui.pixel(512, 518)[0] == 0:
        click(512, 518)
