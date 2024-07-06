import pyautogui
from pynput import keyboard

CARD_1_X = 853
CARD_2_X = 958
CARD_3_X = 1066
CARD_4_X = 1173

Y_VAL = 920

def on_press(key):
    if key == keyboard.Key.esc:
        raise Exception(key)
    
    mouseX, mouseY = pyautogui.position()

    try:
        key_char = key.char

        match key_char:
            case '1':
                pyautogui.moveTo(CARD_1_X, Y_VAL)
                pyautogui.click()
                pyautogui.moveTo(mouseX, mouseY)
            case '2':
                pyautogui.moveTo(CARD_2_X, Y_VAL)
                pyautogui.click()
                pyautogui.moveTo(mouseX, mouseY)
            case '3':
                pyautogui.moveTo(CARD_3_X, Y_VAL)
                pyautogui.click()
                pyautogui.moveTo(mouseX, mouseY)
            case '4':
                pyautogui.moveTo(CARD_4_X, Y_VAL)
                pyautogui.click()
                pyautogui.moveTo(mouseX, mouseY)
            case _:
                print('Key {0} pressed'.format(key))
                return
    except:
        print("invalid key pressed")

def main():
    while True:
        # start keyboard listener (blocking)
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()


if __name__ == '__main__':
    main()