

init offset = -1


style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    bottom_padding 10
    top_padding 10
    background Frame("gui/extra/frame.png", gui.frame_borders, tile=gui.frame_tile)



screen say(who, what):
    style_prefix "say"
    key "mousedown_4" action ShowMenu("history")
    key "mouseup_3" action ShowMenu("game_menu")
    
    window:
        background Transform(Frame("gui/textbox.png", xalign=50, yoffset=-100, ysize=500), alpha=persistent.window_opacity)
        id "window"
        yalign 0.956
        ysize 175

        if who is not None:
            hbox:
                xalign 0.5
                yalign 0.5
                yoffset -150
                text who id "who"
        hbox:
            text what id "what"

    

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 0.5


init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

style nvl_dialogue:
    properties gui.text_properties("dialogue")

    
## Input screen ################################################################

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################

screen quick_menu(): 
    
    zorder 100
    
    if quick_menu:
        frame:
            background None
            xfill 0.5 
            yalign 0.9999
            yoffset 10
            
            
            hbox:
                xalign 0.975
                yalign 0.5
                spacing 0
                frame:
                    # background "gui/navbar.png"
                    background None
                    yoffset -10
                    xoffset -550
                    hbox:
                        yoffset 7.5
                        xoffset 550
                        imagebutton:
                            xoffset 90
                            idle "gui/gui_buttons/GUI quick_buttons/save_idle.png"
                            hover "gui/gui_buttons/GUI quick_buttons/save_hover.png"
                            action ShowMenu('save')
                        imagebutton:
                            xoffset 80
                            idle "gui/gui_buttons/GUI quick_buttons/load_idle.png"
                            hover "gui/gui_buttons/GUI quick_buttons/load_hover.png"
                            action ShowMenu('load')
                        imagebutton:
                            xoffset 60
                            idle "gui/gui_buttons/GUI quick_buttons/auto_idle.png"
                            hover "gui/gui_buttons/GUI quick_buttons/auto_hover.png"
                            selected_idle "gui/gui_buttons/GUI quick_buttons/auto_hover.png"
                            action Preference("auto-forward", "toggle")
                        imagebutton:
                            xoffset 30
                            idle "gui/gui_buttons/GUI quick_buttons/skip_idle.png"
                            hover "gui/gui_buttons/GUI quick_buttons/skip_hover.png"
                            action Skip() alternate Skip(fast=True, confirm=True)
                        imagebutton:
                            idle "gui/gui_buttons/GUI quick_buttons/logs_idle.png"
                            hover "gui/gui_buttons/GUI quick_buttons/logs_hover.png"
                            action ShowMenu('history')
                        imagebutton:
                            idle "gui/gui_buttons/GUI quick_buttons/settings_idle.png"
                            hover "gui/gui_buttons/GUI quick_buttons/settings_hover.png"
                            action ShowMenu('preferences')
        hbox:
            xalign 0.97
            yalign 0.775
            xoffset 18

            imagebutton:
                idle "gui/game_menu_icons/hide_ui_idle.png"
                hover "gui/game_menu_icons/hide_ui_selected.png"
                selected "gui/game_menu_icons/hide_ui_selected.png"
                action HideInterface()
        hbox:
            xalign 0.97
            yalign 0.875
            xoffset 35
            yoffset 25
            imagebutton:
                idle "gui/game_menu_icons/notebook_idle.png"
                hover "gui/game_menu_icons/notebook_selected.png"
                selected "gui/game_menu_icons/notebook_selected.png"
                action ShowMenu("game_menu")

init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")    

style quick_button_text:
    properties gui.button_text_properties("quick_button")

## Navigation screen ###########################################################

screen navigation():


    python:

        newest_slot = renpy.newest_slot()
        if newest_slot:
            newest_slot = newest_slot.split("-")

    vbox:

        spacing -5
        xalign 0.8
        yalign 0.50
        box_layout u'vertical'
        text "{size=195}F{/size}OR {size=195}T{/size}HEE" size 150 xalign 0.785 yalign 0.25 font "fonts/Cinzel-Extrabold.ttf"
        text "{size=50}T{/size}HE {size=50}U{/size}NBROKEN" size 35 xalign 0.5 yoffset -50 font "fonts/Cinzel-Extrabold.ttf"
        
        
        if main_menu:
           
            textbutton _("START") action Start():
                xalign 0.5
            
            textbutton _("CONTINUE"):
                xalign 0.5
                if newest_slot:
                    action [SetField(no_rollback, "last_loaded_slot", newest_slot),
                            FileLoad(newest_slot[1], confirm=False, page=newest_slot[0], newest=False)]
                else:
                    action SensitiveIf(False)
                

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("LOAD") action ShowMenu("load"):
            xalign 0.5

        textbutton _("SETTINGS") action ShowMenu("preferences"):
            xalign 0.5

        textbutton _("EXTRA") action ShowMenu("extra"):
            xalign 0.5

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        if renpy.variant("pc"):

            textbutton _("QUIT") action Quit(confirm=not main_menu):
                xalign 0.5


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    xalign 0.5
    font "Swiss721LightBT.ttf"
    

## Main Menu screen ############################################################

screen main_menu():

    tag menu


    add "flickering_light"
    add "title_art"
    # add "rain_layer"
    frame:
        style "main_menu_frame"

    use navigation


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Settings Menu screen ############################################################

