
define bgm_titles = {
    "bgm_00" : _("Day"),
    "bgm_01" : _("Easing Tension"), 
    "bgm_02" : _("Flashback"),
    "bgm_03" : _("Home"),
    "bgm_04" : _("Homey"),
    "bgm_05" : _("Prologue"),
    "bgm_06" : _("Tense"),
    "bgm_07" : _("Tension"),
    "bgm_08" : _("Thin Purple"),
    "bgm_09" : _("Title"),
    "bgm_10" : _("True Home"),
}

define scenes = {
    "00" : _("Prologue"),
    "01" : _("Home"),
    "02" : _("School Day")
}

define locations = {
    "01" : {"name" : _("？？？"), "tip" : ""},
    "02" : {"name" : _("Somewhere in Tokyo"), "tip" : "This is home to the Fuuji's, which was built upon many years ago."},
    "03" : {"name" : _("Tokyo University"), "tip" : "The school was said to be only accepting Elites, but you'll see for yourself if that's true."}    
}

init -5:

    define times = {
        None : { "label" : "", "icon" : None},
        "morning" : { "label" : _("朝"), "icon" : "gui/game_menu_icons/sunrise.png" },
        "day" : { "label" : _("昼"), "icon" : "gui/game_menu_icons/day.png" },
        "evening" : { "label" : _("夕方"), "icon" : "gui/game_menu_icons/sunset.png" },
        "night" : { "label" : _("夜"), "icon" : "gui/game_menu_icons/midnight.png" },
    }