# -*- coding: ひきこもり -*-

#Само меню
label before_main_menu:
    $ renpy.block_rollback()
    scene bg Fl_menu
    show Fl_rain_hard_left
    $ Fl.StopSound(1)
    $ Fl.StopAmbience(1)
    $ Fl.PlayMusic("Fl_senritsu", 1, 2)
    $ Fl.PlayAmbience("Fl_rain", 1, 2)

    if persistent.Fl_update_2 == False:
        $ persistent.Fl_update_2 = True
        call screen update_bg

    else:
        call screen main_menu

screen main_menu():
        tag menu
        modal True

        text "{font=[Fl_Script]}{size=80}ВСЛЕД ЗА СВЕТОМ{/size}{/font}":
                yalign -0.5
                xalign 0.08
                antialias True
                at Fl_menu_rotate


        
        vbox:
            style_prefix "navigation"

            xpos gui.navigation_xpos
            yalign 0.59
            spacing gui.navigation_spacing
            

            textbutton _("Начать") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (Hide ("main_menu"), Start("Fl_start")) at Fl_menu_hover

            textbutton _("Загрузить") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (ShowMenu("Fl_load_bg")) at Fl_menu_hover

            textbutton _("DLC") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (ShowMenu("dls")) at Fl_menu_hover

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
    $ Fl.PlaySound("Fl_tv_noise", 1, 1, True)
    scene Fl_night_TV_sl
    show Fl_pulsing at Fl_alpha(0.4)
    show Fl_layer_preference

    #Вызов самой префер
    call screen Fl_preference_menu
    screen Fl_preference_menu:
        tag menu
        modal True
        add "gui/main_menu/Fl_ground.png"

        add "gui/main_menu/preferences/Fl_preference_osn.png":
            zoom 0.7 xpos 90 ypos 41
        text ["{font=[Fl_Script]}:{/font}"]:
            size 60
            xalign 0.202
            yalign 0.0425


        add "gui/main_menu/preferences/Fl_rezim_osn.png":
            zoom 0.8 xpos 172 ypos 104

        if not _preferences.fullscreen:
            imagebutton:
                xalign 0.044 yalign 0.149 yoffset 0
                idle ("gui/main_menu/preferences/Fl_window_hover.png")
                hover ("gui/main_menu/preferences/Fl_window_hover.png")
            imagebutton:
                xalign 0.219 yalign 0.151 yoffset 0
                auto "gui/main_menu/preferences/Fl_fullscreen_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action (Preference("display", "fullscreen"))
        else:
            imagebutton:
                xalign 0.044 yalign 0.149 yoffset 0
                auto "gui/main_menu/preferences/Fl_window_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action (Preference("display", "window"))
            imagebutton:
                xalign 0.219 yalign 0.151 yoffset 0
                idle ("gui/main_menu/preferences/Fl_fullscreen_hover.png")
                hover ("gui/main_menu/preferences/Fl_fullscreen_hover.png")


        add "gui/main_menu/preferences/Fl_theme.png":
            zoom 0.74 xpos 732 ypos 104
                
        if persistent.Fl_ch_interface == True:
            imagebutton:
                xalign 0.394 yalign 0.149 yoffset 0
                idle ("gui/main_menu/preferences/Fl_ch_hover.png")
                hover ("gui/main_menu/preferences/Fl_ch_hover.png")
            imagebutton:
                xalign 0.479 yalign 0.151 yoffset 0
                auto "gui/main_menu/preferences/Fl_rgb_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action (SetField(persistent, "Fl_ch_interface", False))
        else:
            imagebutton:
                xalign 0.394 yalign 0.149 yoffset 0
                auto "gui/main_menu/preferences/Fl_ch_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action (SetField(persistent, "Fl_ch_interface", True))
            imagebutton:
                xalign 0.479 yalign 0.151 yoffset 0
                idle ("gui/main_menu/preferences/Fl_rgb_hover.png")
                hover ("gui/main_menu/preferences/Fl_rgb_hover.png")


        add "gui/main_menu/preferences/Fl_filtr_osn.png": 
            zoom 0.8 xpos 168 ypos 222

        if persistent.Fl_swear_filter == True:
            imagebutton:
                xalign 0.039 yalign 0.267 yoffset 0
                idle ("gui/main_menu/preferences/Fl_on_hover.png")
                hover ("gui/main_menu/preferences/Fl_on_hover.png")
    
            imagebutton:
                xalign 0.243 yalign 0.269 yoffset 0
                auto "gui/main_menu/preferences/Fl_off_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action (SetField(persistent, "Fl_swear_filter", False))
        
        else:
            imagebutton:
                xalign 0.039 yalign 0.267 yoffset 0
                auto "gui/main_menu/preferences/Fl_on_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action (SetField(persistent, "Fl_swear_filter", True))
            imagebutton:
                xalign 0.243 yalign 0.269 yoffset 0
                idle ("gui/main_menu/preferences/Fl_off_hover.png")
                hover ("gui/main_menu/preferences/Fl_off_hover.png")

            

        add "gui/main_menu/preferences/Fl_skip_menu.png":
            zoom 0.8 xpos 171 ypos 341
                
        if not _preferences.skip_unseen:
            imagebutton:
                xalign 0.163 yalign 0.385 yoffset 0
                idle ("gui/main_menu/preferences/Fl_readed_hover.png")
                hover ("gui/main_menu/preferences/Fl_readed_hover.png")
            imagebutton:
                xalign 0.068 yalign 0.385 yoffset 0
                auto "gui/main_menu/preferences/Fl_all_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action (Preference("skip", "all"))
        else:
            imagebutton:
                xalign 0.163 yalign 0.385 yoffset 0
                auto "gui/main_menu/preferences/Fl_readed_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action (Preference("skip", "seen"))
            imagebutton:
                xalign 0.068 yalign 0.385 yoffset 0
                idle ("gui/main_menu/preferences/Fl_all_hover.png")
                hover ("gui/main_menu/preferences/Fl_all_hover.png")


        add "gui/main_menu/preferences/Fl_podsk_osn.png":
            zoom 0.8 xpos 163 ypos 464

        if persistent.Fl_podsk_count == True:
            imagebutton:
                xalign 0.049 yalign 0.502 yoffset 0
                idle ("gui/main_menu/preferences/Fl_on2_hover.png")
                hover ("gui/main_menu/preferences/Fl_on2_hover.png")
            imagebutton:
                xalign 0.236 yalign 0.502 yoffset 0
                auto "gui/main_menu/preferences/Fl_off2_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action (SetField(persistent, "Fl_podsk_count", False))
            
        else:
            imagebutton:
                xalign 0.049 yalign 0.502 yoffset 0
                auto "gui/main_menu/preferences/Fl_on2_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action (SetField(persistent, "Fl_podsk_count", True))
            imagebutton:
                xalign 0.236 yalign 0.502 yoffset 0
                idle ("gui/main_menu/preferences/Fl_off2_hover.png")
                hover ("gui/main_menu/preferences/Fl_off2_hover.png")
    



        add "gui/main_menu/preferences/Fl_music_menu.png":
            zoom 0.8 xpos 271 ypos 565    
        bar:
            value Preference("music volume")
            right_bar "gui/main_menu/preferences/Fl_scale_chist.png"
            left_bar "gui/main_menu/preferences/Fl_scale_poln.png"
            thumb "gui/main_menu/preferences/Fl_begunok.png"
            xpos 188
            ypos 626
            xmaximum 365
            ymaximum 70


        add "gui/main_menu/preferences/Fl_sound_menu.png":
            zoom 0.8 xpos 261 ypos 694 
        bar:
            value Preference("sound volume")
            right_bar "gui/main_menu/preferences/Fl_scale_chist.png"
            left_bar "gui/main_menu/preferences/Fl_scale_poln.png"
            thumb "gui/main_menu/preferences/Fl_begunok.png"
            xpos 188
            ypos 761
            xmaximum 365
            ymaximum 70


        add "gui/main_menu/preferences/Fl_ambience_menu.png":
            zoom 0.8 xpos 261 ypos 825
        bar:
            value Preference("voice volume")
            right_bar "gui/main_menu/preferences/Fl_scale_chist.png"
            left_bar "gui/main_menu/preferences/Fl_scale_poln.png"
            thumb "gui/main_menu/preferences/Fl_begunok.png"
            xpos 188
            ypos 887
            xmaximum 365
            ymaximum 70
            


        textbutton ["Назад"]:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_setting" style "Fl_button_None"
            pos (90, 985) action [Hide("Fl_preference_menu", Dissolve(1.0)), Jump("before_main_menu")]

        imagebutton:
            xpos 1440 ypos 885
            auto "gui/main_menu/preferences/Fl_knopka_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_activate_screen_nya")







