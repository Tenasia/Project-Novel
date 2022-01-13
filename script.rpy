
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

define gameinfo_time = ""
define gameinfo_date = ""
define gameinfo_location = ""

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