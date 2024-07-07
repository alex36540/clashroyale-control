from pynput import keyboard, mouse

# Constants for mouse positions
CARD_1_X = 853
CARD_2_X = 958
CARD_3_X = 1066
CARD_4_X = 1173

Y_VAL = 920

mouse_ctrl = mouse.Controller()

def on_press(key):
    # Quit case
    if key == keyboard.Key.esc:
        raise Exception(key)
    
    original_pos = mouse_ctrl.position

    try:
        key_char = key.char

        # Move mouse to correct card
        match key_char:
            case '1':
                mouse_ctrl.position = (CARD_1_X, Y_VAL)
            case '2':
                mouse_ctrl.position = (CARD_2_X, Y_VAL)
            case '3':
                mouse_ctrl.position = (CARD_3_X, Y_VAL)
            case '4':
                mouse_ctrl.position = (CARD_4_X, Y_VAL)
            case _:
                print('Key {0} pressed'.format(key))
                return
        
        # Click card and move back
        mouse_ctrl.click(mouse.Button.left)
        mouse_ctrl.position = original_pos

    except Exception as e:
        if key == keyboard.Key.esc:
            print('Exiting program')
        else:
            print(e)

def main():
    while True:
        # start keyboard listener (blocking) and link on_press fn
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()


if __name__ == '__main__':
    main()