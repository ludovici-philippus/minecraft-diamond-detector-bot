import pyautogui
import pydirectinput
import keyboard
import numpy as np
import cv2
from time import sleep

found_diamond = False
lower_range_diamond = np.array([75, 80, 100])
upper_range_diamond = np.array([90, 255, 255])

lower_range_lava = np.array([7, 216, 193])
upper_range_lava = np.array([23, 255, 255])

pyautogui.alert("A automação vai começar, não mexa em nada.")

def mine():
    terminated = False
    while not found_diamond and not terminated:
        if keyboard.is_pressed("u"):
            release_keys()
            terminated = True
            break
        
        else:
            detect_color()
            sleep(1)
            if detect_color():
                break
            pydirectinput.keyDown("shift")
            pydirectinput.keyDown("w")
            pydirectinput.mouseDown()

def release_keys():
    pydirectinput.keyUp("w")
    pydirectinput.mouseUp()

def detect_color():
    global found_diamond
    img_1 = pyautogui.screenshot(".\currentImagem.png")
    img_1 = cv2.imread(".\currentImagem.png")
    hsv = cv2.cvtColor(cv2.UMat(img_1), cv2.COLOR_BGR2HSV)
    mask_diamond = cv2.inRange(hsv, lower_range_diamond, upper_range_diamond)
    mask_lava = cv2.inRange(hsv, lower_range_lava, upper_range_lava)

    cv2.imwrite(r".\CurrentMaskDiamond.png", mask_diamond)
    cv2.imwrite(r".\CurrentMaskLava.png", mask_lava)
    if cv2.countNonZero(mask_diamond) > 5000:
        pydirectinput.press("t")
        pydirectinput.press("a")
        pydirectinput.write("Achei diamante!")
        pydirectinput.press("enter")
        found_diamond = True
        return True
        quit() 
    
    if cv2.countNonZero(mask_lava) > 25000:
        release_keys()
        pydirectinput.moveRel(0, -1000)
        pydirectinput.press("8")
        pydirectinput.rightClick()
        print("Found lava")
        sleep(2)
        pydirectinput.rightClick()
        pydirectinput.press('1')
        pydirectinput.moveRel(0, 500)

sleep(3)


mine()
