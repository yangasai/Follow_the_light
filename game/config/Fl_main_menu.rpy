# -*- coding: ひきこもり -*-

#Само меню
label before_main_menu:
    $ renpy.block_rollback()
    scene bg Fl_menu
    show Fl_rain_hard_left
    show Fl_smoke at Fl_alpha(0.15)
    with Fl_fast
    $ Fl.StopSound(1)
    $ Fl.StopAmbience(1)
    $ Fl.PlayMusic("Fl_senritsu", 1, 5)
    $ Fl.PlayAmbience("Fl_rain", 0.4, 5)

    if persistent.Fl_update_2 == False:
        $ persistent.Fl_update_2 = True
        call screen update_bg

    else:
        call screen main_menu with Fl_fast

screen main_menu():
        tag menu
        modal True

        text "{font=[Fl_Script]}{size=92}ВСЛЕД ЗА СВЕТОМ{/size}{/font}":
                yalign -0.6
                xalign 0.05
                antialias True
                outlines [(1, "#000000", 0, 0)]
                at Fl_menu_rotate


        
        vbox:
            style_prefix "navigation"

            xpos gui.navigation_xpos
            yalign 0.59
            spacing gui.navigation_spacing
            

            textbutton _("Начать") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (Hide ("main_menu"), Start("Fl_start")) at Fl_menu_hover

            textbutton _("Загрузить") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (ShowMenu("Fl_load_bg")) at Fl_menu_hover

            textbutton _("DLC") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (ShowMenu("Fl_dls")) at Fl_menu_hover

            textbutton _("Галерея") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (ShowMenu("gallery")) at Fl_menu_hover

            textbutton _("Настройки") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (ShowMenu("Fl_preference_bg")) at Fl_menu_hover

            textbutton _("Достижения") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (ShowMenu("achievements")) at Fl_menu_hover

            textbutton _("Об игре") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (ShowMenu("about_bg")) at Fl_menu_hover

            if _in_replay:

                textbutton _("Завершить повтор") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (EndReplay(confirm=True)) at Fl_menu_hover

            if renpy.variant("pc"):

                textbutton _("Выход") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (Quit(confirm=not main_menu)) at Fl_menu_hover

        if gui.show_name:

            vbox:
                style "main_menu_vbox"

                text "[config.name!t]":
                    style "main_menu_title"

                text "[config.version]":
                    style "main_menu_version"



#Пауза
screen save():
    tag menu
    modal True
    add "Fl_prolog_dream" at Fl_alpha(0.15)
    add "gui/quick_menu_zad.png"
    text ["{font=[Fl_Script]}Игра на паузе:{/font}"]:
        size 55
        yalign 0.05 
        xalign 0.5
    text ["{font=[Fl_Script]}Время игры текущей сессии:{/font}"]:
        yalign 0.92 
        xalign 0.5
    add "Fl_game_time"
    use navigation





#Экран префер Fl
label Fl_preference_bg:
    $ Fl.StopAmbience(1)
    $ Fl.PlaySound("Fl_tv_noise", 0.5, 1, True)
    scene Fl_night_TV_sl
    show Fl_pulsing at Fl_alpha(0.4)
    show Fl_layer_preference

    #Вызов самой префер
    call screen Fl_preference_menu
    screen Fl_preference_menu:
        tag menu modal True
        add "gui/main_menu/Fl_ground.png"

        default current_tab = "main"

        text "{font=[Fl_Script]}{size=60}Настройки:{/size}{/font}":
            yalign 0.02
            xalign 0.02
            antialias True
            outlines [(1, "#000000", 0, 0)]

        hbox:
            align(0.14, 0.11)
            spacing 4

            textbutton _("Основные") text_size 28 hover_sound "gui/main_menu/Fl_click_menu.mp3" action SetScreenVariable("current_tab", "main")
            textbutton _("Звук") text_size 28 hover_sound "gui/main_menu/Fl_click_menu.mp3" action SetScreenVariable("current_tab", "sound_text")

        if current_tab == "main":
            use Fl_preferences_main
        elif current_tab == "sound_text":
            use Fl_preferences_sound_text

        textbutton ["Назад"] at Fl_menu_hover:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_setting" style "Fl_button_None"
            align (0.02, 0.98) action [Hide("Fl_preference_menu", Dissolve(1.0)), Jump("before_main_menu")]

        imagebutton:
            xpos 1440 ypos 885
            auto "gui/main_menu/preferences/Fl_knopka_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_activate_screen_nya")

        

