
transform game_menu_info_appear(delay=0):
        yanchor 0.0
        alpha 0.0
        xoffset -200


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
            easein .5 alpha 0.0 xoffset 0
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

        on show:
            pause delay
            easein .5 alpha 1.0 xoffset 0
        on hide:
            pause delay
            easein .5 alpha 0.0 xoffset 0
            
        

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