label Fl_preference_bg_q66:
    $ Fl.StopAmbience(1)
    $ Fl.PlaySound("Fl_tv_noise", 1, 1, True)
    scene Fl_night_TV_sl
    show Fl_pulsing at Fl_alpha(0.4)
    show Fl_layer_preference

    #Вызов самой префер
    call screen Fl_preference_menu_q66
    screen Fl_preference_menu_q66:
        tag menu
        modal True
        add "gui/main_menu/Fl_ground.png"

        add "gui/main_menu/preferences/Fl_preference_osn.png":
            zoom 0.7 xpos 90 ypos 41
        text ["{font=[Fl_Script]}:{/font}"]:
            size 60
            xalign 0.202
            yalign 0.0425


        add "gui/main_menu/preferences/Fl_rezim_osn.png":
            zoom 0.8 xpos 172 ypos 104

        if not _preferences.fullscreen:
            imagebutton:
                xalign 0.044 yalign 0.149 yoffset 0
                idle ("gui/main_menu/preferences/Fl_window_hover.png")
                hover ("gui/main_menu/preferences/Fl_window_hover.png")
            imagebutton:
                xalign 0.219 yalign 0.151 yoffset 0
                auto "gui/main_menu/preferences/Fl_fullscreen_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action (Preference("display", "fullscreen"))
        else:
            imagebutton:
                xalign 0.044 yalign 0.149 yoffset 0
                auto "gui/main_menu/preferences/Fl_window_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action (Preference("display", "window"))
            imagebutton:
                xalign 0.219 yalign 0.151 yoffset 0
                idle ("gui/main_menu/preferences/Fl_fullscreen_hover.png")
                hover ("gui/main_menu/preferences/Fl_fullscreen_hover.png")


        add "gui/main_menu/preferences/Fl_theme.png":
            zoom 0.74 xpos 732 ypos 104
                
        if persistent.Fl_ch_interface == True:
            imagebutton:
                xalign 0.394 yalign 0.149 yoffset 0
                idle ("gui/main_menu/preferences/Fl_ch_hover.png")
                hover ("gui/main_menu/preferences/Fl_ch_hover.png")
            imagebutton:
                xalign 0.479 yalign 0.151 yoffset 0
                auto "gui/main_menu/preferences/Fl_rgb_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action (SetField(persistent, "Fl_ch_interface", False))
        else:
            imagebutton:
                xalign 0.394 yalign 0.149 yoffset 0
                auto "gui/main_menu/preferences/Fl_ch_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action (SetField(persistent, "Fl_ch_interface", True))
            imagebutton:
                xalign 0.479 yalign 0.151 yoffset 0
                idle ("gui/main_menu/preferences/Fl_rgb_hover.png")
                hover ("gui/main_menu/preferences/Fl_rgb_hover.png")


        add "gui/main_menu/preferences/Fl_filtr_osn.png": 
            zoom 0.8 xpos 168 ypos 222

        imagebutton:
            xalign 0.039 yalign 0.267 yoffset 0
            idle ("gui/main_menu/preferences/Fl_on_idle.png")
            hover ("gui/main_menu/preferences/Fl_on_idle.png")
        imagebutton:
            xalign 0.243 yalign 0.269 yoffset 0
            idle ("gui/main_menu/preferences/Fl_off_idle.png")
            hover ("gui/main_menu/preferences/Fl_off_idle.png")
            

        add "gui/main_menu/preferences/Fl_skip_menu.png":
            zoom 0.8 xpos 171 ypos 341
                
        if not _preferences.skip_unseen:
            imagebutton:
                xalign 0.163 yalign 0.385 yoffset 0
                idle ("gui/main_menu/preferences/Fl_readed_hover.png")
                hover ("gui/main_menu/preferences/Fl_readed_hover.png")
            imagebutton:
                xalign 0.068 yalign 0.385 yoffset 0
                auto "gui/main_menu/preferences/Fl_all_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action (Preference("skip", "all"))
        else:
            imagebutton:
                xalign 0.163 yalign 0.385 yoffset 0
                auto "gui/main_menu/preferences/Fl_readed_%s.png"
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                action (Preference("skip", "seen"))
            imagebutton:
                xalign 0.068 yalign 0.385 yoffset 0
                idle ("gui/main_menu/preferences/Fl_all_hover.png")
                hover ("gui/main_menu/preferences/Fl_all_hover.png")


        add "gui/main_menu/preferences/Fl_podsk_osn.png":
            zoom 0.8 xpos 163 ypos 464

        imagebutton:
            xalign 0.049 yalign 0.502 yoffset 0
            idle ("gui/main_menu/preferences/Fl_on2_idle.png")
            hover ("gui/main_menu/preferences/Fl_on2_idle.png")
        imagebutton:
            xalign 0.236 yalign 0.502 yoffset 0
            idle ("gui/main_menu/preferences/Fl_off2_idle.png")
            hover ("gui/main_menu/preferences/Fl_off2_idle.png")



        add "gui/main_menu/preferences/Fl_music_menu.png":
            zoom 0.8 xpos 271 ypos 565    
        bar:
            value Preference("music volume")
            right_bar "gui/main_menu/preferences/Fl_scale_chist.png"
            left_bar "gui/main_menu/preferences/Fl_scale_poln.png"
            thumb "gui/main_menu/preferences/Fl_begunok.png"
            xpos 188
            ypos 626
            xmaximum 365
            ymaximum 70


        add "gui/main_menu/preferences/Fl_sound_menu.png":
            zoom 0.8 xpos 261 ypos 694 
        bar:
            value Preference("sound volume")
            right_bar "gui/main_menu/preferences/Fl_scale_chist.png"
            left_bar "gui/main_menu/preferences/Fl_scale_poln.png"
            thumb "gui/main_menu/preferences/Fl_begunok.png"
            xpos 188
            ypos 761
            xmaximum 365
            ymaximum 70


        add "gui/main_menu/preferences/Fl_ambience_menu.png":
            zoom 0.8 xpos 261 ypos 825
        bar:
            value Preference("voice volume")
            right_bar "gui/main_menu/preferences/Fl_scale_chist.png"
            left_bar "gui/main_menu/preferences/Fl_scale_poln.png"
            thumb "gui/main_menu/preferences/Fl_begunok.png"
            xpos 188
            ypos 887
            xmaximum 365
            ymaximum 70
            


        textbutton ["Назад"]:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_setting" style "Fl_button_None"
            pos (90, 985) action [Hide("Fl_preference_menu", Dissolve(1.0)), Jump("main_menu_q_66")]

        imagebutton:
            xpos 1440 ypos 885
            auto "gui/main_menu/preferences/Fl_knopka_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("Fl_activate_screen_nya")






