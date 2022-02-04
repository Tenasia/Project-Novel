label start:
    # if persistent.firstchapter_clear:
    #     jump prologue
    # $ persistent.unlocked_text = [] 

    
    
    stop music fadeout 1.0
    stop movie


    python:
        set_info_scene("00")
        set_info_location("01")
        

    # play music audio.maintheme
    # scene black
    # pause 3
    # scene ecg pattern nor a large:
    #     zoom 1.3
    #     yalign 0.5
    #     xalign 0.0
    #     subpixel True
    #     linear 150 xalign 1.0
    # show smoke at smoke_rl(100, 0.6)
    # with Dissolve(5)
    # pause 1
    # call discord_status ("Chapter 1", "2")

    play music audio.prologue

    scene bg war
    with fade
    Thought2 "..."
    Thought2 "Izanagis was looked upon as cold and relentless. He hailed from Germany but he is a Japanese in blood, after their lost war in 1945. They had been experimenting with genes and had countless times failed. They were trying to make a superhuman to get back at the western and eastern folks."   
    Thought2 "His ancestors, the Izanagis. Was part of the “Dunkelblau Runder Tisch” {size=-10}(Obsidian Round Table){/size} which was formed as a hub for high-profile members of the Waffen Schutzstaffel {size=-10}(ß){/size} organization formed before the outbreak of the second world war. He was by then a part of it."
    Thought2 "Seemingly before the war had been lost for the Nazis, they have decided to push everything on the Obsidian Round Table to form a saving grace for their country. To make a superhuman that can contest every piece of weaponry, that only hydrogen bomb can only disperse the said subject."
    nvl clear
    
    scene bg shady_lab
    with fade 
    nvl show 
    Thought2 "After some time had passed since the end of the second world war, the experiment had begun hidden away from any civilization. They hid it for long that not one would thought of a war brewing after what they just had gone through."
    Thought2 "He was the second test subject for their experiment. As they had ‘superior’ blood, they were the only fitting subjects for this goal. At first, since the war has ended, He thought that there was no need for more conflicts and the ‘revival’ experiment would either make him a monster, or a corpse. He had already contemplated with this, as sort of punishment of the world."
    Thought2 "But the experiment succeeded on him. The scientists were in awe, and he did not feel any different than he was before the experiment."
    nvl clear

    scene bg japan
    with fade
    nvl show 
    Thought2 "Years passed without conflict and he was allowed to go back to his country, Japan. There he settled with a girl that came from a family of heritage. As he made a family, his first child was a boy named Fuuji. Followed by a daughter after 4 years, Akane."
    Thought2 "Before even making his children be fond of him. Obsidian Round Table called for every subject of the 'revival' had succeeded with. Fuuji was only 9 years old, Akane being 5. They had to part with their father at such a young age with no clear explanation on even when will their father come back."
    nvl clear
    

    stop music fadeout 1.0
    scene bg black
    # with fade
    Thought "A decade had passed. While the financial situation was not a problem somehow. There has been no communication between him and his family."

label prologue:
    scene bg living_room
    $ add_seen_chapter("1-1")

   
    python:
        set_info_scene("01")
        set_info_location("02")
        set_info_date(2, "May", "wed")
        set_info_time("day")

    show img1 
    show img2 
    hide img1 
    hide img2
    $ renpy.music.play(audio.thin_purple, channel="music", fadeout=1.0, fadein = 2.0)

    # play music audio.thin_purple fadeout 2.0 fadein 1.0
    
    $ add_seen_words("1-1")
    $ add_seen_words("1-2")
    $ add_seen_words("1-3")
    # scene bg unknown_place    
    # scene bg japan
    show fuuji sigh 
    $ show_date()
    Fuuji "Sigh, Akane you need to stop doing this. You’re already almost an adult."
    $ add_seen_chapter("1-2")
    show fuuji sigh_dark
    Thought "We’re having our usual breakfast, when a strong taste was mixed in my hot drink."
    hide fuuji 
    show fuuji sigh at left 
    $ add_seen_chapter("1-3")
    show akane smirk at right 
    $ add_seen_chapter("2-1")
    Akane "What, you mean adding dried chilies in your coffee is immature? Hah."
    show fuuji sigh_dark 
    show akane smirk_dark

    show img3
    hide img3

    $ add_seen_chapter("2-2")
    $ show_people()
    Thought "My little sister, Akane. She has always been mischievous since childhood, and does things that will annoy anyone. Although she only does it to me, it gets tiring at times."
    hide fuuji
    hide akane 
    $ show_date()
    $ show_people()
    with fade

    $ add_seen_chapter("3-1")
    $ add_seen_chapter("3-2")
    show rain_particle
    Mom "Now, now. I’ll just replace your coffee and Akane, you really need to stop with that behavior."
    $ add_seen_chapter("4-1")
    $ show_people()

    Thought "And my mother, she had been taking care of us this whole time without our father figure, to which she explained subtlety but we already got an inkling feeling on what was happening."
    Thought "But we don’t want to pry any further, we love mother as much as she loves us and we best not to fret it over."
    show akane sad 
    $ add_seen_chapter("5-1")

    Akane "Pssh, alright alright."


    show img4
    hide img4   

    $ add_seen_chapter("6-1")
    $ add_seen_chapter("6-2")
    show akane sarcastic 
    Akane "I'll just do something else next time." 
    $ add_seen_chapter("7-1")
    $ show_cases()
    Thought "She says while having a grin in her face."
    hide akane 
    show fuuji sad 
    Fuuji "You never get tired, do you?"
    $ add_seen_chapter("8-1")
    show fuuji neutral2  
    $ show_tips()
    Fuuji "Anyway, graduation is nearing, I will have to find a Juku (cram) school to get into Tokyo University. So, I won’t be coming back here much often."
    $ add_seen_chapter("9-1")
    show fuuji neutral2_dark 
    hide title_art
    Thought "Since College was just in a few months away, I asked my uncle if I could use a spare house he had so that I can get to the university easily."
    $ add_seen_chapter("10-1")
    $ add_seen_chapter("10-2")
    hide fuuji
    show akane sad 
    Akane "..."
    $ show_date()
    show akane sad_dark
    Mom "My, it’s that time already… are you really fine by yourself?"
    $ add_seen_chapter("11-1")
    Mom "Just come home whenever you’re running low on ingredients or pocket money."
    hide akane 
    show fuuji smile 
    Fuuji "I do.{w} And thanks mom for keeping up with my selfishness."
    $ add_seen_chapter("12-1")
    $ add_seen_chapter("12-2")
    show fuuji smile_dark 
    Thought "We weren’t exactly rich, but we live comfortably because we’ve been receiving financial assistance from a certain organization my dad has an affiliation with, and mom provides us with everything else we need."
    hide fuuji 
    $ add_seen_chapter("13-1")
    show akane sad 
    Akane "..."
    show akane sad_dark 
    # $ add_seen_chapter("3-1")
    $ add_seen_chapter("14-1")
    Mom "Son, there’s no need to thank me, it’s my responsibility after all, if I can see you two being happy then I’m also happy."
    Thought "I smiled at mom. She clearly supports us as best as she can."
    Thought "Akane has been silent this whole time."
    $ add_seen_chapter("15-1")
    # $ add_seen_chapter ("4-1")
    show akane sad 
    Akane "..."
    show akane sad_dark
    $ show_date()
    Thought "She proceeds to eat without looking at the food."
    hide akane 
    show fuuji happy 
    Fuuji "Akane, you can still come to the house whenever you feel like it, just contact me before doing so, alright?"
    hide fuuji 
    show akane shock 
    Akane "..."
    show akane tsun 
    Akane "…I-is that so? Hmph! Then I’ll do just that since you asked me to."
    show akane blush_dark
    Thought "She then started eating as if the food was the most delicious thing ever, although it is delicious, it just makes me happy she’s back to being chirpy again."
    Thought "I have known Akane for so long so I know what’s the cause for her discomfort, she’d always been quite the annoying but loving sibling you’ll have in a family, but I don’t hate it."
    hide akane 
    stop music fadeout 1.0


    $ persistent.firstchapter_clear = True

    
