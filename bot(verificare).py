import pyautogui
import time 
import keyboard

def cautare_google():
    time.sleep(3)
    if pyautogui.locateOnScreen(r'C:\Users\Tudor\Desktop\Univer\Metode avansate de programare\Laborator\poza.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'C:\Users\Tudor\Desktop\Univer\Metode avansate de programare\Laborator\poza.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write('https://www.youtube.com/')
        pyautogui.press('enter')
    else:
        print("Imaginea nu este pe ecran")

cautare_google()

def cautare_youtube():
    time.sleep(3)
    if pyautogui.locateOnScreen(r'C:\Users\Tudor\Desktop\Univer\Metode avansate de programare\Laborator\poza1.png', confidence=0.7) != None:
        camp_youtube = pyautogui.locateOnScreen(r'C:\Users\Tudor\Desktop\Univer\Metode avansate de programare\Laborator\poza1.png', confidence=0.7)
        pyautogui.click(camp_youtube)
        time.sleep(1)
        pyautogui.write('iUmor')
        pyautogui.press('enter')
    else:
        print("Imaginea nu este pe ecran")

cautare_youtube()

def click_canal():
    time.sleep(3)
    if pyautogui.locateOnScreen(r'C:\Users\Tudor\Desktop\Univer\Metode avansate de programare\Laborator\poza2.png', confidence=0.7) != None:
        imagine_canal = pyautogui.locateOnScreen(r'C:\Users\Tudor\Desktop\Univer\Metode avansate de programare\Laborator\poza2.png', confidence=0.7)
        pyautogui.click(imagine_canal)
        time.sleep(1)
    else:
        print("Imaginea nu este pe ecran")

click_canal()

def click_aboneazate():
    time.sleep(3)
    if pyautogui.locateOnScreen(r'C:\Users\Tudor\Desktop\Univer\Metode avansate de programare\Laborator\poza3.png', confidence=0.7) != None:
        imagine_aboneazate = pyautogui.locateOnScreen(r'C:\Users\Tudor\Desktop\Univer\Metode avansate de programare\Laborator\poza3.png', confidence=0.7)
        pyautogui.click(imagine_aboneazate)
        time.sleep(1)
    else:
        print("Imaginea nu este pe ecran")

click_aboneazate()

def click_videoclipuri():
    time.sleep(3)
    if pyautogui.locateOnScreen(r'C:\Users\Tudor\Desktop\Univer\Metode avansate de programare\Laborator\poza4.png', confidence=0.7) != None:
        imagine_videoclipuri = pyautogui.locateOnScreen(r'C:\Users\Tudor\Desktop\Univer\Metode avansate de programare\Laborator\poza4.png', confidence=0.7)
        pyautogui.click(imagine_videoclipuri)
        time.sleep(1)
    if pyautogui.locateOnScreen(r'C:\Users\Tudor\Desktop\Univer\Metode avansate de programare\Laborator\poza5.png', confidence=0.7) != None:
        imagine_videoclipuri = pyautogui.locateOnScreen(r'C:\Users\Tudor\Desktop\Univer\Metode avansate de programare\Laborator\poza5.png', confidence=0.7)
        pyautogui.click(imagine_videoclipuri)
        time.sleep(1)
    if pyautogui.locateOnScreen(r'C:\Users\Tudor\Desktop\Univer\Metode avansate de programare\Laborator\poza6.png', confidence=0.7) != None:
        imagine_videoclipuri = pyautogui.locateOnScreen(r'C:\Users\Tudor\Desktop\Univer\Metode avansate de programare\Laborator\poza6.png', confidence=0.7)
        pyautogui.click(imagine_videoclipuri)
        time.sleep(1)
    else:
        print("Imaginea nu este pe ecran")

click_videoclipuri()