#Экран загрузки Fl
label Fl_load_bg:
    $ Fl.StopAmbience(1)
    $ Fl.PlayAmbience("Fl_bizzard_outside", 1, 2)
    $ Fl.PlaySound("Fl_knife_loop", 1, 1, True)
    scene bus 
    show hand at Fl_rotate_hand
    show Fl_layer_load
    show Fl_snow at Fl_linear_effects_repeat(0.4, 0.75, 0.7, 0.75, 0.25, 0.3, 0.25)

    #Вызов самой загрузки
    call screen Fl_load_menu
    screen Fl_load_menu():
        tag menu
        modal True
        fixed yoffset 120 xoffset 400 at Fl_menu_move(0.75, 0.5, 0):
            add "gui/main_menu/save/save_background.png"


        text "{font=[Fl_Script]}{size=75}ВСЛЕД ЗА СВЕТОМ{/size}{/font}":
            yalign -0.5
            xalign 0.9
            antialias True
            at Fl_menu_rotate_min

        fixed align (0.5, 0.5) anchor (0.5, 0.5) at Fl_menu_move(0.7, 0.5, 0):
            text ["{font=[Fl_Script]}Загрузить{/font}"]:
                size 60
                text_align 0.5
                xalign 0.873
                yalign 0.305
                antialias True
                kerning 2

            textbutton ["{font=[Fl_Script]}Загрузить игру{/font}"]:
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                text_style "Fl_text_big_save_load"
                style "Fl_button_None"
                text_size 50
                ypos 1010
                xalign 0.887
                action (Fl_FunctionCallback(Fl.CallbackOnLoad, selected_slot), FileLoad(selected_slot))
            textbutton ["Удалить"]:
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                text_style "Fl_text_big_save_load"
                style "Fl_button_None"
                text_size 50
                xpos 1900
                ypos 1010
                action FileDelete(selected_slot)
            textbutton ["Назад"]:
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                text_style "Fl_text_big_save_load"
                style "Fl_button_None"
                text_size 50
                xpos 930
                ypos 1010
                action [Hide("Fl_load_menu", Dissolve(1.0)), Jump("before_main_menu")]
        use Fl_save_load_slots_menu





