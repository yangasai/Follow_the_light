﻿# -*- coding: ひきこもり -*-
init offset = -1


#Стили
style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################

#Внутриигровые экраны

#Экран разговора



## Делает namebox доступным для стилизации через объект Character.



#Экран ввода
screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

#Экран автоСейва
screen Fl_autosave:
    layer "front"
    fixed at Fl_show_hide_alpha(1.0):
        text "Автосохранение" pos (0.722, 0.78) size 32:
            style "Fl_text_label"
            at Fl_alpha_ease_repeat(0.4, 1.0, 1.0)
    timer 3.5 action Hide("Fl_autosave")




screen Fl_disco_qte(index, sec, lose):
    add QTE_image_list[index] xalign 0.5 yalign 0.5
    for qte in QTE_list[index]:
        key qte action [Hide("Fl_disco_qte"), Return()]
    timer sec action Jump(lose)

screen Fl_lent_qte(index, sec, lose):
    add QTE_image_list_l[index] xalign 0.5 yalign 0.5
    for qte in QTE_list_l[index]:
        key qte action [Hide("Fl_lent_qte"), Return()]
    timer sec action Jump(lose)


screen Fl_podsk_save:
    layer "front"
    fixed at Fl_show_hide_alpha(1.0):
        add "Fl_podsk_1" at Fl_alpha_ease_repeat(0.4, 1.0, 1.0)
    timer 3.0 action Hide("Fl_podsk_save")


screen Fl_podsk_dict:
    layer "front"
    fixed at Fl_show_hide_alpha(1.0):
        add "Fl_podsk_2" at Fl_alpha_ease_repeat(0.4, 1.0, 1.0)
    timer 3.0 action Hide("Fl_podsk_dict")


screen Fl_new_item(name, message):
    layer "front"
    fixed at Fl_new_item_move:
        add "gui/overlay/Fl_new_item_frame.png" pos (-0.012, -0.01)
        add "gui/inventory/slots/" + name + "_idle.png"
        text message style "Fl_text_label" size 20 pos (0.05, 0.005) xanchor 0.0
        text Fl_items_dict[name] style "Fl_text_label" size 30 pos (0.05, 0.025) xanchor 0.0
    timer 5.0 action Hide("Fl_new_item")


################################################################################



#Экраны Главного и Игрового меню
screen navigation():
    
    

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Начать") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (Hide ("main_menu"), Start("Fl_start"))

        else:

            textbutton _("История") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (Hide ("main_menu"), ShowMenu("history")) at Fl_menu_hover

            textbutton _("Словарь") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (Hide ("main_menu"), ShowMenu("dictionary")) at Fl_menu_hover


            textbutton _("Сохранить") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (Hide ("main_menu"), ShowMenu("Fl_save")) at Fl_menu_hover

        textbutton _("Загрузить") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (Hide ("main_menu"), ShowMenu("load")) at Fl_menu_hover

        #textbutton _("Инвентарь") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (Hide ("main_menu"), SetVariable("Fl_hover_slot", {"slot":None, "name":"empty", "stats":None}), ShowMenu("Fl_inventory")) at Fl_menu_hover

        textbutton _("Настройки") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (Hide ("main_menu"), ShowMenu("preferences")) at Fl_menu_hover

        if _in_replay:

            textbutton _("Завершить повтор") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (Hide ("main_menu"), EndReplay(confirm=True)) at Fl_menu_hover

        elif not main_menu:

            textbutton _("Главное меню") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (Hide ("main_menu"), ShowMenu("Fl_quit_menu")) at Fl_menu_hover


        if renpy.variant("pc"):

            textbutton _("Выход") hover_sound "gui/main_menu/Fl_click_menu.mp3" action (Hide ("main_menu"), Quit(confirm=not main_menu)) at Fl_menu_hover


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


#Экран главного меню


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")




style return_button is navigation_button
style return_button_text is navigation_button_text



style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45







style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")



style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675




