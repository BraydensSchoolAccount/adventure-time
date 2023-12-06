# Adventure
# Brayden Towner
# 12/06/2023
import os

TOTAL_FAILS = 17
TOTAL_ENDINGS = 2
completed_fails = 0
completed_endings = 0

os.system("cls")

def game():
    input_value = ""
    fails = ""
    endings = ""
    def end():
        game()
        return
    def get_input(accept_string = False):
        global input_value
        input_value = input("> ").lower()
        if not accept_string:
            try:
                input_value=int(input_value)
            except:
                command_check("")
    def command_check(command):
        match command:
            case "reset":
                end()
            case "fails":
                print(f"You have found {completed_fails}/{TOTAL_FAILS} fails. Nice going")
                if completed_fails == TOTAL_FAILS:
                    print("Congrats! You really do suck")
            case "endings", "ends":
                print(f"You have found {completed_endings}/{TOTAL_ENDINGS} endings. Nice going!")
                if completed_endings == TOTAL_ENDINGS:
                    print("Now that you did that, maybe find all the fails?")
            case "help", "?":
                print("""reset: Reset the game from the start
fails: Tells you how many fails you've completed and how many there are
endings/ends: Tells you how many endings there are and how many you've done
help/?: Print this message
""")
            case _:
                print("That's not a valid command or choice")
    print("""You walk into your favorite donut shop, what topping do you get?
    """)
    get_input(True)
    print(input_value)
    if input_value == "sprinkles":
        print("...wow you're basic")
    print("""Actually, as you're walking towards it, you see a sign for a museum showing of "The Pharaoh's bracelet" made of gold and jewels. Know what? Screw that donut, let's go rob that crap

You wait until the dead of night and approach the back wall of the museum
You use the...""")
    get_input()

print("If you want a list of commands, use 'help' or '?'. They aren't required for this")
game()