




image ctc:
    "gui/arrow.png"
    xalign 0.80
    yalign 0.9
    xoffset 50
    yoffset 25
    xsize 75
    ysize 75
    alpha 1

    block:
        linear 1 alpha 1
        "gui/arrow.png"
        linear 1 alpha 0
        repeat

label splashscreen:

    scene black
    with Pause(1)

    show text "This story is undoubtedly nothing more than fantasy.\n It could not possibly have any relation to real persons,\norganizations, or events." with dissolve 
    with Pause(5)

    hide text with dissolve
    with Pause(1)
    # $ renpy.movie_cutscene("images/Osu.mp4") 
    return 

init:
    image flickering_light:
        "images/background_GUI/Lit.png"
        pause 1.5
        "images/background_GUI/Not_lit.png"
        pause 0.1
        "images/background_GUI/Lit.png"
        pause 1.5
        "images/background_GUI/Not_lit.png"
        pause 0.1
        "images/background_GUI/Lit.png"
        pause 0.2
        "images/background_GUI/Not_lit.png"
        pause 0.1
        "images/background_GUI/Dim.png"
        pause 0.2
        "images/background_GUI/Lit.png"
        pause 1.5
        
        repeat



















#Oswald Sprites
image fuuji angry :
    "images/Oswald/os_angry.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji angry_dark :
    "images/Oswald/os_angry_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji angry2 :
    "images/Oswald/os_angry2.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji angry2_dark :
    "images/Oswald/os_angry2_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji annoyed :
    "images/Oswald/os_annoyed.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji annoyed_dark :
    "images/Oswald/os_annoyed_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji blush :
    "images/Oswald/os_blush.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji blush_dark :
    "images/Oswald/os_blush_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji disgust :
    "images/Oswald/os_disgust.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji disgust_dark :
    "images/Oswald/os_disgust_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji happy :
    "images/Oswald/os_happy.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji happy_dark :
    "images/Oswald/os_happy_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji laugh :
    "images/Oswald/os_laugh.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji laugh_dark :
    "images/Oswald/os_laugh_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji laugh2 :
    "images/Oswald/os_laugh2.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji laugh2_dark :
    "images/Oswald/os_laugh2_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji neutral :
    "images/Oswald/os_neutral.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji neutral_dark :
    "images/Oswald/os_neutral_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji neutral2 :
    "images/Oswald/os_neutral2.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji neutral2_dark :
    "images/Oswald/os_neutral2_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji sad :
    "images/Oswald/os_sad.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji sad_dark :
    "images/Oswald/os_sad_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji sigh :
    "images/Oswald/os_sigh.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji sigh_dark :
    "images/Oswald/os_sigh_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji smile :
    "images/Oswald/os_smile.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji smile_dark :
    "images/Oswald/os_smile_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji smirk :
    "images/Oswald/os_smirk.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji smirk_dark :
    "images/Oswald/os_smirk_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji tsun :
    "images/Oswald/os_tsun.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji tsun_dark :
    "images/Oswald/os_tsun_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji worry :
    "images/Oswald/os_worry.png" with renpy.transition(Dissolve(0.25), layer="master")

image fuuji worry_dark :
    "images/Oswald/os_worry_dark.png" with renpy.transition(Dissolve(0.25), layer="master")


#Lacie Sprites
image akane angry :
    "images/Lacie/lc_angry.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane angry_dark :
    "images/Lacie/lc_angry_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane blush :
    "images/Lacie/lc_blush.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane blush_dark :
    "images/Lacie/lc_blush_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane blush2 :
    "images/Lacie/lc_blush2.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane blush2_dark :
    "images/Lacie/lc_blush2_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane default2 :
    "images/Lacie/lc_default2.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane default2_dark :
    "images/Lacie/lc_default2_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane frown :
    "images/Lacie/lc_frown.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane frown_dark :
    "images/Lacie/lc_frown_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane happy :
    "images/Lacie/lc_happy.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane happy_dark :
    "images/Lacie/lc_happy_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane neutral :
    "images/Lacie/lc_neutral.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane neutral_dark :
    "images/Lacie/lc_neutral_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane neutral2 :
    "images/Lacie/lc_neutral2.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane neutral2_dark:
    "images/Lacie/lc_neutral2_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane sad :
    "images/Lacie/lc_sad.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane sad_dark :
    "images/Lacie/lc_sad_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane sarcastic :
    "images/Lacie/lc_sarcastic.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane sarcastic_dark :
    "images/Lacie/lc_sarcastic_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane shock :
    "images/Lacie/lc_shock.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane shock_dark :
    "images/Lacie/lc_shock_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane smile :
    "images/Lacie/lc_smile.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane smile_dark :
    "images/Lacie/lc_smile_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane smirk :
    "images/Lacie/lc_smirk.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane smirk_dark :
    "images/Lacie/lc_smirk_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane tsun :
    "images/Lacie/lc_tsun.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane tsun_dark :
    "images/Lacie/lc_tsun_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane worry :
    "images/Lacie/lc_worry.png" with renpy.transition(Dissolve(0.25), layer="master")

image akane worry_dark :
    "images/Lacie/lc_worry_dark.png" with renpy.transition(Dissolve(0.25), layer="master")


#Kikuchiyo Sprites
image kikuchiyo neutral :
    "images/Kikuchiyo/kk_neutral.png" with renpy.transition(Dissolve(0.25), layer="master")

image kikuchiyo neutral_dark :
    "images/Kikuchiyo/kk_neutral_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image kikuchiyo smile :
    "images/Kikuchiyo/kk_smile.png" with renpy.transition(Dissolve(0.25), layer="master")

image kikuchiyo smile_dark :
    "images/Kikuchiyo/kk_smile_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image kikuchiyo sad :
    "images/Kikuchiyo/kk_sad.png" with renpy.transition(Dissolve(0.25), layer="master")

image kikuchiyo sad_dark :
    "images/Kikuchiyo/kk_sad_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image kikuchiyo shy :
    "images/Kikuchiyo/kk_shy.png" with renpy.transition(Dissolve(0.25), layer="master")

image kikuchiyo shy_dark :
    "images/Kikuchiyo/kk_shy_dark.png" with renpy.transition(Dissolve(0.25), layer="master")

image kikuchiyo upset :
    "images/Kikuchiyo/kk_upset.png" with renpy.transition(Dissolve(0.25), layer="master")

image kikuchiyo upset_dark :
    "images/Kikuchiyo/kk_upset_dark.png" with renpy.transition(Dissolve(0.25), layer="master")
