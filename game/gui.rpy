﻿# -*- coding: ひきこもり -*-
init offset = -2

init python:
    gui.init(1920, 1080)


################################################################################

#Конфигурируемые Переменные GUI



#Цвета

#Цвета текста в интерфейсе.

#Акцентный цвет используется в заголовках и подчёркнутых текстах.
define gui.accent_color = u'#ffffff'

#Цвет, используемый в текстовой кнопке, когда она не выбрана и не наведена.
define gui.idle_color = u'#888888'

define gui.idle_small_color = u'#aaaaaa'

#Цвет, используемых в кнопках и панелях, когда они наведены.
define gui.hover_color = u'#ffffff'

#Цвет, используемый текстовой кнопкой, когда она выбрана, но не наведена.
define gui.selected_color = u'#ffffff'

#Цвет, используемый текстовой кнопкой, когда она не может быть выбрана.
define gui.insensitive_color = u'#8888887f'

#Цвета, используемые для частей панелей, которые не заполняются.
define gui.muted_color = u'#5a5a5a'
define gui.hover_muted_color = u'#6b6b6b'

## Цвета, используемые в тексте диалогов и выборов.
define gui.text_color = u'#ffffff'
define gui.interface_text_color = u'#ffffff'


#Шрифты и их размеры


#Шрифт, используемый внутриигровым текстом.
define gui.text_font = "font/Fl_font.ttf"

#Шрифт, используемый именами персонажей.
define gui.name_text_font = "font/Fl_font.ttf"

#Шрифт, используемый текстом вне игры.
define gui.interface_text_font = "font/Fl_mainmenu.ttf"

#Размер нормального текста диалога.
define gui.text_size = 32

#Размер имён персонажей.
define gui.name_text_size = 38

#Размер текста в пользовательском интерфейсе.
define gui.interface_text_size = 32

#Размер заголовков в пользовательском интерфейсе.
define gui.label_text_size = 35

#Размер текста на экране уведомлений.
define gui.notify_text_size = 24

#Размер заголовка игры.
define gui.title_text_size = 65


#Диалог(Эти переменные контролируют, как диалог появляется на отдельной строчке)

#Высота текстового окна, содержащего диалог.
define gui.textbox_height = 275

#Местоположение текстового окна по вертикали экрана(0.0 — верх, 0.5 — центр, 1.0 — низ)
define gui.textbox_yalign = 1.0


#Местоположение имени говорящего персонажа по отношению к текстовому окну.
define gui.name_xpos = 350
define gui.name_ypos = 0

## Горизонтальное выравнивание имени персонажа(0.0 для левоориентированного, 0.5 для центрированного и 1.0 для правоориентированного)
define gui.name_xalign = 0.0

#Ширина, высота и границы окна
define gui.namebox_width = None
define gui.namebox_height = None

#Границы окна
define gui.namebox_borders = Borders(5, 5, 5, 5)

define gui.namebox_tile = False


#Размещение диалога по отношению к текстовому окну.
define gui.dialogue_xpos = 315
define gui.dialogue_ypos = 55

#Максимальная ширина текста диалога в пикселях.
define gui.dialogue_width = 1290

#Горизонтальное выравнивание текста диалога(0.0 для левоориентированного, 0.5 для центрированного и 1.0 для правоориентированного)
define gui.dialogue_text_xalign = 0.0


#Кнопки


#Ширина и высота кнопки в пикселях
define gui.button_width = None
define gui.button_height = None

#Границы каждой стороны кнопки в порядке слева, сверху, справа, снизу.
define gui.button_borders = Borders(6, 6, 6, 6)

define gui.button_tile = False

#Шрифт, используемый кнопкой.
define gui.button_text_font = gui.interface_text_font

#Размер текста, используемый кнопкой.
define gui.button_text_size = gui.interface_text_size

#Цвет текста в кнопке в различных состояниях.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

#Горизонтальное выравнивание текста в кнопке(0.0 — лево, 0.5 — по центру, 1.0 — право).
define gui.button_text_xalign = 0.0

#Настройки используются стандартным интерфейсом:

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

# define gui.navigation_button_width = 250


#Кнопки Выбора
#Кнопки выбора используются во внутриигровых меню.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = "#444444"


#Кнопки Слотов

#Кнопка слота сохранения.
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

#Ширина и высота миниатюры, используемой слотом сохранения.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

#Количество колонок и рядов в таблице слотов.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


#Позиционирование и Интервалы

define gui.navigation_xpos = 60

#Вертикальная позиция индикатора пропуска.
define gui.skip_ypos = 15

#Вертикальная позиция экрана уведомлений.
define gui.notify_ypos = 68

#Интервал между выборами в меню.
define gui.choice_spacing = 33

#Кнопки в секции навигации главного и игрового меню.
define gui.navigation_spacing = 6

#Контролирует интервал между настройками.
define gui.pref_spacing = 15

#Контролирует интервал между кнопками настройки.
define gui.pref_button_spacing = 0

#Интервал между кнопками страниц.
define gui.page_spacing = 0

#Интервал между слотами.
define gui.slot_spacing = 15

#Позиция текста главного меню.
define gui.main_menu_text_xalign = 1.0


#Рамки

#Генерация рамки.
define gui.frame_borders = Borders(6, 6, 6, 6)

#Рамки, используемые в частях экрана подтверждения.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

#Рамки, используемые в частях экрана пропуска.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

#Рамки, используемые в частях экрана уведомлений.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

define gui.frame_tile = False


#Панели, Полосы прокрутки и Ползунки

#Высота горизонтальных панелей, полос прокрутки и ползунков. Ширина вертикальных панелей, полос прокрутки и ползунков.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

#Горизонтальные границы.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

#Вертикальные границы.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

#Что делать с непрокручиваемыми полосами прокрутки в интерфейсе. "hide" прячет их, а None их показывает.
define gui.unscrollable = "hide"


#История

## Количество диалоговых блоков истории, для хранения.
define config.history_length = 250

#Высота доступных записей на экране истории
define gui.history_height = 210

#Местоположение, ширина и выравнивание заголовка, имя персонажа.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

#Местоположение, ширина и выравнивание диалогового текста.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


#Режим NVL

#Границы фона окна NVL.
define gui.nvl_borders = Borders(0, 15, 0, 30)

#Максимальное число показываемых строк в режиме NVL.
define gui.nvl_list_length = 6

#Высота доступных строчек в режиме NVL.
define gui.nvl_height = 173

#Интервал между строчками в режиме NVL
define gui.nvl_spacing = 15

#Местоположение, ширина и выравнивание заголовка, имя персонажа.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

#Местоположение, ширина и выравнивание диалогового текста.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

#Местоположение, ширина и выравнивание текста nvl_thought
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

#Местоположение кнопок меню NVL.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0

#Локализация
define gui.language = "unicode"


################################################################################
## Мобильные устройства
################################################################################

init python:

    ## Этот параметр увеличивает размер быстрых кнопок, чтобы сделать их
    ## доступнее для нажатия на планшетах и телефонах.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## Это изменяет размеры и интервалы различных элементов GUI, чтобы
    ## убедиться, что они будут лучше видны на телефонах.
    @gui.variant
    def small():

        ## Размеры шрифтов.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## Регулирует местоположение текстового окна.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Изменяет размеры и интервалы различных объектов.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## Местоположение кнопок слотов.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## Режим NVL.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