screen settings_menu(title, scroll=None, yinitial=0.0):
    
    style_prefix "game_menu"
    
    
    add "flickering_light"
    add "title_art"
    frame:
        style "game_menu_outer_frame"

        hbox:

            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    if main_menu:
        frame:
            xsize 850
            ysize 100
            xalign 0.5
            yalign 0.9
            xoffset 322.5
            background None
            hbox:
                spacing 50


                textbutton "SAVE" action ShowMenu('save')
                textbutton "LOAD" action ShowMenu('load')
                textbutton "SETTINGS" action ShowMenu('preferences') 
                textbutton "TITLE" action MainMenu()
                textbutton "QUIT" action Quit(True)
                textbutton "BACK" action Return()

        key "game_menu" action ShowMenu("main_menu")



#info panel



screen info_panel(label_text, message_text, icon_d, alignment, trans=None):

    style_prefix "info_panel"

    frame at trans:
        background Frame("gui/var_bar.png", 38, 0, 12, 0, ysize = 48, yoffset=0)
        align alignment

        has vbox:
            spacing 5

        hbox:
            spacing 10
            xalign 0.09


            add icon_d xsize 50 ysize 50 yoffset -25


            label label_text text_size 30 yoffset -8


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

            text message_text size 25

        transclude

init -2:

    style info_panel_label_text is text:
        font "fonts/Poppins-Light.ttf"
        size 20
        spacing 0
        kerning 0
        layout "nobreak"

        # outlines [(1, "#00000099", 0, 0)]

    style info_panel_text is text:
        font "fonts/Poppins-Light.ttf"
        size 13
        spacing 0
        kerning 0
        # outlines [(1, "#00000088", 0, 0)]



# Game menu


screen game_menu():
    key "mousedown_3" action Return()


    style_prefix "game_menu" tag menu

    default tp = Tooltip("")
    $ bgm_title = get_current_bgm_title()

    
    
        
        

    add "gui/nvl.png"

    frame:
        background "gui/game_frames/notebook_frame.png"
        align (0.10, 0.3)
        xysize (567, 564)

        textbutton "Glossary" action ShowMenu("tips_page") xoffset 100 yoffset 100

        default current_chapter = None


    # use menu_navigation(config.menu_navigation_align)

    #     window:
    #         background None
    #         align (0.5, 0.5)
    #         xmaximum 250
    #         ymaximum 300
    #         padding (0, 0, 0 , 0)

    #         showif tp.value != "":
    #             text tp.value at game_menu_tooltip_appear:
    #                 style_suffix "tooltip_text"

    vbox style_suffix "chaptername_vbox":

        text save_name style_suffix "chaptername_text"

        hbox:
            spacing 15
            xalign 0.5

            add get_time_icon() xsize 60 ysize 60 xoffset -5 yoffset 0

            text "[gameinfo_date]" style_suffix "date_text"

    on "show" action [Preference("auto-forward", "disable"), SetField(config, "skipping", None)]

    use info_panel(_("BGM"), get_current_bgm_title(), "gui/game_menu_icons/audio-playlist_w.png", (0.90, 0.35))

    use info_panel(_("Location"), get_location_name(), "gui/game_menu_icons/map_w.png", (0.90, 0.525))

    use info_panel(_("Tip"), get_location_tip(), "gui/game_menu_icons/comment-bubble_w.png", (0.90, 0.730))

    # use story_info()
init -2:

    style game_menu_chaptername_vbox:
        spacing 15
        align (0.85, 0.15)

    style game_menu_chaptername_text:
        font "fonts/Poppins-Light.ttf"
        size 48
        xalign 0.5
        xoffset 0

    style game_menu_date_text:
        font "fonts/Poppins-Light.ttf"
        size 30
        line_spacing 0
        line_leading 0
        yoffset 7.5

    style game_menu_tooltip_text:
        font "fonts/Poppins-Light.ttf"
        align (0.5, 0.5)
        size 18
        color "#fff"
        outlines [(1, "#00000099", 0, 0)]
        kerning 0
        line_spacing 0
        line_leading 0
        layout "subtitle"
        text_align 0.5

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

style game_menu_navigation_frame:
    xsize 250 
    yfill 0

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 1920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

screen hud():

    zorder 100
    style_prefix "hud"

    frame at hud_appear:
        background Frame("gui/nvl.png", 40)
        align (1.0, 0.05)
        left_padding 40
        right_padding 30

        has hbox:
            spacing 10

        add get_time_icon() yalign 0.5 xysize(50, 50)
        text "[gameinfo_date]" size 30 yoffset 5

    timer 5 action Hide('hud')

init -2:

    style hud_text is notify_text

# menu page title


default seen_chapters = None



screen menu_page_title(title, alignment):

    style_prefix "menu_page_title"

    frame:
        align alignment
        background None
        # background "gui/nvl.png"
        xysize (312, 122)
        right_padding 20

        

init -2:

    style menu_page_title_label_text is text:
        font "fonts/Poppins-Light.ttf"
        size 34


init -2:

    style chapter_name_label_text is cardbook_character_name_label_text

    style chapter_buttons_frame:
        # background Frame("gui/nvl.png", 4, 4)
        background None
        xoffset 10
        yoffset -50
        xsize 450
        ysize 535

        right_padding 1
        left_padding 1
        ypadding 1

    style chapter_buttons_button is cardbook_button

    style chapter_buttons_text is cardbook_button_text:
        text_align 0.5

    style chapter_contents_frame:
        background None
        yoffset -50
        xsize 500
        ysize 535

    style chapter_contents_window:
        background None
        margin (0, 0)
        padding (20, 0)
        yoffset -250

    style chapter_contents_text:
        font "fonts/Poppins-Light.ttf"
        color "#000000"
        size 25
        spacing 24
        outlines []

