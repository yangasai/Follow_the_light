# -*- coding: ひきこもり -*-
screen say:
    window:
        background None
        id "window"
        if persistent.Fl_ch_interface == True:
            add ("gui/dialogue_box/prologue/dialogue_box_st.png"):
                xpos 118
                ypos 866
            if Fl_status_action:
                text Fl_status_name pos (1280, 893) size 16 xanchor 0.0 font "font/Fl_mainmenu.ttf" color Fl_status_color
                text (str(Fl_status_points[0]) if Fl_status else "") pos (1236, 892) size 17 xanchor 0.5 font "font/Fl_mainmenu.ttf" color Fl_status_color
            if persistent.Fl_podsk_count == True:
                use view_score_screen
            imagebutton:
                auto ("gui/dialogue_box/prologue/backward_%s.png")
                xpos 0
                ypos 912
                action ShowMenu("history")
            imagebutton:
                auto ("gui/dialogue_box/prologue/hide_%s.png")
                xpos 1508
                ypos 903
                action HideInterface()
            imagebutton:
                auto ("gui/dialogue_box/prologue/save_%s.png")
                xpos 1567
                ypos 903
                action ShowMenu('Fl_save')
            imagebutton:
                auto ("gui/dialogue_box/prologue/menu_%s.png")
                xpos 1625
                ypos 903
                action ShowMenu('save')
            imagebutton:
                auto ("gui/dialogue_box/prologue/load_%s.png")
                xpos 1682
                ypos 903
                action ShowMenu('load')
            if not config.skipping:
                imagebutton:
                    auto ("gui/dialogue_box/prologue/forward_%s.png")
                    xpos 1759
                    ypos 912
                    action Skip()
            else:
                imagebutton:
                    auto ("gui/dialogue_box/prologue/fast_forward_%s.png")
                    xpos 1759
                    ypos 912
                    action Skip()
            text what:
                id "what"
                xpos 194
                ypos 930
                xmaximum 1481
                size 28
                color "#ffffff"
                line_spacing 1
            if who:
                text who:
                    id "who"
                    xpos 220
                    ypos 900
                    size 31
                    line_spacing 1


        elif persistent.Fl_ch_interface == False:
            add ("gui/dialogue_box/"+Fl_timeofday+"/dialogue_box_st.png"):
                xpos 118
                ypos 866
            if Fl_status_action:
                text Fl_status_name pos (1280, 893) size 16 xanchor 0.0 font "font/Fl_mainmenu.ttf" color Fl_status_color
                text (str(Fl_status_points[0]) if Fl_status else "") pos (1236, 892) size 17 xanchor 0.5 font "font/Fl_mainmenu.ttf" color Fl_status_color
            if persistent.Fl_podsk_count == True:
                use view_score_screen
            imagebutton:
                auto ("gui/dialogue_box/"+Fl_timeofday+"/backward_%s.png")
                xpos 0
                ypos 912
                action ShowMenu("history")
            imagebutton:
                auto ("gui/dialogue_box/"+Fl_timeofday+"/hide_%s.png")
                xpos 1508
                ypos 903
                action HideInterface()
            imagebutton:
                auto ("gui/dialogue_box/"+Fl_timeofday+"/save_%s.png")
                xpos 1567
                ypos 903
                action ShowMenu('Fl_save')
            imagebutton:
                auto ("gui/dialogue_box/"+Fl_timeofday+"/menu_%s.png")
                xpos 1625
                ypos 903
                action ShowMenu('save')
            imagebutton:
                auto ("gui/dialogue_box/"+Fl_timeofday+"/load_%s.png")
                xpos 1682
                ypos 903
                action ShowMenu('load')
            if not config.skipping:
                imagebutton:
                    auto ("gui/dialogue_box/"+Fl_timeofday+"/forward_%s.png")
                    xpos 1759
                    ypos 912
                    action Skip()
            else:
                imagebutton:
                    auto ("gui/dialogue_box/"+Fl_timeofday+"/fast_forward_%s.png")
                    xpos 1759
                    ypos 912
                    action Skip()
            text what:
                id "what"
                xpos 194
                ypos 930
                xmaximum 1481
                size 28
                color "#ffffff"
                line_spacing 1
            if who:
                text who:
                    id "who"
                    xpos 220
                    ypos 900
                    size 31
                    line_spacing 1



