let cislo = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    cislo += 0 - 1
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    cislo += 1
})
basic.forever(function on_forever() {
    basic.showNumber(cislo)
})