label school:

    
    python:
        set_info_scene("02")
        set_info_location("03")
        set_info_date(2, "may", "wed")
        set_info_time("day")

    play music audio.day
    scene bg road_school
    with fade
    Thought "..."
    # play music "audio/day.mp3" fadein 3.0 volume 0.5
    Thought "We were done with our breakfast and since we go to the same school. We always go together whenever I came back home to visit mom, and well of course, Akane."
    Thought "I'm in my last year in high school and Akane was in her second year in junior high, we had to part ways inside as the buildings were of opposite ends."
    scene bg school_room 
    with fade
    show fuuji neutral 
    Fuuji "..."
    show fuuji neutral2_dark
    Student "Ah, he's here... let's get back later yeah?"
    hide fuuji 
    Thought "My classmates are avoiding me again, it was always like this since my early childhood having no father to grow with, there was a lot of rumors that I was the cause and whatnot, I ignore them."
    
    
    # $ add_seen_chapter("4-1")
    # $ add_seen_chapter("5-1")
    # $ add_seen_chapter("6-1")
    # $ add_seen_chapter("7-1")
    # $ add_seen_chapter("8-1")
    # $ add_seen_chapter("9-1")
    # $ add_seen_chapter("10-1")

    Thought "I know that I look unapproachable but I just can’t change it, I also don’t have any reason to make friends proactively."
    Thought "Of course, there were still some people who would talk to me, despite the rumors. But they didn’t take long to change their mind and believe it. The usual. Ah and well the bad ones let’s not forget them."
    show fuuji neutral_dark 
    Student "Yo Fuuji-kun, you’re still trying to act cool after all this time huh, that face really never fails to irritate me hahaha!"
    show fuuji sigh_dark 
    Thought "The man who’s also a third year but has a bigger and taller build than me has his ‘goons’ surrounding me."
    Student "Let’s take this outside." 
    Thought "He then waved his hand and everyone follows him.{w} Including me."
    hide fuuji 
    stop music fadeout 1.0
    Thought "It’s been like this since; people treat me as if I wanted this.  I just have to keep up the act."
    play music audio.tense fadein 1.0
    scene bg school_corner
    show fuuji disgust with vpunch
    python:
        set_info_scene("02")
        set_info_location("04")
        set_info_date(2, "may", "wed")
        set_info_time("evening")

    play sound "audio/sfx/punch1.mp3"
    Fuuji "...!"
    show fuuji disgust_dark
    Thought "I took a punch to the stomach, almost making me puke. I got into my knees having a painful expression."
    Student "Hey."
    show fuuji sigh_dark 
    Thought "He held my head as if I was a doll."
    show fuuji worry with hpunch
    Fuuji "Ghh-"
    show fuuji worry_dark
    Student "Look, I’m gonna ask you one more time."
    Thought "Still having a strong grip on my hair, he stares at me."
    Student "Stop acting like a hot shit."
    show fuuji sigh
    Fuuji "..."
    show fuuji sigh_dark
    Student "No reply huh, well-"
    show fuuji worry with vpunch
    play sound "audio/sfx/punch1.mp3"
    Fuuji "Gah-"
    show fuuji worry_dark
    Thought "He started punching me with his other fist."
    Student "Would you-"
    show fuuji sigh with hpunch
    play sound "audio/sfx/punch2.mp3"
    Fuuji "-Guh"
    show fuuji disgust_dark
    Student "Stop being-"
    show fuuji worry with vpunch
    play sound "audio/sfx/punch1.mp3"
    Fuuji "Akh-"
    show fuuji worry_dark
    Student "A little bitch-"
    show fuuji sigh with hpunch
    play sound "audio/sfx/punch2.mp3"
    Fuuji "Kha-" 
    show fuuji disgust_dark
    play sound "audio/sfx/punch1.mp3"
    Student "And act normal-"
    show fuuji worry with vpunch
    play sound "audio/sfx/punch2.mp3"
    Fuuji "Ugh-"
    show fuuji worry_dark
    Student "For once."
    show fuuji sigh 
    Fuuji "..."
    show fuuji sigh_dark
    Student "Phew! Man, that was tiresome."
    Thought "He lets go of me, the other students that was here was just watching."
    hide fuuji 
    Student "That exercise made me hungry, let’s bounce, you. Take his wallet."
    Thought "A smaller man fiddled with my pockets as I lie in the ground, finally finding what he was looking for he starts walking towards the man."
    stop music fadeout 1.0
    Thought "My face was seemingly swelling. I was more concerned that if my sister sees me like this, she’ll just be disappointed instead of trying to tend me."
    Thought "Since she was still a junior high, she gets to leave the school much early than me, she only has to take a train 5 minutes away from the school to get back home."
    Thought "..."
    play music audio.home fadein 1.0
    show fuuji sigh 
    Fuuji "Sigh, now where was the faucet again in this side of the building."
    show fuuji sigh_dark
    Thought "My face was bloodied, but no visible tear in the skin. I’ll just have to wash my face and a good night rest and everything would be back to normal. This was normal, at least in the family."
    hide fuuji 

label flashback:
    
    scene bg flashback
    with fade
    Thought2 "When I was a child, I still remember Dad being a little bit too strong for his size, he carries things bigger and heavier than him. Compared to his appearance, it just looked odd."
    Thought2 "\"Dad, how can you lift those things, you’re amazing!\""
    Thought2 "\"Ah well, can’t you see your dad’s biceps?\""
    nvl clear 
    nvl show  
    Thought2 "He then flexes his arms."
    Thought2 "It wasn’t anything but normal,{w} but I hadn’t thought of that back then."
    Thought2 "\"Woah! Dad, Dad lift me up as well.\""
    nvl clear 
    nvl show 
    Thought2 "\"Aiyo!\""
    Thought2 "He lifts me up on his shoulders with ease."
    Thought2 "\"Fuwaah... I'm as tall as you are now Dad!\""
    nvl clear 
    nvl show 
    Thought2 "A few years after that Dad left us, not having much to tell us we just kind of accept it,{w} well atleast I did since Akane didn’t quite remember Dad that much since she was pretty much just a kid." 
    Thought2 "Mom had to take care both of us for our daily needs, reason why I have so much respect to her."
    Thought2 "I do not hate my dad, but I’m just disappointed that after all these years there has been no communication between us."
    stop music fadeout 1.0
    nvl clear
