
define config.rollback_enabled = False

init:
    
    $ config.keymap['game_menu'].remove('mouseup_3')

init -3:

    define audio.day = "<loop 000.000 to 143.704>bgm_00"
    define audio.easing_tension = "<loop 000.577 to 067.038>bgm_01"
    define audio.flashback = "<loop 008.478 to 091.957>bgm_02"
    define audio.home = "<loop 000.109 to 083.587>bgm_03"
    define audio.homey = "<loop 000.000 to 097.818>bgm_04"
    define audio.prologue = "<loop 000.167 to 181.500>bgm_05"
    define audio.tense = "<loop 000.167 to 181.500>bgm_06"
    define audio.tension = "<loop 000.167 to 097.818>bgm_07"
    define audio.thin_purple = "<loop 000.167 to 097.818>bgm_08"
    define audio.Title = "<loop 000.0167 to 150.019>bgm_09"
    define audio.true_home = "<loop 000.0167 to 150.019>bgm_10"

return


init -2 python:

    if persistent.firstchapter_clear is None:
        persistent.firstchapter_clear = False
init -2 python:
    
    import datetime

    def set_info_scene(scene_id):
        global save_name
        
        if scene_id in scenes:
            save_name = scenes[scene_id]
        else:
            raise ValueError("The scene id '{0}' is unknown.".format(scene_id))

    def set_info_time(time_id):
        global gameinfo_time
        
        if time_id in times:
            gameinfo_time = time_id
        else:
            raise ValueError("The time id '{0}' is unknown.".format(time_id))

    def set_info_date(month, day, weekday):
        global gameinfo_date
        
        if (weekday != "mon" and 
            weekday != "tue" and 
            weekday != "wed" and 
            weekday != "thu" and 
            weekday != "fri" and
            weekday != "sat" and
            weekday != "sun" and
            weekday != "???"):
            raise ValueError("No such a weekday: {0}.".format(weekday))
        
        gameinfo_date = "{0}/{1} ({2})".format(str(month).zfill(2), str(day).zfill(2), weekday.upper())

    def get_current_bgm_title():
            
            now_playing = renpy.music.get_playing()
            
            if now_playing:
                now_playing = now_playing[-6:]
                if now_playing in bgm_titles:
                    return bgm_titles[now_playing]
            
            return 

    def set_info_location(location_id):
        global gameinfo_location
        
        if location_id in locations:
            gameinfo_location = location_id
        else:
            raise ValueError("The location id '{0}' is unknown.".format(location_id))
    
    def get_time_icon():
        if gameinfo_time in times:
            return times[gameinfo_time]["icon"]
        else:
            return None

    def get_location_name():       
        if gameinfo_location in locations:  
            return locations[gameinfo_location]["name"]
        else:
            return ""

    def get_location_tip():       
        if gameinfo_location in locations:  
            return locations[gameinfo_location]["tip"]
        else:
            return ""

    def get_seen_chapters():
        global gameinfo_seen_chapters
        
        chapters_dic = {}
        chapters = gameinfo_seen_chapters.split(",")[:-1]
        
        for chapter in chapters:
            split_chapter = chapter.split("-")
            
            if split_chapter[0] not in chapters_dic:
                chapters_dic[split_chapter[0]] = []
            
            chapters_dic[split_chapter[0]].append(split_chapter[1])
        
        return chapters_dic       


    def add_seen_chapter(chapter_name):
        global gameinfo_seen_chapters
        
        if chapter_name not in plots:
            raise Exception("'" + chapter_name + "' is not a valid chapter.")
        
        if chapter_name not in gameinfo_seen_chapters.split(","):
            gameinfo_seen_chapters += chapter_name + ","
        
        
        
        chapter_name_split = chapter_name.split("-")
        key = chapter_name_split[0]
        value = chapter_name_split[1]
        
        if key not in persistent.seen_chapters:
            persistent.seen_chapters[key] = []
        
        if value not in persistent.seen_chapters[key]:
            persistent.seen_chapters[key].append(value)
            
    def sort_story_buttons(key):
        
        split_key = key.split("_")
        
        split_key_len = len(split_key) 
        
        if split_key_len > 2 or split_key_len == 0:
            raise Exception("'" + key + "' is not a valid format for the chapter key.")
        
        elif split_key_len == 2:
            return int(split_key[0]) * 10 + int(split_key[1])
        
        else:
            return int(split_key[0]) * 10
    
    def show_date():
        global gameinfo_date

        if config.skipping:
            if renpy.get_screen("hud"):
                renpy.hide_screen("hud")
                hud = True
            else:
                return
                hud = False
        
        if not renpy.get_screen("hud") and not renpy.in_rollback():
            renpy.show_screen("hud")
    
    def show_people():

        hud1 = False
        if config.skipping:
            if renpy.get_screen("hud1"):
                renpy.hide_screen("hud1")
            else:
                return
        if not renpy.get_screen("hud1") and not renpy.in_rollback():
            renpy.show_screen("hud1")
    
    def show_cases():   

        if config.skipping:
            if renpy.get_screen("hud2"):
                renpy.hide_screen("hud2")
            else:
                return
        if not renpy.get_screen("hud2") and not renpy.in_rollback():
            renpy.show_screen("hud2")

    def show_tips():

        hud1 = False
        if config.skipping:
            if renpy.get_screen("hud3"):
                renpy.hide_screen("hud3")
            else:
                return
        if not renpy.get_screen("hud3") and not renpy.in_rollback():
            renpy.show_screen("hud3")
            
    def convertSeconds(scs):
        ##convertimos los segundos a entero
        scs = round(scs)

        ##ahora este valor pasará a ser un hh:mm:ss
        scs = str(datetime.timedelta(seconds=scs))
        ##se convierte ahora en un array
        scs = scs.split(":")

        return scs


