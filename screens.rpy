

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

        
screen say(who, what, side_image=None, two_window=False):

    key "mousedown_4" action ShowMenu("history")
    key "mouseup_3" action ShowMenu("game_menu", transition= Dissolve(0.2))
    
    if not two_window:
        window:
            style_prefix "say"
            background Transform(Frame("gui/game_frames/textbox.png"), alpha=persistent.window_opacity)
            id "window"
            yalign 1.0
            ysize 285
            if who is not None:
                hbox:
                    xalign 0.5
                    yalign 0.5
                    yoffset -125
                    text who id "who" font "fonts/Poppins-Regular.ttf"
            hbox:
                text what id "what" yoffset 65 xoffset -170 font"fonts/Poppins-Regular.ttf"
       
    else:
        
        window:
            background Transform(Frame("gui/game_frames/textbox.png"), alpha=persistent.window_opacity)
            style_prefix "say"
            id "window"
            ysize 285
            has vbox

            fixed:
                ysize 34

                if who:
                    window:
                        style "say_who_window"
                        background Transform(Frame("gui/game_frames/name_box.png", yoffset = -87.5,xoffset= 0, ysize = 82, xsize = 481), alpha=persistent.window_opacity)
                        yoffset 16
                        xoffset 0
                        xalign 1.0
                        # if (len(_history_list) == 0) or (len(_history_list) > 0 and _history_list[-1].who != who):
                        #     at trans_say_label
                            
                        text who:
                            yoffset -75
                            id "who" xalign 0.5 xoffset -685 
                            font "fonts/Poppins-Regular.ttf"
                            # if (len(_history_list) == 0) or (len(_history_list) > 0 and _history_list[-1].who != who):
                            #     at trans_say_label
                                

            text what id "what" yoffset 25 xoffset -170 font "fonts/Poppins-Regular.ttf"
            
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0


    use quick_menu

    if renpy.in_rollback():

        key "mousedown_5" action RollForward()
    


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

    background Image("gui/game_frames/textbox.png", xalign=0.5, yalign=1.0)

# style namebox:
#     xpos gui.name_xpos
#     xanchor gui.name_xalign
#     xsize gui.namebox_width
#     ypos gui.name_ypos
#     ysize gui.namebox_height

#     background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
#     padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)

style say_dialogue:
    properties gui.text_properties("dialogue")
    justify False
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

screen quick_menu(trans = None): 
    
    zorder 100
    
    if quick_menu:
        frame at trans:
            background None
            xalign 0.99
            yalign 0.9999
            yoffset 10
            # yoffset 10
            
            
            hbox:
                # xalign 0.975
                # yalign 0.9
                spacing 0
                frame:
                    # background "gui/navbar.png"
                    background None
                    # yoffset -10
                    # xoffset -460
                    vbox:
                        spacing 5
                        # yoffset 7.5
                        # xoffset 110
                        # xoffset 550
                        imagebutton:
                            # xoffset 60
                            idle "gui/gui_buttons/GUI quick_buttons/auto_idle.png"
                            hover "gui/gui_buttons/GUI quick_buttons/auto_hover.png"
                            selected_idle "gui/gui_buttons/GUI quick_buttons/auto_hover.png"
                            action Preference("auto-forward", "toggle")
                        # textbutton: _("SKIP") action S
                        imagebutton:
                            # xoffset 30
                            idle "gui/gui_buttons/GUI quick_buttons/skip_idle.png"
                            hover "gui/gui_buttons/GUI quick_buttons/skip_hover.png"
                            selected_idle "gui/gui_buttons/GUI quick_buttons/skip_hover.png"
                            selected_background "gui/gui_buttons/GUI quick_buttons/skip_hover.png"
                            action Skip()
                        imagebutton:
                            idle "gui/gui_buttons/GUI quick_buttons/logs_idle.png"
                            hover "gui/gui_buttons/GUI quick_buttons/logs_hover.png"
                            action ShowMenu('history')
                        imagebutton:
                            # xoffset 90
                            idle "gui/gui_buttons/GUI quick_buttons/save_idle.png"
                            hover "gui/gui_buttons/GUI quick_buttons/save_hover.png"
                            action ShowMenu('save')
                        imagebutton:
                            # xoffset 80
                            idle "gui/gui_buttons/GUI quick_buttons/load_idle.png"
                            hover "gui/gui_buttons/GUI quick_buttons/load_hover.png"
                            action ShowMenu('load')
                        imagebutton:
                            # xoffset -20
                            idle "gui/gui_buttons/GUI quick_buttons/settings_idle.png"
                            hover "gui/gui_buttons/GUI quick_buttons/settings_hover.png"
                            action ShowMenu('preferences')
        hbox:
            xalign 0.89
            yalign 0.775
            xoffset 18

            imagebutton:
                idle "gui/gui_buttons/GUI quick_buttons/hide_idle.png"
                hover "gui/gui_buttons/GUI quick_buttons/hide_hover.png"
                selected "gui/gui_buttons/GUI quick_buttons/hide_hover.png"
                action HideInterface()
