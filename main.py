cislo = 0

def on_button_pressed_a():
    global cislo
    cislo += 0 - 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global cislo
    cislo += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.show_number(cislo)
basic.forever(on_forever)
