﻿################################################################################
## Initialization
################################################################################

init offset = -1



################################################################################
## Styles
################################################################################

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
    # padding gui.frame_borders.padding
    bottom_padding 10
    top_padding 10
    # background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
    background Frame("gui/extra/frame.png", gui.frame_borders, tile=gui.frame_tile)


################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"
    # window background Transform(Frame("gui/textbox.png",0.5,0.5), alpha=persistent.window_opacity)
    # window background Transform(Frame("gui/bar/Auto.png",x,y), alpha=persistent.window_opacity)
    key "mousedown_4" action ShowMenu("history")
    key "mouseup_3" action ShowMenu("game_menu2")
    
    window:
        background Transform(Frame("gui/textbox.png", xalign=50, yoffset=-100, ysize=500), alpha=persistent.window_opacity)
        id "window"
        yalign 0.956
        ysize 175
        # if who is not None:

        #     # window:
        #     #     id "namebox"
        #     #     style "namebox"
        #         text who id "who"
        if who is not None:
            hbox:
                xalign 0.5
                yalign 0.5
                yoffset -150
                text who id "who"
        hbox:
            text what id "what"

    
    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 0.5


## Make the namebox available for styling through the Character object.
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
    # xoffset 330
    # yoffset -7.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    # size 22.5
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

style nvl_dialogue:
    properties gui.text_properties("dialogue")

    


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

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
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

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
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu(): 
    

    # Ensure this appears on top of other screens.
    zorder 100
    
    if quick_menu:
        frame:
            background None
            xfill 0.5 
            yalign 0.9999
            yoffset 10
            
            
            hbox:
                # style_prefix "quick"
                # add "gui/textbox.png"
                xalign 0.975
                yalign 0.5
                spacing 0
                frame:
                    background "gui/navbar.png"
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
                        
                # textbutton _("Save") action ShowMenu('save')
                # textbutton _("Load") action ShowMenu('load')
                # textbutton _("Auto") action Preference("auto-forward", "toggle")
                # textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
                # textbutton _("Logs") action ShowMenu('history')
                # textbutton _("Settings") action ShowMenu('preferences')
                
    # screen quick_menu(): 
    
    # # Ensure this appears on top of other screens.
    # zorder 100
    
    # if quick_menu:
        
    #         hbox:
    #             style_prefix "quick"

    #         imagebutton:
    #             idle "gui/save_idle.png"
    #             hover "gui/save_hover.png"
    #             action ShowMenu('save')
    #             xoffset 600
    #             yoffset 680
    #             #hovered Play("sound", "click.ogg")
                      
    #         imagebutton:
    #             idle "gui/load_idle.png"
    #             hover "gui/load_hover.png"
    #             action ShowMenu('load')
    #             xoffset 620
    #             yoffset 680
    #             #hovered Play("sound", "click.ogg")
                   
    #         imagebutton:
    #             idle "gui/auto_idle.png"
    #             hover "gui/auto_hover.png"
    #             action Preference("auto-forward", "toggle")
    #             xoffset 635
    #             yoffset 688
    #             #hovered Play("sound", "click.ogg")
                
    #         imagebutton:
    #             idle "gui/skip_idle.png"
    #             hover "gui/skip_hover.png"
    #             action Skip() alternate Skip(fast=True, confirm=True)
    #             xoffset 645
    #             yoffset 686
    #             #hovered Play("sound", "click.ogg")

    #         imagebutton:
    #             idle "gui/logs_idle.png"
    #             hover "gui/logs_hover.png"
    #             action ShowMenu('history')
    #             xoffset 655
    #             yoffset 686
    #             #hovered Play("sound", "click.ogg")
                
    #         imagebutton:
    #             idle "gui/settings_idle.png"
    #             hover "gui/settings_hover.png"
    #             action ShowMenu('preferences')
    #             xoffset 665
    #             yoffset 688
    #             #hovered Play("sound", "click.ogg")
                    


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")    

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:

        spacing 50
        xalign 0.8
        yalign 0.865
        box_layout u'horizontal'
        
        
        if main_menu:
           
            textbutton _("NEW GAME") action Start()
                

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("LOAD") action ShowMenu("load")

        textbutton _("SETTINGS") action ShowMenu("preferences")

        textbutton _("EXTRA") action ShowMenu("extra")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        if renpy.variant("pc"):

            textbutton _("QUIT") action Quit(confirm=not main_menu)


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
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    # add gui.main_menu_background xalign 0.5 yalign 0.3
    add "flickering_light"
    

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    # if gui.show_name:

    #     vbox:
    #         style "main_menu_vbox"

    #         text "[config.name!t]":
    #             style "main_menu_title"

    #         text "[config.version]":
    #             style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    # background "gui/overlay/main_menu.png"

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


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"
    
    
    add "flickering_light"

    frame:
        style "game_menu_outer_frame"

        hbox:
            
            ## Reserve space for the navigation section.
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
    # frame:
    #     xsize 850
    #     ysize 100
    #     xalign 0.5
    #     yalign 0.9
    #     xoffset 350
    #     background None
    #     hbox:
    #         spacing 50


    #         # textbutton "SAVE" action ShowMenu('save')
    #         textbutton "LOAD" action ShowMenu('load')
    #         textbutton "CONFIG" action ShowMenu('preferences') 
    #         textbutton "TITLE" action MainMenu()
    #         textbutton "QUIT" action Quit(True)
    #         textbutton "BACK" action Return()

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


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

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