screen menu_navigation(alignment):

    # style_prefix "menu_navigation"

    frame:
        align alignment
        background None

        if not main_menu:
            hbox:
                spacing 10


                textbutton _("close") action Return()
        else:
            textbutton _("back") action Return()


    key "game_menu" action Return()

init -2:

    style menu_navigation_button is menu_button:
        xsize 130
        ysize 30
        selected_background Frame("gui/button01_idle.png", 4, 4)

    style menu_navigation_button_text is menu_button_text:
        size 16


# screen cardbook


# screen cardbook():
#     tag menu


#     default current_character = None
#     default current_card = None

#     $ cards_count = get_character_cards_count(current_character)


#     add "gui/cardbook_bg.png"


#     use menu_page_title(_("カードブック"), (1.0, 0.03))


#     if current_character:
#         label "Numeral " + character_info[current_character]["numeral"] style "cardbook_character_name_label":
#             align (0.05, 0.06)


#     grid 2 6:
#         style_prefix "cardbook_characters"
#         xalign 0.04
#         yalign 0.55
#         spacing 10


#         button:
#             idle_background "gui/thumb_rnk_idle.png"
#             selected_background "gui/thumb_rnk_selected.png"
#             hover_background "gui/thumb_rnk_hover.png"

#             action [SetScreenVariable("current_card", None),
#                     SetScreenVariable("current_character", "rnk"),
#                     SelectedIf(current_character == "rnk"),
#                     SensitiveIf(current_character != "rnk" and gameinfo_cardbook_rnk_unlocked)]


#         button:
#             idle_background "gui/thumb_cnh_idle.png"
#             selected_background "gui/thumb_cnh_selected.png"
#             hover_background "gui/thumb_cnh_hover.png"

#             action [SetScreenVariable("current_card", None),
#                     SetScreenVariable("current_character", "cnh"),
#                     SelectedIf(current_character == "cnh"),
#                     SensitiveIf(current_character != "cnh" and gameinfo_cardbook_cnh_unlocked)]


#         button:
#             idle_background "gui/thumb_mhr_idle.png"
#             selected_background "gui/thumb_mhr_selected.png"
#             hover_background "gui/thumb_mhr_hover.png"

#             action [SetScreenVariable("current_card", None),
#                     SetScreenVariable("current_character", "mhr"),
#                     SelectedIf(current_character == "mhr"),
#                     SensitiveIf(current_character != "mhr" and gameinfo_cardbook_mhr_unlocked)]


#         button:
#             idle_background "gui/thumb_kik_idle.png"
#             selected_background "gui/thumb_kik_selected.png"
#             hover_background "gui/thumb_kik_hover.png"

#             action [SetScreenVariable("current_card", None),
#                     SetScreenVariable("current_character", "kik"),
#                     SelectedIf(current_character == "kik"),
#                     SensitiveIf(current_character != "kik" and gameinfo_cardbook_kik_unlocked)]


#         button:
#             idle_background "gui/thumb_fed_idle.png"
#             selected_background "gui/thumb_fed_selected.png"
#             hover_background "gui/thumb_fed_hover.png"

#             action [SetScreenVariable("current_card", None),
#                     SetScreenVariable("current_character", "fed"),
#                     SelectedIf(current_character == "fed"),
#                     SensitiveIf(current_character != "fed" and gameinfo_cardbook_fed_unlocked)]


#         button:
#             idle_background "gui/thumb_sca_idle.png"
#             selected_background "gui/thumb_sca_selected.png"
#             hover_background "gui/thumb_sca_hover.png"

#             action [SetScreenVariable("current_card", None),
#                     SetScreenVariable("current_character", "sca"),
#                     SelectedIf(current_character == "sca"),
#                     SensitiveIf(current_character != "sca" and gameinfo_cardbook_sca_unlocked)]


#         button:
#             idle_background "gui/thumb_yuu_idle.png"
#             selected_background "gui/thumb_yuu_selected.png"
#             hover_background "gui/thumb_yuu_hover.png"

#             action [SetScreenVariable("current_card", None),
#                     SetScreenVariable("current_character", "yuu"),
#                     SelectedIf(current_character == "yuu"),
#                     SensitiveIf(current_character != "yuu" and gameinfo_cardbook_yuu_unlocked)]


#         button:
#             idle_background "gui/thumb_son_idle.png"
#             selected_background "gui/thumb_son_selected.png"
#             hover_background "gui/thumb_son_hover.png"

#             action [SetScreenVariable("current_card", None),
#                     SetScreenVariable("current_character", "son"),
#                     SelectedIf(current_character == "son"),
#                     SensitiveIf(current_character != "son" and gameinfo_cardbook_son_unlocked)]


#         button:
#             idle_background "gui/thumb_sig_idle.png"
#             selected_background "gui/thumb_sig_selected.png"
#             hover_background "gui/thumb_sig_hover.png"

#             action [SetScreenVariable("current_card", None),
#                     SetScreenVariable("current_character", "sig"),
#                     SelectedIf(current_character == "sig"),
#                     SensitiveIf(current_character != "sig" and gameinfo_cardbook_sig_unlocked)]