screen Fl_preferences_main:
        vbox:
            align (0.1, 0.33)
            spacing 30

            vbox xalign 0.5:
                text "Режим экрана" xalign 0.5:
                    font Fl_Script size 45
                    antialias True
                    outlines [(1, "#000000", 0, 0)]

                hbox:
                    xalign 0.5
                    spacing 35

                    if not _preferences.fullscreen:
                        textbutton "В окне" at Fl_menu_hover:
                            action None
                        textbutton "На весь экран" at Fl_menu_hover:
                            hover_sound "gui/main_menu/Fl_click_menu.mp3"
                            action (Preference("display", "fullscreen"))
                    else:
                        textbutton "В окне" at Fl_menu_hover:
                            hover_sound "gui/main_menu/Fl_click_menu.mp3"
                            action (Preference("display", "window"))
                        textbutton "На весь экран" at Fl_menu_hover:
                            action None

            vbox xalign 0.5:
                text "Тема" xalign 0.5:
                        font Fl_Script size 45
                        antialias True
                        outlines [(1, "#000000", 0, 0)]

                hbox:
                    xalign 0.5
                    spacing 35

                    if persistent.Fl_ch_interface == True:
                        textbutton "Ч/б" at Fl_menu_hover:
                            action None
                        textbutton "Цветная" at Fl_menu_hover:
                            hover_sound "gui/main_menu/Fl_click_menu.mp3"
                            action (SetField(persistent, "Fl_ch_interface", False))
                    else:
                        textbutton "Ч/б" at Fl_menu_hover:
                            hover_sound "gui/main_menu/Fl_click_menu.mp3"
                            action (SetField(persistent, "Fl_ch_interface", True))
                        textbutton "Цветная" at Fl_menu_hover:
                            action None

            vbox xalign 0.5:
                text "Фильтр мата" xalign 0.5:
                    font Fl_Script size 45
                    antialias True
                    outlines [(1, "#000000", 0, 0)]

                hbox:
                    xalign 0.5
                    spacing 35

                    if persistent.Fl_swear_filter == True:
                        textbutton "Включить" at Fl_menu_hover:
                            action None
                
                        textbutton "Выключить" at Fl_menu_hover:
                            hover_sound "gui/main_menu/Fl_click_menu.mp3"
                            action (SetField(persistent, "Fl_swear_filter", False))
                    
                    else:
                        textbutton "Включить" at Fl_menu_hover:
                            hover_sound "gui/main_menu/Fl_click_menu.mp3"
                            action (SetField(persistent, "Fl_swear_filter", True))
                        textbutton "Выключить" at Fl_menu_hover:
                            action None

            vbox xalign 0.5:
                text "Пропуск текста" xalign 0.5:
                    font Fl_Script size 45
                    antialias True
                    outlines [(1, "#000000", 0, 0)]
                    
                hbox:
                    xalign 0.5
                    spacing 35

                    if not _preferences.skip_unseen:
                        textbutton "Только прочитанное" at Fl_menu_hover:
                            action None
                        textbutton "Всё" at Fl_menu_hover:
                            hover_sound "gui/main_menu/Fl_click_menu.mp3"
                            action (Preference("skip", "all"))
                    else:
                        textbutton "Только прочитанное" at Fl_menu_hover:
                            hover_sound "gui/main_menu/Fl_click_menu.mp3"
                            action (Preference("skip", "seen"))
                        textbutton "Всё" at Fl_menu_hover:
                            action None

            vbox xalign 0.5:
                text "Подсказки" xalign 0.5:
                    font Fl_Script size 45
                    antialias True
                    outlines [(1, "#000000", 0, 0)]

                hbox:
                    xalign 0.5
                    spacing 35

                    if persistent.Fl_podsk_count == True:
                        textbutton "Включить" at Fl_menu_hover:
                            action None
                        textbutton "Выключить" at Fl_menu_hover:
                            hover_sound "gui/main_menu/Fl_click_menu.mp3"
                            action (SetField(persistent, "Fl_podsk_count", False))
                        
                    else:
                        textbutton "Включить" at Fl_menu_hover:
                            hover_sound "gui/main_menu/Fl_click_menu.mp3"
                            action (SetField(persistent, "Fl_podsk_count", True))
                        textbutton "Выключить" at Fl_menu_hover:
                            action None

            

screen Fl_preferences_sound_text:
    vbox:
        align (0.1, 0.31)
        spacing 30

        vbox xalign 0.5:
            text "Текст" xalign 0.5:
                font Fl_Script size 45
                antialias True
                outlines [(1, "#000000", 0, 0)]
            bar:
                value Preference("text speed")
                right_bar "gui/main_menu/preferences/Fl_scale_chist.png"
                left_bar "gui/main_menu/preferences/Fl_scale_poln.png"
                thumb "gui/main_menu/preferences/Fl_begunok.png"
                xmaximum 365
                ymaximum 70

        vbox xalign 0.5:
            text "Музыка" xalign 0.5:
                font Fl_Script size 45
                antialias True
                outlines [(1, "#000000", 0, 0)] 
            bar:
                value Preference("music volume")
                right_bar "gui/main_menu/preferences/Fl_scale_chist.png"
                left_bar "gui/main_menu/preferences/Fl_scale_poln.png"
                thumb "gui/main_menu/preferences/Fl_begunok.png"
                xmaximum 365
                ymaximum 70

        vbox xalign 0.5:
            text "Звуки" xalign 0.5:
                font Fl_Script size 45
                antialias True
                outlines [(1, "#000000", 0, 0)]
            bar:
                value Preference("sound volume")
                right_bar "gui/main_menu/preferences/Fl_scale_chist.png"
                left_bar "gui/main_menu/preferences/Fl_scale_poln.png"
                thumb "gui/main_menu/preferences/Fl_begunok.png"
                xmaximum 365
                ymaximum 70

        vbox xalign 0.5:
            text "Эмбиент" xalign 0.5:
                font Fl_Script size 45
                antialias True
                outlines [(1, "#000000", 0, 0)]
            bar:
                value Preference("voice volume")
                right_bar "gui/main_menu/preferences/Fl_scale_chist.png"
                left_bar "gui/main_menu/preferences/Fl_scale_poln.png"
                thumb "gui/main_menu/preferences/Fl_begunok.png"
                xmaximum 365
                ymaximum 70