#Экран о новелле/обнове
screen about_bg:
    modal True

    add "gui/choice.png" at Fl_alpha(0.8)
    fixed yoffset 170 xoffset 635 at Fl_menu_move(0.91, 0.5, 0):
            add "gui/main_menu/save/save_background.png"

    frame at Fl_from_about(-1500, 0.5):
        align (0.72, 0.29)

        hbox:
            spacing 10
            add "images/preview/logo.png" at Fl_zoom_pr(0.32)
            
            vbox:
                spacing 2

                text "Coding:" xalign 0.0 size 50 font Fl_Script
                text "ひきこもり" xalign 0.0 size 50

    frame at Fl_from_about(-1500, 0.5):
        align (0.925, 0.59)

        vbox:
            spacing 4

            text "Погрузитесь в мир снов, где реальность и фантазия переплетаются в захватывающем тан-" xalign 0.0 size 24
            text "це. Иногда сон — это не просто отдых. Это врата в неизведанное, где каждое мгновение" xalign 0.0 size 24
            text "может стать началом новой истории. Но будьте осторожны! В этом загадочном месте реаль-" xalign 0.0 size 24
            text "ность принимает неожиданные формы, и то, что кажется знакомым, может обернуться самым" xalign 0.0 size 24
            text "страшным кошмаром. Что, если ваши самые глубокие страхи и желания начнут преследовать" xalign 0.0 size 24
            text "вас? Каждый шаг по протоптанной дорожке может привести к неожиданным поворотам, зас-" xalign 0.0 size 24
            text "таляя вас вновь и вновь сталкиваться с тем, что вы пытались забыть." xalign 0.0 size 24
            text "Каждый сон — это новая возможность, а каждый кошмар — шанс на искупление." xalign 0.0 size 24


    frame at Fl_from_about(-1500, 0.5):
        align (0.96, 0.838)

        text "Version 0.3.4" size 34 font Fl_Script

    frame at Fl_from_about(-1500, 0.5):
        align (0.47, 0.84)

        textbutton ["Назад"] at Fl_menu_hover:
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            text_style "Fl_text_big_save_load"
            style "Fl_button_None"
            text_size 35
            action [Hide("about_bg", Dissolve(0.25))]



screen update_bg:
    tag menu

    add "update_layer"
    textbutton ["Назад"]:
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        text_style "Fl_text_big_save_load"
        style "Fl_button_None"
        text_size 50
        xpos 100
        ypos 1010
        action [Hide("update_bg", Dissolve(1.0)), Jump("before_main_menu")]


screen choice:
    tag menu
    modal True
    window at Fl_choice_anim:
        background Frame("gui/choice_box.png", 50, 50)
        padding (75, 50, 75, 50)
        yalign 0.5
        xfill True
        has vbox xalign 0.5
        for caption, action, chosen in items:
            if action and caption:
                button:
                    hover_sound "gui/main_menu/Fl_click_menu.mp3"
                    background None
                    xalign 0.5
                    action action
                    text caption:
                        font "font/Fl_mainmenu.ttf"
                        size 42
                        hover_size 42
                        color "#808080"
                        hover_color "#FFFFFF"
                        xcenter 0.5
                        text_align 0.5
            else:
                text caption:
                    font "font/Fl_mainmenu.ttf"
                    size 55
                    color "#808080"
                    text_align 0.5
                    xcenter 0.5
        xcenter 0.5
        ycenter 0.5




## Экран подтверждения #########################################################
##
## Экран подтверждения вызывается, когда Ren'Py хочет спросить у игрока вопрос
## Да или Нет.


screen confirm(message, yes_action, no_action):

    ## Гарантирует, что другие экраны будут недоступны, пока показан этот экран.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/choice.png" at Fl_at_dissolve(0.65, 0.5)

    frame at Fl_at_dissolve(0.65, 0.5):

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                text_style "Fl_text_big_save_load"
                text_size 43
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Да"):
                    text_size 50
                    action yes_action
                textbutton _("Нет"):
                    text_size 50
                    action no_action



style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame(["gui/main_menu/none.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


#Экран индикатора пропуска
screen skip_indicator():

    zorder 100
    style_prefix "skip"

    add "Fl_prolog_dream" at Fl_alpha(0.15)
    add "gui/quick_menu_zad.png"

    hbox:
        align(0.5, 0.5)
        spacing 9

        text "▸" at delayed_blink(0.0, 1.0) size 110 style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) size 110 style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) size 110 style "skip_triangle"


## Эта трансформация используется, чтобы мигать стрелками одна за другой.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Нам надо использовать шрифт, имеющий в себе символ U+25B8 (стрелку выше).
    font "DejaVuSans.ttf"


#Экран уведомлений 
screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


#Экран NVL 
screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Показывает диалог или в vpgrid, или в vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Показывает меню, если есть. Меню может показываться некорректно, если
        ## config.narrator_menu установлено на True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Это контролирует максимальное число строк NVL, могущих показываться за раз.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")