# init -2:

#     style quick_button is menu_button:
#         xysize (138, 24)
#         background None
#         hover_background "gui/quick_button_bg_hover.png"
#         selected_background "gui/quick_button_bg_hover.png"

#     style quick_button_text is menu_button_text:
#         font "gui/fonts/NotoSansCJKjp-Thin.otf"
#         size 13
#         outlines [(absolute(1), Color("#bbbbbb88"), absolute(0), absolute(0))]

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
        text "{size=195}R{/size}ainfall" size 150 xalign 0.785 yalign 0.25 font "fonts/Cinzel-Extrabold.ttf"
        # text "{size=50}T{/size}HE {size=50}U{/size}NBROKEN" size 35 xalign 0.5 yoffset -50 font "fonts/Cinzel-Extrabold.ttf"
        
        
        if main_menu:

            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/start_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/start_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/start_selected1.png"
                selected_hover "gui/gui_buttons/GUI main_buttons/start_selected1.png"
                action [SetVariable("current_mode", "chapters"), Show("chapters", dissolve)]
                xalign 0.5

            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/continue_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/continue_selected.png"
                selected "gui/gui_buttons/GUI main_buttons/continue_selected"
                insensitive "gui/gui_buttons/GUI main_buttons/blank_image.png"
                action [SetField(no_rollback, "last_loaded_slot", newest_slot),
                        FileLoad(newest_slot[1], confirm=False, page=newest_slot[0], newest=False),
                        SensitiveIf(current_mode != "chapters")]
                xalign 0.5

         
                

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        imagebutton:
            idle "gui/gui_buttons/GUI main_buttons/load_idle.png"
            hover "gui/gui_buttons/GUI main_buttons/load_selected.png"
            insensitive "gui/gui_buttons/GUI main_buttons/blank_image.png"
            action [ShowMenu("load"),Hide("chapters"), SensitiveIf(current_mode != "chapters")]
            xalign 0.5

        imagebutton:
            idle "gui/gui_buttons/GUI main_buttons/settings_idle.png"
            hover "gui/gui_buttons/GUI main_buttons/settings_selected.png"
            insensitive "gui/gui_buttons/GUI main_buttons/blank_image.png"
            action [ShowMenu("preferences", transition= Dissolve(0.3)),Hide("chapters"), SensitiveIf(current_mode != "chapters")]
            xalign 0.5

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        if renpy.variant("pc"):
            
            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/quit_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/quit_selected.png"
                insensitive "gui/gui_buttons/GUI main_buttons/blank_image.png"
                action [Quit(confirm=not main_menu), SensitiveIf(current_mode != "chapters")]
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

screen arc_buttons1(arc_name, alignment, trans=None):


    frame at trans:
        background None
        align alignment
        yoffset 0 

        has vbox:
            spacing 5
        
        hbox:
            spacing 10
            xalign 0.09
            
        textbutton arc_name: 
            text_size 30 
            action Jump("chapter1")
        
    transclude




