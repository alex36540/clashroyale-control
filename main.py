from pynput import keyboard, mouse

# Constants

# default values for mouse positions
card_1_pos = (853, 920)
card_2_pos = (958, 920)
card_3_pos = (1066, 920)
card_4_pos = (1173, 920)

click_count = 0

mouse_ctrl = mouse.Controller()

def on_press(key):
    global card_1_pos, card_2_pos, card_3_pos, card_4_pos

    # Quit case
    if key == keyboard.Key.esc:
        raise Exception("Program exited by pressing escape")
    
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
                mouse_ctrl.position = card_1_pos
            case '2':
                mouse_ctrl.position = card_2_pos
            case '3':
                mouse_ctrl.position = card_3_pos
            case '4':
                mouse_ctrl.position = card_4_pos
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
        elif key == keyboard.Key.f9:
            # CALIBRATION
            num_calibration()
        else:
            print(e)

### Calibrate number keys to match with the center of all cards
def num_calibration():
    global card_1_pos, card_2_pos, card_3_pos, card_4_pos

    print("Calibration mode")
    with mouse.Listener(on_click=calibration_on_click) as listener:
        listener.join()

def calibration_on_click(x, y, button, pressed):
    global click_count

    print()
    # on release
    if not pressed:
        match button.name:
            case 'left':
                print(click_count)
                click_count += 1
            case 'right':
                click_count = 0
                return False # This stops the mouse event listener


def main():
    while True:
        # start keyboard listener (blocking) and link on_press fn
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()


if __name__ == '__main__':
    main()