label Fl_load_bg_q66:
    $ Fl.StopAmbience(1)
    $ Fl.PlayAmbience("Fl_bizzard_outside", 1, 2)
    $ Fl.PlaySound("Fl_knife_loop", 1, 1, True)
    scene bus 
    show hand at Fl_rotate_hand
    show Fl_layer_load
    show Fl_snow at Fl_linear_effects_repeat(0.4, 0.75, 0.7, 0.75, 0.25, 0.3, 0.25)

    #Вызов самой загрузки
    call screen Fl_load_menu_q66
    screen Fl_load_menu_q66():
        tag menu
        modal True
        fixed yoffset 120 xoffset 400 at Fl_menu_move(0.75, 0.5, 0):
            add "gui/main_menu/save/save_background.png"


        fixed align (0.5, 0.5) anchor (0.5, 0.5) at Fl_menu_move(0.7, 0.5, 0):
            text ["{font=[Fl_Script]}Загрузить{/font}"]:
                size 60
                text_align 0.5
                xalign 0.873
                yalign 0.305
                antialias True
                kerning 2

            textbutton ["{font=[Fl_Script]}Загрузить игру{/font}"]:
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                text_style "Fl_text_big_save_load"
                style "Fl_button_None"
                text_size 50
                ypos 1010
                xalign 0.887
                action (Fl_FunctionCallback(Fl.CallbackOnLoad, selected_slot), FileLoad(selected_slot))
            textbutton ["Удалить"]:
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                text_style "Fl_text_big_save_load"
                style "Fl_button_None"
                text_size 50
                xpos 1900
                ypos 1010
                action FileDelete(selected_slot)
            textbutton ["Назад"]:
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                text_style "Fl_text_big_save_load"
                style "Fl_button_None"
                text_size 50
                xpos 930
                ypos 1010
                action [Hide("Fl_load_menu", Dissolve(1.0)), Jump("main_menu_q_66")]
        use Fl_save_load_slots_menu