#Сейвы
screen Fl_save():
    modal True

    add "Fl_prolog_dream" at Fl_alpha(0.15)
    add "gui/quick_menu_zad.png"
    fixed yoffset 120 xoffset 270 at Fl_menu_move(0.9, 0.5, 0):
            add "gui/main_menu/save/save_background.png"

    fixed align (0.5, 0.5) anchor (0.5, 0.5) at Fl_menu_move(0.7, 0.5, 0):
        text ["{font=[Fl_Script]}Сохранить{/font}"]:
            size 70
            text_align 0.5
            xalign 0.5
            yalign 0.08
            antialias True
            kerning 2
        textbutton "<":
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            style "Fl_button_None"
            text_style "Fl_text_setting_s"
            text_size 60
            xalign 0.36
            yalign 0.08
            action [Hide("Fl_save", Dissolve(0.5)), ShowMenu("load")]
        textbutton ">":
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            style "Fl_button_None"
            text_style "Fl_text_setting_s"
            text_size 60
            xalign 0.64
            yalign 0.08
            action [Hide("Fl_save", Dissolve(0.5)), ShowMenu("preferences")]
        textbutton ["Сохранить игру"]:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_big_save_load"
            style "Fl_button_None"
            text_size 55
            ypos 950
            xalign 0.5
            if persistent._file_page != "Fl_FilePage_auto":
                action (Fl_FunctionCallback(Fl.CallbackOnSave, selected_slot), FileSave(selected_slot))
        textbutton ["Удалить"]:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_big_save_load"
            style "Fl_button_None"
            text_size 55
            xpos 1450
            ypos 950
            action FileDelete(selected_slot)
        textbutton ["Назад"]:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_big_save_load"
            style "Fl_button_None"
            text_size 55
            xpos 290
            ypos 950
            action Hide("Fl_save", Dissolve(0.5))
    use Fl_save_load_slots
        

#Загрузка
screen load():
    modal True

    add "Fl_prolog_dream" at Fl_alpha(0.15)
    add "gui/quick_menu_zad.png"
    fixed yoffset 120 xoffset 270 at Fl_menu_move(0.9, 0.5, 0):
            add "gui/main_menu/save/save_background.png"

    fixed align (0.5, 0.5) anchor (0.5, 0.5) at Fl_menu_move(0.7, 0.5, 0):
        text ["{font=[Fl_Script]}Загрузить{/font}"]:
            size 70
            text_align 0.5
            xalign 0.5
            yalign 0.08
            antialias True
            kerning 2
        textbutton "<":
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            style "Fl_button_None"
            text_style "Fl_text_setting_s"
            text_size 60
            xalign 0.36
            yalign 0.08
            action [Hide("load", Dissolve(0.5)), ShowMenu("preferences")]
        textbutton ">":
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            style "Fl_button_None"
            text_style "Fl_text_setting_s"
            text_size 60
            xalign 0.64
            yalign 0.08
            action [Hide("load", Dissolve(0.5)), ShowMenu("Fl_save")]

        textbutton ["Загрузить игру"]:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_big_save_load"
            style "Fl_button_None"
            text_size 55
            ypos 950
            xalign 0.51
            action (Fl_FunctionCallback(Fl.CallbackOnLoad, selected_slot), FileLoad(selected_slot))
        textbutton ["Удалить"]:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_big_save_load"
            style "Fl_button_None"
            text_size 55
            xpos 1450
            ypos 950
            action FileDelete(selected_slot)
        textbutton ["Назад"]:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_big_save_load"
            style "Fl_button_None"
            text_size 55
            xpos 290
            ypos 950
            action Hide("load", Dissolve(0.5))
    use Fl_save_load_slots
    