screen chapters():
    
    # $ current_screen = str(FileCurrentPage())
    default current_mode = "chapters"
    # add "flickering_light"
    hbox at chapter_line_disappear(delay=0.1):
        # add "underline" xoffset 1200 yoffset 570 xsize 425
        # add "gui/cover_buttons.png" xoffset 1195 yoffset 640 
        add "gui/game_frames/arc_lines.png" xoffset 1250 yoffset 538 xsize 195

       
    frame at chapters_appear:
        
        background None
        yalign 0.725
        xoffset 1275

        
        vbox:
            spacing 10
            yalign 0.854
            xalign 0.05
            xoffset -47.5 - 225
            
            hbox at chapters_disappear(delay = 0):
                add "gui/game_frames/arc_lines.png" xoffset 85
                
                imagebutton:
                    xoffset -75
                    idle "gui/gui_buttons/GUI main_buttons/arc1_idle.png"
                    hover "gui/gui_buttons/GUI main_buttons/arc1_selected.png"
                    action [Jump("start1"), SensitiveIf(persistent.firstchapter_clear)]

            hbox at chapters_disappear(delay = 0.25):
                add "gui/game_frames/arc_lines.png" xoffset 135
                imagebutton:
                    xoffset -25
                    idle "gui/gui_buttons/GUI main_buttons/arc2_idle.png"
                    hover "gui/gui_buttons/GUI main_buttons/arc2_selected.png"
                    insensitive "gui/gui_buttons/GUI main_buttons/arc2_insensitive.png"
                    action [Jump("start1"), SensitiveIf(persistent.secondchapter_clear)]
            hbox at chapters_disappear(delay = 0.5):
                add "gui/game_frames/arc_lines.png" xoffset 185
                imagebutton:
                    xoffset 25
                    idle "gui/gui_buttons/GUI main_buttons/arc3_idle.png"
                    hover "gui/gui_buttons/GUI main_buttons/arc3_selected.png"
                    insensitive "gui/gui_buttons/GUI main_buttons/arc3_insensitive.png"
                    action [Jump("start1"), SensitiveIf(persistent.thirdchapter_clear)]
            hbox at chapters_disappear(delay = 0.65):
                add "gui/game_frames/arc_lines.png" xoffset 235
                imagebutton:
                    xoffset 75
                    idle "gui/gui_buttons/GUI main_buttons/back_idle.png"
                    hover "gui/gui_buttons/GUI main_buttons/back_selected.png"
                    action [Hide("chapters", dissolve), SetVariable("current_mode", "main")]
        

## Main Menu screen ############################################################

screen main_menu():

    tag menu
    # # $ rain_volume = change_rain_volume()
    # textbutton _("セーブ"):
    #         action [SetScreenVariable("current_mode", "save"),
    #                 Function(FileManipulation.reset_selected),
    #                 SensitiveIf(current_mode != "save" and not main_menu)]
    add "flickering_light"

    add "high_rain_volume"

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
    add "high_rain_volume"

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
            xoffset 165
            background None
            hbox:

                imagebutton:
                    idle "gui/gui_buttons/GUI main_buttons/save_idle.png"
                    hover "gui/gui_buttons/GUI main_buttons/save_selected.png"
                    selected_idle "gui/gui_buttons/GUI main_buttons/save_selected.png"
                    insensitive "gui/gui_buttons/GUI main_buttons/save_insensitive.png"
                    action ShowMenu('save')
                imagebutton:
                    idle "gui/gui_buttons/GUI main_buttons/load_idle.png"
                    hover "gui/gui_buttons/GUI main_buttons/load_selected.png"
                    selected_idle "gui/gui_buttons/GUI main_buttons/load_selected.png"
                    insensitive None
                    action ShowMenu('load')
                imagebutton:
                    idle "gui/gui_buttons/GUI main_buttons/settings_idle.png"
                    hover "gui/gui_buttons/GUI main_buttons/settings_selected.png"
                    selected_idle "gui/gui_buttons/GUI main_buttons/settings_selected.png"
                    insensitive None
                    action ShowMenu('preferences') 
                imagebutton:
                    idle "gui/gui_buttons/GUI main_buttons/title_idle.png"
                    hover "gui/gui_buttons/GUI main_buttons/title_selected.png"
                    selected_idle "gui/gui_buttons/GUI main_buttons/title_selected.png"
                    insensitive "gui/gui_buttons/GUI main_buttons/title_insensitive.png"
                    action MainMenu()
                imagebutton:
                    idle "gui/gui_buttons/GUI main_buttons/quit_idle.png"
                    hover "gui/gui_buttons/GUI main_buttons/quit_selected.png"
                    selected_idle "gui/gui_buttons/GUI main_buttons/quit_selected.png"
                    insensitive None
                    action Quit(True)
                imagebutton:
                    idle "gui/gui_buttons/GUI main_buttons/back1_idle.png"
                    hover "gui/gui_buttons/GUI main_buttons/back1_selected.png"
                    selected_idle "gui/gui_buttons/GUI main_buttons/back1_selected.png"
                    insensitive None
                    action Return()

        key "game_menu" action ShowMenu("main_menu")