#Экран слотов(меню)
screen Fl_save_load_slots_menu:
    fixed align (0.5, 0.5) anchor (0.5, 0.5) at Fl_menu_move(0.7, 0.5, 0, 0.45):
        vbox:
            xalign 0.52
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
            yoffset 170 xoffset 650
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
    fixed align (0.5, 0.5) anchor (0.5, 0.5) at Fl_menu_move(0.7, 0.5, 0):
        vbox:
            xalign 0.08
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
            xpos 0.125
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
        add "gui/main_menu/gallery/Fl_gallery_14.png":
            xpos 1700 ypos 975


        imagebutton:
            auto "gui/main_menu/gallery/Fl_strelka2_gallery_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action ShowMenu("Fl_gallery2")
            at Fl_strel_zoom1

        textbutton ["Назад"]:
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                text_style "Fl_text_big_save_load" style "Fl_button_None"
                pos (90, 985) action [Hide("gallery", Dissolve(1.0)), Jump("before_main_menu")]

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
    add "gui/main_menu/gallery/Fl_gallery_24.png":
        xpos 1700 ypos 975
    imagebutton:
        auto "gui/main_menu/gallery/Fl_strelka2_gallery_%s.png"
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        action ShowMenu("Fl_gallery2")
        at Fl_strel_zoom1

    textbutton ["Назад"]:
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        text_style "Fl_text_big_save_load" style "Fl_button_None"
        pos (90, 985) action [Hide("gallery", Dissolve(1.0)), Jump("before_main_menu")]

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
        auto "gui/main_menu/gallery/Fl_strelka2_gallery_%s.png"
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        action ShowMenu("Fl_gallery3")
        at Fl_strel_zoom1

    imagebutton:
        auto "gui/main_menu/gallery/Fl_strelka_gallery_%s.png"
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        action ShowMenu("Fl_gallery")
        at Fl_strel_zoom2

    textbutton ["Назад"]:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_big_save_load" style "Fl_button_None"
            pos (90, 985) action [Hide("gallery2", Dissolve(1.0)), Jump("before_main_menu")]

    add "Fl_gallery_lych" at Fl_gallery_lych_anim


