
transform game_menu_info_appear(delay=0):
        yanchor 0.0
        alpha 0.0
        xoffset -200


        pause delay
        ease_back .5 alpha 1.0 xoffset 0

transform game_menu_chapter_info_appear:
        alpha 0.0
        yoffset -200


        ease_back 1.0 alpha 1.0 yoffset 0

transform game_menu_buttons_appear:
        alpha 0.0
        xoffset 200


        ease_back .5 alpha 1.0 xoffset 0

transform rain_layer_appear:
        alpha 0.0
        yoffset 200


        ease_back .5 alpha 1.0 xoffset 0

transform zoom(n):
        zoom n