## Info Panel Screen ############################################################



screen info_panel(label_text, message_text, icon_d, alignment, trans=None):

    style_prefix "info_panel"

    frame at trans:
        background Frame("gui/game_frames/var_bar.png", 38, 0, 12, 0, ysize = 53, yoffset=10, xsize= 535, xoffset= 15)
        align alignment
        yoffset 100

        has vbox:
            spacing 5

        hbox:
            spacing 10
            xalign 0.09


            add icon_d xsize 45 ysize 45 yoffset -5 xoffset 15


            label label_text text_size 30 yoffset 0 xoffset 10 


        window:
            background None
            margin (0, 0)
            top_padding 5
            bottom_padding 0
            left_padding 40
            right_padding 0
            
            xsize 510


            text message_text size 24 yoffset 10

        transclude

init -2:
    style info_panel_label_text is text:
        font "fonts/Poppins-Regular.ttf"
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



## Game Menu screen ############################################################


screen game_menu():
    key "mousedown_3" action Return()
    
    style_prefix "game_menu" tag menu
    $ hours_played = convertSeconds( renpy.get_game_runtime() )[0]
    $ minutes_played = convertSeconds( renpy.get_game_runtime() )[1]
    $ seconds_played = convertSeconds( renpy.get_game_runtime() )[2]
    $ bgm_title = get_current_bgm_title()
    $ seen_chapters = get_seen_chapters()
    add "gui/game_frames/right_click_bg.png"
    frame:
        background None
        add "gui/game_frames/black_image.png" xoffset 75 yoffset 140

        hbox:
            imagebutton:
                xoffset 530
                yoffset 102.5
                idle "gui/gui_buttons/GUI notebook_buttons/tips_idle.png"
                hover "gui/gui_buttons/GUI notebook_buttons/tips_selected.png"
                selected_idle "gui/gui_buttons/GUI notebook_buttons/tips_selected.png"
                action ShowMenu("tips_page", transition= None)
            imagebutton:
                xoffset 200
                yoffset 102.5
                idle "gui/gui_buttons/GUI notebook_buttons/cases_idle.png"
                hover "gui/gui_buttons/GUI notebook_buttons/cases_selected.png"
                selected_idle "gui/gui_buttons/GUI notebook_buttons/cases_selected.png"
                action ShowMenu("gallery", transition= None)

        frame:
            background None
            xoffset 70
            yoffset 50
            add "gui/game_frames/notebook_paper.png" xoffset 60 yoffset 100.5
            hbox:
                imagebutton:
                    xoffset 127.5
                    yoffset 42.5
                    idle "gui/gui_buttons/GUI notebook_buttons/people_idle.png"
                    hover "gui/gui_buttons/GUI notebook_buttons/people_selected.png"
                    selected_idle "gui/gui_buttons/GUI notebook_buttons/people_selected.png"
                    action ShowMenu("game_menu", transition= None)

        default current_chapter = None

    

    use menu_page_title(_("あらすじ"), (1.0, 0.03))

    if current_chapter:
        label plot_titles[current_chapter] style "chapter_name_label" align (0.51, 0.21) text_color "#000"
    
    hbox:
        spacing 50
        xalign 0.225
        yalign 0.60

        frame:
            style_prefix "chapter_buttons"
            yoffset -10
            ysize 600
            has vpgrid:
                cols 1
                xfill True
                spacing 0
            
            if seen_chapters:

                if len(seen_chapters.keys()) >= 12:
                    scrollbars "vertical"
                    mousewheel True
                    draggable False


                for k in sorted(seen_chapters.keys(), key=sort_story_buttons):
                    button:
                        text plot_labels[k] font "fonts/Kalam-Regular.ttf"
                        sensitive "#000"
                        action [SetScreenVariable("current_chapter", k), SensitiveIf(current_chapter != k)] 
                        
                        

        frame:
            
            style_prefix "chapter_contents"
            yoffset 60
            ysize 625
            window:
                has viewport:
                    id "chapter_contents_window_vp"
                    mousewheel True
                    ysize 575
                    yoffset -100

                if current_chapter:

                    $ separator_height = 20

                    vbox:
  
                        null height separator_height

                        for obj in seen_chapters[current_chapter]:
                            text plots[current_chapter + "-" + obj] font "fonts/Kalam-Regular.ttf"
                            null height separator_height

            vbar:
                value YScrollValue("chapter_contents_window_vp")
                bar_invert True
                unscrollable "hide"
                xsize 19
                ysize 575
                yoffset -20
                xalign 1.0
            
    vbox style_suffix "chaptername_vbox":
        
        xalign 0.5
        xoffset 610
        yalign 0.175
        text save_name style_suffix "chaptername_text" xalign 0.5
        
        hbox:
            spacing 15
            xalign 0.5

            add get_time_icon() xsize 60 ysize 60 xoffset -5 yoffset 0

            text "[gameinfo_date]" style_suffix "date_text"

    on "show" action [Preference("auto-forward", "disable"), SetField(config, "skipping", None)]

    use info_panel(_(" BGM"), get_current_bgm_title(), "gui/game_menu_icons/audio-playlist_w.png", (0.925, 0.325))

    use info_panel(_(" Location"), get_location_name(), "gui/game_menu_icons/map_w.png", (0.925, 0.550))

    use info_panel(_(" Info"), get_location_tip(), "gui/game_menu_icons/comment-bubble_w.png", (0.925, 0.775))

    frame:
        xoffset 135
        yoffset 895
        text "Playtime:" size 35 xoffset 51 yoffset 0 color "#000" font "fonts/Kalam-Regular.ttf"
        background None
        hbox:
            yoffset 0
            xoffset 200
            text "[hours_played]:[minutes_played]:[seconds_played]" color "#000" font "fonts/Kalam-Regular.ttf" size 35 
    
    imagebutton:
        xalign 0.95
        yalign 0.925
        idle "gui/gui_buttons/GUI main_buttons/back1_idle.png"
        hover "gui/gui_buttons/GUI main_buttons/back1_selected.png"
        selected_idle "gui/gui_buttons/GUI main_buttons/back1_selected.png"
        insensitive None
        action Return()

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

    frame at hud_appear_date:
        background Frame("gui/game_frames/hud_bg.png", 40)
        align (0.0, 0.05)
        left_padding 40
        right_padding 30

        has hbox:
            spacing 10

        add get_time_icon() yalign 0.5 xysize(50, 50)
        text "[gameinfo_date]" size 30 yoffset 5

    timer 5 action Hide('hud')