screen Fl_gallery3:
    tag menu
    modal True
    add "gui/main_menu/gallery/Fl_gallery_34.png":
        xpos 1700 ypos 975

    imagebutton:
        auto "gui/main_menu/gallery/Fl_strelka2_gallery_%s.png"
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        action ShowMenu("Fl_gallery4")
        at Fl_strel_zoom1

    imagebutton:
        auto "gui/main_menu/gallery/Fl_strelka_gallery_%s.png"
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        action ShowMenu("Fl_gallery2")
        at Fl_strel_zoom2

    textbutton ["Назад"]:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_big_save_load" style "Fl_button_None"
            pos (90, 985) action [Hide("gallery3", Dissolve(1.0)), Jump("before_main_menu")]

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
    add "gui/main_menu/gallery/Fl_gallery_44.png":
        xpos 1700 ypos 975

    text "{font=[Fl_Script]}{size=80}Скоро...{/size}{/font}":
            yalign 0.5
            xalign 0.5
            antialias True
            at Fl_menu_rotate

    imagebutton:
        auto "gui/main_menu/gallery/Fl_strelka_gallery_%s.png"
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        action ShowMenu("Fl_gallery3")
        at Fl_strel_zoom2

    textbutton ["Назад"]:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_big_save_load" style "Fl_button_None"
            pos (90, 985) action [Hide("gallery4", Dissolve(1.0)), Jump("before_main_menu")]

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




#DLS
label dls:
    $ Fl.StopAmbience(1)
    call screen Fl_dls
    screen Fl_dls:
        tag menu
        modal True
        add "Fl_vignette"


        imagebutton:
            xalign 0.5
            yalign 0.5
            auto "gui/main_menu/dls/Fl_dls1_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Jump("dls1")

        textbutton "X":
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            style "Fl_button_None"
            text_style "Fl_text_setting_dls_s"
            text_size 40
            xpos 1880 
            ypos 0
            action [Hide("dls", Dissolve(0.5)), Jump("before_main_menu")]


        textbutton ">":
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            style "Fl_button_None"
            text_style "Fl_text_setting_dls_s"
            text_size 140
            xpos 1780
            ypos 500
            action ShowMenu("Fl_dls2")

        


screen Fl_dls2:
    tag menu
    modal True
    add "Fl_vignette"


    imagebutton:
        xalign 0.5
        yalign 0.5
        auto "gui/main_menu/dls/Fl_dls2_%s.png"
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        action Jump("dls2")

    textbutton "X":
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        style "Fl_button_None"
        text_style "Fl_text_setting_dls_s"
        text_size 40
        xpos 1880 
        ypos 0
        action [Hide("dls", Dissolve(0.5)), Jump("before_main_menu")]


    textbutton ">":
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        style "Fl_button_None"
        text_style "Fl_text_setting_dls_s"
        text_size 140
        xpos 1780
        ypos 500
        action ShowMenu("Fl_dls3")


screen Fl_dls3:
    tag menu
    modal True
    add "Fl_vignette"


    imagebutton:
        xalign 0.5
        yalign 0.5
        auto "gui/main_menu/dls/Fl_dls3_%s.png"
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        action [Hide("dls", Dissolve(0.5)), Jump("intro_q66")]

    textbutton "X":
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        style "Fl_button_None"
        text_style "Fl_text_setting_dls_s"
        text_size 40
        xpos 1880 
        ypos 0
        action [Hide("dls", Dissolve(0.5)), Jump("before_main_menu")]


    textbutton ">":
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        style "Fl_button_None"
        text_style "Fl_text_setting_dls_s"
        text_size 140
        xpos 1780
        ypos 500
        action ShowMenu("Fl_dls")






