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

screen quick_game_menu:
    key "mousedown_3" action Return()
    add "gui/nvl.png"
    frame:
        background None
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        hbox:
            spacing 40
            vbox:
                spacing 10
                text "Knowledge" size 40
                text "Charm" size 40
                text "Guts" size 40
                text "Kindness" size 40
                text "Proficiency" size 40
        
            # vbox:
            #     spacing 10
            #     text "[knowledge]" size 40
            #     text "[charm]" size 40
            #     text "[guts]" size 40
            #     text "[kindness]" size 40
            #     text "[proficiency]" size 40

            vbox:
                spacing 10
                textbutton _("History") action ShowMenu('history') text_size 50
                textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            vbox:
                spacing 10
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                textbutton _("Save") action ShowMenu('save')
                textbutton _("Return") action Return()
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
    grid gui.file_slot_cols gui.file_slot_rows:
        xsize 1500
        xalign 0.5
        yalign 0.425
        xoffset 335
        xspacing 150
        yspacing 60
        
        for slot in range(gui.file_slot_cols * gui.file_slot_rows):
        # for slot in range(1, 7):
            # Each file slot is a button.
            # $ file_name = FileSlotName(i, 30)
            # $ file_time = FileTime(i)
            # $ save_name = FileSaveName(i)
            $ slot_foot = FileSlotName(slot + 1, 7)
            if len(slot_foot) == 1:
                $ slot_foot = '0' + slot_foot
            # if len(slot_foot) < 3:
            #     $ slot_foot = '0' + slot_foot
            # $ slot_foot = "No " + slot_foot


            vbox:

                button:
                    # style_prefix "text_hover"
                    left_padding 5
                    right_padding 5
                    xysize (300, 180)
                    background None
                    hover_background "images/bg border_385_170.png"
                    action FileAction(slot)
                    # hovered tt.Action((FileScreenshot(slot), slot_foot, file_time, save_name))
                    vbox:
                        style_prefix "text_hover"
                        add FileScreenshot(slot) xalign 0.5 size(300, 180)
                        text FileTime(slot, format=_("{#file_time}%b/%d/%Y"), empty=_("No Data")):
                            xalign 0 size 25 yoffset 0 hover_color "#000000"
                        text FileSaveName(slot) xalign 0.99999 size 25 yoffset -33 hover_color "#000000"
                        add "gui/number_slot_small.png" xalign 0.01 yoffset -240 xoffset -0
                        # add "gui/number_slot_small.png" xalign 0.99999 yoffset -120 xoffset -10
                        text slot_foot xalign 0.01 size 20 yoffset -267.5 xoffset 5 color "#000000"
                        # text slot_foot xalign 0.01 size 20 yoffset -267.5 xoffset 5 color "#000000"
                    xfill True

                    
                    # Add the screenshot.
                    # if file_time:
                    #     add FileScreenshot(slot) xalign .5 xysize(300, 180)
                    #     # xsize 200 ysize 125
                    # else:
                    #     add Solid("#900", xysize=(325, 190)) # HERE THE IMAGE OF THE EMPTY SLOT

                    key "save_delete" action FileDelete(slot)

                # text slot_foot xalign .5 size 15

    # frame:
    #     xsize 200
    #     xalign 0.85
    #     yalign 0.75
    #     yoffset 300
        
    #     add tt.value[0] xalign .5 xsize 525 ysize 350 yoffset 50
    #     text tt.value[1] xalign 0.5
    #     text tt.value[2] xalign .5
    #     text tt.value[3] size 15
    
        
    hbox:
        
        xalign 0.835
        yalign 0.125
        spacing 15
        xoffset 0
        hbox:
            # xoffset 500
            # default mouse_clicked = False
            # fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/one.png"
                hover "gui/gui_buttons/GUI save_load_pages/selected_onebutton_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/selected_onebutton.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/selected_onebutton.png"
                action FilePage(1)
        hbox:
            # xoffset -500
            # default mouse_clicked = True
            # fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/two.png"
                hover "gui/gui_buttons/GUI save_load_pages/selected_twobutton_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/selected_twobutton.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/selected_twobutton.png"
                action FilePage(2)
        hbox:
            # xoffset -500
            # default mouse_clicked = True
            # fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/three.png"
                hover "gui/gui_buttons/GUI save_load_pages/selected_threebutton_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/selected_threebutton.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/selected_threebutton.png"
                action FilePage(3)
        hbox:
            # xoffset -500
            # default mouse_clicked = True
            # fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/four.png"
                hover "gui/gui_buttons/GUI save_load_pages/selected_fourbutton_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/selected_fourbutton.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/selected_fourbutton.png"
                action FilePage(4)
        hbox:
            # xoffset -500
            # default mouse_clicked = True
            # fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/five.png"
                hover "gui/gui_buttons/GUI save_load_pages/selected_fivebutton_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/selected_fivebutton.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/selected_fivebutton.png"
                action FilePage(5)
        hbox:
            # xoffset -500
            # default mouse_clicked = True
            # fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/six.png"
                hover "gui/gui_buttons/GUI save_load_pages/selected_sixbutton_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/selected_sixbutton.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/selected_sixbutton.png"
                action FilePage(6)
        hbox:
            # xoffset -500
            # default mouse_clicked = True
            # fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/seven.png"
                hover "gui/gui_buttons/GUI save_load_pages/selected_sevenbutton_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/selected_sevenbutton.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/selected_sevenbutton.png"
                action FilePage(7)
        hbox:
            # xoffset -500
            # default mouse_clicked = True
            # fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/eight.png"
                hover "gui/gui_buttons/GUI save_load_pages/selected_eightbutton_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/selected_eightbutton.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/selected_eightbutton.png"
                action FilePage(8)
        hbox:
            # xoffset -500
            # default mouse_clicked = True
            # fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
            imagebutton:
                idle "gui/gui_buttons/GUI save_load_pages/nine.png"
                hover "gui/gui_buttons/GUI save_load_pages/selected_ninebutton_hovered.png"
                selected_idle "gui/gui_buttons/GUI save_load_pages/selected_ninebutton.png"
                selected_hover "gui/gui_buttons/GUI save_load_pages/selected_ninebutton.png"
                action FilePage(9)
    frame:
        xsize 850
        ysize 100
        xalign 0.5
        yalign 0.9
        xoffset 350
        background None
        hbox:
            spacing 50


            textbutton "SAVE" action ShowMenu('save')
            textbutton "LOAD" action ShowMenu('load')
            textbutton "CONFIG" action ShowMenu('preferences') 
            textbutton "TITLE" action MainMenu()
            textbutton "QUIT" action Quit(True)
            textbutton "BACK" action Return()
                