screen hud1():
    zorder 100
    style_prefix "hud"

    frame at hud_appear:
        background Frame("gui/game_frames/hud_bg.png", 40)
        align (1.0, 0.05)
        left_padding 40
        right_padding 30

        has hbox:
            spacing 10
        add "gui/game_menu_icons/mouse_icon.png" yalign 0.5
        text "People's tab updated!" size 30
    
    timer 5 action Hide('hud1')

screen hud2():
    zorder 100
    style_prefix "hud"

    frame at hud_appear:
        
        background Frame("gui/game_frames/hud_bg.png", 40)
        align (1.0, 0.05)
        left_padding 40
        right_padding 30

        has hbox:
            spacing 10
        add "gui/game_menu_icons/mouse_icon.png" yalign 0.5
        text "Cases's tab updated!" size 30
    
    timer 5 action Hide('hud2')

screen hud3():
    zorder 100
    style_prefix "hud"

    frame at hud_appear:
        background Frame("gui/game_frames/hud_bg.png", 40)
        align (1.0, 0.05)
        left_padding 40
        right_padding 30

        has hbox:
            spacing 10
        add "gui/game_menu_icons/mouse_icon.png" yalign 0.5
        text "Tip's tab updated!" size 30
    
    timer 5 action Hide('hud3')

init -2:

    style hud_text is notify_text


## Menu Title screen ############################################################


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