#         button:
#             idle_background "gui/thumb_ode_idle.png"
#             selected_background "gui/thumb_ode_selected.png"
#             hover_background "gui/thumb_ode_hover.png"

#             action [SetScreenVariable("current_card", None),
#                     SetScreenVariable("current_character", "ode"),
#                     SelectedIf(current_character == "ode"),
#                     SensitiveIf(current_character != "ode" and gameinfo_cardbook_ode_unlocked)]


#         button:
#             idle_background "gui/thumb_cha_idle.png"
#             selected_background "gui/thumb_cha_selected.png"
#             hover_background "gui/thumb_cha_hover.png"


#             action [SetScreenVariable("current_card", None),
#                     SetScreenVariable("current_character", "cha"),
#                     SelectedIf(current_character == "cha"),
#                     SensitiveIf(current_character != "cha" and gameinfo_cardbook_cha_unlocked)]


#         button:
#             idle_background "gui/thumb_aln_idle.png"
#             selected_background "gui/thumb_aln_selected.png"
#             hover_background "gui/thumb_aln_hover.png"

#             action [SetScreenVariable("current_card", None),
#                     SetScreenVariable("current_character", "aln"),
#                     SelectedIf(current_character == "aln"),
#                     SensitiveIf(current_character != "aln" and gameinfo_cardbook_aln_unlocked)]

#     frame:
#         background Frame("gui/frame.png", 4, 4)
#         xsize 180
#         ysize 506

#         xalign 0.23
#         yalign 0.55

#         right_padding 1
#         left_padding 1
#         ypadding 1

#         has vpgrid:
#             cols 1
#             xfill True
#             spacing 0

#         if current_character:

#             if cards_count > 0:


#                 if cards_count > 12:
#                     scrollbars "vertical"
#                     mousewheel True
#                     draggable False

#                 for obj in sorted(get_character_cards(current_character), key = lambda x: cards[x]["order"]):
#                     button:
#                         style "cardbook_button"
#                         hbox:
#                             spacing 0
#                             align (0.0, 0.5)
#                             text cards[obj]["title"]["chara"] style "cardbook_button_text"
#                             text " - " style "cardbook_button_text"
#                             text cards[obj]["title"]["type"] style "cardbook_button_text"

#                         action [SetScreenVariable("current_card", cards[obj]), SensitiveIf(current_card != cards[obj])]






#     if current_character:

#         window:
#             style_prefix "cardbook_card"
#             background current_card and "gui/card_front.png" or "gui/card_back.png"
#             xysize (213, 400)
#             align (0.7, 0.55)
#             margin (0, 0)
#             padding (10, 10)

#             if current_card:

#                 label current_card["title"]["chara"]:
#                     align (0.5, 0.01)

#                 text current_card["desc"]:
#                     align (0.5, 0.5)

#                 label current_card["title"]["type"]:
#                     align (0.5, 0.99)


#     use menu_navigation(config.menu_navigation_align)

#     on "replace" action Function(grant_achievement, "open_cardbook")

# init -2:


#     style cardbook_character_name_label_text:
#         font "gui/fonts/NotoSerifCJKjp-Medium.otf"

#         text_align 0.0
#         size 46

#     style cardbook_characters_button:
#         xysize (76, 76)
#         insensitive_background "gui/thumb_unk.png"

#     style cardbook_button:
#         ysize 40
#         xfill True
#         background None
#         hover_background "#74040488"
#         selected_background "#4b4b4b88"

#     style cardbook_button_text:
#         font "gui/fonts/NotoSerifCJKjp-Light.otf"
#         size 16
#         selected_color "#fff"





#     style cardbook_card_text:
#         font "gui/fonts/NotoSerifCJKjp-Light.otf"
#         color "#000"
#         size 18
#         text_align 0.5

#     style cardbook_card_label_text is cardbook_text:
#         font "gui/fonts/NotoSerifCJKjp-SemiBold.otf"
#         color "#000"
#         size 22
#         text_align 0.5


# default seen_chapters = None

## Load and Save screens #######################################################

style text_hover:
    color "#ffffff"
    hover_color "#4b4b4b"

init python:
    config.thumbnail_width = 1920
    config.thumbnail_height = 1080

screen save():
    add "flickering_light" 
    add "title_art"
    key "mousedown_3" action Return() 
    text "SAVE" text_align 0.5 xalign 0.75 yalign 0.125 xoffset 355 size 80 font "fonts/Poppins-Light.ttf"
    tag menu
    use file_picker

screen load():
    add "flickering_light" 
    add "title_art"
    key "mousedown_3" action Return() 
    text "LOAD" text_align 0.5 xalign 0.75 yalign 0.125 xoffset 355 size 80 font "fonts/Poppins-Light.ttf"

    tag menu
    use file_picker



