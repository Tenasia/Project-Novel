screen tips_page():
    key "mousedown_3" action Return()
    style_prefix "game_menu" tag menu

    $ hours_played = convertSeconds( renpy.get_game_runtime() )[0]
    $ minutes_played = convertSeconds( renpy.get_game_runtime() )[1]
    $ seconds_played = convertSeconds( renpy.get_game_runtime() )[2]
    $ bgm_title = get_current_bgm_title()

    $ seen_words = get_seen_words()
    add "gui/game_frames/right_click_bg.png"
    frame:

        #notebook cover
        background None
        add "gui/game_frames/black_image.png" xoffset 75 yoffset 140

        hbox:
            #notebook stubs
            xoffset 160        
            imagebutton:
                xoffset 200
                yoffset 102.5
                idle "gui/gui_buttons/GUI notebook_buttons/cases_idle.png"
                hover "gui/gui_buttons/GUI notebook_buttons/cases_selected.png"
                selected_idle "gui/gui_buttons/GUI notebook_buttons/cases_selected.png"
                action ShowMenu("gallery")

            imagebutton:
                xoffset -130
                yoffset 102.5
                idle "gui/gui_buttons/GUI notebook_buttons/people_idle.png"
                hover "gui/gui_buttons/GUI notebook_buttons/people_selected.png"
                selected_idle "gui/gui_buttons/GUI notebook_buttons/people_selected.png"
                action ShowMenu("game_menu")

        frame:
            #notebook paper
            background None
            # align (0.15, 0.5)
            xoffset 70
            yoffset 50
            add "gui/game_frames/notebook_paper.png" xoffset 60 yoffset 100.5
            hbox: 
                imagebutton:
                    xoffset 455
                    yoffset 40
                    idle "gui/gui_buttons/GUI notebook_buttons/tips_idle.png"
                    hover "gui/gui_buttons/GUI notebook_buttons/tips_selected.png"
                    selected_idle "gui/gui_buttons/GUI notebook_buttons/tips_selected.png"
                    action ShowMenu("tips_page")

    default current_word = None

    

    use menu_page_title(_("あらすじ"), (1.0, 0.03))

    if current_word:
        label word_titles[current_word] style "chapter_name_label" align (0.51, 0.21) text_color "#000"
        # text "________________________" xalign 0.51 yalign 0.24 color "#000" font "fonts/Kalam-Regular.ttf"
    
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
            
            if seen_words:
                # ysize 1000

                if len(seen_words.keys()) >= 12:
                    # ysize 1000
                    scrollbars "vertical"
                    mousewheel True
                    draggable False


                for k in sorted(seen_words.keys(), key=sort_word_buttons):
                    button:
                        text word_labels[k] font "fonts/Kalam-Regular.ttf"
                        sensitive "#000"
                        action [SetScreenVariable("current_word", k), SensitiveIf(current_word != k)] 
                        
                        

        frame:
            
            style_prefix "chapter_contents"
            yoffset 60
            ysize 625
            window:
                has viewport:
                    id "word_contents_window_vp"
                    mousewheel True
                    ysize 575
                    yoffset -100

                if current_word:

                    $ height_separator = 20

                    vbox:
  
                        null height height_separator

                        for obj in seen_words[current_word]:
                            text word_definition[current_word + "-" + obj] font "fonts/Kalam-Regular.ttf"
                            null height height_separator

            vbar:
                value YScrollValue("word_contents_window_vp")
                bar_invert True
                unscrollable "hide"
                xsize 25
                ysize 575
                yoffset -20
                xalign 1.0

    # add "gui/nvl.png"

    # frame:
    #     background None
    #     add "gui/game_frames/black_image.png" xoffset 75 yoffset 140

    #     hbox:
    #         #notebook stubs
    #         xoffset 160        
    #         imagebutton:
    #             xoffset 200
    #             yoffset 102.5
    #             idle "gui/gui_buttons/GUI notebook_buttons/cases_idle.png"
    #             hover "gui/gui_buttons/GUI notebook_buttons/cases_selected.png"
    #             selected_idle "gui/gui_buttons/GUI notebook_buttons/cases_selected.png"
    #             action ShowMenu("gallery")

    #         imagebutton:
    #             xoffset -130
    #             yoffset 102.5
    #             idle "gui/gui_buttons/GUI notebook_buttons/people_idle.png"
    #             hover "gui/gui_buttons/GUI notebook_buttons/people_selected.png"
    #             selected_idle "gui/gui_buttons/GUI notebook_buttons/people_selected.png"
    #             action ShowMenu("game_menu")
    #     frame:
    #         background None
    #         # align (0.10, 0.3)
    #         xoffset 70
    #         yoffset 50
    #         add "gui/game_frames/notebook_paper.png" xoffset 60 yoffset 100.5
    #         hbox: 
    #             imagebutton:
    #                 xoffset 455
    #                 yoffset 40
    #                 idle "gui/gui_buttons/GUI notebook_buttons/tips_idle.png"
    #                 hover "gui/gui_buttons/GUI notebook_buttons/tips_selected.png"
    #                 selected_idle "gui/gui_buttons/GUI notebook_buttons/tips_selected.png"
    #                 action ShowMenu("tips_page")

    #         hbox spacing 200:
    #             viewport:
    #                 xoffset 155
    #                 yoffset 200
    #                 xsize 445
    #                 ysize 600
    #                 child_size (None, 4000)
    #                 scrollbars "vertical"
    #                 spacing 5
    #                 draggable True
    #                 mousewheel True
    #                 arrowkeys True
    #                 # add "#000c"
    #                 vbox spacing 20:
    #                     #glossary_dict
    #                     #use sorted(glossary_dict.keys())
    #                     for word in sorted(persistent.unlocked_text):
    #                         textbutton word:
    #                             style "chapter_name_label"
    #                             text_size 33
    #                             action SetVariable("display_desc", word)
    #                             # action Jump("flashback")
    #             vbox ypos 150 xsize 500 ysize 500:
    #                 xoffset 15
    #                 text glossary_dict.get(display_desc, ""):
    #                     size 33
    #                     font "fonts/Kalam-Regular.ttf"
    #                     color "#000"
    #     default current_chapter = None

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
        # ysize 48
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
# screen cardbook