#Экран загрузки Fl
label Fl_load_bg:
    $ Fl.StopAmbience(1)
    $ Fl.PlayAmbience("Fl_bizzard_outside", 1, 2)
    $ Fl.PlaySound("Fl_knife_loop", 0.5, 1, True)
    scene bus 
    show hand at Fl_rotate_hand
    show Fl_layer_load
    show Fl_snow at Fl_linear_effects_repeat(0.4, 0.75, 0.7, 0.75, 0.25, 0.3, 0.25)

    #Вызов самой загрузки
    call screen Fl_load_menu
    screen Fl_load_menu():
        tag menu
        modal True
        fixed yoffset 200 xoffset 635 at Fl_menu_move(0.75, 0.5, 0):
            add "gui/main_menu/save/save_background.png"

        fixed align (0.5, 0.5) anchor (0.5, 0.5) at Fl_menu_move(0.7, 0.5, 0):
            text ["{font=[Fl_Script]}Загрузить{/font}"]:
                size 60
                text_align 0.5
                xalign 0.873
                yalign 0.305
                antialias True
                kerning 2

            textbutton ["{font=[Fl_Script]}Загрузить игру{/font}"] at Fl_menu_hover:
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                text_style "Fl_text_big_save_load"
                style "Fl_button_None"
                text_size 50
                ypos 1010
                xalign 0.887
                action (Fl_FunctionCallback(Fl.CallbackOnLoad, selected_slot), FileLoad(selected_slot))
            textbutton ["Удалить"] at Fl_menu_hover:
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                text_style "Fl_text_big_save_load"
                style "Fl_button_None"
                text_size 50
                xpos 1900
                ypos 1010
                action FileDelete(selected_slot)
            textbutton ["Назад"] at Fl_menu_hover:
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                text_style "Fl_text_big_save_load"
                style "Fl_button_None"
                text_size 50
                xpos 1010
                ypos 1010
                action [Hide("Fl_load_menu", Dissolve(1.0)), Jump("before_main_menu")]
        use Fl_save_load_slots_menu






#Экран слотов(меню)
screen Fl_save_load_slots_menu:
    fixed align (0.5, 0.5) anchor (0.5, 0.5) at Fl_menu_move(0.7, 0.5, 0, 0.45):
        vbox:
            xalign 0.515
            yalign 0.805 #(0.805 if persistent.Fl_autosaves else 0.4)
            grid 1 10:
                for slot in range(0, 10):
                    if slot == 0:
                        textbutton ["А"]:
                            text_size 38 
                            style "Fl_button_None"
                            text_style "Fl_text_big_save_load"
                            action [FilePage("Fl_FilePage_auto"), SetVariable("selected_slot", False), SelectedIf(persistent._file_page == "Fl_FilePage_auto")]
                    else:
                        textbutton str(slot):
                            text_size 38 right_padding 50 
                            style "Fl_button_None"
                            text_style "Fl_text_big_save_load"
                            action [FilePage("FilePage_" + str(slot)), SetVariable("selected_slot", False), SelectedIf(persistent._file_page == "FilePage_" + str(slot))]
        #Ячейки
        grid 4 3 at Fl_menu_move(0.77, 0.5, 0):
            yoffset 170 xoffset 675
            xmaximum 0.81 #Ширина полей
            ymaximum 0.65 #Ширина полей
            transpose False
            xfill True
            yfill True
            for slot in range(1, 13):
                fixed:
                    add FileScreenshot(slot):
                        zoom 0.815
                        xpos 10
                        ypos 10
                    button:
                        action SetVariable("selected_slot", slot)
                        xfill False
                        yfill False
                        style "Fl_save_load_button"
                        has fixed
                        text ("%s." % slot + FileTime(slot, format=" %d.%m.%y, %H:%M", empty=" "+"Пусто") + "\n" + FileSaveName(slot)):
                            style "Fl_save_load_button"
                            xpos 15
                            ypos 15
                            xmaximum 0.8



#Экран слотов(стандарт)
screen Fl_save_load_slots:
    fixed align (0.5, 0.5) anchor (0.5, 0.5) at Fl_menu_move(0.65, 0.5, 0):
        vbox:
            xalign 0.07
            yalign 0.53
            grid 1 10:
                for slot in range(0, 10):
                    if slot == 0:
                        textbutton ["А"]:
                            text_size 50 style "Fl_button_None"
                            text_style "Fl_text_big_save_load"
                            action [FilePage("Fl_FilePage_auto"), SetVariable("selected_slot", False), SelectedIf(persistent._file_page == "Fl_FilePage_auto")]
                    else:
                        textbutton str(slot):
                            text_size 50 right_padding 50 style "Fl_button_None"
                            text_style "Fl_text_big_save_load"
                            action [FilePage("FilePage_" + str(slot)), SetVariable("selected_slot", False), SelectedIf(persistent._file_page == "FilePage_" + str(slot))]
        grid 4 3:
            xpos 0.130
            ypos 0.2
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True
            for slot in range(1, 13):
                fixed:
                    add FileScreenshot(slot):
                        zoom 0.815
                        xpos 10
                        ypos 10
                    button:
                        action SetVariable("selected_slot", slot)
                        xfill False
                        yfill False
                        style "Fl_save_load_button"
                        has fixed
                        text ("%s." % slot + FileTime(slot, format=" %d.%m.%y, %H:%M", empty=" "+"Пусто") + "\n" + FileSaveName(slot)):
                            style "Fl_save_load_button"
                            xpos 15
                            ypos 15
                            xmaximum 0.8