label application:
    
    python:
        set_info_scene("04")
        set_info_location("04")
        set_info_date(5, "may", "wed")
        set_info_time("day")

    scene bg cram_hallway
    with fade 
    play music audio.day fadein 1.0
    show fuuji neutral2
    Fuuji "Hmmm… This cram school is neat."
    show fuuji neutral2_dark
    Thought "By that I meant that they have the newest equipment."
    show fuuji neutral_dark
    Thought "The seats look comfortable and the room is spacious enough for each student to move around."
    Thought "While the fee seems to be much higher than those of other, this is still within the budget mom gave me."
    stop music fadeout 1.0
    Thought "As I was waiting in line to manage the fees –"
    hide fuuji 
    show kikuchiyo neutral with fade
    play music audio.presence fadein 1.0
    Princess "..."
    show kikuchiyo neutral_dark 
    Thought "I met her, a girl in Kimono entered the premise with a 2 man in a traditional garb side by side as if ready to answer to any whims of the maiden."
    hide kikuchiyo 
    Thought "The other people in-line then gave way as soon as they saw her and bow as deep as they can, the two men lead the way. She then walks gracefully as she passes by each and every one."
    Thought "But I didn’t know who she was. I found myself standing in what was once a line of people."
    Man "Insolent! Move aside now or you will be cut down!"
    Thought "He’s readying his stance to wield his sword to what seems like a katana with that size."
    show kikuchiyo neutral 
    Princess "..."
    show kikuchiyo neutral_dark
    Fuuji "...Ah, I'm sorry."
    hide kikuchiyo 
    Thought "I then move aside."
    Man "Hmph!"
    Thought "The man then proceeds to lead the way for the girl in kimono."
    Thought "I glanced at her just before she passes to me and our eyes met."
    show kikuchiyo neutral 
    Princess "..."
    show kikuchiyo neutral_dark
    Thought "She’s pretty, with everything that I’ve seen. I concluded that she’s someone of high profile in this city at least so far, not that I know much really."
    hide kikuchiyo 
    Thought "When Akane wanted to be in a school that is popular, we decided to move here, that was just a few years ago."
    Thought "As you already guess my mother and I heed to Akane seemingly. We love her that much, but she’s still annoying."
    stop music fadeout 1.0
    Thought "After a few minutes the said people came back to where they came from, and the line was restored, seemingly back to normal. Even the people who bowed are now standing upright and some of them sighed as they do."
    play music audio.day fadein 1.0
    Applicant "Sheesh, that was scary. Is the {i}hime{/i} {size=-10}(Princess){/size} applying on this cram school as well?"
    Applicant "She could have gotten a personal tutor instead. Man, it would be scary to be in the same room with her." 
    Thought "The man begrudgingly says to what looks like his friend."
    Applicant "Ah well I can see this being a propaganda for them, but well only few can even afford a cram school, much so this specific one."
    Thought "He replied."
    show fuuji angry 
    Fuuji "..."
    show fuuji angry_dark 
    Thought "He’s got a point, if a high-profile person needs to study for their exams, they could easily hire a personal instructor to teach the girl." 
    Thought "She must have her own reasons, but there’s not much going to happen if I keep thinking about it.{w} The two man is now quiet,{w}  Ah I was staring at them all this time."
    hide fuuji 
    Applicant "..."
    Applicant "I just remembered, let’s go grab a drink, it seems like this would take a while ahaha…"
    show fuuji sigh 
    Thought "..."
    show fuuji sigh_dark
    Thought "Sigh, anyway just a few more applicants before my turn, their building is quite nice and accommodating so the waiting isn’t that tiresome."
    hide fuuji 
    stop music fadeout 1.0
    Thought "The day has gone on completely normal, but a hitch. I was accepted in the cram school."
    
label meeting:
    scene bg apartment 
    with fade
    Thought "..."
    play music audio.strolling fadein 1.0
    Thought "Fortunately, the cram school is only available during weekends, and so I woke up today a bit earlier than usual so I can prepare myself."
    show fuuji smile
    Fuuji "Hmm, if Akane comes here right now, my room being this empty, she'll nag me."
    show fuuji smile_dark
    Thought "The house my uncle had, it was a simple house with two floors. Thankfully there were some furnitures left especially on the living room.{w=0.5} Not that I'll get visitors anyway." 
    hide fuuji 
    Thought "I can cook my own food as I was tasked to cook back then when mom was doing other chores."
    Thought "As the house was in the middle of the city, I can get to my current school in my bicycle in about 25 minutes." 
    Thought "But the real take is that the universities are just 10 minutes away. It’s what I’d call investment. Since it’s been getting populated by the year."
    show fuuji happy 
    Fuuji "…Ah well, let’s look for a flower décor on the way back."
    hide fuuji 
    stop music fadeout 1.0
    
    scene bg black with fade
    Thought "I locked the door, and I head outside."
    
    scene bg road_cram 
    with fade 
    Thought "..."
    play music audio.day fadein 1.0
    Thought "On my way to the cram school, I saw Akane with her friends, eating a crepe by the side."
    show akane happy_dark
    Thought "Akane is quite popular as she can communicate with everyone with ease, and other people that are talking to her also seems to like her."
    show akane shock_dark
    Thought "She was the first one to notice me, she then hurriedly ran up to me."
    show akane happy with fade
    Akane "Aniki!"
    hide akane 
    show fuuji neutral 
    Fuuji "Akane, did you inform Mom you’re going out?"
    show fuuji neutral_dark
    Thought "I asked,{w} a senseless one."
    hide fuuji
    show akane sarcastic 
    Akane "I did! but I said I’ll only be out for a bit."
    show akane smile 
    extend "Teehee~"
    hide akane 
    show fuuji sigh 
    Fuuji "Sigh, just get back home before dawn, there has been a lot of crimes around here lately."
    show fuuji neutral2 
    Fuuji "And thank you for taking care of my little sister as always."
    show fuuji sigh_dark 
    Thought "I bowed to her other two friends."
    Girl "…A-ah, you’re welcome."
    Thought "The girl says to me with a hint of nervousness."
    hide fuuji
    Thought "I met them a few times when I came back home and Akane brought these two along with her, they seem to be nice kids."
    show akane tsun 
    Akane "Hmph! I’m no trouble!"
    show akane tsun_dark
    Thought "She poutingly says."
    hide akane 
    show fuuji smirk 
    Fuuji "Hah, whatever you say Akane." 
    show fuuji smile_dark
    Thought "I grin."
    hide fuuji 
    Girl "...Pfft-"
    show akane default2
    Akane "Ugh... what about you Aniki, what are you doing outside anyway?"
    hide akane 
    show fuuji neutral2 
    Fuuji "I’m on my way to my cram school, I only have half an hour before the session starts, that said I got to keep moving now."
    show fuuji sad 
    Fuuji "And remember to go home before dawn."
    hide fuuji 
    show akane frown 
    Akane "Hmm, okay..."
    show akane blush 
    Akane "Have a safe trip Aniki!"
    show akane blush_dark
    Thought "I waved my hand as I walked away from their group."
    hide akane 
    Thought "They were laughing as I get to the first corner."
    stop music fadeout 1.0

label cram:
    scene bg black
    with fade
    Thought "I arrived."
    scene bg cram_hallway 
    with fade
    Thought "..."
    play music "audio/strolling.mp3" fadein 3.0
    Thought "My room was at the second floor, but the building itself has up to 6th floor, including a rooftop."
    scene bg cram_room1
    with fade 
    Thought "As I’ve settled my things in my seat, some people are still coming in."
    Thought "After a few minutes later, people are already chattering."
    Girl "She's really here! What should I do, it’s really going to be awkward if she’s also in here!"
    Man "Ah… man do you think she already has a boyfriend? maybe no one was able to tell the tale. They’ll just be swiss cheese if they come near the princess."
    show fuuji neutral 
    Fuuji "..."
    show fuuji neutral_dark 
    stop music fadeout 1.0
    Thought "Then no more than a minute, silence befell in the room."
    hide fuuji with fade 
    show kikuchiyo neutral_dark 
    # play music "audio/presence.mp3" fadein 5.0 
    Thought "The princess everyone was talking about just now, is about to step in this room."
    Thought "She still has her retainers onlooking for her safety. But this time they stopped outside of the room."
    Thought "There are only 20 seats on this room, and with a stroke of either fortune or misfortune. The only free seat left is the one next to me."
    play sound "audio/sfx/heartbeat.mp3" 
    Thought "As if everything was normal, she proceeds to walk."
    show kikuchiyo neutral_dark with fade 
    Thought "Approaching."
    show kikuchiyo neutral_dark with fade 
    Thought "Her steps are the only sounds the room was making."
    show kikuchiyo neutral_dark with fade 
    Thought "Nearing."
    show kikuchiyo neutral_dark with fade 
    Thought "She’s now 5 meters away from the seat."
    show kikuchiyo neutral_dark with fade 
    stop sound fadeout 5.0 
    Thought "Stopped."
    show kikuchiyo neutral 
    
    Princess "..."
    show kikuchiyo neutral_dark 
    play sound "audio/sfx/chair.mp3" 
    Thought "She then took her seat and she still does it elegantly."
    
    Thought "Everyone was still tense, as I do not know her weight of responsibility, I’m not too affected by her presence."
    hide kikuchiyo 

    play music "audio/strolling.mp3" fadein 3.0 
    Thought "After a few minutes later, the instructor came in, also a bit staggered. But he managed to speak for the class to start."
    Thought "Some people then took a heavy breath."
    
    scene bg black
    with fade
    Thought "The class ended smoothly without much of a hitch, but everyone was still on their edge as the class proceeded."
    stop music fadeout 1.0

