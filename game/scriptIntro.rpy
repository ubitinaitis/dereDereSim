# Character art
image CelesteBashful: 
    "./assets/Partner1Bashful.png"

image CelesteSmile:
    "./assets/Partner1Smile.png"

image CelesteTeary:
    "./assets/Partner1Teary.png"

image OrionSmile:
    "./assets/Partner2Smile.png"

image OrionSmileGlasses:
    "./assets/Partner2SmileGlasses.png"

image OrionStoic:
    "./assets/Partner2Stoic.png"

image OrionStoicGlasses:
    "./assets/Partner2StoicGlasses.png"

image SoleilAngry:
    "./assets/Partner3Angy.png"

image SoleilShy:
    "./assets/Partner3Shy.png"

image SoleilSmile:
    "./assets/Partner3Smile.png"

# Background art
image Bridge:
    "./assets/Bridge.png"

image CafeEvening:
    "./assets/CafeEve.png"

image CafeNoon:
    "./assets/CafeNoon.png"

image Road:
    "./assets/RoadBlur.png"

image StreetEvening:
    "./assets/StreetEve.png"

image StreetNight:
    "./assets/StreetNight.png"

# Three different dates and main character
define m - Character("[user]")
define d = Character("Celeste")
define k = Character("Orion")
define t = Character("Soleil")

label start:

    $ mc = renpy.input("What is your name?")
    $ mc = user.strip()

    if not user:
        $ user = 

    # Night before date 1
    # Insert a background of a phone
    #Insert some kind of ringtone here

    "You have a new message from urSweetLittleLamb"

    d "Hiii~~ I think you're soooo cute! <3"

    p "{i} Huh. Wasn't expecting a "

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

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