#Галерея
label gallery:
    $ Fl.StopAmbience(1)
    scene Fl_gallery_fon_osn
    call screen Fl_gallery
    screen Fl_gallery:
        tag menu
        modal True

        text "{font=[Fl_Script]}{size=60}Галерея{/size}{/font}":
            yalign 0.02
            xalign 0.5
            antialias True
            outlines [(1, "#000000", 0, 0)]

        text "{font=[Fl_Script]}{size=55}1/4{/size}{/font}":
            outlines [(1, "#000000", 0, 0)]
            xpos 1790 ypos 980


        imagebutton:
            auto "gui/button/Fl_strelka2_gallery_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action ShowMenu("Fl_gallery2")
            at Fl_strel_zoom1

        textbutton ["Назад"] at Fl_menu_hover:
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                text_style "Fl_text_big_save_load" style "Fl_button_None"
                align (0.02, 0.98) action [Hide("gallery", Dissolve(1.0)), Jump("before_main_menu")]

        if persistent.Fl_photo_pallery_1 == True:
            imagebutton:
                xpos 156 ypos 134
                auto "gui/main_menu/gallery/Fl_photo_1_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action Jump("Fl_prosmotr_1")
        else:
            add "Fl_gallery_photo_none":
                xpos 156 ypos 134


        if persistent.Fl_photo_pallery_2 == True:
            imagebutton:
                xpos 579 ypos 134
                auto "gui/main_menu/gallery/Fl_photo_2_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action Jump("Fl_prosmotr_2")
        else:
            add "Fl_gallery_photo_none":
                xpos 579 ypos 134


        if persistent.Fl_photo_pallery_3 == True:
            imagebutton:
                xpos 1002 ypos 134
                auto "gui/main_menu/gallery/Fl_photo_3_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action Jump("Fl_prosmotr_3")
        else:
            add "Fl_gallery_photo_none":
                xpos 1002 ypos 134

        if persistent.Fl_photo_pallery_4 == True:
            imagebutton:
                xpos 1425 ypos 134
                auto "gui/main_menu/gallery/Fl_photo_4_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action Jump("Fl_prosmotr_4")
        else:
            add "Fl_gallery_photo_none":
                xpos 1425 ypos 134

        
        if persistent.Fl_photo_pallery_5 == True:
            imagebutton:
                xpos 156 ypos 419
                auto "gui/main_menu/gallery/Fl_photo_5_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action Jump("Fl_prosmotr_5")
        else:
            add "Fl_gallery_photo_none":
                xpos 156 ypos 419

        if persistent.Fl_photo_pallery_6 == True:
            imagebutton:
                xpos 579 ypos 419
                auto "gui/main_menu/gallery/Fl_photo_6_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action Jump("Fl_prosmotr_6")
        else:
            add "Fl_gallery_photo_none":
                xpos 579 ypos 419


        if persistent.Fl_photo_pallery_7 == True:
            imagebutton:
                xpos 1002 ypos 419
                auto "gui/main_menu/gallery/Fl_photo_7_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action Jump("Fl_prosmotr_7")
        else:
            add "Fl_gallery_photo_none":
                xpos 1002 ypos 419

        
        if persistent.Fl_photo_pallery_8 == True:
            imagebutton:
                xpos 1425 ypos 419
                auto "gui/main_menu/gallery/Fl_photo_8_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action Jump("Fl_prosmotr_8")
        else:
            add "Fl_gallery_photo_none":
                xpos 1425 ypos 419


        if persistent.Fl_photo_pallery_9 == True:
            imagebutton:
                xpos 156 ypos 704
                auto "gui/main_menu/gallery/Fl_photo_9_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action Jump("Fl_prosmotr_9")
        else:
            add "Fl_gallery_photo_none":
                xpos 156 ypos 704


        if persistent.Fl_photo_pallery_10 == True:
            imagebutton:
                xpos 579 ypos 704
                auto "gui/main_menu/gallery/Fl_photo_10_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action Jump("Fl_prosmotr_10")
        else:
            add "Fl_gallery_photo_none":
                xpos 579 ypos 704


        if persistent.Fl_photo_pallery_11 == True:
            imagebutton:
                xpos 1002 ypos 704
                auto "gui/main_menu/gallery/Fl_photo_11_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action Jump("Fl_prosmotr_11")
        else:
            add "Fl_gallery_photo_none":
                xpos 1002 ypos 704


        if persistent.Fl_photo_pallery_12 == True:
            imagebutton:
                xpos 1425 ypos 704
                auto "gui/main_menu/gallery/Fl_photo_12_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action Jump("Fl_prosmotr_12")
        else:
            add "Fl_gallery_photo_none":
                xpos 1425 ypos 704

        add "Fl_gallery_lych" at Fl_gallery_lych_anim