label sabotage:

    scene bg cram_room1 
    with fade 
    Thought "..."
    play music "audio/tense.mp3" fadein 3.0 
    Thought "As I was preparing to leave, a commotion can be heard outside –"
    Man "Hey, hey what are they doing?"
    Thought "I peeked at the full window glass and saw them."
    Thought "Two small trucks stopped abruptly in the opposite road of the building I was in."
    Thought "After a few seconds, four people got out of each truck from the rear in orderly fashion."
    Thought "They were wearing a field-gray colored jacket – they had a gun in hand, a rifle."
    Girl "*Shrieks*"
    Thought "The people from the outside panicked and started running away from the ominous party."
    Thought "The said party is now walking – towards us, this building."
    Thought "Everyone inside was panicking except for the princess, she is still preparing her things in an elegant manner. Her retainers on the other hand are now in their stance, ready to slice anyone who poses a danger to the princess."
    Thought "This building was made so that it feels like you’re in a university even if you were just in a cram school, it’s a square building but in the middle, it also has a small fountain that is lit up by the sky." 
    Thought "We were in the second floor and the men are at the ground level scanning their surrounding while the people fled in sight."
    Thought "I suddenly remembered what their outfit resembles, German infantry."
    Thought "They were worn by Germans in World War 2 as the grey color was said to be effective in becoming less visible for the enemy. It hit me just then that my father was associated with them in some way or another."
    Thought "As the people from the building fled, the men just ignored them and cautiously watched their surroundings."
    Thought "I was trying to think of ways on how I can get out of this building without them seeing me."
    Thought "But – "
    Thought "The princess was still here inside, I just noticed that we were the only people in this room."
    Thought "The two men that was guarding outside confronted the said men, I am not sure how they can fight off a gun with just a sword, I muttered."
    show fuuji angry2 
    Fuuji "Hey, you need to get out of here now." 
    show fuuji angry_dark 
    Thought "I said nonchalantly as I was pondering."
    hide fuuji 
    show kikuchiyo neutral 
    Princess "Hmph, my men would take care of them with ease. I’ll just have to wait."
    hide kikuchiyo 
    show fuuji sad 
    Fuuji "You don’t understand, they’re soldiers and they are looking out for me. You can just get out of here without needing to get hurt."
    hide fuuji 
    show kikuchiyo upset 
    Princess "Are you deaf, I do not care in the slightest who these people are, they are in my presence with hostility, then they are to be-"
    show kikuchiyo upset_dark
    Thought "To what a mans voice screaming out – "
    hide kikuchiyo 
    Man "PRINCESS RUN!"
    Thought "Echoing in the building. After a second a loud burst of gunshots was heard on the ground floor."
    stop music fadeout 3.0
    Thought "Silence."
    Thought "I concluded that they are a goner. Now they are free to look in every corner of this building."
    Thought "The princess stood up from her seat, started walking up to the door and was about to step outside."  
    show kikuchiyo upset 
    Princess "What is going-"
    show kikuchiyo upset_dark
    Thought "She might expose me if she leaves now."
    hide kikuchiyo 
    Thought "I ran up to her and covered her mouth with my hand."
    show fuuji angry 
    Fuuji "Shhh! I’m sorry to do this but you’re endangering me with what you are doing right now."
    show fuuji angry_dark 
    Thought "I whispered."
    hide fuuji 
    Thought "She’s still resisting and her kimono shuffles as she does so."
    show kikuchiyo upset 
    Princess "Mmmm! Mm!"
    show kikuchiyo upset_dark
    Thought "I heard footsteps that is clearly walking upstairs. They were nearing."
    hide kikuchiyo 
    Thought "I won’t get out of this room without them noticing me, I need to hide."
    Thought "Fortunately, as this was a high-end cram school, they had lockers for each student big enough to fit a body on it. It was seemingly convenient."
    Thought "The princess was still protesting, my hand was quite moist from her trying to talk through my hand."
    Thought "I also need to hide her."

    scene bg black 
    with fade 
    stop music fadeout 1.0
    play sound "audio/sfx/heartbeat.mp3" fadein 3.0
    Thought "I dragged her resisting body to the locker with me, it is cramped but I had no other choice on how I can make her quiet down."
    Thought "The footsteps outside were nearing, I then closed off the locker door. The room was now silent."
    Thought "She’s also seemed to have panicked more but her voice became softer."
    Fuuji "Look, I’m sorry again for this but I need you to be quiet. I’ll let go of my hand once we are clear."
    Thought "Speaking as quietly as I could."
    Princess "Mmmm... mmm."
    Thought "I just noticed that she’s being awkward now. But I need to keep her from making any sound. "
    Thought "The men are just outside of the room. They stopped."
    Man "Du, hast du das Mädchen schon gesehen? <You, have you seen the girl yet?>"
    Thought "As I expected, they were Germans."
    Man "Nein, sie müssen versucht haben, nach oben zu fliehen. <No, they must have tried to escape upstairs.>"
    Thought "The other man replied."
    Man "Wie auch immer, Intel sagte, sie trage einen Kimono. Achten Sie darauf, die Augen offen zu halten. <Anyway, Intel said she was wearing a kimono. Be sure to keep your eyes open.>"
    Thought "After talking to each other, they were peering each room as they came across."