#Подсказки очков рутов
screen view_score_screen():
    textbutton ["{font=[Fl_Script]}Прогресс{/font}"]:
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        pos (1113, 886) 
        style "Fl_button_None"
        text_size 16
        xanchor 0.0 
        text_style "Fl_text_big_save_load"
        action ShowMenu('score_screen')


screen score_screen():
    tag menu
    modal True
    add "Fl_prolog_dream"
    add "gui/quick_menu_zad.png"
    add "gui/podsk/Fl_zad.png":
        yalign 0.5 
        xalign 0.5
    text ["{font=[Fl_Script]}Прогресс{/font}"]:
        size 63
        yalign 0.5 
        xalign 0.5

    add "gui/podsk/Fl_prog1.png" at Fl_leftside_podsk
    add "gui/podsk/Fl_prog2.png" at Fl_leftside_podsk
    add "gui/podsk/Fl_prog3.png" at Fl_leftside_podsk
    add "gui/podsk/Fl_prog4.png" at Fl_leftside_podsk
    add "gui/podsk/Fl_prog5.png" at Fl_leftside_podsk

    add "gui/podsk/Fl_prog1_1.png" at Fl_rightside_podsk
    add "gui/podsk/Fl_prog2_2.png" at Fl_rightside_podsk
    add "gui/podsk/Fl_prog3_3.png" at Fl_rightside_podsk
    add "gui/podsk/Fl_prog4_4.png" at Fl_rightside_podsk
    add "gui/podsk/Fl_prog5_5.png" at Fl_rightside_podsk
    #Лена
    text "{font=[Fl_Script]}Искажение-[add_ln]\nПривязанность-[lp_un]\n{/font}":
        size 20
        yalign 0.13 
        xalign 0.01
        at Fl_leftside_podsk
    #Мику
    text "{font=[Fl_Script]}Истинна-[Ist_mi]\nОдержимость-[Obs_mi]\nОбычные-[add_mi]\n{/font}":
        size 20
        yalign 0.32 
        xalign 0.01
        at Fl_leftside_podsk
    #Виола
    text "{font=[Fl_Script]}Отношения-[lp_cs]{/font}":
        size 20
        yalign 0.53 
        xalign 0.01
        at Fl_leftside_podsk
    #Катя
    text "{font=[Fl_Script]}Эрос-[Eros_kt]\nДофенизм-[Dfm_kt]\n{/font}":
        size 20
        yalign 0.75 
        xalign 0.01
        at Fl_leftside_podsk
    #Аня
    text "{font=[Fl_Script]}Эрос-[Eros_an]\nДофенизм-[Dfm_an]\n{/font}":
        size 20
        yalign 0.96
        xalign 0.01
        at Fl_leftside_podsk

    #Маша
    text "{font=[Fl_Script]}Эрос-[Eros_ma]\nДофенизм-[Dfm_ma]\n{/font}":
        size 20
        yalign 0.13
        xalign 0.99
        at Fl_rightside_podsk
    #Алиса
    text "{font=[Fl_Script]}Эрос-[Eros_al]\nДофенизм-[Dfm_al]\n{/font}":
        size 20
        yalign 0.33
        xalign 0.99
        at Fl_rightside_podsk
    #Роза
    text "{font=[Fl_Script]}Эрос-[Eros_rz]\nДофенизм-[Dfm_rz]\n{/font}":
        size 20
        yalign 0.54
        xalign 0.99
        at Fl_rightside_podsk
    #Одиночка
    text "{font=[Fl_Script]}Социофобия-[Sph_ln]\nСоциапатия-[Sp_ln]\nБезумие-[lp_ln]\nАбсолют-[Ist_ln]\n{/font}":
        size 20
        yalign 0.74
        xalign 0.99
        at Fl_rightside_podsk
    #Мира
    text "{font=[Fl_Script]}Истинна-[Ist_mir]\nОтношения-[Good_mir]\nДружба-[Bad_mir]\n{/font}":
        size 20
        yalign 0.96
        xalign 0.99
        at Fl_rightside_podsk




