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

    def end(
        completed_fails=completed_fails,
        completed_endings=completed_endings,
        fails=fails,
        endings=endings,
    ):
        game(completed_fails, completed_endings, fails, endings)
        return

    def get_input(accept_string=False, clear=True, *options, allow_commands = True):
        """Get's the users input and checks if its a command or not

        Args:
            accept_string (bool, optional): Only used once, but allows string inputs instead of the normal int. Defaults to False.
            clear (bool, optional): Clear screen.
            options (str, optional): Options to choose from.

        Returns:
            int or string: Allows the input value to be used outside the function
        """
        input_invalid = True
        while input_invalid:
            count = 0
            for i in options:
                # List out options for user
                count += 1
                print(f"{count}.", i)
            input_value = input("> ").lower()
            if clear:
                os.system("cls")
            # Only check for commands if it doesn't accept strings
            if not accept_string:
                try:
                    input_value = int(input_value)
                    if 1 > input_value or input_value > count:
                        print("Invalid option")
                    else:
                        input_invalid = False
                except:
                    if allow_commands:
                        command_check(input_value)
                    else:
                        print("Please type the number of the option you want to pick")
            else:
                input_invalid = False
            clear = False
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
                print(
                    f"You have found {completed_fails}/{TOTAL_FAILS} fails. Nice going"
                )
                if completed_fails == TOTAL_FAILS:
                    print("Congrats! You really do suck")
            case "endings" | "ends":
                print(
                    f"You have found {completed_endings}/{TOTAL_ENDINGS} endings. Nice going!"
                )
                if completed_endings == TOTAL_ENDINGS:
                    print("Now that you did that, maybe find all the fails?")
            case "exit":
                print("All progress will be deleted, are you sure?")
                confirmation = get_input(False, True, "Yes!", "WAIT, No!", allow_commands=False)
                if confirmation == 1:
                    print("Okay, bye!")
                    exit()
            case "help" | "?":
                print(
                    """reset: Reset the game from the start
fails: Tells you how many fails you've completed and how many there are
endings/ends: Tells you how many endings there are and how many you've done
exit: Leave this program (It will NOT save)
help/?: Print this message
If you're confused about the options, you type the number of what you want to do
"""
                )
            case _:
                print("That's not a valid command or choice")

    def pause():
        input("Press enter to continue...")

    def fail(
        message,
        completed_fails=completed_fails,
        completed_endings=completed_endings,
        fails=fails,
        endings=endings,
    ):
        pause()
        os.system("cls")
        print(f"{FAIL_BANNER}\n{message}")
        # Check if the fail has been done already
        if fails.count(message) == 0:
            print("**NEW FAIL**")
            completed_fails += 1
            fails += message
        print("You have completed", completed_fails, "fails out of", TOTAL_FAILS)
        input("Press enter to restart...")
        end(completed_fails, completed_endings, fails, endings)

    def ending(
        message,
        completed_fails=completed_fails,
        completed_endings=completed_endings,
        fails=fails,
        endings=endings,
    ):
        pause()
        os.system("cls")
        print(f"{END_BANNER}\n{message}")
        # Check if the fail has been done already
        if endings.count(message) == 0:
            print("**NEW ENDING**")
            completed_endings += 1
            endings += message
        print("You have completed", completed_endings, "endings out of", TOTAL_ENDINGS)
        input("Press enter to restart...")
        end(completed_fails, completed_endings, fails, endings)

    print("You walk into your favorite donut shop, what topping do you get?")
    input_value = get_input(True)
    if input_value == "sprinkles":
        print("...wow you're basic")
    print(
        "If you want a list of commands, use 'help' or '?' in any section other then the first one. They aren't required for this\n"
    )
    print(
        """Actually, as you're walking towards it, you see a sign for a museum showing of "The Pharaoh's bracelet" made of gold and jewels. Know what? Screw that donut, let's go rob that crap

You wait until the dead of night and approach the back wall of the museum
You use the..."""
    )
    input_value = get_input(False, True, "Jetpack", "Teleporter", "Sticky Bomb")
    match input_value:
        case 1:
            pass
        case 2:
            print(
                """Beep. Boop. Bop. You press some buttons, but you don't really know how to work this thing.
Well, after you're sure enough you made it into the museum, you press the big middle button. Turns out you teleported out of bounds and softlock yourself. Nice going"""
            )
            fail("Speedrun Strats")
        case 3:
            print(
                "You throw the sticky bomb. Off-topic, but have you ever wondered how a bomb covered in a completely sticky substance can be thrown?"
            )
            pause()
            print("It can't. You desperately try to shake it off, but it's too sticky.")
            fail("Shake it off, Shake it off, shake, shake, sh- no?")
    print("You don't really know how to use this thing, but how hard can it be?")
    pause()
    print(
        """You fly up successfully!
Then backwards... Then left, right, down, up, down again, forward, and through the wall. Somehow the head trauma didn't kill you. Yet. You're in the broom closet."""
    )
    input_value = get_input(
        False, True, "Book it to the exhibit", "Vent", "Use the mop bucket"
    )
    match input_value:
        case 1:
            print(
                "You BUST down the door of the broom closet and run as fast as you can through all the doors, following the signs to the bracelet. You run like you never had before. Out of breath, you bust the glass open and grab the bracelet! Congratulations, you got it!"
            )
            pause()
            os.system("cls")
            print(f"{END_BANNER}\nMcqueen would cry")
            pause()
            os.system("cls")
            print(
                "You suddenly feel cold metal on the back of your head. The museum is guarded"
            )
            fail("YAYYY! WOO! YOU DID IT! YIPEEEE!")
        case 2:
            print(
                "You jump up into the vent above your head and start crawling through the ac system. You see an exhibit through another vent so you drop down"
            )
            pause()
            print(
                "It's not the one with the bracelet! You look over and see a sign pointing to the bracelet exhibit, but there's a locked door in the way. You're in some sort of artifact room"
            )
            input_value = get_input(
                False,
                True,
                "Liquidifier",
                "Backwards long jump",
                "Mummies Hair",
                "Godly Hammer",
                "Telekinesis",
            )
            match input_value:
                case 1:
                    print(
                        "You use the Liquidifier and slide the slider all the way to the right, successfully turning into water! The guards in the next room try to shoot at you but it does nothing."
                    )
                    pause()
                    print("...wait, how do you work the slider?")
                    fail("You just HAD to go all in!")
                case 2:
                    print(
                        "After a good kick backwards and a few wahoos, you clip through the door! But your velocity is too great and you proceed to hit your skull on even more walls, killing you."
                    )
                    fail("Did you leave the plot armor with the jetpack?")
                case 3:
                    pass
                case 4:
                    print(
                        """You read the label of the exhibit. It read something like "tor hammer".
You proceed to lift it with all your might, it starts to move! You finally get it off the stand over your feet and- *comedic slip sound*"""
                    )
                    pause()
                    print("aaaaAAAAAAAAAAAAAAAHHH!!")
                    fail(
                        "Only the worthy shall lift the hammer... and you're stealing a bracelet"
                    )
                case 5:
                    print(
                        "You point your hands to your head and hunch over to try to use your telekinesis"
                    )
                    pause()
                    print("A guard walks by and sees you")
                    fail("You look like a moron")
            print(
                "This doesn't exactly seem too helpful. You try putting it in the lock, hoping it will somehow do something."
            )
            pause()
            print(
                "Somehow, click! The lock falls off the door. That's... not how locks work but oh well. You walk into the exhibit with the bracelet, there are 2 guards talking. They haven't noticed you yet"
            )
            input_value = get_input(
                False, True, "KILLSTREAK", "Unplug Router", "Boombox"
            )
            match input_value:
                case 1:
                    print(
                        "You forgot what killstreak you equipped, but they must be good. Is it a predator missile? A drone strike? A nuke?"
                    )
                    pause()
                    os.system("cls")
                    print('"Friendly UAV active"')
                    pause()
                    print(
                        "The guards, seeing the message, turn around to see you crouching on the floor like a gremlin"
                    )
                    fail("Knowledge is power!")
                case 2:
                    print(
                        "After unplugging the router, you walk right through the guards getting to the case. You plug the router back in and wait the 30 seconds required for the internet to kick back on."
                    )
                    pause()
                    os.system("cls")
                    print("Kicked: Failed to receive packet from server")
                    fail("Error: Unable to receive variable snarky_message")
                case 3:
                    pass
            print("You put on some old school hip-hop next to the cardboard boxes.")
            pause()
            print(
                """The guards are so "annoyed" that they go to "investigate" that while "breaking some boxes up".
Despite how much you want to see the obvious dance battle happening, you came here for the bracelet. There's a thick glass casing between you and the bracelet"""
            )
            input_value = get_input(
                False, True, "Smash glass using hammer", "Use laser"
            )
            match input_value:
                case 1:
                    print(
                        'Wha-What? WHY WOULD YOU DO THAT! Glass is loud you idiot, who told you "hammer" was the right option? I don\'t even think I need to tell you what happened.'
                    )
                    fail("What logic lead you to that conclusion?")
                case 2:
                    pass
            print(
                "The laser cuts cleanly through the glass. After you remove the glass carefully, you grab the bracelet and retrace your steps. With no problems, you leave the way you came"
            )
            ending("Venting Ninja")
        case 3:
            print(
                "You get in the surprisingly dry mop bucket, equip the mop like a jousting lance, and put a bucket on your head for protection. You open the door and ride into battle"
            )
            pause()
            print("You are confronted by two guards in a doorway")
            input_value = get_input(False, True, "Green Shell", "Drift", "Nitro Boost")
            match input_value:
                case 1:
                    print(
                        "You throw the green shell with all your might and hit a guard! Good job! Wait, 1... 2- oh no there were 2 guards. The other one opens fire"
                    )
                    fail("You should've had the bullet bill")
                case 2:
                    print(
                        "You do a sick drift, going right into a guard, knocking them over! Unfortunately, you didn't see the wall behind them before you crashed into it."
                    )
                    fail("I'm surprised that has traction")
                case 3:
                    pass
            print(
                "Just like real life, you decide to avoid your problems. Turning on the boosters, you go right past the guards, who proceed to miss all their shots. You're right next to the bracelet, what's your next move?"
            )
            input_value = get_input(
                False,
                True,
                "Think",
                "Throw the glass",
                "Smash the glass using fist",
                "Smash the glass hammer",
            )
            match input_value:
                case 1:
                    print("While thinking, you get shot")
                    fail("This says a lot about society (im literally the joker)")
                case 2:
                    pass
                case 3:
                    print(
                        "You hype yourself up to punch the glass. Breathe in, Breathe out, throw some shadow punches, get ready..."
                    )
                    pause()
                    print("While being your own hype-man, you get shot")
                    fail("Don't worry, you weren't getting through that glass anyways")
                case 4:
                    print(
                        "You smash the glass hammer nearby. What did this accomplish?"
                    )
                    fail("Can you even read?")
            print(
                "It's heavy, but it was pretty easy to throw off. You grab the bracelet and put it on. Now you might wanna get out before those guards catch up"
            )
            input_value = get_input(
                False,
                True,
                "Cheat",
                "Use the mop bucket",
                "Break Dino Egg"
            )
            match input_value:
                case 1:
                    print(
                        "You grab the cheat gun off a table and type \">noclip >fly\" into the console, and get out of there. But cheats aren't allowed on this server, so I'm banning you"
                    )
                    pause()
                    os.system("cls")
                    print("Banned: Cheats/Exploits")
                    fail("Cheaters never prosper")
                case 2:
                    pass
                case 3:
                    print(
                        "You break the dino egg with your bare hands. It's a few million years old though, any dino that would be in there is long dead. It stinks up the whole room causing all the guards to pass out. You aren't immune to the stench"
                    )
                    fail("ALRIGHT! I'm back with the drin- what the heck happened")
            print(
                """Your only real option, let's be honest. You charge into the wall, blowing it down using the mop as you ride out at high speeds.
hey didn't even have the time to sound the alarm before you were gone. They try to fire a few rounds, but they bounce off the bucket! (Mostly because the bullets were slow but lets ignore that)"""
            )
            ending("MOP MASTER")


if not game():
    print("The game has a loose end somewhere, so you have been booted. Sorry")