label easing:

    Thought "As they pass each room, the sound they are making is easing out as they walk away farther."
    Thought "..."
    stop sound fadeout 1.0
    scene bg cram_room1
    with fade 
    Thought "I got both of us out from the cramped locker and scans the area."
    Thought "..."
    show fuuji sigh 
    Fuuji "Phew... okay it seems like they are gone now."
    show fuuji sigh_dark 
    Thought "I took off my hands off of her."
    hide fuuji 
    show kikuchiyo upset 
    Princess "Fuwah... you bastard..."
    Princess "You will pay for this you insolent man."
    show kikuchiyo upset_dark
    Thought "She spoke begrudgingly."
    show kikuchiyo upset
    Princess "That was the first time a man has touched me, and you did it the crudest way you can do!"
    show kikuchiyo upset_dark
    Thought "Still scanning the sorroundings for any of the men's presence."
    hide kikuchiyo 
    show fuuji worry 
    Fuuji "Look, I'm sorry. But the situation was abnormal, those men have the intent to kill."
    hide fuuji 
    show kikuchiyo upset 
    Princess "You are the only abnormal in this forsaken place, here I had thought I could finally redeem myself by trying to get along with you common folks."
    show kikuchiyo upset_dark
    Thought "She seemingly forgot what kind of situation we are in."
    show kikuchiyo upset
    Princess "What a disgrace, I'll have to get my retainers and make them punish for what you've done to me."
    show kikuchiyo sad_dark 

    scene bg cram_hallway with fade
    Thought "Before I got to say anything, she walks towards the door and leaned to the window onlooking the ground floor."
    hide kikuchiyo 
    Thought "She stops as soon as she peered on the window."
    show fuuji angry2 
    Fuuji "Hey-"
    hide fuuji 
    show kikuchiyo sad 
    Princess "...ah"
    Princess ".........AHHHHHHHH!!!!"
    hide kikuchiyo with fade 
    Thought "From her strict and elegant demeanor, she's now screaming at the sight of her former retainers lying dead on the ground."
    
    play music "audio/tension.mp3" fadein 3.0 volume 1

    Man "Das Mädchen! Das Mädchen! <The girl! The girl!>"
    Thought "One of the men on the upper floor saw us."
    Thought "The princess is still crying, now sitting on the ground."
    Thought "Her kimono that was once pretty is now wrinkled."
    Man "Lukas Das Mädchen ist im zweiten Stock, hol ihn dir jetzt! <Lukas The girl is on the second floor, get him now!>"
    show fuuji neutral 
    Fuuji "Tch."
    show fuuji neutral2 
    Fuuji "Sorry, but we'll have to get out of here now."
    show fuuji neutral_dark 
    Thought "She's not responding to any of my words, she's still bawling. Ruining her makeup she just had."
    show fuuji neutral 
    Fuuji "..."
    show fuuji neutral2 
    Fuuji "I guess I need to do it."
    hide fuuji 
    Man "Du! Hör auf, du dreckiger Bauer! <You! Stop it, you filthy peasant!>"
    Thought "Two men standing on the ground floor was onlooking us to prevent our escape, thankfully they are not shooting with their rifles at hand."
    Thought "I briskly lifted the girl in my arms. Without batting an eye, I head to the classroom with the princess in my arms."
    scene bg cram_room1
    with fade
    show kikuchiyo upset 
    Princess "Sniff... w-what are you doing! Get me back in there!"
    show kikuchiyo upset_dark
    Thought "She pleads while wiping the tears off of her face."
    hide kikuchiyo 
    show fuuji neutral 
    Fuuji "I'm afraid I can't do that now, I'll have to get us out of here, now."
    hide fuuji 
    Princess "...what-"
    with fade 
    #sfx of broken glass 
    Thought "I smashed the windows of the classroom with my feet, shattering it from the inside without so much of an effort."
    Thought "She wasn't crying anymore, then she looked at the shattered window."
    show fuuji angry2 
    Fuuji "Hold tight now."
    hide fuuji 
    show kikuchiyo neutral 
    Princess "what are we-"
    show kikuchiyo upset
    Princess "what are you going to-"
    hide kikuchiyo 
    show fuuji sigh 
    Fuuji "Uph!" 
    show fuuji angry2_dark with fade
    Thought "I jumped off the window with ease, and landed with my two feet up."
    hide fuuji 

    scene bg outside_school_dawn 
    with fade 
    stop music fadeout 1.0

    Thought "I landed by the side of the road, the sorrounding was clear of any pedestrians."
    Thought "Having this strength can only help me at situations like these."
    show fuuji sigh 
    Fuuji "Phew."
    hide fuuji 
    show kikuchiyo neutral 
    Princess "...y-you"
    show kikuchiyo upset
    Princess "You fool!"
    Princess "Just what did you think were you doing!"
    hide kikuchiyo 
    show fuuji neutral2 
    Fuuji "I was trying to get us out of the-"
    hide fuuji 
    show kikuchiyo upset 
    Princess "That was so dangerous, what would happen if I get hurt! You really-"
    show kikuchiyo sad_dark
    
    play music "audio/easing_tension.mp3" fadein 3.0 

    Thought "A series of footsteps can be heard nearing our position."
    hide kikuchiyo 
    show fuuji sigh 
    Fuuji "Okay listen, we'll need to move somewhere safe."
    show fuuji neutral2 
    Fuuji "Can you walk now?"
    hide fuuji 
    show kikuchiyo sad 
    Princess "I ca-"
    show kikuchiyo neutral_dark 
    Thought "I just noticed she's wearing {i}geta{/i} {size=10}(japanese sandals).{/size}"
    show kikuchiyo sad_dark 
    Thought "If she runs wearing that she'll just trip and fall."
    hide kikuchiyo 
    show fuuji worry 
    Fuuji "Scratch that, Hop in my back now."
    hide fuuji 
    show kikuchiyo upset 
    Princess "What do you think you're doing?"
    show kikuchiyo upset_dark 
    Thought "I knelt in the ground with my back to her."
    hide kikuchiyo 
    Man "Beeil dich, sie fliehen! <Hurry up, they are fleeing!>"
    show fuuji angry2 
    Fuuji "No more time dawdling, get on my back now."
    show fuuji angry_dark 
    Thought "The voices of the man were near, they'll catch up at this rate."
    hide fuuji 
    show kikuchiyo upset 
    Princess "Ugh! Just when will this boorish day end!"
    show kikuchiyo upset_dark
    Thought "She hopped on my back clumsily, seemingly awkward with the idea."
    show kikuchiyo neutral_dark 
    Thought "After she was settled, I started running to the nearest alleyway."
    hide kikuchiyo 
    Princess "Kyaah!"
    show fuuji smirk 
    Fuuji "Hold on tight."
    hide fuuji 
    show kikuchiyo sad 
    Princess "J-just what in god's name is happening!"
    hide kikuchiyo 
    Thought "I was still running at a pace a normal human can't."
    Man "Sollen wir Sir feuern? <Shall we fire sir?>"
    Thought "I can hear them talking from afar."
    Man "Nein, es ist zu riskant, wir müssen das melden. <No, it's too risky, we have to report this.>"
    stop music fadeout 3.0
    Thought "The men didn't gave chase, with the speed I was gaining, they have to get into their car before having a chance to catch me."

