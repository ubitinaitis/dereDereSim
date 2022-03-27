label date1:
    "Today's the day!"

    menu:
        "Show up at 2:30 pm.":
            call earlyBird 
        "Show up at 2:59 pm.":
            call onTime
        "Show up at 4:20 pm.":
            call bruh
    
    label earlyBird:
        scene StreetEvening

        "You were all dressed and ready by the time the clock struck two, but you decided to give it thirty more minutes so as to not seem {i} too {/i} eager to impress."

        "The entire time, though, you were pacing back and forth across the length of your apartment, the tension rising in your chest with each minute gone by."

        m "{i} God I barely remember what even happened on the last date I went on. Is it normal to be this nervous? {/i}"

        scene CafeNoon with fade

        "Despite the rest of the shopping district being cricket silent, Cosmic Cafe was still bustling with people, making it almost impossible to find even an inch of space to sit down."

        "Wading through the crowd felt like trying to survive against a raging sea of molasse. At least the space looked charming with its gleaming dark wood counters and abundance of plants."

        "You breathed in the rich smell of coffee and buttery pastries to motivate yourself to push forward."

        show CelesteBashful at center

        m "{i} Oh, Celeste's already here?! {/i}"

        show CelesteSmile at center

        d "Oh [p], you're early!"

        m "Wait, but you're even earlier?"

        d "You're too kind… To think you took an extra thirty minutes of your precious time to meet someone like {i} me? {/i}"

        show CelesteTeary at center

        d "I don't deserve you…"

        m "H-hey, it's no big deal! Don't cry!"

        d "S-Sorry, it's been so long since someone's cared so much about me…"

        d "We really are meant to be together, aren't we?"

        "They wipe away their tears in relief."

        return
    
    label onTime:
        scene StreetEvening 

        "You made sure to leave the apartment early so you could get to the cafe with ten minutes left to spare. Just enough time to make yourself comfortable and perhaps order a fun drink."

        "Unfortunately you forgot that traffic was a thing that existed and barely arrived on time, feeling a little weary and disheveled."

        m "{i} Hey you'll be fine! This isn't like a job interview or anything. {/i}"

        m "{i} Then again, if you think about it hard enough, a first date and a job interview are pretty similar… {/i}"

        m "{i} No no no you're not going down this rabbit hole again. {/i}"

        scene CafeNoon with fade

        "Despite the rest of the shopping district being cricket silent, Cosmic Cafe was still bustling with people, making it almost impossible to find even an inch of space to sit down."

        "Wading through the crowd felt like trying to survive against a raging sea of molasse. At least the space looked charming with its gleaming dark wood counters and abundance of plants."

        "You breathed in the rich smell of coffee and buttery pastries to motivate yourself to push forward."

        show CelesteBashful at center

        "Celeste is already here. They even saved a seat for you!"

        show CelesteSmile at center

        d "Right on time, hehe! I already know so much about you, but I'm excited to learn more!"

        m "Wait, you do?"

        show CelesteBashful

        d "What? Oh, uh, this is our first meeting isn't it?"

        d "I just mean, ah, uhm… that it feels like we've known each other for ages! Yeah! That's right…"

        m "Uhhh y-yeah! Haha…"

        return

    label bruh:
        scene StreetEvening

        