define gameinfo_time = ""
define gameinfo_date = ""
define gameinfo_location = ""
define gameinfo_seen_chapters = ""

# init python:
#     g = Gallery()

#     g.button()


init -2 python:
    if persistent.seen_chapters is None:
        persistent.seen_chapters = {}


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

    def ResetToDefaults():
        _preferences.text_cps = config.default_text_cps
        _preferences.afm_time = config.default_afm_time
        _preferences.afm_enable = config.default_afm_enable
        _preferences.set_volume('sfx', 1.0)
        _preferences.set_volume('music', 1.0)
        # _preferences.window_opacity(persistent, 1.0)
        # persistent('window_opacity', 1.0)
        renpy.restart_interaction()

    class NoRollbackObj(NoRollback):
        def __init__(self):
            self.rollback_color_set = False
            self.just_loaded = False
            self.voice_count_done = True
            self.last_loaded_slot = None

    no_rollback = NoRollbackObj()



init python:
    
    maxnumx = 2
    maxnumy = 2
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy
    gallery_page = 0
    closeup_page = 0
    
    class GalleryItem:
        def __init__(self, name, images, thumb, locked="lockedthumb"):
            self.name = name 
            self.images = images
            self.thumb = thumb
            self.locked = locked 
            self.refresh_lock()
        def num_images(self):
            return len(self.images)

        def refresh_lock(self):
            self.num_unlocked = 0
            lockme = False

            for img in self.images:
                if not renpy.seen_image(img):
                    lockme = True
                else:
                    self.num_unlocked += 1
                
            self.is_locked  = lockme
            
    gallery_items = []
    #page 1
    gallery_items.append(GalleryItem("", ["img1"], "thumb1"))
    gallery_items.append(GalleryItem("", ["img2"], "thumb2"))
    gallery_items.append(GalleryItem("", ["img3"], "thumb3"))
    gallery_items.append(GalleryItem("", ["img4"], "thumb4"))
    #page 2
    gallery_items.append(GalleryItem("", ["img1"], "thumb1"))
    gallery_items.append(GalleryItem("", ["img2"], "thumb2"))
    gallery_items.append(GalleryItem("", ["img3"], "thumb3"))
    gallery_items.append(GalleryItem("", ["img4"], "thumb4"))
    #page 3
    gallery_items.append(GalleryItem("", ["img5"], "thumb4"))
    gallery_items.append(GalleryItem("", ["img5"], "thumb4"))
    gallery_items.append(GalleryItem("", ["img5"], "thumb4"))
    gallery_items.append(GalleryItem("", ["img5"], "thumb4"))
    #page 4
    gallery_items.append(GalleryItem("", ["img5"], "thumb4"))
    gallery_items.append(GalleryItem("", ["img5"], "thumb4"))
    gallery_items.append(GalleryItem("", ["img5"], "thumb4"))
    gallery_items.append(GalleryItem("", ["img5"], "thumb4"))


define persistent.unlocked_text = [] # empty word list WITH define

    