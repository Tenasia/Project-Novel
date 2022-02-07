
transform game_menu_info_appear(delay=0):
        # yanchor 0.0
        alpha 0.0
        xoffset 200


        pause delay
        ease_back .5 alpha 1.0 xoffset 0


transform chapters_appear(delay=0):
        # alpha 0
        # xoffset 0
        
        on show:
            pause delay
            easein .5 alpha 1.0 xoffset 200
        on hide:
            pause delay
        #     add "underline"
            easein .5 alpha 0.0 xoffset 200
        # pause delay

transform chapters_disappear(delay=0):
        yanchor 0.0
        alpha 0.0
        xoffset -200

        pause delay
        easein .5 alpha 1.0 xoffset 0
        # on hide:
        #         pause delay
        #         ease_back .3 alpha 0.0 xoffset 0

transform chapter_line_disappear(delay=0):
        yanchor 0.0
        alpha 0.0
        # xoffset -200

        pause delay
        easein .5 alpha 1.0 xoffset 0
        # on hide:
        #     pause delay
        #     easein .5 alpha 0.0 xoffset 0
            
transform trans_say_label:
        alpha 0.0
        easein 0.3 alpha 1.0 xoffset 0


transform game_menu_chapter_info_appear:
        alpha 0.0
        yoffset -200


        ease_back 1.0 alpha 1.0 yoffset 0

transform game_menu_buttons_appear:
        alpha 0.0
        xoffset 200


        ease_back .5 alpha 1.0 xoffset 0

transform zoom(n):
        zoom n

transform hud_appear:
        alpha 0
        xoffset 200

        on show:
            easein .3 alpha 1.0 xoffset 0
        on hide:
            easein .3 alpha 0.0 xoffset 200

transform hud_appear_date:
        alpha 0
        xoffset -200

        on show:
            easein .3 alpha 1.0 xoffset 0
        on hide:
            easein .3 alpha 0.0 xoffset -200


transform casefiletransform:
        subpixel True

        parallel:
                zoom 1
                ease 10 zoom 1.05
                ease 10 zoom 1
                repeat

transform CF_SUSBUTTON:
        on idle:
            zoom 0.3
            alpha 0.8
           # rotate 0
        on hover:
            zoom 0.31
            alpha 1
        on selected_idle:
            zoom 0.3
            alpha 0.51