init -2:

    style menu_navigation_button is menu_button:
        xsize 130
        ysize 30
        selected_background Frame("gui/button01_idle.png", 4, 4)

    style menu_navigation_button_text is menu_button_text:
        size 16


## Load and Save screens #######################################################

style text_hover:
    color "#ffffff"
    hover_color "#4b4b4b"

init python:
    config.thumbnail_width = 1920
    config.thumbnail_height = 1080

screen save():
    add "flickering_light" 
    add "high_rain_volume"
    key "mousedown_3" action Return() 
    text "SAVE" text_align 0.5 xalign 0.75 yalign 0.125 xoffset 355 size 80 font "fonts/Poppins-Light.ttf"
    tag menu
    use file_picker

screen load():
    # on "replaced" action Stop("music", fadeout=2.0)
    add "flickering_light" 
    add "high_rain_volume"
    key "mousedown_3" action Return() 
    text "LOAD" text_align 0.5 xalign 0.75 yalign 0.125 xoffset 355 size 80 font "fonts/Poppins-Light.ttf"

    tag menu
    use file_picker



screen file_picker():
    
    default tt = Tooltip((Null(), "", "", ""))
    # from datetime import datetime
    
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

                $ slot_foot = FileSlotName(slot + 1, 6)
                # $ get_date = Filetime
                if len(slot_foot) == 1:
                    $ slot_foot = '0' + slot_foot
                
                


                vbox:

                    button:
                 
                        xoffset 2.5
                        yoffset 3
                        xysize (374, 307)
                        background None
                        hover_background "gui/game_frames/bg_slot.png"
                        action FileAction(slot)

                        vbox:
                            xoffset 18
                            yoffset 12.5

                            add FileScreenshot(slot)  size(325, 190)
                            frame:
                                background None
                                text FileTime(slot, format= _("{#file_time}%d/" + "%m" + "/%Y"), empty=_("No Data")):
                                    xalign 0 size 25 yoffset 0 hover_color "#000000" font "fonts/Poppins-Light.ttf"
                                text slot_foot xalign 0.89 size 25 hover_color "#000000" font "fonts/Poppins-Light.ttf"
                                text FileSaveName(slot) xalign 0 yoffset 35 size 25  hover_color "#000000"    
                            
                            
                        xfill True


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
        xoffset 165
        background None
        hbox:


            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/save_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/save_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/save_selected.png"
                insensitive "gui/gui_buttons/GUI main_buttons/save_insensitive.png"
                action ShowMenu('save')
            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/load_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/load_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/load_selected.png"
                insensitive None
                action ShowMenu('load')
            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/settings_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/settings_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/settings_selected.png"
                insensitive None
                action ShowMenu('preferences') 
            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/title_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/title_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/title_selected.png"
                insensitive "gui/gui_buttons/GUI main_buttons/title_insensitive.png"
                action MainMenu()
            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/quit_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/quit_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/quit_selected.png"
                insensitive None
                action Quit(True)
            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/back1_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/back1_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/back1_selected.png"
                insensitive None
                action Return()
                



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

style text_speed:
    yalign 0.5
    xysize(600, 38)
    left_bar "gui/bar/Text.png"
    right_bar "gui/bar/Text_right.png"
    thumb "gui/bar/thumb.png"

style auto_speed:
    yalign 0.5
    xysize(600, 38)
    left_bar "gui/bar/Auto.png"
    right_bar "gui/bar/Music_right.png"
    thumb "gui/bar/thumb.png"

style music_volume:
    yalign 0.5
    xysize(600, 38)
    left_bar "gui/bar/Music.png"
    right_bar "gui/bar/Music_right.png"
    thumb "gui/bar/thumb.png"