label after_dawn:
    
    scene bg near_apartment_dawn
    with fade
    Thought "..."
    play music "audio/relief.mp3" fadein 3.0 volume 0.5
    Thought "After half an hour of running away from the men, I decided to scan my sorrounding again before taking a break."
    Thought "I was not sure where I was going, but I somehow got into my street near the house."
    show kikuchiyo sad 
    Princess "A-are we safe now?"
    hide kikuchiyo 
    show fuuji neutral 
    Fuuji "I'm not sure yet."
    show fuuji neutral2 
    Fuuji "But my house is just nearby, we need to rest somewhere and a house seems to be the logical choice right now."
    show fuuji neutral_dark 
    Thought "It was not my house, but I need to assure that it was still my own property at the moment."
    hide fuuji 
    show kikuchiyo neutral 
    Princess "...into your house?"
    show kikuchiyo neutral_dark 
    Thought "I knelt down signaling to make her stand."
    show kikuchiyo upset 
    Princess "Hmph! Don't get too ahead of yourself, I need to contact my family soon, and you'll have to answer them in due time."
    show kikuchiyo upset_dark 
    Thought "She did get off my back but only with a sermon included."
    show kikuchiyo upset 
    Princess "And in what grounds do you have thinking I will just walk into someone's premises, especially the person is question is you? Hmph."
    show kikuchiyo upset_dark
    Thought "I guess that too is a concern, maybe I should call my sister then?"
    hide kikuchiyo with fade 
    Thought "..."  
    show akane frown_dark 
    Thought "Just as I had thought of that, I see Akane across the street just right by the door of the house."
    show akane neutral2_dark 
    Thought "Sigh, just when I told her to get back home before dawn, apparently uncle's house is one."
    show akane shock_dark 
    Thought "Akane then looked at my direction, seemingly squinting her eyes."
    hide akane 
    show fuuji worry 
    Fuuji "*Sigh* Look erm, princess. My sister is there, maybe that can ease you now? I have no intention of doing anything to you, we need to contact your family anyway."
    hide fuuji 
    show kikuchiyo neutral 
    Princess "T-then that’s fine…"
    show kikuchiyo upset  
    Princess "I swear that if you touch me again that will be the last thing you’ll ever feel!"
    hide kikuchiyo 
    show fuuji sigh 
    Fuuji "..."
    show fuuji neutral_dark 
    Thought "As long as that's cleared out of the way, now..."
    hide fuuji 
    Thought "Akane is now walking towards us, with a skeptic look on her face."
    Thought "..."
    show akane worry 
    Akane "Uhm... Aniki,{w} what are you doing with-"
    show akane shock
    extend "with the princess!?"
    show akane shock_dark 
    Thought "I am not sure with what’s she is surprised with, that I am with the princess, or does she think that something is going on between us."
    hide akane 
    show fuuji neutral2 
    Fuuji "Circumstances, anyway what about you, I told you to contact me before coming here right?"
    show fuuji neutral_dark 
    Thought "I remember telling her that to remind me if ever she’ll come to the house, she already nagged me a lot back when my room was so empty."
    hide fuuji 
    show akane sarcastic 
    Akane "I-I just thought of surprising you..." 
    show akane happy_dark 
    Akane "*whistles*"
    show akane frown 
    Akane "But instead I was the one who is surprised here, just what sort of deviant are you Aniki!?"
    hide akane 
    show fuuji sigh 
    Fuuji "*Sigh*... It's nothing like that, you are just trying to shift the problem here."
    show fuuji neutral_dark 
    Thought "Akane comes closer, she then tries to whisper"
    hide fuuji 
    show akane worry 
    Akane "Just what are you doing exactly, she’s with the Mibu’s! What do you think you’re doing!"
    hide akane 
    show fuuji worry 
    Fuuji "W-what, I said something happened at the cram school I was in, I just kind of had her with me."
    hide fuuji 
    show akane sad 
    Akane "*Sigh* I do not know what you did or what happened."
    show akane neutral  
    Akane "But be sure to not make her angry."
    hide akane 
    show fuuji disgust 
    Fuuji "..."
    show fuuji disgust_dark 
    Thought "I might have made her feel that way countless times already..."
    show fuuji sigh 
    Fuuji "...anyway."
    show fuuji neutral_dark 
    Thought "Akane then took a step away from me and she then stares at her."
    show fuuji neutral2 
    Fuuji "Uh… princess, here’s my sister Akane."
    hide fuuji 
    show akane sarcastic 
    Akane "H-{w}Hi there, princess!"
    show akane neutral_dark 
    Thought "Even Akane is stuttering at her presence, just what is this woman."
    hide akane 
    show kikuchiyo neutral 
    Princess "..."
    show kikuchiyo neutral_dark 
    Thought "She’s just standing besides me and seemingly scanning the area."
    hide kikuchiyo 
    Thought "Maybe she might not have a lot of chances to go out on her own, I guess."
    Thought "After a moment, the princess then finally talks."
    show kikuchiyo sad 
    Princess "Hmm, is he really your brother?"
    show kikuchiyo sad_dark 
    Thought "I'd say we quite look alike right?"
    hide kikuchiyo 
    show akane happy 
    Akane "O-oh yes.. he is definitely my brother alright."
    hide akane 
    show kikuchiyo neutral 
    Princess "..."
    Princess "All right, just get me a phone already. Just how long will we stand here?"
    hide kikuchiyo 
    show fuuji sad 
    Fuuji "..."
    show fuuji neutral2
    Fuuji "We're here."
    show fuuji neutral_dark 
    Thought "I pointed at the house Akane was just standing in front of mere minutes ago"
    hide fuuji 
    show kikuchiyo neutral 
    Princess "..."
    show kikuchiyo neutral_dark 
    Thought "No more response? Finally, peace."
    hide kikuchiyo 
    stop music fadeout 1.0 
    Thought "I guess I have some more time now to rethink what just had happened."

label apartment_company:
  
    scene bg living_room1 
    with fade 
    play music "audio/thin_purple.mp3" fadein 10.0
    Thought "We arrived at the house, it was neat as I had left it, having furnitures left by my uncle helped me this time."
    Thought "Thankfully I still had some of the gift set my mom gave me for my neighbors when I first came here, including some branded teas"
    show fuuji neutral2 
    Fuuji "I'm sorry for the place, but make way to the living room, I'll serve tea in just a moment."
    show fuuji neutral 
    Fuuji "And Akane, please keep her accompanied."
    hide fuuji 
    show akane shock_dark
    Akane "M-me?"
    show akane happy
    extend " Oh... I guess I'll have to. You have no experience with women after all ha ha ha..."
    Thought "She's really shaken being with her, well goodluck my dear sister."
    hide akane 
    show kikuchiyo neutral
    Princess "..."
    show kikuchiyo neutral_dark
    Thought "She's looking everywhere, as if it's a foreign place."
    hide kikuchiyo 
    show fuuji neutral2
    Fuuji "Oh and, the phone should be near the radio by the window."
    show fuuji neutral
    show fuuji neutral_dark 
    Thought "She nods."
    hide fuuji 
    scene bg black 
    with fade 
    Thought "After leaving that remark, I headed to the kitchen, and looked for the tea I had stocked up, along with some sweets that came along with it."
    scene bg kitchen_window_dawn
    with fade 
    Thought "As I was doing so, I looked at the window and the sun is already setting, wait… the last train today was at 18:00."
    Thought "Was Akane planning to stay here at the house today?"
    Thought "Cheeky brat. Well, at least she still kind of helped me today, if not saved me from the awkward situation with the princess."
    Thought "As I finish up preparing the tea, I headed to the living room."
    scene bg living_room1
    with fade 
    show akane happy_dark 
    Thought "They were both in the opposite ends of the table, but seemingly they are conversing with each other just fine."
    hide akane 
    show kikuchiyo neutral_dark
    Thought "In contrast, the princess is sitting with formality. Akane on the other hand is the opposite, she looks too comfortable."
    hide kikuchiyo 
    show akane blush
    Akane "I know right! Those things really are adorable, they help me sleep at night." 
    hide akane 
    show kikuchiyo shy 
    Princess "…really? I should try that then, thanks Akane."
    hide kikuchiyo 
    show akane happy 
    Akane "O-oh no problem Kiku-nee." 
    show akane happy_dark 
    Thought "I know my sister has no qualms talking to others… but just minutes ago she was intimidated by her presence."
    Thought "Must be {i}genetics{/i}…" 
    hide akane 
    Thought "As I lay the teas and the sweets I had in the table, I asked."
    show fuuji neutral2 
    stop music fadeout 3.0