screen file_picker():
    
    default tt = Tooltip((Null(), "", "", ""))
    
    frame:
        background "gui/game_frames/load_frame_with_slot_frame.png"
        xalign 0.5
        yalign 0.5
        xoffset 320
        yoffset 7.5

        grid gui.file_slot_cols gui.file_slot_rows:
     
            yoffset -10
            xoffset 2
   
            xspacing 2
            yspacing 2
    
            

            
            for slot in range(gui.file_slot_cols * gui.file_slot_rows):
            # for slot in range(1, 7):
                # Each file slot is a button.
                # $ file_name = FileSlotName(i, 30)
                # $ file_time = FileTime(i)
                # $ save_name = FileSaveName(i)
                $ slot_foot = FileSlotName(slot + 1, 6)
                if len(slot_foot) == 1:
                    $ slot_foot = '0' + slot_foot
                # if len(slot_foot) < 3:
                #     $ slot_foot = '0' + slot_foot
                # $ slot_foot = "No " + slot_foot


                vbox:

                    button:
                 
                        xoffset 2.5
                        yoffset 3
                        xysize (374, 307)
                        background None
                        hover_background "gui/game_frames/bg_slot.png"
                        action FileAction(slot)
                        # hovered tt.Action((FileScreenshot(slot), slot_foot, file_time, save_name))
                        vbox:
                            xoffset 18
                            yoffset 12.5
                            # style_prefix "text_hover"
                            add FileScreenshot(slot)  size(325, 190)
                            frame:
                                background None
                                text FileTime(slot, format=_("{#file_time}%b/%d/%Y"), empty=_("No Data")):
                                    xalign 0 size 25 yoffset 0 hover_color "#000000" font "fonts/Poppins-Light.ttf"
                                text slot_foot xalign 0.89 size 25 hover_color "#000000" font "fonts/Poppins-Light.ttf"
                                text FileSaveName(slot) xalign 0 yoffset 35 size 25  hover_color "#000000"    
                            # add "gui/number_slot_small.png" xalign 0.01 yoffset -240 xoffset -0
                            
                            
                        xfill True

                        
                        # Add the screenshot.
                        # if file_time:
                        #     add FileScreenshot(slot) xalign .5 xysize(300, 180)
                        #     # xsize 200 ysize 125
                        # else:
                        #     add Solid("#900", xysize=(325, 190)) # HERE THE IMAGE OF THE EMPTY SLOT

                        key "save_delete" action FileDelete(slot)


    add "gui/bar/stick_fill.png" xalign 0.6170 yalign 0.1725 yoffset 1.5 xoffset -88
    add "gui/bar/stick_fill.png" xalign 0.6170 yalign 0.1725 yoffset 1.5 xoffset -166
    hbox:
        
        xalign 0.6170
        yalign 0.1725

        xoffset 1
        yoffset 1.5
        spacing 1
        hbox:
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/one.png"
                hover "gui/gui_buttons/GUI save_load_pages/one_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/one_selected.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/one_selected.png"
                action FilePage(1)
        hbox:
            xoffset -1
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/two.png"
                hover "gui/gui_buttons/GUI save_load_pages/two_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/two_selected.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/two_selected.png"
                action FilePage(2)
        hbox:
            xoffset -2
            
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/three.png"
                hover "gui/gui_buttons/GUI save_load_pages/three_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/three_selected.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/three_selected.png"
                action FilePage(3)
        hbox:
            xoffset -3
           
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/four.png"
                hover "gui/gui_buttons/GUI save_load_pages/four_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/four_selected.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/four_selected.png"
                action FilePage(4)
        hbox:
            xoffset -2
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/five.png"
                hover "gui/gui_buttons/GUI save_load_pages/five_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/five_selected.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/five_selected.png"
                action FilePage(5)
        hbox:
            xoffset 0
    
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/six.png"
                hover "gui/gui_buttons/GUI save_load_pages/six_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/six_selected.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/six_selected.png"
                action FilePage(6)
        hbox:
            xoffset -1
           
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/seven.png"
                hover "gui/gui_buttons/GUI save_load_pages/seven_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/seven_selected.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/seven_selected.png"
                action FilePage(7)
        hbox:
            xoffset -2
           
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/eight.png"
                hover "gui/gui_buttons/GUI save_load_pages/eight_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/eight_selected.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/eight_selected.png"
                action FilePage(8)
        hbox:
            xoffset -3
            
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/nine.png"
                hover "gui/gui_buttons/GUI save_load_pages/nine_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/nine_selected.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/nine_selected.png"
                action FilePage(9)
        hbox:
            xoffset -4
           
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/ten.png"
                hover "gui/gui_buttons/GUI save_load_pages/ten_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/ten_selected.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/ten_selected.png"
                action FilePage(10)
    frame:
        xsize 850
        ysize 100
        xalign 0.5
        yalign 0.9
        xoffset 322.5
        background None
        hbox:
            spacing 50


            textbutton "SAVE" action ShowMenu('save')
            textbutton "LOAD" action ShowMenu('load')
            textbutton "SETTINGS" action ShowMenu('preferences') 
            textbutton "TITLE" action MainMenu()
            textbutton "QUIT" action Quit(True)
            textbutton "BACK" action Return()
                



style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

style pref_bar:
    yalign 0.5
    xysize(313, 27)
    # left_bar "gui/slot.png"
    # right_bar "gui/slot.png"

style text_speed:
    yalign 0.5
    xysize(600, 38)
    left_bar "gui/bar/Text.png"
    right_bar "gui/bar/Text_right.png"
    thumb "gui/thumb.png"

style auto_speed:
    yalign 0.5
    xysize(600, 38)
    left_bar "gui/bar/Auto.png"
    right_bar "gui/bar/Music_right.png"
    thumb "gui/thumb.png"

style music_volume:
    yalign 0.5
    xysize(600, 38)
    left_bar "gui/bar/Music.png"
    right_bar "gui/bar/Music_right.png"
    thumb "gui/thumb.png"

