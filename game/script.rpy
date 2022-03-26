# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("temp")

define d = Character("Deredere")
define t = Character("Tsundere")
define k = Character("Kuudere")
define tinder = Character("Tinder")

define mc = Character("[name]")

# The game starts here.

label start:

    # play music "musicfile.mp3"
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room # replace with cafe, etc.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    python:
        name = renpy.input("What is your name?", length=32)
        name = name.strip()

        if not name:
            name = "MC"

    label notifs:
        tinder "*beep beep* … *beep beep* … "
        menu:
            "Check your phone?"
            "Check notifications":
                jump check
            "Ignore phone":
                jump notifs

    label check:
        t "Helloooooo!!!! hwo r u :D"
        # menu:
        #     "I think so! Maybe?":
        #     {..code to run here}
        #     "Yeah... No. You're super annoying.":
        #     {..code to run here}
        #     "Yes-- underneath your... attitude... you seem to truly care about me." # if cond:
        #     {..code to run here}

    # This ends the game.

    return