screen gallery():
    
    key "mousedown_3" action Return()

    style_prefix "game_menu" tag menu

    $ hours_played = convertSeconds( renpy.get_game_runtime() )[0]
    $ minutes_played = convertSeconds( renpy.get_game_runtime() )[1]
    $ seconds_played = convertSeconds( renpy.get_game_runtime() )[2]
    $ bgm_title = get_current_bgm_title()
    
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
                action ShowMenu("tips_page")
        
            imagebutton:
                xoffset 30
                yoffset 102.5
                idle "gui/gui_buttons/GUI notebook_buttons/people_idle.png"
                hover "gui/gui_buttons/GUI notebook_buttons/people_selected.png"
                selected_idle "gui/gui_buttons/GUI notebook_buttons/people_selected.png"
                action ShowMenu("game_menu")
    
        frame:
            xoffset 25
            yoffset 65

            background None
            add "gui/game_frames/notebook_paper_cases.png" xoffset 105 yoffset 85.5
            hbox:
                imagebutton:
                    xoffset 335
                    yoffset 25
                    idle "gui/gui_buttons/GUI notebook_buttons/cases_idle.png"
                    hover "gui/gui_buttons/GUI notebook_buttons/cases_selected.png"
                    selected_idle "gui/gui_buttons/GUI notebook_buttons/cases_selected.png"
                    action ShowMenu("gallery")
                    
            $start = gallery_page * maxperpage
            $end = min(start + maxperpage - 1, len(gallery_items) - 1)
            frame:
                background None
                
                xalign 0.20 
                yalign 0.25
                grid maxnumx maxnumy:

                    xspacing 150
                    yspacing 100
                    xalign 0.23
                    yalign 0.35
                    for i in range(start, end + 1):
                        $gallery_items[i].refresh_lock()
                        if gallery_items[i].is_locked:
                            add gallery_items[i].locked:
                                xsize 350
                                ysize 250
                        else:
                            imagebutton idle gallery_items[i].thumb:
                                xysize(350,250)
                                action Show("gallery_closeup", dissolve, gallery_items[i].images)

                                

                    for i in range(end - start + 1, maxperpage):
                        null 
                grid maxnumx maxnumy:
                    xspacing 275
                    yspacing 300
                    xalign 0.25
                    yalign 0.65

                    for i in range(start, end + 1):
                        hbox:


                            xalign 0.20
                            yalign 0.3 
                            $total = gallery_items[i].num_images()
                            $partial = gallery_items[i].num_unlocked
                            text gallery_items[i].name:
                                font "fonts/Kalam-Regular.ttf"
                                color "#000"
                            # text "[partial]/[total]"
                    
                    for i in range(end - start + 1, maxperpage):
                        null

            if gallery_page > 0:
                imagebutton:
                    idle "gui/gui_buttons/GUI notebook_buttons/left_idle.png"
                    hover "gui/gui_buttons/GUI notebook_buttons/left.png"
                    # style "chapter_name_label"

                    action SetVariable("gallery_page", gallery_page - 1)
                    xalign 0.0875
                    yalign 0.425
            if (gallery_page + 1) * maxperpage < len(gallery_items):
                imagebutton:
                    idle "gui/gui_buttons/GUI notebook_buttons/right_idle.png"
                    hover "gui/gui_buttons/GUI notebook_buttons/right.png"
                    action SetVariable("gallery_page", gallery_page + 1)
                    xalign 0.6
                    yalign 0.425
              

        default current_chapter = None

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
        # ysize 48
        xoffset 135
        yoffset 895
        text "Playtime:" size 35 xoffset 51 yoffset 0 color "#000" font "fonts/Kalam-Regular.ttf"
        background None
        # background Frame("gui/var_bar.png", 38, 0, 12, 0, ysize = 48, yoffset=0, xsize= 525)
        # add "gui/clock.png" xsize 50 ysize 50 xoffset 32.5 yoffset -25 
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

style font_kalam:
    font "fonts/Kalam-Regular.ttf"
    
screen gallery_closeup(images):

    add images[closeup_page]

    if closeup_page > 0:

        textbutton "Previous":
            action SetVariable("closeup_page", closeup_page - 1)
            xalign 0.1 
            yalign 0.98
            background Black 
    
    if closeup_page < len(images) - 1:
        
        textbutton "Next":
            action SetVariable("closeup_page", closeup_page + 1)
            xalign 0.9
            yalign 0.98
            background Black


    textbutton "Return":
        action [SetVariable("closeup_page", 0), Hide("gallery_closeup", dissolve)]
        xalign 0.5
        yalign 0.5

init -2:
    
    style cardbook_character_name_label_text:
        font "fonts/Kalam-Regular.ttf"
        hover_color "#000000"
        idle_color "#29292988"
        selected_color "#000"
        text_align 0.0
        # xoffset -25
        size 46