style sfx_volume:
    yalign 0.5
    xysize(600, 38)
    left_bar "gui/bar/Text.png"
    right_bar "gui/bar/Sfx_right.png"
    thumb "gui/thumb.png"

style bold_text:
    bold True

style hovered_text:
    background None
    hover_background "#c05d5d"


screen text_test():
    zorder 100
    frame:
        
        xalign 0.4975 yalign 0.55
        xoffset 28.5
        yoffset 22.5
        background None
        text "This is a test." slow_cps True color "#000000" yoffset -7.5 xoffset 10
        
        hbox:
            xsize 758
            text "This is a preview text." slow_cps True color "#ffffff" xoffset 810 yoffset 615 font "fonts/Poppins-Light.ttf"      
    timer 2.0 action Hide("text_test")

screen sound_settings():
    tag menu
    key "mousedown_3" action Return()   
    use settings_menu(_("Configurations"), scroll="viewport")
    hbox:
        style_prefix "mailbox_button"
        text "SETTINGS" size 80 color "#ffff" font "fonts/Poppins-Light.ttf" xoffset 1490.5 yoffset 125
    hbox:
        xsize 1000
        xoffset 202
        yoffset 5
        xalign 0.5
        yalign 0.1520
        spacing 0
        

        default mouse_clicked = False
        fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
            imagebutton:
                xoffset 54
                yoffset 175
                idle "gui/gui_buttons/GUI system_settings/system_idle.png"
                hover ("gui/gui_buttons/GUI system_settings/system_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/system_hovered.png")
                selected_idle "gui/gui_buttons/GUI system_settings/system_selected.png"
                selected_hover "gui/gui_buttons/GUI system_settings/system_selected.png"
                action ShowMenu("preferences")
            imagebutton:
                xoffset 211
                yoffset 175
                idle "gui/gui_buttons/GUI system_settings/text_idle.png"
                hover ("gui/gui_buttons/GUI system_settings/text_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/text_hovered.png")
                selected_idle "gui/gui_buttons/GUI system_settings/text_selected.png"
                selected_hover "gui/gui_buttons/GUI system_settings/text_selected.png"
                action ShowMenu("text_settings")
            imagebutton:
                xoffset 368.5
                yoffset 175
                idle "gui/gui_buttons/GUI system_settings/sound_idle.png"
                hover ("gui/gui_buttons/GUI system_settings/sound_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/sound_hovered.png")
                selected_idle "gui/gui_buttons/GUI system_settings/sound_selected.png"
                selected_hover "gui/gui_buttons/GUI system_settings/sound_selected.png"
                action ShowMenu("sound_settings")
    frame:
        background "gui/game_frames/settings_frame_wide.png"
        xoffset 716
        yoffset 230
        
        hbox:
            xalign 0.5
            yalign 0.5
            vbox:
                xoffset 75
                yoffset 55
                hbox:
                    text "MUSIC VOLUME" xalign 0.5 size 33 color "#ffffff"  
                hbox:
                    yoffset 50
                    text "SFX VOLUME" xalign 0.5 size 33 color "#ffffff"

            vbox:
                xalign 0.5
                yalign 0.5
                xoffset 223
                yoffset 56
                hbox:
                    yoffset -4
                    spacing 10
                    bar:
                        style "music_volume"
                        value Preference("music volume")
                hbox:
                    spacing 10
                    yoffset 55
                    bar:
                        style "sfx_volume"
                        value Preference("sound volume")
        
    frame:
        xsize 850
        ysize 100
        xalign 0.5
        yalign 0.9
        xoffset 322.5
        background None
        hbox:
            spacing 50


            textbutton "SAVE" action ShowMenu('save')
            textbutton "LOAD" action ShowMenu('load')
            textbutton "SETTINGS" action ShowMenu('preferences') 
            textbutton "TITLE" action MainMenu()
            textbutton "QUIT" action Quit(True)
            textbutton "BACK" action Return()

