# Adventure
# Brayden Towner
# 12/06/2023
import os

TOTAL_FAILS = 17
TOTAL_ENDINGS = 2
FAIL_BANNER = """
███████╗ █████╗ ██╗██╗
██╔════╝██╔══██╗██║██║
█████╗  ███████║██║██║
██╔══╝  ██╔══██║██║██║
██║     ██║  ██║██║███████╗
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝
"""
END_BANNER = """
███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗
██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝
█████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗
██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║
███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝
╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝
"""
os.system("cls")

def game(*global_vars):
    if not bool(global_vars):
        completed_fails = 0
        completed_endings = 0
        fails = ""
        endings = ""
    else:
        completed_fails, completed_endings, fails, endings = global_vars
    def end(completed_fails=completed_fails, completed_endings=completed_endings, fails=fails, endings=endings):
        print(completed_fails)
        game(completed_fails, completed_endings, fails, endings)
        return
    def get_input(accept_string = False, clear = True,*options):
        """Get's the users input and checks if its a command or not

        Args:
            accept_string (bool, optional): Only used once, but allows string inputs instead of the normal int. Defaults to False.
            clear (bool, optional): Clear screen.
            options (str, optional): Options to choose from.

        Returns:
            int or string: Allows the input value to be used outside the function
        """
        count = 0
        for i in options:
            # List out options for user
            count+=1
            print(f"{count}.",i)
        input_value = input("> ").lower()
        if clear:
            os.system("cls")
        # Only check for commands if it doesn't accept strings
        if not accept_string:
            try:
                input_value=int(input_value)
                if 1 > input_value > count:
                    print("Invalid option")
                    return
            except:
                command_check(input_value)
        return input_value
    def command_check(command):
        """Checks if the input given is a command

        Args:
            command (str): The possible command given
        """
        match command:
            case "reset":
                end()
            case "fails":
                print(f"You have found {completed_fails}/{TOTAL_FAILS} fails. Nice going")
                if completed_fails == TOTAL_FAILS:
                    print("Congrats! You really do suck")
            case "endings" | "ends":
                print(f"You have found {completed_endings}/{TOTAL_ENDINGS} endings. Nice going!")
                if completed_endings == TOTAL_ENDINGS:
                    print("Now that you did that, maybe find all the fails?")
            case "help" | "?":
                print("""reset: Reset the game from the start
fails: Tells you how many fails you've completed and how many there are
endings/ends: Tells you how many endings there are and how many you've done
help/?: Print this message
If you're confused about the options, you type the number of what you want to do
""")
            case _:
                print("That's not a valid command or choice")
    def pause():
        input("Press enter to continue...")
    def fail(message, completed_fails=completed_fails, completed_endings=completed_endings, fails=fails, endings=endings):
        pause()
        os.system("cls")
        print(f"{FAIL_BANNER}\n{message}")
        # Check if the fail has been done already
        if fails.count(message) == 0:
            print("**NEW FAIL**")
            completed_fails += 1
            fails+=message
        input("Press enter to restart...")
        end(completed_fails, completed_endings, fails, endings)
    def ending(message, completed_fails=completed_fails, completed_endings=completed_endings, fails=fails, endings=endings):
        pause()
        os.system("cls")
        print(f"{FAIL_BANNER}\n{message}")
        # Check if the fail has been done already
        if fails.count(message) == 0:
            print("**NEW FAIL**")
            completed_fails += 1
            fails+=message
    print("You walk into your favorite donut shop, what topping do you get?")
    input_value = get_input(True)
    if input_value == "sprinkles":
        print("...wow you're basic")
    print("If you want a list of commands, use 'help' or '?' in any section other then the first one. They aren't required for this\n")
    print("""Actually, as you're walking towards it, you see a sign for a museum showing of "The Pharaoh's bracelet" made of gold and jewels. Know what? Screw that donut, let's go rob that crap

You wait until the dead of night and approach the back wall of the museum
You use the...""")
    input_value = get_input(False, True, "Jetpack","Teleporter", "Sticky Bomb")
    match input_value:
        case 1:
            pass
        case 2:
            print("""Beep. Boop. Bop. You press some buttons, but you don't really know how to work this thing.
Well, after you're sure enough you made it into the museum, you press the big middle button. Turns out you teleported out of bounds and softlock yourself. Nice going""")
            fail("Speedrun Strats")
        case 3:
            print("You throw the sticky bomb. Off-topic, but have you ever wondered how a bomb covered in a completely sticky substance can be thrown?")
            pause()
            print("It can't. You desperately try to shake it off, but it's too sticky.")
            fail("Shake it off, Shake it off, shake, shake, sh- no?")
    print("You don't really know how to use this thing, but how hard can it be?")
    pause()
    print("""You fly up successfully!
Then backwards... Then left, right, down, up, down again, forward, and through the wall. Somehow the head trauma didn't kill you. Yet. You're in the broom closet.""")
    input_value = get_input(False, True, "Book it to the exhibit","Vent", "Use the mop bucket")
    match input_value:
        case 1:
            print("""You BUST down the door of the broom closet and run as fast as you can through all the doors, following the signs to the bracelet. You run like you never had before. Out of breath, you bust the glass open and grab the bracelet! Congratulations, you got it!
Mcqueen would cry

You suddenly feel cold metal on the back of your head. The museum is guarded
Fail: YAYYY! WOO! YOU DID IT! YIPEEEE!""")
        case 2:
            print("""Beep. Boop. Bop. You press some buttons, but you don't really know how to work this thing.
Well, after you're sure enough you made it into the museum, you press the big middle button. Turns out you teleported out of bounds and softlock yourself. Nice going""")
            fail("Speedrun Strats")
        case 3:
            print("You throw the sticky bomb. Off-topic, but have you ever wondered how a bomb covered in a completely sticky substance can be thrown?")
            pause()
            print("It can't. You desperately try to shake it off, but it's too sticky.")
            fail("Shake it off, Shake it off, shake, shake, sh- no?")


game()