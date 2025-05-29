# -*- coding: ひきこもり -*-
init python:

    from random import randint


    #ТЕКСТОВЫЕ
    Fl_th = Character(u'', what_prefix='«', what_suffix='»', color="#ffa200", what_color="ffffff", font="font/Fl_font.ttf",  drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_r = Character(u'', what_prefix='', what_suffix='', color="#ffa200", what_color="ffffff", font="font/Fl_font.ttf",  drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    #ПЕРСЫ
    Fl_gg = Character(u'Ян', color="#7B68EE", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_sin = Character(u'Я', color="#FF0000", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_pi = Character(u'Пионер', color="#7B68EE", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_pib = Character(u'Пионер', color="#FF0000", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_pior = Character(u'Пионер', color="#faa600", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_vp = Character(u'Главный', color="#faa600", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_kt = Character(u'...', color="#808080", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_kvl = Character(u'...', color="#808080", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_kvp = Character(u'Голос', color="#808080", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_ktv = Character(u'???', color="#808080", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_d = Character(u'Девушка', color="#808080", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_unk1 = Character(u'Неизвестный 1', color="#808080", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_unk2 = Character(u'Неизвестный 2', color="#808080", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    
    Fl_h = Character(u'Хозяйка', color="#ffa200", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    Fl_park = Character(u'Неизвестный', color="#808080", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_par = Character(u'Доктор Парки', color="#808080", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    Fl_to = Character(u'Толик', color="#008000", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_ka = Character(u'Катя', color="#00BFFF", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    
    Fl_mv = Character(u'Марина Владимировна', color="#A901DB", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_mvv = Character(u'Вожатая', color="#A901DB", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    
    Fl_mirk = Character(u'Пионерка', color="#C0C0C0", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_mir = Character(u'Мира', color="#C0C0C0", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    
    Fl_anp = Character(u'Пионерка', color="#FF0000", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_an = Character(u'Аня', color="#FF0000", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    Fl_mip = Character(u'Пионерка', color="#00deff", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_mi = Character(u'Мику', color="#00deff", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    Fl_lnp = Character(u'Пионерка', color="#9400D3", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_ln = Character(u'Лена', color="#9400D3", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_lnd = Character(u'Лена', color="#9400D3", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    Fl_msk = Character(u'Михан', color="#FF8C00", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    Fl_artp = Character(u'Кучерявый', color="#32CD32", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_art = Character(u'Артём', color="#32CD32", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    Fl_ssp = Character(u'Седой', color="#66CDAA", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_ss = Character(u'Саша', color="#66CDAA", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    Fl_mzp = Character(u'Библиотекарша', color="#000080", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_mz = Character(u'Женя', color="#000080", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    Fl_csk = Character(u'Медсестра', color="#483D8B", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_cs = Character(u'Виола', color="#483D8B", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    Fl_ba = Character(u'Физрук', color="#8B0000", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    Fl_alp = Character(u'Пионерка', color="#faa600", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_al = Character(u'Алиса', color="#faa600", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    Fl_krp = Character(u'Пионерка', color="#4682B4", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_kr = Character(u'Кристина', color="#4682B4", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    Fl_kuv = Character(u'Девушка в платье', color="#008000", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_uv = Character(u'Юля', color="#008000", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    

    #Сказители
    Fl_lnt = Character(u'Тихоня', color="#9400D3", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_q66 = Character(u'Q-66', color="#FF0000", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_q6 = Character(u'Q-66', color="#7B68EE", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_liz87 = Character(u'L-87', color="#FF0000", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_liz = Character(u'Импостер', color="#FF0000", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_qu = Character(u'Королева', color="#FF0000", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_setk = Character(u'Кукловод', color="#faa600", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_tul = Character(u'Деформация', color="#d7e2f9", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_ul34 = Character(u'Псионик', color="#f12016", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")



    #ПЕРСЫ(Упротые)
    Fl_uto = Character(u'Т0лЕг', color="#008000", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_uka = Character(u'КуТя', color="#00BFFF", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_ualp = Character(u'Еbатъ Хто Это?', color="#faa600", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_ual = Character(u'АлИska-pip1ska', color="#faa600", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_umv = Character(u'Моринад Vлодiм1раВна', color="#A901DB", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Fl_uan = Character(u'Red-СадиСто4ка', color="#FF0000", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")


default evil = True


    


init:
    #Часы
    image Fl_game_time = DynamicDisplayable(show_gametime)


    #ЗАГРУЗОЧНЫЙ ЭКРАН  
    image Fl_loading = "gui/loading/none.png"


    #FLASH
    $ Fl_flash_fast = Fade(0.5, 0, 0.5, color="#fff")
    $ Fl_flash = Fade(1, 0, 1, color="#fff")
    $ Fl_flash2 = Fade(2, 0, 2, color="#fff")
    $ Fl_flash_red = Fade(1, 0, 1, color="#FF0000")
    $ backdrop = "prologue"


    #ПЕРЕМЕННЫЕ DISSOLVE
    $ dopscene = False
    $ Fl_dspr = Dissolve(0.2)
    $ Fl_fast = Dissolve(0.5)
    $ Fl_dissolve1 = Dissolve(1.0)
    $ Fl_dissolve1_5 = Dissolve(1.5)
    $ Fl_dissolve2 = Dissolve(2.0)
    $ Fl_dissolve3 = Dissolve(3.0)
    $ Fl_dissolve4 = Dissolve(4.0)
    $ Fl_dissolve5 = Dissolve(5.0)
    $ Fl_dissolve6 = Dissolve(6.0)


    #User
    $ Fl_user = os.environ.get('username')






    #ЭФФЕКТ ПЕРЕХОДА
    $ Fl_effect_time = ImageDissolve("move/Fl_effect1.png", 1.0, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_time_pause = ImageDissolve("move/Fl_effect1.png", 2.5, ramplen = 25, reverse = False, alpha = True)

    $ Fl_effect_1 = ImageDissolve("move/Fl_effect2.png", 1.0, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_1_pause = ImageDissolve("move/Fl_effect2.png", 1.0, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_2 = ImageDissolve("move/Fl_effect3.png", 2.0, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_2_pause = ImageDissolve("move/Fl_effect3.png", 2.0, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_3 = ImageDissolve("move/Fl_effect4.png", 1.5, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_3_pause = ImageDissolve("move/Fl_effect4.png", 2.0, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_4 = ImageDissolve("move/Fl_effect5.png", 1.5, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_4_pause = ImageDissolve("move/Fl_effect5.png", 2.5, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_5 = ImageDissolve("move/Fl_effect6.png", 1.5, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_5_pause = ImageDissolve("move/Fl_effect6.png", 2.5, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_6 = ImageDissolve("move/Fl_effect7.png", 2.5, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_6_pause = ImageDissolve("move/Fl_effect7.png", 2.5, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_left1 = ImageDissolve("move/Fl_effect_left.png", 1.2, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_left1_pause = ImageDissolve("move/Fl_effect_left.png", 2.5, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_left2 = ImageDissolve("move/Fl_effect_left.png", 2.0, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_left2_pause = ImageDissolve("move/Fl_effect_left.png", 2.5, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_right1 = ImageDissolve("move/Fl_effect_right.png", 1.2, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_right1_pause = ImageDissolve("move/Fl_effect_right.png", 2.5, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_right2 = ImageDissolve("move/Fl_effect_right.png", 2.0, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_right2_pause = ImageDissolve("move/Fl_effect_right.png", 2.5, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_down1 = ImageDissolve("move/Fl_effect_down.png", 1.2, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_down1_pause = ImageDissolve("move/Fl_effect_down.png", 2.5, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_down2 = ImageDissolve("move/Fl_effect_down.png", 2.0, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_down2_pause = ImageDissolve("move/Fl_effect_down.png", 2.5, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_mosaic = ImageDissolve("move/Fl_mosaic.png", 2.0, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_mosaic_pause = ImageDissolve("move/Fl_mosaic.png", 2.5, ramplen = 25, reverse = False, alpha = True) 


    #СПЕЦАЛЬНЫЕ
    image Fl_vignette = "special/Fl_vignette.png"
    image Fl_vignette2 = "special/Fl_vignette2.png"
    image Fl_vignette3 = "special/Fl_vignette3.png"
    image Fl_entrance_night_vision_layer = "special/Fl_entrance_night_vision_layer.png"
    image Fl_rage1 = "special/Fl_rage1.png"
    image Fl_rage2 = "special/Fl_rage2.png"
    image Fl_belizna_eff = "special/Fl_belizna_eff.png"
    image Fl_blood_eff = "special/Fl_blood_eff.png"


    #МЕНЮ
    image main_menu = "gui/main_menu/main_menu.png"
    image mine_menu_bad = "gui/main_menu/mine_menu_bad.png"


    image bg Fl_menu:
        subpixel True
        "main_menu" with Fl_dissolve3
        pause(8)
        "mine_menu_bad" with Fl_flash
        pause(4)
        "main_menu" with Fl_dissolve3
        pause(8)
        "mine_menu_bad" with Fl_flash
        pause(4)
        repeat


    #Загрузка
    image layer2 = "gui/main_menu/layer2.png"
    image layer3 = "gui/main_menu/layer3.png"
    image bus = "gui/main_menu/bus.png"
    image hand = "gui/main_menu/hand.png"

    image Fl_layer_load:
        subpixel True
        "layer2" with Fl_dissolve1
        pause(5)
        "layer3" with Fl_dissolve1
        pause(4)
        "layer2" with Fl_dissolve1
        pause(5)
        "layer3" with Fl_dissolve1
        pause(4)
        repeat

    #Экран о игре/обнове
    image update_layer = "gui/about/update_layer.png"

    #Настройки
    image Fl_night_TV_layer = "gui/main_menu/Fl_night_TV_layer.png"
    image Fl_night_TV_layer2 = "gui/main_menu/Fl_night_TV_layer2.png"
    image Fl_night_TV_layer3 = "gui/main_menu/Fl_night_TV_layer3.png"
    image Fl_sl1 = "gui/main_menu/Fl_sl1.png"
    image Fl_sl2 = "gui/main_menu/Fl_sl2.png"
    image Fl_sl3 = "gui/main_menu/Fl_sl3.png"

    image Fl_layer_preference:
        subpixel True
        "Fl_night_TV_layer" with Fl_dissolve2
        pause(6)
        "Fl_night_TV_layer2" with Fl_dissolve3
        pause(6)
        "Fl_night_TV_layer3" with Fl_dissolve2
        pause(5)
        repeat

    image Fl_night_TV_sl:
        subpixel True
        "Fl_sl1" with Fl_flash
        pause(4)
        "Fl_sl2" with Fl_flash
        pause(4)
        "Fl_sl3" with Fl_dissolve2
        pause(4)
        "bg Fl_black" with Fl_flash
        pause(5)
        repeat


    #Галерея
    image Fl_gallery_fon_osn = "gui/main_menu/gallery/Fl_gallery_fon_osn.png"
    image Fl_gallery_photo_none = "gui/main_menu/gallery/Fl_gallery_photo_none.png"
    image Fl_gallery_lych = "gui/main_menu/gallery/Fl_gallery_lych.png"



    #Словарь
    image Fl_dictionary = "gui/dictionary/Fl_dictionary.jpg"


    #Достижения
    image Fl_progress_osn = "gui/progress/Fl_progress_osn.png"



    #Туман
    image Fl_smoke:
        Fl_ease_slowly_repeat



    #СНЕГ
    image Fl_snow = "snow/Fl_snow.png"






    #ДОЖДЬ 
    image Fl_rain:
        truecenter
        xzoom 1.3 yzoom 1.7
        contains:
            SnowBlossom("Fl_rain_particle_large", 10, 50, (75, 125), (1600, 1700))
        contains:
            SnowBlossom("Fl_rain_particle_normal", 25, 50, (50, 100), (1500, 1600))
        contains:
            SnowBlossom("Fl_rain_particle_small", 150, 50, (25, 50), (1400, 1500))
    
    
    image Fl_rain_particle_large = "rain/Fl_rain_large.png"
    image Fl_rain_particle_large2 = "rain/Fl_rain_large2.png"
    image Fl_rain_particle_normal = "rain/Fl_rain_normal.png"
    image Fl_rain_particle_normal2 = "rain/Fl_rain_normal2.png"
    image Fl_rain_particle_small = "rain/Fl_rain_small.png"
    image Fl_rain_particle_small2 = "rain/Fl_rain_small2.png"
    
    
    image Fl_rain_right:
        "Fl_rain"
        rotate 16.0

    image Fl_rain_left:
        "Fl_rain"
        rotate -16.0

    image Fl_rain_hard:
        contains:
            "Fl_rain"
        contains:
            "Fl_rain"

    image Fl_rain_hard_right:
        contains:
            "Fl_rain_right"
        contains:
            "Fl_rain_right"

    image Fl_rain_hard_left:
        contains:
            "Fl_rain_left"
        contains:
            "Fl_rain_left"

    #Пыль
    image Fl_dust5:
        Fl_dust_alpha_linear_repeat(5, 10.0, 14.0)
    
    image Fl_dust6:
        Fl_dust_alpha_linear_repeat(6, 28.0, 32.0)
    
    image Fl_dust7:
        Fl_dust_alpha_linear_repeat(7, 13.0, 17.0)

    image Fl_dust8:
        Fl_dust_alpha_linear_repeat(8, 15.0, 19.0)
    
    image Fl_dust9:
        Fl_dust_alpha_linear_repeat(9, 10.0, 14.0)

    image Fl_dust10:
        Fl_dust_alpha_linear_repeat(10, 28.0, 32.0)

    image Fl_dust11:
        Fl_dust_alpha_linear_repeat(11, 13.0, 17.0)

    image Fl_dust12:
        Fl_dust_alpha_linear_repeat(12, 15.0, 19.0)


    image Fl_dust_full:
        "Fl_dust5"
        "Fl_dust6"
        "Fl_dust7"
        "Fl_dust8"
        "Fl_dust9"
        "Fl_dust10"
        "Fl_dust11"
        "Fl_dust12"


    #Освещение с пылью
    image Fl_light_l:
        Fl_light_and_dust_contains("Fl_l_light")

    image Fl_light_r:
        Fl_light_and_dust_contains("Fl_r_light")

    image Fl_light_c:
        "Fl_light_l"
        "Fl_light_r"




    #QTE
    image Fl_QTE1:
        "QTE/Fl_QTE_1.png" with Dissolve(1.0)
        0.1
        "QTE/Fl_QTE_11.png" with Dissolve(1.0)
        0.1
        repeat
        
    image Fl_QTE2:
        "QTE/Fl_QTE_2.png" with Dissolve(1.0)
        0.1
        "QTE/Fl_QTE_22.png" with Dissolve(1.0)
        0.1
        repeat
        
    image Fl_QTE3:
        "QTE/Fl_QTE_3.png" with Dissolve(1.0)
        0.1
        "QTE/Fl_QTE_33.png" with Dissolve(1.0)
        0.1
        repeat
        
    image Fl_QTE4:
        "QTE/Fl_QTE_4.png" with Dissolve(1.0)
        0.1
        "QTE/Fl_QTE_44.png" with Dissolve(1.0)
        0.1
        repeat



    image qte_1_button_anim = Animation("QTE/qte_1_button.png", 0.1, "QTE/qte_1_button2.png", 0.1,)
    image qte_2_button_anim = Animation("QTE/qte_2_button.png", 0.1, "QTE/qte_2_button2.png", 0.1,)
    image qte_3_button_anim = Animation("QTE/qte_3_button.png", 0.1, "QTE/qte_3_button2.png", 0.1,)
    image qte_4_button_anim = Animation("QTE/qte_4_button.png", 0.1, "QTE/qte_4_button2.png", 0.1,)
    image qte_5_button_anim = Animation("QTE/qte_5_button.png", 0.1, "QTE/qte_5_button2.png", 0.1,)
    image qte_6_button_anim = Animation("QTE/qte_6_button.png", 0.1, "QTE/qte_6_button2.png", 0.1,)
    image qte_7_button_anim = Animation("QTE/qte_7_button.png", 0.1, "QTE/qte_7_button2.png", 0.1,)
    image qte_8_button_anim = Animation("QTE/qte_8_button.png", 0.1, "QTE/qte_8_button2.png", 0.1,)
    image qte_9_button_anim = Animation("QTE/qte_9_button.png", 0.1, "QTE/qte_9_button2.png", 0.1,)




    image avenger_1 = "QTE/qte_second1.png"
    image avenger_2 = "QTE/qte_second2.png"
    image avenger_3 = "QTE/qte_second3.png"
    image avenger_4 = "QTE/qte_second4.png"
    image avenger_5 = "QTE/qte_second5.png"
    image avenger_6 = "QTE/qte_second6.png"
    image avenger_7 = "QTE/qte_second7.png"


    image battleaction1 = "QTE/qte01.png"
    image battleaction2 = "QTE/qte02.png"
    image battleaction3 = "QTE/qte03.png"
    image battleaction4 = "QTE/qte04.png"
    image battleaction5 = "QTE/qte05.png"
    image battleaction6 = "QTE/qte06.png"


    image shadowaction = "QTE/lenaqte.png"
    image shadowaction1 = "QTE/lenaqte1.png"
    image shadowaction2 = "QTE/lenaqte2.png"
    image shadowaction3 = "QTE/lenaqte3.png"
    image shadowaction4 = "QTE/lenaqte4.png"
    image shadowaction5 = "QTE/lenaqte5.png"
    image shadowaction6 = "QTE/lenaqte6.png"
    image shadowaction7 = "QTE/lenaqte7.png"





    #Дисклеймер
    image Fl_preview:
        Fl_preview_anim

    image layer = "preview/layer.png"
    image text_1 = "preview/text_1.png"

    image disclaimer_day = "preview/disclaimer_day.jpg"
    image disclaimer_sunset = "preview/disclaimer_sunset.jpg"
    image disclaimer_night = "preview/disclaimer_night.jpg"



    #Прода
    image Proda_layer = "proda/Proda_layer.jpg"
    image Proda_layer_loner = "proda/Proda_layer_loner.jpg"
    image dialogue_box1 = "proda/dialogue_box1.png"
    image dialogue_box2 = "proda/dialogue_box2.png"
    image dialogue_box3 = "proda/dialogue_box3.png"
    image dialogue_box4 = "proda/dialogue_box4.png"
    image dialogue_box5 = "proda/dialogue_box5.png"
    image dialogue_box6 = "proda/dialogue_box6.png"
    image dialogue_box7 = "proda/dialogue_box7.png"
    image dialogue_box8 = "proda/dialogue_box8.png"
    image dialogue_box9 = "proda/dialogue_box9.png"


    image Proda_1 = "proda/Proda_1.png"
    image Proda_2 = "proda/Proda_2.png"
    image Proda_3 = "proda/Proda_3.png"
    image Proda_4 = "proda/Proda_4.png"
    image Proda_5 = "proda/Proda_5.png"
    image Proda_6 = "proda/Proda_6.png"
    image Proda_7 = "proda/Proda_7.png"
    image Proda_8 = "proda/Proda_8.png"


    #Подсказки
    image Fl_podsk_1 = "podsk/Fl_podsk_1.png"
    image Fl_podsk_2 = "podsk/Fl_podsk_2.png"



    #Заставка
    image Fl_intro1 = "intro/Fl_intro1.jpg"
    image Fl_intro2 = "intro/Fl_intro2.jpg"
    image Fl_intro3 = "intro/Fl_intro3.jpg"
    image Fl_intro3_1 = "intro/Fl_intro3_1.jpg"
    image Fl_intro3_2 = "intro/Fl_intro3_2.jpg"
    image Fl_intro_text1 = "intro/Fl_intro_text1.png"
    image Fl_intro_text2 = "intro/Fl_intro_text2.png"
    image Fl_intro2_text1 = "intro/Fl_intro2_text1.png"
    image Fl_intro2_text2 = "intro/Fl_intro2_text2.png"
    image Fl_intro3_text1 = "intro/Fl_intro3_text1.png"
    image Fl_intro3_text2 = "intro/Fl_intro3_text2.png"
    image Fl_intro3_text3 = "intro/Fl_intro3_text3.png"
    image Fl_intro3_text4 = "intro/Fl_intro3_text4.png"

    #DLS
    image Fl_q_66_1 = "intro/dls/Fl_q_66_1.jpg"
    image Fl_q_66_2 = "intro/dls/Fl_q_66_2.jpg"
    image Fl_q_66_3 = "intro/dls/Fl_q_66_3.jpg"
    image Fl_q_66_4 = "intro/dls/Fl_q_66_4.jpg"
    image Fl_q_66_text1 = "intro/dls/Fl_q_66_text1.png"
    image Fl_q_66_text2 = "intro/dls/Fl_q_66_text2.png"
    image Fl_q_66_text3 = "intro/dls/Fl_q_66_text3.png"
    image Fl_q_66_text4 = "intro/dls/Fl_q_66_text4.png"




    #Достижения
    image Fl_dost_1_in_kod = "gui/progress/Fl_dost_1_in_kod.png"
    image Fl_dost_2_in_kod = "gui/progress/Fl_dost_2_in_kod.png"
    image Fl_dost_3_in_kod = "gui/progress/Fl_dost_3_in_kod.png"
    image Fl_dost_4_in_kod = "gui/progress/Fl_dost_4_in_kod.png"
    image Fl_dost_5_in_kod = "gui/progress/Fl_dost_5_in_kod.png"
    image Fl_dost_6_in_kod = "gui/progress/Fl_dost_6_in_kod.png"
    image Fl_dost_7_in_kod = "gui/progress/Fl_dost_7_in_kod.png"
    image Fl_dost_8_in_kod = "gui/progress/Fl_dost_8_in_kod.png"
    image Fl_dost_9_in_kod = "gui/progress/Fl_dost_9_in_kod.png"
    image Fl_dost_10_in_kod = "gui/progress/Fl_dost_10_in_kod.png"
    image Fl_dost_11_in_kod = "gui/progress/Fl_dost_11_in_kod.png"
    



    #ТЕКСТ
    image Fl_pause = "text/Fl_pause.jpg"
    image Fl_void = "text/Fl_void.jpg"
    image Fl_proda = "text/Fl_proda.jpg"

    image Fl_week_1 = "text/Fl_week_1.jpg"
    image Fl_week_2 = "text/Fl_week_2.jpg"

    image Fl_dls_q66_1 = "text/Fl_dls_q66_1.jpg"
    image Fl_dls_q66_2 = "text/Fl_dls_q66_2.jpg"




    #ИЗОБРАЖЕНИЯ ОБЪЕКТНЫЕ
    image Fl_sl_fly = "objects/Fl_sl_fly.png"
    image Fl_room_gg_snow_zad = "objects/Fl_komnata_snow_zad.png"
    image Fl_room_gg_snow = "objects/Fl_komnata_snow_layer.png"
    image Fl_room_gg_rain_zad = "objects/Fl_komnata_rain_zad.png"
    image Fl_room_gg_rain = "objects/Fl_komnata_rain_layer.png"
    image Fl_ext_camp_entrance_night_vision_uvao = "objects/Fl_ext_camp_entrance_night_vision_uvao.png"
    image Fl_skrim = "objects/Fl_skrim.png"
    image Fl_skrim2 = "objects/Fl_skrim2.jpg"
    image Fl_game_over1 = "objects/Fl_game_over1.png"
    image Fl_game_over2 = "objects/Fl_game_over2.png"
    image Fl_chair = "objects/Fl_chair.png"
    image Fl_chair2 = "objects/Fl_chair2.png"
    image Fl_chair3 = "objects/Fl_chair3.png"
    image Fl_int_house_of_un_night_mi_sleep = "objects/Fl_int_house_of_un_night_mi_sleep.png"
    image Fl_int_mi_house_shadow = "objects/Fl_int_mi_house_shadow.png"
    image Fl_int_mi_house_shadow2 = "objects/Fl_int_mi_house_shadow2.png"
    image Fl_kitchen_gray = "objects/Fl_kitchen_gray.png"
    image Fl_kitchen_layer = "objects/Fl_kitchen_layer.png"
    image Fl_q_66_layer = "objects/Fl_q_66_layer.png"
    image Fl_food = "objects/Fl_food.png"

    image kr_dream = "objects/kr_dream.png"
    image mi_dream = "objects/mi_dream.png"



    #ИЗОБРАЖЕНИЯ ДЛЯ АНИМАЦИЙ
    image Fl_prologue_1 = "anim/Fl_prologue_1.png"
    image Fl_prologue_2 = "anim/Fl_prologue_2.png"
    image Fl_prologue_3 = "anim/Fl_prologue_3.png"
    image Fl_blink_up = "anim/Fl_blink_up.png"
    image Fl_blink_down = "anim/Fl_blink_down.png"
    image Fl_pulsing1 = "anim/Fl_pulsing1.png"
    image Fl_pulsing2 = "anim/Fl_pulsing2.png"
    image Fl_pulsing3 = "anim/Fl_pulsing3.png"



    #ИЗОБРАЖЕНИЯ С ЭФФЕКТАМИ
    image Fl_int_bus_red = "effects/Fl_int_bus_red.jpg"
    image Fl_ext_bus_red = "effects/Fl_ext_bus_red.jpg"
    image Fl_ext_sea_red = "effects/Fl_ext_sea_red.jpg"
    image Fl_ext_house_of_mt_red = "effects/Fl_ext_house_of_mt_red.jpg"
    image Fl_int_house_of_mt_red = "effects/Fl_int_house_of_mt_red.jpg"
    image Fl_ext_camp_entrance_red = "effects/Fl_ext_camp_entrance_red.jpg"
    image Fl_tunnel_blur = "effects/Fl_tunnel_blur.jpg"
    image Fl_tunnel_blur2 = "effects/Fl_tunnel_blur2.jpg"
    image Fl_mine_elevator_blur = "effects/Fl_mine_elevator_blur.jpg"
    image Fl_desolation = "effects/Fl_desolation.jpg"
    image Fl_desolation2 = "effects/Fl_desolation2.jpg"
    image Fl_desolation3 = "effects/Fl_desolation3.jpg"
    image Fl_ext_bus_light = "effects/Fl_ext_bus_light.png"
    image Fl_ext_bus_light2 = "effects/Fl_ext_bus_light2.png"
    image Fl_ext_bus_light3 = "effects/Fl_ext_bus_light3.png"
    image Fl_ext_camp_entrance_night_vision = "effects/Fl_ext_camp_entrance_night_vision.png"
    image Fl_ext_houses_night_bl = "effects/Fl_ext_houses_night_bl.png"
    image Fl_ext_houses_day_glitch = "effects/Fl_ext_houses_day_glitch.png"
    image Fl_ext_square_day_glitch = "effects/Fl_ext_square_day_glitch.png"
    image Fl_ext_houses_day_sep = "effects/Fl_ext_houses_day_sep.png"
    image Fl_desolation_bl = "effects/Fl_desolation_bl.png"
    image Fl_int_aidpost_night_lamplight2 = "effects/Fl_int_aidpost_night_lamplight2.png"



    #ИЗОБРАЖЕНИЯ С АНИМАЦИЯМИ
    image Fl_r_effect: 
        "images/special/Fl_r_ef1.jpg"
        0.1
        "images/special/Fl_r_ef2.jpg"
        0.1
        "images/special/Fl_r_ef3.jpg"
        0.1
        repeat

    image Fl_rage:
        "Fl_rage1" with Fl_dissolve1
        pause 2.0
        "Fl_rage2" with Fl_dissolve1
        pause 2.0
        repeat



    image Fl_blink:
        contains:
            "Fl_blink_up"
            pos (0,-1080)
            ease 1.5 xalign 0 yalign 0
        contains:
            "Fl_blink_down"
            pos (0,1080)
            ease 1.5 xalign 0 yalign 0


    image Fl_blinking:
        contains:
            "Fl_blink_up"
            pos (0,-1080)
            ease 1.5 xalign 0 yalign 0
        contains:
            "Fl_blink_down"
            pos (0,1080)
            ease 1.5 xalign 0 yalign 0
        pause 2.0
        contains:
            "Fl_blink_up"
            xalign 0 yalign 0
            ease 1.5 pos (0,-1080)
        contains:
            "Fl_blink_down"
            xalign 0 yalign 0
            ease 1.5 pos (0,1080)

    image Fl_unblink:
        contains:
            "Fl_blink_up"
            xalign 0 yalign 0
            ease 1.5 pos (0,-1080)
        contains:
            "Fl_blink_down"
            xalign 0 yalign 0
            ease 1.5 pos (0,1080)


    image Fl_pulsing:
        subpixel True
        "Fl_pulsing1"
        pause(0.2) 
        "Fl_pulsing2"
        pause(0.2) 
        "Fl_pulsing3"
        pause(0.2) 
        "Fl_pulsing2"
        repeat


    image Fl_prolog_dream:
        subpixel True
        "Fl_prologue_1"
        pause(0.1) 
        "Fl_prologue_2"
        pause(0.1) 
        "Fl_prologue_3"
        pause(0.1) 
        "Fl_prologue_2"
        repeat


    image Fl_houses_day1_bl:
        subpixel True
        "Fl_houses_day1_bl_1" with Fl_dissolve2
        pause(3.0) 
        "Fl_houses_day1_bl_2" with Fl_dissolve2
        pause(3.0) 


    image Fl_houses_day1_bl_1:
        subpixel True
        "bg Fl_ext_houses_night"
        Fl_bg_rotate(5.0, 5.0, 3.2, -3.2, 1.5)


    image Fl_houses_day1_bl_2:
        subpixel True
        "Fl_ext_houses_night_bl"
        Fl_bg_rotate(5.0, 5.0, 3.2, -3.2, 1.5)


    image bg Fl_train_rain:
        subpixel True
        "objects/Fl_mm_1.png" with Fl_dissolve1
        pause(5)
        "objects/Fl_mm_2.png" with Fl_dissolve1
        pause(4)
        "objects/Fl_mm_3.png" with Fl_dissolve1
        pause(5)
        "objects/Fl_mm_1.png" with Fl_dissolve1
        pause(4)
        repeat


    image Fl_unblink:
        subpixel True
        contains:
            "Fl_blink_up"
            xalign 0 yalign 0
            ease 1.5 pos (0,-1080)
        contains:
            "Fl_blink_down"
            xalign 0 yalign 0
            ease 1.5 pos (0,1080)

    image Fl_blink:
        subpixel True
        contains:
            "Fl_blink_up"
            pos (0,-1080)
            ease 1.5 xalign 0 yalign 0
        contains:
            "Fl_blink_down"
            pos (0,1080)
            ease 1.5 xalign 0 yalign 0


    image Fl_blinking:
        subpixel True
        contains:
            "Fl_blink_up"
            pos (0,-1080)
            ease 1.5 xalign 0 yalign 0
        contains:
            "Fl_blink_down"
            pos (0,1080)
            ease 1.5 xalign 0 yalign 0
        pause 2.0
        contains:
            "Fl_blink_up"
            xalign 0 yalign 0
            ease 1.5 pos (0,-1080)
        contains:
            "Fl_blink_down"
            xalign 0 yalign 0
            ease 1.5 pos (0,1080)


    image Fl_music_effect:
        subpixel True
        "Fl_vignette2" with Fl_dissolve1
        pause 3.0
        "Fl_vignette" with Fl_dissolve1
        pause 3.0
        repeat

    image Fl_mute_effect:
        subpixel True
        "Fl_vignette2" with Fl_dissolve1
        pause 2.0
        "Fl_vignette" with Fl_dissolve1
        pause 2.0
        repeat


    image Fl_interference_anim:
        Fl_four_contains_xyzoom_effects("Fl_interference")



    image bg Fl_blink_square_party:
        subpixel True
        "bg Fl_ext_square_night_party" with Dissolve(0.2)
        pause 0.4
        "bg Fl_ext_square_night_party2" with Dissolve(0.2)
        pause 0.4
        repeat

    image bg Fl_blink_square_party_2:
        subpixel True
        "bg Fl_ext_square_night_party" with Dissolve(0.2)
        pause 0.2
        "bg Fl_ext_square_night_party2" with Dissolve(0.2)
        pause 0.2
        repeat

    image bg Fl_blink_square_diskach1:
        subpixel True
        "bg Fl_ext_square_night_party"
        pause .3
        "bg Fl_ext_square_night_party2"
        pause .3
        "bg Fl_ext_square_night_party"
        pause .2
        "bg Fl_ext_square_night_party2"
        pause .2
        "bg Fl_ext_square_night_party"
        pause .1
        "bg Fl_ext_square_night_party2"
        pause .1
        "bg Fl_ext_square_night_party"
        pause .05
        "bg Fl_ext_square_night_party2"
        pause 0.2

    image bg Fl_blink_square_diskach2:
        subpixel True
        "bg Fl_ext_square_night_party"
        pause 0.6
        "bg Fl_ext_square_night_party2"
        pause 0.9
        "bg Fl_ext_square_night_party"
        pause 0.3
        "bg Fl_ext_square_night_party2"
        pause 0.5
        repeat

    image Fl_desolation_anim:
        subpixel True
        "Fl_desolation"
        3.0
        "Fl_desolation2"
        0.1
        "Fl_desolation3"
        0.2
        "Fl_desolation"
        2.0
        "Fl_desolation3"
        0.1
        "Fl_desolation"
        repeat


    image Fl_tunnel_anim:
        subpixel True
        "Fl_tunnel_blur" with Fl_dissolve1
        1.0
        "Fl_tunnel_blur2" with Fl_dissolve1
        0.5
        repeat




    image bg Fl_black = "bg/Fl_black.png"

    #Упоротые
    image Fl_ext_square_uprt_day = "uprt/Fl_ext_square_uprt_day.jpeg"
    image Fl_housesuprt = "uprt/Fl_housesuprt.jpg"
    image Fl_int_aidpost_night_uprt = "uprt/Fl_int_aidpost_night_uprt.jpeg"
    image Fl_int_dining_hall_full_uprt_day = "uprt/Fl_int_dining_hall_full_uprt_day.jpeg"
    image Fl_ext_dining_hall_away_uprt_day = "uprt/Fl_ext_dining_hall_away_uprt_day.jpeg"
    image Fl_ext_dining_hall_near_uprt_day = "uprt/Fl_ext_dining_hall_near_uprt_day.jpeg"
    image uprtal = "uprt/uprtal.png"
    image uprtan = "uprt/uprtan.png"
    image uprtkt = "uprt/uprtkt.png"
    image uprtmv = "uprt/uprtmv.png"
    image uprttolik = "uprt/uprttolik.png"



    #БГ ГГ
    image bg Fl_city = "bg/real_word/Fl_city.png"
    image bg Fl_komnata_vos = "bg/real_word/Fl_komnata_vos.png"
    image bg Fl_padic = "bg/real_word/Fl_padic.jpg"
    image bg Fl_moon_red1 = "bg/real_word/Fl_moon_red1.jpg"
    image bg Fl_moon_red2 = "bg/real_word/Fl_moon_red2.jpg"
    image bg Fl_ext_khruschevka_night = "bg/real_word/Fl_ext_khruschevka_night.jpg"
    image bg Fl_ext_street_night_vos = "bg/real_word/Fl_ext_street_night_vos.jpg"


    #БГ Пустоты
    image bg Fl_black_flash = "bg/space/Fl_black_flash.jpg"
    image bg Fl_black_flash2 = "bg/space/Fl_black_flash2.jpg"
    image bg Fl_pyst = "bg/space/Fl_pyst.jpg"
    image bg Fl_pyst_ch = "bg/space/Fl_pyst_ch.jpg"
    image bg Fl_pyst_red = "bg/space/Fl_pyst_red.jpg"
    image bg Fl_pyst_red_nightmare = "bg/space/Fl_pyst_red_nightmare.jpg"


    #БГ ЛАГЕРЬ(Убийства)
    image bg Fl_int_clubs_blood_day = "bg/blood_lager/Fl_int_clubs_blood_day.jpg"
    image bg Fl_int_musclub_night_blood = "bg/blood_lager/Fl_int_musclub_night_blood.jpg"
    image bg Fl_ext_square_day_blood = "bg/blood_lager/Fl_ext_square_day_blood.jpg"
    image bg Fl_int_clubs_blood_night_light = "bg/blood_lager/Fl_int_clubs_blood_night_light.jpg"
    image bg Fl_int_clubs_blood_night = "bg/blood_lager/Fl_int_clubs_blood_night.jpg"
    image bg Fl_ext_bus_kt_dead = "bg/blood_lager/Fl_ext_bus_kt_dead.jpg"
    image bg Fl_int_musclub_sunset_blood = "bg/blood_lager/Fl_int_musclub_sunset_blood.jpg"
    image bg Fl_int_sklad_night_blood = "bg/blood_lager/Fl_int_sklad_night_blood.jpg"


    #БГ ЛАГЕРЬ(Убийства)
    image bg Fl_houses_ruined = "bg/ruined/Fl_houses_ruined.jpg"
    image bg Fl_library_outside_ruined = "bg/ruined/Fl_library_outside_ruined.jpg"
    image bg Fl_medical_point_inside_ruined = "bg/ruined/Fl_medical_point_inside_ruined.jpg"
    image bg Fl_workshop_outside_ruined = "bg/ruined/Fl_workshop_outside_ruined.jpg"


    #БГ ЛАГЕРЬ(Зима)
    image bg Fl_ext_musclub_day_winter = "bg/winter/Fl_ext_musclub_day_winter.jpg"
    image bg Fl_house_of_mt_day_winter = "bg/winter/Fl_house_of_mt_day_winter.jpg"
    image bg Fl_ext_dining_hall_near_winter = "bg/winter/Fl_ext_dining_hall_near_winter.jpg"
    image bg Fl_ext_houses_winter = "bg/winter/Fl_ext_houses_winter.jpg"
    image bg Fl_ext_entrance_winter = "bg/winter/Fl_ext_entrance_winter.jpg"


    #БГ ЛАГЕРЬ(Дождь)
    image Fl_int_musclub_rain = "bg/rain/Fl_int_musclub_rain.png"
    image Fl_int_musclub_rain2 = "bg/rain/Fl_int_musclub_rain2.png"
    image Fl_int_musclub_rain3 = "bg/rain/Fl_int_musclub_rain3.jpg"
    image Fl_int_house_of_mt_rain = "bg/rain/Fl_int_house_of_mt_rain.png"
    image Fl_int_house_of_mt_rain2 = "bg/rain/Fl_int_house_of_mt_rain2.png"
    image Fl_int_house_of_mt_rain3 = "bg/rain/Fl_int_house_of_mt_rain3.jpg"
    image Fl_ext_musclub_rain = "bg/rain/Fl_ext_musclub_rain.jpg"
    image Fl_ext_musclub_rain_night = "bg/rain/Fl_ext_musclub_rain_night.jpg"
    image Fl_ext_dining_hall_away_rain = "bg/rain/Fl_ext_dining_hall_away_rain.jpg"
    image Fl_ext_dining_hall_near_rain = "bg/rain/Fl_ext_dining_hall_near_rain.jpg"
    image Fl_ext_house_of_mt_rain = "bg/rain/Fl_ext_house_of_mt_rain.jpg"
    image Fl_ext_houses_rain = "bg/rain/Fl_ext_houses_rain.jpg"
    image Fl_ext_houses_rain_night = "bg/rain/Fl_ext_houses_rain_night.jpg"
    image Fl_ext_no_bus_rain = "bg/rain/Fl_ext_no_bus_rain.jpg"
    image Fl_ext_square_rain = "bg/rain/Fl_ext_square_rain.jpg"
    image Fl_ext_boathouse_rain = "bg/rain/Fl_ext_boathouse_rain.jpg"
    image Fl_ext_path_rain = "bg/rain/Fl_ext_path_rain.jpg"
    image Fl_ext_clubs_rain = "bg/rain/Fl_ext_clubs_rain.jpg"
    image Fl_ext_square_rain_night = "bg/rain/Fl_ext_square_rain_night.jpg"
    image Fl_musclub_rain = "bg/rain/Fl_musclub_rain.jpg"
    image Fl_ext_clubs_rain_night = "bg/rain/Fl_ext_clubs_rain_night.jpg"
    image Fl_squere_rain_night = "bg/rain/Fl_squere_rain_night.jpg"
    image Fl_ext_house_of_mt_rain_night_light = "bg/rain/Fl_ext_house_of_mt_rain_night_light.jpg"
    image Fl_sky_rain_nht = "bg/rain/Fl_sky_rain_nht.jpg"


    #БГ ЛАГЕРЬ
    image bg Fl_ext_boathouse_alt_night = "bg/Fl_ext_boathouse_alt_night.png"
    image bg Fl_ext_houses_night = "bg/Fl_ext_houses_night.png"
    image bg Fl_ext_houses_night2 = "bg/Fl_ext_houses_night2.jpg"
    image bg Fl_ext_sky_day = "bg/Fl_ext_sky_day.jpg"
    image bg Fl_int_clubs_night_TV = "bg/Fl_int_clubs_night_TV.png"
    image bg Fl_ext_road_day = "bg/Fl_ext_road_day.jpg"
    image bg Fl_ext_bus = "bg/Fl_ext_bus.jpg"
    image bg Fl_ext_no_bus = "bg/Fl_ext_no_bus.jpg"
    image bg Fl_night_sky_lager = "bg/Fl_night_sky_lager.jpg"
    image bg Fl_ext_camp_entrance_day = "bg/Fl_ext_camp_entrance_day.jpg"
    image bg Fl_ext_clubs_day = "bg/Fl_ext_clubs_day.jpg"
    image bg Fl_ext_clubs_night = "bg/Fl_ext_clubs_night.jpg"
    image bg Fl_ext_square_day = "bg/Fl_ext_square_day.jpg"
    image bg Fl_ext_square_sunset = "bg/Fl_ext_square_sunset.jpg"
    image bg Fl_ext_houses_day = "bg/Fl_ext_houses_day.jpg"
    image bg Fl_ext_house_of_dv_day = "bg/Fl_ext_house_of_dv_day.jpg"
    image bg Fl_ext_houses2_day = "bg/Fl_ext_houses2_day.png"
    image bg Fl_sklad_day = "bg/Fl_sklad_day.jpg"
    image bg Fl_sklad_sunset = "bg/Fl_sklad_sunset.jpg"
    image bg Fl_house_of_mt_day = "bg/Fl_house_of_mt_day.jpg"
    image bg Fl_house_of_mt_sunset = "bg/Fl_house_of_mt_sunset.jpg"
    image bg Fl_int_house_of_mv_day = "bg/Fl_int_house_of_mv_day.jpg"
    image bg Fl_int_house_of_mv_sunset = "bg/Fl_int_house_of_mv_sunset.jpg"
    image bg Fl_ext_musclub_day = "bg/Fl_ext_musclub_day.jpg"
    image bg Fl_ext_musclub_night = "bg/Fl_ext_musclub_night.png"
    image bg Fl_ext_musclub_sunset = "bg/Fl_ext_musclub_sunset.png"
    image bg Fl_ext_musclub_verandah_day = "bg/Fl_ext_musclub_verandah_day.png"
    image bg Fl_ext_musclub_verandah_night = "bg/Fl_ext_musclub_verandah_night.png"
    image bg Fl_ext_musclub_verandah_sunset = "bg/Fl_ext_musclub_verandah_sunset.png"
    image bg Fl_int_musclub_mattresses_day = "bg/Fl_int_musclub_mattresses_day.png"
    image bg Fl_int_musclub_mattresses_night = "bg/Fl_int_musclub_mattresses_night.png"
    image bg Fl_int_musclub_mattresses_sunset = "bg/Fl_int_musclub_mattresses_sunset.png"
    image bg Fl_ext_dining_bench_sunset = "bg/Fl_ext_dining_bench_sunset.png"
    image bg Fl_int_house_of_un_ceiling_rain = "bg/Fl_int_house_of_un_ceiling_rain.png"
    image bg Fl_int_house_of_un_right_side_night = "bg/Fl_int_house_of_un_right_side_night.png"
    image bg Fl_ext_dining_bench_day = "bg/Fl_ext_dining_bench_day.png"
    image bg Fl_ext_dining_hall_near_day = "bg/Fl_ext_dining_hall_near_day.jpg"
    image bg Fl_ext_dining_hall_near_night = "bg/Fl_ext_dining_hall_near_night.jpg"
    image bg Fl_ext_dining_hall_near_sunset = "bg/Fl_ext_dining_hall_near_sunset.jpg"
    image bg Fl_int_dining_hall_day = "bg/Fl_int_dining_hall_day.jpg"
    image bg Fl_int_dining_hall_people_day = "bg/Fl_int_dining_hall_people_day.jpg"
    image bg Fl_int_dining_hall_sunset = "bg/Fl_int_dining_hall_sunset.jpg"
    image bg Fl_int_house_of_mi_day = "bg/Fl_int_house_of_mi_day.jpg"
    image bg Fl_int_house_of_mi_sunset = "bg/Fl_int_house_of_mi_sunset.jpg"
    image bg Fl_int_house_of_mi_night = "bg/Fl_int_house_of_mi_night.jpg"
    image bg Fl_ext_house_of_mi_day = "bg/Fl_ext_house_of_mi_day.jpg"
    image bg Fl_ext_warehouse_day = "bg/Fl_ext_warehouse_day.jpg"
    image bg Fl_ext_warehouse_sunset = "bg/Fl_ext_warehouse_sunset.jpg"
    image bg Fl_int_sklad_day = "bg/Fl_int_sklad_day.jpg"
    image bg Fl_int_sklad_night = "bg/Fl_int_sklad_night.jpg"
    image bg Fl_ext_warehouse_night = "bg/Fl_ext_warehouse_night.jpg"
    image bg Fl_ext_house_of_mi_sunset = "bg/Fl_ext_house_of_mi_sunset.png"
    image bg Fl_ext_house_of_mi_night = "bg/Fl_ext_house_of_mi_night.jpg"
    image bg Fl_ext_square_night_skaz = "bg/Fl_ext_square_night_skaz.png"
    image bg Fl_int_editorial_day = "bg/Fl_int_editorial_day.jpg"
    image bg Fl_ext_beach_day = "bg/Fl_ext_beach_day.jpg"
    image bg Fl_ext_beach_sunset = "bg/Fl_ext_beach_sunset.jpg"
    image bg Fl_ext_beach_night = "bg/Fl_ext_beach_night.jpg"
    image bg Fl_ext_playground_day = "bg/Fl_ext_playground_day.jpg"
    image bg Fl_playground_sunset = "bg/Fl_playground_sunset.jpg"
    image bg Fl_ext_playground_night = "bg/Fl_ext_playground_night.jpg"
    image bg Fl_ext_boathouse_day = "bg/Fl_ext_boathouse_day.jpg"
    image bg Fl_ext_boathouse_sunset = "bg/Fl_ext_boathouse_sunset.png"
    image bg Fl_ext_boathouse_night = "bg/Fl_ext_boathouse_night.jpg"
    image bg Fl_ext_houses_sunset = "bg/Fl_ext_houses_sunset.jpg"
    image bg Fl_ext_houses2_sunset = "bg/Fl_ext_houses2_sunset.jpg"
    image bg Fl_int_house_yan_day = "bg/Fl_int_house_yan_day.jpg"
    image bg Fl_int_house_yan_night = "bg/Fl_int_house_yan_night.jpg"
    image bg Fl_sky = "bg/Fl_sky.jpg"
    image bg Fl_hor_les_obr1 = "bg/Fl_hor_les_obr1.jpg"
    image bg Fl_mine_elevator_down = "bg/Fl_mine_elevator_down.jpg"
    image bg Fl_mine_elevator_up = "bg/Fl_mine_elevator_up.jpg"
    image bg Fl_int_laboratory = "bg/Fl_int_laboratory.jpg"
    image bg Fl_int_tunnel = "bg/Fl_int_tunnel.jpg"
    image bg Fl_int_tunnel_with_door = "bg/Fl_int_tunnel_with_door.jpg"
    image bg Fl_ext_washstand_day = "bg/Fl_ext_washstand_day.png"
    image bg Fl_int_clubs_night_light = "bg/Fl_int_clubs_night_light.png"
    image bg Fl_nt_aidpost_sunset = "bg/Fl_nt_aidpost_sunset.png"
    image bg Fl_int_sporthall_day = "bg/Fl_int_sporthall_day.jpg"
    image bg Fl_int_sporthall_night = "bg/Fl_int_sporthall_night.jpg"
    image bg Fl_int_clubs_dj = "bg/Fl_int_clubs_dj.jpg"
    image bg Fl_int_clubs_dj_nolight = "bg/Fl_int_clubs_dj_nolight.jpg"
    image bg Fl_ext_medstation_night_light = "bg/Fl_ext_medstation_night_light.jpg"
    image bg Fl_ext_path_night = "bg/Fl_ext_path_night.jpg"
    image bg Fl_ext_ymiv_vbl = "bg/Fl_ext_ymiv_vbl.jpg"
    image bg Fl_ext_ymivalniki = "bg/Fl_ext_ymivalniki.jpg"
    image bg Fl_int_clubs_male_night = "bg/Fl_int_clubs_male_night.jpg"
    image bg Fl_int_extra_house_day = "bg/Fl_int_extra_house_day.jpg"
    image bg Fl_int_extra_house_night = "bg/Fl_int_extra_house_night.jpg"
    image bg Fl_int_clubs_male_sunset = "bg/Fl_int_clubs_male_sunset.jpg"
    image bg Fl_int_clubs_male_day = "bg/Fl_int_clubs_male_day.jpg"
    image bg Fl_int_aidpost_day = "bg/Fl_int_aidpost_day.jpg"
    image bg Fl_int_aidpost_night = "bg/Fl_int_aidpost_night.jpg"
    image bg Fl_ext_aidpost_day = "bg/Fl_ext_aidpost_day.jpg"
    image bg Fl_ext_aidpost_night = "bg/Fl_ext_aidpost_night.jpg"
    image bg Fl_int_library_day = "bg/Fl_int_library_day.jpg"
    image bg Fl_int_library_night = "bg/Fl_int_library_night.jpg"
    image bg Fl_int_library_night2 = "bg/Fl_int_library_night2.jpg"
    image bg Fl_ext_washstand2_day = "bg/Fl_ext_washstand2_day.jpg"
    image bg Fl_ext_library_sunset = "bg/Fl_ext_library_sunset.png"
    image bg Fl_ext_library_day = "bg/Fl_ext_library_day.jpg"
    image bg Fl_ext_library_night = "bg/Fl_ext_library_night.jpg"
    image bg Fl_int_dining_hall_people_sunset = "bg/Fl_int_dining_hall_people_sunset.jpg"
    image bg Fl_ext_path_day = "bg/Fl_ext_path_day.jpg"
    image bg Fl_ext_path2_day = "bg/Fl_ext_path2_day.jpg"
    image bg Fl_ext_artroom_day = "bg/Fl_ext_artroom_day.jpg"
    image bg Fl_ext_artroom_sunaet = "bg/Fl_ext_artroom_sunaet.jpg"
    image bg Fl_ext_dom_day = "bg/Fl_ext_dom_day.jpg"
    image bg Fl_ext_dining_hall_away_day = "bg/Fl_ext_dining_hall_away_day.jpg"
    image bg Fl_ext_dom_sunset = "bg/Fl_ext_dom_sunset.jpg"
    image bg Fl_ext_dom_night = "bg/Fl_ext_dom_night.jpg"
    image bg Fl_int_extra_dom_sunset = "bg/Fl_int_extra_dom_sunset.jpg"
    image bg Fl_int_kitchen_day = "bg/Fl_int_kitchen_day.jpg"
    image bg Fl_int_kitchen_night = "bg/Fl_int_kitchen_night.jpg"
    image bg Fl_int_music_club_mattresses_night_lights_on = "bg/Fl_int_music_club_mattresses_night_lights_on.jpg"
    image bg Fl_ext_forest_sunset_holm = "bg/Fl_ext_forest_sunset_holm.jpg"
    image bg Fl_ext_house_of_dv_night = "bg/Fl_ext_house_of_dv_night.jpg"
    image bg Fl_int_bus_people_night = "bg/Fl_int_bus_people_night.jpg"
    image bg Fl_int_bus = "bg/Fl_int_bus.jpg"
    image bg Fl_int_house_of_sl_night2 = "bg/Fl_int_house_of_sl_night2.jpg"
    image bg Fl_int_catacombs_entrance_lighter = "bg/Fl_int_catacombs_entrance_lighter.png"
    image bg Fl_ext_musclub_night2 = "bg/Fl_ext_musclub_night2.png"
    image bg Fl_ext_musclub_night3 = "bg/Fl_ext_musclub_night3.png"
    image bg Fl_int_musclub_night = "bg/Fl_int_musclub_night.jpg"
    image bg Fl_int_mine_coalface_lighter = "bg/Fl_int_mine_coalface_lighter.png"
    image bg Fl_int_mine_crossroad_lighter = "bg/Fl_int_mine_crossroad_lighter.png"
    image bg Fl_int_mine_door_lighter = "bg/Fl_int_mine_door_lighter.png"
    image bg Fl_int_mine_halt_lighter = "bg/Fl_int_mine_halt_lighter.png"
    image bg Fl_int_mine_room_ligher = "bg/Fl_int_mine_room_ligher.png"
    image bg Fl_int_mine_wallbreak = "bg/Fl_int_mine_wallbreak.png"
    image bg Fl_ext_admin_day = "bg/Fl_ext_admin_day.png"
    image bg Fl_int_library_cellar_day = "bg/Fl_int_library_cellar_day.png"
    image bg Fl_ext_musclub_fire = "bg/Fl_ext_musclub_fire.png"
    image bg Fl_int_catacombs_entrance_new = "bg/Fl_int_catacombs_entrance_new.png"
    image bg Fl_int_catacombs_entrance_new_light = "bg/Fl_int_catacombs_entrance_new_light.png"
    image bg Fl_coridor = "bg/Fl_coridor.png"
    image bg Fl_int_old_building_floorroom_night = "bg/Fl_int_old_building_floorroom_night.png"
    image bg Fl_ext_path_dark = "bg/Fl_ext_path_dark.jpg"
    image bg Fl_ext_camp_entrance_night = "bg/Fl_ext_camp_entrance_night.jpg"
    image bg Fl_ext_no_bus_night = "bg/Fl_ext_no_bus_night.jpg"
    image bg Fl_ext_path_sunset = "bg/Fl_ext_path_sunset.jpg"
    image bg Fl_ext_path2_night = "bg/Fl_ext_path2_night.jpg"
    image bg Fl_ext_square_night = "bg/Fl_ext_square_night.jpg"
    image bg Fl_ext_square_night2 = "bg/Fl_ext_square_night2.jpg"
    image bg Fl_koridor_ma_son_obr = "bg/Fl_koridor_ma_son_obr.jpg"
    image bg Fl_int_house_of_mt_night2 = "bg/Fl_int_house_of_mt_night2.jpg"
    image bg Fl_ext_house_of_mt_night_without_light = "bg/Fl_ext_house_of_mt_night_without_light.jpg"
    image bg Fl_underwater = "bg/Fl_underwater.jpg"
    image bg Fl_underwater2 = "bg/Fl_underwater2.jpg"
    image bg Fl_underwater3 = "bg/Fl_underwater3.jpg"
    image bg Fl_int_musclub_day = "bg/Fl_int_musclub_day.jpg"
    image bg Fl_int_house_of_sl_day = "bg/Fl_int_house_of_sl_day.jpg"
    image bg Fl_ext_house_of_sl_day = "bg/Fl_ext_house_of_sl_day.jpg"
    image bg Fl_ext_path2_dark = "bg/Fl_ext_path2_dark.jpg"
    image bg Fl_int_medstation = "bg/Fl_int_medstation.jpg"
    image bg Fl_int_mine = "bg/Fl_int_mine.jpg"
    image bg Fl_int_mine_crossroad = "bg/Fl_int_mine_crossroad.jpg"
    image bg Fl_int_mine_door = "bg/Fl_int_mine_door.jpg"
    image bg Fl_int_mine_halt = "bg/Fl_int_mine_halt.jpg"
    image bg Fl_int_mine_room = "bg/Fl_int_mine_room.jpg"
    image bg Fl_int_mine_exit_night_light = "bg/Fl_int_mine_exit_night_light.jpg"
    image bg Fl_int_musclub_sunset = "bg/Fl_int_musclub_sunset.jpg"
    image bg Fl_ext_old_building_night = "bg/Fl_ext_old_building_night.jpg"
    image bg Fl_ext_old_building_night_moonlight = "bg/Fl_ext_old_building_night_moonlight.jpg"
    image bg Fl_ext_old_building_day = "bg/Fl_ext_old_building_day.jpg"
    image bg Fl_ext_dining_hall_away_sunset = "bg/Fl_ext_dining_hall_away_sunset.jpg"
    image bg Fl_int_old_building_night = "bg/Fl_int_old_building_night.jpg"
    image bg Fl_int_mine_coalface = "bg/Fl_int_mine_coalface.jpg"
    image bg Fl_int_mine_room_dark = "bg/Fl_int_mine_room_dark.jpg"
    image bg Fl_ext_square_night_party = "bg/Fl_ext_square_night_party.jpg"
    image bg Fl_ext_square_night_party2 = "bg/Fl_ext_square_night_party2.jpg"
    image bg Fl_ext_beach_water_sunset = "bg/Fl_ext_beach_water_sunset.jpg"
    image bg Fl_ext_forest_day_rainy = "bg/Fl_ext_forest_day_rainy.jpg"
    image bg Fl_ext_forest2_day_rainy = "bg/Fl_ext_forest2_day_rainy.jpg"
    image bg Fl_ext_bus_red = "bg/Fl_ext_bus_red.jpg"
    image bg Fl_palata_loner = "bg/Fl_palata_loner.jpg"
    image bg Fl_bynker = "bg/Fl_bynker.jpg"
    image bg Fl_bynker_dark = "bg/Fl_bynker_dark.jpg"
    image bg Fl_bynker_pr = "bg/Fl_bynker_pr.jpg"
    image bg Fl_bynker_light = "bg/Fl_bynker_light.jpg"
    image bg Fl_bynker_light_no_door = "bg/Fl_bynker_light_no_door.jpg"
    image bg Fl_ext_polyana_night = "bg/Fl_ext_polyana_night.jpg"
    image bg Fl_ext_bathhouse_night = "bg/Fl_ext_bathhouse_night.jpg"
    image bg Fl_int_aidpost_night_nolight = "bg/Fl_int_aidpost_night_nolight.jpg"
    image bg Fl_int_aidpost_lamp = "bg/Fl_int_aidpost_lamp.jpg"
    image bg Fl_int_bathhouse = "bg/Fl_int_bathhouse.jpg"
    image bg Fl_int_warehouse_day = "bg/Fl_int_warehouse_day.jpg"
    image bg Fl_int_warehouse3_day = "bg/Fl_int_warehouse3_day.jpg"
    image bg Fl_int_warehouse3_night = "bg/Fl_int_warehouse3_night.jpg"
    image bg Fl_ext_sky_sunset = "bg/Fl_ext_sky_sunset.jpg"
    image bg Fl_ext_backdoor_day = "bg/Fl_ext_backdoor_day.jpg"
    image bg Fl_ext_backdoor_sunset = "bg/Fl_ext_backdoor_sunset.jpg"
    image bg Fl_ext_backdoor_night = "bg/Fl_ext_backdoor_night.jpg"
    image bg Fl_ext_un_hideout_day = "bg/Fl_ext_un_hideout_day.jpg"
    image bg Fl_ext_un_hideout_sunset = "bg/Fl_ext_un_hideout_sunset.jpg"
    image bg Fl_ext_un_hideout_night = "bg/Fl_ext_un_hideout_night.jpg"
    image bg Fl_ext_platform_train = "bg/Fl_ext_platform_train.jpg"
    image bg Fl_int_medstation_zombie = "bg/Fl_int_medstation_zombie.jpg"
    image bg Fl_int_infirmary = "bg/Fl_int_infirmary.jpg"
    image bg Fl_int_shower = "bg/Fl_int_shower.png"
    image bg Fl_int_shower_light = "bg/Fl_int_shower_light.png"
    image bg Fl_int_shower_no_light = "bg/Fl_int_shower_no_light.png"
    image bg Fl_int_shower_no_light2 = "bg/Fl_int_shower_no_light2.png"
    image bg Fl_int_house_sn_vk_night = "bg/Fl_int_house_sn_vk_night.png"
    image bg Fl_ext_house_gr_night = "bg/Fl_ext_house_gr_night.png"




    #CG
    image cg Fl_hent_uri = "cg/Fl_hent_uri.jpg"
    image cg Fl_vogatay_hot = "cg/Fl_vogatay_hot.jpg"
    image cg Fl_d1_food_fork = "cg/Fl_d1_food_fork.png"
    image cg Fl_d1_food_normal = "cg/Fl_d1_food_normal.jpg"
    image cg Fl_boathouse_lena = "cg/Fl_boathouse_lena.jpg"
    image cg Fl_micu_lib = "cg/Fl_micu_lib.jpg"
    image cg Fl_mi_sleeping_happily = "cg/Fl_mi_sleeping_happily.png"
    image cg Fl_msk_canteen_rage = "cg/Fl_msk_canteen_rage.png"
    image cg Fl_mi_eye = "cg/Fl_mi_eye.png"
    image cg Fl_mi_bath_1 = "cg/Fl_mi_bath_1.png"
    image cg Fl_catmiku = "cg/Fl_catmiku.jpg"
    image cg Fl_madness = "cg/Fl_madness.jpg"
    image cg Fl_un_fireyes1 = "cg/Fl_un_fireyes1.jpg"
    image cg Fl_un_fireyes2 = "cg/Fl_un_fireyes2.jpg"





    #CG МИКУ ПЕРВЫЙ ДЕНЬ
    image Fl_light_layer = "cg/mi_d1/Fl_light_layer.png"
    image Fl_ground_night = "cg/mi_d1/Fl_ground_night.png"
    image Fl_ground_no_miku = "cg/mi_d1/Fl_ground_no_miku.png"
    image Fl_brows_happy_night = "cg/mi_d1/Fl_brows_happy_night.png"
    image Fl_brows_sad_night = "cg/mi_d1/Fl_brows_sad_night.png"
    image Fl_eyes_close_night = "cg/mi_d1/Fl_eyes_close_night.png"
    image Fl_eyes_open_night = "cg/mi_d1/Fl_eyes_open_night.png"
    image Fl_mouth_happy_night = "cg/mi_d1/Fl_mouth_happy_night.png"
    image Fl_mouth_normal_night = "cg/mi_d1/Fl_mouth_normal_night.png"
    image Fl_mouth_smile_night = "cg/mi_d1/Fl_mouth_smile_night.png"
    image Fl_mouth_smile2_night = "cg/mi_d1/Fl_mouth_smile2_night.png"




    #CG МИКУ ЧЕТВЁРТЫЙ ДЕНЬ
    image Fl_bed = "cg/mi_d4/Fl_bed.png"
    image Fl_bed_mi_open = "cg/mi_d4/Fl_bed_mi_open.png"
    image Fl_bed_mi_sleep = "cg/mi_d4/Fl_bed_mi_sleep.png"




    #CG НЕИЗВЕСТНЫЕ
    image Fl_ground = "cg/two_in_the_void/Fl_ground.png"
    image Fl_unk1 1 = "cg/two_in_the_void/Fl_unk1_1.png"
    image Fl_unk1 2 = "cg/two_in_the_void/Fl_unk1_2.png"
    image Fl_unk2 1 = "cg/two_in_the_void/Fl_unk2_1.png"
    image Fl_unk2 2 = "cg/two_in_the_void/Fl_unk2_2.png"
    image Fl_unk2 3 = "cg/two_in_the_void/Fl_unk2_3.png"



    #CG DlS_Loner
    image cg Fl_dead_gg_wosp = "cg/dls_loner/Fl_dead_gg_wosp.jpg"
    image cg Fl_dead_gg_wosp_light = "cg/dls_loner/Fl_dead_gg_wosp_light.jpg"
    image cg Fl_dead_pioneer = "cg/dls_loner/Fl_dead_pioneer.jpg"
    image cg Fl_mi_guitar = "cg/dls_loner/Fl_mi_guitar.jpg"
    image cg Fl_miku_piano = "cg/dls_loner/Fl_miku_piano.jpg"
    image cg Fl_lena_catacombs = "cg/dls_loner/Fl_lena_catacombs.png"
    image cg Fl_pioneer_falling = "cg/dls_loner/Fl_pioneer_falling.png"
    image cg Fl_pioneer_falling2 = "cg/dls_loner/Fl_pioneer_falling2.png"
    image cg Fl_mine_fint = "cg/dls_loner/Fl_mine_fint.png"
    image cg Fl_nekto = "cg/dls_loner/Fl_nekto.png"
    image cg Fl_mik = "cg/dls_loner/Fl_mik.png"
    image cg Fl_bloodsquare = "cg/dls_loner/Fl_bloodsquare.png"
    image cg Fl_bloodsquare2 = "cg/dls_loner/Fl_bloodsquare2.jpg"
    image cg Fl_bloodsquare3 = "cg/dls_loner/Fl_bloodsquare3.jpg"
    image cg Fl_bloodsquare4 = "cg/dls_loner/Fl_bloodsquare4.jpg"
    image cg Fl_bloodsquare5 = "cg/dls_loner/Fl_bloodsquare5.jpg"
    image cg Fl_p_say = "cg/dls_loner/Fl_p_say.jpg"
    image cg Fl_vurtal = "cg/dls_loner/Fl_vurtal.jpg"
    image cg Fl_heads_off = "cg/dls_loner/Fl_heads_off.jpg"
    image cg Fl_lip_on_bench_1 = "cg/dls_loner/Fl_lip_on_bench_1.jpg"
    image cg Fl_un_book = "cg/dls_loner/Fl_un_book.jpg"
    image cg Fl_un_knife = "cg/dls_loner/Fl_un_knife.jpg"
    image cg Fl_mine_inside_elevator = "cg/dls_loner/Fl_mine_inside_elevator.jpg"
    image cg Fl_lisa_in_darkness_1 = "cg/dls_loner/Fl_lisa_in_darkness_1.jpg"
    image cg Fl_lisa_in_darkness_2 = "cg/dls_loner/Fl_lisa_in_darkness_2.jpg"
    image cg Fl_lisa_in_darkness_3 = "cg/dls_loner/Fl_lisa_in_darkness_3.jpg"
    image cg Fl_viola_not_wine = "cg/dls_loner/Fl_viola_not_wine.jpg"
    image cg Fl_gg_bol = "cg/dls_loner/Fl_gg_bol.jpg"
    image cg Fl_forest_zombie = "cg/dls_loner/Fl_forest_zombie.jpg"
    image cg Fl_loner_lena = "cg/dls_loner/Fl_loner_lena.jpg"
    image cg Fl_mi_dark = "cg/dls_loner/Fl_mi_dark.jpg"
    image cg Fl_mi_gost = "cg/dls_loner/Fl_mi_gost.jpg"
    image cg Fl_mi_gost2 = "cg/dls_loner/Fl_mi_gost2.jpg"
    image cg Fl_mi_gost3 = "cg/dls_loner/Fl_mi_gost3.jpg"
    image cg Fl_mi_gost4 = "cg/dls_loner/Fl_mi_gost4.jpg"
    





init -15:
    #Переменные
    $ hp = 0
    $ ph = 0
    $ it_0 = 0
    $ it_1 = 0
    $ it_2 = 0
    $ it_3 = 0
    $ it_4 = 0
    $ it_5 = 0
    $ it_6 = 0
    $ time = 0
    $ room = "komnata"
    $ pick = 0
    $ lnt_v = 1
    $ persistent.Fl_autosaves = True
    $ persistent.Fl_status_sound = True
    $ load_value = 0
    $ Fl_scrim_ckick = 0
    $ Fl_proverka = True
    if persistent.Fl_ch_interface == None:
        $ persistent.Fl_ch_interface = False
    if persistent.Fl_swear_filter == None:
        $ persistent.Fl_swear_filter = False
    if persistent.Fl_podsk_count == None:
        $ persistent.Fl_podsk_count = False
    if persistent.Fl_update_2 == None:
        $ persistent.Fl_update_2 = False


    #Галерея
    if persistent.Fl_photo_pallery_1 == None:
        $ persistent.Fl_photo_pallery_1 == False
    if persistent.Fl_photo_pallery_2 == None:
        $ persistent.Fl_photo_pallery_2 == False
    if persistent.Fl_photo_pallery_3 == None:
        $ persistent.Fl_photo_pallery_3 == False
    if persistent.Fl_photo_pallery_4 == None:
        $ persistent.Fl_photo_pallery_4 == False
    if persistent.Fl_photo_pallery_5 == None:
        $ persistent.Fl_photo_pallery_5 == False
    if persistent.Fl_photo_pallery_6 == None:
        $ persistent.Fl_photo_pallery_6 == False
    if persistent.Fl_photo_pallery_7 == None:
        $ persistent.Fl_photo_pallery_7 == False
    if persistent.Fl_photo_pallery_8 == None:
        $ persistent.Fl_photo_pallery_8 == False
    if persistent.Fl_photo_pallery_9 == None:
        $ persistent.Fl_photo_pallery_9 == False
    if persistent.Fl_photo_pallery_10 == None:
        $ persistent.Fl_photo_pallery_10 == False
    if persistent.Fl_photo_pallery_11 == None:
        $ persistent.Fl_photo_pallery_11 == False
    if persistent.Fl_photo_pallery_12 == None:
        $ persistent.Fl_photo_pallery_12 == False
    if persistent.Fl_photo_pallery_13 == None:
        $ persistent.Fl_photo_pallery_13 == False
    if persistent.Fl_photo_pallery_14 == None:
        $ persistent.Fl_photo_pallery_14 == False
    if persistent.Fl_photo_pallery_15 == None:
        $ persistent.Fl_photo_pallery_15 == False
    if persistent.Fl_photo_pallery_16 == None:
        $ persistent.Fl_photo_pallery_16 == False
    if persistent.Fl_photo_pallery_17 == None:
        $ persistent.Fl_photo_pallery_17 == False
    if persistent.Fl_photo_pallery_18 == None:
        $ persistent.Fl_photo_pallery_18 == False
    if persistent.Fl_photo_pallery_19 == None:
        $ persistent.Fl_photo_pallery_19 == False
    if persistent.Fl_photo_pallery_20 == None:
        $ persistent.Fl_photo_pallery_20 == False
    if persistent.Fl_photo_pallery_21 == None:
        $ persistent.Fl_photo_pallery_21 == False
    if persistent.Fl_photo_pallery_22 == None:
        $ persistent.Fl_photo_pallery_22 == False
    if persistent.Fl_photo_pallery_23 == None:
        $ persistent.Fl_photo_pallery_23 == False
    if persistent.Fl_photo_pallery_24 == None:
        $ persistent.Fl_photo_pallery_24 == False
    if persistent.Fl_photo_pallery_25 == None:
        $ persistent.Fl_photo_pallery_25 == False
    if persistent.Fl_photo_pallery_26 == None:
        $ persistent.Fl_photo_pallery_26 == False
    if persistent.Fl_photo_pallery_27 == None:
        $ persistent.Fl_photo_pallery_27 == False
    if persistent.Fl_photo_pallery_28 == None:
        $ persistent.Fl_photo_pallery_28 == False
    if persistent.Fl_photo_pallery_29 == None:
        $ persistent.Fl_photo_pallery_29 == False
    if persistent.Fl_photo_pallery_30 == None:
        $ persistent.Fl_photo_pallery_30 == False
    if persistent.Fl_photo_pallery_31 == None:
        $ persistent.Fl_photo_pallery_31 == False
    if persistent.Fl_photo_pallery_32 == None:
        $ persistent.Fl_photo_pallery_32 == False
    if persistent.Fl_photo_pallery_33 == None:
        $ persistent.Fl_photo_pallery_33 == False
    if persistent.Fl_photo_pallery_34 == None:
        $ persistent.Fl_photo_pallery_34 == False
    


    #Достижения
    if persistent.Fl_dostn_1 == None:
        $ persistent.Fl_dostn_1 = False
    if persistent.Fl_dostn_2 == None:
        $ persistent.Fl_dostn_2 = False
    if persistent.Fl_dostn_3 == None:
        $ persistent.Fl_dostn_3 = False
    if persistent.Fl_dostn_4 == None:
        $ persistent.Fl_dostn_4 = False
    if persistent.Fl_dostn_5 == None:
        $ persistent.Fl_dostn_5 = False
    if persistent.Fl_dostn_6 == None:
        $ persistent.Fl_dostn_6 = False
    if persistent.Fl_dostn_7 == None:
        $ persistent.Fl_dostn_7 = False
    if persistent.Fl_dostn_8 == None:
        $ persistent.Fl_dostn_8 = False
    if persistent.Fl_dostn_9 == None:
        $ persistent.Fl_dostn_9 = False
    if persistent.Fl_dostn_10 == None:
        $ persistent.Fl_dostn_10 = False
    if persistent.Fl_dostn_11 == None:
        $ persistent.Fl_dostn_11 = False



    #Словарь
    if persistent.Fl_dictionary_1 == None:
        $ persistent.Fl_dictionary_1 == False
    if persistent.Fl_dictionary_2 == None:
        $ persistent.Fl_dictionary_2 == False
    if persistent.Fl_dictionary_3 == None:
        $ persistent.Fl_dictionary_3 == False
    if persistent.Fl_dictionary_4 == None:
        $ persistent.Fl_dictionary_4 == False
    if persistent.Fl_dictionary_5 == None:
        $ persistent.Fl_dictionary_5 == False
    if persistent.Fl_dictionary_6 == None:
        $ persistent.Fl_dictionary_6 == False
    if persistent.Fl_dictionary_7 == None:
        $ persistent.Fl_dictionary_7 == False
    if persistent.Fl_dictionary_8 == None:
        $ persistent.Fl_dictionary_8 == False
    if persistent.Fl_dictionary_9 == None:
        $ persistent.Fl_dictionary_9 == False
    if persistent.Fl_dictionary_10 == None:
        $ persistent.Fl_dictionary_10 == False
    if persistent.Fl_dictionary_11 == None:
        $ persistent.Fl_dictionary_11 == False
    if persistent.Fl_dictionary_12 == None:
        $ persistent.Fl_dictionary_12 == False
    if persistent.Fl_dictionary_13 == None:
        $ persistent.Fl_dictionary_13 == False
    if persistent.Fl_dictionary_14 == None:
        $ persistent.Fl_dictionary_14 == False
    if persistent.Fl_dictionary_15 == None:
        $ persistent.Fl_dictionary_15 == False
    if persistent.Fl_dictionary_16 == None:
        $ persistent.Fl_dictionary_16 == False
    if persistent.Fl_dictionary_17 == None:
        $ persistent.Fl_dictionary_17 == False






label Fl_activate_screen_nya:

    if Fl_scrim_ckick < 4:
        show Fl_skrim
        play sound "gui/main_menu/Fl_nya.mp3"
        with Fl_dspr
        $ Fl.Pause(0.3)
        hide Fl_skrim
        with Fl_dspr
        $ Fl_scrim_ckick += 1
        call screen Fl_preference_menu
        
    if Fl_scrim_ckick == 4:
        play sound "gui/main_menu/Fl_scrimer.mp3"
        show Fl_skrim2 with hpunch
        with hpunch
        with hpunch
        with hpunch
        $ Fl.Pause(0.01)
        hide Fl_skrim2
        
        if Fl_proverka == True:
        
            $ Fl.Pause(0.5)
            $ persistent.Fl_dostn_1 == True
            show Fl_dost_1_in_kod:
                xalign -1.0 yalign 0.7
            show Fl_dost_1_in_kod:
                ease 1.0 xalign 0.01
            $ Fl.Pause(0.5)
            $ Fl.PlaySound("Fl_achievement", 1, 0, False)
            $ Fl.Pause(1.5)
            hide Fl_dost_1_in_kod with dissolve
            if persistent.Fl_dostn_1 == False:
                $ persistent.Fl_dostn_1 = True
            $ persistent.replay = ""
            
            $ Fl_proverka = False
        
        $ Fl_scrim_ckick -= 4
        call screen Fl_preference_menu


label game_over:
    $ quick_menu = False
    $ Fl.PlayMusic("Fl_careless_whisper", 1, 2)
    scene Fl_game_over1 with Fl_flash
    $ Fl.Pause(2.0)
    scene Fl_game_over2 with Fl_flash
    $ persistent.Fl_dostn_2 = True
    show Fl_dost_2_in_kod:
        xalign -1.0 yalign 0.7
    show Fl_dost_2_in_kod:
        ease 1.0 xalign 0.01
    $ Fl.Pause(0.5)
    $ Fl.PlaySound("Fl_achievement", 1, 0, False)
    $ Fl.Pause(1.5)
    hide Fl_dost_2_in_kod with dissolve
    scene bg Fl_black with Fl_dissolve2

    return



init -18:
    #Очки рутов/1
    $ lp_mi = 0
    $ lp_mir = 0
    $ lp_an = 0
    $ lp_kt = 0
    $ lp_ma = 0
    $ lp_rz = 0
    $ lp_al = 0
    #Одиночные
    $ lp_ln = 0
    $ lp_un = 0
    $ lp_mv = 0
    $ lp_sz = 0
    $ lp_ed = 0
    #Побочные переменные
    $ add_to = 0
    $ add_ln = 0
    $ add_mi = 0
    $ add_msk = 0


    #Очки рутов(медсестра)
    $ lp_cs = 0

    #Очки рутов(одиночка)
    $ Ist_ln = 0
    $ Sph_ln = 0
    $ Sp_ln = 0

    #Очки рутов(Мику)
    $ Obs_mi = 0
    $ Ist_mi = 0


    #Очки рутов(Миры)
    $ Bad_mir = 0
    $ Good_mir = 0
    $ Ist_mir = 0

    #Очки рутов(Ани)
    $ Dfm_an = 0
    $ Eros_an = 0
    $ Ist_an = 0

    #Очки рутов(Катя)
    $ Dfm_kt = 0
    $ Eros_kt = 0

    #Очки рутов(Маши)
    $ Dfm_ma = 0
    $ Eros_ma = 0
    $ Ist_ma = 0

    #Очки рутов(Роза)
    $ Dfm_rz = 0
    $ Eros_rz = 0

    #Очки рутов(Алиса)
    $ Dfm_al = 0
    $ Eros_al = 0