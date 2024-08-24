# -*- coding: ひきこもり -*-

init -15 python:

    QTE_list = [
         ["2", "2", "2", "2"],
         ["3", "3", "3", "3"],
         ["4", "4", "4", "4"],
         ["м", "М", "v", "V"],
         ["п", "П", "g", "G"],
         ["y", "Y", "н", "Н"],
         ["л", "Л", "k", "K"],
    ]
    QTE_image_list = ["avenger_1", "avenger_2", "avenger_3", "avenger_4", "avenger_5", "avenger_6", "avenger_7"]

    QTE_list_l = [
         ["ь", "Ь", "m", "M"],
         ["л", "Л", "k", "K"],
         ["з", "З", "p", "P"],
         ["н", "Н", "y", "Y"],
         ["о", "О", "j", "J"],
         ["м", "М", "v", "V"],
         ["c", "C", "с", "С"],
         ["д", "Д", "l", "L"],
    ]
    QTE_image_list_l = ["shadowaction", "shadowaction1", "shadowaction2", "shadowaction3", "shadowaction4", "shadowaction5", "shadowaction6", "shadowaction7"]

    Fl_items_dict = {"phone":"Старый телефон", "matches":"Спички", "flashlight":"Фонарик", "knife":"Кухонный нож", "easy":"Лёгкий рюкзак", "key13":"Ключ от 13-го домика", "brush":"Щётка", "dentifrice":"Зубной порошок", "keydoor":"Ключ от домика вожатой", "keypr":"Ключ от склада.", "headphones":"Наушники", "bag":"Пакет"}
    Fl_reusable_items_list = ["key13", "brush", "keydoor", "dentifrice", "keypr"]
    Fl_key_dismiss_list = ["K_MENU", "K_ESCAPE", "dismiss", "button_select", "input_enter", "bar_activate", "bar_deactivate", "mouseup_1", "mouseup_3", "K_SPACE"]
    Fl_names_list = []
    Fl_items_list = ["phone", "matches", "flashlight", "key13", "brush", "dentifrice", "keydoor", "keypr", "headphones", "bag"]
    Fl_key_i_list = ["i", "I", "ш", "Ш"]
    Fl_ordinary_items_list = []
    Fl_backpacks_list = ["easy"]
    Fl_weapons_list = ["knife"]

    config.layers = ["underlay", "master", "mapoverlay", "widgetoverlay", "transient", "screens", "front", "overlay", "onlyverlay"]
    renpy.music.register_channel("ambience","voice",loop=True,tight=True) 
    config.main_menu_music = "audio/music/Fl_senritsu.ogg" 


    Fl_black_color = "#000000"
    Fl_white_color = "#FFFFFF"
    Fl_red_color = "#DB0000"
    Fl_red_light_color = "#FF0000"
    Fl_red_dark_color = "#690000"
    Fl_blue_color = "#00FFFF"
    Fl_blue_dark_color = "#0042FF"
    Fl_blue_dark_color2 = "#2E9AFE"
    Fl_orange_color = "#DF5500"
    Fl_orange_light_color = "#FAAC58"
    Fl_orange_dark_color = "#853300"
    Fl_gray_color = "#848484"
    Fl_gray_light_color = "#BDBDBD"
    Fl_gray_dark_color = "#222222"
    Fl_gray_dark_color2 = "#4E4E4E"
    Fl_yellow_color = "#E4CE13"
    Fl_green_color = "#31BE00"
    Fl_green_light_color = "#00FF00"
    Fl_green_dark_color = "#00CB22"
    Fl_purple_color = "#A901DB"
    Fl_brown_color = "#D2691E"
    Fl_black_light_color = "#292929"


    Fl_swear_dict = {"А БЛ*ТЬ":"ТВОЮ Ж", "п*зде":"караганде", "Бл*ть":"Блин", "бл*ть":"блин", "еб*ло":"лицо",
        "С*КААА!":"КАКОГО?", "БЛ*ТЬ":"БЛИН", "расп*здатые":"гениальные", "Х*евый":"Фиговый", "Бл*":"Чёрт",
        "п*здец":"капец", "п*зда":"капец", "С*ка":"Чёрт", "ХР*НА":"ФИГА", "х*рнёй":"ерундой",
        "у*бал":"откинул", "п*здел":"врал", "х*йня":"чертовшина", "еб*нулись":"с ума сошли",
        "х*рню":"дичь", "еб*нутый":"дурак", "нах*й":"к чёрту", "н*хрена":"ничего", "ни фига":"ничего",
        "бл*":"блин", "х*ре":"хватит", "п*зданул":"ударил", "х*ёвый":"плохой",
        "БЛ*":"БЛИИН", "Них*я":"Нифига", "за*бала":"достала", "х*йню":"ерунду",
        "ах*е":"шоке", "нихр*на":"ничего", "про*бал":"потерял", "за*бало":"достало",
        "С*КА":"ТВАРЬ"}