from pynput import keyboard, mouse

# Constants

# default values for mouse positions
card_1_x = 853
card_2_x = 958
card_3_x = 1066
card_4_x = 1173

y_val = 920

mouse_ctrl = mouse.Controller()

def on_press(key):
    global card_1_x, card_2_x, card_3_x, card_4_x, y_val

    # Quit case
    if key == keyboard.Key.esc:
        raise Exception(key)
    
    original_pos = mouse_ctrl.position

    # Check if y value is on the card, because if it is, it's possible that
    # the mouse hasn't moved yet from a previous input
    # if (Y_VAL - 50) <= original_pos[1] <= (Y_VAL + 50):
    #     return

    try:
        key_char = key.char

        # Move mouse to correct card
        match key_char:
            case '1':
                mouse_ctrl.position = (card_1_x, y_val)
            case '2':
                mouse_ctrl.position = (card_2_x, y_val)
            case '3':
                mouse_ctrl.position = (card_3_x, y_val)
            case '4':
                mouse_ctrl.position = (card_4_x, y_val)
            case '<67>':
                 # Pressing Ctrl+Alt+C
                 num_calibration()
            case _:
                print('Key {0} pressed'.format(key))
                return
        
        print("click at %d, %d", mouse_ctrl.position[0], mouse_ctrl.position[1])

        # Click card and move back (check if on card when clicking)
        #if (y_val - 50) <= mouse_ctrl.position[1] <= (y_val + 50):
        
        mouse_ctrl.click(mouse.Button.left)

        # Putting this twice seems to fix the issue of staying at the bottom
        mouse_ctrl.position = original_pos
        mouse_ctrl.position = original_pos

    except Exception as e:
        if key == keyboard.Key.esc:
            print('Exiting program')
        else:
            print(e)

### Calibrate number keys to match with the center of all cards
def num_calibration():
    global card_1_x, card_2_x, card_3_x, card_4_x, y_val
    print("Calibration mode")
    input("Press enter with mouse centered on card 1")
    pos = mouse_ctrl.position
    card_1_x = pos[0]
    y_val = pos[1]

    input("Press enter with mouse centered on card 2")
    pos = mouse_ctrl.position
    card_2_x = pos[0]

    input("Press enter with mouse centered on card 3")
    pos = mouse_ctrl.position
    card_3_x = pos[0]

    input("Press enter with mouse centered on card 4")
    pos = mouse_ctrl.position
    card_4_x = pos[0]


def main():
    while True:
        # start keyboard listener (blocking) and link on_press fn
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()


if __name__ == '__main__':
    main()