screen text_settings():
    tag menu
    key "mousedown_3" action Return()   
    use settings_menu(_("Configurations"), scroll="viewport")
    hbox:
        style_prefix "mailbox_button"
        text "SETTINGS" size 80 color "#ffff" font "fonts/Poppins-Light.ttf" xoffset 1490.5 yoffset 125
    hbox:
        xsize 1000
        xoffset 202
        yoffset 5
        xalign 0.5
        yalign 0.1520
        spacing 0

        default mouse_clicked = False
        fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
            imagebutton:
                xoffset 54
                yoffset 175
                idle "gui/gui_buttons/GUI system_settings/system_idle.png"
                hover ("gui/gui_buttons/GUI system_settings/system_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/system_hovered.png")
                selected_idle "gui/gui_buttons/GUI system_settings/system_selected.png"
                selected_hover "gui/gui_buttons/GUI system_settings/system_selected.png"
                action ShowMenu("preferences")
            imagebutton:
                xoffset 211
                yoffset 175
                idle "gui/gui_buttons/GUI system_settings/text_idle.png"
                hover ("gui/gui_buttons/GUI system_settings/text_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/text_hovered.png")
                selected_idle "gui/gui_buttons/GUI system_settings/text_selected.png"
                selected_hover "gui/gui_buttons/GUI system_settings/text_selected.png"
                action ShowMenu("text_settings")
            imagebutton:
                xoffset 368.5

                yoffset 175
                idle "gui/gui_buttons/GUI system_settings/sound_idle.png"
                hover ("gui/gui_buttons/GUI system_settings/sound_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/sound_hovered.png")
                selected_idle "gui/gui_buttons/GUI system_settings/sound_selected.png"
                selected_hover "gui/gui_buttons/GUI system_settings/sound_selected.png"
                action ShowMenu("sound_settings")
    frame:
        background "gui/game_frames/settings_frame_wide.png"
        xoffset 716
        yoffset 230

        hbox:
            xalign 0.5
            yalign 0.5
            vbox:

                xoffset 75
                yoffset 55
                hbox:
                    
                    text "TEXTBOX OPACITY" xalign 0.5 size 33 color "#ffffff"        
                hbox:
                    yoffset 50
                    text "TEXT SPEED" xalign 0.5 size 33 color "#ffffff"
                hbox:
                    yoffset 100
                    text "AUTOPLAY SPEED" xalign 0.5 size 33 color "#ffffff"
            vbox:
                xalign 0.5
                yalign 0.5
                xoffset 185
                yoffset -405
                hbox:
                    spacing 10
                    yoffset -7.5
                    bar:
                        style "sfx_volume" 
                        value FieldValue(persistent, "window_opacity", range=1.0)
                hbox:
                    spacing 10
                    yoffset 52.5
                    bar:
                        style "text_speed"
                        value Preference("text speed")
                hbox:
                    spacing 10
                    yoffset 107.5
                    bar:
                        style "auto_speed"
                        value Preference("auto-forward time")

            hbox:

                xoffset -750
                yoffset 225
                xsize 250
                ysize 50
                spacing 150
                frame:
                    background None
                    add Transform(Frame("gui/preview_textbox.png", xalign=0.5, yalign=0.5, ysize=167, xsize=1000, xoffset= 100, yoffset= 75), alpha=persistent.window_opacity)

                    hbox:
                        xsize 841
                        ysize 217
                        text "_______________________________________" color "#ffffff" yoffset 25 xoffset -100
                    hbox:
                        xsize 841
                        ysize 217
                        text "_______________________________________" color "#ffffff" yoffset 75 xoffset -100

                    xsize 500
                    xoffset 87.5
                    yoffset 155
            hbox:
                xsize 500
                default mouse_clicked = False
                fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
                    imagebutton:
                        yoffset 343 
                        xoffset -1313
                        idle "gui/gui_buttons/GUI system_settings/preview_textspeed_idle.png"
                        hover ("gui/gui_buttons/GUI system_settings/preview_textspeed_selected.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/preview_textspeed_clicked.png")
                        selected "gui/gui_buttons/GUI system_settings/preview_textspeed_selected.png"
                        action Show("text_test") 

    frame:
        xsize 850
        ysize 100
        xalign 0.5
        yalign 0.9
        xoffset 322.5
        background None
        hbox:
            spacing 50


            textbutton "SAVE" action ShowMenu('save')
            textbutton "LOAD" action ShowMenu('load')
            textbutton "SETTINGS" action ShowMenu('preferences') 
            textbutton "TITLE" action MainMenu()
            textbutton "QUIT" action Quit(True)
            textbutton "BACK" action Return()
                