screen Fl_gallery2:
    tag menu
    modal True

    text "{font=[Fl_Script]}{size=60}Галерея{/size}{/font}":
            yalign 0.02
            xalign 0.5
            antialias True
            outlines [(1, "#000000", 0, 0)]

    text "{font=[Fl_Script]}{size=55}2/4{/size}{/font}":
        outlines [(1, "#000000", 0, 0)]
        xpos 1790 ypos 980

    imagebutton:
        auto "gui/button/Fl_strelka2_gallery_%s.png"
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        action ShowMenu("Fl_gallery2")
        at Fl_strel_zoom1

    if persistent.Fl_photo_pallery_13 == True:
        imagebutton:
            xpos 156 ypos 134
            auto "gui/main_menu/gallery/Fl_photo_13_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_13")
    else:
        add "Fl_gallery_photo_none":
            xpos 156 ypos 134


    if persistent.Fl_photo_pallery_14 == True:
        imagebutton:
            xpos 579 ypos 134
            auto "gui/main_menu/gallery/Fl_photo_14_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_14")
    else:
        add "Fl_gallery_photo_none":
            xpos 579 ypos 134


    if persistent.Fl_photo_pallery_15 == True:
        imagebutton:
            xpos 1002 ypos 134
            auto "gui/main_menu/gallery/Fl_photo_15_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_15")
    else:
        add "Fl_gallery_photo_none":
            xpos 1002 ypos 134

    if persistent.Fl_photo_pallery_16 == True:
        imagebutton:
            xpos 1425 ypos 134
            auto "gui/main_menu/gallery/Fl_photo_16_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_16")
    else:
        add "Fl_gallery_photo_none":
            xpos 1425 ypos 134

        
    if persistent.Fl_photo_pallery_17 == True:
        imagebutton:
            xpos 156 ypos 419
            auto "gui/main_menu/gallery/Fl_photo_17_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_17")
    else:
        add "Fl_gallery_photo_none":
            xpos 156 ypos 419

    if persistent.Fl_photo_pallery_18 == True:
        imagebutton:
            xpos 579 ypos 419
            auto "gui/main_menu/gallery/Fl_photo_18_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_18")
    else:
        add "Fl_gallery_photo_none":
            xpos 579 ypos 419


    if persistent.Fl_photo_pallery_19 == True:
        imagebutton:
            xpos 1002 ypos 419
            auto "gui/main_menu/gallery/Fl_photo_19_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_19")
    else:
        add "Fl_gallery_photo_none":
            xpos 1002 ypos 419

        
    if persistent.Fl_photo_pallery_20 == True:
        imagebutton:
            xpos 1425 ypos 419
            auto "gui/main_menu/gallery/Fl_photo_20_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_20")
    else:
        add "Fl_gallery_photo_none":
            xpos 1425 ypos 419


    if persistent.Fl_photo_pallery_21 == True:
        imagebutton:
            xpos 156 ypos 704
            auto "gui/main_menu/gallery/Fl_photo_21_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_21")
    else:
        add "Fl_gallery_photo_none":
            xpos 156 ypos 704


    if persistent.Fl_photo_pallery_22 == True:
        imagebutton:
            xpos 579 ypos 704
            auto "gui/main_menu/gallery/Fl_photo_22_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_22")
    else:
        add "Fl_gallery_photo_none":
            xpos 579 ypos 704


    if persistent.Fl_photo_pallery_23 == True:
        imagebutton:
            xpos 1002 ypos 704
            auto "gui/main_menu/gallery/Fl_photo_23_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_23")
    else:
        add "Fl_gallery_photo_none":
            xpos 1002 ypos 704


    if persistent.Fl_photo_pallery_24 == True:
        imagebutton:
            xpos 1425 ypos 704
            auto "gui/main_menu/gallery/Fl_photo_24_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_24")
    else:
        add "Fl_gallery_photo_none":
            xpos 1425 ypos 704

    imagebutton:
        auto "gui/button/Fl_strelka2_gallery_%s.png"
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        action ShowMenu("Fl_gallery3")
        at Fl_strel_zoom1

    imagebutton:
        auto "gui/button/Fl_strelka_gallery_%s.png"
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        action ShowMenu("Fl_gallery")
        at Fl_strel_zoom2

    textbutton ["Назад"] at Fl_menu_hover:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_big_save_load" style "Fl_button_None"
            align (0.02, 0.98) action [Hide("gallery2", Dissolve(1.0)), Jump("before_main_menu")]

    add "Fl_gallery_lych" at Fl_gallery_lych_anim


screen Fl_gallery3:
    tag menu
    modal True

    text "{font=[Fl_Script]}{size=60}Галерея{/size}{/font}":
            yalign 0.02
            xalign 0.5
            antialias True
            outlines [(1, "#000000", 0, 0)]

    text "{font=[Fl_Script]}{size=55}3/4{/size}{/font}":
        outlines [(1, "#000000", 0, 0)]
        xpos 1790 ypos 980

    imagebutton:
        auto "gui/button/Fl_strelka2_gallery_%s.png"
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        action ShowMenu("Fl_gallery4")
        at Fl_strel_zoom1

    imagebutton:
        auto "gui/button/Fl_strelka_gallery_%s.png"
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        action ShowMenu("Fl_gallery2")
        at Fl_strel_zoom2

    textbutton ["Назад"] at Fl_menu_hover:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_big_save_load" style "Fl_button_None"
            align (0.02, 0.98) action [Hide("gallery3", Dissolve(1.0)), Jump("before_main_menu")]

    add "Fl_gallery_lych" at Fl_gallery_lych_anim


    if persistent.Fl_photo_pallery_25 == True:
        imagebutton:
            xpos 156 ypos 134
            auto "gui/main_menu/gallery/Fl_photo_25_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_25")
    else:
        add "Fl_gallery_photo_none":
            xpos 156 ypos 134

    if persistent.Fl_photo_pallery_26 == True:
        imagebutton:
            xpos 579 ypos 134
            auto "gui/main_menu/gallery/Fl_photo_26_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_26")
    else:
        add "Fl_gallery_photo_none":
            xpos 579 ypos 134


    if persistent.Fl_photo_pallery_27 == True:
        imagebutton:
            xpos 1002 ypos 134
            auto "gui/main_menu/gallery/Fl_photo_27_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_27")
    else:
        add "Fl_gallery_photo_none":
            xpos 1002 ypos 134

    if persistent.Fl_photo_pallery_28 == True:
        imagebutton:
            xpos 1425 ypos 134
            auto "gui/main_menu/gallery/Fl_photo_28_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_28")
    else:
        add "Fl_gallery_photo_none":
            xpos 1425 ypos 134

        
    if persistent.Fl_photo_pallery_29 == True:
        imagebutton:
            xpos 156 ypos 419
            auto "gui/main_menu/gallery/Fl_photo_29_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_29")
    else:
        add "Fl_gallery_photo_none":
            xpos 156 ypos 419

    if persistent.Fl_photo_pallery_30 == True:
        imagebutton:
            xpos 579 ypos 419
            auto "gui/main_menu/gallery/Fl_photo_30_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_30")
    else:
        add "Fl_gallery_photo_none":
            xpos 579 ypos 419


    if persistent.Fl_photo_pallery_31 == True:
        imagebutton:
            xpos 1002 ypos 419
            auto "gui/main_menu/gallery/Fl_photo_31_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_31")
    else:
        add "Fl_gallery_photo_none":
            xpos 1002 ypos 419

        
    if persistent.Fl_photo_pallery_32 == True:
        imagebutton:
            xpos 1425 ypos 419
            auto "gui/main_menu/gallery/Fl_photo_32_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_32")
    else:
        add "Fl_gallery_photo_none":
            xpos 1425 ypos 419


    if persistent.Fl_photo_pallery_33 == True:
        imagebutton:
            xpos 156 ypos 704
            auto "gui/main_menu/gallery/Fl_photo_33_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_33")
    else:
        add "Fl_gallery_photo_none":
            xpos 156 ypos 704


    if persistent.Fl_photo_pallery_34 == True:
        imagebutton:
            xpos 579 ypos 704
            auto "gui/main_menu/gallery/Fl_photo_34_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_34")
    else:
        add "Fl_gallery_photo_none":
            xpos 579 ypos 704


    if persistent.Fl_photo_pallery_35 == True:
        imagebutton:
            xpos 1002 ypos 704
            auto "gui/main_menu/gallery/Fl_photo_35_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_35")
    else:
        add "Fl_gallery_photo_none":
            xpos 1002 ypos 704


    if persistent.Fl_photo_pallery_36 == True:
        imagebutton:
            xpos 1425 ypos 704
            auto "gui/main_menu/gallery/Fl_photo_36_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_prosmotr_36")
    else:
        add "Fl_gallery_photo_none":
            xpos 1425 ypos 704