label reaveal:
    Fuuji "So, have you contacted your family, they must be worried-sick." 
    hide fuuji 
    show kikuchiyo neutral 
    Princess "I have, they should be coming here any minute now."
    show kikuchiyo neutral_dark
    Thought "She's talking a bit more relaxed, maybe it's just my imagination."
    show kikuchiyo neutral 
    Princess "They sounded furious, but that is the usual in the family."
    Princess "And don't worry about them, Mr…"
    hide kikuchiyo 
    show fuuji neutral2 
    Fuuji "Fuuji, Izanagi Fuuji."
    hide fuuji 
    show kikuchiyo sad
    Princess "I-Izanagi…?"
    hide kikuchiyo 
    show fuuji neutral 
    Fuuji "Yes, that would be our surname."
    show fuuji neutral_dark 
    Thought "Akane nods in agreement."
    hide fuuji 
    show kikuchiyo neutral 
    Princess "Apologies, I was just surprised."
    Princess "While you were in the kitchen, I introduced myself to your sister."
    Princess "I will be formally introducing myself now."
    Kikuchiyo "I'm Kikuchiyo Mibu. The only heir to the Mibu Clan."
    show kikuchiyo sad_dark 
    Thought "She was now being her formal self, although a lot less hostile against me."
    show kikuchiyo neutral 
    Kikuchiyo "This should have been a common information here. But I am assuming that both of you are not originally a resident of this city."
    hide kikuchiyo 
    show fuuji neutral2 
    Fuuji "Yes. We just moved in here 2 years ago. As I do not interact with others too much, I couldn't have known much about your clan… Mibu."
    hide fuuji 
    show akane smirk 
    Akane "Aniki, you're just weird. You can't really help it!" 
    hide akane 
    show fuuji sad 
    Fuuji "Is that right, *smacks*."
    hide fuuji 
    show akane sad 
    Akane "O-ouch, see!"
    hide akane 
    show kikuchiyo shy
    Kikuchiyo "-pfft."
    show kikuchiyo shy_dark 
    Thought "Mibu was holding her laugh."
    show kikuchiyo neutral 
    Kikuchiyo "O-oh. *clears throat*"
    Kikuchiyo "Well then, I do not have much of an idea about what happened earlier…"
    Kikuchiyo "But you, Fuuji-san. You said that {i}they{/i} were looking out for you."
    hide kikuchiyo 
    show fuuji neutral 
    Fuuji "…yes."
    show fuuji neutral_dark
    Thought "I thought of dismissing Akane for this discussion, but they might look for her as well, she needs to be aware of them."
    hide fuuji 
    show akane shock
    Akane "Who's {i}they{/i}?" 
    hide akane 
    show fuuji neutral
    Fuuji "Akane… listen,"
    show fuuji neutral2
    extend "there are some bad guys wandering around this city, I am still not exactly sure about the reason, but they are bad news as it can be."
    show fuuji neutral 
    Fuuji "Do you remember our mother talking about dad's job?"
    show fuuji sigh_dark
    Thought "I am not so open talking about him, but with the danger they pose, I'll need to."
    hide fuuji 
    show akane neutral2 
    Akane "…yes,{w=0.5} but I can only recall some things." 
    hide akane 
    show fuuji sigh 
    Fuuji "And princess, since you are here, I'll explain it from the start."
    hide fuuji 
    show kikuchiyo neutral
    Kikuchiyo "…"
    Kikuchiyo "You can call me by my name, Fuuji-san."
    show kikuchiyo neutral_dark
    Thought "…?"
    Thought "Oh well, calling her name would be preferable."
    hide kikuchiyo 
    show fuuji worry 
    Fuuji "Okay, Kikuchiyo-san. This happened because the reason might be…"
    scene bg black
    with fade 
    show fuuji sigh_dark 
    Thought "I explained what happened at the cram school, Akane was shocked and asked me about my condition. She was genuinely worried about me."
    show fuuji neutral2_dark
    Thought "Kikuchiyo was a bit fidgety when I was telling Akane how we managed to escape, she looked at me suspiciously."
    show fuuji neutral_dark
    Thought "As I finish talking about the scene, I told Kikuchiyo about the possible reason the school was attacked, that includes but oddly she didn't put up much of a reaction. It feels like she knew it all along."
    hide fuuji 
    scene bg living_room1 
    with fade
    show kikuchiyo neutral
    Kikuchiyo "…"
    show kikuchiyo sad 
    Kikuchiyo "You are mistaken, Mr. Fuuji. While I can see why you would think that way, my family were aware of the round table and their movement. Their target, was the heir of the Mibu Clan. It was me." 
    show kikuchiyo neutral
    Kikuchiyo "But it seems like I underestimated them, with my two loyal retainers dying in my feet."
    show kikuchiyo upset
    Kikuchiyo "I swear I'll get their heads before I fall."
    show kikuchiyo neutral 
    Kikuchiyo "…"
    hide kikuchiyo 
    show fuuji neutral2 
    Fuuji "Hmm, that might as well be true, I don't have any actual evidence for them to target me." 
    show fuuji neutral_dark
    Thought "…so my father isn't related to this accident." 
    show fuuji sigh_dark
    Thought "I am not sure if I feel relieved or not, as there's still no way of knowing what happened to him." 
    hide fuuji 
    show kikuchiyo sad 
    Kikuchiyo "Mr Fuuji, forgive me for how I acted in front of you, as no man has dared tried getting close to me, this is a new experience."
    show kikuchiyo neutral 
    Kikuchiyo "As you see, Izanagi's are our family's long-lost confederate."
    Kikuchiyo "Our archive says that Izanagi's fled to another country, never to be heard again… we uncovered the members consisting of the round table. But we weren't able to have a clear contact any further with him." 
    Kikuchiyo "And now a descendant is in front me, as the heir of the Mibu's. This occurrence is once in a blue moon." 
    hide kikuchiyo
    show fuuji worry 
    Fuuji "…I didn't know any of that."
    hide fuuji 
    show kikuchiyo neutral
    Kikuchiyo "We owe a great deal to the Izanagi's; I was hoping that we could establish a new relationship we had lost."
    hide kikuchiyo 
    show fuuji sad 
    Fuuji "Hold on… this is still new to me,"
    show fuuji neutral2  
    extend "and even if that were the case. Our family isn't something that would benefit your family, despite the debt that you owe us."
    hide fuuji 
    show kikuchiyo neutral
    Kikuchiyo "Fret not, Mr. Fuuji. While you may think of it as that. Our family was built upon the efforts of the Izanagi's, I won't be here in front of you if that were not the case." 
    hide kikuchiyo 
    show fuuji sigh 
    Fuuji "…"
    show fuuji sigh_dark 
    Thought "I didn't know that my family had that kind of history… but if they managed to make even a princess of the clan be polite to me, it must run deep."
    show fuuji sigh 
    Fuuji "*sigh*, I do not know what to say, this day never exhaust of things to unravel." 
    hide fuuji 
    show kikuchiyo neutral 
    Kikuchiyo "…" 
    show kikuchiyo neutral_dark 
    Thought "Is she really serious? This might be some sort of a joke to get a kick out of it. But she sounded sincere while talking about the endeavors of my family."
    show kikuchiyo neutral
    Kikuchiyo "So Mr. Fuuji, do you still want to form a relationship between the families, although even if you refuse, we would respect your decision and will try to aid your family as best as we can." 
    Kikuchiyo "Forming the lost relationship will empower the Mibu clan, so it is a selfish request of me. Especially requesting so just after I met you, Mr. Fuuji."
    show kikuchiyo neutral_dark 
    Thought "I am not sure what kind of help I will be to make the Mibu more powerful, but she seems sincere and eager to do so. But on the other hand, our daily lives of my family now might get disrupted. But I don't think that would be the case here."
    Thought "If those people are targeting the Mibu's that would also affect us if we do form some kind of relationship, although I cannot foresee the future. I've got a feeling that I would be able to know more about my dad if I was with them."
    hide kikuchiyo 
    #Accept the offer.
    #Decline the offer.

