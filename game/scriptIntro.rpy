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
define g = Character("Galaxy")

label start:

    $ mc = renpy.input("What is your name?")
    $ mc = user.strip()

    if not user:
        $ user = "Olive"

    # Night before date 1
    # Insert a background of a phone
    #Insert some kind of ringtone here

    "*beep beep*... *beep beep*..."

    m "{i} Huh? Weird. Wasn't expecting notifs at this time. {/i}"

    g "You have a new message from urSweetLittlePeach!"

    d "Hiii~~ I think you're soooo cute! <3"

    d "How are youuuuu? :>"

    m "{i} O-oh... I wasn't epxecting a match so soon. {/i}"

    menu:
        "I'm doing good! How about you?":
            d "Yay!! That's good!! :D"

            d "I've been doing great since I started talking to you :3"

        "Eh, alright I guess":
            d "Awwww </3"

            d "At least it's not terrible!!"

            d "Here's hoping I can cheer you up!! :3"
        
        "Huh? What's up with you?":
            d "Oh I'm sorry, I'm coming on you too strong right?"

            d "I promise I'll tone it down! Pinky promise!"

    d "Hehe, I've always dreamed of meeting someone like you!!"
    
    d "I don't think I've ever met anyone who's shared my passion for exploring different milk alternatives! >///<"

    m "{i} I did post something about plant milk on my warp, but that was a year ago… weird. {/i}"

    menu:
        "I do liek the occasional glass of oat milk, but I wouldn't call it a passion lmao":
            d "Ah wait, I thought you were a huge fan like me! Lol silly Celeste ^^;"
        
        "Wait, when did I put that in my bio?":
            d "Oh uhhhh"

            d "I must have misread something then! Oopsies! Hehe"

            m "Lmao it's ok, I like milk alternatives"

        "Huh? Where'd you get that idea from you creep?":
            d "I'm sorry!! I'm sorry!!"
            d "I just thought you were a huge fan like me,,,"
    
    d "Anyways,,,you're sooo pretty!! Or handsome!! Or cute!! I'd love to meet up with you sometime,,,"

    m "I'm free tomorrow"

    m "{i} Why not? It's been a while since I've been on a date. And from the pictures on their profile they do seem cute… {/i}"

    d "Ok ok!! How's Cosmic Cafe at three? They had their grand opening last weekend!!"

    d "Oh I just {i} got {/i} to try the peach pies everyone's talking about! I heard they were to DIE for :O"

    m "{i} Hmmm, death by peach pie… I could get down with that. {/i}"

    d "The second I saw that place, oh I could just see us falling in love there!!"

    "..."

    "..."

    d "I'm sorry! That was a little too soon, wasn't it?"

    d "You're creeped out now, aren't you? I'm so so sorry." 
    
    d "I really screwed up didn't I? Celeste, you fool… T^T"

    menu:
        "No worries! I love peach pie!":
            d "Really??! Omg we already have so much in common hehehe"

            m "{i} Never tried it though… {/i}"
        
        "It's fineeee":
            d "Are you sureeee?"

            d "Ok ok! If you say so"

        "...":
            d "Hey are you still there? I must have scared you off, didn't I?"

    d "Alright, I'll see you there! Remember: 3:00 sharp!! Mwah!! -3-"

    m "{i} Wow, that went a lot better than I thought. They do seem a bit intense… but kinda in an endearing way? I guess we'll have to see during the date. {/i}"

    m "{i} Oh shoot, do I even have date clothes? Ugh I can't show up looking like a sack of lumpy turnips… {/i}"

    jump date1