screen Fl_gallery4:
    tag menu
    modal True

    text "{font=[Fl_Script]}{size=60}Галерея{/size}{/font}":
            yalign 0.02
            xalign 0.5
            antialias True
            outlines [(1, "#000000", 0, 0)]
            
    text "{font=[Fl_Script]}{size=55}4/4{/size}{/font}":
        outlines [(1, "#000000", 0, 0)]
        xpos 1790 ypos 980

    text "{font=[Fl_Script]}{size=80}Скоро...{/size}{/font}":
            yalign 0.5
            xalign 0.5
            antialias True
            at Fl_menu_rotate

    imagebutton:
        auto "gui/button/Fl_strelka_gallery_%s.png"
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        action ShowMenu("Fl_gallery3")
        at Fl_strel_zoom2

    textbutton ["Назад"] at Fl_menu_hover:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_big_save_load" style "Fl_button_None"
            align (0.02, 0.98) action [Hide("gallery4", Dissolve(1.0)), Jump("before_main_menu")]

    add "Fl_gallery_lych" at Fl_gallery_lych_anim






label Fl_prosmotr_1:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_vogatay_hot with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_2:
    
    scene bg Fl_black with Fl_dissolve1
    scene Fl_ext_camp_entrance_night_vision
    show Fl_smoke
    show Fl_ext_camp_entrance_night_vision_uvao
    with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_3:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_d1_food_normal with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_4:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_boathouse_lena with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_5:
    
    scene bg Fl_black with Fl_dissolve1
    scene Fl_ground_night 
    show Fl_eyes_open_night
    show Fl_brows_happy_night
    show Fl_mouth_smile_night
    show Fl_light_layer at Fl_alpha(0.3)
    with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_6:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_micu_lib with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_7:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_msk_canteen_rage with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_8:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_catmiku:
        subpixel True
        truecenter
        yalign 0.85
        zoom 1.3
        ease 10.0 yalign 0.1 zoom 1.0
    with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1



label Fl_prosmotr_9:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_bloodsquare with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('Fl_prosmotr_9_2')
    with Fl_dissolve1


label Fl_prosmotr_9_2:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_bloodsquare2 with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('Fl_prosmotr_9_3')
    with Fl_dissolve1


label Fl_prosmotr_9_3:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_bloodsquare3 with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('Fl_prosmotr_9_4')
    with Fl_dissolve1


label Fl_prosmotr_9_4:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_bloodsquare4 with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('Fl_prosmotr_9_5')
    with Fl_dissolve1


label Fl_prosmotr_9_5:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_bloodsquare5 with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_10:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_dead_gg_wosp with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1

    
label Fl_prosmotr_11:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_dead_pioneer with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_12:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_lena_catacombs with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_13:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_mi_guitar with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_14:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_mik with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_15:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_miku_piano with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_16:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_mine_fint with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_17:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_p_say with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_18:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_pioneer_falling with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('Fl_prosmotr_18_2')
    with Fl_dissolve1



label Fl_prosmotr_18_2:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_pioneer_falling2 with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_19:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_dead_gg_wosp_light with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_20:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_vurtal with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_21:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_heads_off with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_22:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_lip_on_bench_1 with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_23:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_lisa_in_darkness_1 with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('Fl_prosmotr_23_2')
    with Fl_dissolve1


label Fl_prosmotr_23_2:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_lisa_in_darkness_2 with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('Fl_prosmotr_23_3')
    with Fl_dissolve1