#Словарь
screen dictionary():
    tag menu
    modal True


    add "Fl_dictionary"
    add "Fl_dust_full"
    text "Словарь":
        font "font/Fl_mainmenu.ttf"
        size 55
        xpos 855
        ypos 40

    textbutton ["Назад"]:
        hover_sound "gui/main_menu/Fl_click_menu.mp3"
        text_style "Fl_text_big_save_load"
        style "Fl_button_None"
        text_size 40
        xpos 40
        ypos 1000
        action Hide("dictionary", Dissolve(0.5)), Return()

    #слова
    viewport:
        draggable True
        mousewheel True
        xpos 486 
        ypos 160
        xsize 1100
        ysize 800
        
        vbox:

            spacing 20
            if persistent.Fl_dictionary_1 == True:
                text "{b}{i}Ноздрёв{/i}{/b} - болтливый персонаж из поэмы «Мёртвые души».":
                    size 38
            else:
                text"{color=#808080}???{/color}":
                    size 38


            if persistent.Fl_dictionary_2 == True:
                text "{b}{i}Дофамин{/i}{/b} - Гормон счастья.":
                    size 38
            else:
                text"{color=#808080}???{/color}":
                    size 38
            

            if persistent.Fl_dictionary_3 == True:
                text "{b}{i}Алекситимия{/i}{/b} - неспособность выражать эмоции.":
                    size 38
            else:
                text"{color=#808080}???{/color}":
                    size 38
            

            if persistent.Fl_dictionary_4 == True:
                text "{b}{i}ПорноФильмы{/i}{/b} - рок-группа, основанная в 2008г.":
                    size 38
            else:
                text"{color=#808080}???{/color}":
                    size 38
                

            if persistent.Fl_dictionary_5 == True:
                text "{b}{i}Одзиги{/i}{/b} - низкий японский поклон.":
                    size 38
            else:
                text"{color=#808080}???{/color}":
                    size 38
            

            if persistent.Fl_dictionary_6 == True:
                text "{b}{i}Hentai{/i}{/b} - Яп. - Извращенец/Пошлый.":
                    size 38
            else:
                text"{color=#808080}???{/color}":
                    size 38
                

            if persistent.Fl_dictionary_7 == True:
                text "{b}{i}Дереализация{/i}{/b} - нарушение восприятия окружающего мира.":
                    size 38
            else:
                text"{color=#808080}???{/color}":
                    size 38
            

            if persistent.Fl_dictionary_8 == True:
                text "{b}{i}Adieu!{/i}{/b} - Фр. - прощай.":
                    size 38
            else:
                text"{color=#808080}???{/color}":
                    size 38
                

            if persistent.Fl_dictionary_9 == True:
                text "{b}{i}Анабиоз{/i}{/b} - состояние организма, при котором жизненные процессы (дыхание, сердцебиение) временно прекращаются.":
                    size 38
            else:
                text"{color=#808080}???{/color}":
                    size 38
            

            if persistent.Fl_dictionary_10 == True:
                text "{b}{i}Амбидекстр{/i}{/b} - человек, который одинаково владеет обеими руками.":
                    size 38
            else:
                text"{color=#808080}???{/color}":
                    size 38
                

            if persistent.Fl_dictionary_11 == True:
                text "{b}{i}Псионика{/i}{/b} - способность человека, а именно его разума, влиять на окружающий мир силой мысли, игнорируя законы физики. Как правило, псионикой обладают избранные люди.":
                    size 38
            else:
                text"{color=#808080}???{/color}":
                    size 38
                

            if persistent.Fl_dictionary_12 == True:
                text "{b}{i}Повеяло юностью{/i}{/b} - Англ. перевод названия песни Nirvana - «Smells Like Teen Spirit».":
                    size 38
            else:
                text"{color=#808080}???{/color}":
                    size 38
                

            if persistent.Fl_dictionary_13 == True:
                text "{b}{i}Гипоксия{/i}{/b} - пониженное содержание кислорода в организме или отдельных органах и тканях.":
                    size 38
            else:
                text"{color=#808080}???{/color}":
                    size 38
                

            if persistent.Fl_dictionary_14 == True:
                text "{b}{i}Петрикор{/i}{/b} - характерный запах, остающийся в воздухе после дождя.":
                    size 38
            else:
                text"{color=#808080}???{/color}":
                    size 38
                

            if persistent.Fl_dictionary_15 == True:
                text "{b}{i}Эксгибициониистка{/i}{/b} - Женщина со склонностью к публичному обнажению интимных частей своего тела с целью самовозбуждения.":
                    size 38
            else:
                text"{color=#808080}???{/color}":
                    size 38
                
            
            if persistent.Fl_dictionary_16 == True:
                text "{b}{i}Itadakimasu!{/i}{/b} - Яп. - Приятного аппетита.":
                    size 38
            else:
                text"{color=#808080}???{/color}":
                    size 38
                

            if persistent.Fl_dictionary_17 == True:
                text "{b}{i}Гетерохромия{/i}{/b} - Различный цвет радужной оболочки правого и левого глаза.":
                    size 38
            else:
                text"{color=#808080}???{/color}":
                    size 38