#Достижения
label achievements:
    $ Fl.StopAmbience(1)
    scene Fl_progress_osn
    call screen Fl_achievements
    screen Fl_achievements:
        tag menu
        modal True

        textbutton ["Назад"]:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_big_save_load" style "Fl_button_None"
            pos (40, 985) action [Hide("gallery4", Dissolve(1.0)), Jump("before_main_menu")]
        if persistent.Fl_dostn_1 == True:
            add "gui/progress/Fl_dost1.png"
        else:
            add "gui/progress/Fl_dost1_none.png"

        if persistent.Fl_dostn_2 == True:
            add "gui/progress/Fl_dost2.png"
        else:
            add "gui/progress/Fl_dost2_none.png"

        if persistent.Fl_dostn_3 == True:
            add "gui/progress/Fl_dost3.png"
        else:
            add "gui/progress/Fl_dost3_none.png"

        if persistent.Fl_dostn_4 == True:
            add "gui/progress/Fl_dost4.png"
        else:
            add "gui/progress/Fl_dost4_none.png"

        if persistent.Fl_dostn_5 == True:
            add "gui/progress/Fl_dost5.png"
        else:
            add "gui/progress/Fl_dost5_none.png"

        if persistent.Fl_dostn_6 == True:
            add "gui/progress/Fl_dost6.png"
        else:
            add "gui/progress/Fl_dost6_none.png"

        if persistent.Fl_dostn_7 == True:
            add "gui/progress/Fl_dost7.png"
        else:
            add "gui/progress/Fl_dost7_none.png"

        if persistent.Fl_dostn_8 == True:
            add "gui/progress/Fl_dost8.png"
        else:
            add "gui/progress/Fl_dost8_none.png"

        if persistent.Fl_dostn_9 == True:
            add "gui/progress/Fl_dost9.png"
        else:
            add "gui/progress/Fl_dost9_none.png"

        if persistent.Fl_dostn_10 == True:
            add "gui/progress/Fl_dost10.png"
        else:
            add "gui/progress/Fl_dost10_none.png"

        if persistent.Fl_dostn_11 == True:
            add "gui/progress/Fl_dost11.png"
        else:
            add "gui/progress/Fl_dost11_none.png"

        if persistent.Fl_dostn_12 == True:
            add "gui/progress/Fl_dost12.png"
        else:
            add "gui/progress/Fl_dost12_none.png"
        
        if persistent.Fl_dostn_13 == True:
            add "gui/progress/Fl_dost13.png"
        else:
            add "gui/progress/Fl_dost13_none.png"

        if persistent.Fl_dostn_11 == True:
            add "gui/progress/Fl_dost11.png"
        else:
            add "gui/progress/Fl_dost11_none.png"

        if persistent.Fl_dostn_12 == True:
            add "gui/progress/Fl_dost12.png"
        else:
            add "gui/progress/Fl_dost12_none.png"

        if persistent.Fl_dostn_13 == True:
            add "gui/progress/Fl_dost13.png"
        else:
            add "gui/progress/Fl_dost13_none.png"

        if persistent.Fl_dostn_14 == True:
            add "gui/progress/Fl_dost14.png"
        else:
            add "gui/progress/Fl_dost14_none.png"

        if persistent.Fl_dostn_15 == True:
            add "gui/progress/Fl_dost15.png"
        else:
            add "gui/progress/Fl_dost15_none.png"

        if persistent.Fl_dostn_16 == True:
            add "gui/progress/Fl_dost16.png"
        else:
            add "gui/progress/Fl_dost16_none.png"

        if persistent.Fl_dostn_17 == True:
            add "gui/progress/Fl_dost17.png"
        else:
            add "gui/progress/Fl_dost17_none.png"

        if persistent.Fl_dostn_18 == True:
            add "gui/progress/Fl_dost18.png"
        else:
            add "gui/progress/Fl_dost18_none.png"

        if persistent.Fl_dostn_19 == True:
            add "gui/progress/Fl_dost19.png"
        else:
            add "gui/progress/Fl_dost19_none.png"

        if persistent.Fl_dostn_20 == True:
            add "gui/progress/Fl_dost20.png"
        else:
            add "gui/progress/Fl_dost20_none.png"

        if persistent.Fl_dostn_21 == True:
            add "gui/progress/Fl_dost21.png"
        else:
            add "gui/progress/Fl_dost21_none.png"

        if persistent.Fl_dostn_22 == True:
            add "gui/progress/Fl_dost22.png"
        else:
            add "gui/progress/Fl_dost22_none.png"

        if persistent.Fl_dostn_23 == True:
            add "gui/progress/Fl_dost23.png"
        else:
            add "gui/progress/Fl_dost23_none.png"

        if persistent.Fl_dostn_24 == True:
            add "gui/progress/Fl_dost24.png"
        else:
            add "gui/progress/Fl_dost24_none.png"

        if persistent.Fl_dostn_25 == True:
            add "gui/progress/Fl_dost25.png"
        else:
            add "gui/progress/Fl_dost25_none.png"

        if persistent.Fl_dostn_26 == True:
            add "gui/progress/Fl_dost26.png"
        else:
            add "gui/progress/Fl_dost26_none.png"

        if persistent.Fl_dostn_27 == True:
            add "gui/progress/Fl_dost27.png"
        else:
            add "gui/progress/Fl_dost27_none.png"

        if persistent.Fl_dostn_28 == True:
            add "gui/progress/Fl_dost28.png"
        else:
            add "gui/progress/Fl_dost28_none.png"