label Fl_prosmotr_23_3:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_lisa_in_darkness_3 with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_24:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_un_book with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_25:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_un_knife:
        subpixel True
        truecenter
        yalign 0.85
        zoom 1.26
        ease 8.5 yalign 0.1 zoom 1.0
    with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_26:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_viola_not_wine with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_27:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_gg_bol:
        subpixel True
        truecenter
        yalign 0.85
        zoom 1.18
        ease 8.5 yalign 0.1 zoom 1.0
    show Fl_light_c
    with Fl_dissolve2
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_28:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_forest_zombie with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_29:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_loner_lena with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_30:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_mi_dark with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_31:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_mine_inside_elevator with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_32:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_nekto with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1


label Fl_prosmotr_33:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_mi_gost with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('Fl_prosmotr_33_2')
    with Fl_dissolve1


label Fl_prosmotr_33_2:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_mi_gost2 with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('Fl_prosmotr_33_3')
    with Fl_dissolve1

label Fl_prosmotr_33_3:
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_mi_gost3 with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('Fl_prosmotr_33_4')
    with Fl_dissolve1


label Fl_prosmotr_33_4:
    
    scene bg Fl_black with Fl_dissolve1
    scene cg Fl_mi_gost4 with Fl_dissolve1
    $ renpy.pause(999.2)
    scene bg Fl_black with Fl_dissolve1
    
    $ renpy.transition(Fl_dissolve1)
    $ self.result = renpy.jump('gallery')
    with Fl_dissolve1





#DLS
screen Fl_dls:
    modal True

    default current_page = 1
    
    add "gui/choice.png" at Fl_alpha(0.8)
    
    fixed yoffset 170 xoffset 635 at Fl_menu_move(0.91, 0.5, 0):
        add "gui/main_menu/save/save_background.png"

    frame at Fl_from_about(-1500, 0.5):
        if current_page == 1:
            imagebutton:
                xalign 0.78
                yalign 0.3
                auto "gui/main_menu/dls/Fl_dls1_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action Play("sound", "gui/main_menu/Fl_lock.ogg")

            imagebutton:
                align (0.97, 0.55)
                auto "gui/button/Fl_strelka2_gallery_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action SetScreenVariable("current_page", 2)
                at Fl_strel_zoom3

            vbox:
                align (0.85, 0.66)
                spacing 4

                text "Обычная жизнерадостная пионерка, мечтающая найти друзей, однажды оказалась" xalign 0.0 size 21
                text "в мире, где музыка стала её единственным утешением. Она играла симфонии вы-" xalign 0.0 size 21
                text "сокого уровня, наполняя сердца окружающих радостью и светом. Каждая нота, вы-" xalign 0.0 size 21
                text "зывала улыбки на лицах слушателей. В этот роковой день её жизнь перевернулась" xalign 0.0 size 21
                text "Она осознала, что осталась одна — единственная живая душа среди бездушёных" xalign 0.0 size 21
                text "слушателей, которые лишь улыбались, не понимая ужасного происходящего вокруг." xalign 0.0 size 21
                text "Мелодия, некогда полная жизни, зазвучала ещё более халтурно, и она не могла" xalign 0.0 size 21
                text "представить, что этот реквием призовёт тех, кто страшнее бездушных зрителей." xalign 0.0 size 21
                text "Теперь ей предстоит столкнуться с темными тенями, которые были вызваны её му-" xalign 0.0 size 21
                text "зыкой, и выжить на этой сцене безумия." xalign 0.0 size 21

        elif current_page == 2:
            imagebutton:
                xalign 0.78
                yalign 0.3
                auto "gui/main_menu/dls/Fl_dls2_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action Play("sound", "gui/main_menu/Fl_lock.ogg")

            imagebutton:
                align (0.97, 0.55)
                auto "gui/button/Fl_strelka2_gallery_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action SetScreenVariable("current_page", 3)
                at Fl_strel_zoom3

            imagebutton:
                align (0.455, 0.55)
                auto "gui/button/Fl_strelka_gallery_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action SetScreenVariable("current_page", 1)
                at Fl_strel_zoom4

            vbox:
                align (0.865, 0.66)
                spacing 4

                text "Поэзия бывает разной: грустной, весёлой, фантастической, но всегда она захва-" xalign 0.0 size 21
                text "тывает дух. Что, если бы у вас была возможность воплотить произведение искус-" xalign 0.0 size 21
                text "ства в реальность? Создать персонажей, наделить их чувствами и поиграть с эти-" xalign 0.0 size 21
                text "ми чувствами? Так думала Тихая пионерка, сидя на площади с книжкой в руках. Дос-" xalign 0.0 size 21
                text "таточно было просто захлопнуть книгу, и реальность могла бы стать обыденнной..." xalign 0.0 size 21
                text "или нет? Что, если реальность — это пьеса, а вы — её писатель, и ваша ручка — ост-" xalign 0.0 size 21
                text "рый нож, способный резать границы между мирами? Тихий омут может показаться спо-" xalign 0.0 size 21
                text "койным, но он остаётся таковым лишь до тех пор, пока не позовёте своих чертей. И" xalign 0.0 size 21
                text "вот, моих чертей разбудил один пионер, и всё изменилось. В этот момент я поняла:" xalign 0.0 size 21
                text "впервые в истории я не главная героиня." xalign 0.0 size 21

        elif current_page == 3:
            imagebutton:
                xalign 0.78
                yalign 0.3
                auto "gui/main_menu/dls/Fl_dls3_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action Jump("intro_q66")

            imagebutton:
                align (0.455, 0.55)
                auto "gui/button/Fl_strelka_gallery_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action SetScreenVariable("current_page", 2)
                at Fl_strel_zoom4

            vbox:
                align (0.865, 0.64)
                spacing 4

                text "Скучный реальный мир, травмирующие воспоминания и бесконечные скитания. Но в" xalign 0.0 size 21
                text "один день всё изменилось. Новый мир, названный Совёнок, открыл двери к тому, че-" xalign 0.0 size 21
                text "го так давно хотелось: любви, счастью и забытым чувствам. Каждое мгновение в этом" xalign 0.0 size 21
                text "мире казалось волшебным, но радость не продлилась долго. Всё, что было даровано," xalign 0.0 size 21
                text "безжалостно исчезло в один миг, оставив меня наедине с бездушными куклами, кото-" xalign 0.0 size 21
                text "рые когда-то были друзьями, но теперь лишь пустые оболочки. Такой мир меняет каждо-" xalign 0.0 size 21
                text "го. Боль, некогда сковывавшая душу, переросла в ненависть, а ненависть — в безумие." xalign 0.0 size 21
                text "Теперь только окровавленная, протоптанная дорога ведёт куда-то а человечность оста-" xalign 0.0 size 21
                text "лась где-то позади, затерянная среди теней прошлого." xalign 0.0 size 21

    frame at Fl_from_about(-1500, 0.5):
        align (0.47, 0.855)
        textbutton ["Назад"] at Fl_menu_hover:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_big_save_load"
            style "Fl_button_None"
            text_size 35
            action Hide("Fl_dls", Dissolve(0.25))









