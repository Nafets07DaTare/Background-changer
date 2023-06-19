import os
import random
import ctypes
import time
import nafets
import winreg
from colorama import init, Fore
import pystray
from pystray import MenuItem as item
from PIL import Image

init(autoreset=True)

nafets.my_information()
print(Fore.GREEN + "AUTO CHANGE WALLPAPER")
print(Fore.GREEN + "MADE BY NAFETS")


def wallpaper_set(imagine):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, imagine, 3)


def startup():
    script_path = os.path.abspath(__file__)
    key_name = "Background changer"
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, key_name, 0, winreg.REG_SZ, script_path)
    winreg.CloseKey(key)


startup()

while True:
    photochoice = random.randint(1, 7)

    if photochoice == 1:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        imagine = os.path.join(current_dir, '1.jpg')
        wallpaper_set(imagine)
    if photochoice == 2:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        imagine = os.path.join(current_dir, '2.jpg')
        wallpaper_set(imagine)
    if photochoice == 3:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        imagine = os.path.join(current_dir, '3.jpg')
        wallpaper_set(imagine)
    if photochoice == 4:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        imagine = os.path.join(current_dir, '4.jpg')
        wallpaper_set(imagine)
    if photochoice == 5:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        imagine = os.path.join(current_dir, '5.jpg')
        wallpaper_set(imagine)
    if photochoice == 6:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        imagine = os.path.join(current_dir, '6.jpg')
        wallpaper_set(imagine)
    if photochoice == 7:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        imagine = os.path.join(current_dir, '7.jpg')
        wallpaper_set(imagine)

    time.sleep(1800)