init python:
    def ResetToDefaults():
        _preferences.text_cps = config.default_text_cps
        _preferences.afm_time = config.default_afm_time
        _preferences.afm_enable = config.default_afm_enable
        _preferences.set_volume('sfx', 1.0)
        _preferences.set_volume('music', 1.0)
        # persistent('window_opacity', 1.0)
        renpy.restart_interaction()

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
            # add Transform(Frame("gui/preview_textbox.png", xalign=0.5, yalign=0.5, ysize=222, xsize=444, xoffset=867.5, yoffset=542.5), alpha=persistent.window_opacity)
            text "This is a preview text." slow_cps True color "#ffffff" xoffset 810 yoffset 615 font "Poppins-Light.ttf"      
    timer 2.0 action Hide("text_test")
    # key "mouseup_1" action Hide("text_test") 

screen sound_settings():
    tag menu
    key "mousedown_3" action Return()   
    use game_menu(_("Configurations"), scroll="viewport")
    hbox:
        style_prefix "mailbox_button"
        text "SETTINGS" size 80 color "#ffff" font "Poppins-Light.ttf" xoffset 1490.5 yoffset 125
    hbox:
        xsize 1000
        xoffset 202
        yoffset 5
        xalign 0.5
        yalign 0.1520
        spacing 0
        # text "CONFIGURATIONS" xoffset 975 yoffset 15 size 40
        # imagebutton:
    #             idle "gui/gui_buttons/GUI save_load_pages/nine.png"
    #             hover "gui/gui_buttons/GUI save_load_pages/selected_ninebutton_hovered.png"
    #             selected_idle "gui/gui_buttons/GUI save_load_pages/selected_ninebutton.png"
    #             selected_hover "gui/gui_buttons/GUI save_load_pages/selected_ninebutton.png"
    #             action FilePage(9)

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
            # textbutton "SYSTEM" action ShowMenu("preferences") xoffset 150
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
                # xoffset 54 + 47.5
                yoffset 175
                idle "gui/gui_buttons/GUI system_settings/sound_idle.png"
                hover ("gui/gui_buttons/GUI system_settings/sound_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/sound_hovered.png")
                selected_idle "gui/gui_buttons/GUI system_settings/sound_selected.png"
                selected_hover "gui/gui_buttons/GUI system_settings/sound_selected.png"
                action ShowMenu("sound_settings")
    frame:
        background "gui/settings_frame_wide.png"
        xoffset 716
        yoffset 230
        # xalign 0.5
        # yalign 0.5
        # # xalign 0.86
        # # yalign 0.35
        # xoffset 855
        # yoffset 229

        # style_prefix "mailbox_button"
        
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
                    yoffset 0
                    spacing 10
                    bar:
                        style "music_volume"
                        value Preference("music volume")
                hbox:
                    spacing 10
                    yoffset 50
                    bar:
                        style "sfx_volume"
                        value Preference("sound volume")
        
    # frame:
    #     xsize 850
    #     ysize 100
    #     xalign 0.5
    #     yalign 0.9
    #     xoffset 322.5
    #     background None
    #     hbox:
    #         spacing 50


    #         textbutton "SAVE" action ShowMenu('save')
    #         textbutton "LOAD" action ShowMenu('load')
    #         textbutton "SETTINGS" action ShowMenu('preferences') 
    #         textbutton "TITLE" action MainMenu()
    #         textbutton "QUIT" action Quit(True)
    #         textbutton "BACK" action Return()