style sfx_volume:
    yalign 0.5
    xysize(600, 38)
    left_bar "gui/bar/Text.png"
    right_bar "gui/bar/Sfx_right.png"
    thumb "gui/bar/thumb.png"

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
        xoffset 165
        background None
        hbox:

            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/save_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/save_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/save_selected.png"
                insensitive "gui/gui_buttons/GUI main_buttons/save_insensitive.png"
                action ShowMenu('save')
            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/load_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/load_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/load_selected.png"
                insensitive None
                action ShowMenu('load')
            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/settings_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/settings_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/settings_selected.png"
                insensitive None
                action ShowMenu('sound_settings') 
            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/title_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/title_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/title_selected.png"
                insensitive "gui/gui_buttons/GUI main_buttons/title_insensitive.png"
                action MainMenu()
            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/quit_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/quit_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/quit_selected.png"
                insensitive None
                action Quit(True)
            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/back1_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/back1_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/back1_selected.png"
                insensitive None
                action Return()

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
                    add Transform(Frame("gui/game_frames/preview_textbox.png", xalign=0.5, yalign=0.5, ysize=167, xsize=1000, xoffset= 100, yoffset= 75), alpha=persistent.window_opacity)

                    hbox:
                        xsize 841
                        ysize 217
                        text "_____________________________________" color "#ffffff" yoffset 25 xoffset -100
                    hbox:
                        xsize 841
                        ysize 217
                        text "_____________________________________" color "#ffffff" yoffset 75 xoffset -100

                    xsize 500
                    xoffset 87.5
                    yoffset 155
            hbox:
                xsize 500
                default mouse_clicked = False
                fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
                    imagebutton:
                        yoffset 340
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
        xoffset 165
        background None
        hbox:

            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/save_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/save_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/save_selected.png"
                insensitive "gui/gui_buttons/GUI main_buttons/save_insensitive.png"
                action ShowMenu('save')
            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/load_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/load_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/load_selected.png"
                insensitive None
                action ShowMenu('load')
            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/settings_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/settings_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/settings_selected.png"
                insensitive None
                action ShowMenu('text_settings')
            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/title_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/title_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/title_selected.png"
                insensitive "gui/gui_buttons/GUI main_buttons/title_insensitive.png"
                action MainMenu()
            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/quit_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/quit_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/quit_selected.png"
                insensitive None
                action Quit(True)
            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/back1_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/back1_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/back1_selected.png"
                insensitive None
                action Return()
                

