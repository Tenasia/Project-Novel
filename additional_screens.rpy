init python:
    def run_action(action):
        try:
            for a in action:
                run_action(a)
        except TypeError, te:
            action()
    class Keymapper(renpy.Displayable):
        def __init__(self, vargs, child, **kwargs):
            super(Keymapper, self).__init__(**kwargs)
            self.child = child
            self.vargs = vargs
        def render(self, width, height, st, at):
            return renpy.render(self.child, width, height, st, at)
        def event(self, ev, x, y, st):
            for keysym, action in self.vargs:
                if renpy.map_event(ev, keysym):
                    run_action(action)
            self.child.event(ev, x, y, st)
        def visit(self):
            return [ self.child ]

    KeymapTransform = renpy.curry(Keymapper)


    # key "mousedown_3" action Return()
    # add "gui/nvl.png"
    # frame:
    #     background None
    #     xalign 0.5
    #     yalign 0.5

    #     hbox:
    #         spacing 40
    #         vbox:
    #             spacing 10
    #             textbutton _("History") action ShowMenu('history') text_size 50
    #             textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
    #         vbox:
    #             spacing 10
    #             textbutton _("Auto") action Preference("auto-forward", "toggle")
    #             textbutton _("Save") action ShowMenu('save')
    #             textbutton _("Return") action Return()
    # imagebutton:
    #     xalign 1.0
    #     yalign 0.0
    #     xoffset -30
    #     yoffset 30
    #     auto "return_%s.png"
    #     action Return()

style text_hover:
    color "#ffffff"
    hover_color "#4b4b4b"

init python:
    config.thumbnail_width = 1920
    config.thumbnail_height = 1080
    
screen file_picker():

    default tt = Tooltip((Null(), "", "", ""))
    
    # hbox:
    # add Solid("#900", xysize=(384, 210), xalign=0.75, yalign=0.415)
    frame:
        background "gui/load_frame_with_slot_frame1.png"
        xalign 0.5
        yalign 0.5
        xoffset 320
        yoffset 7.5
        # yoffset 50
        grid gui.file_slot_cols gui.file_slot_rows:
            # xsize 1500
            # xalign 0.5
            # yalign 0.425
            # xoffset 50
            yoffset -10
            xoffset 2
            # xoffset 2.5
            xspacing 2
            yspacing 2
            # yspacing 5
            
            # yspacing 130
            
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
                        # style_prefix "text_hover"
                        # left_padding 5
                        # right_padding 5
                        xoffset 2.5
                        yoffset 3
                        xysize (374, 307)
                        background None
                        hover_background "images/bg border_374_307_12.png"
                        action FileAction(slot)
                        # hovered tt.Action((FileScreenshot(slot), slot_foot, file_time, save_name))
                        vbox:
                            xoffset 18
                            yoffset 12.5
                            style_prefix "text_hover"
                            add FileScreenshot(slot)  size(325, 190)
                            frame:
                                background None
                                text FileTime(slot, format=_("{#file_time}%b/%d/%Y"), empty=_("No Data")):
                                    xalign 0 size 25 yoffset 0 hover_color "#000000" font "Poppins-Light.ttf"
                                text slot_foot xalign 0.89 size 25 hover_color "#000000" font "Poppins-Light.ttf"
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

                    # text slot_foot xalign .5 size 15

    add "gui/stick_fill.png" xalign 0.6170 yalign 0.1725 yoffset 1.5 xoffset -88
    add "gui/stick_fill.png" xalign 0.6170 yalign 0.1725 yoffset 1.5 xoffset -166
    hbox:
        
        xalign 0.6170
        yalign 0.1725
        # spacing 15
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
            # xoffset -500
            # default mouse_clicked = True
            # fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/two.png"
                hover "gui/gui_buttons/GUI save_load_pages/two_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/two_selected.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/two_selected.png"
                action FilePage(2)
        hbox:
            xoffset -2
            # xoffset -500
            # default mouse_clicked = True
            # fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/three.png"
                hover "gui/gui_buttons/GUI save_load_pages/three_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/three_selected.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/three_selected.png"
                action FilePage(3)
        hbox:
            xoffset -3
            # xoffset -500
            # default mouse_clicked = True
            # fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/four.png"
                hover "gui/gui_buttons/GUI save_load_pages/four_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/four_selected.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/four_selected.png"
                action FilePage(4)
        hbox:
            xoffset -2
            # xoffset -500
            # default mouse_clicked = True
            # fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/five.png"
                hover "gui/gui_buttons/GUI save_load_pages/five_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/five_selected.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/five_selected.png"
                action FilePage(5)
        hbox:
            xoffset 0
            # xoffset -500
            # default mouse_clicked = True
            # fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/six.png"
                hover "gui/gui_buttons/GUI save_load_pages/six_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/six_selected.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/six_selected.png"
                action FilePage(6)
        hbox:
            xoffset -1
            # xoffset -500
            # default mouse_clicked = True
            # fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/seven.png"
                hover "gui/gui_buttons/GUI save_load_pages/seven_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/seven_selected.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/seven_selected.png"
                action FilePage(7)
        hbox:
            xoffset -2
            # xoffset -500
            # default mouse_clicked = True
            # fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/eight.png"
                hover "gui/gui_buttons/GUI save_load_pages/eight_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/eight_selected.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/eight_selected.png"
                action FilePage(8)
        hbox:
            xoffset -3
            # xoffset -500
            # default mouse_clicked = True
            # fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/nine.png"
                hover "gui/gui_buttons/GUI save_load_pages/nine_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/nine_selected.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/nine_selected.png"
                action FilePage(9)
        hbox:
            xoffset -4
            # xoffset -500
            # default mouse_clicked = True
            # fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
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
                

screen save():
    add "flickering_light" 
    key "mousedown_3" action Return() 
    text "SAVE" text_align 0.5 xalign 0.75 yalign 0.125 xoffset 355 size 80 font "Poppins-Light.ttf"
    tag menu
    use file_picker

screen load():
    add "flickering_light" 
    key "mousedown_3" action Return() 
    text "LOAD" text_align 0.5 xalign 0.75 yalign 0.125 xoffset 355 size 80 font "Poppins-Light.ttf"

    tag menu
    use file_picker