screen text_settings():
    tag menu
    key "mousedown_3" action Return()   
    use game_menu(_("Configurations"), scroll="viewport")
    hbox:
        style_prefix "mailbox_button"
        text "SETTINGS" size 80 color "#ffff" font "Poppins-Light.ttf" xoffset 1490.5 yoffset 125
    hbox:
        xsize 1000
        xoffset 202
        yoffset 5
        xalign 0.5
        yalign 0.1520
        spacing 0
        # imagebutton:
    #             idle "gui/gui_buttons/GUI save_load_pages/nine.png"
    #             hover "gui/gui_buttons/GUI save_load_pages/selected_ninebutton_hovered.png"
    #             selected_idle "gui/gui_buttons/GUI save_load_pages/selected_ninebutton.png"
    #             selected_hover "gui/gui_buttons/GUI save_load_pages/selected_ninebutton.png"
    #             action FilePage(9)

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
            # textbutton "SYSTEM" action ShowMenu("preferences") xoffset 150
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
                # xoffset 54 + 47.5
                yoffset 175
                idle "gui/gui_buttons/GUI system_settings/sound_idle.png"
                hover ("gui/gui_buttons/GUI system_settings/sound_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/sound_hovered.png")
                selected_idle "gui/gui_buttons/GUI system_settings/sound_selected.png"
                selected_hover "gui/gui_buttons/GUI system_settings/sound_selected.png"
                action ShowMenu("sound_settings")
    frame:
        background "gui/settings_frame_wide.png"
        xoffset 716
        yoffset 230
        # xalign 0.5
        # yalign 0.5
        # xoffset 855
        # yoffset 229
        # xoffset 350
        
        hbox:
            xalign 0.5
            yalign 0.5
            vbox:
                # spacing 60
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
                # xalign 0.5
                # yalign 0.5
                # yoffset -25
                # xoffset -50
                xoffset -750
                yoffset 225
                xsize 250
                ysize 50
                spacing 150
                frame:
                    background None
                    add Transform(Frame("gui/preview_textbox.png", xalign=0.5, yalign=0.5, ysize=167, xsize=1000, xoffset= 100, yoffset= 75), alpha=persistent.window_opacity)
                    # background "gui/preview_textbox.png"
                    hbox:
                        xsize 841
                        ysize 217
                        text "_______________________________________" color "#ffffff" yoffset 25 xoffset -100
                    hbox:
                        xsize 841
                        ysize 217
                        text "_______________________________________" color "#ffffff" yoffset 75 xoffset -100
                        # if "text_test" == True:
                        #     text "None"
                        # if persistent.window_opacity > 0.5: 
                            
                        # else:
                        #     text "This is a textbox for textspeed, this is just a test dialogue for your mother and your whole ass family" color "#ffffff" yoffset -7.5 xoffset 15

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
                        idle "gui/preview_textspeed_idle.png"
                        hover ("gui/preview_textspeed_selected.png" if mouse_clicked else "gui/preview_textspeed_clicked.png")
                        selected "gui/preview_textspeed_selected.png"
                        action Show("text_test") 

    # frame:
    #     xsize 850
    #     ysize 100
    #     xalign 0.5
    #     yalign 0.9
    #     xoffset 2.5
    #     background None
    #     hbox:
    #         spacing 50


    #         textbutton "SAVE" action ShowMenu('save')
    #         textbutton "LOAD" action ShowMenu('load')
    #         textbutton "SETTINGS" action ShowMenu('preferences') 
    #         textbutton "TITLE" action MainMenu()
    #         textbutton "QUIT" action Quit(True)
    #         textbutton "BACK" action Return()
                

screen preferences():

    tag menu
    key "mousedown_3" action Return()   
    use game_menu(_("Configurations"), scroll="viewport")
    # show screen "text_test"
    add "flickering_light"
    hbox:
        style_prefix "mailbox_button"
        text "SETTINGS" size 80 color "#ffff" font "Poppins-Light.ttf" xoffset 1490.5 yoffset 125
    hbox:
        xsize 1000
        xoffset 202
        yoffset 5
        xalign 0.5
        yalign 0.1520
        spacing 0
        
        
        # imagebutton:
        #     idle "gui/gui_buttons/text_fullscreen.png" xalign 0.5 yalign 0.5 yoffset 27.5
        #     hover ("gui/gui_buttons/selected_fullscreen_clicked.png" if mouse_clicked else "gui/gui_buttons/selected_fullscreen_hovered.png")
        #     selected_idle "gui/gui_buttons/selected_fullscreen.png"
        #     selected_hover ("gui/gui_buttons/selected_fullscreen_clicked.png" if mouse_clicked else "gui/gui_buttons/selected_fullscreen.png")
        #     action Preference("display", "fullscreen")


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
            # textbutton "SYSTEM" action ShowMenu("preferences") xoffset 150
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
                # xoffset 54 + 47.5
                yoffset 175
                idle "gui/gui_buttons/GUI system_settings/sound_idle.png"
                hover ("gui/gui_buttons/GUI system_settings/sound_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/sound_hovered.png")
                selected_idle "gui/gui_buttons/GUI system_settings/sound_selected.png"
                selected_hover "gui/gui_buttons/GUI system_settings/sound_selected.png"
                action ShowMenu("sound_settings")
    frame:
        
        background "gui/settings_frame_wide.png"
        xalign 0.5
        yalign 0.5
        yoffset -249.5
        xoffset 71
        style_prefix "mailbox_button"
        # xoffset 350
        
        
        hbox:
            xalign 0.5
            yalign 0.5
            vbox:
                # spacing 25
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


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"
    
    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15
            xoffset 500
            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
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
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
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
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

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


## This transform is used to blink the arrows one after another.
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
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

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
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


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



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.

screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Continue") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 600
