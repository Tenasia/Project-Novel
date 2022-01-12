screen info_panel(label_text, message_text, icon_d, alignment, trans=None):

    style_prefix "info_panel"

    frame at trans:
        background Frame("gui/nvl.png", 38, 0, 12, 0, ysize = 24, yoffset=28)
        align alignment

        has vbox:
            spacing 5

        hbox:
            spacing 10
            xalign 0.09


            add icon_d


            label label_text


        window:
            background None
            margin (0, 0)
            top_padding 5
            bottom_padding 0
            left_padding 40
            right_padding 0
            xsize 500
            yminimum 50
            ymaximum 150

            text message_text

        transclude

init -2:

    style info_panel_label_text is text:
        font "Poppins-Light.ttf"
        size 20
        spacing 0
        kerning 0
        layout "nobreak"

        outlines [(1, "#00000099", 0, 0)]

    style info_panel_text is text:
        font "Poppins-Light.ttf"
        size 13
        spacing 0
        kerning 0
        outlines [(1, "#00000088", 0, 0)]

screen game_menu2():
    key "mousedown_3" action Return()


    style_prefix "game_menu" tag menu

    default tp = Tooltip("")
    $ bgm_title = get_current_bgm_title()


    add "gui/nvl.png"


    use info_panel(_("BGM"), get_current_bgm_title(), "gui/thumb.png", (0.05, 0.35), game_menu_info_appear)

    # use info_panel(_("Location"), get_location_name(), "gui/right_click_content_location.png", (0.1, 0.50), game_menu_info_appear(0.1))

    # use info_panel(_("Tip"), get_location_tip(), "gui/right_click_content_tips.png", (0.2, 0.65), game_menu_info_appear(0.2))
init -2 python:
    renpy.music.register_channel("music", mixer="music", loop = True, file_prefix="audio/", file_suffix=".mp3")

define bgm_titles = {
    "bgm_00" : _("day"),
    "bgm_01" : _("easing_tension"), 
    "bgm_02" : _("flashback"),
    "bgm_03" : _("home"),
    "bgm_04" : _("homey"),
    "bgm_05" : _("prologue"),
    "bgm_06" : _("tense"),
    "bgm_07" : _("tension"),
    "bgm_08" : _("thin_purple"),
    "bgm_09" : _("Title"),
    "bgm_10" : _("true_home"),
}

init -3:

    define audio.day = "<loop 000.000 to 143.704>bgm_00"
    define audio.easing_tension = "<loop 000.577 to 067.038>bgm_01"
    define audio.flashback = "<loop 008.478 to 091.957>bgm_02"
    define audio.home = "<loop 000.109 to 083.587>bgm_03"
    define audio.homey = "<loop 000.000 to 097.818>bgm_04"
    define audio.prologue = "<loop 000.167 to 181.500>bgm_05"
    define audio.tense = "<loop 000.167 to 181.500>bgm_06"
    define audio.tension = "<loop 000.167 to 097.818>bgm_07"
    define audio.thin_purple = "<loop 000.167 to 097.818>bgm_08"
    define audio.Title = "<loop 000.0167 to 150.019>bgm_09"
    define audio.true_home = "<loop 000.0167 to 150.019>bgm_10"

init -2 python:
    def get_current_bgm_title():
            
            now_playing = renpy.music.get_playing()
            
            if now_playing:
                now_playing = now_playing[-6:]
                if now_playing in bgm_titles:
                    return bgm_titles[now_playing]
            
            return 

transform game_menu_info_appear(delay=0):
        yanchor 0.0
        alpha 0.0
        xoffset -200


        pause delay
        ease_back .5 alpha 1.0 xoffset 0