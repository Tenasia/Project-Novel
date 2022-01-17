screen tips_page():
    key "mousedown_3" action Return()


    style_prefix "game_menu" tag menu

    default tp = Tooltip("")
    $ bgm_title = get_current_bgm_title()

    

    add "gui/nvl.png"



    frame:
        background "gui/game_frames/notebook_frame.png"
        align (0.10, 0.3)
        xysize (567, 564)

        textbutton "Home" action ShowMenu("game_menu") xoffset 100 yoffset 100
        default current_chapter = None

    $ seen_chapters = get_seen_chapters()


    # add "gui/nvl.png"


    use menu_page_title(_("あらすじ"), (1.0, 0.03))

    if current_chapter:
        label plot_titles[current_chapter] style "chapter_name_label" align (0.20, 0.21)

    hbox:
        spacing 50
        xalign 0.225
        yalign 0.65


        frame:
            style_prefix "chapter_buttons"

            has vpgrid:
                cols 1
                xfill True
                spacing 0

            if seen_chapters:


                if len(seen_chapters.keys()) >= 14:
                    scrollbars "vertical"
                    mousewheel True
                    draggable False

                for k in sorted(seen_chapters.keys(), key=sort_story_buttons):
                    button:
                        text plot_labels[k]

                        action [SetScreenVariable("current_chapter", k), SensitiveIf(current_chapter != k)]






        frame:
            
            style_prefix "chapter_contents"





            window:
                has viewport:
                    id "chapter_contents_window_vp"
                    mousewheel True
                    ysize 500

                if current_chapter:

                    $ separator_height = 20

                    vbox:
                        spacing 0
                        # height 1000
                        # ysize True 
                        null height separator_height

                        for obj in seen_chapters[current_chapter]:
                            text plots[current_chapter + "-" + obj]
                            null height separator_height

            vbar:
                value YScrollValue("chapter_contents_window_vp")
                bar_invert True
                unscrollable "hide"
                xalign 1.0
                # ysize 250


    use menu_navigation(config.menu_navigation_align)

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