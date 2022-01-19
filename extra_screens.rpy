screen tips_page():
    key "mousedown_3" action Return()
    style_prefix "game_menu" tag menu

    $ bgm_title = get_current_bgm_title()

    add "gui/nvl.png"

    frame:
        background None
        add "gui/black_image.png" xoffset 75 yoffset 140

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
            background None
            # align (0.10, 0.3)
            xoffset 70
            yoffset 50
            add "gui/game_frames/notebook_paper.png" xoffset 5.5 yoffset 72.5
            hbox: 
                imagebutton:
                    xoffset 455
                    yoffset 40
                    idle "gui/gui_buttons/GUI notebook_buttons/tips_idle.png"
                    hover "gui/gui_buttons/GUI notebook_buttons/tips_selected.png"
                    selected_idle "gui/gui_buttons/GUI notebook_buttons/tips_selected.png"
                    action ShowMenu("tips_page")

        default current_chapter = None

    $ seen_chapters = get_seen_chapters()

    use menu_page_title(_("あらすじ"), (1.0, 0.03))

    if current_chapter:
        label plot_titles[current_chapter] style "chapter_name_label" align (0.51, 0.21) text_color "#000"

    hbox:
        spacing 50
        xalign 0.225
        yalign 0.45


        frame:
            style_prefix "chapter_buttons"
            yoffset 70
            ysize 725
            has vpgrid:
                cols 1
                xfill True
                spacing 0

            if seen_chapters:
                # ysize 1000

                if len(seen_chapters.keys()) >= 12:
                    # ysize 1000
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
            yoffset 125
            ysize 680
            window:
                has viewport:
                    id "chapter_contents_window_vp"
                    mousewheel True
                    ysize 650
                    yoffset -125

                if current_chapter:

                    $ separator_height = 20

                    vbox:
                        # yoffset 100
                        # height 1000
                        #ysize
                        null height separator_height

                        for obj in seen_chapters[current_chapter]:
                            text plots[current_chapter + "-" + obj] font "fonts/Kalam-Regular.ttf"
                            null height separator_height

            vbar:
                value YScrollValue("chapter_contents_window_vp")
                bar_invert True
                unscrollable "hide"
                xalign 1.0
                # ysize 250


    # use menu_navigation(config.menu_navigation_align)

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

    use info_panel(_("Pointers"), get_location_tip(), "gui/game_menu_icons/comment-bubble_w.png", (0.90, 0.730))


# screen cardbook

screen gallery():
    key "mousedown_3" action Return()
    # add "flickering_light"
    # add "title_art"

    style_prefix "game_menu" tag menu

    $ bgm_title = get_current_bgm_title()
    add "gui/nvl.png"
    frame:
        background None
        add "gui/black_image.png" xoffset 75 yoffset 140
        hbox:
            #notebook stubs
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
            #notebook cover
            background None
            add "gui/game_frames/notebook_paper.png" xoffset 50 yoffset 57 
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
                    # spacing 150
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
                            # button:
                            #     xysize (350, 250)
                                

                    for i in range(end - start + 1, maxperpage):
                        null 
                grid maxnumx maxnumy:
                    xspacing 275
                    yspacing 300
                    xalign 0.25
                    yalign 0.65

                    for i in range(start, end + 1):
                        hbox:

                            # spacing maxthumbx - 70
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
                textbutton "Previous":
                    # font "fonts/Kalam-Regular.ttf"
                    style "chapter_name_label"
                    action SetVariable("gallery_page", gallery_page - 1)
                    xalign 0.125
                    yalign 0.825
            if (gallery_page + 1) * maxperpage < len(gallery_items):
                textbutton "Next":
                    # font "fonts/Kalam-Regular.ttf"
                    style "chapter_name_label"
                    action SetVariable("gallery_page", gallery_page + 1)
                    xalign 0.6
                    yalign 0.825
            frame:
                #notebook paper
                background None
                # background "gui/game_frames/notebook_paper.png"
                align (0.10, 0.3)
                # xysize (567, 564)
              

        default current_chapter = None

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

    use info_panel(_("Pointers"), get_location_tip(), "gui/game_menu_icons/comment-bubble_w.png", (0.90, 0.730))

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

init -2:


    style cardbook_character_name_label_text:
        font "fonts/Kalam-Regular.ttf"
        hover_color "#000000"
        idle_color "#29292988"
        selected_color "#000"
        text_align 0.0
        xoffset -25
        size 46

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