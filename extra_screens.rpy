screen tips_page():
    key "mousedown_3" action Return()
    style_prefix "game_menu" tag case

    $ hours_played = convertSeconds( renpy.get_game_runtime() )[0]
    $ minutes_played = convertSeconds( renpy.get_game_runtime() )[1]
    $ seconds_played = convertSeconds( renpy.get_game_runtime() )[2]
    $ bgm_title = get_current_bgm_title()

    $ seen_words = get_seen_words()
    add "gui/game_frames/right_click_bg.png"
    frame:

        background None
        add "gui/game_frames/black_image.png" xoffset 115 yoffset 160
        hbox:
            xoffset 160        
            imagebutton:
                xoffset 200
                yoffset 102.5
                idle "gui/gui_buttons/GUI notebook_buttons/cases_idle.png"
                hover "gui/gui_buttons/GUI notebook_buttons/cases_selected.png"
                selected_idle "gui/gui_buttons/GUI notebook_buttons/cases_selected.png"
                hover_sound None
                activate_sound "audio/sfx/pageflip.wav"
                action ShowMenu("gallery", transition= None)

            imagebutton:
                xoffset -130
                yoffset 102.5
                idle "gui/gui_buttons/GUI notebook_buttons/people_idle.png"
                hover "gui/gui_buttons/GUI notebook_buttons/people_selected.png"
                selected_idle "gui/gui_buttons/GUI notebook_buttons/people_selected.png"
                hover_sound None
                activate_sound "audio/sfx/pageflip.wav"
                action ShowMenu("game_menu", transition= None)

        frame:
            background None
            xoffset 70
            yoffset 50
            add "gui/game_frames/notebook_paper_tips.png" xoffset 60 yoffset 100.5
            hbox: 
                imagebutton:
                    xoffset 455
                    yoffset 40
                    idle "gui/gui_buttons/GUI notebook_buttons/tips_idle.png"
                    hover "gui/gui_buttons/GUI notebook_buttons/tips_selected.png"
                    selected_idle "gui/gui_buttons/GUI notebook_buttons/tips_selected.png"
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    action ShowMenu("tips_page", transition= None)
    ### The number of people and their profile sprites ############################################

    if tip_of_interest == 1:
        add None
    elif tip_of_interest == 2:
        add None
    elif tip_of_interest == 3:
        add None
    elif tip_of_interest == 4:
        add None
    elif tip_of_interest == 5:
        add None
    elif tip_of_interest == 6:
        add None
    elif tip_of_interest == 7:
        add None
    elif tip_of_interest == 8:
        add None
    elif tip_of_interest == 9:
        add None
    elif tip_of_interest == 10:
        add None    


    ### The number of buttons on the list of people ########################################

    if notebook_page_tip == 1:
        vbox:
            xpos 200 
            ypos 242
            if tip1 == True:
                textbutton "Cut":
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    text_size 36
                    if tip_of_interest == 1:
                        action SetVariable("tip_of_interest", 1)
                    else:
                        action SetVariable("tip_of_interest", 1)
            if tip2 == True:
                textbutton "Test":
                    yoffset -10
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if tip_of_interest == 2:
                        action SetVariable("tip_of_interest", 2) 
                    else:
                        action SetVariable("tip_of_interest", 2)  
            if tip3 == True:
                textbutton "TE":
                    yoffset -15
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if tip_of_interest == 3:
                        action SetVariable("tip_of_interest", 3) 
                    else:
                        action SetVariable("tip_of_interest", 3) 
            if tip4 == True:
                textbutton "TBD":
                    yoffset -20
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if tip_of_interest == 4:
                        action SetVariable("tip_of_interest", 4) 
                    else:
                        action SetVariable("tip_of_interest", 4)
            if tip5 == True:
                textbutton "Hikari":
                    yoffset -25
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if tip_of_interest == 5:
                        action SetVariable("tip_of_interest", 5) 
                    else:
                        action SetVariable("tip_of_interest", 5)  
            if tip6 == True:
                textbutton "Maeda":
                    yoffset -30
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if tip_of_interest == 6:
                        action SetVariable("tip_of_interest", 6) 
                    else:
                        action SetVariable("tip_of_interest", 6)
            if tip7 == True:
                textbutton "Tetsuro":
                    yoffset -35
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if tip_of_interest == 7:
                        action SetVariable("tip_of_interest", 7) 
                    else:
                        action SetVariable("tip_of_interest", 7)
            if tip8 == True:
                textbutton "Kotani":
                    yoffset -40
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if tip_of_interest == 8:
                        action SetVariable("tip_of_interest", 8) 
                    else:
                        action SetVariable("tip_of_interest", 8)
            if tip9 == True:
                textbutton "Eizo":
                    yoffset -45
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if tip_of_interest == 9:
                        action SetVariable("tip_of_interest", 9) 
                    else:
                        action SetVariable("tip_of_interest", 9)
            if tip10 == True:
                textbutton "Genji":
                    yoffset -50
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if tip_of_interest == 10:
                        action SetVariable("tip_of_interest", 10) 
                    else:
                        action SetVariable("tip_of_interest", 10)
    elif notebook_page_people == 2:
        vbox:
            xpos 200 
            ypos 242
            if tip11 == True:
                textbutton "Takumi":
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    text_size 36
                    if tip_of_interest == 11:
                        action SetVariable("tip_of_interest", 11)
                    else:
                        action SetVariable("tip_of_interest", 11)
            if tip12 == True:
                textbutton "Nakamura":
                    yoffset -10
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if tip_of_interest == 12:
                        action SetVariable("tip_of_interest", 12) 
                    else:
                        action SetVariable("tip_of_interest", 12)  
            if tip13 == True:
                textbutton "Hiraku":
                    yoffset -15
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if tip_of_interest == 13:
                        action SetVariable("tip_of_interest", 13) 
                    else:
                        action SetVariable("tip_of_interest", 13) 
            if tip14 == True:
                textbutton "TBD":
                    yoffset -20
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if tip_of_interest == 14:
                        action SetVariable("tip_of_interest", 14) 
                    else:
                        action SetVariable("tip_of_interest", 14)
            if tip15 == True:
                textbutton "Hikari":
                    yoffset -25
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if tip_of_interest == 15:
                        action SetVariable("tip_of_interest", 15) 
                    else:
                        action SetVariable("tip_of_interest", 15)  
            if tip16 == True:
                textbutton "Maeda":
                    yoffset -30
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if tip_of_interest == 16:
                        action SetVariable("tip_of_interest", 16) 
                    else:
                        action SetVariable("tip_of_interest", 16)
            if tip17 == True:
                textbutton "Tetsuro":
                    yoffset -35
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if tip_of_interest == 17:
                        action SetVariable("tip_of_interest", 17) 
                    else:
                        action SetVariable("tip_of_interest", 17)
            if tip18 == True:
                textbutton "Kotani":
                    yoffset -40
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if tip_of_interest == 18:
                        action SetVariable("tip_of_interest", 18) 
                    else:
                        action SetVariable("tip_of_interest", 18)
            if tip19 == True:
                textbutton "Eizo":
                    yoffset -45
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if tip_of_interest == 19:
                        action SetVariable("tip_of_interest", 19) 
                    else:
                        action SetVariable("tip_of_interest", 19)
            if tip20 == True:
                textbutton "Genji":
                    yoffset -50
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if tip_of_interest == 20:
                        action SetVariable("tip_of_interest", 20) 
                    else:
                        action SetVariable("tip_of_interest", 20)
    
    ### The pages flips ###############

    if available_page_tip >= 2:
        imagebutton:
            # NEXT   
            idle "gui/cases_ui/right.png"
            hover "gui/cases_ui/right_hover.png"
            xpos 440 ypos 742
            hover_sound None
            activate_sound "audio/sfx/pageflip.wav"
            if notebook_page_tip == available_page_tip:
                action NullAction()
            else:
                action SetVariable("notebook_page_tip", notebook_page_tip + 1)
        imagebutton:
            # PREVIOUS
            idle "gui/cases_ui/left.png"
            hover "gui/cases_ui/left_hover.png"
            xpos 305 ypos 723
            hover_sound None
            activate_sound "audio/sfx/pageflip.wav"
            if notebook_page_tip == 1:
                action NullAction()
            else:
                action SetVariable("notebook_page_tip", notebook_page_tip - 1)


    ### The content of each people's information per page ###################################

    frame:
        background None
        xpadding 10
        ypadding 10
        xpos 725
        ypos 198
        xsize 482
        ysize 722

        ### Information content about themselves ################################

        viewport:
            scrollbars "vertical"
            xoffset 10
            yoffset -5
            mousewheel True
            draggable True
            side_yfill True

            vbox:

                if tip_of_interest == 1:
                    null height 20
                    text "{color=#000}Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." size 30 font "fonts/Kalam-Regular.ttf"

                if tip_of_interest == 2:
                    null height 20
                    text "{color=#000}Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." size 30 font "fonts/Kalam-Regular.ttf"