#Достижения
label achievements:
    $ Fl.StopAmbience(1)
    scene Fl_progress_osn
    call screen Fl_achievements
    screen Fl_achievements:
        tag menu
        modal True

        text "{font=[Fl_Script]}{size=60}Достижения{/size}{/font}":
            yalign 0.02
            xalign 0.5
            antialias True
            outlines [(1, "#000000", 0, 0)]

        textbutton ["Назад"] at Fl_menu_hover:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_big_save_load" style "Fl_button_None"
            align (0.02, 0.98) action [Hide("gallery4", Dissolve(1.0)), Jump("before_main_menu")]
            

        hbox:
            align(0.425, 0.3)
            spacing 8

            vbox:
                spacing 3

                for i in range(1, 5):
                    $ achievement_var = getattr(persistent, "Fl_dostn_%d" % i, False)
                    if achievement_var:
                        add "gui/progress/Fl_dost_%d_in_kod.png" % i
                    else:
                        add "gui/progress/Fl_dost_none.png"

            vbox:
                spacing 3

                for i in range(4, 8):
                    $ achievement_var = getattr(persistent, "Fl_dostn_%d" % i, False)
                    if achievement_var:
                        add "gui/progress/Fl_dost_%d_in_kod.png" % i
                    else:
                        add "gui/progress/Fl_dost_none.png"

            vbox:
                spacing 3

                for i in range(8, 12):
                    $ achievement_var = getattr(persistent, "Fl_dostn_%d" % i, False)
                    if achievement_var:
                        add "gui/progress/Fl_dost_%d_in_kod.png" % i
                    else:
                        add "gui/progress/Fl_dost_none.png"

            vbox:
                spacing 3

                for i in range(12, 16):
                    $ achievement_var = getattr(persistent, "Fl_dostn_%d" % i, False)
                    if achievement_var:
                        add "gui/progress/Fl_dost_%d_in_kod.png" % i
                    else:
                        add "gui/progress/Fl_dost_none.png"






#Меню длс
label intro_q66:
    $ Fl.StopAmbience(2)
    $ Fl.StopMusic(2)
    scene bg Fl_black with Fl_dissolve1_5
    $ Fl.Pause (2.0)
    $ renpy.movie_cutscene("videos/Fl_intro_dls.ogv")
    jump dls_q66







#Подтверждение
screen Fl_quit_menu:
    tag menu3
    modal True
    fixed at Fl_menu_move:
    
    
        $ timeofday = persistent.timeofday
        $ time_of_day = persistent.timeofday
        button:
            style "blank_button"
            xalign 0
            yalign 0
            xfill True
            yfill True
            action Return()

        add "gui/choice.png"
        text "{font=[Fl_Script]}{size=50}Вы действительно хотите выйти в главное меню?{/size}{/font}":
            text_align 0.5
            yalign 0.40
            xalign 0.5
            antialias True
            kerning 2
            
        textbutton ["Да"]:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_big_save_load"
            style "Fl_button_None"
            yalign 0.5
            xalign 0.42
            action [Start('Fl_exit')] #MainMenu(confirm = False)]
            at Fl_menu_hover
        
        textbutton ["Нет"]:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_big_save_load"
            style "Fl_button_None"
            yalign 0.5
            xalign 0.58
            action Return()
            at Fl_menu_hover


screen Fl_loading(time):
    tag menu
    modal True
    for key_dismiss in Fl_key_dismiss_list:
        key key_dismiss action NullAction()
    add "gui/loading/none.png" at Fl_loading_bg_move
    add "Fl_interference_anim" at Fl_alpha(0.5)
    timer 0.013 repeat True action If(load_value < 100, 
        true=SetVariable("load_value", load_value + time), 
        false=[Stop("music", fadeout=3), Hide("Fl_loading", transition=Dissolve(2.0, alpha=True)), Return()])
    vbox xalign 0.5 yalign 0.95:
        text "Загрузка..." xalign 0.5 xanchor 0.5 style "Fl_text_setting"
        bar range 100 value load_value style "Fl_loading_bar"
        text str(int(load_value)) + "%" xalign 0.5 xanchor 0.5 style "Fl_text_setting_s"
    








label Fl_exit:#ВЫХОД ИЗ МОДА
    $ _window_hide(dissolve)
    $ Fl.Pause (1, hard=True)
    $ Fl.StopMusic(2)
    scene bg Fl_black with Fl_dissolve1
    $ Fl.Pause (3, hard=True)
    return     

