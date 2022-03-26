
# Players can choose the name of the protagonist
$ protag = renpy.input("What is your name?")
$ protag = user.strip()

# Three different dates and protagonist
define p = Character("[protag]")
define d = Character("Deredere")
define t = Character("Tsundere")
define k = Character("Kuudere")
define tinder = Character("Tinder")


# The game starts here.

label start:

    # play music "musicfile.mp3"
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    scene bg room # replace with cafe, etc.

    # Insert a background of a phone
    #Insert some kind of ringtone here

    "You have a new message from urSweetLittleLamb"

    d "Hiii~~ You're soooo cute! <3"

    d "Hehe, I've always dreamed of meeting someone like you!!"

    d "I don't think I've ever met anyone who's shared my passion for exploring different milk alternatives! >///<"

    p "{i} I did post something about plant milk on my insta, but that was a year ago... weird {/i}"

    d "Ah wait, I thought you were a huge fan like me! Lol silly [Date 1] ^^;"

    d "Anyways,,,you're sooo pretty!! Or handsome!! Or cute!!! I'd love to meet up with you sometime,,,"

    d "Ok ok!! How's [Cafe name] at three? They had their grand opening last weekend!!"

    d "Oh I just {i} got {/i} to try the peach pies everyone's talking about! I heard they were to DIE for :O"

    d "The second I saw that place, oh I could just {i} see {/i} us falling in love there!!"

    "..."

    "..."

    d "I'm sorry! That was a little too soon, wasn't it?"
    
    d "You're creeped out now, aren't you? I'm so so sorry. I really screwed up didn't I?"

    d "[Date 1], you fool... T^T"

    d "Alright, I'll see you there! 3:00 sharp!! Mwah!! -3-"

    # Date 1 at the cafe
    ""
    menu:
        "Show up at 2:30 pm":
            call earlybird
        "Show up at 2:50 pm":
            call onTime
        "Show up at 4:20 pm":
            call youDick
    
    label earlybird:
        p "{i} Oh, [Date 1]'s already here? {/i}"
        d "[p], you're early!"
        p "Haha, you're too kind! To think you took an extra thirty minutes of your precious time to meet {i} me? {/i} I really don't deserve you..."
        p "Sorry sorry, it's just been so long since someone's cared so much about me..."
        p "We really are meant to be together, aren't we?"
        "[Date 1] wipes away their tears."
        return
    
    label onTime:


    label youDick:
        "[Partner 1] is sitting at a booth, fidgeting with an empty coffee cup clasped between their hands and looking expectantly out the window."

        d "Oh! [p] You're finally here ... No no no you don't have to explain yourself."
        d "It's ok, I understand you have more important things to take care of first."
        p 
        d "No worries. I see that look in your eyes. I know you'll love me not matter what."
        d "N-NO! I-I meant, uh, {i} I'll {/i} love you no matter what."
        d "Wait that's weird too. I-I'm so sorry! I'm just messing things up aren't I? Haha..."
        return
    
    d "Oh! I almost forgot! I brought "


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