### INFO PANEL ####################
    
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
        hover_sound None
        activate_sound "audio/sfx/clickcool.wav"
        action Return()
# screen cardbook

screen gallery():
    
    key "mousedown_3" action Return()

    style_prefix "game_menu" tag case

    $ hours_played = convertSeconds( renpy.get_game_runtime() )[0]
    $ minutes_played = convertSeconds( renpy.get_game_runtime() )[1]
    $ seconds_played = convertSeconds( renpy.get_game_runtime() )[2]
    $ bgm_title = get_current_bgm_title()
    
    add "gui/game_frames/right_click_bg.png"
    ### The state of the notebook itself #########################################

    if notebook_case == "bloody":
        add "gui/game_frames/black_image.png" xoffset 75 yoffset 140
    else:
        frame:
            background None
            add "gui/game_frames/black_image.png" xoffset 115 yoffset 160
            hbox:

                imagebutton:
                    xoffset 530
                    yoffset 102.5
                    idle "gui/gui_buttons/GUI notebook_buttons/tips_idle.png"
                    hover "gui/gui_buttons/GUI notebook_buttons/tips_selected.png"
                    selected_idle "gui/gui_buttons/GUI notebook_buttons/tips_selected.png"
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    action ShowMenu("tips_page", transition= None)
            
                imagebutton:
                    xoffset 30
                    yoffset 102.5
                    idle "gui/gui_buttons/GUI notebook_buttons/people_idle.png"
                    hover "gui/gui_buttons/GUI notebook_buttons/people_selected.png"
                    selected_idle "gui/gui_buttons/GUI notebook_buttons/people_selected.png"
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    action ShowMenu("game_menu", transition= None)
        
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
                        hover_sound None
                        activate_sound "audio/sfx/pageflip.wav"
                        action ShowMenu("gallery", transition= None)

    ### The number of people and their profile sprites ############################################

    if case_of_interest == 1:
        add "gui/people_info/casefilephotom1.png" xpos 129 ypos 200       
    elif case_of_interest == 2:
        add "gui/people_info/casefilephotom2.png" xpos 129 ypos 200  
    elif case_of_interest == 3:
        add "gui/people_info/casefilephotom1.png" xpos 129 ypos 200  
    elif case_of_interest == 4:
        add "gui/people_info/casefilephotom2.png" xpos 129 ypos 200  
    elif case_of_interest == 5:
        add "gui/people_info/casefilephotom1.png" xpos 129 ypos 200  
    elif case_of_interest == 6:
        add "gui/people_info/casefilephotom2.png" xpos 129 ypos 200  
    elif case_of_interest == 7:
        add "gui/people_info/casefilephotom1.png" xpos 129 ypos 200  
    elif case_of_interest == 8:
        add "gui/people_info/casefilephotom2.png" xpos 129 ypos 200  
    elif case_of_interest == 9:
        add "gui/people_info/casefilephotom1.png" xpos 129 ypos 200  
    elif case_of_interest == 10:
        add "gui/people_info/casefilephotom2.png" xpos 129 ypos 200      


    ### The number of buttons on the list of people ########################################

    # if notebook_page_case == 1:
    #     add None
    
    ### The pages flips ###############

    if available_page_case >= 2:
        imagebutton:
            # NEXT   
            idle "gui/cases_ui/right.png"
            hover "gui/cases_ui/right_hover.png"
            xpos 600 ypos 875
            hover_sound None
            activate_sound "audio/sfx/pageflip.wav"
            if case_of_interest == available_page_case:
                action NullAction()
            else:
                action SetVariable("case_of_interest", case_of_interest + 1)
        imagebutton:
            # PREVIOUS
            idle "gui/cases_ui/left.png"
            hover "gui/cases_ui/left_hover.png"
            xpos 500 ypos 875
            hover_sound None
            activate_sound "audio/sfx/pageflip.wav"
            if case_of_interest == 1:
                action NullAction()
            else:
                action SetVariable("case_of_interest", case_of_interest - 1)


    ### The content of each people's information per page ###################################

    frame:
        background None
        xpadding 10
        ypadding 10
        xpos 725
        ypos 200
        xsize 482
        ysize 722
        if case_of_interest >= 1:
            text str(case_of_interest) + "/" + str(available_page_case) size 32 font "fonts/Kalam-Regular.ttf" color "#000" yoffset 700
        ### Information near the image sprite #######################



        ### Information content about themselves ################################

        viewport:
            scrollbars "vertical"
            xoffset 10
            yoffset -7.5
            mousewheel True
            draggable True
            side_yfill True

            vbox:
                if case_of_interest == 1:
                    if case_note1 == True:
                        add None
                    if case_note1_1 == "first_note":
                        null height 20
                        text "{color=#000}Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." size 30 font "fonts/Kalam-Regular.ttf"
                    elif case_note1_1 == "first_note_redacted":
                        null height 20
                        text "{color=#000}{s}Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.{/s}, my first iteration was wrong," size 30 font "fonts/Kalam-Regular.ttf"
                    if case_note1_2 == "second_note":
                        null height 20
                        text "{color=#000}Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." size 30 font "fonts/Kalam-Regular.ttf"
                    elif case_note1_2 == "second_note_redacted":
                        null height 20
                        text "{color=#000}{s}Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.{/s}, my first iteration was wrong," size 30 font "fonts/Kalam-Regular.ttf"
                if case_of_interest == 2:
                    if case_note2 == True:
                        add None
                    if case_note2_1 == "first_note":
                        null height 20
                        text "{color=#000}Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." size 30 font "fonts/Kalam-Regular.ttf"
                    elif case_note2_1 == "first_note_redacted":
                        null height 20
                        text "{color=#000}{s}Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.{/s}, my first iteration was wrong," size 30 font "fonts/Kalam-Regular.ttf"
                    if case_note2_2 == "second_note":
                        null height 20
                        text "{color=#000}Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." size 30 font "fonts/Kalam-Regular.ttf"
                    elif case_note2_2 == "second_note_redacted":
                        null height 20
                        text "{color=#000}{s}Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.{/s}, my first iteration was wrong," size 30 font "fonts/Kalam-Regular.ttf"
    
#### INFO PANEL ############################################# 
    
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
        hover_sound None
        activate_sound "audio/sfx/clickcool.wav"
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