screen preferences():

    tag menu
    key "mousedown_3" action Return()   
    use settings_menu(_("Configurations"), scroll="viewport")

    add "flickering_light"
    add "title_art"
    hbox:
        style_prefix "mailbox_button"
        text "SETTINGS" size 80 color "#ffff" font "fonts/Poppins-Light.ttf" xoffset 1490.5 yoffset 125
    hbox:
        xsize 1000
        xoffset 202
        yoffset 5
        xalign 0.5
        yalign 0.1520
        spacing 0
        


        default mouse_clicked = False
        fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
            imagebutton:
                xoffset 54
                yoffset 175
                idle "gui/gui_buttons/GUI system_settings/system_idle.png"
                hover ("gui/gui_buttons/GUI system_settings/system_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/system_hovered.png")
                selected_idle "gui/gui_buttons/GUI system_settings/system_selected.png"
                selected_hover "gui/gui_buttons/GUI system_settings/system_selected.png"
                action ShowMenu("preferences")
            imagebutton:
                xoffset 211
                yoffset 175
                idle "gui/gui_buttons/GUI system_settings/text_idle.png"
                hover ("gui/gui_buttons/GUI system_settings/text_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/text_hovered.png")
                selected_idle "gui/gui_buttons/GUI system_settings/text_selected.png"
                selected_hover "gui/gui_buttons/GUI system_settings/text_selected.png"
                action ShowMenu("text_settings")
            imagebutton:
                xoffset 368.5

                yoffset 175
                idle "gui/gui_buttons/GUI system_settings/sound_idle.png"
                hover ("gui/gui_buttons/GUI system_settings/sound_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/sound_hovered.png")
                selected_idle "gui/gui_buttons/GUI system_settings/sound_selected.png"
                selected_hover "gui/gui_buttons/GUI system_settings/sound_selected.png"
                action ShowMenu("sound_settings")
    frame:
        
        background "gui/game_frames/settings_frame_wide.png"
        xalign 0.5
        yalign 0.5
        yoffset -249.5
        xoffset 71
        style_prefix "mailbox_button"

        
        
        hbox:
            xalign 0.5
            yalign 0.5
            vbox:

                xoffset 75
                yoffset 55
                hbox:
                    text "DISPLAY WINDOW" xalign 0.5 yoffset -5 color "#ffffff"
                hbox:
                    yoffset 32.5
                    text "SKIP MODE" xalign 0.5 yoffset 20 color "#ffffff"
            vbox:
                xalign 0.5
                yalign 0.5

                
                hbox:
                    xalign 0.5
                    yalign 0.5
                    yoffset 22.5
                    xoffset 250
                    xsize 200
                    ysize 50
                    spacing 150
                    hbox:
                        default mouse_clicked = False
                        fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
                
                            imagebutton:
                                idle "gui/gui_buttons/GUI system_settings/text_windowed.png" xalign 0.5 yalign 0.5 yoffset 27.5
                                hover ("gui/gui_buttons/GUI system_settings/selected_windowed_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/selected_windowed_hovered.png")
                                selected_idle "gui/gui_buttons/GUI system_settings/selected_windowed.png"
                                selected_hover ("gui/gui_buttons/GUI system_settings/selected_windowed_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/selected_windowed.png")
                                action Preference("display", "window")

                    hbox:
                        xoffset 50
                        default mouse_clicked = False
                        fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
                
                            imagebutton:
                                idle "gui/gui_buttons/GUI system_settings/text_fullscreen.png" xalign 0.5 yalign 0.5 yoffset 27.5
                                hover ("gui/gui_buttons/GUI system_settings/selected_fullscreen_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/selected_fullscreen_hovered.png")
                                selected_idle "gui/gui_buttons/GUI system_settings/selected_fullscreen.png"
                                selected_hover ("gui/gui_buttons/GUI system_settings/selected_fullscreen_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/selected_fullscreen.png")
                                action Preference("display", "fullscreen")

                hbox: 
                    xalign 0.5
                    yalign 0.5
                    yoffset 80
                    xoffset 250
                    xsize 200
                    ysize 50
                    spacing 150
                    hbox:
                        default mouse_clicked = False
                        fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
                
                            imagebutton:
                                idle "gui/gui_buttons/GUI system_settings/text_skipall.png" xalign 0.5 yalign 0.5 yoffset 27.5
                                hover ("gui/gui_buttons/GUI system_settings/selected_skipall_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/selected_skipall_hovered.png")
                                selected_idle "gui/gui_buttons/GUI system_settings/selected_skipall.png"
                                selected_hover ("gui/gui_buttons/GUI system_settings/selected_skipall_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/selected_skipall.png")
                                action Preference("skip", "all")
                    hbox:
                        xoffset 50
                        default mouse_clicked = False
                        fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
                
                            imagebutton:
                                idle "gui/gui_buttons/GUI system_settings/text_skipseen.png" xalign 0.5 yalign 0.5 yoffset 27.5
                                hover ("gui/gui_buttons/GUI system_settings/selected_skipseen_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/selected_skipseen_hovered.png")
                                selected_idle "gui/gui_buttons/GUI system_settings/selected_skipseen.png"
                                selected_hover ("gui/gui_buttons/GUI system_settings/selected_skipseen_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/selected_skipseen.png")
                                action Preference("skip", "seen")

    hbox:
        xalign 0.5
        yalign 0.5
        xoffset 725
        yoffset 250
        textbutton "Reset Settings" action ResetToDefaults              

    frame:
        xsize 850
        ysize 100
        xalign 0.5
        yalign 0.9
        xoffset 322.5
        background None
        hbox:
            spacing 50


            textbutton "SAVE" action ShowMenu('save')
            textbutton "LOAD" action ShowMenu('load')
            textbutton "SETTINGS" action ShowMenu('preferences') 
            textbutton "TITLE" action MainMenu()
            textbutton "QUIT" action Quit(True)
            textbutton "BACK" action Return()
                        
style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu
    key "mousedown_3" action Return()
    predict False
    frame:
        background Image("gui/nvl.png")
    frame:
        # background Image("gui/nvl.png")
        background None
        # background None
        # style_prefix "history"

        # left_margin 200
        # right_margin 200
        # top_margin 50
        # bottom_margin 50

        # left_padding 0
        # right_padding 0
        # top_padding 50
        # bottom_padding 100

        vpgrid:
            yoffset 90
            ysize 900
            cols 1
            yinitial 1.0

            draggable True
            mousewheel True
            scrollbars "vertical"

            for h in _history_list:

                window:
                    ysize 300
                    ## This lays things out properly if history_height is None.
                    has fixed:
                        yfit True
                    
                    if h.who:
                        
                        label h.who:
                            style "history_name"
                            xoffset -25
                            yoffset 50
                            ## Take the color of the who text from the Character, if
                            ## set.
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what xoffset 125 yoffset 100 xsize 1580

            if not _history_list:

                text "The dialogue history is empty." line_spacing 10
                ## Adding line_spacing prevents the bottom of the text
                ## from getting cut off. Adjust when replacing the
                ## default fonts.

        textbutton _("Return") action Return() text_size 50 xalign 0.9 yalign 0.9 yoffset 100 xoffset 125
        text "History" size 100 yoffset -30 xalign 0.5

## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################

screen confirm(message, yes_action, no_action):

    modal True

    zorder 200

    style_prefix "confirm"
    
    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/nvl.png", "gui/game_frame/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    font "DejaVuSans.ttf"


## Notify screen ###############################################################

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.

define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    justify True
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")