screen preferences():

    tag menu
    
    key "mousedown_3" action Return()
    use settings_menu(_("Configurations"), scroll="viewport")

    add "flickering_light"
    add "high_rain_volume"

    default current_tab = "system"
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
                action SetScreenVariable("current_tab", "system")
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
                                selected_hover "gui/gui_buttons/GUI system_settings/selected_windowed.png"
                                action Preference("display", "window")

                    hbox:
                        xoffset 50
                        default mouse_clicked = False
                        fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
                
                            imagebutton:
                                idle "gui/gui_buttons/GUI system_settings/text_fullscreen.png" xalign 0.5 yalign 0.5 yoffset 27.5
                                hover ("gui/gui_buttons/GUI system_settings/selected_fullscreen_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/selected_fullscreen_hovered.png")
                                selected_idle "gui/gui_buttons/GUI system_settings/selected_fullscreen.png"
                                selected_hover "gui/gui_buttons/GUI system_settings/selected_fullscreen.png"
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
                                selected_hover "gui/gui_buttons/GUI system_settings/selected_skipall.png"
                                action Preference("skip", "all")
                    hbox:
                        xoffset 50
                        default mouse_clicked = False
                        fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
                
                            imagebutton:
                                idle "gui/gui_buttons/GUI system_settings/text_skipseen.png" xalign 0.5 yalign 0.5 yoffset 27.5
                                hover ("gui/gui_buttons/GUI system_settings/selected_skipseen_clicked.png" if mouse_clicked else "gui/gui_buttons/GUI system_settings/selected_skipseen_hovered.png")
                                selected_idle "gui/gui_buttons/GUI system_settings/selected_skipseen.png"
                                selected_hover "gui/gui_buttons/GUI system_settings/selected_skipseen.png"
                                action Preference("skip", "seen")
        # hbox:
        #     textbutton "low rain":
        #         action SetVariable(current_rain_volume, "low_rain_volume")
    hbox:
        xalign 0.5
        yalign 0.5
        xoffset 685
        yoffset 250
        imagebutton:
            idle "gui/gui_buttons/GUI system_settings/restart_idle.png"
            hover "gui/gui_buttons/GUI system_settings/restart_hover.png"
            action SetPreferencesDefault()              

    frame:
        xsize 850
        ysize 100
        xalign 0.5
        yalign 0.9
        xoffset 165
        background None
        hbox:

            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/save_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/save_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/save_selected.png"
                insensitive "gui/gui_buttons/GUI main_buttons/save_insensitive.png"
                action ShowMenu('save')
            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/load_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/load_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/load_selected.png"
                insensitive None
                action ShowMenu('load')
            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/settings_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/settings_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/settings_selected.png"
                insensitive None
                action ShowMenu('preferences') 
            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/title_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/title_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/title_selected.png"
                insensitive "gui/gui_buttons/GUI main_buttons/title_insensitive.png"
                action MainMenu()
            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/quit_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/quit_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/quit_selected.png"
                insensitive None
                action Quit(True)
            imagebutton:
                idle "gui/gui_buttons/GUI main_buttons/back1_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/back1_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/back1_selected.png"
                insensitive None
                action Return()
                        
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
        background Image("gui/game_frames/right_click_bg.png")
        add "gui/scrollbar/black_arrows.png" xalign 0.96575 yoffset 47.5 xoffset -50
        vpgrid:
            yoffset 75  
            ysize 910
            cols 1
            yinitial 1.0
            xsize 1850
            xoffset -50
            draggable True
            mousewheel True
            scrollbars "vertical" 

            
            for h in _history_list:
                
                window:
                    xoffset 185
                          
                    background None
                    ysize 350
                    
                    ## This lays things out properly if history_height is None.
                    has fixed:
                        yfit True

                        if h.rollback_identifier is not Null:
                            imagebutton:
                                idle "gui/gui_buttons/GUI main_buttons/jump_idle.png"
                                hover "gui/gui_buttons/GUI main_buttons/jump_selected.png"
                                action Confirm("Jump back on this dialogue?", RollbackToIdentifier(h.rollback_identifier))
                                yoffset 125 xoffset 55

                        

                    if h.who:
                        frame:
                            background None
                            add "gui/game_menu_icons/separator.png" xoffset 215
                            label h.who:
                                style "history_name"
                                xoffset 0
                                yoffset 0
                                ## Take the color of the who text from the Character, if set.
                                if "color" in h.who_args:
                                    text_color h.who_args["color"]

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        xoffset 235
                        yoffset 10
                        xsize 1250

            if not _history_list:

                text "The dialogue history is empty." line_spacing 10
                ## Adding line_spacing prevents the bottom of the text
                ## from getting cut off. Adjust when replacing the
                ## default fonts.

        imagebutton:
                xalign 0.9 yalign 0.9 yoffset 75 xoffset 25
                idle "gui/gui_buttons/GUI main_buttons/back1_idle.png"
                hover "gui/gui_buttons/GUI main_buttons/back1_selected.png"
                selected_idle "gui/gui_buttons/GUI main_buttons/back1_selected.png"
                insensitive None
                action Return()

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
    
    add "gui/game_frames/right_click_bg.png"
    frame:
        background None
        vbox:
            xalign .5
            yalign .5
            spacing 30
            text message xalign 0.5
            # text _(message) xalign 0.5:
            #     style "confirm_prompt"
            #     xalign 0.5

            hbox:
                xalign 0.5
                spacing 100
                yoffset 25

                imagebutton:
                    idle "gui/gui_buttons/GUI main_buttons/confirm_idle.png"
                    hover "gui/gui_buttons/GUI main_buttons/confirm_selected.png"
                    action yes_action
                imagebutton:
                    idle "gui/gui_buttons/GUI main_buttons/confirm_idle1.png"
                    hover "gui/gui_buttons/GUI main_buttons/confirm_selected1.png"
                    action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action

screen reset_default_navigation(page, alignment):

    style_prefix "menu_navigation"

    frame:
        align alignment
        background None

        has hbox:
            spacing 10

        textbutton _("reset page") action SetPreferencesDefault(page)

        textbutton _("reset all") action SetPreferencesDefault()

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/game_frames/nvl.png", "gui/game_frames/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
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


# Skip indicator screen #######################################################

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    # frame:

    #     hbox:
    #         spacing 6

    #         text _("Skipping")

    #         text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
    #         text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
    #         text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

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

# style skip_frame:
#     ypos gui.skip_ypos
#     background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
#     padding gui.skip_frame_borders.padding

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
    use quick_menu

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

    background "gui/game_frames/nvl.png"
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