#Меню длс
label intro_q66:
    scene bg Fl_black with Fl_dissolve1
    $ Fl.Pause (1.5)
    $ renpy.movie_cutscene("videos/Fl_intro_dls.ogv")
    jump main_menu_q_66


label main_menu_q_66:
    $ Fl.StopSound(1)
    $ Fl.StopMusic(1)
    $ Fl.StopAmbience(1)
    $ Fl.PlayMusicFrom("<from 0 to 50>", "Fl_one_step_to_the_horizon", 1, 2)
    scene bg Fl_menu_q66
    call screen main_menu_q66

screen main_menu_q66():
        tag menu
        modal True

        text "{font=[Fl_dls]}{size=80}Одиночка{/size}{/font}":
                yalign 0.1
                xalign 0.09
                antialias True
                at Fl_menu_rotate

        
        vbox:
            style_prefix "navigation"

            xpos gui.navigation_xpos
            yalign 0.59

            spacing gui.navigation_spacing

            textbutton _("{font=[Fl_dls]}{size=40}Начать{/size}{/font}") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (Hide ("main_menu"), Start("dls_q66")) at Fl_menu_hover

            textbutton _("{font=[Fl_dls]}{size=40}Загрузить{/size}{/font}") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (ShowMenu("Fl_load_bg_q66")) at Fl_menu_hover

            textbutton _("{font=[Fl_dls]}{size=40}Настройки{/size}{/font}") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (ShowMenu("Fl_preference_bg_q66")) at Fl_menu_hover

            if renpy.variant("pc"):

                textbutton _("{font=[Fl_dls]}{size=40}Выход{/size}{/font}") hover_sound "gui/main_menu/Fl_click_menu.mp3" action [Hide("main_menu_q66", Dissolve(1.0)), Jump("before_main_menu")] at Fl_menu_hover

        if gui.show_name:

            vbox:
                style "main_menu_vbox"

                text "[config.name!t]":
                    style "main_menu_title"

                text "[config.version]":
                    style "main_menu_version"







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
    timer 0.01 repeat True action If(load_value < 100, 
        true=SetVariable("load_value", load_value + time), 
        false=[Stop("music", fadeout=3), Hide("Fl_loading", transition=Dissolve(2.0, alpha=True)), Return()])
    vbox xalign 0.5 ypos 0.8:
        text "Загрузка..." xalign 0.5 xanchor 0.5 style "Fl_text_setting"
        bar range 100 value load_value style "Fl_loading_bar"
        text str(int(load_value)) + "%" xalign 0.5 xanchor 0.5 style "Fl_text_setting_s"
        text "В игре присуствует автосохранение." xalign 0.5 xanchor 0.5 style "Fl_text_setting_sl"
    add "icon" yoffset 160 at Fl_full_rotate_repeat(1.0, 0.5, 1.0, 0.8)








label Fl_exit:#ВЫХОД ИЗ МОДА
    $ _window_hide(dissolve)
    $ Fl.Pause (1, hard=True)
    $ Fl.StopMusic(2)
    scene bg Fl_black with Fl_dissolve1
    $ Fl.Pause (3, hard=True)
    return     