label accepted:
    #--Accepted the offer--#
    show fuuji sigh
    Fuuji "I am still unclear about the deeds my family had done to you,"
    show fuuji neutral2 
    extend "but If I can know more about my family, especially that my dad is missing. I would appreciate your offer."
    show fuuji neutral_dark 
    Thought "My mind still wasn't in the clear, but I hope that I made the right decision."
    hide fuuji
    show kikuchiyo shy 
    Kikuchiyo "R-really, Mr. Fuuji?"
    hide kikuchiyo 
    show fuuji neutral2 
    Fuuji "Yes, although this seems to be a rash decision, I'll fulfill whatever is asked of me in exchange of getting aid to know more about my dad." 
    hide fuuji 
    show kikuchiyo smile 
    Kikuchiyo "Certainly, Mr. Fuuji, we won't disappoint and you would have no burden whatsoever, we just need your presence. We would help you in anyway we can." 
    show kikuchiyo shy_dark
    Thought "Akane who has been silently listening to us this whole time, finally spoke up."
    hide kikuchiyo
    show akane worry
    Akane "O-oh, umm,"
    show akane sarcastic 
    extend "this turned into something serious all of a sudden. May I still call you Kiku-nee…?" 
    hide akane 
    show kikuchiyo smile 
    Kikuchiyo "If you wish to do so, Akane-san." 
    hide kikuchiyo 
    show akane neutral 
    Akane "Kiku-nee…"
    show akane happy  
    extend "please still call me as Akane without the -san!"
    hide akane 
    show kikuchiyo smile 
    Kikuchiyo "O-oh… sure Akane." 
    show kikuchiyo smile_dark 
    Thought "Indeed it was definitely something all of a sudden, but this time I'm taking a step forward, I hope."
    hide kikuchiyo 
    show akane blush_dark 
    Thought "For the longest time, I was just relying on most other people to solving my mundane problems, my mother who has been lonely this time still greets us with a smile every day and I took it for granted."
    hide akane 
    Thought "My father that had no communication for more than a decade, I was thinking that maybe someday he would just come home and everything is back to normal." 
    show fuuji neutral_dark 
    Thought "But life isn't that lucky for everyone. While I had these {i}strengths{/i} a normal human can't do, it's still because of them that my family can't lead a happy normal life."
    show fuuji neutral2 
    Fuuji "Are you not afraid of us? We can literally wreak havoc if we do so."
    hide fuuji 
    show akane sarcastic 
    Akane "Geez Aniki, you make me sound like a Gorilla on a rampage." 
    show akane default2 
    Akane "Sorry Kiku-nee, Aniki is just scaring you, we won't do something so barbaric… although if needed, we'll do it."
    show akane neutral_dark 
    Thought "Akane sounded determined, but with the case in hand, people with guns loitering this land, just to get their objective after sullying someone."
    hide akane 
    show kikuchiyo neutral
    Kikuchiyo "Yes, Fuuji-san. I am aware, although not to this extent. At first, I thought you were too athletic for your build. But after what you have explained just now, I am not so bothered if you chose to do anything what you judged is right."
    hide kikuchiyo
    show fuuji neutral 
    Fuuji "…"
    show fuuji sigh 
    Fuuji "*sigh* I guess there's no undoing this, alright."
    hide fuuji 
    show akane sarcastic 
    Akane "Aniki you're just being stubborn now, c'mon I'll finally have a sister!"
    hide akane 
    show fuuji neutral2 
    Fuuji "You're making it sounds like I'm getting married." 
    hide fuuji 
    show kikuchiyo smile 
    Kikuchiyo "…!"
    show kikuchiyo shy_dark
    Thought "Kikuchiyo was… blushing?" 
    show kikuchiyo neutral 
    Kikuchiyo "*clears throat*, my family would be here in a moment and would escort me back home. I'll explain the circumstances, so pardon them if they react violently in your presence." 
    hide kikuchiyo 
    show fuuji neutral2
    Fuuji "Okay, I already had a taste of that when I first met you, so it's fine."
    show fuuji neutral_dark 
    Thought "Just a few days ago, I wouldn't imagine her being so polite to me, even being accommodating."
    hide fuuji 
    show kikuchiyo upset 
    Kikuchiyo "I-I'm sorry for that display Mr. Fuuji."
    hide kikuchiyo 
    show fuuji smile_dark 
    Thought "I just laughed. it was too comical at the time."
    show fuuji smile 
    Fuuji "It's fine, although I hope that I could still talk to you as normal… this is the first time I was able to open up to someone else."
    hide fuuji 
    show kikuchiyo smile 
    Kikuchiyo "O-oh… is that right."
    show kikuchiyo shy 
    Kikuchiyo "…"
    show kikuchiyo shy_dark 
    Thought "She's… probably getting a wrong idea. But I guess that is how I worded it." 
    hide kikuchiyo with renpy.transition(Dissolve(0.25), layer="master")
    Thought "The sound of cars stopping in front of the house can be heard."
    Thought "They must be with Kikuchiyo."

label yakuza: 

    show kikuchiyo neutral 
    Kikuchiyo "Fuuji-san, Akane, please let me explain the situation."
    Kikuchiyo "I told them that I took shelter from here after the incident."
    show kikuchiyo neutral_dark 
    Thought "Well that should sum it up…"
    hide kikuchiyo 
    Thought "A series of knocks can be heard from the door."
    Man "Princess! are you there? If you can't answer within 30 seconds, we'll bust through this door to save you!"
    show kikuchiyo upset
    Kikuchiyo "*sigh*, forgive my men's attitude." 
    show kikuchiyo neutral
    extend "It seems like they were frantic after learning about my whereabouts."
    hide kikuchiyo 
    show fuuji neutral2 
    Fuuji "Sure, they really seem agitated."
    hide fuuji 
    show akane shock
    Akane "They're actually covered in tattoos… isn't that painful?"
    show akane neutral_dark 
    Thought "It's true, their presence alone is intimidating, bundled together they can overthrow anyone. That's what I thought."
    hide akane 
    show kikuchiyo neutral 
    Kikuchiyo "Well if you may excuse me."
    hide kikuchiyo 
    Thought "Kikuchiyo headed to the entrance, fixing her demeanor as she opens the front door."
    Thought "Akane and I was in the living room, waiting for what's to come next."
    Thought "After the men saw the princess, they all seemingly teared up. Some even cheered in unison. But one man stood and looked at Kikuchiyo, after a moment he entered the house and peered through every room his eye could see."
    Thought "Finally, he saw us. He walked up and-"
    show fuuji disgust 
    Fuuji "…-ugh"
    show fuuji disgust_dark
    Man "You… you're the one who sullied the princess."
    show fuuji sigh_dark 
    Thought "He held my neck, lifting me from the ground."
    hide fuuji 
    show akane angry
    Akane "Wh-what are you doing!? Drop my brother now!"
    show akane angry_dark
    Thought "It doesn't hurt. But I got taken aback and I couldn't react properly."
    Thought "For now I'll… just let him do what he wants." 
    show akane frown_dark 
    Thought "Akane knows that I'm not getting hurt by this, but she's just too caring to bear seeing me like this."
    Thought "I just need to gauge what they can do."
    hide akane 
    show kikuchiyo upset 
    Kikuchiyo "SHINAZU!"
    show kikuchiyo upset_dark 
    Thought "To what sounded like a shriek from a madwoman." 
    hide kikuchiyo 
    Man "…!"
    Thought "The man lifting me, draw back his hands and dropped me."
    Thought "As he did so, his face contorted as if he did a grievous sin just now."
    show kikuchiyo upset 
    Kikuchiyo "You're acting on your own again!"
    show kikuchiyo upset_dark 
    Thought "I didn't notice Kikuchiyo was already here."
    show kikuchiyo upset 
    Kikuchiyo "While I appreciate you acting for my own well-being."
    Kikuchiyo "Learn to listen to me before acting so rashly, do you even know who you just attacked!?"
    show kikuchiyo upset_dark 
    Thought "She's… really furious."
    hide kikuchiyo 
    Thought "The man in question knelt in front of her."
    Shinazu "Hah, this man has touched you despite knowing who you are, princess."
    Shinazu "I assumed that he was being too familiar in your presence."
    show kikuchiyo upset
    Kikuchiyo "Enough, we will continue on this later. Apologize to what you've just done to Mr. Fuuji." 
    hide kikuchiyo
    Thought "The man trembled, as if he's too reluctant to do so."
    show akane worry 
    Akane "Aniki… are you okay? Does it hurt somewhere?"
    hide akane 
    show fuuji sigh 
    Fuuji "Yes, Akane. I'm fine, thank you."
    show akane sad 
    Akane "*sigh*,"
    show akane blush2 
    extend " you still keep doing this after all this time, I just can't leave you alone."
    hide akane 
    show fuuji smile 
    Fuuji "Now now… I'm sorry for that display."
    show fuuji sigh_dark 
    Thought "Akane and I cares for each other equally, although I have trouble trying to express it myself."
    hide fuuji 
    show kikuchiyo upset 
    Kikuchiyo "Are you not listening, Shinazu?"
    Kikuchiyo "Apologize, now."
    hide kikuchiyo 
    Shinazu "B-but princess, we do not bow ourselves to peasants. It would disgrace the Mibu's integrity."
    show kikuchiyo neutral 
    Kikuchiyo "…did you just call him a peasant?"
    show kikuchiyo neutral_dark 
    Shinazu "Ye-"   
    Thought "*slaps*"
    with fade
    Thought "…"
    Kikuchiyo "This man in front of you is a descendant of the Izanagi, you wretched."
    Shinazu "…!"
    Shinazu "T-the Izanagi…?"