# screen file_slots(title):

#     default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

#     use game_menu(title):

#         fixed:

#             order_reverse True


#             button:
#                 xsize 300 
#                 ysize 180

#                 key_events True
#                 xalign 0.5
#                 action page_name_value.Toggle()

#                 input:
#                     style "page_label_text"
#                     value page_name_value


#             grid gui.file_slot_cols gui.file_slot_rows:
#                 style_prefix "slot"

#                 xalign 0.5
#                 yalign 0.4

#                 spacing gui.slot_spacing

#                 for i in range(gui.file_slot_cols * gui.file_slot_rows):

#                     $ slot = i + 1

#                     button:
#                         action FileAction(slot)

#                         has vbox

#                         add FileScreenshot(slot) xalign 0.5 xsize 300 ysize 180

#                         text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
#                             xsize 300 ysize 180

#                         text FileSaveName(slot):
#                             style "slot_name_text"

#                         key "save_delete" action FileDelete(slot)


#             hbox:
#                 style_prefix "page"

#                 xalign 0.5
#                 yalign 1.15

#                 spacing gui.page_spacing

#                 textbutton _("<") action FilePagePrevious()

#                 if config.has_autosave:
#                     textbutton _("{#auto_page}A") action FilePage("auto")

#                 if config.has_quicksave:
#                     textbutton _("{#quick_page}Q") action FilePage("quick")


#                 for page in range(1, 6):
#                     textbutton "[page]" action FilePage(page)

#                 textbutton _(">") action FilePageNext()

screen save():
    add "flickering_light" 
    text "SAVE GAME" text_align 0.5 xalign 0.3375 yalign 0.125 xoffset 350 size 40
    tag menu
    use file_picker

screen load():
    add "flickering_light" 
    text "LOAD GAME" text_align 0.5 xalign 0.3375 yalign 0.125 xoffset 350 size 40

    tag menu
    use file_picker