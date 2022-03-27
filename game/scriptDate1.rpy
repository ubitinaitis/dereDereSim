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

        show CelesteBashful at center with dissolve

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

        show CelesteBashful at center with dissolve

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

        "You spent the entire morning and early afternoon fooling around on your computer in the hopes that it would keep your mind off the impending date."

        "Turns out that plan worked a little too well. By the time you dragged yourself out the rabbit hole of social media, it was already 4:10."

        m "{i} Oh no they're going to be so mad at me. {/i}"

        m "{i} Ok ok breatheeee. People are late to things all the time, and it's only been an hour and twenty minutes… Ugh who am I kidding. {/i}"
        
        scene CafeNoon with fade

        "Despite the rest of the shopping district being cricket silent, Cosmic Cafe was still bustling with people, making it almost impossible to find even an inch of space to sit down."

        "Wading through the crowd felt like trying to survive against a raging sea of molasse. At least the space looked charming with its gleaming dark wood counters and abundance of plants."

        "You breathed in the rich smell of coffee and buttery pastries to motivate yourself to push forward."

        show CelesteBashful at center with dissolve

        "Celeste is sitting at a booth, fidgeting with the empty coffee cup clasped between their hands and looking expectantly out the window."

        "You waved awkwardly."

        m "Hey~!"

        m "{i} Maybe if I play it up a little it'll make her feel better… I hope. {/i}"

        show CelesteTeary at center

        d "Oh! [p]! You're finally here."

        d "No no no you don't have to explain yourself. It's ok, I understand you have more important things to take care of first."

        m "I'm sorry. I completely lost track of time."

        show CelesteSmile at center

        d "No worries! I see that look in your eyes. I know you'll love me no matter what."

        m "What are you talking about? I've never said that."

        show CelesteBashful at center

        d "N-NO! I-I meant, uh, {i} I'll {/i} love you no matter what."

        d "Wait, that's weird too. I-I'm so sorry! I'm just messing things up aren't I? Haha…"

        return
        
    show CelesteBashful at center
    
    d "Oh! I almost forgot! I brought you flowers."

    "Celeste shoved a small, handpicked bouquet into your arms. It was full of your favorite blossoms - field flowers, clover, baby's breath…"

    m "{i} It's lovely {/i}"

    m "Did you make this yourself?"

    "They nodded."

    d "I passed by this beautiful garden on the way here!" 

    show CelesteBashful at center

    d "I thought you'd like it, you know, by pure coincidence."

    m "I love it! Thank you so much."

    show CelesteSmile at center

    d "Of course, love. Though none of the flowers here are as fragrant as the ones back at home."

    m "At home?"

    d "Yeah! I sure do miss it. I haven't been back in ages cause of how busy I've been."

    d "The sky, oh it's so blue there. And the stars! They're like, right up in your face! Like you could touch them! You'd have to see for yourself if you want to believe it."

    m "Touch the stars? For real?"

    show CelesteBashful at center

    d "Yes! I mean, uh, not literally of course."

    "Celeste laughs awkwardly, but their eyes are sparkling."

    m "{i} Like you could touch the stars, huh? {/i}"

    "An awkward silence settled between the two of you, and you realized with a panic that you have no idea how to continue a date conversation."

    m "{i} Man I've gotten really rusty over the years. {/i}"

    "As discreetly as you could, you searched up a list of first date icebreakers, your fingers fumbling with the tiny, clunky keyboard."

    "At one point you nearly dropped the phone, thankfully catching it with the grace of an elephant trying to do ballet."

    m "{i} What is with these questions? {/i}"

    "Which one of these should I ask?"

    menu:
        "What is your favorite constellation?":
            call constellation
        
        "What is your favorite color?":
            call colors 
        
        "What kind of birb would you be?":
            call birb

    label constellation:
        show CelesteSmile at center

        d "I thought you'd never ask! Orion of course."

        m "O-oh. I didn't think you would actually have an answer for that. Not many people I know think too deeply about the stars in the sky."

        d "Hehe I find them very fascinating, especially those stories you all have created from them."

        d "They are far different from the stories my mom used to tell me as a kid, but they are still fun to listen to anyway!"

        menu:
            "What kind of stories did your mom tell you?":
                d "Oh where do I start? The one about Orion was always my favorite of course."
                
                "A neverending flood of words began to flow from their mouth, sweeping you along with them."
                
                "You didn't quite understand everything they said, something about giant crab-like creatures roaming the empty space and mouths that served as portals, but you nodded your head along with the words, your eyes staring rapt at Celeste."
                
                show CelesteBashful at center

                d "Oh I'm so sorry! I talked too much didn't I? I didn't mean to, I promise!"

                m "No no it's ok! It was all really interesting! Trust me."

                m "{i} She's so cute when she gets excited like this {/i}"

                d "Haha wow… I didn't think I could fall for you even more but… "

            "Huh that's cool.":
                show CelesteBashful at center

                d "Hehe you think so?"

                show CelesteSmile at center

                d "If you have any questions about constellations, planets, anything space related just ask me!"

                d "I'll probably talk your ear off though so, uh, sorry beforehand."

                m "Hmmm noted."

                m "{i} I don't think I'm in desperate need of space knowledge, but you never know. {/i}"
            
            "Yeah yeah, who cares. They're just hot fireballs in the sky. They can't be that interesting.":
                show CelesteTeary at center

                d "O-oh, you think so? I'm… I'm sorry. I should've considered your feelings before talking so much about it."

                d "I'll stop then."

                m "{i} About time. {/i}"

        return

    label colors:
        m "{i} Wow that's a lame question. What is this? Kindergarten? {/i}" 

        m "{i} I don't even know why I asked it. I must really be running out of ideas. {/i}"
        
        show CelesteSmile at center

        d "White!" 

        show CelesteBashful at center

        d "Oh wait, uh, I mean pink! Yeah, yeah…"

        show CelesteSmile at center

        "They gestured to their dress."

        d "In fact, most of my clothes, including this dress, are pink. I know I should get some variety in my closet, but I just can't help it. Pink just looks too pretty!"

        menu:
            "I think you look pretty in pink!":
                show CelesteBashful at center

                d "Really?!"

                "They looked like they were about to fall off their chair before burying their hands in their face."

                d "Do you really think so, love?"

                m "Of course! Why would I say it then?"

                d "Haha… you're the best [p]."
            
            "Ehh there's a lot of better colors out there to like in my opinion.":
                show CelesteTeary at center

                d "Y-yeah… yeah you're right…" 
                
                d "Haha it's kinda silly of me to like pink this much isn't it?"

                "They turned their eyes down to the floor, suddenly more focused on the whorls of the wood than your face."
        return

    label birb:
        m "{i} Huh? Why would you call a bird a birb? {/i}"

        "Celeste tilted their head to the side, trying to seem deep in thought, but it's clear from their eyes that they're confused."

        m "Uhhh a bird, yeah, that's what I meant."

        "Their eyes lit up."

        show CelesteSmile at center

        d "Oh! Ok! I know what that is! A weird way of saying bird though, haha."

        m "Yeah uh sorry about."

        m "{i} Stupid website… making me look like a fool in front of my date. {/i}"

        d "Hmmm I think I would be a hummingbird! They seem so cheerful and energetic just like me! And they're also so pretty!"

        m "Just like you!"

        show CelesteBashful at center

        d "Ahh stop it! You're embarrassing me!"

        m "{i} It's kinda fun making them this flustered. {/i}"

        return

    show CelesteSmile at center

    d "Oh oh oh! I must have forgotten with all this talking, but will you try the peach pie with me?"

    m "Yes!"

    d "And pick a drink, sweetheart. It's on me!"

    menu:
        "I'll take the Signature Cosmic Frappe!"

        "An iced coffee."

        "Just water, please."

    "You spent the rest of the date chatting with Celeste and enjoying your juicy and flaky peach pies."

    "You agreed with the critics: you would totally die just have an another bite of that pie."

    "Before you know it, it's far past dinnertime."