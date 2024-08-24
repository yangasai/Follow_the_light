# -*- coding: ひきこもり -*-
init python:
    gui.init(1920, 1080)


define gui.name_text_font = "font/Fl_font.ttf"
define gui.interface_text_font = "font/Fl_font.ttf"


#Main_menu
define gui.main_menu_background = "gui/main_menu.png"

init -777 python:
    import datetime
    persistent.game_last_time = datetime.datetime.now()
    if persistent.gametime is None:
        persistent.gametime = 0
    def show_gametime(st, at):
        t = datetime.datetime.now()
        dt = t - persistent.game_last_time
        persistent.game_last_time = t
        persistent.gametime += dt.total_seconds() 
        minutes, seconds = divmod(int(persistent.gametime), 60)
        hours, minutes = divmod(minutes, 60)
        img = Text("%0*d:%0*d:%0*d" % (2, hours, 2, minutes, 2, seconds), 
            style="Fl_text_big_save_load", yalign=0.97, xalign=0.5, font="font/Fl_mainmenu.ttf", size=35)
        return img, .1