#Настройки
screen preferences():
    modal True

    add "Fl_prolog_dream" at Fl_alpha(0.15)
    add "gui/quick_menu_zad.png"
    fixed yoffset 120 xoffset 270 at Fl_menu_move(0.9, 0.5, 0):
            add "gui/main_menu/save/save_background.png"

    fixed align (0.5, 0.5) anchor (0.5, 0.5) at Fl_menu_move(0.7, 0.5, 0):
        text ["{font=[Fl_Script]}Настройки{/font}"]:
            size 70
            text_align 0.5
            xalign 0.5
            yalign 0.08
            antialias True
            kerning 2
            
        textbutton "<":
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            style "Fl_button_None"
            text_style "Fl_text_setting_s"
            text_size 60
            xalign 0.36
            yalign 0.08
            action [Hide("preferences", Dissolve(0.5)), ShowMenu("Fl_save")]
        textbutton ">":
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            style "Fl_button_None"
            text_style "Fl_text_setting_s"
            text_size 60
            xalign 0.64
            yalign 0.08
            action [Hide("preferences", Dissolve(0.5)), ShowMenu("load")]

        textbutton ["Назад"]:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_big_save_load"
            style "Fl_button_None"
            text_size 55
            xpos 290
            ypos 950
            action Hide("preferences", Dissolve(0.5))

    vbox:
        align (0.33, 0.5)
        spacing 25

        vbox xalign 0.5:
            text "Режим экрана" xalign 0.5:
                font Fl_Script size 40
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
            text "Фильтр мата" xalign 0.5:
                font Fl_Script size 40
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
                font Fl_Script size 40
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
                font Fl_Script size 40
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


    vbox:
        align (0.69, 0.53)
        spacing 25

        vbox xalign 0.5:
            text "Текст" xalign 0.5:
                font Fl_Script size 40
                antialias True
                outlines [(1, "#000000", 0, 0)]
            bar:
                value Preference("text speed")
                right_bar "gui/main_menu/preferences/Fl_scale_chist.png"
                left_bar "gui/main_menu/preferences/Fl_scale_poln.png"
                thumb "gui/main_menu/preferences/Fl_begunok.png"
                xmaximum 365
                ymaximum 60

        vbox xalign 0.5:
            text "Музыка" xalign 0.5:
                font Fl_Script size 40
                antialias True
                outlines [(1, "#000000", 0, 0)] 
            bar:
                value Preference("music volume")
                right_bar "gui/main_menu/preferences/Fl_scale_chist.png"
                left_bar "gui/main_menu/preferences/Fl_scale_poln.png"
                thumb "gui/main_menu/preferences/Fl_begunok.png"
                xmaximum 365
                ymaximum 60

        vbox xalign 0.5:
            text "Звуки" xalign 0.5:
                font Fl_Script size 40
                antialias True
                outlines [(1, "#000000", 0, 0)]
            bar:
                value Preference("sound volume")
                right_bar "gui/main_menu/preferences/Fl_scale_chist.png"
                left_bar "gui/main_menu/preferences/Fl_scale_poln.png"
                thumb "gui/main_menu/preferences/Fl_begunok.png"
                xmaximum 365
                ymaximum 60

        vbox xalign 0.5:
            text "Эмбиент" xalign 0.5:
                font Fl_Script size 40
                antialias True
                outlines [(1, "#000000", 0, 0)]
            bar:
                value Preference("voice volume")
                right_bar "gui/main_menu/preferences/Fl_scale_chist.png"
                left_bar "gui/main_menu/preferences/Fl_scale_poln.png"
                thumb "gui/main_menu/preferences/Fl_begunok.png"
                xmaximum 365
                ymaximum 60




#История
define config.history_length = 70
define gui.history_height = 610
define gui.history_name_xpos = 0
define gui.history_name_ypos = 0
define gui.history_name_width = 0
define gui.history_name_xalign = 0.0
define gui.history_text_xpos = 250
define gui.history_text_ypos = 0
define gui.history_text_width = 1500
define gui.history_text_xalign = 0.0
define gui.scrollbar_size = 18

screen history():
    modal True
    predict False
    add "Fl_prolog_dream" at Fl_alpha(0.15)
    add "gui/quick_menu_zad.png"
    fixed yoffset 120 xoffset 270 at Fl_menu_move(0.9, 0.5, 0):
            add "gui/main_menu/save/save_background.png"
    
    $ xmax = 1250
    $ xposition = 95


    text "{font=[Fl_Script]}История:{/font}" size 70 at Fl_menu_move(0.7, 0.2, 0)

    window top_padding 33 bottom_padding 40 at Fl_menu_move:
        xfill True
        ysize gui.history_height

        fixed align (0.5, 0.5) anchor (0.5, 0.5) at Fl_menu_move(0.93, 0.5, 0):
            viewport id "text_history_screen":
                draggable True
                mousewheel True
                scrollbars None
                yinitial 1.0
                has vbox
                for history in _history_list:
                    if history.who:
                        text history.who:
                            font "font/Fl_mainmenu.ttf"
                            pos (450, 0)
                            size 27
                            if "color" in history.who_args:
                                color history.who_args["color"]
                    textbutton history.what:
                        style "log_button"
                        text_font "font/Fl_font.ttf"
                        text_size 25
                        xmaximum 1070
                        pos (450, 0)
                        
            vbar:
                value YScrollValue("text_history_screen")
                bottom_bar Frame("gui/main_menu/history/vbar_nofull.png",0,0)
                top_bar Frame("gui/main_menu/history/vbar_full.png",0,0)
                thumb "gui/main_menu/history/thumb.png"
                thumb_offset 10
                ymaximum 800
                align (0.795, 0.49)

    fixed align (0.5, 0.5) anchor (0.5, 0.5) at Fl_menu_move(1.0, 0.5, 0):
        textbutton ["Назад"]:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_setting" style "Fl_button_None"
            pos (485, 835) action Hide("history", Dissolve(0.5))
