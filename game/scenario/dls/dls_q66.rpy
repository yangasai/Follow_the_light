# -*- coding: ひきこもり -*-


label dls_q66:
    scene bg Fl_black with Fl_dissolve2
    $ Fl.StopSound(2)
    $ Fl.StopAmbience(2)
    $ Fl.StopMusic(2)
    $ serial = Fl.serial()
    $ Fl.Pause (4.5)

    $ Fl.PlayMusic("Fl_hron", 1, 4)
    scene Fl_dls_q66_1 with Fl_effect_right2
    $ Fl.Pause (2.0)

    scene bg Fl_black with Fl_dissolve2
    $ Fl.Pause (1.5)

    scene Fl_dls_q66_2 with Fl_effect_right2
    $ Fl.Pause (1.0)

    $ Fl.PlaySound("Fl_glith", 1, 0, False)
    show Fl_r_effect

    $ Fl.Pause (1.5)
    scene bg Fl_black
    show text "{font=font/Fl_mainmenu.ttf}{size=55}Эй, {color=#f00}[Fl_user]{/color}, хочешь я сам расскажу тебе свою историю?{/size}{/font}"
    with Fl_dissolve1

    $ Fl.Pause (3.0)
    show text "{font=font/Fl_mainmenu.ttf}{size=55}Ведь первоисточник куда лучше, второсортного сценариста.{/size}{/font}"
    with Fl_dissolve1
    $ Fl.Pause (3.5)

    show text "{font=font/Fl_mainmenu.ttf}{size=55}Ну, так что скажешь, {color=#f00}[Fl_user]{/color}?{/size}{/font}"
    with Fl_dissolve1
    $ Fl.Pause (2.0)

    call screen vibor_storu with Fl_dissolve1
    screen vibor_storu:
        tag menu
        modal True

        timer 1.5 action MouseMove(x=490, y=650, duration=0.8)
        
        textbutton "Да":
            style "Fl_button_None"
            text_style "Fl_text_big_save_load"
            text_size 55
            xpos 480 
            ypos 640
            action Hide("vibor_storu"), Jump("q66_yes")

        textbutton "Нет":
            style "Fl_button_None"
            text_style "Fl_text_big_save_load"
            text_size 55
            xpos 1380 
            ypos 640
            action Hide("vibor_storu"), Jump("q66_no")



label q66_yes:
    show text "{font=font/Fl_mainmenu.ttf}{size=55}Тогда присаживайся поудобнее. Я начинаю...{/size}{/font}"
    with Fl_dissolve1
    $ Fl.Pause (2.5)
    scene bg Fl_black with Fl_dissolve2
    $ Fl.StopMusic(4)
    jump dls_q66_prolog


label q66_no:
    show text "{font=font/Fl_mainmenu.ttf}{size=55}Какая досада.{/size}{/font}"
    with Fl_dissolve1
    $ Fl.Pause (1.5)
    show text "{font=font/Fl_mainmenu.ttf}{size=55}Прощай, {color=#f00}[Fl_user]{/color}{/size}{/font}"
    with Fl_dissolve1
    $ Fl.Pause (1.0)
    jump Pc_off






label dls_q66_prolog:


    $ Fl.Pause (5.5)
    scene Fl_q_66_1 with Fl_dissolve2
    show Fl_q_66_layer with Fl_effect_down1
    show Fl_q_66_text1 with Fl_dissolve1
    $ Fl.Pause (4.5)

    scene bg Fl_black with Fl_dissolve2




    $ Fl.Save("Dls Одиночка:Пролог")
    $ Fl.DayTime("night", "night")

    $ Fl.Pause (6.5)
    $ Fl.PlayAmbience("Fl_bus_interior_moving", 0.2, 4)
    scene bg Fl_int_bus_people_night with Fl_dissolve3

    $ Fl.Pause (1.0)
    $ Fl.PlayMusic("Fl_snowfall", 1, 7)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.Status("80")
    $ Fl.Status("normal", False)
    $ Fl.say(Fl_r, "Кристина тихонько сопела на моём плече. {w}Уснула.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_th, "Так или иначе, я не могу сказать что мне здесь не понравилось. {w}Конечно не могу чёрт возьми!")
    $ Fl.say(Fl_th, "Это были лучшие пять дней в моей жизни. {w}По крайне мере, если рассматривать последний год моего существования до перерождения...")
    $ Fl.say(Fl_th, "Почему спросите вы? {w}Да потому что я познакомился с хорошими людьми, {w}нашёл свою любовь, почувствовал давно забытые эмоции.")
    $ Fl.say(Fl_th, "Чего только стоит это спящее чудо рядом со мной?{w} Кристина - это самое лучшее что есть сейчас в моей жизни. {w}Она очень сильно изменила меня за эти дни, и я ей благодарен за это.")
    $ Fl.say(Fl_th, "Именно она залечила все раны, моего никчёмного прошлого. Только с ней я наконец-то смог засиять, как раньше.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause (2.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Впереди сидят два пионера, которые ведут бессмысленную беседу и смеются.")
    $ Fl.HideScreens(_with=Fl_fast)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.ShowScreens(_with=Fl_fast)
    show art smile pioneer1:
        right
    show ss smile pioneer1:
        left
    with Fl_dissolve1

    $ Fl.say(Fl_th, "Саня и Тёмыч. {w}Помню, как первый раз встретился с этими двумя индивидами в их обиталище(клубах), когда заполнял обходной.")
    $ Fl.say(Fl_th, "Парни мне по началу показались ненадёжными и обычными быдлонами. И я даже представить не мог, что в итоге мы так сдружимся. А всё из-за одного инцидента... Хотелось бы конечно вновь воспроизвести его из памяти, но не буду зацикливаться на парнях.")

    hide art smile pioneer1
    hide ss smile pioner1
    with Fl_dissolve1

    $ Fl.say(Fl_th, "Ведь по-мимо их, есть ещё один интерсеный дуэль.")

    show an smile pioner1:
        right
    show al smile pioner1:
        left
    with Fl_dissolve1

    $ Fl.say(Fl_th, "Аня и Алиса. Первая конечно знатно мне вставила палки в колёса, когда я только очутился в этом мире, но всё же хорошая подруга, как и Алиса.")
    $ Fl.say(Fl_th, "Про девочку-цундерку, думаю ничего не стоит говорить. Типичная стесняша, которая прячется за маской агрессии. А вот Аня, ещё та садистка! Любит она поиздеваться над кем-то, играть на нервах наверное это её главное хобби.")
    $ Fl.ShowScreens(_with=Fl_dissolve1)


    hide an smile pioner1
    hide al smile pioneer1
    with Fl_dissolve1
    $ Fl.Pause (2.0)


    scene bg Fl_int_bus_people_night with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "В моём отряде были ещё и другие пионеры, но про них я мало что могу сказать. Разве что, я был рад провести эту смену с ними.")
    $ Fl.say(Fl_th, "И всё же я счастлив, что всё сложилось именно так.{w} Никак иначе мне и не нужно.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "«У каждой истории есть начало и конец». - Эта цитата подходит идеально, чтобы описать мою небольшую историю попаданца.")
    $ Fl.say(Fl_th, "Что уж говорить, можно долго думать об этом лагере,{w} и о том что было,{w} но что же будет дальше?")
    $ Fl.say(Fl_th, "Существует ли жизнь за пределами этого пионерлагеря?")
    $ Fl.say(Fl_th, "А если да, то как я выживу в этом мире без паспорта, меня ведь по факту здесь вообще несуществует. Для этого мира я обычный фантом...")
    $ Fl.say(Fl_r, "Небольшая прядь волос Кристины упала ей на лицо. {w}Я аккуратно поправил их, чтобы ненароком не разбудить девушку.")
    
    $ Fl.Pause (1.5)
    $ Fl.say(Fl_th, "А ведь она тоже фантом в этом мире. Такой же попаданец, как и я...")
    $ Fl.say(Fl_r, "Пионерка улыбнулась сквозь сон. {w}Я легонько приобнял её и сделал заключение.")
    $ Fl.say(Fl_th, "Плевать, что будет потом. Чтобы не случилось, вместе мы справимся с любыми трудностями!")
    
    $ Fl.Pause (1.0)
    $ Fl.ShowBlink()
    $ Fl.say(Fl_r, "Глаза начали закрываться сами собой, словно кто-то мне их закрывает.")
    $ Fl.say(Fl_r, "Я не мог сопротивляться и в конце концов уснул.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause (2.0)
    scene bg Fl_black with Fl_dissolve1
    $ Fl.HideBlink()

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Сон, опять... {w}всегда ненавидел это состояние, {w}ничего не можешь в нём сделать, а после ничего не помнишь и не вспомнишь. Во сне мы просто наблюдатели. Пленики мира грёз, который порой может сильно ранить, исполняя твои заветные мечты и забирая их после пробуждения.")
    $ Fl.say(Fl_th, "Мир грёз - поистине очень жесток...")
    $ Fl.HideScreens(_with=Fl_fast)

    $ Fl.Pause (0.5)
    show kr_dream with Fl_dissolve2
    $ Fl.Pause (0.5)

    $ Fl.say(Fl_th, "Но даже во сне мне кажется что я вижу Кристину. {w}Ту самую Кристину, которая спасла меня. {w}Спасла от самого себя.")
    $ Fl.say(Fl_th, "Надеюсь, что у нас с Кристиной всё будет хорошо. {w}Больше мне ничего не нужно в жизни. {w}{b}Только Кристина.{/b}")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(5)
    $ Fl.StopAmbience(5)
    scene bg Fl_black with Fl_dissolve2
    $ Fl.ShowBlink()






    $ Fl.Pause (7.5)
    $ Fl.DayTime("day", "day")

    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 4)
    $ Fl.Pause(2.0)
    scene bg Fl_int_bus
    $ Fl.ShowUnblink()

    $ Fl.Pause(2.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Медленно открыв свои заспанные очи, перед глазами появился салон автобуса, который уже хорошо мне был знаком.")
    $ Fl.say(Fl_th, "Уже приехали?")
    $ Fl.say(Fl_r, "Я повернул голову в сторону окон, в надежде увидеть своих новых знакомых возле райцентра(куда мы собственно и ехали).")

    $ Fl.Pause(2.0)
    $ Fl.Status("-40")
    $ Fl.Status("normal", False)
    $ Fl.say(Fl_th, "КАКОГО?!", _with=hpunch)
    $ Fl.say(Fl_r, "Никакого райцентра не было и в помине. Вместо него на меня смотрели ворота и две статуи пионеров.")
    $ Fl.say(Fl_th, "Почему мы вернулись обратно?", _with=hpunch)
    $ Fl.say(Fl_r, "Я немного осмотрел автобус и понял одно:")

    $ Fl.Status("-10")
    $ Fl.Status("panic", False)
    $ Fl.say(Fl_th, "Кристина! Как я не заметил, что её нет со мной? {w}Так, не время думать о том насколько я слепой, сейчас о другом...")
    $ Fl.say(Fl_th, "Где она?!")
    $ Fl.HideBlink()
    $ Fl.HideUnblink
    $ Fl.HideScreens()


    scene bg Fl_int_bus at Fl_bg_zoom(1.0, 1.25, 1.5, 0.5, 0.0, 0.5, 0.7, 1.25, 2.0, 1.0, 0.7, 1.0, 2.0, 0.5, 0.5)
    $ Fl.Pause(6.0)
    $ Fl.say(Fl_r, "После того, как я осмотрел салон автобусв и никого так и не нашёл, я сел назад на своё место и предался размышлениям.")
    $ Fl.say(Fl_th, "Какого чёрта я снова в автобусе, а за окном опять «Совёнок»?")
    $ Fl.say(Fl_th, "Всё в точности, как после моего перерождения...")
    $ Fl.say(Fl_th, "Или нет?")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_gg, "Жарко...")
    with vpunch

    $ Fl.AttackScreens()
    $ Fl.Status("-10")
    $ Fl.say(Fl_gg, "КАКОГО?!")
    $ Fl.say(Fl_r, "На мне было моё старое пальто, в котором я выходил за продуктами перед реинкарнацией.")

    show Fl_vignette2 with Fl_dissolve1
    $ Fl.PlaySound("Fl_head_heartbeat", 1.0, 0, True)
    $ Fl.say(Fl_r, "От огромного количества мыслей мне стало плохо. {w}Захотелось мгновенно выйти из автобуса, как если бы неведомая сила выталкивала меня из него.")
    $ Fl.say(Fl_r, "Я скинул пальто на сиденье автобуса и стал выходить.")
    hide Fl_vignette2 with Fl_dissolve1
    $ Fl.StopSound(2)
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.HideUnblink()


    $ Fl.Pause(1.5)
    $ Fl.PlaySound("Fl_shagi", 1.0, 0, False)
    scene bg Fl_int_bus:
        subpixel True
        xalign 0.65 yalign 0.47
        linear 2.0 zoom 1.5 
    $ Fl.Pause(2.5)
    scene bg Fl_black with Fl_dissolve1

    $ Fl.Pause(1.5)
    
    scene bg Fl_ext_camp_entrance_day 
    show Fl_light_c
    with Fl_effect_2

    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.AutoSave()
    $ Fl.say(Fl_r, "Оставив салон автобуса позади я уставился на масивные ворота, за которыми скрывался далеко не обычный пионерлагерь.")
    $ Fl.say(Fl_th, "Неужели правда всё повторяется?")
    $ Fl.say(Fl_th, "На это вопрос может дать ответ только...")
    $ Fl.say(Fl_r, "Я прислонился к металическим вратам. {w}За ними раздались шаги, которые с каждым разом становились всё отчётливее. {w}Значит приближаются ко мне.")
    $ Fl.HideScreens(_with=Fl_fast)

    $ Fl.Pause(2.5)

    show to normal pioneer with Fl_dissolve2

    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Из-за ворот показался пухлый пионер с залысиной. На его лице был уже знакомый покерфейс.")

    $ Fl.Status("70")
    $ Fl.Status("normal", False)
    $ Fl.say(Fl_gg, "Толян, дружище! Как я рад тебя видеть!")
    $ Fl.say(Fl_gg, "Слушай, можешь объяснить зачем мы вернулись обратно в лагерь? Смена ведь закончилась.")
    if persistent.Fl_dictionary_7 == False:
        $ Fl.PodskDict()
    $ persistent.Fl_dictionary_7 = True
    $ Fl.say(Fl_th, "Никогда бы не поверил, что буду рад видеть Толяна. Но сейчас он для меня хоть какая-то надежда избавиться от {i}дереализации{/i}.")
    $ Fl.say(Fl_to, "Мы никуда не уезжали. Зачем нам уезжать, только половина смены прошла.")
    $ Fl.say(Fl_to, "И откуда ты знаешь, как меня зовут?")

    $ Fl.Status("-20")
    $ Fl.say(Fl_gg, "Всмысле? Толян, ты чего? Это же я - Ян, забыл что-ли?")

    show to cry pioneer with Fl_fast

    $ Fl.say(Fl_to, "Не знаю я никакую Яну...")

    show Fl_vignette with Fl_dissolve1
    $ Fl.PlayMusic("Fl_important_negotiations", 1, 5)

    $ Fl.say(Fl_th, "Нет{mn} Этого не может быть! Он и правда меня не помнит.")
    $ Fl.Status("-40")
    $ Fl.say(Fl_r, "Я опустил руки и наклонил голову вниз. Толик резко потерял интерес. {w}Возможно после того как худшие догадки были подтверждены, мой мозг перегрелся и отключился, стараясь поддерживать только координацию и работу мышц ног...")

    hide to normal pioneer with Fl_fast
    $ Fl.Pause(1.0)
    $ Fl.Master(Fl_bg_zoom_to_e(1.7, 8.0, 0.5, 0.64))

    $ Fl.Pause(3.0)
    $ Fl.say(Fl_to, "Яна, ты куда?")
    $ Fl.HideScreens(_with=Fl_fast)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause(2.0)

    scene bg Fl_ext_clubs_day
    show Fl_light_c 
    show Fl_vignette
    with Fl_dissolve2

    $ Fl.Pause(3.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Проходя мимо клуба кибернетики, я заметил пионерку с ярко-голубыми волосами. Она заглядывала в окна здания. На её лице читалось недовольство.")
    $ Fl.say(Fl_th, "Интересно не Артёма ли с Саней она ищет?")

    hide Fl_vignette with Fl_dissolve1

    $ Fl.Status("+60")
    $ Fl.say(Fl_th, "Точно! {w}Может у неё стоит лучше спросить что здесь происходит. Она то наверняка знает правду.")
    $ Fl.say(Fl_th, "И почему я сразу не додумался спросить у нормальных людей. {w}Кто его знает что там в голову взбрело нашей главной звезде отряда со справкой!")

    show kt normal pioner1 with Fl_dissolve1

    $ Fl.say(Fl_gg, "Привет, Кать. Ты случаем не знаешь, почему все так странно себя ведут?")
    $ Fl.say(Fl_ka, "В каком смысле странно? И откуда ты знаешь моё имя?")

    $ Fl.Pause(1.5)
    $ Fl.Status("-30")
    $ Fl.say(Fl_th, "И она тоже... {w}ничего не помнит.")

    show Fl_vignette with Fl_dissolve1

    $ Fl.say(Fl_gg, "Прости, я лучше пойду.")

    hide kt normal pioner1 with Fl_dissolve1

    $ Fl.say(Fl_ka, "Эй, ты же нов...")
    $ Fl.HideScreens(_with=Fl_fast)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause(2.0)

    scene bg Fl_ext_square_day
    show Fl_light_c 
    show Fl_vignette
    with Fl_dissolve2

    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Почему? {w}Почему всё вернулось в самое начало? {w}Как такое вообще возможно?")
    $ Fl.say(Fl_th, "Пальто, которое волшебным образом оказалось снова на мне, хотя я даже не брал его обратно. {w}Снова «Совёнок». {w}Мой отряд, который меня не помнит. {w}И одинаковые события.")
    $ Fl.HideScreens(_with=Fl_fast)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause(2.0)

    scene bg Fl_house_of_mt_day
    show Fl_light_c 
    show Fl_vignette
    with Fl_dissolve2
    
    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Словно день сурка. Только тут диапозон побольше.")
    $ Fl.say(Fl_r, "Пока я анализировал всё происходящее. Мои ноги принесли меня к треугольному домику, окружённого со всех сторон кустами сирени.")
    hide Fl_vignette with Fl_dissolve1
    
    $ Fl.say(Fl_th, "Может, Марина Владимировна сможет дать мне просвет на эту ситуацию.")
    $ Fl.say(Fl_r, "Я уже было хотел открыть дверь, как вспомнил, про то что было в прошлый раз.")

    $ Fl.PlaySound ("Fl_door_knock", 1, 0, False)
    $ Fl.Pause(1.5)
    $ Fl.say(Fl_mv, "Подождите минуту!")
    $ Fl.say(Fl_th, "Ещё одно событие повторилось.")
    $ Fl.say(Fl_r, "В голове снова нарисовался образ вожатой в одном нижнем белье.")
    $ Fl.say(Fl_mv, "Входите!")
    $ Fl.StopAmbience(2)
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)

    
    scene bg Fl_int_house_of_mv_day 
    show mv normal pioner1
    with Fl_effect_1
    
    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_mv, "О, Ян, наконец-то ты приехал!")
    $ Fl.say(Fl_mv, "Я Марина Владимирована - твоя вожатая!")
    $ Fl.say(Fl_gg, "Марина Владимирована, вы тоже ничего не помните? Не про райцентр, не про окончание смены?")

    show mv sad pioner1 with Fl_fast

    $ Fl.say(Fl_mv, "О чём ты?")
    $ Fl.say(Fl_th, "Всё понятно{mn}")
    $ Fl.say(Fl_r, "И тут меня словно пронзило...")
    $ Fl.say(Fl_th, "Меня больше никто не помнит. {w}Я здесь - никто. {w}Я уже не Ян...")
    $ Fl.say(Fl_mv, "Ян?")
    
    $ Fl.Pause(1.5)
    $ Fl.say(Fl_th, "Мне срочно нужно найти Кристину!")
    $ Fl.say(Fl_gg, "Марина Владимирована, а вы знаете Кристину из второго отряда?")
    $ Fl.say(Fl_mv, "Кристину{mn} {w}Во втором отряде нет пионерки с таким именем.")
    $ Fl.say(Fl_gg, "Ч-что? {w}А точно{mn} {w}Хах...")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    scene bg Fl_house_of_mt_day
    show Fl_light_c 
    with Fl_dissolve1

    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Я оставил вожатаю за дверью, она что-то пыталась сказать, но мне было всё равно. {w}В данный момент я не хотел никого слушать. Хотелось чтобы этот мир полностью заткнулся и оставил меня одного.")
    with vpunch

    $ Fl.say(Fl_r, "Я упал на колени и поднял свои глаза высоко вверх. Я хотел чтобы солнце мне выжгло глаза, так бы я смог заглушить внутреннюю боль, которая была словно большим комом в горле, не давала сделать ни единого вдоха.")
    $ Fl.say(Fl_r, "Меня не особо волновала потеря памяти других, ведь с Кристиной мы бы во всём разобрались. {w}Вот только никакой Кристины больше здесь нет, только я.")

    show Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_th, "{b}Я ненавижу эту неделю.{/b}")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.Status("")
    $ Fl.StopAmbience(5)
    $ Fl.StopMusic(5)
    scene bg Fl_black with Fl_dissolve3





    $ Fl.Pause(8.5)

    scene Fl_q_66_2 with Fl_dissolve2
    show Fl_q_66_layer with Fl_effect_down1
    show Fl_q_66_text2 with Fl_dissolve1
    $ Fl.Pause (4.5)

    scene bg Fl_black with Fl_dissolve2

    $ Fl.Pause (6.5)


    scene bg Fl_ext_square_day
    show Fl_light_c 
    show Fl_vignette3
    with Fl_dissolve3


    $ Fl.Save("Dls Одиночка:Глава 1")

    $ Fl.Pause (1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Какая это уже посчёту неделя?")
    $ Fl.say(Fl_th, "Сколько мне приходилось раз слушать одни и те же диалоги, видеть одни и те же лица...")
    $ Fl.say(Fl_th, "Неважно. Это всё равно не имеет никакого значения.")

    $ Fl.Pause (1.0)
    $ Fl.say(Fl_gg, "И снова эта площадь! {w}Здесь и правда красиво{mn} {w}так и хочется сломать что-нибудь!")
    $ Fl.say(Fl_th, "А не пойти ли мне в моё любимое место? {w}В единственное место, где я могу хоть немного успокоиться и расслабиться.")
    $ Fl.say(Fl_r, "Я направился в музкружок.")
    $ Fl.HideScreens(_with=Fl_fast)
    $ Fl.Pause (1.0)
    scene bg Fl_black with Fl_dissolve1

    $ Fl.Pause (3.0)

    scene bg Fl_ext_houses_day
    show Fl_light_c 
    show Fl_vignette3
    with Fl_dissolve2

    $ Fl.PlayMusic("Fl_hron", 1, 6)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "С того момента поменялось многое, например - я. {w}Я всем сердцем ненавижу того, кто решил поиздеваться надо мной, кто сделал мою жизнь такой.")
    $ Fl.say(Fl_r, "Хотя трудно назвать это вообще жизнью. Существовать в промежутке пяти дней, где тебя не помнят и не должно существовать вовсе...")
    $ Fl.say(Fl_r, "Поэтому только музыка заставляет меня оставить реальность далеко позади. {w}Забавно, что в прошлом мире я тоже благодаря музыки смог сбежать от всех проблем.")

    $ Fl.Pause (2.0)
    $ Fl.say(Fl_th, "Музыкальный клуб, да?")
    $ Fl.say(Fl_r, "Неосознанно этот клуб стал моим неким укрытием ото всех, даже от Мику.")
    $ Fl.say(Fl_r, "Мику, самая болтливая пионерка. Я терпеть не могу её быструю речь, а её лучезарная улыбка меня бесит. {w}Дередере, как же меня раздражают вот такие яркие и невинные личности...")
    $ Fl.say(Fl_r, "Но, даже в таком раздраженном состоянии мне всегда нравилась её музыка.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Возможно вы спросите меня: «Так что произошло то?» {w} - а я отвечу, что именно! {w}В {b}ту{/b} самую неделю я потерял свою любовь, после чего мне стали всё чаще сниться кошмары.")
    $ Fl.say(Fl_r, "Именно из-за той недели я больше не могу чувствовать себя собой. Я начал избегать любого контакта с пионерами, что бы не вспоминать {u}о ней{/u}.")

    $ Fl.Pause (2.5)
    $ Fl.say(Fl_th, "Интересно, сколько сейчас времени? {w}Наверное около двух часов. Скоро обед будет.")
    $ Fl.say(Fl_r, "Я летал в облаках и думал про время, как вдруг!")

    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    with vpunch
    $ Fl.Pause (1.5)

    show mi shy pioneer4 f with Fl_dissolve1

    $ Fl.say(Fl_r, "Мику врезалась в меня и обронила свои листки с нотами.")
    $ Fl.say(Fl_mi, "Ой! Извини меня пожалуйста! Я шла и думала как раз про новую песню, которую я вчера сочинила и как-то так получилось, что не заметила тебя!")
    $ Fl.say(Fl_th, "Ага, и правда.")
    $ Fl.say(Fl_mi, "Не сильно ушибся? {w}А то я знаю что иногда достаточно просто легонько удариться, но болит так, что...")
    $ Fl.say(Fl_th, "Хватит.")
    $ Fl.say(Fl_r, "Пионерка-пулемёт и не думала останавливаться. Она перешла в привычний режим обстрела.")
    $ Fl.say(Fl_mi, "Однажды как-то {b}Роза{/b} упала на колени, из-за чего у нее синяк появился, так вот...")
    $ Fl.say(Fl_th, "Да сколько можно? Раздражает!", _with=hpunch)

    $ Fl.AttackScreens(True)
    $ Fl.say(Fl_r, "Я взял и сильно пнул лежащие мелодии, из-за чего они в тот же миг взлетели вверх. {w}Насолив пионерке, я стал уходить.")

    hide mi shy pioneer4 f with Fl_dissolve1

    $ Fl.say(Fl_r, "Сзади послышались всхлипы. {w}Стоило мне на секунду обернуться, как тотчас же я повернулся назад.")
    $ Fl.say(Fl_r, "Мне стало больно смотреть на это. {w}Мику, которая всегда была такой жизнерадостной и веселой, собирает свои нотные листки на коленях и плачет.")
    $ Fl.say(Fl_th, "Почему нужно всегда быть такой неуклюжей? Разве так трудно просто смотреть вперёд когда идёшь? Тогда бы и проблем не было!")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause (3.0)
    scene bg Fl_ext_musclub_day
    show Fl_light_c 
    show Fl_vignette3
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_gg, "Не хотел я всего этого...")
    $ Fl.say(Fl_r, "Я глубоко вдохнул.")
    $ Fl.say(Fl_r, "Меня охватило чувство вины. Мне было тошно от того, каким жестоким я стал за последнее время. {w}Мику была не виновата и она наверное единственная с кем я хоть немного контактировал в пионерлагере. А я умудрился довести её до слёз.")
    $ Fl.say(Fl_r, "Но я припозднился слегка, Мику наверное убежала далеко в противоположную сторону, лишь бы со мной случайно не пересечься.")
    $ Fl.say(Fl_gg, "Э-эх, вот и музыкальный клуб.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause (4.0)

    scene bg Fl_ext_no_bus
    show Fl_light_c 
    show Fl_vignette3
    with Fl_flash

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Опять он просто пропал. Уже в который раз{mn} {w}Стоит мне перешагнуть за ворота пионерлагеря, как автобус в очередной раз пропадает бесследно, неиздав ни единого звука.")
    $ Fl.say(Fl_gg, "Ты издеваешься надо мной что-ли? {w}Ты хочешь что бы я приходил сюда каждый раз с надеждой, которую ТЫ разрушаешь?")
    $ Fl.say(Fl_r, "Потихоньку самоконтроль начал ослабевать.")
    $ Fl.say(Fl_gg, "Или ты ждёшь от меня действий? {w}Может быть ты хочешь, чтобы я на колени встал?!", _with=hpunch)
    $ Fl.say(Fl_gg, "Просто скажи мне и я сделаю! ДАЙ МНЕ ХОТЬ КАКОЙ-ТО ЗНАК!", _with=hpunch)
    $ Fl.say(Fl_gg, "Я{mn} {w}просто тебя{mn}")
    $ Fl.say(Fl_gg, "{b}НЕНАВИЖУ!{/b}", _with=hpunch)
    $ Fl.say(Fl_mi, "За что? {w}Что я тебе плохого сделала?")
    $ Fl.say(Fl_th, "Что?")

    scene bg Fl_ext_camp_entrance_day
    show Fl_light_c 
    show Fl_vignette3
    show mi cry pioneer4 f
    with pushright

    $ Fl.say(Fl_r, "Я обернулся в сторону ворот. {w}Рядом с вывеской стояла Мику и плакала. Из-за недопонимания я задел пионерку за живое. {w}Но я ничего не чувствовал. Уже ничего не чувствовал и это меня пугало.")
    $ Fl.say(Fl_gg, "Перестань, это того не стоит.")
    $ Fl.say(Fl_mi, "Почему ты так говоришь!")
    $ Fl.say(Fl_gg, "Потому что это факт.")
    $ Fl.say(Fl_mi, "Неужели ты меня так ненавидишь?! Почему?!")
    $ Fl.say(Fl_gg, "Да с чего ты так решила?")
    $ Fl.say(Fl_th, "А точно, я ведь сам только что это прокричал...")
    $ Fl.StopMusic(4)

    $ Fl.say(Fl_gg, "Просто{mn} Я больше не могу тут находиться, всё очертело. {w}Но ты всё равно не поймёшь...")

    $ Fl.PlayMusic("Fl_no_tresspassing", 1, 2)
    $ Fl.say(Fl_kvl, "Ты так считаешь?")
    $ Fl.say(Fl_r, "Тон, которым прозвучали эти слова был таким задорным... Даже весёлым.")
    $ Fl.say(Fl_gg, "Кто здесь?!")
    $ Fl.HideScreens()

    scene bg Fl_ext_no_bus with Fl_fast
    scene bg Fl_ext_road_day with Fl_fast

    scene bg Fl_ext_camp_entrance_day
    show Fl_light_c 
    show mi cry pioneer4 f
    with Fl_fast

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Бегло осмотрев всё вокруг, я не нашёл кому принадлежат эти слова. {w}Такое происходило впервые...")
    $ Fl.say(Fl_th, "Странно{mn} Может послышалось?")
    $ Fl.say(Fl_gg, "Мику, ты что-нибудь слышала?")
    $ Fl.say(Fl_mi, "Нет!")
    $ Fl.say(Fl_th, "Значит всё же послышалось... {w}Или крыша начинает ехать?")

    $ Fl.Pause (2.0)
    $ Fl.say(Fl_gg, "Хватит уже!")
    $ Fl.say(Fl_gg, "Сколько можно плакать? Неужели я так сильно тебя обидел? {w}Я не хотел...")

    show mi angry pioneer6 with Fl_fast 

    $ Fl.say(Fl_mi, "Тогда может скажешь, чего ты хотел?")
    $ Fl.say(Fl_r, "Мику так внезапно сократила между нами дистанцию, что я чуть не подпрыгнул.")
    $ Fl.say(Fl_r, "Это первый раз, когда она перешла в наступление за все эти недели.")

    show mi cry pioneer4 with Fl_fast

    $ Fl.say(Fl_mi, "Ведь это приятно делать б-больно? Правда?!")
    $ Fl.say(Fl_r, "Моё тело онимело, в горле образовался ком, а пульс участился. {w}За долгое время меня впервые сковал {b}страх{/b}.")
    $ Fl.say(Fl_gg, "Да что ты несёшь, Мику?")
    $ Fl.say(Fl_gg, "Ты хоть знаешь какого это испытывать чувство вины из-за своей беспомощности?")
    $ Fl.say(Fl_mi, "Знаю! Ты думаешь что я глупая, да?! {w}Вы думаете что я ничего не понимаю, но это чертовск-ки...")
    $ Fl.say(Fl_mi, "БОЛЬНО БЫТЬ СОВСЕМ ОДНОЙ!", _with=hpunch)

    hide mi cry pioneer4 with Fl_fast

    $ Fl.AttackScreens()
    $ Fl.say(Fl_r, "Слёзы ручьём полились с глаз Мику, она вытерла их рукой, после чего толкнув меня, уебажала в сторону леса.")
    $ Fl.StopMusic(4)
    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    $ Fl.say(Fl_r, "Я упал на колени.")
    $ Fl.say(Fl_th, "Да что чёрт возьми происходит!")
    with Fl_flash_red

    $ Fl.say(Fl_gg, "Кхе-кхе... Да чтоб тебя!")
    with Fl_flash_red

    $ Fl.say(Fl_r, "Я стоял на четвереньках и не мог шевельнуться, словно что-то сдавливало меня изнутри. {w}Чем больше времени проходило, тем сильнее оно выворачивало меня наизнанку, из-за чего в конечном итоге я упал в бессознательном состоянии около ворот.")
    $ Fl.HideScreens()
    scene bg Fl_black with vpunch


    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Реальность исчезла, оставив меня одного с тьмой. Я ничего не видел и не слышал, только лицезрел густую дымку, которая поглотила всё живое в свои объятия.")
    $ Fl.say(Fl_th, "Я должен выяснить, что здесь происходит, потому что я больше не могу. Я хочу обратно!")
    $ Fl.say(Fl_gg, "Прощу. {w}НЕТ УМОЛЯЮ! ПУСКАЙ ЭТО ВСЁ ПРЕКРАТИТСЯ!")
    $ Fl.say(Fl_th, "Тишина, покой, давно забытое чувство любви и воспоминания. {w}Набор ли это слов или что-то действительно важное?")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause (5.0)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Никогда бы не подумал, что моё перерождение направится в такое русло. Конечно в аниме были схожее развитие событий, где главный герой возвращался в один и тот же промежуток времени. Вот только предпринимая какие-либо действия он смещал этот промежуток дальше.")
    $ Fl.say(Fl_r, "Моя же реальность была длиной в пять дней и чтобы я не предпринимал всё начиналось с начала...")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Хотя может проблема как раз таки во мне? {w}Может я просто что-то упускаю и делаю не так? Поэтому и не могу выбраться из этой временной петли?")
    $ Fl.say(Fl_r, "Тогда я определённо должен с этим разобраться! Открыть занавес пионерлагеря «Совёнок».")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause (2.5)
    $ Fl.PlayAmbience("Fl_camp_center_night", 1, 4)
    $ Fl.DayTime("night", "night")
    scene bg Fl_ext_camp_entrance_night
    show Fl_dust_full
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Наконец-то я смог выбраться из собственной клетки разума. {w}Ночь захватила власть над лагерем.")
    $ Fl.say(Fl_th, "Странный голос, приступ и головная боль, так ещё и галлюцинации в придачу. Не нравится мне это...")

    scene bg Fl_ext_no_bus_night
    show Fl_dust_full
    with Fl_effect_left2

    $ Fl.Pause (0.5)
    $ Fl.say(Fl_th, "Забавно. {w}{b}Он{/b} так и не появился...")

    $ Fl.Pause (2.5)
    $ Fl.say(Fl_th, "Красиво тут{mn} Даже сейчас.")
    $ Fl.say(Fl_r, "Заключил я. {w}Красота природы единственное что до сих пор удивляло меня в этом лагере.")
    $ Fl.say(Fl_th, "Интересно, а никто не заметил, что меня нет столько времени? {w}Даже не так, никто за это время к воротам даже не вышел? {w}Странно это всё.")
    $ Fl.say(Fl_gg, "Ладно, пора возвращаться обратно. Во всех смыслах...")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(4)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause (6.0)
    $ Fl.DayTime("sunset", "sunset")

    $ Fl.PlayAmbience("Fl_forest_evening", 1, 4)
    scene bg Fl_ext_path_sunset
    show Fl_light_c 
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Следующие пару недель прошли как обычно. Подобных инцидентов, как с Мику не было. {w}Разве что...")
    $ Fl.say(Fl_th, "Каким образом Толян успевает пропасть я не понимаю. {w}И это ещё при том условии, что я сидел около его дома и следил за каждым шорохом.")
    $ Fl.say(Fl_al, "Толи-и-ик!")
    $ Fl.say(Fl_th, "А ты то что тут забыла, цундерка? {w}Что-то я не припомню, чтобы ты хоть раз Толика искала. Неужели снова отклонение от сценария?")
    $ Fl.say(Fl_al, "Попался!")

    $ Fl.StopAmbience(2)
    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.PlayMusic("Fl_demilitarized_zone", 1, 3)
    show Fl_vignette3 with Fl_flash_red

    $ Fl.say(Fl_r, "Я даже толком не успел что-то понять, как мне прилетел кулак прямо в нос.")

    show al angry pioner1 with Fl_dissolve1

    $ Fl.say(Fl_al, "Будешь знать как весь лагерь на дыбы поднимать. И за мной подглядывать!")
    $ Fl.say(Fl_gg, "Ты что совсем страх потеряла?")
    $ Fl.say(Fl_r, "Злобно проскрипел я, вытерая кровь из носа.")
    $ Fl.say(Fl_al, "Придурка этого искала{break2}")

    show al scared pioner1 with Fl_fast

    $ Fl.say(Fl_al, "Ой!")

    show al sad pioner1 with Fl_fast

    $ Fl.say(Fl_al, "Ян, это ты. Прости, я думала это Толя.")
    $ Fl.say(Fl_gg, "Это не повод брать и без разбору людей бить!")
    $ Fl.say(Fl_al, "Прости я правда не хотела.")
    $ Fl.say(Fl_th, "Не хотела! Не хотела! {w}Как же ты порой бесишь.")
    $ Fl.say(Fl_r, "Одарив цундеру пронзительным взглядом, я ещё раз вытер кровь и отправился вглубь леса.")
    $ Fl.StopMusic(4)
    $ Fl.HideScreens(_with=Fl_fast)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause (4.0)
    $ Fl.DayTime("night", "night")

    $ Fl.PlayAmbience("Fl_forest_night", 1, 4)
    scene bg Fl_ext_path2_night
    show Fl_dust_full
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Раз куст, два куст. Поворот направо. {w}Я давно запомнил все дороги в этом лагере.")
    $ Fl.say(Fl_th, "Может как-нибудь уйти на всю неделю в лес? {w}Хотя{mn} В лесу опасно, вон всякие Алисы ходят людей бьют.")

    scene bg Fl_ext_path_night
    show Fl_dust_full
    with Fl_dissolve1

    $ Fl.say(Fl_th, "А может ну его это всё? Я уже давно перестал искать выход(хоть и пообещал). {w}Однако, что-то изменилось, как минимум по голове мне ещё так не прилетало. {w}Вроде.")
    $ Fl.say(Fl_th, "Уже ночь{mn} Неужели я так долго гулял по лесу? {w}Похоже опять ушёл в себя и не обратил внимания.")
    $ Fl.say(Fl_r, "Блуждая в своих мыслях, я не заметил, как подошёл к лагерю.")
    $ Fl.StopAmbience(4)
    $ Fl.HideScreens(_with=Fl_fast)

    $ Fl.PlayAmbience("Fl_camp_center_night", 1, 4)
    scene bg Fl_ext_square_night
    show Fl_dust_full
    with Fl_effect_3

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_gg, "Пожалуй, на сегодня хватит приключений.")
    $ Fl.say(Fl_r, "Это был трудный день, поэтому, полностью вымотанный, я решил пойти лечь спать.")
    $ Fl.say(Fl_th, "Прошу только одного. {w}Чтобы мне не приснился вновь этот кошмар.")
    $ Fl.say(Fl_r, "С неопределенного момента я начал видеть кошмары. {w}Точнее он только один - кошмар.")
    $ Fl.say(Fl_r, "Я точно не помню когда он появился, но точно знаю, что относительно недавно.")
    $ Fl.say(Fl_r, "А самое смешное, что каждый раз видя его, меня охватывает незабываемый ужас, словно я - маленький ребёнок, а кошмар - демон во плоти.")
    $ Fl.HideScreens(_with=Fl_fast)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause (4.0)

    scene bg Fl_ext_house_of_mt_night_without_light
    show Fl_dust_full
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "А вот и дом вожатой. Марина{mn} Владимировна? {w}Да. Точно.")
    $ Fl.say(Fl_th, "Безразницы. Надо заканчивать очередной день.")
    $ Fl.HideScreens(_with=Fl_fast)

    $ Fl.PlaySound("Fl_open_door_2", 1, 0, False)
    scene bg Fl_int_house_of_mt_night2 with Fl_effect_4

    $ Fl.Pause (2.0)
    $ Fl.say(Fl_r, "Как обычно вожатая уже мирно посапывала, отвернувшись к стенке. В такое время было неудивительно. Наверное она уже давно привыкла засыпать одна, пока я шляюсь невесть где.")
    
    scene bg Fl_int_house_of_mt_night2:
        ease 1.5 zoom 1.5 xalign 0.2 yalign 0.65
    
    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Я упал на кровать.")
    $ Fl.say(Fl_r, "Я много думал о том почему и каким образом это происходит. {w}Цикл за циклом. Причины почему всё повторяется. {w}Тщетно.")
    $ Fl.say(Fl_r, "Мне надоело уже думать. {w}Надоело вспоминать, надоело понимать, надоело находиться здесь и видеть одинаковые места и лица, надоело слушать одинаковые диалоги, надоело просматривать один и тот же сценарий множество раз.")
    $ Fl.say(Fl_r, "Я просто хочу жить. {w}Хочу вновь побывать в нормальном мире, в котором я могу пойти куда захочу и когда захочу! {w}А мой же нынешний мир ограничен одним лишь пионерлагерем.")
    $ Fl.say(Fl_r, "По-тихоньку веки начали тяжелеть. Я же легко поддался соблазну сна и отключился.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.ShowBlink()
    $ Fl.StopAmbience(5)

    $ Fl.Pause (7.5)
    scene bg Fl_black with Fl_dissolve1
    $ Fl.HideBlink()
    $ Fl.ShowUnblink()

    $ Fl.DayTime("rain", "rain")

    scene bg Fl_int_mine_wallbreak 
    show Fl_interference_anim
    with Fl_dissolve3
    $ Fl.Pause (2.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.PlayMusic("Fl_dead_city", 1, 5)
    $ Fl.say(Fl_r, "Перед глазами появилась следующая картина. {w}Я находился в какой-то шахте, повсюду разбросан уголь, а вдали лишь непроглядная мгла. Электричество должно быть, если судить по толстым кабелям, висящих на стенах шахты. Следовательно проблема с лампочкой.")
    $ Fl.say(Fl_th, "Заброшенная шахта под старым корпусом? {w}Почему я здесь?")
    $ Fl.say(Fl_r, "Я посмотрел на свои руки. {w}Я попытался посчитать сколько у меня пальцев, но задача оказалась непосильной.")
    $ Fl.say(Fl_th, "Понятно. Сон, значит.")
    $ Fl.HideUnblink()
    $ Fl.HideScreens(_with=Fl_dissolve1)


    scene bg Fl_int_mine_crossroad_lighter
    show Fl_interference_anim
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Не смотря на кромешную тьму, я уверенно шёл прямо. Эту шахту я знал, как своих пять пальцев(хотя я минуту назад их так и не смог посчитать).")
    $ Fl.say(Fl_r, "Наш друг со справкой любит здесь ошиваться, а мы потом его всем лагерем ищем.")
    $ Fl.say(Fl_th, "Направо...")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    scene bg Fl_int_mine_halt_lighter
    show Fl_interference_anim
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Я знал конечную цель своего маршрута, но я не понимал зачем туда иду.")
    $ Fl.say(Fl_r, "Каждый шаг давался всё труднее, тело почему-то неслушалось. Какая-то неведомая сила пыталась остановить меня, но мои ноги сопротивлялись.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    scene bg Fl_int_mine_door_lighter
    show Fl_interference_anim
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Возле двери контроль над телом вернулся, а усталось куда-то ушла. Интересно почему? {w}Может моё упорство смогло победить инстинкт самосохранения? {w}Или это выброс адреалина перед неизвестностью, скрывающейся за дверь?")
    $ Fl.say(Fl_r, "Перестав гадать, я дотронулся до ручки, после чего резко её опустил.")
    $ Fl.say(Fl_r, "Замок не издал ниединого звука, и это меня насторожило.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    scene bg Fl_int_mine_room_ligher
    show Fl_interference_anim
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Стоило мне зайти внутрь, как я тут же скривился. {w}Помещение, отдалённо похожее на пристанище алкашей и наркоманов, встретило меня своей нагнетающей обстановкой.")
    $ Fl.say(Fl_r, "Хоть глаза уже и привыкли к темноте, но без света внутри всё выглядело жутко.")
    $ Fl.say(Fl_r, "Метаясь глазами дабы зацепить хоть за что-то по-мимо мусора и надписей, я заметил чью-то фигуру в дальнем углу комнаты. {w}Свет туда не попадал, поэтому мне оставалось только надеется, что силуэт принадлежит человеку.")
    $ Fl.say(Fl_kvl, "Ну привет, Ян.")
    $ Fl.say(Fl_th, "Ян? Откуда он знает, как меня зовут?")
    $ Fl.say(Fl_r, "Фигура поднялась и начала двигаться в мою сторону.")
    $ Fl.say(Fl_r, "На этот раз инстинкт самосохранения решил взять вверх, поэтому я пулей побежал к двери.")
    $ Fl.say(Fl_th, "Нужно сматываться. Жопой чую, что встреча с ним не сулит ни к чему хорошему.")
    $ Fl.say(Fl_kvl, "Куда же ты?")
    $ Fl.say(Fl_r, "Я дёрнул ручку двери, но она по неведомой причине никак не отреагрировала.")
    $ Fl.say(Fl_th, "Какого чёрта?! Я ведь не закрывал дверь!")
    $ Fl.say(Fl_r, "Не ожиданно мне стало трудно дышать. {w}Я ощутил удушье.")
    $ Fl.say(Fl_r, "Упав на колени, я наблюдал, как некто или нечто приближалось ко мне.")
    $ Fl.say(Fl_r, "Паника и животный страх овладели мной и я что есть силы крикнул.")
    $ Fl.StopMusic()


    $ Fl.DayTime("night", "night")


    $ Fl.PlayAmbience("Fl_camp_center_night", 1, 8)
    scene bg Fl_int_house_of_mt_night2 with vpunch
    $ Fl.say(Fl_gg, "КТО ТЫ?", _with=hpunch)
    $ Fl.say(Fl_r, "Мой крик, нет даже вопль разлетелся по комнате. {w}Я в холодном поту начал держался за сердце, которое билось с бешенной скоростью, отдаваясь покалыванием.")
    $ Fl.say(Fl_r, "Вожатая спала как ни в чём не бывало. Её сон не смог побеспокоить даже мой крик.")
    $ Fl.say(Fl_th, "Мне бы так крепко спать. Тогда и сны вроде бы не сняться...")

    $ Fl.Pause (2.0)
    $ Fl.say(Fl_th, "Это был сон. Просто сон. {w}Сон который повторяется уже бесчисленное множество раз! {w}Может быть, это видение? Или на самом деле такое уже было? {w}Может я просто забыл? Звучит бредово.")
    $ Fl.say(Fl_th, "Надо пройтись. {w}Голова идет кругом, да и после этих кошмаров я всё равно не усну.")
    $ Fl.say(Fl_r, "После того как я сталкивался с данным кошмаром, я подолгу пытался заснуть, но всё бессполезно. Как будто что-то или кто-то не давал мне сделать это.")
    $ Fl.say(Fl_r, "Чтобы не разбудить вожатую, я тихо встал с кровати и отправился на прогулку по ночному лагерю.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.PlaySound("Fl_open_door_2", 1, 0, False)
    scene bg Fl_black with Fl_dissolve1

    $ Fl.Pause (3.0)
    scene bg Fl_ext_square_night
    show Fl_dust_full
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Снова площадь{mn} {w}Не знаю почему, но я уверен, что на ней я смогу собраться с мыслями.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_th, "Как же меня достал этот кошмар. {w}Ещё эта фигура и голос. Я схожу с ума?")
    $ Fl.say(Fl_gg, "Только этого мне ещё не хватало.")
    $ Fl.say(Fl_gg, "Хотя судя по тому, что я сам с собой разговариваю{mn}")
    $ Fl.StopAmbience(4)

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_gg, "Интересно, почему никто не знает где этот лагерь находится? {w}Или может знает, но не говорит?")

    $ Fl.PlayMusic("Fl_powerless", 1, 4)
    $ Fl.say(Fl_kvl, "Ты так действительно думаешь?")
    $ Fl.say(Fl_r, "Услышав знакомый голос, я резко повернулся. Но никого не обнаружил.")
    $ Fl.say(Fl_gg, "Кто ты? И где прячешься?")
    $ Fl.say(Fl_th, "Я определённо где-то слышал этот голос, но где?")
    $ Fl.say(Fl_r, "Таинственный незнакомец вышел из-за дерева, но уличный фонарь не смог его осветить.")
    $ Fl.say(Fl_kvl, "Ну привет, Ян!")
    $ Fl.say(Fl_th, "Это{mn}")

    $ Fl.Pause (1.0)
    $ Fl.say(Fl_th, "Голос из моего сна!", _with=hpunch)
    $ Fl.say(Fl_gg, "Невозможно! Это ты!")
    $ Fl.say(Fl_kvl, "Я? {w}О чём ты? {w}Хотя догадываюсь о чём ты. Кошмары да?")
    $ Fl.say(Fl_r, "В голосе собеседника была отчётливая нотка наигранности и ликования. Казалось, что он специально строит дурачка из себя.")
    $ Fl.say(Fl_kvl, "Странно, почему ты не убегаешь сломя голову. Ты ведь так меня боишься, стоит мне сказать что-то, как ты бежишь, так что пятки только сверкают.")
    $ Fl.say(Fl_th, "Действительно. Во сне я и правда делал всё что перечислил мой собеседник.")
    $ Fl.say(Fl_th, "Хотя у меня есть этому феномену объяснение. {w}Я не чувствую страха, как во сне. Теперь эта фигура и голос не кажутся мне чем-то зловещим.")
    $ Fl.say(Fl_gg, "Может представишься наконец-то?")
    $ Fl.say(Fl_kvl, "С радостью, вот только я не помню своего имени. Так что зови меня {b}добродетель{/b}.")
    $ Fl.say(Fl_gg, "Нет, спасибо. В нашем диалоге я обозначу тебя, как {b}голос{/b}.")
    $ Fl.say(Fl_r, "На что голос лишь рассмеялся. {w}Но судя по реакции он был не против.")
    $ Fl.say(Fl_kvp, "Хочешь я расскажу тебе настоящую правду об этом месте, прежде чем ты завалишь меня своими вопросами?")
    $ Fl.say(Fl_th, "Хах... Так просто? {w}Нееет, так просто ничего не бывает.")
    $ Fl.say(Fl_r, "Я оценил обстановку и понял, что мне интересно то, что он скажет мне.")
    $ Fl.say(Fl_gg, "Я слушаю.")
    $ Fl.say(Fl_kvp, "Ох как резко, даже не хочешь узнать кто я на самом деле? {w}Ха-хах! Может ты и выход знаешь как найти?")
    $ Fl.say(Fl_gg, "К чему эта вся игра? Может лучше к делу перейдёшь?")
    $ Fl.say(Fl_kvp, "Да ты прям сама серьёзность я погляжу. Ладно...")
    $ Fl.say(Fl_kvp, "На самом деле, как ты уже наверно понял, ты не один здесь застрял. {w}Нас много. Это ловушка. Ловушка которая захлопывается без твоего ведома.")
    $ Fl.say(Fl_kvp, "А знаешь кто виноват? Они! Эти бездушные куклы!")
    $ Fl.say(Fl_gg, "Много? {w}Куклы? {w}О чём ты вообще?")
    $ Fl.say(Fl_kvp, "Да ну. Ты разве ничего ещё не понял?")
    $ Fl.say(Fl_kvp, "Все в этом лагере, обычные марионетки, которыми помыкает лагерь.")
    $ Fl.say(Fl_gg, "Не говори так!")
    $ Fl.say(Fl_kvp, "Не веришь...")
    $ Fl.say(Fl_kvp, "Ты мне не веришь?! ТАК ИДИ И СПРОСИ ИХ ОБ ЭТОМ МЕСТЕ, ПОПРОБУЙ УЗНАТЬ - ОНИ НЕ ОТВЕТЯТ.", _with=hpunch)
    $ Fl.say(Fl_r, "Неожиданно голос сорвался на крик. {w}Такой реакции я точно ожидать не мог. В тот же миг, от него вновь повеяло тёмной аурой.")
    $ Fl.say(Fl_kvp, "Тогда почему бы тебе не спросить их об этом месте, про время, {b}год{/b}, {b}число{/b}, например. ДА ВООБЩЕ ПРО ЧТО УГОДНО?")
    $ Fl.say(Fl_gg, "Да что ты забред несёшь?!")
    $ Fl.say(Fl_r, "Мне было тяжело воспринимать слова голоса всерьёз. {w}Всё напоминало бред сумашедщего неболее.")
    $ Fl.say(Fl_kvp, "Неужели? Тогда иди и попробуй! ПОПРОБУЙ! Зачем мне тебе врать?!")
    $ Fl.say(Fl_kvp, "Все они куклы. И ты скоро в этом убедишься.")
    $ Fl.say(Fl_th, "Как же ты надоел.")
    $ Fl.say(Fl_kvp, "Ладненько. Дальше вести беседу нет смысла. {w}Ещё увидимся, Ян!")
    $ Fl.say(Fl_gg, "Постой!")
    $ Fl.say(Fl_r, "Только успел я произнести, как фигура буквально расстворилась в воздухе.")
    $ Fl.say(Fl_th, "Какого?!")
    $ Fl.HideScreens(_with=Fl_fast)
    $ Fl.StopMusic(3)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause (3.0)
    scene bg Fl_ext_square_night
    show Fl_dust_full
    with Fl_dissolve1

    $ Fl.PlayAmbience("Fl_camp_center_night", 1, 8)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Мне понадобилась какое-то время. Чтобы переварить весь диалог со странной личностью(голоса).")
    $ Fl.say(Fl_gg, "Год, дата{mn} {w}Стоп. Об этом я размышлял в первые дни! {w}Почему же я не спросил никого об этом?")
    $ Fl.say(Fl_th, "Хотя вроде бы в каком-то цикле мне удалось найти новостную газету. {w}Но правда ли она существовала или это уже плод моей фанатзии...")
    $ Fl.say(Fl_th, "Я должен узнать! {w}Мне просто нужны подтверждения, что голос ошибся и все жители лагеря живые люди, как и я. Просто я единсвтенный кто помню.")
    $ Fl.say(Fl_r, "На следующий день я отправился искать пионеров.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(4)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.DayTime("day", "day")

    $ Fl.Pause (6.0)
    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 6)
    scene bg Fl_ext_square_day
    show Fl_light_c 
    with Fl_dissolve2

    $ Fl.Pause (1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_gg, "Стой! Подожди!")
    $ Fl.say(Fl_r, "Аквамариновая пионерка остановилась, после чего уставилась на меня.")

    show mi pity2 pioneer4 with Fl_dissolve1

    $ Fl.say(Fl_gg, "Слушай, Мику, можешь пожалуйста сказать какое сегодня число. Я, просто, запамятовал...")
    $ Fl.say(Fl_mi, "Опять, ты начинаешь...")
    $ Fl.say(Fl_gg, "Да, я серьёзно!")

    show mi dontlike pioneer4 with Fl_fast

    $ Fl.say(Fl_mi, "Ты издеваешься, да?")
    $ Fl.say(Fl_gg, "Мику, пожалуйста! Я ведь не прошу многого!")
    $ Fl.say(Fl_r, "Она просто смотрела на меня своими лучезарными глазами и не отвечала.")
    $ Fl.say(Fl_th, "Неужели ей так трудно, назвать число?")
    $ Fl.say(Fl_r, "Вдруг она начала уходить и я поймал её за руку.")
    $ Fl.say(Fl_mi, "ОТПУСТИ!", _with=hpunch)
    $ Fl.say(Fl_gg, "Просто скажи мне что-нибудь! {w}Число, месяц, год! {w}Или где я! {w}Хоть что-то! УМОЛЯЮ!!")
    $ Fl.say(Fl_al, "А ну отпусти Мику!")

    hide mi dontlike pioneer4 with Fl_fast

    $ Fl.say(Fl_r, "Стоило мне на миг отвернуться, как Мику вырвалась с моей хватки и рванула прочь.")
    $ Fl.say(Fl_th, "Снова, она{mn} Как же ты вовремя!")

    $ Fl.PlayMusic("Fl_pile", 1, 5)
    show al angry pioner1 with Fl_dissolve1

    $ Fl.say(Fl_r, "Я повернулся в сторону Алисы, как в тот же момент в меня устремился кулак девушки. Но к счастью для меня, я уже не первый день вижу её удары и успел изучить их.")
    
    $ Fl.AttackScreens(True)
    $ Fl.say(Fl_r, "Я увернулся от удара и стал наблюдать за Алисой.", _with=hpunch)
    $ Fl.say(Fl_gg, "Ты не так поняла! {w}Я ничего не хотел сделать. Мне нужен только ответ на один вопрос и всё.")
    $ Fl.say(Fl_al, "Я давно заметила что ты какой-то странный.")
    $ Fl.say(Fl_gg, "Просто назови мне сегодняшнее число! Ничего более!")
    $ Fl.say(Fl_al, "У тебя точно крыша поехала!")
    $ Fl.say(Fl_th, "Вам <бл*ть> так сложно сказать {b}грёбанное число{/b}?!")
    $ Fl.say(Fl_al, "Ты опасен для общества!")
    $ Fl.say(Fl_al, "Все в лагере считают тебя психом!")
    $ Fl.say(Fl_r, "Я не понимал, что происходит. Мои руки начали наливаться кровью. {w}Чем больше Алиса говорила, тем больше гнев наполнял меня.")
    $ Fl.say(Fl_th, "Псих? {w}Да вы издеваетесь...")
    $ Fl.say(Fl_r, "Моё удивление от её слов перекрывала злость... Её слова задевали меня слишком глубоко.")
    $ Fl.say(Fl_th, "Хах{mn}")
    $ Fl.say(Fl_al, "Хочешь узнать, как я поняла?{w} Так мы за тобой следили!{w} Чтобы такие как {b}ты{/b}...")
    
    with Fl_flash_red
    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    hide al angry pioner1 with hpunch

    $ Fl.say(Fl_r, "Мозг отключился на пару секунд...")
    $ Fl.say(Fl_r, "Я резко подбежал к Алисе и совершил удар. Отчего та потеряла сознание.")
    $ Fl.say(Fl_r, "Она сильная. {w}Но это было неожиданно, быстро, а главное - страшно.")
    $ Fl.say(Fl_gg, "Ненавижу!", _with=hpunch)
    $ Fl.say(Fl_r, "Сердце бешено колотилось, адреналин разлился по-всему телу. {w}Мне стало страшно от того, что я сделал, от того в кого я превращаюсь.")
    $ Fl.say(Fl_gg, "Что{mn} Ч-что я наделал?")
    $ Fl.say(Fl_r, "Я решил скрыться с места битвы.")
    $ Fl.say(Fl_th, "Бежать... Но куда? {w}Точно! В лес, в других местах меня найдут.")
    $ Fl.HideScreens()


    scene bg Fl_ext_path_day:
        Fl_run_fast
    show Fl_light_c 
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_th, "Что я сука наделал?! {w}Я{mn} Я не хотел этого!")
    $ Fl.say(Fl_th, "Но я правда больше не могу держать это в себе! Это уже слишком даже для меня! {w}Постоянное повторяющиеся дни, недели, месяцы...")
    $ Fl.say(Fl_th, "Я начинал сходить с ума. {w}Ме-е-едлено, а главное мучительно.{w} Каким образом? {w}Да всё тем же. Одни и те же разговоры, места, люди - вообще всё. Константа переменных лагеря давит на психику!")
    $ Fl.HideScreens()


    scene bg Fl_ext_path2_day
    show Fl_light_c 
    with Fl_dissolve2
    $ Fl.StopMusic(7)

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Настало время снять розовые очки и осознать ту тяжёлую ношу, которую я нёс на себе всё это время...")
    $ Fl.StopAmbience(5)
    scene bg Fl_black with Fl_dissolve1

    $ Fl.say(Fl_gg, "Я больше не могу.")
    $ Fl.say(Fl_gg, "Я устал. {w}Я просто хочу покоя...")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause (8.0)
    $ Fl.DayTime("prologue", "prologue")

    scene bg Fl_komnata_vos with Fl_dissolve3
    $ Fl.PlayMusic("Fl_pacefic", 1, 8)
    $ Fl.Pause (2.0)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Отложив гитару, я открыл холодильник для напитков. {w}Пусто. Что довольно ожидаемо...")
    $ Fl.say(Fl_r, "Тяжело вздохнув, я бросил усталый взгляд в сторону окна.")
    $ Fl.say(Fl_r, "Уже светало. Солнце потихоньку вставало, попутно озаряя город своими лучиками. Я прищурился и отвернулся.")

    $ Fl.Pause (1.0)
    $ Fl.say(Fl_th, "Ещё одна бессонная ночка. Опять{mn}")
    $ Fl.say(Fl_r, "Наверное стоит представиться. {w}Меня зовут Ян, мне 17 лет, скоро стукнет 18. Живу с родителями(сижу у них на шее). Безработный, имею образование 11 классов. Хикка, сижу целыми днями и ночами дома. Почти не сплю и не ем, ибо доход не позволяет.")
    $ Fl.say(Fl_r, "Так уж сложилось, хоть я и живу с родителями, но стараюсь обеспечить себя сам, зарабатывая на творчестве.")
    $ Fl.say(Fl_r, "Рисование - единственное, что способно меня прокормить. {w}Художник из меня так себе, но людям вроде нравится, да и я своими работами доволен. Что ещё нужно для счастья?")
    $ Fl.say(Fl_r, "Я присел на кровать.")
    $ Fl.say(Fl_r, "За окном был разгар лета. {w}Время года, когда город разливается зелёными красками, {w}когда ясное солнце стучит в окно уже к 4 утра, {w}когда у детей начинаются каникулы, а у взрослых долгожданный отпуск, {w}когда кондиционер становится мечтой любого...")

    $ Fl.Pause (3.5)
    $ Fl.say(Fl_th, "Лето{mn}")
    $ Fl.say(Fl_r, "В голове до сих пор плавали образы тех самых врат, украшаемых хоть и слегка поржавевшим, однако тем не менее приличным набором букв. {w}«Совёнок»...")
    $ Fl.say(Fl_r, "От одного лишь этого слова, я как будто вспомнил вечность. {w}Моё первое счастье, когда я завёл отношения, причём, вполне успешные.")
    $ Fl.say(Fl_th, "А ведь как оно всё было бы, если бы мы действительно встретились здесь...")
    $ Fl.say(Fl_th, "...Разочарование, горечь, и злоба, от той потери{mn}")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Недавно мне приснился очень странный и очень реалистичный сон. {w}Во сне я прожил жалкую жизнь до своего совершеннолетия, а потом произошло то что не подвласно логике. Повстречав плохой конец, я переродился в пионерлагере, где я встретил девушку, влюбился, а потом потерял её...")
    $ Fl.say(Fl_r, "В том мире мне приходилось проживать один и тот же промежуток времени, словно в фильме день сурка, только вместо одного дня у меня было пять.")
    $ Fl.say(Fl_th, "Почему мне кажется, будто это был не сон?")
    $ Fl.say(Fl_th, "...Однако, это всё не то.")
    $ Fl.say(Fl_r, "Мой мозг как будто перезагрузился заново, хоть и с самого начала прекрасно понимал, что это всё - лишь временный сон. Я вновь уставился в окно.")
    $ Fl.say(Fl_r, "Яркий свет больше не раздражал меня, а наоборот подарил мне какую-то умеревотворённость что-ли. Наблюдая за картиной через толстое стекло, туман в голове потихоньку развеивался.")
    $ Fl.say(Fl_r, "Я смотрел на эти монотонные Хрущёвки, которые пережили немало за свою жизнь и повидали ещё больше. {w}Я начал понимать людей ностальгирующих, и депрессирующих. {w}Как я.")
    $ Fl.say(Fl_r, "Когда ты смотришь на это строение - ты видишь в нём нечто большее, чем простое коммунальное жильё. {w}Ты видишь в нём бетонного гиганта, который вежливо впускает всех прохожих, взамен требуя лишь код от домофона, или волшебный магнитик. Не более.")
    $ Fl.say(Fl_r, "За такую мизерную плату, этот гигант готов обогреть тебя изнутри. {w}Передать своё тепло, что бы ты мог приготовить еду. {w}Что бы ты мог спокойно спать, игнорируя все опасности ночной тьмы. {w}Что бы ты никогда не чувствовал себя одиноким, или уж тем более, брошенным.")
    $ Fl.say(Fl_r, "Они никогда не скажут тебе «Прощай», не выгонят на улицу без твоего ведома.")
    $ Fl.say(Fl_r, "Они даже никогда не расскажут тебе очередную будничную историю о очкарике Васе, у которого гопники украли телефон. Они никогда не расскажут тебе, как у дяди Димы протекала крыша, и сколько раз его пол затопило из-за этого.")
    $ Fl.say(Fl_r, "Они никогда не расскажут тебе, как тётя Зина в очередной раз застряла в аварийном лифте...")
    $ Fl.say(Fl_th, "Они никогда ничего тебе не расскажут.")
    $ Fl.say(Fl_r, "От этой мысли мне стало грустно на душе. Меня одолела совесть, а вместе с ней - сочувствие.")
    $ Fl.say(Fl_th, "Правильным ли было всё что я делал всё это время? {w}Правильно ли я распорядился своей жизнью? {w}Закрылся от всего мира, заменив его на двоичный код, влечением к музыке(в частности к гитаре), влеченим к рисованию 2д девочек...")
    $ Fl.say(Fl_r, "Однако на эти вопросы у меня не нашлось ответа. А если бы он и был всё равно толку от него было мало. Во мне нет уже ничего живого, после смерти моей подруги, погибло что-то и во мне, оставив глубокую рану и пустоту в душе.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Я решил, что сеанс психотерапевта окончен, и что меня ждёт ещё сотня таких же непонятных снов, как и раньше.")
    $ Fl.say(Fl_r, "Бросив взгляд на выключенный монитор, я решил оставить своё старое железо в покое и пройтись подышать свежим воздухом.")
    scene bg Fl_black with Fl_dissolve1

    $ Fl.say(Fl_r, "Стараясь особо не шуметь, я прошёл в коридор и обулся. {w}Родители крепко спали, у меня было примерно часика 2-3, пока они проснуться. Они ведь не знают о моих вот таких прогулках.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause (5.5)
    scene bg Fl_ext_khruschevka_night with Fl_effect_mosaic
    $ Fl.Pause (1.0)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Я решил далеко не ходить, а прогуляться вокруг дома. Подышать свежим воздухом для меня было достаточно.")
    $ Fl.say(Fl_r, "И правда мне стало намного легче, будто груз спал с плечь. Пессимистичные мысли сменились на размышления насчёт моей новой песни, которую я недавно написал.")
    $ Fl.say(Fl_r, "Это была уже моя вторая песню, которую я сочинил за время моего затворничества. {w}Первая была что-то своего рода выплеск эмоций после потери дорого мне человека. А нынешняя имела схожий характер, но активнее и жёстче, как никак она написана под жанр рок.")
    $ Fl.say(Fl_th, "Интересно, может Женька попросить на барабанах отыграть. Какая рок композиция без них?")
    $ Fl.say(Fl_r, "Я уже думал набрать старого знакомого, но меня остановило время, которое отобразилось на экране мобильника.")
    $ Fl.say(Fl_th, "Точно он наверняка дрыхнет без задних ног.")
    $ Fl.say(Fl_th, "Тогда днём наберу его, если не забуду...")

    $ Fl.Pause (3.0)
    $ Fl.say(Fl_r, "Зайдя за угол дома, я достал пачку сигарет, которые мне приходилось прятать от родителей. {w}Я обзавёлся этой вредной привычкой месяц назад, хотел просто попробовать, но что вышло то вышло.")
    $ Fl.say(Fl_r, "Понятное дело я не рассказал об этом родителям. И не потому что боюсь признаться, а потому что боюсь что они так же легко смиряться с этим, как с моим новым образом жизни.")
    $ Fl.say(Fl_r, "Поэтому выходить на прогулку, когда родители спят, стало своего рода привычкой. Только так я мог чувствовать себя спокойным, зная что не попаду в неловкую ситуацию, словно подросток с порножурналом.")
    $ Fl.say(Fl_r, "Я достал последнюю никотиновую палочку и аккуратно поднёс зажигалку.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause (1.5)
    $ Fl.PlaySound("Fl_zazigalka", 1, 0, False)
    $ Fl.Pause (2.0)
    $ Fl.PlaySound("Fl_smoking", 1, 0, False)
    $ Fl.Pause (2.5)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Не о такой жизни я мечтал{mn} Хотя положение у меня сейчас явно лучше, чем во сне. Я хотя бы существую.")
    $ Fl.say(Fl_r, "Мрачные мысли вновь залезли ко мне в голову, но я быстро их отбросил сделав очередную тягу.")
    $ Fl.say(Fl_th, "Опять придётся ехать в ларёк за сигаретами... {w}Ещё один повод проветриться?")
    $ Fl.say(Fl_r, "На моём лице появилось что-то похожее на улыбку, предвкушение очередной авантюры почему то подняло мне настроние, что шло на перекос моему образу жизни.")
    scene bg Fl_black with Fl_dissolve1

    $ Fl.say(Fl_r, "И я решил не терять ни минуты, отправиться в магазин прямо сейчас, пока родители не проснулись.")

    $ Fl.Pause (2.5)
    $ Fl.say(Fl_r, "Шагая по дороге, мне начало казаться, что уж слишком долго я иду.")
    $ Fl.say(Fl_th, "То есть, я настолько долго не выходил, что мне уже какие-то сотни метров кажутся бесконечными?")
    $ Fl.say(Fl_th, "Да не, бред. Я ещё не успел преисполниться в домоседстве. Я как минимум выходил на улицу хотя бы через день, а то и каждый день.")

    $ Fl.Pause (2.0)
    $ Fl.say(Fl_r, "Но дорога не прекращалась... Я шёл десять, двадцать, тридцать минут...")

    $ Fl.StopMusic(3)
    $ Fl.say(Fl_r, "Глубоко внутри появилось чувство тревоги. Я резко почувствовал как моё тело начало дрожать. Только не от мурашек, а от холода...")

    scene bg Fl_ext_street_night_vos with hpunch
    $ Fl.PlayMusic("Fl_hron", 1, 5)

    $ Fl.say(Fl_r, "Не замечая вокруг себя ничего, я внезапно спохватился и начал осматривать улицу вокруг себя.")
    $ Fl.say(Fl_th, "Какого чёрта здесь вокруг снег?! И почему так холодно?!")
    $ Fl.say(Fl_r, "Снежинки начали кружиться возле меня, а ветер принялся сдувать всё и вся рядом со мной.")
    $ Fl.say(Fl_r, "Было трудно описать моё удивление от всего происходящего(я был в <ах*е>!). У меня не было ни единой зацепки, почему лето сменилось на зиму. Весь мир принял искажённый облик.")
    $ Fl.say(Fl_th, "Это просто сон, правда?")
    $ Fl.say(Fl_r, "Понимание ситуации приходило со временем... Я ринулся вправо, после чего влево - тупик.")
    $ Fl.say(Fl_r, "Отбегая от своей изначальной точки десятки метров, в скором времени я выходил обратно... Картина перед глазами даже и не планировала меняться.")
    $ Fl.say(Fl_gg, "Да что тут в конце концов происходит-то?!", _with=hpunch)
    $ Fl.say(Fl_r, "Неожиданно я почувствовал дежавю, словно я уже оказывался в подобной ситуации. Но вот только когда? Во сне? Или в реальной жизни?")

    $ Fl.ShowBlink()
    $ Fl.say(Fl_r, "Закрыв глаза, я бежал по дороге снова и снова... {w}Пытавшись улизнуть от этой чёртовой ситуации, я открыл глаза только спустя какое-то время.")
    $ Fl.say(Fl_r, "Вокруг меня уже не было привычных домов... {w}всё было как-то иначе...{w} неестественно...")
    $ Fl.HideScreens(_with=Fl_fast)

    $ Fl.HideBlink()
    $ Fl.ShowUnblink()
    scene bg Fl_ext_street_night_vos with Fl_dissolve1
    with vpunch
    scene bg Fl_black with hpunch
    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Я споткнулся на ровном месте. Удержать равновесие мне не удалось, поэтому я моментально полетел вниз.")
    $ Fl.say(Fl_r, "Когда же я поднял голову... я едва потерял дар речи.")
    $ Fl.HideScreens(_with=Fl_fast)


    scene bg Fl_ext_path_sunset
    show Fl_light_c 
    with Fl_dissolve2
    $ Fl.StopMusic(7)


    $ Fl.Pause(1.5)
    $ Fl.DayTime("sunset", "sunset")

    $ Fl.PlayAmbience("Fl_forest_evening", 1, 4)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Лето. {w}Лес. {w}СССР.")
    $ Fl.say(Fl_r, "Три слова больно ударили в голову.")

    show Fl_vignette3 with Fl_dissolve1

    $ Fl.say(Fl_r, "Всё вокруг меня это сплошной обман. Весь этот мир наполнен ложью.")
    $ Fl.say(Fl_r, "Последние остатки моего здравомыслия иссякали из моего разума.")
    $ Fl.say(Fl_ka, "Ян?")
    $ Fl.HideUnblink()
    hide Fl_vignette3 with Fl_fast

    show kt smile pioner1:
        xcenter -1
        ease 1 xcenter 0.5
    $ Fl.Pause(1.0)

    $ Fl.say(Fl_r, "Я очень быстро обернулся, словно дикий зверь чующий опасность, и посмотрел на пионерку позади себя.")
    $ Fl.say(Fl_gg, "К-катя?")

    show kt normal pioner1 with Fl_fast

    $ Fl.say(Fl_r, "Она как-то странно посмотрела на меня.")
    $ Fl.say(Fl_ka, "Ян, ты в порядке? Что-то неважно выглядишь.")
    $ Fl.say(Fl_r, "Катя сделала небольшой шаг вперёд и вопросительным взглядом пыталась меня изучить.")

    show kt smile pioner1 with Fl_fast

    $ Fl.say(Fl_r, "После чего на её лице нарисовалась мягкая улыбка. {w}Девушка протянула мне руку.")
    $ Fl.say(Fl_r, "В тот же миг в голове всё перемешалось: вопросы, ответы, загадки, побеги, выход. А есть ли он - выход?")
    $ Fl.say(Fl_gg, "Катя{mn} с-скажи мн-не, какое сейчас число? З-забыл, просто.")

    show kt normal pioner1 with Fl_fast

    $ Fl.say(Fl_ka, "Что ты имеешь в виду?")
    $ Fl.say(Fl_gg, "Забыл, просто... Тут у меня нет календаря...")
    $ Fl.say(Fl_r, "Повторил я дружелюбно.")
    $ Fl.say(Fl_gg, "Так какое сегодня число?")

    show kt angry pioner1 with Fl_fast

    $ Fl.say(Fl_ka, "Давай вставай и пойдём! Нас Марина Владимировна искать будет!")

    show kt surprise pioner1:
        ease 1 zoom 1.5

    $ Fl.AttackScreens()
    $ Fl.say(Fl_r, "Я мягко взял её за руку и притянул её к себе.")
    $ Fl.say(Fl_gg, "Прошу скажи мне хоть что-то! Число, месяц, год!")
    $ Fl.say(Fl_gg, "Где я?! Где находится этот лагерь?!", _with=hpunch)
    $ Fl.say(Fl_r, "Ведь я пытался узнать всего лишь один ответ на вопрос...")

    hide kt surprise pioner1 with vpunch
    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    $ Fl.say(Fl_r, "Катя резко вырвалась из хватки моей руки. Пионерка в страхе хотела убежать, но я среагировал быстрее и повалил её держа за руки.")
    $ Fl.say(Fl_gg, "Скажи мне! Я ведь не причиню тебе зла!")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    with Fl_flash_red

    $ Fl.say(Fl_r, "Но паника взяла надо мной вверх и я потерял бдительность. Этим и воспользовалась пионерка, ударив меня ногой.")
    $ Fl.say(Fl_r, "Катя попыталсь скрыться в лесу, но я не мог позволить ей сбежать. Я обязан был догнать её, ведь она моя последняя надежда.")

    scene bg Fl_ext_path_sunset:
        Fl_run_fast
    show Fl_light_c 
    with Fl_dissolve1

    $ Fl.say(Fl_gg, "Катя, подожди, пожалуйста!")

    $ Fl.Pause(3.0)

    $ Fl.say(Fl_r, "Прошло довольно много времени, по крайней мере достаточно для того, чтобы солнце полностью ушло, оставив меня одного в ночном лесу.")
    $ Fl.HideScreens(_with=Fl_fast)
    scene bg Fl_black with Fl_dissolve1

    $ Fl.DayTime("night", "night")

    scene bg Fl_ext_path2_night
    show Fl_dust_full
    with Fl_effect_2
    $ Fl.Pause(1.5)

    $ Fl.PlayAmbience("Fl_forest_night", 1, 4)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Осмотрев всё вокруг, я со всей злости ударил кулаком в дерево и повернулся предположительно в сторону где должен находится лагерь. {w}Как вдруг услышал звук...")

    $ Fl.PlaySound("Fl_fall1", 1, 0, False)
    $ Fl.Pause(1.0)
    
    $ Fl.say(Fl_r, "Через некоторое время я нашёл её... {w}Дыру в тоннели.")
    $ Fl.StopAmbience(3)
    $ Fl.HideScreens(_with=Fl_fast)


    scene bg Fl_int_catacombs_entrance_new with vpunch
    $ Fl.PlaySound("Fl_fall2", 1, 0, False)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.PlayAmbience("Fl_catacombs", 1, 4)
    $ Fl.say(Fl_r, "Спрыгнув вниз, я осмотрелся. {w}И увидел следующее...")
    $ Fl.HideScreens()


    show Fl_prolog_dream
    $ Fl.Pause(1.0)
    hide Fl_prolog_dream

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Тело дрогнуло, от увиденного подкосились ноги. Сердце начало обливаться кровью и бешенно колотиться.")
    $ Fl.say(Fl_r, "Неподалёку я заметил Катю... {w}лежавшую под завалом.")
    $ Fl.HideScreens()


    show Fl_prolog_dream
    $ Fl.Pause(1.0)
    hide Fl_prolog_dream
    $ Fl.PlayMusic("Fl_important_negotiations", 1, 5)

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_gg, "Катя, держись! Я с-сейчас!", _with=hpunch)
    $ Fl.say(Fl_r, "Вопреки ватному телу, я попытался достать пионерку из завала, убирая камни. {w}Но было уже поздно{mn} {w}Большая лужа крови из под завала давала о себе знать.")
    $ Fl.say(Fl_r, "Она посмотрела на меня. {w}Слёзы из её глаз были лучшим доказательством, что она не знала...")
    $ Fl.say(Fl_r, "Катя улыбнулась, находясь на грани жизни и смерти, она вновь озарила меня своей тёплой улыбкой.")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_r, "Последний вздох - её больше нет.")
    $ Fl.HideScreens()


    show Fl_prolog_dream
    $ Fl.Pause(1.0)
    hide Fl_prolog_dream
    scene bg Fl_int_catacombs_entrance_new:
        ease 1.0 zoom 1.15 xalign 0.5 yalign 0.6
    with vpunch
    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Я упал на колени, не в силах сдерживать свои слёзы. {w}Это была моя вина, вся вина только во мне и я - причина всего этого...")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2
    $ Fl.StopAmbience(4)


    $ Fl.DayTime("rain", "rain")


    $ Fl.Pause(2.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Снова{mn} Снова из-за меня погиб человек...")
    $ Fl.say(Fl_th, "Если бы я только не был так настойчив... {w}если бы я не пристал к ней с этой долбанной датой! {w}Она бы была {b}жива{/b}...")
    $ Fl.say(Fl_th, "Как я теперь могу смотреть Кате в глаза после того, что на творил?!")
    $ Fl.StopMusic(4)

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_gg, "Прости меня... Катя. {w}Я обещаю, что изменюсь{mn} больше никто не пострадает{mn} из-за {b}меня{/b}.")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_r, "С тех пор я отдался в липкие объятия глубокой депрессии...")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause(4)
    scene Fl_week_1 with Fl_dissolve1
    $ Fl.Pause(0.5)
    scene Fl_week_2
    $ Fl.Pause(0.2)
    scene Fl_week_1
    $ Fl.Pause(2.0)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.DayTime("day", "day")


    $ Fl.Pause (6.0)
    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 6)
    scene bg Fl_ext_square_day
    show Fl_light_c 
    with Fl_dissolve2

    $ Fl.Pause (1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Пионеры. {w}Линейка. {w}Автобус. {w}Снова и снова, всё то же самое...")
    $ Fl.say(Fl_r, "Со мной начало происходить что-то странное. Я будто перестал понимать происходящее. Реальность больше неощущалась, а тело стало лишь пустой оболочкой.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Спустя сотни попыток побега я сдался. {w}Просто сдался.")
    $ Fl.say(Fl_r, "Вожатая(чьё имя я уже не помню или не знал никогда) пыталась до меня докричаться. {w}Чем-то недовольна, опять.")
    $ Fl.say(Fl_mvv, "Ян! Хватит спать на линейке!")
    $ Fl.say(Fl_an, "Хи-хи. Ты прям как ходячий мертвец!")
    $ Fl.say(Fl_r, "Пошутила Аня.")
    $ Fl.say(Fl_th, "А жив ли я? {w}Может, внешне и не скажешь, но я не чувствую себя живым. {w}Внутри меня давно уже пусто.")
    $ Fl.say(Fl_th, "Внутри я мёртв. Зачем мне жить, если из всех жителей этого мира я один - {u}настоящий{/u}?")
    $ Fl.say(Fl_r, "Пытаясь найти выход, я перепробывал столько вариантов, что не один из них теперь не казался мне реальным.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Некоторое время я даже пробовал заводить романы, но они забывали. {w}Забывали всё и все, кроме меня.")
    $ Fl.say(Fl_r, "Слова голоса всплывали в моей голове и не один раз, будто подказывая выход...")
    $ Fl.say(Fl_r, "«Они все - куклы! Простые марионетки, которых дёргают за ниточки...»")
    $ Fl.say(Fl_r, "Они никогда мне не отвечали. {w}Мои вопросы о лагере всегда оставались без ответа, они пытались сменить тему, или вовсе строили из себя дурачков...")

    scene bg Fl_ext_houses2_day
    show Fl_light_c 
    with Fl_dissolve2

    $ Fl.say(Fl_r, "Игнорируя всех, я направился к своему {b}будущему{/b} домику.")
    $ Fl.say(Fl_r, "Вожатая что-то кричала мне в спину, девочки смеялись, а пионеры просто недоумевая наблюдали. {w}Плевать.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    scene bg Fl_house_of_mt_day
    show Fl_light_c 
    with Fl_dissolve2
    $ Fl.Pause (1.0)

    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
    $ Fl.StopAmbience(4)
    $ Fl.Pause (0.5)
    scene bg Fl_int_house_of_mv_day with Fl_effect_3

    scene bg Fl_int_house_of_mv_day:
        Fl_bg_zoom_th(1.0, 1.5, 1.5, 0.5, 0.2, 0.5, 0.55)
    $ Fl.Pause (1.5)
    $ Fl.PlaySound("Fl_bed_squeak", 1, 0, False)
    $ Fl.AttackMaster()
    $ Fl.say(Fl_r, "Я упал на кровать. {w}Лицо оставалось таким же болезненным и не выражало никаких эмоций.")
    $ Fl.say(Fl_r, "Достав из своего кармана телефон и посмотрев на него, из глаз начали идти слёзы.")
    $ Fl.say(Fl_r, "Нет, я не плакал, как обычные люди, надрываясь и, буквально, крича о том, как мне больно... {w}Нет.")
    $ Fl.say(Fl_r, "На моём лице не промелькнуло ни единой эмоции. {w}Прозрачные, как стекло, ручейки выливались из моих глаз, словно так и надо.")
    $ Fl.say(Fl_th, "Пожалуйста, если ты, Бог, меня слышишь останови этот ад...")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    scene bg Fl_int_house_of_mt_night2 with Fl_dissolve6:
        zoom 1.5 xalign 0.2 yalign 0.55
    $ Fl.Pause (1.0)
    $ Fl.ShowBlink()
    $ Fl.Pause (3.0)
    $ Fl.HideBlink()
    scene bg Fl_int_house_of_mv_day
    $ Fl.ShowUnblink()
    $ Fl.Pause (1.5)
    scene bg Fl_black with Fl_dissolve2
    $ Fl.HideUnblink()

    scene bg Fl_house_of_mt_day 
    show Fl_light_c 
    show Fl_vignette3
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.PlayMusic("Fl_reeducated", 1, 8)
    $ Fl.say(Fl_r, "Логика? {w}Смысл? {w}Смешно{mn}")
    $ Fl.say(Fl_r, "Я не начинал, а уже сходил с ума.")
    $ Fl.HideScreens(_with=Fl_fast)


    scene bg Fl_ext_square_day
    show Fl_light_c 
    show Fl_vignette3
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Потихоньку былые яркие краски этого места начала тускнеть, словно вместе со мной погибает сама природа этого мира.")
    $ Fl.HideScreens(_with=Fl_fast)


    scene bg Fl_ext_beach_day
    show Fl_light_c 
    show Fl_vignette3
    with Fl_dissolve2

    show Fl_prolog_dream
    $ Fl.Pause(1.0)
    hide Fl_prolog_dream

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Я подошёл к пляжу. {w}И вновь ничего. Когда-то от этого места дух захватывало, оно очаровывало своей атмосферой и красотой, но теперь... {w}привычная красота просто исчезла, не оставив от себя и следа.")
    $ Fl.say(Fl_r, "Я ещё раз посмотрел на водную гладь. {w}В голове не было ни единой капли сомнения, только холодная решимость.")
    $ Fl.say(Fl_r, "Привязав к ноге ящик с каким-то металлоломом, я начал неспеша входить в воду.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1

    $ Fl.Pause(1.5)
    scene bg Fl_underwater with Fl_dissolve1
    $ Fl.Pause(1.5)
    scene bg Fl_underwater2
    show Fl_vignette
    with Fl_dissolve1
    $ Fl.Pause(1.5)
    scene bg Fl_underwater3
    show Fl_vignette2
    with Fl_dissolve1

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Ящик резко пошёл ко дну, а моё тело вслед за ним. В области груди началось жжение, вода попала в лёгкие. Я захлёбывался, давление внутри росло, но... {w}Сопротивления не было.")
    $ Fl.say(Fl_r, "По всей видимости, не только я, но и мой организм понимал, что больше ничего не имеет смысл. {w}Моё существование не имеет никакого смысла.")


    show Fl_blood_eff with Fl_flash_red
    $ Fl.DayTime("nightmare", "nightmare")


    $ Fl.say(Fl_r, "Ведь я в этом мире ошибка...")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_flash_red


    $ Fl.Pause(4.5)
    $ Fl.DayTime("night", "night")
    scene bg Fl_int_house_of_mt_night2 with Fl_dissolve3

    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Шла очередная неделя моего бессмысленного существования...")
    $ Fl.say(Fl_r, "Время летело так же медленно, как и я, совершающий очередной акт суицида...")
    $ Fl.say(Fl_r, "На секунду в голове возник главный вопрос.")
    $ Fl.say(Fl_th, "Какой это уже раз?")
    $ Fl.say(Fl_r, "Так и недав ответ на вопрос, я завершил начатое и откинул стул, который разделял меня между жизнью и смертью.")

    with vpunch
    with Fl_flash_red
    $ Fl.PlaySound("Fl_table_hit", 1, 0, False)
    $ Fl.say(Fl_r, "Моё горло сжалось верёвкой, позвоночник хрустнул, а руки начали машинально пытаться снять верёвку, стирая свои ладони в кровь...")
    $ Fl.say(Fl_th, "Суицид не выход, в моём случае так оно и было. Выход из этого ад попросту отсуствовал.")


    scene bg Fl_black with Fl_flash_red
    $ Fl.DayTime("nightmare", "nightmare")


    $ Fl.say(Fl_r, "Моё тело замертво висело в домике вожатой.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(5)

    $ Fl.DayTime("day", "day")


    $ Fl.Pause(7.0)
    scene bg Fl_ext_houses_day:
        Fl_walking3
    show Fl_light_c 
    show Fl_vignette3
    with Fl_dissolve3

    scene Fl_ext_houses_day_glitch:
        Fl_walking3
    $ Fl.Pause(0.3)

    scene bg Fl_ext_houses_day:
        Fl_walking3
    show Fl_light_c 

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Я шёл по дороге, как вдруг повстречал Мику.")

    scene bg Fl_ext_houses_day with vpunch
    show mi shocked pioneer4 with Fl_dissolve1

    scene Fl_ext_houses_day_glitch
    $ Fl.Pause(0.3)

    scene bg Fl_ext_houses_day
    show Fl_light_c 

    $ Fl.PlayMusic("Fl_fyrsta", 1, 4)
    $ Fl.say(Fl_mi, "Ой! Прости-прости, я, наверное, задела тебя? Я не хотела! Честно-честно! Просто, я в очередной раз думала...")
    scene bg Fl_ext_houses_day:
        Fl_walking3
    show Fl_light_c 

    $ Fl.say(Fl_r, "Не став даже начинать слушать её, я просто двинулся дальше по дороге медленными шагами...")
    show Fl_prolog_dream
    $ Fl.Pause(1.0)
    hide Fl_prolog_dream
    $ Fl.say(Fl_r, "Пионерка подбежала ко мне, и продолжила.")

    scene bg Fl_ext_houses_day
    show Fl_light_c 
    show mi upset pioneer6 
    with Fl_dissolve1

    $ Fl.say(Fl_mi, "Что-то случилось? {w}Почему ты такой... грустный? Может, тебе спеть? Да, точно! Давай я спою, и тебе сразу станет лучше!")

    show mi smile pioneer5 with Fl_fast 

    $ Fl.say(Fl_r, "Она схватила меня за руку и понеслась в направлении музклуба.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1

    $ Fl.Pause(2.0)

    scene bg Fl_int_musclub_day
    show mi normal pioneer6
    with Fl_dissolve1

    $ Fl.say(Fl_r, "Я стал ощущать себя трупом. {w}Ходячим трупом. {w}Никак не живым, а именно ходячим.")

    hide mi normal pioneer6 with Fl_fast

    $ Fl.say(Fl_r, "Мику взяла гитару и начала что-то на ней играть, но я её не слушал.")
    show Fl_prolog_dream
    $ Fl.Pause(1.0)
    hide Fl_prolog_dream
    $ Fl.say(Fl_r, "Я был где-то далеко там - у себя дома. {w}Сидел и пялился на экран монитора. Из динамиков слышно речь на японском. А руки аккуратно перебирают струны гитары.")
    $ Fl.HideScreens(_with=Fl_fast)


    $ Fl.DayTime("prologue", "day")


    scene bg Fl_pyst_ch with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_th, "А что, если моя жизнь всегда и была такой?")
    $ Fl.say(Fl_r, "Внезапно подумал я.")
    $ Fl.say(Fl_r, "Где-то глубоко в душе мне стало обидно, а главное - противно. Хотелось снова уйти, чтобы не видеть себя, не чувствовать, забыть о том, кто я.")
    $ Fl.HideScreens(_with=Fl_fast)


    $ Fl.DayTime("day", "day")


    scene bg Fl_int_musclub_day
    show mi happy pioneer5
    with pixellate

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Я ощутил тепло. {w}Вернувшись в реальность, я заметил, как Мику обнимает меня, прижавшись ко мне своим телом.")
    $ Fl.say(Fl_pi, "Зачем ты это делаешь?")

    $ Fl.AttackMaster()
    $ Fl.say(Fl_r, "Мику только сильнее прижалась ко мне. {w}Но я ничего не чувствовал.")
    $ Fl.say(Fl_pi, "Ты же ненастоящая! Вы все ненастоящие - так зачем?! Чего вы хотите добиться от меня?!")

    hide mi happy pioneer5 with vpunch
    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)

    $ Fl.say(Fl_r, "Я сорвался на крик и оттолкнул от себя пионерку. {w}Та упала на пол и заплакала.")
    $ Fl.say(Fl_r, "Не в силах на это смотреть, моё тело вышвырнуло меня из музкружка.")
    $ Fl.HideScreens(_with=Fl_fast)
    scene bg Fl_black with Fl_dissolve2
    $ Fl.StopMusic(2)

    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 4)
    scene bg Fl_ext_houses2_day
    show Fl_light_c 
    with Fl_dissolve2

    $ Fl.say(Fl_r, "Пробегая по лагерю, в голове всплыли слова голоса.")

    show Fl_prolog_dream with Fl_fast
    $ Fl.say(Fl_kvp, "Только мы здесь - настоящие!")
    $ Fl.HideScreens(_with=Fl_fast)

    scene bg Fl_ext_square_day
    show Fl_light_c 
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Пока я шёл, навстречу мне вышла Алиса, загородив мне путь.")

    show al normal pioner2 with Fl_dissolve1
    $ Fl.say(Fl_al, "Куда идёшь?")
    $ Fl.say(Fl_th, "Не живые. {w}Не люди, а куклы. {w}Марионетки...")
    $ Fl.say(Fl_th, "Марионетки{mn}")
    $ Fl.say(Fl_r, "В голове эхом отдавалось одно единственное слово.")
    $ Fl.say(Fl_th, "Марионетки{mn}")
    $ Fl.say(Fl_al, "Эй, ты...")

    show Fl_prolog_dream
    $ Fl.Pause(1.0)
    hide Fl_prolog_dream

    $ Fl.say(Fl_kvp, "Ну ты чего?")
    $ Fl.say(Fl_pi, "Ч-что?")

    scene Fl_ext_square_day_glitch 
    $ Fl.Pause(0.3)
    scene bg Fl_ext_square_day
    show Fl_light_c 

    show al smile pioner1 with Fl_fast

    $ Fl.say(Fl_al, "Ну, ты точно тупой!")
    $ Fl.say(Fl_kvp, "Так ведь, Ян?")
    $ Fl.say(Fl_r, "Раздался вновь голос.")

    show Fl_vignette
    show al smile pioner1
    with Fl_fast
    $ Fl.StopAmbience(3)

    $ Fl.PlayMusic("Fl_psychoflashback", 1, 4)
    $ Fl.say(Fl_r, "Тело сковал леденящий ужас...")
    $ Fl.say(Fl_pi, "Н-нет...")
    $ Fl.say(Fl_kvp, "Нет? А по тебе не скажешь!")
    $ Fl.say(Fl_r, "Она начала смеяться, но я слышал совершенно другой смех...")

    scene Fl_ext_square_day_glitch 
    $ Fl.Pause(0.3)
    scene bg Fl_ext_square_day
    show Fl_light_c 
    show Fl_vignette

    $ Fl.say(Fl_r, "Тот самый дьявольский смех, который однажды пришлось мне услышать.")

    show Fl_prolog_dream
    $ Fl.Pause(0.4)
    hide Fl_prolog_dream with Fl_fast

    $ Fl.say(Fl_r, "Тот самый смех, пробирающий до мозга костей...")
    $ Fl.say(Fl_pi, "Отстань от меня!", _with=hpunch)

    show al surprise pioner1 with Fl_fast

    $ Fl.say(Fl_al, "Ян?")
    $ Fl.say(Fl_kvp, "Как же жалко смотреть на тебя!")
    $ Fl.say(Fl_kvp, "Отстаньте от меня! Я маленький и беспомощный!")
    $ Fl.say(Fl_pi, "Заткнись! Хватит!", _with=hpunch)
    $ Fl.say(Fl_r, "Я больше не мог себя контролировать, я сорвался на крик.")
    $ Fl.say(Fl_kvp, "А значешь, почему ты злишься?! Потому что тебе не выбраться отсюда!")
    $ Fl.say(Fl_kvp, "Добро пожаловать в ад!")


    $ Fl.DayTime("prologue", "day")


    scene cg Fl_pioneer_falling with Fl_fast
    $ persistent.Fl_photo_pallery_18 = True
    $ Fl.say(Fl_r, "Я упал на землю и схватился за голову. {w}Всё тело дрожало, а зрачки расширились.")
    $ Fl.say(Fl_r, "Перед глазами начинало происходить что-то страшное. Мир вокруг меня резко начал принимать совсем другой окрас...")
    $ Fl.say(Fl_r, "Повсюду доносился смех пионеров.")
    $ Fl.say(Fl_r, "Невыносимый шум в голове сводил меня с ума.")
    $ Fl.say(Fl_r, "Я кричал...")
    $ Fl.say(Fl_r, "Со всех сторон доносился какой-то шум, голоса. Ко мне начали подходить люди.")
    $ Fl.say(Fl_art, "Ян, что с тобой?!")
    $ Fl.say(Fl_ss, "Тебе плохо?")
    $ Fl.say(Fl_kvp, "Нет ему сейчас очень хорошо, так ведь?")
    $ Fl.say(Fl_r, "Меня до безумия пугал окружающих смех, который издавали пионеры вокруг меня.")
    $ Fl.say(Fl_r, "У меня задёргался глаз. {w}Сердце невыносимо быстро стучало... {w}Голос сел. Было тяжело дышать.")
    $ Fl.say(Fl_r, "А они всё смеялись и смеялись, смеялись и смеялись!")
    $ Fl.say(Fl_pi, "П-перестаньте! {w}Х-хватит! {w}ПРЕКРАТИТЕ!", _with=hpunch)
    $ Fl.say(Fl_r, "Крича, я надеялся чего-то добиться...")
    $ Fl.say(Fl_r, "Но смех лишь усиливался в моей голове. {w}Ко мне подходило всё больше и больше людей...")
    $ Fl.say(Fl_mir, "Его надо к Виоле!")
    $ Fl.say(Fl_kvp, "Хахахаха!")
    $ Fl.say(Fl_art, "Саня, сбегай за медсестрой!")
    $ Fl.say(Fl_kvp, "Бедненький, Ян.")
    $ Fl.say(Fl_pi, "ЗАКРОЙТЕ СВОИ РТЫ!", _with=hpunch)
    $ Fl.say(Fl_r, "Голоса смешались между собой, создавая адский гул из звуков.")
    $ Fl.say(Fl_r, "До меня пытались докоснуться.")
    $ Fl.say(Fl_r, "Завопив, я отмахивался от всех, кто пытался дотронуться до меня...")
    $ Fl.say(Fl_r, "Я чувствовал, как всё, что находится вокруг меня стало меняться...")

    scene cg Fl_pioneer_falling2 with Fl_dissolve1
    $ Fl.say(Fl_r, "Повернувшись, перед моим лицом были пионеры в смеющихся масках, а их тело состояло из чёрной дымки...")
    $ Fl.say(Fl_r, "Они все делали одно и то же — заливались нескончаемым хохотом.")
    $ Fl.Master(Fl_bghorrorflicker)

    $ Fl.say(Fl_r, "Пионеры звали меня по имени, но вместо привычной речи, я слышал искажённые, отдалённо напоминающие на человеческие, голоса.")
    $ Fl.say(Fl_r, "Закричав, что есть мочи...")
    $ Fl.StopMusic(3)
    $ Fl.HideScreens()
    with hpunch


    $ Fl.DayTime("kira", "day")


    scene cg Fl_pioneer_falling2
    show Fl_blood_eff
    with Fl_dissolve1
    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.PlayMusic("Fl_bloodwork", 1, 5)
    $ Fl.say(Fl_r, "Я со всей силы ударил одного, затем другого пионера...")

    with vpunch
    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.say(Fl_r, "Мои руки были в крови, но я не останавливался.")
    $ Fl.say(Fl_r, "Моё тело действовало само по себе, я был не в силах его остановить.")
    $ Fl.say(Fl_r, "Кто-то пытался ударить меня, другие же бежали прочь...")
    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    $ Fl.say(Fl_r, "Я выдавил глаза парнишке, который повалил меня.")
    $ Fl.say(Fl_r, "Некоторые были умнее, пытаясь задеть меня ножом, но это была роковая ошибка...")

    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    $ Fl.say(Fl_r, "Забрав нож себе, я располостал лицо каждому пионеру.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(4.5)

    scene bg Fl_ext_square_day_blood 
    show Fl_light_c 
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Спустя несколько часов лагерь был переполнен трупами.")
    $ Fl.say(Fl_r, "Вырезанные глаза, перерезанные шеи, фарш из пионеров был раскидан по всей территории.")
    $ Fl.say(Fl_r, "Они ничего не сделали... {w}Никто им не помог...")
    $ Fl.say(Fl_r, "В порыве бешенства Ян, как именовался данный индивид, отрезал голову пионера и попытался закинуть её на флаг, но не вышло.")
    $ Fl.say(Fl_r, "Всё тело было в крови, включая лицо, руки, голову...")
    $ Fl.say(Fl_r, "Бросив взгляд на площадь, а потом на окровавленные руки на моём лице появилась улыбка. После чего я начал тихо посмеиваться, сидя около трупов своих «товарищей». {w}Смешки переросли в истеричный смех. Мне было весело. Я первый раз в жизни почувствовал себя живым.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(4.5)

    scene bg Fl_int_house_of_sl_day
    show kt surprise pioner1
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_ka, "Пожалуйста, не надо! Умоляю! Я ведь ничего плохого не сделала!")
    $ Fl.say(Fl_r, "Катя вжалась в угол комнаты и боялась сдвинуться с места.")
    $ Fl.say(Fl_pib, "Хаха. Ты серьёзно? Умоляешь? {w}А как {b}вы{/b} мне ответили, когда я умолял?!")

    show kt cry2 pioner1 with Fl_fast

    $ Fl.say(Fl_ka, "П-пожалуйста{mn} Я никому ничего не расскажу, обещаю!")
    $ Fl.say(Fl_r, "У пионерки началась в прямом смысле истерика, она захлёбывалась в собственных слезах.")
    $ Fl.say(Fl_th, "Дура! Ты думаешь хоть один убийца отпустит своё жертву за молчание? {w}Ну и бред!")
    $ Fl.say(Fl_th, "Хотя возможно, ты бы хотела сбежать из окна... Но ты же уже поняла - я и это предусмотрел.")
    $ Fl.say(Fl_pib, "Прости, меня это не интересует.")
    $ Fl.say(Fl_r, "Я ухмыльнулся...")

    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    $ Fl.say(Fl_r, "А затем со всей силы ударил арматурой, которую раздобыл в шахтах, по лицу Кати.")

    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    show kt cry2 pioner1 at Fl_punch

    $ Fl.say(Fl_r, "Катя упала издав последний вздох.")
    $ Fl.say(Fl_pib, "Кто дальше?")
    $ Fl.say(Fl_r, "От этих слов веяло холодом... мраком.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause(3.5)

    scene bg Fl_ext_house_of_sl_day
    show Fl_light_c 
    with Fl_dissolve1

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Покинув домик, я неспеша докуривал сигарету. Мыслей никаких не было, только больная фантазия, которая подсказывала мне как лучше поиграть со своей следующей жертвой.")
    $ Fl.say(Fl_mv, "Пионер, тебе кто давал права курить на территории лагеря?!")
    $ Fl.say(Fl_th, "А вот и жертва нашлась!")
    $ Fl.say(Fl_r, "Даже неудосужившись потушить окурок, я медленно повернулся к вожатой.")

    show mv angry pioner1 with Fl_fast

    $ Fl.say(Fl_mv, "Да что ты се{break2}")

    show mv scared pioner1 with Fl_fast

    $ Fl.say(Fl_r, "Мне так и неудалось услышать речь вожатой до конца. Её гримаса наполненная первобытным страхом прервала поток её мыслей.")
    $ Fl.say(Fl_th, "Интересно, что её так напугало? Кровь на моей форме или окровавленная арматура?")
    $ Fl.say(Fl_th, "Хахах. Наверное и то и другое!")
    $ Fl.say(Fl_pib, "Марина Владимировна, я как раз вас искал. Мне бы новый комплект формы, а то не гоже пионеру в грязном ходить.")
    $ Fl.say(Fl_r, "Вожатую начало трясти. Она пыталась что-то сказать, но дрожащие губы не давали ей издать хотя бы малейший писк.")

    hide mv scared pioner1 with Fl_fast

    $ Fl.say(Fl_r, "Она развернулась на 180 градусов и только собралась от меня сбежать, но я был быстрее...")

    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    $ Fl.say(Fl_r, "Меткий бросок арматурой и тело вожатой наповал. {w}Саму арматуру я решил не доставать, пускай будет для неё маленький презент от меня.")
    $ Fl.say(Fl_r, "Нестав париться над скрытием следов приступления, я отправился на площадь.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause(3.0)

    scene bg Fl_ext_square_day
    show Fl_light_c 
    with Fl_dissolve1

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_pib, "Площадь. Снова. Какой это уже раз?")
    $ Fl.say(Fl_an, "Чего ты там бомочешь, новенький?")
    $ Fl.say(Fl_r, "Я обернулся.")

    show an smile pioner1 with Fl_dissolve1

    $ Fl.say(Fl_pib, "Говорю о том какая здесь прекрасная площадь.")
    $ Fl.say(Fl_th, "Не заметила?")
    $ Fl.say(Fl_an, "Конечно прекрасная!")
    $ Fl.say(Fl_r, "Пионерка протянула мне руку.")
    $ Fl.say(Fl_an, "Меня зовут - Аня, а тебя?")
    $ Fl.say(Fl_r, "Я пожал руку в ответ, после чего не разжимая ладонь, поставил другую на плечо девушки. А после...")
    with Fl_flash_red

    hide an smile pioner1 with vpunch

    $ Fl.say(Fl_an, "АААА!", _with=vpunch)
    $ Fl.say(Fl_r, "Вывернул руку хрупкой девушки в другую сторону.")
    $ Fl.say(Fl_r, "И вновь боль, отчаяние и страх. {w}Единственное что могло мне принести удовольствие и покой в этом аду под названием «Совёнок». Наблюдать за страданием кукол помогало мне ощущать себя живым.")
    $ Fl.say(Fl_r, "Её крик начал мне резать слух, поэтому я придавил горло пионерки ногой.")
    $ Fl.say(Fl_r, "Она пыталась. {w}Она боролась. {w}Но что она могла противопоставить такому чудовищу, как я?")
    $ Fl.StopMusic(6)

    $ Fl.say(Fl_r, "Когда в глазах пионерки перестало хоть что-то отражаться, я наконец-то решил представиться. {w}А то некультурно...")
    $ Fl.say(Fl_pib, "А меня - Ян.{w} Когда-то.")
    $ Fl.say(Fl_pib, "Приятно познакомиться.")
    $ Fl.HideScreens()

    $ Fl.PlayMusicFrom("<from 116 to 154>", "Fl_bloodwork", 1, 2)

    scene bg Fl_int_bus with Fl_flash
    scene bg Fl_ext_bus with Fl_flash
    scene bg Fl_ext_houses2_day with Fl_flash
    scene bg Fl_ext_path_day with Fl_flash
    scene cg Fl_d1_food_normal with Fl_flash
    scene bg Fl_ext_path2_night with Fl_flash
    scene bg Fl_ext_no_bus with Fl_flash
    scene cg Fl_dead_pioneer with Fl_flash
    $ persistent.Fl_photo_pallery_11 = True
    scene bg Fl_int_bus with Fl_flash
    scene bg Fl_ext_bus with Fl_dissolve1
    scene bg Fl_ext_square_day with Fl_dissolve1
    scene bg Fl_ext_path_day with Fl_dissolve1
    scene bg Fl_ext_road_day with Fl_dissolve1
    scene bg Fl_ext_path2_night with Fl_fast
    scene bg Fl_ext_medstation_night_light with Fl_fast
    scene bg Fl_int_bus with Fl_fast
    scene bg Fl_ext_houses_day with Fl_fast
    scene bg Fl_ext_houses_night with Fl_fast
    scene bg Fl_ext_no_bus_night with Dissolve(0.3)
    scene bg Fl_ext_square_day with Dissolve(0.3)
    scene bg Fl_ext_musclub_sunset with Dissolve(0.3)
    scene bg Fl_int_bus_people_night with Dissolve(0.3)
    scene bg Fl_ext_no_bus_night with Dissolve(0.3)
    scene bg Fl_ext_square_day with Dissolve(0.3)
    scene cg Fl_d1_food_normal with Dissolve(0.3)
    scene bg Fl_int_bus_people_night with Dissolve(0.3)
    scene bg Fl_int_bus with Dissolve(0.3)
    scene bg Fl_int_clubs_night_TV with Dissolve(0.3)
    scene bg Fl_ext_square_day with Dissolve(0.2)
    scene bg Fl_ext_path_night with Dissolve(0.2)
    scene bg Fl_ext_playground_night with Dissolve(0.2)
    scene bg Fl_ext_musclub_verandah_night with Dissolve(0.2)
    scene bg Fl_int_catacombs_entrance_new with Dissolve(0.2)
    scene cg Fl_miku_piano with Dissolve(0.2)
    $ persistent.Fl_photo_pallery_15 = True
    scene cg Fl_mi_guitar with Dissolve(0.2)
    $ persistent.Fl_photo_pallery_13 = True
    scene bg Fl_ext_road_day with Dissolve(0.2)
    scene bg Fl_house_of_mt_sunset with Dissolve(0.1)
    scene bg Fl_ext_square_night with Dissolve(0.1)
    scene cg Fl_d1_food_normal with Dissolve(0.1)
    scene cg Fl_dead_pioneer with Dissolve(0.1)
    scene cg Fl_miku_piano with Dissolve(0.1)
    scene cg Fl_mi_guitar with Dissolve(0.1)
    scene bg Fl_int_bus with Dissolve(0.1)

    scene bg Fl_black

    $ Fl.StopMusic(6)

    $ Fl.Pause(5.0)
    scene bg Fl_int_bus with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_pib, "Ну что, приступим?! А-ха-ха!")

    $ Fl.PlayMusicFrom("<from 103 to 304>", "Fl_hellwalker", 1, 10)
    $ Fl.say(Fl_pib, "Что же, давайте сегодня сделаем это быстро!")
    $ Fl.say(Fl_r, "Контроль над собой и своим телом был утерян, как и обычный набор стандартных эмоций.")
    $ Fl.say(Fl_r, "Из них остались только безумие... {w}и гнев{mn} Много гнева.")

    scene bg Fl_ext_camp_entrance_day 
    show Fl_light_c 
    with Fl_dissolve1

    $ Fl.say(Fl_pib, "И первым на очереди будет наш дружище со справкой!")
    $ Fl.say(Fl_th, "Терпеть не могу этого аутиста! Только и делает что своим существование создаёт море проблем!")

    show to normal pioneer with Fl_dissolve1

    $ Fl.say(Fl_r, "Толян вышел из-за ворот лагеря и неуклёжо начал идти ко мне.")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_to, "Привет, ты навер...")
    $ Fl.say(Fl_pib, "Ага. Я новенький!")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    show to cry pioneer with Fl_flash_red

    $ Fl.say(Fl_r, "После чего сразу последовал удар.")
    $ Fl.say(Fl_r, "Толик пошатнулся и едва удержался на ногах.")
    $ Fl.say(Fl_pib, "Ну ты чего, дружище, вообще на ногах не держишься.")

    hide to cry pioneer with vpunch
    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)

    $ Fl.say(Fl_pib, "Мог хоть раз что-то другое сказать!")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.say(Fl_r, "Добивающий удар в живот с ноги.")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.say(Fl_pib, "Новенький!", _with=hpunch)

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.say(Fl_pib, "НОВЕНЬКИЙ!", _with=vpunch)
    $ Fl.say(Fl_r, "Моя нога полностью стала в кровавом обличии, а пухлого пионера с покерфейсом уже было не узнать. {w}Но я не останавливался.")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.say(Fl_pib, "Это что, ТАК сложно?!", _with=hpunch)
    $ Fl.say(Fl_r, "Окровавленный Толик уже давно не двигался и не подавал признаков жизни.")
    $ Fl.say(Fl_pib, "Пионер - всем ребятам пример! Да?")
    $ Fl.say(Fl_r, "Мысленно обратившись к вожатой и раскинув руки, я начал заливаться дьявольским смехом.")
    $ Fl.say(Fl_pib, "Тебе тут самое место, дружище, отдыхай. {w}Теперь твой идиотизм вылечен.")
    $ Fl.say(Fl_pib, "Что-то занесло меня сегодня! {w}Так-так{mn} Кто же следующий?")
    $ Fl.say(Fl_th, "Уже не терпиться узнать кто станет следующим счастливчиком или жертвой...")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(2.5)

    scene bg Fl_ext_square_day
    show Fl_light_c 
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Неспеша, но я всё же добрался до площади. {w}На лице застыла злобная ухмылка.")
    $ Fl.say(Fl_pib, "Дом, милый дом! {w}Где же вы все?!")
    $ Fl.say(Fl_r, "Недалеко от площади виднелась Аня, выходящая из своего домика с ведром.")
    $ Fl.say(Fl_pib, "Ооо{mn} А для тебя, садисточка, будет отдельный сюрприз!")
    $ Fl.say(Fl_r, "Я отправился быстрым шагом к кибернетикам.")
    $ Fl.HideScreens(_with=Fl_fast)

    scene bg Fl_ext_clubs_day
    show Fl_light_c 
    with Fl_dissolve1

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_pib, "А вот и клуб! {w}Мой клуб! {w}Нет, наш! Знакомься это Саня, а это...")
    $ Fl.say(Fl_pib, "Ладно что-то понесло меня не туда.")
    $ Fl.say(Fl_r, "Я заглянул в окно. {w}Хозяев обнаружить не удалось, Кати тоже поблизости не наблюдалось.")
    $ Fl.say(Fl_th, "Наверное сегодня я поторопил события{mn} За то никто не помешает!")
    $ Fl.say(Fl_r, "Я приоткрыл дверцу клуба и вошел в него, оглядываясь по сторонам.")
    $ Fl.HideScreens(_with=Fl_fast)


    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
    scene bg Fl_int_clubs_male_day with Fl_effect_5

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_pib, "Ещё бы вспомнить где она...")

    $ Fl.Pause(2.5)
    $ Fl.say(Fl_pib, "Вот и она - отверточка!")
    $ Fl.say(Fl_th, "Ах, как приятно! {w}Я - художник, отвёртка - моя кисть, а полотном будет наша красноволосая пионерка!")
    $ Fl.say(Fl_th, "Ведь для девушки важно что? {w}Правильно! Внимание. Вот его то как раз она получит с полна!")
    $ Fl.HideScreens(_with=Fl_fast)


    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
    scene bg Fl_ext_clubs_day
    show Fl_light_c  
    with Fl_effect_5

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Покинув здание клубов, у меня вырвался порыв смеха. Мне хотелось поскорее увидеть очаровательное личико нашей садистки.")
    $ Fl.say(Fl_th, "Ей же вроде нравится играть на эмоциях других? Вот и я поиграю!")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(3.5)

    scene bg Fl_ext_houses_day
    show Fl_light_c 
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Спустя пару минут я уже сидел на лавочке, повторяя события первого дня, около домиков и выжидал.")
    $ Fl.say(Fl_th, "Ну где же ты? Я уже заждался тут изображать из себя идиота! {w}Неужели так тяжело быстро воды набрать?!")
    $ Fl.say(Fl_r, "Сзади послышались шаги.")
    $ Fl.say(Fl_th, "А вот и ты моя дорогая! {w}ДАВАЙ ОБНИМУ!")
    $ Fl.say(Fl_r, "Я резко открыл глаза и вонзил со всей силы отвёртку в тело Ани.")

    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    $ Fl.say(Fl_r, "Пионерка выронила ведро, вылив всё содержимое себе на всё что ниже юбки.")

    $ Fl.PlaySound("Fl_water_obl", 1, 0, False)
    $ Fl.say(Fl_r, "На её лице застыл первобытный страх. {w}Она была сильно напугана. {w}Настолько сильно, что казалось перед ней стоит само исчадие ада.")

    show an surprise pioner2 with Fl_dissolve1 

    $ Fl.say(Fl_r, "Аня захрипела... Начала кашлять кровью, попутно пытаясь бороться со смертью.")
    $ Fl.say(Fl_r, "Ведь это {b}его{/b} игра, соответственно и правила его. {w}По крайней мере, так считает он — безумец, находящийся внутри меня.")

    show an cry pioner2 with Fl_dissolve1

    $ Fl.say(Fl_r, "На глазах пионерки навернулись слёзы. {w}Она не хотела умирать.")
    $ Fl.say(Fl_pib, "Ой, неужели мои объятия были настолько сильны?! {w}Прости меня, Аня!")
    $ Fl.say(Fl_pib, "Или ты растроилась, потому что я тебе цветов на площади не нарвал?")
    $ Fl.say(Fl_r, "Аня истекала кровью и не могла даже выговорить слово, вместо них она могла только плеваться алой жидкостью и плакать.")
    $ Fl.say(Fl_pib, "Что такое? Неприятно? {w}Да?")
    $ Fl.say(Fl_r, "И в этот момент я кое-что вспомнил...")

    scene Fl_ext_houses_day_sep
    show Fl_interference_anim
    with Fl_flash

    $ Fl.say(Fl_pib, "Неприятно, да?")
    $ Fl.say(Fl_r, "В тот момент я погрузился в воспоминание и не заметил, как ослабил хватку, из-за чего Аня упала на дорожку.")

    scene bg Fl_ext_houses_day
    show Fl_light_c 
    with Fl_flash

    $ Fl.say(Fl_pib, "Тебе больно? Так ведь?")
    $ Fl.say(Fl_kr, "ЧТО ТЫ НАДЕЛАЛ?!")
    $ Fl.say(Fl_th, "Что...")
    $ Fl.say(Fl_r, "Я быстро вернулся обратно в реальность и оглянулся. {w}Но там никого не оказалось...")
    $ Fl.say(Fl_pib, "Ааа? {w}Показалось?")
    $ Fl.say(Fl_th, "Странно. Почему у меня чувство дежавю? {w}Забавно!")
    $ Fl.say(Fl_r, "Тем временем пионерка с красными волосами в {b}последний{/b} раз издала свой {b}последний{/b} вздох.")
    $ Fl.say(Fl_pib, "Как жаль, а я хотел тебя помучить подольше...")
    $ Fl.say(Fl_r, "Я лукаво улыбнулся.")
    $ Fl.StopMusic(9)

    $ Fl.say(Fl_pib, "Утомилась небось?! {w}Ну отдыхай моя красноволосая принц{b}э{/b}сса, отдыхай!")
    $ Fl.say(Fl_r, "Дальше в моей очереди стоял музыкальный клуб.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(3.5)

    scene bg Fl_ext_musclub_day
    show Fl_light_c 
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Я уже не помню когда успел создать «расписание» в своей голове, но я точно знал, что почти каждую неделю придерживаюсь только ему.(хотя бывают и исключения)")
    $ Fl.say(Fl_r, "Утолить свою жажду крови? {w}Насмотреться на то, как тебя умоляют о пощаде? Да, забавно.")
    $ Fl.say(Fl_r, "Мне просто хотелось осуществить свою месть... Уничтожить весь лагерь. {w}Ощутить себя по-настоящему живым, боль и страдание других - единственное что осталось у меня.")
    $ Fl.say(Fl_th, "Хех! Ну звездочка моя! Я уже иду к тебе, никуда не уходи!")
    $ Fl.HideScreens(_with=Fl_fast)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause(3.5)

    scene bg Fl_ext_musclub_verandah_day
    show Fl_light_c 
    with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Однако, будем честны, такое уже было: взрывы, поджоги, убийства.")
    $ Fl.say(Fl_r, "Но самое весёлое... Порой они так начинали меня бояться, что просто теряли сознание.")
    $ Fl.say(Fl_pib, "Интересно, если в день убивать только одного, они заметят, или тоже не обратят внимание?")
    $ Fl.say(Fl_pib, "А если на площади у всех на виду как взять да...")

    $ Fl.PlayMusic("Fl_Railgun", 1, 4)
    $ Fl.say(Fl_r, "Мой поток мыслей прервала музыка.")
    $ Fl.say(Fl_pib, "И снова все та же мелодия{mn} Одно и то же.")
    $ Fl.say(Fl_th, "Может быть сделать из неё музыкальный инструмент?")
    $ Fl.say(Fl_th, "Хаххаха. А интересная мысля! {w}Правда времени на это уйдёт много...")
    $ Fl.say(Fl_th, "Точно. У меня же целая бесконечность! Так что времени у меня полно!")
    $ Fl.say(Fl_r, "И снова я повторяюсь...")
    $ Fl.say(Fl_th, "Бесит! Хочется уже что-то новое придумать!")
    $ Fl.say(Fl_pib, "Думаю, стоит поменять план...")
    $ Fl.say(Fl_pib, "Ладно! Не время отвлекаться! {w}Переходим к представлению!")
    $ Fl.StopMusic(4)
    $ Fl.HideScreens(_with=Fl_fast)
    $ Fl.PlaySound("Fl_open_door_2", 1, 0, False)
    scene bg Fl_int_musclub_day with Fl_flash:
        subpixel True
        zoom 1.4 xalign 0.5 yalign 0.5 alpha 1.0
        ease 5 zoom 1.0 xalign 0.5 yalign 0.5 alpha 1.0
            

    $ Fl.Pause(2.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Музыкальный клуб, помещение где создаются шедевры творчества - музыка, способная излечить любую рану(так я считал раньше).")
    $ Fl.say(Fl_th, "Ну приветик, Микуся.")
    $ Fl.say(Fl_r, "Сказал я с нездоровой гримасой на лице, как и с всё той же, но уже кровавой отверткой в кармане.")
    $ Fl.say(Fl_r, "Но в ответ лишь тишина. Никогда раньше так тихо не было здесь.")
    $ Fl.say(Fl_th, "Где же ты? {w}Не нравится мне это.")
    $ Fl.say(Fl_r, "Мой взгляд сфокусировался на открытой двери в кладовку.")
    $ Fl.say(Fl_th, "Что это ты там делаешь, интересно...")
    $ Fl.say(Fl_r, "После того как я вошёл в кладовку, я медленно стал осматривать комнату.")
    scene bg Fl_black with Fl_dissolve1

    $ Fl.say(Fl_th, "Твою мать, <нихр*на> не видно же, такое чувство что я в подвале каком-то шарусь.")
    $ Fl.say(Fl_pib, "Я пришёл записаться в кружок, есть тут кто живой?")
    $ Fl.say(Fl_r, "Я уже собирался покинуть кладовую, как...")
    $ Fl.say(Fl_pib, "Хм-м?")

    $ Fl.PlayMusicFrom("<from 18 to 130>", "Fl_doubled", 1, 10)
    $ Fl.say(Fl_r, "Внезапно на меня сверху набросилась Мику и стала душить, охватив мою шею ногами.")
    $ Fl.say(Fl_r, "Я попятился назад.")
    $ Fl.say(Fl_th, "И откуда ты только свалилась?!")

    scene bg Fl_int_musclub_day with vpunch
    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    $ Fl.say(Fl_r, "Вылетев из кладовки, я упал на чистый пол музкружка, попутно роняя рядом стоящие инструменты.")
    $ Fl.say(Fl_pib, "Неужели оп-паздал?")
    $ Fl.say(Fl_mi, "Ты! Ты убил её!")
    $ Fl.say(Fl_pib, "Не б-бойся.")
    $ Fl.say(Fl_r, "Я приложил все усилия что бы разжать ноги Мику... {w}После чего бросил её в стену.")

    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    $ Fl.say(Fl_pib, "Ты тоже умрёшь!")
    $ Fl.say(Fl_pib, "Но спасибо за эротичный приём, Мику, мне очень понравилось!")
    $ Fl.say(Fl_r, "У неё изначально не было и шанса. {w}У меня было слишком много времени, поэтому я смог прочитать все книги в библиотеке и не один раз. И по чистой случайности, там оказалась книжка по самообороне.")
    $ Fl.say(Fl_r, "Теория это хорошо, но нужна и практика. {w}А она у меня была на пионерах.")
    $ Fl.say(Fl_pib, "Эй, красавица, вставай! Хватит уже отлёживаться!")
    $ Fl.say(Fl_r, "В моей руки оказалась отвёртка. Я уже замахнулся для удара...")
    $ Fl.StopMusic(3)

    $ Fl.say(Fl_r, "Но меня остановила мёртвая тишина, которой несвойственно быть в музклубе. {w}Мику лежала без сознания.")
    $ Fl.say(Fl_th, "Что-то тут не так... {w}Тихо. {w}Даже слишком.")
    $ Fl.say(Fl_pib, "Не понял, а почему тихо?")

    $ Fl.PlaySound("Fl_brass_drop", 1, 0, False)
    $ Fl.say(Fl_r, "Для проверки я пнул, стоящую рядом, бас-гитару.")
    $ Fl.say(Fl_th, "Звук есть. {w}Значит я не оглох{mn}")
    $ Fl.say(Fl_pib, "Ладно, полежишь значит пока тут.")
    $ Fl.say(Fl_th, "Хах. Прикольно.")
    $ Fl.say(Fl_r, "Сказал я Мику, и привстав, бросил глаза в сторону окна.")
    $ Fl.say(Fl_th, "Да вроде всё как обычно...")
    $ Fl.say(Fl_th, "Но лагерь перестал издавать каких-либо звуков{mn} Неужели что-то новенькое?")
    $ Fl.say(Fl_th, "Это так смешно и банально звучит. {w}Я... Я просто не могу!")
    $ Fl.say(Fl_pib, "НОВОЕ! Ухахаххах!")
    $ Fl.say(Fl_pib, "Ай, плевать! Я всё равно собирался уходить.")
    $ Fl.say(Fl_pib, "Японочка конечно хороша, но меня ждёт другая работа.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(2.5)

    scene bg Fl_ext_musclub_day
    show Fl_light_c 
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Я вышел из здания музыкального клуба и осмотрелся.")
    $ Fl.say(Fl_pib, "Действительно, абсолютная тишина.")
    $ Fl.say(Fl_th, "Вот только правда ли это или просто глучит меня. {w}Лучше проверить.")
    $ Fl.say(Fl_th, "Ух и весело же чувствую будет.")
    $ Fl.say(Fl_th, "Но может ли это быть опасно(смешно услышать такое от безумца)? {w}Тогда я в деле! {w}Во всяком случае, это реально что-то новенькое!")
    $ Fl.say(Fl_pib, "Проветрюська я пожалуй.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.DayTime("kira", "sunset")
    $ Fl.Pause(4.0)

    scene bg Fl_ext_square_sunset
    show Fl_light_c 
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.Pause(1.0)
    $ Fl.say(Fl_r, "Я вернулся на площадь. {w}Это был центр лагеря.")
    $ Fl.say(Fl_r, "Время близилось к закату. {w}Солнце потихоньку начало садиться, придавая лагерю совсем иной окрас.")
    $ Fl.say(Fl_th, "И никого{mn} Не понимаю. Что тут происходит? {w}Или произошло?")
    $ Fl.say(Fl_th, "Может как в {b}тот{/b} раз? {w}В прятки решили поиграть что ли? {w}Или неужели уже нашли справочника?")
    $ Fl.say(Fl_th, "Нет не должны были...")

    $ Fl.PlaySound("Fl_wind", 1, 0, False)
    $ Fl.say(Fl_r, "Мой поток мыслей прервал сильный порыв ветра.")

    $ Fl.PlayMusic("Fl_harbin", 1, 3)
    $ Fl.say(Fl_pib, "Так-так. По закону жанра сейчас сто процентов должно что-то произойти? {w}Нет? Тогда я сам сделаю что-то! Начнем с...")
    $ Fl.say(Fl_pior, "А ты я погляжу развлекаешься здесь, да?")
    $ Fl.say(Fl_pior, "Одобряю! {w}Жаль, что у меня нет времени тебе объяснять что происходит.")

    scene cg Fl_bloodsquare with Fl_dissolve1
    $ persistent.Fl_photo_pallery_9 = True
    $ Fl.say(Fl_r, "Не поворачивая голову я произнес.")
    $ Fl.say(Fl_pib, "Хах. А ты у нас ещё кто? {w}Очередной пионеришка? {w}Ну точнее - клон. {w}Или клоун, а?")
    $ Fl.say(Fl_r, "Очередной «пионер» - так я назвал кукол, которые противоречат нормам морали и здравого смысла. Они чем то со стороны напоминают меня. Жестокие психопаты, убивающие ради развлечения.")
    $ Fl.say(Fl_r, "Мои встречи с пионерами начались, когда я пересёк точку невозврата. Поэтому я до сих пор считаю, что это лагерь послал своего рода стражей, охраников, чтобы защитить себя от такого чудовища как я.")
    
    scene cg Fl_bloodsquare2 with Fl_fast
    $ Fl.say(Fl_pior, "Да ты дерзкий. {w}Ну, очередной «Псих» делу не помешает!")
    $ Fl.say(Fl_pib, "Ты так считаешь?")
    $ Fl.say(Fl_r, "Моя улыбка приобрела более безумный вид.")

    scene cg Fl_bloodsquare3 with Fl_fast
    $ Fl.say(Fl_r, "Пионер приблизился на пару шагов.")
    $ Fl.say(Fl_pib, "Не помешает говоришь? {w}Давай проще, я быстренько переломаю твои кости и на этом покончим, а?")
    $ Fl.say(Fl_pior, "Да ну правда что ли? Вот так просто?")

    scene cg Fl_bloodsquare4 with Fl_fast
    $ Fl.say(Fl_pior, "Ладно, ты наверное думаешь зачем я здесь? {w}Я пришёл, конечно же убить тебя! Сказал же - у меня нет времени на тебя.")
    $ Fl.say(Fl_pib, "М-м-м-м... Ну это меняет дело! {w}Наконец-то новый противник!")
    $ Fl.say(Fl_th, "Наш бой будет легендарным!")
    $ Fl.say(Fl_r, "Произнеслось у меня в голове, цитата одного мультика.")
    $ Fl.say(Fl_r, "Я был оживлён таким поворотом событий, ведь все то что было ранее было не впервые, в отличии от этого дня.")
    $ Fl.say(Fl_pib, "Тогда поиграем?")

    scene cg Fl_bloodsquare5 with Fl_fast
    $ Fl.say(Fl_r, "В кровь поступал новый запас адреналина со скоростью пули.")
    $ Fl.say(Fl_pior, "А почему бы и нет. Я только за!")
    $ Fl.say(Fl_r, "Рывок в сторону и его нога уже летит в меня.")
    $ Fl.HideScreens()
    jump pioneer_battle




label pioneer_battle:
    scene cg Fl_bloodsquare5 with Fl_fast
    $ Fl.PlayMusicFrom("<from 86 to 300>", "Fl_harbin", 1, 3)
    call screen pi_battle_1 with Fl_flash_red
    screen pi_battle_1:
        add "battleaction1" xalign 0.5 yalign 0.5
        key "е" action [Hide("pi_battle"), Jump("hit_success")]
        key "Е" action [Hide("pi_battle"), Jump("hit_success")]
        key "T" action [Hide("pi_battle"), Jump("hit_success")]
        key "t" action [Hide("pi_battle"), Jump("hit_success")]
        timer 2 action Jump("pi_lose")




label pi_lose:
    $ Fl.ShowScreens()
    $ Fl.say(Fl_r, "Последнее что я чувствовал, это медленно стекающие алые сгустки крови по моему лицу...")
    $ Fl.say(Fl_pib, "Ещ-щё ув-в-видимся, хах...")
    scene bg Fl_black with Fl_flash_red
    $ Fl.HideScreens(_with=Fl_fast)
    $ Fl.StopMusic(3)
    $ Fl.Pause(2.0)
    jump pi_say



label pi_lose2:
    $ Fl.ShowScreens()
    $ Fl.say(Fl_r, "Лязгонье металла и странное движение.")
    $ Fl.say(Fl_r, "После меня заинтересовали фиолетовые хвостики{mn} А после и моя падающая голова.")
    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    scene bg Fl_black with Fl_flash_red
    $ Fl.HideScreens(_with=Fl_fast)
    $ Fl.StopMusic(3)
    $ Fl.Pause(2.0)
    jump pi_say


label pi_lose3:
    $ Fl.ShowScreens()
    $ Fl.say(Fl_pior, "З-забавно, ведь даже {b}он{/b} не успел тебе помочь.")
    $ Fl.say(Fl_th, "Кто? {w}Мне кто-то должен был помочь?")
    $ Fl.say(Fl_pior, "Вид-димо, хаха, не судьба.")
    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    with vpunch
    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    scene bg Fl_black with Fl_flash_red
    $ Fl.HideScreens(_with=Fl_fast)
    $ Fl.StopMusic(3)
    $ Fl.Pause(2.0)
    jump pi_say


label pi_lose4:
    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    with vpunch
    scene bg Fl_black with Fl_flash_red
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_th, "Я не смог. Он оказался сильнее, но как же так?")
    $ Fl.say(Fl_th, "Не уж то я потерял голову даже не осознав это? {w}Не смог противостоять самому себе, и в итоге тот, кто однажды создал остальных, погиб от своих же рук?")
    $ Fl.say(Fl_th, "Иронично{mn} Но это хотя бы было весело!")
    $ Fl.HideScreens(_with=Fl_fast)
    $ Fl.StopMusic(3)
    $ Fl.Pause(2.0)
    jump pi_say


label pi_say:
    $ Fl.Pause (5.0)
    show text "{font=font/Fl_mainmenu.ttf}{size=55}Ты и правда считаешь это концовкой?{/size}{/font}"
    with Fl_dissolve1

    $ Fl.Pause (3.0)
    show text "{font=font/Fl_mainmenu.ttf}{size=55}Ну уж нет, я так легко бы не слился.{/size}{/font}"
    with Fl_dissolve1

    $ Fl.Pause (3.0)
    show text "{font=font/Fl_mainmenu.ttf}{size=55}Поэтому будь добр, сделай так как надо!{/size}{/font}"
    with Fl_dissolve1
    jump pioneer_battle





label hit_success:
    $ Fl.Pause(0.7)
    call screen pi_battle_2 with hpunch
    screen pi_battle_2:
       add "battleaction5" xalign 0.5 yalign 0.5
       key "h" action [Hide("pi_battle_2"), Jump("hit_success2")]
       key "H" action [Hide("pi_battle_2"), Jump("hit_success2")]
       key "р" action [Hide("pi_battle_2"), Jump("hit_success2")]
       key "Р" action [Hide("pi_battle_2"), Jump("hit_success2")]
       timer 2 action Jump("pi_lose2")


label hit_success2:
    $ Fl.Pause(0.7)
    call screen pi_battle_3 with vpunch
    screen pi_battle_3:
       add "battleaction2" xalign 0.5 yalign 0.5
       key "и" action [Hide("pi_battle_3"), Jump("hit_success3")]
       key "И" action [Hide("pi_battle_3"), Jump("hit_success3")]
       key "b" action [Hide("pi_battle_3"), Jump("hit_success3")]
       key "B" action [Hide("pi_battle_3"), Jump("hit_success3")]
       timer 2 action Jump("pi_lose3")


label hit_success3:
    $ Fl.Pause(0.7)
    call screen pi_battle_4 with vpunch
    screen pi_battle_4:
       add "battleaction4" xalign 0.5 yalign 0.5
       key "в" action [Hide("pi_battle_4"), Jump("hit_success4")]
       key "В" action [Hide("pi_battle_4"), Jump("hit_success4")]
       key "d" action [Hide("pi_battle_4"), Jump("hit_success4")]
       key "D" action [Hide("pi_battle_4"), Jump("hit_success4")]
       timer 2 action Jump("pi_lose4")


label hit_success4:
    $ Fl.Pause(0.7)
    call screen pi_battle_5 with vpunch
    screen pi_battle_5:
       add "battleaction3" xalign 0.5 yalign 0.5
       key "п" action [Hide("pi_battle_5"), Jump("hit_success5")]
       key "П" action [Hide("pi_battle_5"), Jump("hit_success5")]
       key "g" action [Hide("pi_battle_5"), Jump("hit_success5")]
       key "G" action [Hide("pi_battle_5"), Jump("hit_success5")]
       timer 2 action Jump("pi_lose2")


label hit_success5:
    $ Fl.Pause(0.7)
    call screen pi_battle_6 with vpunch
    screen pi_battle_6:
       add "battleaction6" xalign 0.5 yalign 0.5
       key "т" action [Hide("pi_battle_6"), Jump("hit_success6")]
       key "Т" action [Hide("pi_battle_6"), Jump("hit_success6")]
       key "n" action [Hide("pi_battle_6"), Jump("hit_success6")]
       key "N" action [Hide("pi_battle_6"), Jump("hit_success6")]
       timer 2 action Jump("pi_lose3")


label hit_success6:
    $ Fl.Pause(0.7)
    call screen pi_battle_7 with vpunch
    screen pi_battle_7:
       add "battleaction5" xalign 0.5 yalign 0.5
       key "р" action [Hide("pi_battle_7"), Jump("hit_success7")]
       key "Р" action [Hide("pi_battle_7"), Jump("hit_success7")]
       key "h" action [Hide("pi_battle_7"), Jump("hit_success7")]
       key "H" action [Hide("pi_battle_7"), Jump("hit_success7")]
       timer 2 action Jump("pi_lose4")


label hit_success7:
    $ Fl.Pause(0.7)
    call screen pi_battle_8 with vpunch
    screen pi_battle_8:
       add "battleaction1" xalign 0.5 yalign 0.5
       key "е" action [Hide("pi_battle_8"), Jump("hit_success8")]
       key "Е" action [Hide("pi_battle_8"), Jump("hit_success8")]
       key "t" action [Hide("pi_battle_8"), Jump("hit_success8")]
       key "T" action [Hide("pi_battle_8"), Jump("hit_success8")]
       timer 2 action Jump("pi_lose")


label hit_success8:
    $ Fl.Pause(0.7)
    call screen pi_battle_9 with vpunch
    screen pi_battle_9:
       add "battleaction6" xalign 0.5 yalign 0.5
       key "т" action [Hide("pi_battle_9"), Jump("hit_success9")]
       key "Т" action [Hide("pi_battle_9"), Jump("hit_success9")]
       key "n" action [Hide("pi_battle_9"), Jump("hit_success9")]
       key "N" action [Hide("pi_battle_9"), Jump("hit_success9")]
       timer 2 action Jump("pi_lose4")


label hit_success9:
    $ Fl.Pause(0.7)
    call screen pi_battle_10 with vpunch
    screen pi_battle_10:
       add "battleaction3" xalign 0.5 yalign 0.5
       key "п" action [Hide("pi_battle_10"), Jump("pi_win")]
       key "П" action [Hide("pi_battle_10"), Jump("pi_win")]
       key "g" action [Hide("pi_battle_10"), Jump("pi_win")]
       key "G" action [Hide("pi_battle_10"), Jump("pi_win")]
       timer 2 action Jump("pi_lose2")




label pi_win:
    $ Fl.StopMusic(6)
    $ Fl.AttackScreens(True)
    $ Fl.say(Fl_pib, "ДОБИВАЮЩИЙ!")
    scene bg Fl_ext_square_sunset
    show Fl_light_c 
    with Fl_flash_red
    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    with hpunch
    $ Fl.say(Fl_r, "Звук ломающихся костей донёсся до меня. От чего я получил неимоверное удовольствие.")
    $ Fl.say(Fl_pib, "А-ха-хах! Кто из нас больше БЕЗУМЕЦ? {w}Тот, кто им является, {w}или тот кто напал на него?!")
    $ Fl.say(Fl_r, "Улыбка настоящего психа сверкала на моём лице, ведь ничто так не бодрит днём, как битва при лучах солнца и хруст костей.")
    $ Fl.say(Fl_pib, "Жалкий пионеришка! {w}А ведь ты так уверенно дрался, Мразь!")
    $ Fl.say(Fl_pib, "Ты правда думал, что сможешь одолеть меня?")
    $ Fl.say(Fl_pib, "НА-{w=0.5}СЕ-{w=0.5}КО-{w=0.5}МО-{w=0.5}Е.")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_pib, "Ладно{mn}")
    $ Fl.say(Fl_r, "В окружении гробовой тишины, я попытался собраться с мыслями.")
    $ Fl.say(Fl_th, "А ведь эта кукла столько надежд породила. {w}К слову как и забрала в тот же миг...")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_th, "Но вот вопрос. На, что у него не хватило времени объяснить?")
    $ Fl.say(Fl_pib, "Хотя неважно. Теперь у тебя море времени!")
    $ Fl.say(Fl_r, "Улыбнувшись проговорил я.")
    $ Fl.say(Fl_th, "Пора погулять и выяснить, откуда пришёл данный индивид. {w}Встреча с ним явно пошла мне на пользу.")
    $ Fl.say(Fl_r, "Все это время меня не покидало ощущение слежки. Я отчётливо чувствовал чей-то тяжёлый взгляд на спине.")
    $ Fl.say(Fl_th, "Я ведь не настолько тупой, чтобы не заметить это!")
    $ Fl.say(Fl_r, "Я шёл по площади, высматривая переферийным зрением какую-либо зацепку. {w}Казалось, что я поменялся местами, теперь я - жертва, а наблюдатель - охотник, выжидающий свою добычу.")
    $ Fl.say(Fl_r, "Правда охотником моего наблюдателя сложно назвать, скорее он - хищник. {w}Почему хищник? {w}Потому что от охотника не исходит такой жажды крови!")
    $ Fl.say(Fl_r, "Вся ситуация меня начала напрягать, поэтому я решил действовать. В прямом смысле этого слова.")
    if persistent.Fl_dictionary_8 == False:
        $ Fl.PodskDict()
    $ persistent.Fl_dictionary_8 = True
    $ Fl.say(Fl_pib, "{i}Adieu!{/i}", _with=hpunch)

    $ Fl.PlayMusic("Fl_danger", 1, 4)
    scene bg Fl_ext_square_sunset:
        Fl_run_fast
    $ Fl.say(Fl_r, "Рванув с бешенной скоростью, я принялся бежать. {w}Я принял своего рода тактическое отступление.")
    $ Fl.say(Fl_r, "В голове созревал план то, каким образом я нападу на своего надзирателя.")
    $ Fl.say(Fl_r, "И видимо, увлёкся.")
    $ Fl.say(Fl_pib, "Ч-что?!")
    $ Fl.say(Fl_r, "Я прямо чувствовал поток ветра который нёсся в мою сторону со смертельной скоростью.")
    $ Fl.say(Fl_r, "Быстро, не соображая что происходит, я намеренно упал на землю и перекотился.", _with=hpunch)

    $ Fl.PlaySound("Fl_distanceknifehit", 1, 0, False)
    scene bg Fl_ext_square_sunset
    show Fl_light_c 
    with vpunch
    $ Fl.say(Fl_r, "Поднявшись и вернув себя в прежнее состояние, я посмотрел туда, где чисто теоретически должно оказаться то, что летело в меня.")
    $ Fl.say(Fl_th, "Пролетело сверху{mn} но что и куда?")
    $ Fl.say(Fl_r, "Внимательно осмотрев деревья, я воскликнул.")
    $ Fl.say(Fl_pib, "<Бл*ть>, серьёзно?!")
    $ Fl.say(Fl_r, "Из дерева торчал нож.")
    $ Fl.say(Fl_pib, "Это уже ни в какие ворота...")
    $ Fl.say(Fl_r, "Высчитав траекторию откуда мог прилететь интересный предмет, я повернул голову в сторону кустов, в надежде наконец-то лицезреть обладателя сего изделия.")
    $ Fl.say(Fl_r, "Казалось я должен, сжав кулаки, направиться к таинственному наблюдателю... Но всё не так просто...")
    $ Fl.say(Fl_r, "Я подошёл к дереву и достал оттуда ножик.")
    $ Fl.say(Fl_r, "После чего резко провёл им по своей руке.", _with=Fl_flash_red)
    $ Fl.say(Fl_th, "Пхах, вот это я понимаю - нож!")
    $ Fl.say(Fl_th, "Заточен на отлично! Даже я могу позавидовать!")
    $ Fl.say(Fl_r, "Кровь капала с моей руки постепенно все меньше и меньше.")
    $ Fl.say(Fl_pib, "А у тебя серьёзные намерения я погляжу.")
    $ Fl.say(Fl_pib, "Ну давай же! Выходи! {w}Забери свой ножик!")
    $ Fl.say(Fl_r, "Но никто так и не решился нарушить тишину пионерлагеря.")
    $ Fl.say(Fl_pib, "<С*ка>, если я сказал ЗАБЕРИ! Значит ты {b}ДОЛЖЕН{/b} забрать его у меня!!!", _with=hpunch)
    $ Fl.say(Fl_r, "В порыве эмоций я со всей силы кинул нож обратно. {w}Нож улетел в чащу леса.")
    $ Fl.say(Fl_r, "После чего я на некоторые время решил скрыться.")
    $ Fl.say(Fl_th, "Такие приколы мне в лагере не нужны. {w}Весело - да, но не хочу, что бы в один прекрасный момент мне в спину прилетел нож, поэтому...")
    $ Fl.say(Fl_th, "Стоит всё хорошенько обдумать и снова «тактически» отступить.")
    $ Fl.say(Fl_r, "Скрываться пришлось в моем любимом подземном бункере.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(4)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.DayTime("kira", "night")
    $ Fl.Pause(5.5)


    scene bg Fl_ext_musclub_night2
    show Fl_dust_full
    with Fl_dissolve2
    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Спустя какое-то время я всё же решил вернуться на поверхность и разведать обстановку.")
    $ Fl.say(Fl_pib, "Ах, как же интересно получилось! {w}Пришёл к музклубу с которого всё и начилось!")
    $ Fl.say(Fl_r, "На улице во всю была ночь. {w}Но она была какая-то другая... {w}зловещая.")
    $ Fl.say(Fl_r, "Трудно было сказать от чего именно создавалось такое впечатление. {w}Возможно из-за того что до сих пор лагерь не вернул звуки. {w}А может из-за одинокого фонаря, который первый раз решил взять отдых и оставить меня в окружении тёмного леса.")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_pib, "Интересно, как там наша японочка поживает?")
    $ Fl.say(Fl_kvl, "Скажи, чего ты добиваешься?")
    $ Fl.say(Fl_r, "Неожиданно где-то рядом со мной прозвучал голос.")
    $ Fl.say(Fl_pib, "А-а?")
    $ Fl.say(Fl_r, "Напыщенным тоном выдавил из себя я.")
    $ Fl.say(Fl_kvl, "Чего ты хочешь добиться всем этим?")
    $ Fl.say(Fl_pib, "Кто ты? {w}Нет, хах, мне это даже знать не хочется. С чего мне тебе отвечать?")
    $ Fl.say(Fl_kvl, "Давай оставим все эти прилюдия и представим, что у меня нет имени, и никак не зовут.")
    $ Fl.say(Fl_kvl, "А вот отвечать или нет - сугубо твоё решение. {w}Но я задам тот же вопрос.")
    $ Fl.say(Fl_kvl, "Чего ты хочешь добиться всем этим?")
    $ Fl.say(Fl_pib, "Так просто. Ха-а-а. {w}Раз уж ты никто, то тогда я буду...")
    $ Fl.say(Fl_kvl, "Не утруждай себя. Я и так всё прекрасно знаю.")
    $ Fl.say(Fl_r, "Я почувствовал прилив гнева.")
    $ Fl.say(Fl_pib, "Ты думаешь, если ты где-то прячешь, то я не смогу тебя найти?")
    $ Fl.say(Fl_pib, "Кто тебе вообще давал права меня перебивать и дерзить, урод?!")
    $ Fl.say(Fl_kvl, "Понятно, мне с самого начала не стоило тратить на тебя своё время. Пока.")
    $ Fl.say(Fl_r, "Быстро пораскинув мозгами, я понял, что это может быть интересно.")
    $ Fl.say(Fl_pib, "Стой! {w}Почему я это делаю - ты спрашиваешь? {w}Но вот только что {b}это{/b}?")

    $ Fl.PlayMusic("Fl_atmosphere", 1, 5)
    $ Fl.say(Fl_kvl, "Ты серьёзно? {w}По-твоему, убийства разными изощрёнными способами это нормально?")
    $ Fl.say(Fl_pib, "Заткнись! {w}Ты даже не представляешь, каково мне из-за этих тварей запрограмированных.")
    $ Fl.say(Fl_pib, "Эти твари забрали всё что у меня было!")
    $ Fl.say(Fl_kvl, "Думаешь, они не страдали?")
    $ Fl.say(Fl_pib, "О чём ты?")
    $ Fl.say(Fl_kvl, "Как ты думаешь, каково тебе было бы, если бы тебя расчленяли, вешали, поджигали...")
    $ Fl.say(Fl_pib, "Закрой пасть! {w}Кто ТЫ такой, чтобы упрекать меня в этом?")
    $ Fl.say(Fl_pib, "Из-за них я потерял не только всё, но и свой рассудок!")
    $ Fl.say(Fl_kvl, "Неважно, кто я. {w}Вопрос сейчас тот же, чего ты этим хочешь добиться?")
    $ Fl.say(Fl_kvl, "Может, пора перестать себе врать? {w}Ты уже давно {b}упустил{/b} свой шанс вернуться обратно.")
    $ Fl.say(Fl_pib, "Хахах. Правда что-ли?")
    $ Fl.say(Fl_r, "Истерично посмеиваясь, я продолжил.")
    $ Fl.say(Fl_pib, "Упустил говоришь? {w}Я ненавижу{mn}")

    $ Fl.AttackScreens(True)
    $ Fl.say(Fl_pib, "НЕНАВИЖУ ЭТОТ МИР!", _with=hpunch)
    $ Fl.say(Fl_pib, "Этот лагерь... Специально, сначала показывая и приподнося тебе идеальную иллюзию, он моментально и беспощадно уничтожает её вместе с тем, что у тебя было.")
    $ Fl.say(Fl_kvl, "Только ты сам себе навязал данное мнение, не так ли? {w}Ты не хотел воспринимать реальность. {w}Ты воспринял то, что тебе будет легко принять, что тебе казалось правдой, но ей не является.")
    $ Fl.say(Fl_pib, "Что ты имеешь виду?")
    $ Fl.say(Fl_kvl, "Кристина не была иллюзией лагеря. {w}Просто ей в отличии от тебя удалось вернуться в свою реальность, а ты застрял в этих циклах по своей вине.")
    $ Fl.say(Fl_kvl, "Вспомни ты же сам согласился на этот ад.")
    $ Fl.say(Fl_th, "Что...")
    $ Fl.say(Fl_r, "У меня сильно кольнуло в голове, настолько сильно, что по ощущением сравнимо разве что только с ударом арматуры по голове...")
    $ Fl.say(Fl_r, "Воспоминания вновь проносились в голове со скоростью света, не оставляя и секунду на передышку.")
    $ Fl.HideScreens(_with=Fl_fast)


    scene bg Fl_black with Fl_flash

    $ Fl.DayTime("rain", "night")

    $ Fl.Pause(2.5)
    scene cg Fl_dead_gg_wosp
    $ persistent.Fl_photo_pallery_10 = True
    show Fl_prolog_dream
    with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_gg, "...Я согласен. {w}Это малая жертва за её жизнь.")
    $ Fl.say(Fl_ktv, "Пускай будет по-твоему...")
    $ Fl.HideScreens(_with=Fl_fast)


    scene bg Fl_black with Fl_flash

    $ Fl.DayTime("kira", "night")

    scene bg Fl_ext_musclub_night2
    show Fl_dust_full
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Теперь я вспомнил. {w}Частично вспомнил.")
    $ Fl.say(Fl_r, "В ту ночь что-то произошло. {w}И Кристина была на грани смерти...")
    $ Fl.say(Fl_th, "КАК?! {w}Как же так?!", _with=hpunch)
    $ Fl.say(Fl_r, "Голова была перегружена. {w}В один момент вспомнить слишком много. У меня начала кружиться голова и темнело в глазах.")
    $ Fl.say(Fl_r, "Вместо обычных мыслей в голове образовывалась каша, и я медленно начал терять сознание, падая в бездну.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.DayTime("prologue", "night")
    $ Fl.Pause(4.0)

    scene bg Fl_pyst_ch with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Меня окружила темнота. Нет, темнота стало одним целым со мной. {w}К своему сожалению, я так и не научился контролировать себя в порыве эмоций.")
    
    $ Fl.Pause(1.0)
    $ Fl.say(Fl_th, "Скажи, чего ты добиваешься{mn}")
    $ Fl.say(Fl_r, "Интересно, смог бы я начать всё с начала? {w}Вернуть всё как было? {w}Жить с чистого листа?")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_th, "Безумие - это искусство, а безумие в совокупности со смертью - искусство гениальное. {w}Ведь быть одновременно безумным и гениальным не каждому дано.")
    $ Fl.say(Fl_r, "Наверное каждый назовёт меня безумцем, психом, сумашедшим и прочими синонимами.")
    $ Fl.say(Fl_th, "Этого ли я на самом деле хотел?")

    scene bg Fl_pyst_red with Fl_dissolve3

    $ Fl.say(Fl_th, "Сумасшедшие возвращают себе рассудок, а нормальные обезумевают.")
    $ Fl.say(Fl_th, "Но тогда логично, что когда ты вернёшь себе рассудок, ты станешь безумцем, потому что ты вновь станешь нормальным, а не сумасшедшим.")
    $ Fl.say(Fl_th, "Интересная мысль.")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_th, "Чем же на самом деле является «Совёнок?». Для чего он даёт такие надежды?")
    $ Fl.say(Fl_th, "Ведь не бывает такого, когда ты получаешь всё без каких-либо жертв и условий.")
    $ Fl.say(Fl_th, "Блюдечко с голубой каёмочкой, если прибегнуть к фразеологизмам.")
    $ Fl.say(Fl_th, "Если так, то что хочет от меня «Совёнок?» {w}Чтобы я изменился? {w}Или осознал то, чего раньше не мог?")
    $ Fl.say(Fl_th, "Бред, за чем ему это?")
    $ Fl.say(Fl_th, "Таким образом, это самое {b}условие{/b} не раскрывается, что вполне логично. {w}Такие подарки за просто так никому не отдадут, особенно с такими фигурами.")
    $ Fl.say(Fl_th, "Каждый может услышать слова о том, как кому-то было больно, но только прочувствовав это однажды, он по-настоящему поймёт, каково это было на самом деле.")
    $ Fl.say(Fl_th, "Так было/будет всегда.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(5)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.DayTime("night", "night")
    $ Fl.Pause(3.0)

    scene bg Fl_ext_musclub_night2
    show Fl_dust_full
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Понемногу я пришёл в себя.")

    $ Fl.PlayAmbience("Fl_camp_center_night", 1, 4) 
    $ Fl.say(Fl_th, "Что только что произошло?")
    $ Fl.say(Fl_pi, "Эй! Ты ещё тут?")
    $ Fl.say(Fl_r, "Попытался я закричать, но едва не закашлял.")
    $ Fl.say(Fl_r, "Я собирался вновь крикнуть, как вдруг осознал что лагерь снова ожил. {w}Звуки природы вернулись.")
    $ Fl.say(Fl_pi, "Не может быть.")
    $ Fl.say(Fl_pi, "Нет, стоп! Сейчас есть кое-что поважнее.")
    $ Fl.say(Fl_r, "Тот разговор не выходил из моей головы. {w}Кто это был? Откуда он взялся? {w}Чего он пытался добиться этими вопросами?")
    $ Fl.say(Fl_r, "Однако, когда теперь я многое вспомнил, мой гнев{mn} Нет, моё {b}безумие{/b}, потеряло смысл? {w}Я чувствовал, как мой рассудок хоть частично, но стал восстанавливаться, заставив гнев сойти на нет.")
    $ Fl.say(Fl_pi, "Кто же ты на самом деле...")
    $ Fl.say(Fl_r, "Ночь давно охватила пионерлагерь. И только сейчас я кое-что почувствовал...")
    $ Fl.say(Fl_th, "Холодно.")
    $ Fl.say(Fl_r, "За столь большой срок я даже перестал думать о таких вещах как холод. {w}Когда-то перестал.")
    $ Fl.say(Fl_th, "Раз я уже у музкружка, значит тут и переночую.")
    $ Fl.say(Fl_r, "Копаясь в событиях за сегодняшний день, я поплёлся к веранде.")
    $ Fl.say(Fl_th, "Интересно, сколько времени уже прошло?")
    $ Fl.say(Fl_r, "Я аккуратно открыл дверцу клуба, которая оказалась незапертой.")
    $ Fl.StopAmbience(4)
    $ Fl.HideScreens(_with=Fl_fast)


    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
    scene bg Fl_int_musclub_night with Fl_effect_5

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Меня вновь встретил уютный уголок музыки, который при свете ночи выглядел совсем иначе.")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.AttackScreens()
    $ Fl.say(Fl_r, "Меня ударили в спину. {w}Это был довольно сильный удар с ноги, но не для меня. {w}Я перетерпел столько боли, что такие удары стали незначительны для меня.")
    $ Fl.say(Fl_pi, "Да почему вы так все любите бить-то сразу?")
    $ Fl.say(Fl_r, "Я обернулся.")

    $ Fl.PlayMusic("Fl_reeducated", 1, 5)
    show mi sad pioneer5 with Fl_dissolve1

    $ Fl.say(Fl_r, "Сзади стояла Мику. На её лице читалось непонимание всего происходящего и отчаяние.")
    $ Fl.say(Fl_mi, "К-кто ты?")
    $ Fl.say(Fl_r, "Подавлено спросила пионерка.")
    $ Fl.say(Fl_pi, "Знаешь, похоже, что я уже сам не знаю точно, кто я...")
    $ Fl.say(Fl_th, "Она не ожидала что я отвечу.")
    $ Fl.say(Fl_th, "Ну да{mn} Было бы логичнее для неё закончить диалог сразу после первого вопроса парочкой ударов. Но не в этот раз...")
    $ Fl.say(Fl_mi, "Ты один из {b}них{/b}?")
    $ Fl.say(Fl_pi, "Из них? Ты про других странных пионеров, которые похожи на меня?")
    $ Fl.say(Fl_mi, "Несовсем{mn} Почему? П-почему ты...")
    $ Fl.say(Fl_pi, "Не пытаюсь убить тебя или сделать что-то ужасное?")
    $ Fl.say(Fl_pi, "Прости, не могу дать ответ на этот вопрос. {w}Скажем так, я уже точно не понимаю, чего я хочу и кем я являюсь.")
    $ Fl.say(Fl_r, "Опуская подробности о {b}нём{/b} и о том, чем ранее я занимался.")
    $ Fl.say(Fl_mi, "Кто о-они?")
    $ Fl.say(Fl_r, "Спросила Мику заикаясь.")
    $ Fl.say(Fl_pi, "Считай, что они - это отбросы, которые пытаются{mn} Они? Их несколько что ли?!")
    $ Fl.say(Fl_th, "Господи, как я сразу не заметил? {w}Похоже, за это время совсем мозги в кашу превратились.")
    $ Fl.say(Fl_mi, "Ч-человека четыре.")
    $ Fl.say(Fl_th, "Четыре человека? Я наблюдал за свое время только троих, и то думал, что один и тот же два раза приходил. {w}Получается, что это не так... Их больше?")
    $ Fl.say(Fl_th, "Тут явно что-то не так!")
    $ Fl.say(Fl_pi, "Какой сейчас день? Я имею в виду, сейчас же последняя неделя. {w}Какой по счету день этой недели?")
    
    $ Fl.Pause(1.5)
    $ Fl.say(Fl_mi, "Третий день, первой недели.")
    $ Fl.say(Fl_th, "Но этого не может быть! Меня забросило в другой лагерь? {w}Чёрт, все интереснее и интереснее...")

    show mi cry pioneer4 with Fl_fast

    $ Fl.say(Fl_mi, "Они{mn} Они убили всех!")
    $ Fl.say(Fl_r, "На глазах пионерки выступили слёзы. Она больше не смогла сопротивляться.")
    $ Fl.say(Fl_r, "Я много раз видел слёзы. {w}Достаточно много, чтобы больше не чувствовать их страдания.")
    $ Fl.say(Fl_r, "Но говоря обо мне, все это время видеть слёзы именно из-за себя, из-за того, что ты убивал, причинял боль... {w}Вошло в привычку.")
    $ Fl.say(Fl_r, "А здесь другая ситуация: cтрадают не из-за меня, но по той же причине. {w}Тогда почему я чувствую сострадание?")
    $ Fl.say(Fl_r, "Зачем оно мне? Спустя годы я потерял рассудок и всё, что связано вместе с ним.{w} На данный момент я машина для убийств.")
    $ Fl.say(Fl_r, "Но зачем{mn} Зачем пришёл так называемый {b}Некто{/b}? {w}Ради чего меня перебросили в другой лагерь? {w}Каким образом я смог вернуть частично рассудок, взяв под контроль своё тело и разум.")
    $ Fl.say(Fl_th, "Какой в этом смысл...")

    hide mi cry pioneer4 with Fl_dissolve1

    $ Fl.say(Fl_r, "Без каких-либо слов ко мне подошла плачущая Мику и обняла.")
    $ Fl.say(Fl_r, "Меня добили. {w}Добили и уничтожили на собственном поле.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.DayTime("prologue", "night")

    scene bg Fl_pyst_ch with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Поэтому только музыка заставляет меня оставить реальность далеко позади. Забавно, что в прошлом мире я тоже благодаря музыки смог сбежать от всех проблем.")
    $ Fl.say(Fl_th, "Музыкальный клуб, да?")
    $ Fl.say(Fl_r, "Неосознанно этот клуб стал моим неким укрытием ото всех, даже от Мику.")
    $ Fl.say(Fl_r, "Мику, самая болтливая пионерка. Я терпеть не могу её быструю речь, а её лучезарная улыбка меня бесит. {w}Дередере, как же меня раздражают вот такие яркие и невинные личности...")
    $ Fl.say(Fl_r, "Но, даже в таком раздраженном состоянии мне всегда нравилась её музыка.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.DayTime("night", "night")

    scene bg Fl_int_musclub_night with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Но зачем она это сделала? Она же меня даже не знает? {w}А, ну точно, я догадываюсь почему...")
    $ Fl.say(Fl_r, "Без каких-либо раздумий, я обнял девушку в ответ.")
    $ Fl.say(Fl_r, "Она такого не ожидала, и я такого не ожидал. {w}Сейчас мой поступок из разряда вон выходящего.")
    $ Fl.say(Fl_th, "И о чём я только думаю...")
    $ Fl.say(Fl_r, "Мне стало хреново. Появилось чувство вины и желание исправить... Cебя?")
    $ Fl.say(Fl_th, "Боже, настолько я пал. {w}Я даже не смог удержаться поддержать её в такую минуту.")
    $ Fl.say(Fl_r, "Мы стояли молча в обнимку в центре комнаты при свете луны.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.PlaySound("Fl_pause_time", 1.0, 2, False)
    scene Fl_pause
    with Fl_effect_time_pause

    $ Fl.Pause (3.5)
    scene bg Fl_black with Fl_dissolve2
    $ Fl.Pause (1.5)

    scene bg Fl_int_musclub_night with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Хахаха. Это так забавно, надо же было представиться именно так.")
    $ Fl.say(Fl_th, "Хватит с меня.")
    $ Fl.say(Fl_r, "Я вышел из раздумий и задал единственно верный вопрос в данной ситуации.")
    $ Fl.say(Fl_pi, "Ты в порядке?")
    $ Fl.say(Fl_r, "Ответа не последовало.")
    $ Fl.say(Fl_pi, "Эм, Мику?")
    $ Fl.say(Fl_r, "Я внимательней присмотрелся...")
    $ Fl.say(Fl_pi, "Чёрт, уснула.")
    $ Fl.say(Fl_r, "Ноги перерстали держать хрупкое тело пионерки. Теперь она держалась только на мне, используя моё плечо как подушку.")
    $ Fl.say(Fl_r, "Она спокойно спала с улыбкой на лице. Даже не представляя, что за монстр стоит возле неё.")
    $ Fl.say(Fl_r, "Я аккуратно её поднял и уложил на пол, подстелив под голову что-то похожее на подушку из кладовой.")
    $ Fl.say(Fl_r, "Ночь была слишком холодной для пионерлагеря. Поэтому я отыскал ещё и одеяло. В той же кладовой.")
    $ Fl.say(Fl_r, "Я накрыл Мику одеялом.")
    $ Fl.say(Fl_pi, "Спокойной ночи.")
    $ Fl.StopMusic(5)
    $ Fl.HideScreens(_with=Fl_fast)


    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
    scene bg Fl_ext_path_dark
    show Fl_dust_full
    with Fl_effect_5

    $ Fl.PlayAmbience("Fl_forest_night", 1, 4)
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Оставив Мику одну нежиться в своей «кроватки». Я решил прогуляться и подышать свежим воздухом.")
    $ Fl.say(Fl_r, "За все предыдущие смены я не спал ночью, из-за чего это уже вошло в привычку. В отдыхе я не нуждался, тело не успевало измотаться за такой короткий срок.")
    $ Fl.say(Fl_pi, "Да уж{mn} Жизнь и правда странная штука, с утра я пребывал в стадии безумия. А сейчас обмнимаюсь с пионерками и любуюсь звуками природы.")
    $ Fl.say(Fl_th, "Что дальше? {w}Искать ответы, разбираться во всей этой лагерной дичи, которая произошла за сегодня? {w}Наверное, так и есть.")
    $ Fl.say(Fl_pi, "Тогда ночная прогулка по лесу, неплохая идея.")
    $ Fl.say(Fl_r, "Я бросил взгляд через плечо.")
    $ Fl.say(Fl_th, "Правда, было бы плохо, если её тут убьют пока я где-то шастаю по чаще леса. {w}Поэтому запереть её на ключ было правильным решением.")
    $ Fl.say(Fl_th, "А с другой стороны, если они узнают, что она там, то они запросто могут разбить окно и расправиться с ней.")
    $ Fl.say(Fl_th, "Ай, пофиг. Мне всё равно плевать на её жизнь, даже после того что было. Так что у неё одна надежда на удачу. Да и кому...")
    $ Fl.say(Fl_lnp, "Ой!", _with=hpunch)
    $ Fl.say(Fl_th, "Что?")
    $ Fl.say(Fl_r, "Почувствовав неладное, я обернулся к источнику.")
    $ Fl.StopAmbience(5)

    scene bg Fl_ext_path2_dark 
    show Fl_dust_full
    with pushright

    $ Fl.say(Fl_pi, "Твою мать...")
    $ Fl.PlayMusic("Fl_powerless", 1, 4)

    show ln scary with Fl_dissolve1

    $ Fl.say(Fl_th, "Даже я такого не ожидал.")
    $ Fl.say(Fl_lnd, "Что? Ты меня не узнал что ли? Это же я - Лена!")
    $ Fl.say(Fl_lnd, "Хахах. Привет, Ян! Давно не виделись! Где ты пропадал всё это время?")
    $ Fl.say(Fl_pi, "Ты <бл*ть> вообще кто? Я тебя первый раз в жизни вижу!")
    $ Fl.say(Fl_lnd, "Ой-ой! Как же это больно слышать, Ян. Ты так со мной груб. {w}Ты и правда забыл меня?")
    $ Fl.say(Fl_lnd, "Ну ничего! Сейчас я разберусь с {b}этими,{/b} а после ты станешь моим!")
    $ Fl.say(Fl_th, "Мда{mn} Крышу мадам знатно снесло.")
    $ Fl.say(Fl_pi, "Я так не думаю.")
    $ Fl.say(Fl_lnd, "Хахах. Ян, ты собираешься встать на пути нашего общего счастья?")
    $ Fl.say(Fl_lnd, "Тогда, может поиграем, любимый?")
    $ Fl.say(Fl_pi, "Не, давай без меня. Чувствую это плохо для меня закончиться. Так что не унывай, удачи!")
    $ Fl.say(Fl_r, "Я уже собирался развернуться и уйти...")
    $ Fl.say(Fl_lnd, "О не-ет. Ты просто так не уйдёшь!")
    $ Fl.say(Fl_r, "В голове появилась одна занимательная идея.")
    $ Fl.say(Fl_pi, "Вот как! Тогда давай поиграем. {w}Догоняй!")
    $ Fl.say(Fl_lnd, "Ты серьёз{break}")
    $ Fl.HideScreens()


    $ Fl.PlaySound("Fl_run", 1, 0, True)
    scene bg Fl_ext_path2_dark:
        Fl_run_fast
    scene bg Fl_ext_path_dark with Fl_dissolve2:
        Fl_run_fast
    scene bg Fl_ext_path2_dark with Fl_dissolve2:
        Fl_run_fast
    scene bg Fl_ext_path_dark with Fl_dissolve2:
        Fl_run_fast
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Прошло явно не пять минут с тех пор как мы начали забег.")
    $ Fl.say(Fl_th, "Да, когда ты, <с*ка>, выдохнешься?!")
    $ Fl.StopMusic(15)
    $ Fl.say(Fl_r, "Ладно, подбегаем к назначенному месту!")
    $ Fl.StopSound(2)
    scene bg Fl_ext_path2_dark with Fl_dissolve1

    $ Fl.say(Fl_th, "Где она?!")

    $ Fl.PlayAmbience("Fl_forest_night", 1, 4)
    $ Fl.say(Fl_lnd, "И куда ты собрался?")
    $ Fl.say(Fl_r, "Эти слова она произнесла каким-то неестественным голосом.")

    show ln scary with Fl_fast

    $ Fl.say(Fl_th, "Чёрт!")
    $ Fl.say(Fl_r, "Существо, что отдалёно напоминало Лену, стояло от меня в пару шагов.")
    $ Fl.say(Fl_pi, "Куда, куда! Подальше от тебя!")
    $ Fl.say(Fl_lnd, "Хахаах. Ян, так не пойдёт!")
    $ Fl.say(Fl_th, "А обвалиться-то земля где-то тут должна.")
    $ Fl.say(Fl_r, "Я начал пятиться назад.")
    $ Fl.say(Fl_lnd, "Бесполезно.")

    show ln scary:
        ease 1.5 zoom 1.2 

    $ Fl.say(Fl_r, "Она начала стремительно приближаться.")
    with vpunch
    with Fl_flash
    $ Fl.PlaySound4("Fl_simon_fall_2", 1, 0, False)

    hide ln scary with vpunch

    $ Fl.say(Fl_r, "Земля обвалилась, и {b}она{/b} вместе с ней.")
    $ Fl.say(Fl_pi, "Уж не знаю кто ты или что, но{break2}")
    $ Fl.StopAmbience(4)
    $ Fl.PlaySound4("Fl_simon_fall_2", 1, 0, False)
    scene bg Fl_black with vpunch

    $ Fl.say(Fl_r, "Лагерь никого не пощадил и забрал под землю так же и меня.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.PlaySound("Fl_pause_time", 1.0, 2, False)
    scene Fl_pause
    with Fl_effect_time_pause

    $ Fl.Pause (3.5)
    scene bg Fl_black with Fl_dissolve2
    $ Fl.Pause (1.5)

    scene bg Fl_int_catacombs_entrance_new with Fl_dissolve2
    $ Fl.PlayAmbience("Fl_catacombs", 1, 4)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_pi, "Т-тц! Где я?")
    $ Fl.say(Fl_r, "Протянул я.")
    $ Fl.say(Fl_th, "А ну да{mn} Точно...")
    $ Fl.say(Fl_th, "Попробовать встать? {w}Нет, скорее хотя бы пошевелиться.")
    $ Fl.say(Fl_r, "Проверка прошла более чем успешно.")
    $ Fl.say(Fl_th, "Так шевелиться я могу. Особых травм не наблюдается.")
    $ Fl.say(Fl_th, "Интересно только одно: я упал, по сути, неподалёку от {b}неё{/b}, что само по себе уже нехорошо.")
    $ Fl.say(Fl_th, "Не хотелось бы встретиться с этой тварью снова.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_th, "Ладно, хотя бы знаю куда идти, это уже радует. {w}Да и фонарик у меня всегда под рукой.")
    $ Fl.say(Fl_r, "Так и началось мое небольшое путешествие по тоннелям шахт.")
    $ Fl.HideScreens(_with=Fl_dissolve1)

    $ Fl.Pause (3.5)


    scene bg Fl_int_mine with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_pi, "Вот и поиграли...")
    $ Fl.say(Fl_r, "Почти бесшумно произнес я.")
    $ Fl.say(Fl_r, "Конечно назвать прогулку по шахте путешествием трудно. {w}Весь путь занял у меня от силы минут 10, а может и меньше.")
    $ Fl.say(Fl_th, "По моим расчётам выход должен быть через пару минут.")
    $ Fl.say(Fl_lnd, "Какая удача? Хахах.")
    $ Fl.StopAmbience(6)

    $ Fl.say(Fl_r, "Я медленно навёл луч фонаря в глубь тоннеля.")
    $ Fl.say(Fl_r, "Свет озарил тьму и в далеке нарисовалась следующая картина. {w}Уже знакомая мне Лена с окровавленным ножом приближалась ко мне.")


    scene cg Fl_lena_catacombs with Fl_dissolve2
    $ persistent.Fl_photo_pallery_12 = True
    $ Fl.DayTime("kira", "night")


    $ Fl.say(Fl_lnd, "Хах. Спокойной ночи, мой принц!")
    $ Fl.HideScreens()
    jump night_battle




label night_battle:
    scene cg Fl_lena_catacombs with Fl_fast
    $ Fl.PlayMusic("Fl_blood_sugar", 1, 0)
    call screen shadow_battle with Fade(0.10, 0.15, 0, color="ffffff")
    screen shadow_battle:
       add "shadowaction" xalign 0.5 yalign 0.5
       key "ь" action [Hide("shadow_battle"), Jump("night_success1")]
       key "Ь" action [Hide("shadow_battle"), Jump("night_success1")]
       key "M" action [Hide("shadow_battle"), Jump("night_success1")]
       key "m" action [Hide("shadow_battle"), Jump("night_success1")]
       timer 1.0 action Jump("lena_lose")




label lena_lose:
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_lnd, "Как жаль, дорогой!")
    $ Fl.say(Fl_lnd, "Но никто не может помешать нашему счастью! {w}Даже ты сам, Ян!")
    $ Fl.say(Fl_r, "Её глаза воспылали ярким пламенем.")

    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    $ Fl.say(Fl_r, "Резкое движение и нож уже был прямо в моём сердце.", _with=Fl_flash_red)
    $ Fl.say(Fl_r, "Я закричал, по крайней мере, пытался...")
    with vpunch
    with hpunch
    show Fl_blood_eff with Fl_flash_red
    $ Fl.StopMusic(7)
    $ Fl.say(Fl_r, "Боль была невыносимая, словно меня пронзили насквозь, а после совершили это ещё множество раз.")
    $ Fl.say(Fl_r, "Холод подступал ко мне...")
    $ Fl.say(Fl_r, "Лена нагнулась и страстно поцеловала меня в губы, прошептав мне сладким голосом.")
    $ Fl.say(Fl_lnd, "Милый...")
    $ Fl.Pause (1.5)
    $ Fl.HideScreens(_with=Fl_fast)
    scene bg Fl_balck with Fl_dissolve2
    jump pi_say_2


label pi_say_2:
    $ Fl.Pause (5.0)
    show text "{font=font/Fl_mainmenu.ttf}{size=55}Боже ты такой жалкий...{/size}{/font}"
    with Fl_dissolve1

    $ Fl.Pause (3.0)
    show text "{font=font/Fl_mainmenu.ttf}{size=55}Я не позволю тебе просто так слиться.{/size}{/font}"
    with Fl_dissolve1

    $ Fl.Pause (3.0)
    show text "{font=font/Fl_mainmenu.ttf}{size=55}Поэтому будь добр, сделай так как надо!{/size}{/font}"
    with Fl_dissolve1
    jump night_battle




label night_success1:
    call screen shadow_battle1 with Fade(0.10, 0.15, 0, color="ffffff")
    screen shadow_battle1:
       add "shadowaction1" xalign 0.5 yalign 0.5
       key "k" action [Hide("shadow_battle1"), Jump("night_success2")]
       key "K" action [Hide("shadow_battle1"), Jump("night_success2")]
       key "Л" action [Hide("shadow_battle1"), Jump("night_success2")]
       key "л" action [Hide("shadow_battle1"), Jump("night_success2")]
       timer 1.2 action Jump("lena_lose")


label night_success2:
    call screen shadow_battle2 with Fade(0.10, 0.10, 0, color="ffffff")
    screen shadow_battle2:
       add "shadowaction4" xalign 0.5 yalign 0.5
       key "J" action [Hide("shadow_battle2"), Jump("night_success3")]
       key "j" action [Hide("shadow_battle2"), Jump("night_success3")]
       key "О" action [Hide("shadow_battle2"), Jump("night_success3")]
       key "о" action [Hide("shadow_battle2"), Jump("night_success3")]
       timer 1.2 action Jump("lena_lose")


label night_success3:
    call screen shadow_battle3 with Fade(0.10, 0.10, 0, color="ffffff")
    screen shadow_battle3:
       add "shadowaction3" xalign 0.5 yalign 0.5
       key "Y" action [Hide("shadow_battle3"), Jump("night_success4")]
       key "y" action [Hide("shadow_battle3"), Jump("night_success4")]
       key "Н" action [Hide("shadow_battle3"), Jump("night_success4")]
       key "н" action [Hide("shadow_battle3"), Jump("night_success4")]
       timer 1.2 action Jump("lena_lose")


label night_success4:
    call screen shadow_battle4 with Fade(0.10, 0.10, 0, color="ffffff")
    screen shadow_battle4:
       add "shadowaction2" xalign 0.5 yalign 0.5
       key "P" action [Hide("shadow_battle4"), Jump("night_success5")]
       key "p" action [Hide("shadow_battle4"), Jump("night_success5")]
       key "З" action [Hide("shadow_battle4"), Jump("night_success5")]
       key "з" action [Hide("shadow_battle4"), Jump("night_success5")]
       timer 1.2 action Jump("lena_lose")


label night_success5:
      call screen shadow_battle5 with Fade(0.10, 0.10, 0, color="ffffff")
      screen shadow_battle5:
       add "shadowaction5" xalign 0.5 yalign 0.5
       key "V" action [Hide("shadow_battle5"), Jump("night_success6")]
       key "v" action [Hide("shadow_battle5"), Jump("night_success6")]
       key "М" action [Hide("shadow_battle5"), Jump("night_success6")]
       key "м" action [Hide("shadow_battle5"), Jump("night_success6")]
       timer 1.2 action Jump("lena_lose")


label night_success6:
      call screen shadow_battle6 with Fade(0.10, 0.10, 0, color="ffffff")
      screen shadow_battle6:
       add "shadowaction6" xalign 0.5 yalign 0.5
       key "C" action [Hide("shadow_battle6"), Jump("night_success7")]
       key "c" action [Hide("shadow_battle6"), Jump("night_success7")]
       key "С" action [Hide("shadow_battle6"), Jump("night_success7")]
       key "с" action [Hide("shadow_battle6"), Jump("night_success7")]
       timer 1.2 action Jump("lena_lose")


label night_success7:
      call screen shadow_battle7 with Fade(0.10, 0.10, 0, color="ffffff")
      screen shadow_battle7:
       add "shadowaction7" xalign 0.5 yalign 0.5
       key "L" action [Hide("shadow_battle7"), Jump("night_success8")]
       key "l" action [Hide("shadow_battle7"), Jump("night_success8")]
       key "Д" action [Hide("shadow_battle7"), Jump("night_success8")]
       key "д" action [Hide("shadow_battle7"), Jump("night_success8")]
       timer 1.2 action Jump("lena_lose")


label night_success8:
      call screen shadow_battle8 with Fade(0.10, 0.10, 0, color="ffffff")
      screen shadow_battle8:
       add "shadowaction2" xalign 0.5 yalign 0.5
       key "P" action [Hide("shadow_battle8"), Jump("night_success9")]
       key "p" action [Hide("shadow_battle8"), Jump("night_success9")]
       key "З" action [Hide("shadow_battle8"), Jump("night_success9")]
       key "з" action [Hide("shadow_battle8"), Jump("night_success9")]
       timer 1.2 action Jump("lena_lose")


label night_success9:
      call screen shadow_battle9 with Fade(0.10, 0.10, 0, color="ffffff")
      screen shadow_battle9:
       add "shadowaction1" xalign 0.5 yalign 0.5
       key "K" action [Hide("shadow_battle9"), Jump("night_success10")]
       key "k" action [Hide("shadow_battle9"), Jump("night_success10")]
       key "Л" action [Hide("shadow_battle9"), Jump("night_success10")]
       key "л" action [Hide("shadow_battle9"), Jump("night_success10")]
       timer 1.2 action Jump("lena_lose")


label night_success10:
      call screen shadow_battle10 with Fade(0.10, 0.10, 0, color="ffffff")
      screen shadow_battle10:
       add "shadowaction4" xalign 0.5 yalign 0.5
       key "J" action [Hide("shadow_battle10"), Jump("nightcatacombs_win")]
       key "j" action [Hide("shadow_battle10"), Jump("nightcatacombs_win")]
       key "О" action [Hide("shadow_battle10"), Jump("nightcatacombs_win")]
       key "о" action [Hide("shadow_battle10"), Jump("nightcatacombs_win")]
       timer 1.2 action Jump("lena_lose")




label nightcatacombs_win:
    $ Fl.ShowScreens()
    $ Fl.say(Fl_r, "После долгих уклонений мы оба выдохлись.", _with=hpunch)
    $ Fl.say(Fl_th, "Чёрт!")
    $ Fl.say(Fl_th, "Что же делать?{w} Без всяких сомнений кулаки против ножа будут бесполезны.")
    $ Fl.say(Fl_lnd, "Как побегал, дорогой? Вымотался наверное?")
    $ Fl.say(Fl_r, "Мне стало смешно и я рассмеялся что есть силы.")
    $ Fl.say(Fl_lnd, "Хах? Тебе весело? Я хочу присоединиться!")
    $ Fl.say(Fl_r, "Кулаки против ножа бесполезны, но ведь про ноги никто ничего не говорил.")
    $ Fl.say(Fl_th, "Хех. Какой это бой за сегодня? {w}Я что-то сбился со счёту.")
    $ Fl.say(Fl_r, "Она совершила выпад и мимолётно проскачила возле меня.")

    $ Fl.AttackScreens(True)
    $ Fl.say(Fl_r, "Я только и успел отскачить.")
    $ Fl.say(Fl_pi, "А ты быстрая!")
    $ Fl.say(Fl_pi, "НО НЕДОСТАТОЧНО!")
    $ Fl.say(Fl_r, "Лена ничего не ответила, а только покрутила нож в своей руке.")
    $ Fl.say(Fl_th, "Ну держись, Ленуся!")
    $ Fl.say(Fl_r, "Ненормальная жажда крови проснулась во мне и началась настоящая битва... {w}Битва безумцев.")
    $ Fl.say(Fl_r, "Она снова совершила рывок в мою сторону.")
    $ Fl.say(Fl_r, "Мое тело двигалось само по себе.{w} Увернувшись от её атаки вправо, я совершил удар ногой прямо в голову.")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    with vpunch
    $ Fl.say(Fl_r, "Лена пошатнулась, но в один миг нанесла удар ножом прямо в кисть правой руки.")

    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    $ Fl.say(Fl_r, "Посмотрев на правую кисть, лишь произнёс.")
    $ Fl.say(Fl_pi, "И это всё?")
    $ Fl.say(Fl_r, "Не раздумывая я совершил удар левой рукой, затем изо всех сил сразу же ногой в туловище.")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    with hpunch
    $ Fl.say(Fl_th, "До сих пор держишься...")
    $ Fl.say(Fl_pi, "Да откуда ты вообще взялась, {b}тварь{/b}?!")
    $ Fl.say(Fl_lnd, "Ах, м-нне приятно, ч-то ты спрос-сил!")
    $ Fl.say(Fl_lnd, "Н-но, будет неинтересно, если я тебе расскажу!")
    $ Fl.say(Fl_lnd, "А СЕЙЧАС ПРИМИ МОЮ ЛЮБОВЬ, {b}МИЛЫЙ{/b}!")

    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    $ Fl.say(Fl_r, "Нож впился в плечо как змея.", _with=Fl_flash_red)

    $ Fl.AttackScreens(True)
    $ Fl.say(Fl_r, "Я заорал от сильной боли, отпрыгнув в сторону, затем жадно посмотрел на своего оппонента по безумию.", _with=hpunch)
    $ Fl.say(Fl_lnd, "Кстати, как там Мику? Наверное мирно спит. {w}Ах, я так ей завиду, вот бы обо мне Ян так же заботился!")
    $ Fl.say(Fl_r, "Она рассмеялась.")
    $ Fl.say(Fl_r, "От таких перепадов эмоций мне стало сносить крышу...")
    $ Fl.say(Fl_r, "У меня вырвался истерический смех.")
    $ Fl.say(Fl_r, "Собрав все силы которые у меня были я нанёс фатальный удар.")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    scene bg Fl_black with hpunch
    $ Fl.say(Fl_r, "Безумный смех разнёся по всем уголкам шахты.")
    $ Fl.say(Fl_r, "Она не смогла увернуться.")
    $ Fl.say(Fl_r, "Искажённая весёлой улыбкой Лена пала. {w}Скорее всего, погибла. {w}Не став проверять я стал поскорее выбираться.")
    $ Fl.StopMusic(7)
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause (3.5)
    $ Fl.DayTime("night", "night")
    $ Fl.Pause (1.5)


    scene bg Fl_int_mine with Fl_dissolve2
    $ Fl.PlayAmbience("Fl_catacombs", 1, 4)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Немного придя в себя, я смог стабилизировать своё состояние, оставив своё безумие на второй план.")
    $ Fl.say(Fl_th, "Нужно в медпункт...")
    $ Fl.say(Fl_r, "Плечо и кисть руки истекали кровью, а бордово-красные ручейки красочно переплетались и стекали к концу запястья. {w}Тепло, которое создавала кровь, помогало мне двигаться вперёд и не отключиться на ровном месте.")

    scene bg Fl_int_mine_exit_night_light with Fl_dissolve2

    $ Fl.say(Fl_th, "Твою мать! {w}<С*ка>, <с*ка>! Как же больно!")
    $ Fl.say(Fl_th, "Обычно после таких ран, я ждал своей смерти и не парился. {w}Но сейчас во чтобы то ни стало нельзя умирать!")
    $ Fl.say(Fl_th, "А может после этого цикла я вообще не возрождусь?")
    $ Fl.say(Fl_r, "Во время того как я думал, я выбирался из шахты проверенным путём, который выходит на площадь.")

    scene bg Fl_ext_square_night2
    show Fl_dust_full
    with Fl_effect_1
    $ Fl.PlayAmbience("Fl_camp_center_night", 1, 8)
    $ Fl.say(Fl_th, "Да бред это всё. {w}Я уверен, что если погибну, то снова окажусь здесь. {w}Наверное{mn}")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_th, "Она упоминала Мику... {w}неужели она в курсе? {w}А что насчет {b}других{/b}?")
    $ Fl.say(Fl_th, "Я должен проверить...")
    $ Fl.say(Fl_r, "Это всего лишь была моя прихоть не более. Но почему-то на душе было неспокойно.")
    $ Fl.say(Fl_pi, "Д{mn} должен.")
    $ Fl.say(Fl_r, "Вместо того, чтобы бежать в медпункт,{w} этот глупец просто шёл в музыкальный клуб!")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause (3.0)

    scene bg Fl_ext_musclub_night2
    show Fl_dust_full
    show Fl_prolog_dream
    with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Что могло пойти не так? {w}Наверное то, что перед глазами у меня появился туман, всё плыло, а разум из последних сил держался. {w}Клонило в сон, но я боролся.")
    $ Fl.StopAmbience(5)
    $ Fl.say(Fl_r, "Ватными руками мне всё же удалось отрыть ключ в кармане.")
    $ Fl.HideScreens(_with=Fl_fast)


    $ Fl.PlaySound("Fl_open_door_1", 0.5, 0, False)
    scene bg Fl_int_musclub_night:
        Fl_walking3
    show Fl_prolog_dream
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Пионерка невозмутимо продолжала наслаждаться дальше своим сном.")
    $ Fl.say(Fl_pi, "Н-ну, хех... хоть т-так.")
    $ Fl.say(Fl_pi, "Жаль з-здесь нет к-кровати или хотя бы м-матраса.")
    $ Fl.say(Fl_r, "С легкой улыбкой сказал я.")
    $ Fl.say(Fl_r, "Меня начала сильнее покачивать. Последние силы покидали меня. {w}Я больше не мог держать равновесие. {w}В глазах темнело.")
    $ Fl.say(Fl_th, "Не все так просто, да? {w}Пришло время для чего-то большего, чем просто циклы.")
    $ Fl.say(Fl_pi, "Я проиграл? Аха-ха-ха-а-а-а-а-а...")

    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    scene bg Fl_black with hpunch

    $ Fl.say(Fl_r, "Я упал на холодный пол.")
    $ Fl.say(Fl_r, "Но перед этим успел ирочно произнести про себя.")
    $ Fl.say(Fl_th, "Ну что, на второй круг?")
    $ Fl.HideScreens(_with=Fl_dissolve2)




    $ Fl.DayTime("prologue", "night")
    $ Fl.Pause (10.0)


    $ Fl.PlayMusic("Fl_thoughtsindark", 1, 9)
    scene bg Fl_pyst with Fl_dissolve4
    $ Fl.ShowScreens(_with=Fl_dissolve2)
    $ Fl.say(Fl_r, "Каким вам кажется мир? Большим? Огромным? Может, гигантским? Или вовсе бесконечным?")
    $ Fl.say(Fl_r, "Мой мир давно уже сузился до необычного пионерлагеря «Совёнок».")
    $ Fl.say(Fl_r, "И что же мне помешало пойти напролом? {w}Ничего, я так и поступил. Тогда эта идея показалось мне правильной и не самой худшей.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Не получилось... Да и не могло получиться.")
    $ Fl.say(Fl_r, "Пройдя пару дней в лесу и переутомившись - уснул и проснулся в автобусе. {w}Дорога - бесконечная.")
    $ Fl.say(Fl_r, "Выпилиться тоже оказалось не вариант, а наоборот стало толчком к опустошению и апатии.")
    $ Fl.say(Fl_r, "Я думаю каждый на моём месте свехнулся бы. Переживать одни и те же смены с незначительными изменениями, вряд ли кто осилит.")
    $ Fl.say(Fl_r, "Второй круг... третий... уже не имело значения.{w} Я перестал считать.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Вы можете сказать — ты псих! И это будет ваше полное право. {w}Однако...")
    $ Fl.say(Fl_r, "Я не хотел им становиться...")
    $ Fl.say(Fl_r, "Любой человек, попав в примерную ту же ситуацию, что и я, хотел бы вернуться назад — в реальность.")
    $ Fl.say(Fl_r, "Но что такое реальность? {w}Реальность - это всего лишь искажение. Вы видите происходящее - исходя из своих убеждений, но это не значит, что так есть на самом деле...")
    $ Fl.say(Fl_r, "Возможно всё происходящее всего лишь моя бурная фантазия восполённого разума. {w}Не знаю{mn}")
    $ Fl.say(Fl_r, "За долгое пребывание в этом месте мои взгляды на эту самую реальность жёстко пошатнулись.")
    $ Fl.say(Fl_r, "Вы можете лёгко утверждать, что ваш мир - реальность? Но так ли это? {w}Что, если ваша реальность точно такая же, как и это место? {w}Ограниченная локация, со своими лимита и похожими ежедневными событиями?")
    $ Fl.say(Fl_r, "Что, если после смерти происходит просто перезапуск, после чего вы снова оказываетесь в начале своего пути, как и раньше?")
    $ Fl.say(Fl_r, "Теряя воспоминания, вы вновь и вновь проживаете так называемую жизнь, а после... всё заново. {w}Своего рода недокий Лимб.")
    $ Fl.say(Fl_r, "Тогда, назревает довольно логичный вопрос.")
    $ Fl.say(Fl_r, "Что такое настоящая реальность?")
    $ Fl.say(Fl_r, "Поздравляю мы в находимся в полном тупике, из которого нет выхода.")
    $ Fl.StopMusic(5)
    $ Fl.say(Fl_r, "Но в данный момент меня волнует другой насущий вопрос.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.DayTime("nightmare", "night")

    scene bg Fl_pyst_red with Fl_dissolve3
    $ Fl.PlayMusic("Fl_atmosphere", 1, 5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "В чём различие насилия и ультранасилия?")
    $ Fl.say(Fl_r, "Насилие, это ведь просто беспричинное нанесение увечий и вреда другому человеку. {w}Ты не вырываешь его глаза, и не делаешь из них дорогой деликатес, ты не вытаскиваешь его внутренности наружу, нет.")
    $ Fl.say(Fl_r, "Ты просто наносишь ему удары кулаками, или ногами, пока он не попросит пощады слишком жалостливо или не скорчится окончательно от боли. {w}Это немного не то.")
    $ Fl.say(Fl_r, "А вот ультранасилие, это когда ты причиняешь вред, просто потому что тебе скучно. {w}Или потому что это приносит тебе удовольствие.")
    $ Fl.say(Fl_r, "Вот, у этого глаз вырвал, съел прямо у него на глазах(забавно, не так ли?), а потом просто проткнул ему шею, оставив безвольно умирать.")
    $ Fl.say(Fl_r, "А вот того решил сжечь за живо и полюбоваться, как он в конвульсиях пытаеться спасти себя, сдирая кожу ногтями с лица.")
    $ Fl.say(Fl_r, "Этого просто на дереве повесил, из этого все кости вытащил и вставил в пустую тушку, и начал имитировать кукольный театр с одной куклой.")
    $ Fl.say(Fl_r, "Хотя, они и так были куклами, не так ли?")
    $ Fl.say(Fl_r, "Тогда{mn} Может и Совёнок - Театр, а мы в нём - сумасшедшие режиссёры, которые пишут сценарий, забыв о нормах морали и этики, делая что-то действительно из ряда вон выходящее, что буквально взорвёт мозг?")
    $ Fl.say(Fl_r, "Наверное так и есть. Ведь мир всегда жаждит чего-то нового, а мы режиссёры пионерлагеря, как раз таки исполняем свои и чужие прихоти. {w}Да, теперь то всё сходится!")
    $ Fl.say(Fl_r, "Мы хотим сделать настолько уникальную сцену, что совсем забываем про то, что наши декорации слишком однообразные, и считаем это лишь театральной условностью. {w}Как и однообразие самих зданий, впрочем.")
    $ Fl.say(Fl_r, "Это наносит нашему рассудку непоправимый ущерб, однако наша дикая фантазия и не думает утихать.{w} Вот, с чего всё начиналось.")
    $ Fl.say(Fl_r, "Теперь же, слишком поздно.{w} Фантазии давно нет, а при воспоминании слова «рассудок» вырывается лишь безвольный истерический смешок. {w}Остались лишь бездумные животные инстинкты, голодно рыщущие по разуму бедного некогда хиккикомори. {w}А ведь он просто хотел жить...")
    $ Fl.say(Fl_r, "Хотя жил ли он когда-то вообще? {w}По-сути его мир был такой же ошибкой, бессмысленой локацией, где происходило ровным счётом всё тоже самое. Теря что-то мы навсегда теряем понятие {u}жизнь{/u}. Остаётся только существование...")
    $ Fl.say(Fl_pib, "Но я уверен, что скоро всё закончится...")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(6)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.DayTime("prologue", "night")
    $ Fl.Pause (4.5)

    scene cg Fl_mine_fint 
    $ persistent.Fl_photo_pallery_16 = True
    show Fl_vignette3
    with Fl_dissolve2
    $ Fl.PlayMusic("Fl_atmosphere", 1, 5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Что за...")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_pi, "Это же я!")
    $ Fl.say(Fl_r, "По телу пробежали мурашки.")
    $ Fl.say(Fl_kvl, "Знакомься - Ян, собственной персоной, узнаешь? {w}Взгляни на себя со стороны.")
    $ Fl.say(Fl_r, "Спокойным тоном произнес {b}он.{/b}")
    $ Fl.say(Fl_th, "Снова ты...")
    $ Fl.say(Fl_r, "Осколки воспоминаний собирались воедино, рисуя жуткую картину.")
    $ Fl.say(Fl_th, "Точно. Эти чёртовы шахты, Лена...")
    $ Fl.say(Fl_r, "Собрав все силы которые у меня были я нанёс фатальный удар.")
    $ Fl.say(Fl_kvl, "Ну как тебе?")
    $ Fl.say(Fl_th, "Отвратительно. {w}Но что поделать, когда на тебя лезет ненормальная с ножом?")
    $ Fl.say(Fl_pi, "У меня не было выбора. Да и кто-то должен же выполнять грязную работу, верно?")
    $ Fl.say(Fl_r, "Поразмыслив пару секунд я выпалил.")
    $ Fl.say(Fl_pi, "Я просто защищался!")
    $ Fl.say(Fl_r, "Где-то позади во тьме послышался мой собственный смех.")
    $ Fl.say(Fl_th, "Тогда{mn} почему, когда я смотрю на себя мне становится не по себе?")
    $ Fl.say(Fl_kvl, "Мне не зачем давать тебе ответ, ты и так прекрасно знаешь что это.")
    $ Fl.say(Fl_th, "Безумие, не так ли?")
    $ Fl.say(Fl_r, "Саркастично сказал я про себя.")
    $ Fl.say(Fl_kvl, "Нет... Оно тебе ещё пригодится.")
    $ Fl.say(Fl_pi, "Что?")
    $ Fl.say(Fl_r, "Но ответа не последовало, таинственный незнакомец расстворился в непроглядном мраке, оставив меня одного размышлять над его словами.")

    $ Fl.ShowBlink()
    $ Fl.say(Fl_th, "Да кто он такой...")
    $ Fl.StopMusic(5)

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Неожиданно я почувстовал какой-то странный запах. {w}Запах - знакомый с давних времён этот манящий и одновременно сладкий аромат звал меня.")
    $ Fl.say(Fl_th, "Как приятно{mn} Стоп.")
    $ Fl.say(Fl_r, "Я ощутил своё тело. {w}Недавние события пронеслись в моей голове, как падающая звезда.")
    $ Fl.say(Fl_th, "Где я сейчас на самом деле?!")
    $ Fl.say(Fl_r, "Не муча себя интригами, я резко открыл глаза и охнул от происходящего.")
    $ Fl.HideScreens(_with=Fl_fast)


    $ Fl.DayTime("sunset", "sunset")
    scene bg Fl_int_musclub_sunset
    $ Fl.HideBlink()
    $ Fl.ShowUnblink()
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.Pause (1.0)
    $ Fl.say(Fl_th, "Э-э-эмм{mn}")
    $ Fl.say(Fl_r, "Я лежал... {w}А моя голова лежала на подушке. {w}Ну как на подушке{mn} её заменили ножки Мику.")
    $ Fl.HideUnblink()
    $ Fl.PlayMusic("Fl_reeducated", 1, 6)

    $ Fl.say(Fl_mi, "Очнулся!")
    $ Fl.say(Fl_r, "Радостно прокричала Мику, после чего мгновенно же покраснела.")
    $ Fl.say(Fl_mi, "А-а... Я... вот.")
    $ Fl.say(Fl_r, "Её щеки воспылали ещё сильнее. Она замолчала.")
    $ Fl.say(Fl_th, "А ведь может, когда не хочет! Хах.")
    $ Fl.say(Fl_th, "Но почему музклуб?")
    $ Fl.say(Fl_r, "На секунду я забыл о том, что происходило ранее и попытался встать.")
    $ Fl.say(Fl_mi, "Нет-нет! Тебе нельзя, вста...")
    $ Fl.say(Fl_r, "Плечо пронзило острой болью. {w}Стиснув зубы, я процедил.")
    $ Fl.say(Fl_pi, "Чёрт, я совсем забыл про плечо. {w}Сколько я был в отключке?", _with=hpunch)
    $ Fl.say(Fl_mi, "Когда ты упал в музклубе я сразу же проснулась и очень сильно испугалась! Сначала я даже не поняла, ты ли это? Теперь я точно уверена.")
    $ Fl.say(Fl_mi, "Я настолько сильно растерялась, что побежала в медпункт и понабрала оттуда всего и сразу!")
    $ Fl.say(Fl_r, "Раны были перевязаны и единственное, что еще беспокоило правое плечо.")
    $ Fl.say(Fl_th, "<С*ка>, как глубоко вонзила-то!")
    $ Fl.say(Fl_r, "Я повернул голову в сторону окон, сквозь которых пробивался солнечный цвет. {w}Вечерело.")
    $ Fl.say(Fl_pi, "Долго же я проволялся.")
    $ Fl.say(Fl_r, "Я посмотрел на Мику.")
    $ Fl.say(Fl_r, "Она смутилась, но не отвела взгляд.")
    $ Fl.say(Fl_pi, "Спасибо.")
    $ Fl.say(Fl_r, "Впервые за долгое время я произнёс это простое, но настолько важное, слово.")
    $ Fl.say(Fl_mi, "А! Н-не за что.")
    $ Fl.say(Fl_r, "Пионерка покраснела как помидор, а её хвостики мило задёргались.")
    $ Fl.say(Fl_th, "Хах, а я и не знал что у тебя есть такая сторона.")
    $ Fl.say(Fl_th, "Жаль только ты не настоящая...")
    $ Fl.say(Fl_pi, "Есть за что!")
    $ Fl.say(Fl_mi, "Ну-у, хватит смущать меня!")
    $ Fl.say(Fl_r, "Я слабо улыбнулся ей, после чего погрузился в раздумье.")
    $ Fl.say(Fl_pi, "Ночью ничего странного не происходило?")
    $ Fl.say(Fl_mi, "Нет...")
    $ Fl.say(Fl_r, "Только сейчас я осознал, что до сих пор ничего не знаю о всех странностях данного цикла. И это пугала меня больше всего.")
    $ Fl.say(Fl_th, "Психованная знала... и пионер тоже. {w}А-а-а! {w}Почему так сложно? С чего вдруг именно сейчас им всем приспичило?")
    $ Fl.say(Fl_r, "Во мне начинала закипать злость.")
    $ Fl.say(Fl_th, "Хахах. Ну держитесь!")

    $ Fl.Pause (2.5)
    $ Fl.say(Fl_r, "Спустя некоторое время я успокоился и сидел напротив Мику.")

    show mi normal pioneer6 with Fl_dissolve1

    $ Fl.say(Fl_pi, "Итак, что мы будем делать? {w}Мне нужно как-то попытаться узнать, что за чертовщина тут твориться, а без вылазки — нереально.")

    show mi dontlike pioneer4 with Fl_fast

    $ Fl.say(Fl_r, "Мику хотела что-то возразить, но я её опередил.")

    show mi normal pioneer6 with Fl_fast

    $ Fl.say(Fl_pi, "Тебя я взять с собой не могу, так будет вдвойне опасно для нас двоих. {w}Лучше спрячься в кладовке и не шуми, пока я не вернусь.")

    show mi smile pioneer5 with Fl_fast

    $ Fl.say(Fl_r, "Она просто посмотрела мне в глаза и улыбнулась.")
    $ Fl.say(Fl_mi, "Только пообещай, что не бросишь меня тут одну!")
    $ Fl.say(Fl_pi, "Ха, слишком рано для того, что бы говорить «сайонара».")
    $ Fl.say(Fl_th, "Не зря столько времени убил за просмотром аниме. Пригодилось всё же!")
    $ Fl.say(Fl_r, "Я встал, развернулся и начал выходить из музыкального клуба...")

    hide mi smile pioneer5 with Fl_dissolve1

    $ Fl.say(Fl_r, "Как ощутил сзади что-то тёплое и нежное. Пионерка налетела на меня со спины, так что я слегка пошатнулся.")
    $ Fl.say(Fl_th, "Она обняла меня. {w}Снова{mn}")
    $ Fl.say(Fl_r, "Я немного смутился.")
    $ Fl.say(Fl_mi, "Не вернёшься - из под земли достану! И научу играть на гитаре, пианино...")
    $ Fl.say(Fl_r, "Я медленно освободился из её объятий.")
    $ Fl.say(Fl_pi, "Неволнуйся никуда я не денусь.")
    $ Fl.say(Fl_pi, "До встречи!")

    show mi normal pioneer6 with Fl_fast

    $ Fl.say(Fl_r, "Я обернулся и ещё раз напомнил.")
    $ Fl.say(Fl_pi, "Главное не шуми, хорошо?")

    hide mi normal pioneer6 with Fl_fast

    $ Fl.say(Fl_r, "Её улыбка последнее что я увидел, перед тем как отправиться на поиски ответов.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(4)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause (5.5)

    scene bg Fl_ext_houses2_sunset
    show Fl_light_c
    with Fl_effect_4
    $ Fl.PlayMusicFrom("<from 0 to 143>", "Fl_Interlude", 1, 5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Пока что снаружи было тихо...")
    $ Fl.say(Fl_r, "И мне тут же пришла мысль, что обороняться кулаками не лучшая идея. Поэтому я направился в столовую.")

    scene bg Fl_ext_dining_hall_near_sunset
    show Fl_light_c
    with Fl_effect_4
    $ Fl.say(Fl_r, "Столовая и её парадный вход оказались прямо перед моим лицом за считанные секунды.")
    $ Fl.say(Fl_th, "Что-то слишком быстро я сегодня хожу. Неужели адреналин скачет?")
    $ Fl.say(Fl_r, "Как и ожидалось здание было открытым. {w}Кукол не наблюдалось, а значит и закрыть дверь некому.")
    $ Fl.HideScreens(_with=Fl_fast)


    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
    scene bg Fl_int_dining_hall_sunset with Fl_flash
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_pi, "Никто ведь не против если я одолжу нож на какое-то время?")
    $ Fl.say(Fl_r, "Кухня пустовала, как будто здесь никогда никого и не было. Лишь стоявшие порции намекали на то, что совсем недавно здесь были люди.")
    $ Fl.say(Fl_th, "Где же ты, мой родной?")
    $ Fl.say(Fl_th, "Ха-ха! Вот и ты!")
    $ Fl.say(Fl_r, "Кухонный нож уже не казался чем-то диковинным, странным, опасным. {w}За долгое время ты привыкаешь к таком образу жизни и желаешь видеть только одно - смерть тех, кто испортил навсегда твою жизнь.")
    $ Fl.say(Fl_pi, "Аригато!")
    $ Fl.say(Fl_th, "Хах. Что-то я в последнее время часто прибегаю к японскому...")
    $ Fl.say(Fl_r, "Я начал уходить в раздумье.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.DayTime("prologue", "sunset")
    scene bg Fl_pyst_ch with Fl_dissolve3
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Любопытно, когда человек желает бессмертия, что он ожидает? {w}Ту же самую жизнь, но без права на смерть?")
    $ Fl.say(Fl_th, "Но что если это и есть бессмертие? {w}Бессмертие в замкнутом пространстве с одинаковыми правилами... некая закрытая площадка, в которую пускают только избранных.")
    $ Fl.say(Fl_th, "Нет уж, пожалуй я откажусь от такой привелегии. {w}Такое бессмертие сравнимо с лишением всего в том числе и рассудка.")


    $ Fl.DayTime("sunset", "sunset")

    scene bg Fl_int_dining_hall_sunset with Fl_dissolve1
    $ Fl.say(Fl_th, "Я отказываюсь!", _with=hpunch)
    $ Fl.say(Fl_r, "Мой смех разразился на всё помещение.")
    $ Fl.say(Fl_th, "Это всё такой бред!")
    $ Fl.say(Fl_r, "Я долго вдыхал и выдыхал, пытаясь вернуться в норму.")
    $ Fl.say(Fl_th, "Безумие, говоришь, пригодится? {w}И кто тут из нас ещё ненормальный?")
    $ Fl.say(Fl_th, "Каким образом оно мне поможет? Сдохнуть?")
    $ Fl.say(Fl_r, "Мои размышления прервал чей-то силует за окном и отчётливый звук шагов.")
    $ Fl.say(Fl_pi, "И кому приспичило прогуляться по пионерлагерю?")
    $ Fl.say(Fl_r, "Я подошёл к окну, по телу пробежал разряд.")
    $ Fl.say(Fl_th, "Ещё один{mn} и куда это он намылился?")
    $ Fl.say(Fl_r, "Недалеко от столовой расслабленной походкой шёл пионер, копия того, что я повстречал на площади.")
    $ Fl.StopMusic(8)

    $ Fl.say(Fl_th, "Ну тебя я уже просто так не отпущу.")

    scene bg Fl_ext_dining_hall_near_sunset
    show Fl_light_c
    with vpunch
    $ Fl.say(Fl_r, "Забрав нож с собой, я мигом выпрыгнул в окно и начал своё преследование.")
    $ Fl.HideScreens(_with=Fl_fast)


    scene bg Fl_ext_dining_hall_away_sunset
    show Fl_light_c
    with Fl_dissolve1

    $ Fl.Pause (1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Затаившись в кустах я медленно шёл прямиком за пионером, иногда посматривая по сторонам.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.DayTime("night", "night")

    $ Fl.Pause (4.0)
    scene bg Fl_ext_path2_night:
        Fl_walking3
    show Fl_dust_full
    with Fl_dissolve1
    $ Fl.PlayAmbience("Fl_forest_night", 1, 4)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Ночь упала на лагерь так же быстро, как мы оказались в лесу.")
    $ Fl.say(Fl_th, "Не понял...{w} Он в старый корпус прётся что ли?{w} Хах, это мне на руку.")
    scene bg Fl_ext_path2_night
    show Fl_dust_full
    with vpunch
    $ Fl.say(Fl_r, "Спрятавшись за деревом, я резко выглянул, чтобы в очередной раз посмотреть, где моя цель.")
    $ Fl.say(Fl_r, "Пионер находился где-то между кустов, так что видел его я лишь по пояс.")
    $ Fl.say(Fl_r, "Оглядываясь то вперёд, то назад, пионер начал разговаривать...")
    $ Fl.say(Fl_th, "Страно, шизофрения или я просто не вижу никого поблизости? {w}Да, нет, вроде. Только он один.")
    $ Fl.say(Fl_r, "До меня еле-еле доносились обрывки фраз.")
    $ Fl.say(Fl_pior, "...С-страшно.")
    $ Fl.say(Fl_pior, "...Осторожнее...")
    $ Fl.say(Fl_r, "Я поперхнулся, не поверив своим ушам.")
    $ Fl.say(Fl_th, "Ему-то страшно? {w}С какого перепугу он боится?")
    $ Fl.StopAmbience(4)

    $ Fl.PlayMusic("Fl_oldcamp", 1, 10)
    $ Fl.say(Fl_r, "Пионер резко повернулся в мою сторону и начал вглядываться во все кусты.")
    $ Fl.say(Fl_th, "Чёрт!")
    $ Fl.say(Fl_r, "Постоял какое-то время, высматривая и слушая каждый шорох, а после... {w}Он ускорился, но продолжил свой путь в корпус.")

    scene bg Fl_ext_old_building_night
    show Fl_dust_full
    with Fl_dissolve1
    $ Fl.say(Fl_th, "А вот и заброшка...")
    $ Fl.say(Fl_r, "Пионер вошёл в старый корпус.")
    $ Fl.say(Fl_th, "Что-то тут не так...")
    $ Fl.HideScreens(_with=Fl_fast)


    scene bg Fl_ext_old_building_night_moonlight
    show Fl_dust_full
    with Fl_dissolve2
    $ Fl.Pause (2.0)
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Луна подоспела как раз вовремя. В окна старого корпуса пробился свет и мне даже удалось вроде как заметить там какое-то копошение.")
    $ Fl.say(Fl_r, "Дойдя до открытой местности, свободной от деревьев, в центре которой стоял старый и угрюмый заброшенный корпус, я остановился.")
    $ Fl.say(Fl_r, "Я прислушался. Чтобы точно доказать что в корпусе действительно кто-то есть и это всё не мираж.")
    $ Fl.say(Fl_th, "Мне точно не показалось{mn} Там минимум три человека, а может и больше.")
    $ Fl.say(Fl_r, "Звук шёл прямиком с крыши, где, видимо, находился ещё один «клон».")
    $ Fl.say(Fl_th, "Да у вас тут что охраняемый объект, твою мать?!")
    $ Fl.say(Fl_r, "Но помимо звуков на крыше, до меня донёся скрип половиц на первом этаже. Очевидно, что внизу находился клон, выполняющий роль охраника.")
    $ Fl.say(Fl_r, "Подойдя поближе, и спрятавшись за забором детской площадки, я прислушался ещё раз, и уловил ещё один скрип. {w}Он исходил из комнаты, окно которой смотрело как раз на него.")
    $ Fl.say(Fl_th, "Как всё затихнет... Не стоит медлить, иначе шанс пробраться внутрь будет упущен.")
    $ Fl.say(Fl_r, "Выждав несколько минут, я выглянул из-за угла прямо в комнату, окно которой находилось прямо перед ним, заметив странный силуэт, который смотрел в другое окно.")
    $ Fl.say(Fl_th, "Сейчас!", _with=hpunch)
    $ Fl.say(Fl_r, "Не медля ни минуты, я рысью проскочил ко входу в корпус, и засел возле входа. {w}Поискав украдчивым взглядом что-нибудь, чем можно было вырубить наблюдателя, я не обнаружил ничего, и поэтому решил просто незаметно проникнуть внутрь.")
    $ Fl.say(Fl_th, "Облом.")

    scene bg Fl_int_old_building_night with Fl_fast
    $ Fl.say(Fl_r, "Войдя в корпус, я спрятался за углом между входом и комнатой. Подождав несколько секунд, я так же аккуратно выглянул из-за угла, и увидел силуэт, стоящий у окна, выходящий на площадку. Он облокотился, а значит, вряд ли скоро будет менять обзор.")
    $ Fl.say(Fl_r, "Пользуясь моментом, я решил проскочить к лестнице.")
    $ Fl.say(Fl_r, "Бесшумно, каким-то чудом поднявшись по очень старой лестнице, я вновь прислушался, и услышал уже шаги, которые направлялись к нему. Я засел за углом, и начал выжидать.")
    
    scene bg Fl_coridor with Fl_dissolve1
    $ Fl.say(Fl_th, "Только не сейчас!")
    $ Fl.say(Fl_th, "Как я буду весь ваш форпост вырубать, если меня кто-то заметит?!")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Через несколько секунд скрипы прекратились, а затем и вовсе начали отдаляться.")
    $ Fl.say(Fl_r, "Я выглянул в коридор, где меня ждал ещё один патрульный.")
    $ Fl.say(Fl_th, "А что это у нас там?")
    $ Fl.say(Fl_r, "В конце коридора стояли две интересные личности. Девушка с хвостиками и какой-то парниша.")
    $ Fl.say(Fl_th, "А вы ещё кто такие? {w}И неужели это Лена? {w}Я же её вроде прикончил вчера...")
    $ Fl.say(Fl_r, "Я сорвался с места, и тихо, но быстро, пробежал к лестнице на чердак, и засел там. И снова начал прислушиваться к звукам с крыши.")
    $ Fl.say(Fl_th, "Ну вот сейчас мы и узнаем, что за гостей нам лагерь подкинул.")

    scene cg Fl_p_say with Fl_dissolve1
    $ persistent.Fl_photo_pallery_17 = True
    $ Fl.say(Fl_r, "Внизу стоял тот самый парень из коридора. Лица его было не расмотреть, но в темноте казалось, будто у него глаза светятся, как у кошки. Одет он был в нехарактерную для этой местности рубашку чёрного цвета.")
    $ Fl.say(Fl_r, "А рядом с ним была... {w}Лена.")
    $ Fl.say(Fl_th, "Какого?!")
    $ Fl.say(Fl_r, "Она сидела на подоконике и наблюдала за происходящим снаружи, попутно поддерживая диалог с парнем в чёрной рубашке.")
    $ Fl.say(Fl_th, "Я же убил тебя! Какого чёрта ты тут тогда сидишь?")
    $ Fl.say(Fl_vp, "И так, зачем ты пожаловала к нам, Тихоня?")
    $ Fl.say(Fl_r, "Задал вопрос парень, которого я обозначил за «Главного». Его выделяющийся образ дал мне понять, что вожак всей этой шайки именно он.")
    $ Fl.say(Fl_lnt, "Ты новенького встречал?")
    $ Fl.say(Fl_r, "Главный засмеялся, после чего всё же ответил на поставленный вопрос.")
    $ Fl.say(Fl_vp, "Да, было дело. Он тут мне одну пешку убрал. Даже труп за собой не убрал представляешь?")
    $ Fl.say(Fl_lnt, "Хаха. Ну разве он не милаха? {w}Он даже меня смог одолеть. Такой силы я неожидала.")
    $ Fl.say(Fl_lnt, "И что ты планируешь делать?")
    $ Fl.say(Fl_vp, "Одна потеря мои планы не меняет. Я должен отыскать {b}её{/b}.")
    $ Fl.say(Fl_th, "Её{mn} Да сколько вас таких индивидов?")
    $ Fl.say(Fl_lnt, "Хахаха. Ты и правда думаешь что она тебе по силам?")
    $ Fl.say(Fl_r, "Но смех Лены быстро прекратился, а выражение лица сменилось на серьёзное.")
    $ Fl.say(Fl_vp, "Не зазнавайся. Я ведь могу и тебя превратить в куклу, хочешь?")
    $ Fl.say(Fl_r, "На лице главного появилась дьяволская ухмылка. От его мерзкой улыбки меня передёргнуло.")
    $ Fl.say(Fl_th, "П-почему мне так неприятно смотреть на него?!")
    $ Fl.say(Fl_r, "Ответ был очевиден: он был слишком похож на меня недавнего. {w}Не на обычных ненормальных, готовых сделать всё что угодно, а на самого настоящего демона.")
    $ Fl.say(Fl_r, "Лена лишь кивнула в знак понимания.")
    $ Fl.say(Fl_vp, "Кстати, вы достали то что я просил?")
    $ Fl.say(Fl_r, "Задал вопрос главный двум пионерам, позади себя.")
    $ Fl.say(Fl_pior, "Простите, это задание было у наблюдателя, но его кто-то убил.")
    $ Fl.say(Fl_vp, "Яс-сненько.")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.say(Fl_r, "Протянул главный, после чего ударил отвечающего с ноги в живот.")
    $ Fl.say(Fl_r, "От удара пионер сложился по полам. {w}В тот же миг он начал корчиться от дикой боли. А главный молча подошёл и поднял голову бедолаги за волосы.")
    $ Fl.say(Fl_vp, "Вы хоть что-то можете сделать сами? Или мне всё за вас делать, куски мусора?")
    $ Fl.say(Fl_pior, "Простите нас! Такое больше не повторится!")
    $ Fl.say(Fl_r, "Ответил второй пионер.")
    $ Fl.say(Fl_vp, "Конечно не повторится!")
    $ Fl.say(Fl_r, "Главный ослабил хватку и пионер неуверенно встал на ноги.")
    $ Fl.say(Fl_lnt, "Ты так жесток с ними{break2}")
    $ Fl.say(Fl_r, "Движение и громкий скрип раздался на всю округу.")
    $ Fl.say(Fl_r, "Голова главного резко поднялась и посмотрела наверх прямо на меня.")
    $ Fl.say(Fl_vp, "У нас го-о-о-ости!")
    $ Fl.say(Fl_r, "Его психически весёлый смех разнёсся на всё здание. {w}Весело прокричав, в это время все остальные пионеры ринулись ко мне на крышу.")
    $ Fl.say(Fl_th, "Да <бл*ть>! Это мне так не везёт, или всё вокруг внезапно стало против меня?!")
    $ Fl.say(Fl_th, "Пора валить отсюда нахрен!", _with=vpunch)
    $ Fl.say(Fl_th, "Только... Куда?{w} Я же совершенно не знаю, что происходит именно в этом лагере.")
    $ Fl.say(Fl_th, "Ладно, самым разумным вариантом, мне кажется, будет шахта. {w}Много путей, темно, да и я просто смогу спрятаться, пока они не уйдут.")
    $ Fl.say(Fl_r, "Я подбежал к лестнице, ведущей на чердак и быстро спустился.")
    scene bg Fl_coridor with Fl_fast:
        Fl_run

    $ Fl.Pause (1.0)

    $ Fl.say(Fl_r, "Во всем корпусе стоял громкий грохот, который здание, казалось, не выдержит.")
    $ Fl.say(Fl_r, "Посмотрев в коридор я понял, что выйти обратно тем же путём не предоставляется возможным.")
    $ Fl.say(Fl_th, "Походу настал мой час!")
    $ Fl.say(Fl_r, "Я достал тот самый нож.")
    $ Fl.say(Fl_th, "Придётся немного запачкать руки кровью.")
    $ Fl.say(Fl_r, "Все происходило, словно в замедленной съёмке. {w}Нож. Второй этаж. Побег. {w}Я проскачил сквозь одного.")
    scene bg Fl_int_old_building_night with vpunch:
        Fl_run

    $ Fl.say(Fl_r, "Спрыгнув с лестницы между первым и вторым этажом я долго проклинал себя, но в конечном итоге счёт шёл на секунды.")
    $ Fl.say(Fl_r, "Первый этаж.")
    $ Fl.say(Fl_th, "Окно! Парадный вход уже давно обложили.")
    $ Fl.say(Fl_r, "Я мог быть уверен в этом, ведь по их расчётам {b}я{/b} не должен покинуть это здание.")
    $ Fl.say(Fl_r, "Забежав в комнату на первом этаже старого корпуса я не раздумывая сиганул в окно.")

    scene bg Fl_ext_old_building_night_moonlight
    show Fl_dust_full
    with vpunch
    $ Fl.say(Fl_r, "Дальше начался настоящий побег.")
    $ Fl.say(Fl_r, "Определившись с местом прибытия, мои ноги сами несли меня прямиком в лес, к тоннелям.")

    scene bg Fl_ext_path_night:
        Fl_run_fast
    show Fl_dust_full
    with Fl_fast
    $ Fl.say(Fl_th, "Здесь налево...")

    scene bg Fl_ext_path2_night:
        Fl_run_fast
    show Fl_dust_full
    with Fl_fast
    $ Fl.say(Fl_r, "Меня догонял пионер.")
    $ Fl.say(Fl_th, "Ещё чуть-чуть и он сможет меня достать!")
    $ Fl.say(Fl_pi, "Выкуси!")
    $ Fl.say(Fl_r, "Я швырнул нож в его тело, сделав что-то наподобии полукруга, поворачивая три раза направо.")

    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    $ Fl.say(Fl_r, "Точное попадание. {w}Он упал{mn} Упал, и тот самый торчащий нож, легко и просто прошёл насквозь его тело, войдя внутрь.")

    scene bg Fl_ext_path_night:
        Fl_run_fast
    show Fl_dust_full
    with Fl_fast
    $ Fl.say(Fl_pior, "За ним! Не дайте ему уйти!")
    $ Fl.say(Fl_th, "И ради чего я всем этим занимаюсь? Ничего такого не узнал, так ещё и убить хотят!")

    scene bg Fl_ext_path2_night:
        Fl_run_fast
    show Fl_dust_full
    with Fl_fast
    $ Fl.StopMusic(4)

    $ Fl.say(Fl_r, "Я не стал долго думать и на бегу нырнул прямиком в яму.")
    scene bg Fl_black with vpunch

    $ Fl.say(Fl_th, "Правда, сейчас уже не так и весело... {w}Света-то нет.")
    $ Fl.say(Fl_pior, "Сто процентов туда спрыгнул.")
    $ Fl.say(Fl_pior, "Придурок! {w}Нужно туда спуститься проверить.")
    $ Fl.PlayAmbience("Fl_catacombs", 1, 4)

    $ Fl.say(Fl_r, "Я неспеша на ощупь шёл в непроглядной мгле тоннеля. {w}Не было ниединого источника света, который мог бы создать хоть какую-то тень для обзора. Единственная надежда была на моё осязание.")
    $ Fl.say(Fl_th, "Идиоты, ну попробуйте меня отыскать в темноте!")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause (1.5)
    scene bg Fl_int_mine_coalface with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Дойдя до одного из моего любимых мест этого лагеря, я решил затаиться.")
    $ Fl.say(Fl_th, "Жаль ножичек <про*бал>...")
    $ Fl.say(Fl_pior, "...")
    $ Fl.say(Fl_pior, "...")
    $ Fl.say(Fl_pior, "Не думаю, что он остановился здесь. {w}Скорее всего, побежал дальше.")
    $ Fl.say(Fl_pior, "Ты знаешь что с нами сделают, если мы вернёмся без него?")
    $ Fl.say(Fl_pior, "Да не парься, лагерь маленький отыщем эту мразь в два счёта!")
    $ Fl.say(Fl_pior, "Плюс не только мы же ищем. Нас много, на кого-то да наткнётся.")
    $ Fl.say(Fl_pior, "Тихо! Вы это слышали?")
    $ Fl.say(Fl_pior, "Что?")
    $ Fl.say(Fl_pior, "Бегите!")
    $ Fl.say(Fl_r, "Непонятные крики доходили до моих ушей из глубин шахты.{w} Я насторожился.")
    $ Fl.say(Fl_pior, "Валим! ВАЛИМ!")
    $ Fl.say(Fl_r, "Где-то далеков в шахте можно было распознать бег нескольких человек.")
    $ Fl.say(Fl_th, "Самый лучший пионерлагерь! {w}Вы можете остаться здесь на своё целое навсегда!")
    $ Fl.say(Fl_r, "Меня начал пробирать холод.")
    $ Fl.say(Fl_th, "Думаю, мне тоже пора уходить.")
    $ Fl.say(Fl_r, "Неожиданно всё вокруг начало затягивать каким-то странным туманом.")
    $ Fl.say(Fl_pi, "Да вы издеваетесь? Что на этот раз?!")
    $ Fl.say(Fl_r, "Казалось бы, куда может быть ситуация хуже этой?")
    $ Fl.say(Fl_r, "Шаги, которые медленно приближались ко мне. {w}Было рисковано выходить из нычки, поэтому я решил лучше затаиться и переждать напасть, в надежде что меня не заметят.")

    $ Fl.Pause (2.5)
    $ Fl.say(Fl_r, "Спустя полминуты шаги начали отдаляться, судя по звукам, в направлении убежавших пионеров.")
    $ Fl.say(Fl_th, "Вот теперь точно надо уходить.")

    scene bg Fl_int_mine_wallbreak with Fl_dissolve2
    $ Fl.say(Fl_r, "Один, два, три поворота - не имело значения.")

    scene bg Fl_int_mine_halt_lighter with Fl_dissolve2
    $ Fl.say(Fl_r, "Вдали вырисовывался выход.")
    $ Fl.say(Fl_r, "Интуиция подсказывала, что сейчас может что-то случиться.")
    $ Fl.say(Fl_th, "Ну нет... Пожалуйста, только не снова!")
    $ Fl.say(Fl_r, "Я повернулся назад.")

    scene bg Fl_int_mine_wallbreak with Fl_dissolve1
    $ Fl.PlayMusic("Fl_hron", 1, 6)
    $ Fl.say(Fl_vp, "Приве-е-е-ет...")
    $ Fl.say(Fl_r, "Донеслось из темноты.")
    $ Fl.say(Fl_pi, "Неужели нашли всё таки?")
    $ Fl.say(Fl_vp, "Знаешь, мне нравится то, как ты смог выкрутиться в данной ситуации, поэтому...")
    $ Fl.say(Fl_vp, "Я хочу чтобы ты присоединился ко мне. {w}Не подумай, у меня естественно есть, что предложить взамен.")
    $ Fl.say(Fl_pi, "Разве эти куклы с тобой, не потому что бояться тебя?")
    $ Fl.say(Fl_vp, "Хахаха. А ты забавный!")
    $ Fl.say(Fl_vp, "Когда-нибудь замечал, что некоторые из нас слишком нехарактерно быстры для обычных людей?")
    $ Fl.say(Fl_pi, "О чём это ты?")
    $ Fl.say(Fl_vp, "Хах, настолько неосведомлён?")
    $ Fl.say(Fl_vp, "Хотя это не совсем скорость... скорее что-то иное, так сказать. {w}Заинтриговал?")
    $ Fl.say(Fl_r, "Любопытство было слишком велико.")
    $ Fl.say(Fl_pi, "Продолжай!")
    $ Fl.say(Fl_vp, "Представь, что ты можешь очень быстро попасть в любую точку лагеря. {w}Как тебе?")
    $ Fl.say(Fl_vp, "Правда у такого фокуса есть свои минусы - ты теряешь жизненую силу, но это неважно.")
    $ Fl.say(Fl_vp, "Но согласись что такая способность довольно ценная. И я могу тебе её дать!")
    $ Fl.say(Fl_pi, "Что за бред? {w}Сверх способности, прикалываешься? Я уже столько времени...")
    $ Fl.say(Fl_vp, "И что дальше? {w}Я намного дольше тебя заперт в этом мире! Или ты думал ты один такой особенный, {b}живой?{/b}")
    $ Fl.say(Fl_r, "Главный сделал акцент на последнее слово, явно на что-то намекая.")
    $ Fl.say(Fl_vp, "Присоединись и я расскажу тебе абсолютно всё, что знаю.")
    $ Fl.say(Fl_vp, "Какой смысл мне будет таить от тебя данные знания? {w}Или ты предпочитаешь бегать по замкнутому кругу?")
    $ Fl.say(Fl_pi, "Знаешь мне как-то не хочется получить ногой по животу!")
    $ Fl.say(Fl_r, "Глаза моего собеседника засветились, а на лице появилась жуткая ухмылка. {w}Зловещий смех раздался по всей шахте, отражаясь от стен.")
    $ Fl.say(Fl_vp, "Да ладно тебе! Он заслужил.")
    $ Fl.say(Fl_vp, "Кстати, мы тут недавно одного пропавшево нашли... мёртвым. {w}Не знаешь, чьих это рук дело?")
    $ Fl.say(Fl_r, "Он как-то легко растянул последнее предложение, словно ответ был уже у него в кармане.")
    $ Fl.say(Fl_pi, "Хочешь сказать, не знаешь, что это был я?")
    $ Fl.say(Fl_vp, "Меня что, так легко прочитать? {w}Ах, придётся больше тренироваться в сфере актёрского искусства...")
    $ Fl.say(Fl_th, "Да что ты привязался ко мне?!")
    $ Fl.say(Fl_vp, "То, как ты стёр с лица земли этого пионеришку было очень занимательно! {w}А ведь он был далеко не последний в навыках ближнего боя...")
    $ Fl.say(Fl_vp, "Знаешь это место не подходит для беседы, слишком тут темно.")
    $ Fl.say(Fl_pi, "Так ты из темноты выйди на свет... {w}Или ты предпочитаешь скрываться во мраке?")
    $ Fl.say(Fl_vp, "Кто его знает.")
    $ Fl.say(Fl_r, "Мой собеседник был не намерен продолжать разговор, будто ставя точку своей последней фразой.")
    $ Fl.say(Fl_th, "Бесплатный сыр только в мышеловке, поэтому...")
    $ Fl.say(Fl_pi, "Мой ответ - нет.")
    $ Fl.say(Fl_vp, "Как жаль... {w}Хотя... кому я вру?")
    $ Fl.say(Fl_vp, "Прощай.")
    $ Fl.say(Fl_r, "Две жёлтые точки скрылись во тьме.")
    $ Fl.say(Fl_th, "Вот и катись отсюда.")
    $ Fl.StopMusic(4)

    scene bg Fl_int_mine_door_lighter with Fl_dissolve1
    $ Fl.say(Fl_r, "Я развернулся и подошёл к двери.")
    $ Fl.say(Fl_r, "Стоило мне её только открыть, как...")
    $ Fl.say(Fl_pi, "Что за <нах*й>?")
    $ Fl.say(Fl_r, "Возникло желание закрыть эту дверь и никогда не вспоминать то, что я видел.")

    scene bg Fl_int_mine_crossroad_lighter with Fl_dissolve1
    $ Fl.say(Fl_r, "За дверью находилась та же шахта. {w}Сомнений не было.")
    $ Fl.say(Fl_pi, "Какого чёрта?! {w}Где выход?!", _with=hpunch)
    $ Fl.say(Fl_r, "У меня начало появляться ощущение беспомощности. {w}Чувство бесконечно-замкнутого пространства начинало сводить меня с ума...")
    $ Fl.say(Fl_pi, "Ха-ха-ха!")
    $ Fl.say(Fl_r, "Я смеялся, ведь мне действительно было смешно.{w} Ведь как так получилось, что тот, кто, казалось бы знал всё, в итоге не знает ничего?")
    $ Fl.say(Fl_pi, "Какой же я тупица! {w}Невероятно!")
    $ Fl.say(Fl_pi, "П-почему мы все здесь? {w}Или... нет. {w}Нет-нет-нет! Для чего мы здесь?")
    $ Fl.say(Fl_r, "Бесконечность... {w}Раскинув руки в разные стороны, я несильно крикнул.")
    $ Fl.say(Fl_pi, "Забавно!")
    $ Fl.say(Fl_r, "Я продолжал заливаться своим собственным смехом, дико озираясь по сторонам.")
    $ Fl.say(Fl_r, "Лагерь...")
    $ Fl.say(Fl_pi, "ВОСХИТИТЕЛЬНО, ДРУГ МОЙ! {w}Просто поразительно то, как ты это провернул!", _with=hpunch)
    $ Fl.say(Fl_r, "Куклы... {w}Схватившись за голову, начал сильно сжимать её своими ладонями...")
    $ Fl.say(Fl_r, "Пионеры... {w}Я упал на землю в припадке.")
    $ Fl.say(Fl_r, "Меня окружали стены. {w}Казалось, что проход начал потихоньку сужаться и проподать из виду.")
    $ Fl.say(Fl_r, "Мой голос прерывался, а страх всё больше и больше продолжал нарастать.")
    $ Fl.say(Fl_pi, "Бессмыслица... Б-бессмыслица, бессмыслица, бессмыслица!", _with=hpunch)
    $ Fl.say(Fl_r, "Ударял себя по лицу, бился головой об стенку шахт... {w}Всё ради того чтобы привести себя в порядок.")
    $ Fl.say(Fl_pi, "Х-хватит! Возьми себя в руки!", _with=hpunch)
    $ Fl.say(Fl_pi, "Здесь д-должен б-быть выход.{w} Должен!")
    $ Fl.say(Fl_th, "Это всего лишь игра разума, которую затеял пионер с ярко-жёлтыми глазами.")
    $ Fl.say(Fl_th, "Меня чертовски возбуждает это, когда ставки в игре так высоки!")
    $ Fl.say(Fl_pi, "И куда дальше?")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    jump pick 


label pick:
    scene bg Fl_int_mine_crossroad_lighter with Fl_dissolve1
    if pick == 5:
        $ Fl.ShowScreens(_with=Fl_dissolve1)
        $ Fl.say(Fl_q66, "Да сколько можно?! {w}Опять всё делать за тебя!")
        $ Fl.say(Fl_q66, "Запоминай! {b}Лево-право-право-право{/b}!")
        $ Fl.HideScreens(_with=Fl_dissolve1)
        menu:
            "Лево":
                jump pick2
            "Право":
                $ pick += 1
                jump pick_lose
    elif pick == 7:
        $ Fl.ShowScreens(_with=Fl_dissolve1)
        $ Fl.say(Fl_q66, "Ты чё прикалываешь, дибил? Даже с подсказкой не можешь найти выход?!")
        $ Fl.say(Fl_q66, "Придётся всё самому делать!")
        $ Fl.HideScreens(_with=Fl_dissolve1)
        scene bg Fl_int_mine_wallbreak with Fl_dissolve1
        scene bg Fl_int_mine_crossroad_lighter with Fl_dissolve1
        scene bg Fl_int_mine_halt_lighter with Fl_dissolve1
        jump pick_win
    else:
        menu:
            "Лево":
                jump pick2
            "Право":
                $ pick += 1
                jump pick_lose



label pick2:
    scene bg Fl_int_mine_wallbreak with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Поворот за поворотом... Я шёл, в надежде, что это закончится...")
    $ Fl.say(Fl_th, "Не мог же он на полном серьёзе создать совершенно новую шахту? {w}Если она новая, то есть ли в ней выход? {w}Является ли это эдаким лабиринтом?")
    $ Fl.say(Fl_r, "Независимо от моих действий ничего не менялось. {w}Ни-че-го.")
    $ Fl.say(Fl_r, "Гнетущая атмосфера продолжала давить на меня, но я не мог остановиться.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    menu:
        "Лево":
            $ pick += 1
            jump pick_lose
        "Право":
            jump pick3


label pick3:
    scene bg Fl_int_mine_crossroad_lighter with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_pi, "Да сколько можно?!")
    $ Fl.say(Fl_pi, "Конечно, это всё круто, что окружение меняется и всё такое...")
    $ Fl.say(Fl_pi, "Но бродить по одним и тем же местам вообще не весело!")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    menu:
        "Лево":
            $ pick += 1
            jump pick_lose2
        "Право":
            jump pick4


label pick4:
    scene bg Fl_int_mine_halt_lighter with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Ощущая на себе подземное давление невысоких стен, которые в любую минуту могут обрушиться на твою слабенькую черепушку, я вдруг вспомнил о тараканах.")
    $ Fl.say(Fl_th, "Тараканы{mn} Я помню, люди писали, что они могут пережить даже ядерную войну... {w}А что такое ядерная война? {w}Это когда ядра воюют? {w}А за что они воюют?")
    $ Fl.say(Fl_th, "Разве у них есть цели? {w}Убивать другие ядра?")
    $ Fl.say(Fl_th, "А ведь по сути, битва двух людей, эта битва одного десятка миллионов ядер с другими...")
    $ Fl.say(Fl_th, "То есть, каждая драка - ядерная война? Да{mn} Этот мир жесток.")

    $ Fl.AttackScreens()
    $ Fl.say(Fl_r, "Я дал себе смачную оплеуху и вернулся к суровой реальности.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    menu:
        "Лево":
            $ pick += 1
            jump pick_lose2
        "Право":
            jump pick_win





label pick_lose:
    scene bg Fl_int_mine_crossroad_lighter with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Какой это уже раз?")
    $ Fl.say(Fl_r, "Оказавшись на очередной развилке, я уж собирался было задуматься о пути, однако, мне на голову упал камушек. {w}Через несколько секунд неподалёку от меня упало ещё несколько таких.{w} Шахта была явно непригодной для нахождения здесь.")
    $ Fl.say(Fl_r, "Я решил, что мне всё-таки пора валить отсюда.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    jump pick


label pick_lose2:
    scene bg Fl_int_mine_coalface_lighter with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Который раз я прохожу это место?")
    $ Fl.say(Fl_r, "Передо мной нарисовались породные кристалы. {w}От красочности этого места ни осталось и следа. {w}Даже это место лагерь не пощадил.")
    $ Fl.say(Fl_r, "Я продолжил путь.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    jump pick




label pick_win:
    $ Fl.Pause (1.5)
    scene bg Fl_int_mine_door_lighter with Fl_dissolve2
    $ Fl.say(Fl_r, "После долго скитания по лабиринту, я наконец-то вышел к заветной двери.")

    scene bg Fl_int_mine_room_dark with Fl_dissolve1
    $ Fl.say(Fl_r, "И оказался внутри помещения.")
    $ Fl.say(Fl_pi, "П-получилось... Не верю... Получилось!")
    $ Fl.say(Fl_r, "Я радостно принялся смеяться, как маленький ребёнок от покупки игрушки или сладости. {w}В этот момент я был самым счастливым человеком на свете.")
    $ Fl.say(Fl_th, "Но как он смог провернуть такое? {w}Хотя, после всего того, что я видел здесь, задавать такие вопросы даже самому себе - глупо.")
    $ Fl.say(Fl_th, "Ну держись, тварь глазастая!")
    $ Fl.say(Fl_pi, "По твою душу сейчас придёт кровавый дьявол!")
    $ Fl.say(Fl_r, "Меня выворачивало наизнанку от тех мыслей и идей, которые я мог бы воплатить в жизнь с его телом.")
    $ Fl.say(Fl_th, "Не бойся, долго ты не продержишься!")
    $ Fl.StopAmbience(4)

    scene bg Fl_int_mine_exit_night_light with Fl_dissolve1
    $ Fl.say(Fl_r, "Я вприпрыжку добрался до выхода. {w}От ярких картинок мести, меня дёргало в пляс.")


    $ Fl.DayTime("kira", "night")


    $ Fl.say(Fl_pib, "Сейчас кто-то умрёт.")
    
    $ Fl.PlayMusic("Fl_avenge", 1, 8)
    if persistent.Fl_dictionary_9 == False:
        $ Fl.PodskDict()
    $ persistent.Fl_dictionary_9 = True
    $ Fl.say(Fl_r, "Состояние, в котором я находился адекватно можно было называть {i}анабиозом{/i}.")
    $ Fl.say(Fl_r, "Стоило мне только окунуться в естественное для себя безумие, как я сразу начинал воспринимать всё вокруг в штыки. {w}То есть, любая насмешка или оскорбление всегда приводили к одном исходу - убийству.")

    scene bg Fl_ext_square_night 
    show Fl_dust_full
    with Fl_dissolve1
    $ Fl.say(Fl_th, "Интересно, сколько времени я пробыл под землёй? {w}Какова вероятность, что я там пропустил целый день?")
    $ Fl.say(Fl_th, "А впрочем  неважно!")

    scene bg Fl_ext_path2_night
    show Fl_dust_full
    with Fl_dissolve1
    $ Fl.say(Fl_r, "Мы двинулись прямо к старому корпусу. {w}Я и моё любопытсво.")

    scene bg Fl_ext_old_building_night_moonlight
    show Fl_dust_full
    with Fl_dissolve1
    $ Fl.say(Fl_pib, "Однако, здравствуйте.")

    scene bg Fl_int_old_building_night with Fl_dissolve1
    $ Fl.say(Fl_r, "Зайдя внутрь заброшки, меня повстречала тишина и пустота.")
    $ Fl.say(Fl_pib, "Не понял, куда все смылись? {w}Кто меня развлекать будет?!")

    $ Fl.AttackScreens(True)
    $ Fl.say(Fl_r, "И тут же перед лицом пролетел кусок арматуры.")
    $ Fl.say(Fl_r, "Я среагировал настолько быстро, что удивился сам себе своей нечеловеческой реакции. {w}Время будто замедлилось, волосы развились от ветра, а на лице появилась ухмылка.")
    $ Fl.say(Fl_r, "В тот же миг я контроатаковал оппонента, ударив со всей силы в живот.")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.say(Fl_r, "Пионер отлетел в другую часть комнаты, выронив арматуру из рук. {w}Я же быстро подобрал арматуру и молниеносно оказался перед его лицом.")
    $ Fl.say(Fl_r, "На его лице застыла гримаса ужаса вперемешку с удивлением.")

    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    $ Fl.say(Fl_r, "Удар. {w}Ещё удар. {w}Я бил до тех пор, пока лицо клона не превратилось в фарш.", _with=hpunch)
    $ Fl.say(Fl_pior, "Псих ненормальный!")
    $ Fl.say(Fl_r, "Со спины в мою сторону летел с кулаками другой пионер.")

    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    $ Fl.say(Fl_r, "Не сбавляя темп, я вонзил кусок армотуры ему прямо в живот. {w}А после стал вкручивать как болт глубже, пока хруст костей не перекрыл крики пионера.")
    $ Fl.say(Fl_r, "После того, как арматура прошла на сквозь, пионер замолчал.")
    $ Fl.say(Fl_r, "Дикий хохот раздался по всему зданию. {w}Я ликовал. {w}Ликовал своей победе. Хоть и понимал, что у них не было и шанса одолеть, такое чудовище.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause (2.5)
    scene bg Fl_coridor with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "И вот я снова тут.")
    $ Fl.say(Fl_r, "Больше на пути мне никто не попадался. Было наудивление тихо. {w}Даже слишком тихо...")
    $ Fl.say(Fl_th, "Неужели тут было только двое?")
    $ Fl.HideScreens(_with=Fl_fast)
    $ Fl.StopMusic(7)


    $ Fl.DayTime("night", "night")
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Моя жажда крови ослабла, а вместе с ней ко мне пришло логическое мышление.")
    $ Fl.say(Fl_th, "Возвращаясь к изначальному вопросу: где остальные?")
    $ Fl.say(Fl_pi, "Ну не мог же я их себе просто придумать, да?")
    $ Fl.say(Fl_r, "Передо мной находился коридор второго этажа старого корпуса. {w}Сгнившие доски, влажный запах и ночные тона отлично дополняли этот момент.")
    $ Fl.say(Fl_pi, "Эта комната...")

    scene bg Fl_int_old_building_floorroom_night with Fl_dissolve1
    $ Fl.say(Fl_r, "Войдя в комнату, за которой я недавно наблюдал, я ощутил странное чувство. {w}Появились мысли, что за мной следят.")
    $ Fl.say(Fl_r, "Аккуратно осмотрев комнату сначала перефирийным зрением, я продолжил осмотр уже нормально.")
    $ Fl.say(Fl_r, "Старая кровать. {w}Подоконик, на котором сидела Лена. {w}Куча разбросанных игрушек. {w}Много окурков и прочего мусора.")
    $ Fl.say(Fl_r, "Стараясь игнорировать хлам под ногами, я осматривал каждый уголок помещения.")
    $ Fl.say(Fl_r, "Но кроме записок я ничего не нашёл.")
    $ Fl.say(Fl_pi, "Чёрт! {w}Вы хотите сказать, что они ничего здесь не оставили? Совсем?")
    $ Fl.say(Fl_r, "Мой взгляд упал на листик бумаги с разными пометками в виде круга.")
    $ Fl.say(Fl_r, "Цвет этих самых кружков был разный: голубой, зелёный, фиолетовый, оранжевый, красный.")
    $ Fl.say(Fl_th, "Что-то мне это напоминает...")
    $ Fl.say(Fl_r, "В одной из бумаг так же было указано количество этих самых пометок.")
    $ Fl.say(Fl_r, "На всех бумагах было невероятное количество цифр, словно здесь происходили научные расчёты, если не хуже. {w}Вертикально, горизонтально, а так же по диагонали.")
    $ Fl.say(Fl_th, "Для чего бы им это всё понадобилось? Вы пионеры, или секретная организация, а?!")
    $ Fl.say(Fl_r, "Спустя пару минут изучения материала я наткнулся на ещё одну бумагу. Отличии в ней было весомое, а именно - цвет.")
    $ Fl.say(Fl_r, "Абсолютно все бумаги были в стандартном белом цвете, однако здесь... Красный цвет ярко выделялся среди всех белых.")
    $ Fl.say(Fl_r, "Содержание повергло меня в некий ступор и шок одновременно.")
    $ Fl.say(Fl_th, "Завтра вечером вы должны избавиться от источника проблем. {w}На этот раз мы не смогли достать всё, а значит, мы должны как можно скорее уничтожить его и её вместе.")
    $ Fl.say(Fl_th, "И помните, сбежать — не выход.")
    $ Fl.say(Fl_th, "Это{mn} это про меня? {w}Меня и Мику?")
    $ Fl.say(Fl_pi, "Не может быть.{w} Да... этого просто не может быть!")
    $ Fl.say(Fl_r, "Осторожно перевернув страницу, я застыл на месте, смотря только в одну точку.")
    $ Fl.say(Fl_th, "Этот парень мешает, а значит отправится на следующий цикл... {w}вместе со своей аквамариновой подружкой...")

    scene bg Fl_coridor with Fl_fast:
        Fl_run_fast
    $ Fl.PlayMusicFrom("<from 15 to 67>", "Fl_actionmiku", 1, 2)
    $ Fl.say(Fl_r, "Сорвавшись с места, я принялся бежать к музклубу.")
    $ Fl.say(Fl_th, "Если это всё правда{mn} Чёрт!")
    $ Fl.say(Fl_r, "В тот момент я не думал.")

    scene bg Fl_int_old_building_night with vpunch:
        Fl_run_fast
    $ Fl.say(Fl_r, "Я понимал, что это необходимо.")
    $ Fl.say(Fl_r, "После стольких лет внезапно осознать, что всё было зря...")
    $ Fl.say(Fl_r, "Мне жутко хотелось, чтобы она продолжала жить. {w}Возможно, потому, что я долгое время не мог просто поговорить, высказаться... И сейчас, когда такая ситуация, где я могу хоть немного быть собой находится в опасности.")
    $ Fl.say(Fl_th, "Я хочу увидеть продолжение. {w}Я не хочу такого конца!")

    scene bg Fl_ext_old_building_night_moonlight with Fl_dissolve1:
        Fl_run_fast
    $ Fl.say(Fl_pi, "Вы у меня ещё попляшете!", _with=hpunch)
    $ Fl.say(Fl_r, "Я знал, что мне гарантирован ад, если я смогу по-настоящему умереть. {w}Но в тот момент меня это не волновало.")

    scene bg Fl_ext_path2_night with Fl_dissolve1:
        Fl_run_fast
    $ Fl.AttackScreens(True)
    $ Fl.say(Fl_pi, "Да кому какая разница?!", _with=hpunch)
    $ Fl.say(Fl_r, "Заорал я на всю округу.")
    $ Fl.say(Fl_pi, "Какой смысл?!")
    $ Fl.say(Fl_th, "В чём он заключается, если абсолютно всё остаётся, как раньше?!")
    $ Fl.say(Fl_r, "Меня пробирало всего насквозь. {w}Руки дрожали, {w}ноги подкашивались, {w}а глаза пылали ярким синим пламенем.")

    scene bg Fl_ext_path_night with Fl_fast:
        Fl_run_fast
    scene bg Fl_ext_houses_night with Fl_fast:
        Fl_run_fast
    $ Fl.say(Fl_r, "Я бежал настолько быстро, насколько мог в принципе человек, не готовый потерять одну из главных деталей в своей жизни.")
    $ Fl.say(Fl_th, "Оставить всё как есть, продолжая бесконечно страдать в одних и тех же циклах? Наблюдать за тем, как всё происходит в тысячный раз?")
    $ Fl.say(Fl_th, "Это по твоему я заслужил, бог? {w}ОТВЕТЬ ЖЕ!")
    $ Fl.say(Fl_th, "Ну уж нет, лучше убейте!")

    scene bg Fl_int_musclub_night
    show mi sad pioneer5
    show Fl_prolog_dream
    with Fl_flash
    $ Fl.say(Fl_mi, "К-кто ты?")
    $ Fl.say(Fl_pi, "Ты знаешь, похоже, что я уже сам не знаю точно, кто я.")
    $ Fl.say(Fl_mi, "Ты один из {b}них?{/b}")
    $ Fl.say(Fl_pi, "Не знаю. Скажем так, я уже точно не понимаю, чего я хочу на самом деле и кем я теперь являюсь...")
    $ Fl.HideScreens(_with=Fl_fast)


    scene cg Fl_miku_piano with Fl_flash
    $ Fl.Pause (0.5)
    scene cg Fl_mi_guitar with Fl_flash
    $ Fl.Pause (0.5)
    scene bg Fl_ext_musclub_day with Fl_flash
    $ Fl.Pause (1.5)

    scene bg Fl_ext_musclub_night2 with Fl_flash
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Добежав до музклуба, я никого не заметил. Всё было чисто.")
    $ Fl.say(Fl_r, "Стоило мне только подойти, как...")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.say(Fl_r, "Удар со спины не заставил себя долго ждать.", _with=hpunch)
    $ Fl.say(Fl_r, "Получив не хилый удар с ноги в спину, я отпрыгнул в сторону. Моим врагом оказался ещё один клон.")
    $ Fl.say(Fl_pi, "Опять!", _with=hpunch)
    $ Fl.say(Fl_r, "В здании послышались голоса, в том числе и крик аквамариновой пионерки.")
    $ Fl.say(Fl_r, "Пионеры были уже здесь, и один из них встал у меня на пути.")
    $ Fl.say(Fl_pi, "Какой вам прок от того, что вы работаете на эту мразь?")
    $ Fl.say(Fl_r, "В ответ же пионер только рассмеялся.")
    $ Fl.say(Fl_pior, "Какой говоришь?")
    $ Fl.say(Fl_pior, "Он... он убьёт нас... Нет. {w}Он сделает с нами нечто похуже... {w}Сыграет злую шутку. {w}Выкинет наши тела, воспользовавшись ими в своих целях и заберёт нашу душу.")
    $ Fl.say(Fl_r, "Я воспринял его слова как данное, ведь ничего другого они не заслужили. Но что именно он имел виду в последнем предложении?")
    $ Fl.say(Fl_r, "Лицо пионера резко изменилось. Теперь он с серьёзным видом стоял и пилил меня взглядом.")
    $ Fl.say(Fl_pior, "Я д-до сих помню изуродованное тело того парня... {w}Остатки человеческого лица и снятая заживо кожа.")
    $ Fl.say(Fl_th, "Это даже не чудовище это...")
    $ Fl.say(Fl_th, "Стоп! Он же время тянет!")
    $ Fl.say(Fl_pi, "Хватит пудрить мне мозги!")
    $ Fl.say(Fl_r, "Удар. {w}Ещё. {w}Крик. {w}Всё смешалось.")
    $ Fl.StopMusic(6)

    $ Fl.say(Fl_pior, "С-спасибо...")
    $ Fl.say(Fl_r, "На его лица застыла благодарная улыбка.")
    $ Fl.say(Fl_th, "Да что тут мать вашу происходит?!")
    $ Fl.say(Fl_r, "Я не понимал уже ничего. {w}С каждой секундой в мой мозг поступало всё больше вопросов. {w}Но сейчас мне было не до этого.")
    $ Fl.say(Fl_r, "Я влетел внутрь здания.")

    scene bg Fl_int_musclub_night with Fl_flash
    $ Fl.say(Fl_r, "Лунный свет озарил центр помещения...")
    $ Fl.say(Fl_r, "Увидев данную картину я потерял дар речи.")
    $ Fl.HideScreens(_with=Fl_fast)


    $ persistent.Fl_photo_pallery_14 = True
    scene cg Fl_mik with Fl_flash:
        subpixel True
        zoom 1.5 xalign 0.5 yalign 0.85
        ease 6.0 zoom 1.0

    $ Fl.Pause (7.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Посередине комнаты стоял очередной пионер, держа нож у горла Мику.")
    $ Fl.say(Fl_r, "Увидев меня, пионер лишь оскалился больше и поднёс нож к горлу ближе.")
    $ Fl.say(Fl_r, "Тело онемело, сердце начало выдавать 120 ударов в минуту.")
    $ Fl.say(Fl_pi, "Стой!", _with=hpunch)
    $ Fl.say(Fl_pi, "ОСТАНОВИСЬ!", _with=hpunch)
    $ Fl.say(Fl_r, "Её волосы нежно покачивались от небольшого ветра, проникающего внутрь.{w} На её лице одновременно смешались страх, отчаяние, тревога.")
    $ Fl.say(Fl_pior, "Стой на месте и не рыпайся, иначе...")
    $ Fl.say(Fl_r, "Он демонстративно сдвинул нож ещё на сантиметр.")
    $ Fl.say(Fl_r, "Его тональность менялась очень быстро, то вверх, то вниз. {w}А на лице у него застыла улыбка{mn} Моя...")

    $ Fl.PlayMusic("Fl_sayonara", 1, 8)
    $ Fl.say(Fl_pior, "Остановиться!? Зачем!? {w}Мне нравится заниматься этим!")
    $ Fl.say(Fl_r, "Единственное, что мне оставалось - искать момент для спасения Мику.")
    $ Fl.say(Fl_r, "Я сорвался на крик.")
    $ Fl.say(Fl_pi, "Думаешь станет легче?! {w}Не станет! Уж поверь мне, не станет!")
    $ Fl.say(Fl_pi, "Я ведь такой же как ты! {w}Просто посмотри, что происходит вокруг!")
    $ Fl.say(Fl_pi, "Мы для них - просто игрушки! {w}Неважно как, и когда, они просто избаваться от нас! {w}Главное, чтобы мы исполняли то, что нам скажут!")
    $ Fl.say(Fl_r, "Мику лишь еле заметно улыбнулась, не проронив ни слова.")
    $ Fl.say(Fl_r, "Взгляд пионера поменялся. Он посмотрел на меня как-то иначе.")
    $ Fl.say(Fl_pior, "Ты знаешь, а ведь ты прав... {w}Прав в том, что мы — пешки!")
    $ Fl.say(Fl_r, "Он внезапно понизил тон, продолжая уже шёпотом.")
    $ Fl.say(Fl_pior, "Но мне нравится убивать...")
    $ Fl.say(Fl_r, "Он улыбнулся и от всей души истерически рассмеялся.")
    $ Fl.say(Fl_r, "Глаза Мику наполнились слезами, которые отблёскивали на свету.")
    $ Fl.say(Fl_mi, "С-сайон-нара...")
    $ Fl.say(Fl_r, "Сказала она своим дрожащим голосом.")
    $ Fl.say(Fl_r, "Пионер замахнулся ножом...")

    scene bg Fl_int_musclub_night with vpunch:
        Fl_run
    $ Fl.say(Fl_r, "Я ринулся со всех ног на пионера.")
    $ Fl.say(Fl_r, "Но было уже поздно...")
    $ Fl.say(Fl_r, "Струя крови сильно прыснула из её перерезанной гортани.", _with=Fl_flash)
    $ Fl.say(Fl_r, "Бордово-красные оттенки наполнили помещение музклуба.")

    scene bg Fl_black with Fl_flash_red
    $ Fl.say(Fl_r, "Дальше всё было как в тумане... {w}Воткнув нож в голову пионера, я быстро подбежал к пионерке, после чего посмотрел на неё.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    scene bg Fl_int_musclub_night with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Её бездыханное тело лежало посередине клуба, совершенно не подавая какие-либо признаки жизни.")
    $ Fl.say(Fl_r, "Я легонько поднял её на руки и заглянул прямо в глаза.")
    $ Fl.say(Fl_r, "Они были кристально чистые. {w}И смотрели вникуда.")
    $ Fl.say(Fl_r, "Легонько закрыв её глаза рукой, я вместе с ней на руках, облокотился об стену.")
    $ Fl.say(Fl_th, "Такой жизнерадостной{mn} и весёлой{mn} просто не стало...")
    $ Fl.say(Fl_r, "Слёзы, которые начали капать на её тело...{w} Оказались моими.")
    $ Fl.say(Fl_pi, "Почему...")
    $ Fl.say(Fl_pi, "ПОЧЕМУ?!", _with=hpunch)
    $ Fl.say(Fl_r, "Я просто не мог поверить в то, что она погибла.")
    $ Fl.say(Fl_r, "Кричал, бился об стену, снова плакал, молился... {w}Надеялся на чудо.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Но чуда не произошло... да и не могло. {w}Ведь в реальной жизни его попросту не существует.")
    $ Fl.say(Fl_r, "В конце концов, я просто пролежал не двигаясь около двух часов рядом с Мику.")
    $ Fl.say(Fl_r, "Той же ночью, я похоронил эту жизнерадостную, и никогда не унывающую пионерку как следует.")
    $ Fl.say(Fl_r, "Наверное, глубоко в душе я понимал, что такое рано или поздно произойдёт, но не мог смириться с этим.")
    $ Fl.say(Fl_r, "На меня нахлынули многие чувства, которые сложно описать словами.{w} Это была как ненависть, так и отчаяние, как гнев, так и безумие вместе с тоской...")
    $ Fl.say(Fl_th, "Я полюбил только одного человека в жизни, но почему тогда сейчас мне так больно?")
    $ Fl.say(Fl_r, "Слова были не нужны, было и так всё понятно.{w} Я давным давно понимал, что меня с ней связывают другие чувства, но признать их снова было бы невыносимо...")
    $ Fl.say(Fl_r, "Было бы просто невыносимо сейчас.")
    $ Fl.say(Fl_pi, "Что я наделал?!", _with=hpunch)
    $ Fl.say(Fl_r, "Всё просто. Именно она когда-то помогла мне. {w}Всегда старалась помочь. {w}А я не ценил этого...")
    $ Fl.say(Fl_r, "Эта была боль утраты. {w}Одна из самых страшных и мучительных.")
    $ Fl.say(Fl_th, "Это всё моя вина...")

    $ Fl.Pause (2.0)
    $ Fl.say(Fl_th, "Почему всё это происходит именно со мной?!")
    $ Fl.HideScreens(_with=Fl_dissolve1)

    $ Fl.Pause (4.0)
    scene bg Fl_int_musclub_day with Fl_dissolve3
    $ Fl.Pause (3.0)
    scene bg Fl_int_musclub_sunset with Fl_dissolve2
    $ Fl.Pause (3.0)
    scene bg Fl_int_musclub_night with Fl_dissolve2
    $ Fl.Pause (1.5)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Следующий день я провёл... никак.{w} Я просто сидел внутри музклуба, смотря в одну точку. {w}Сидел, не замечая ничего вокруг.")
    $ Fl.say(Fl_r, "Мои глаза были кристально чисты. {w}Настолько, что в них отражался пол музыкального клуба.")
    $ Fl.say(Fl_r, "В тот момент мне было плевать на всё. {w}Самому мне просто уже не хватало сил... {w}Пожалуйста, пусть всё это закончится.")
    $ Fl.say(Fl_r, "Если мне не хватает сил защитить даже одного близкого человека...{w} Что мне делать?!")
    $ Fl.say(Fl_r, "Жить? {w}Ради чего? {w}Ради кого?")
    $ Fl.say(Fl_r, "В голове проносились тысячи разных воспоминаний. {w}Передо мной всплывали сотни разных событий...")

    $ Fl.Pause (2.5)
    $ Fl.say(Fl_r, "Я улыбался. {w}Улыбался тем самым галлюцинациям, которые приходили ко мне в образе Мику.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(11)


    show Fl_prolog_dream with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Я был подавлен.{w} Как физически, так и морально. {w}Внутри была лишь пустота.")
    $ Fl.say(Fl_r, "Из-за моего состояния со мной начали происходить страшные вещи, но я не мог остановить это...")
    $ Fl.say(Fl_r, "Вскоре, перед моим лицом начали всплывать знакомые недавние сцены.")
    hide Fl_prolog_dream with Fl_dissolve1

    $ Fl.say(Fl_r, "Знакомые фразы вгрызались в мой разум, подталкивая на какие-то действия.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.DayTime("rain", "day")
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Слова голоса...")
    $ Fl.Pause (1.0)
    $ Fl.say(Fl_r, "Слова незнакомца...")

    show kr_dream with Fl_dissolve1

    $ Fl.Pause (1.0)
    $ Fl.say(Fl_r, "Кристины...")
    
    hide kr_dream with Fl_dissolve1
    $ Fl.Pause (0.5)
    show mi normal pioneer6 with Fl_dissolve1

    $ Fl.Pause (1.0)
    $ Fl.say(Fl_r, "Мику...")

    hide mi normal pioneer6 with Fl_dissolve1

    $ Fl.Pause (1.0)
    $ Fl.say(Fl_r, "И то, что я обнаружил внутри старого корпуса.")
    $ Fl.HideScreens(_with=Fl_dissolve1)

    scene bg Fl_ext_old_building_night_moonlight
    show Fl_prolog_dream
    $ Fl.Pause (2.5)
    scene bg Fl_int_old_building_night
    show Fl_prolog_dream
    $ Fl.Pause (2.5)
    scene cg Fl_p_say
    show Fl_prolog_dream


    $ Fl.DayTime("kira", "night")

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Я взбесился... {w}Ненависть к пионерам не могла пройти так быстро...")
    $ Fl.say(Fl_r, "Как и гнев за ту, которую убили на моих глазах.")

    scene bg Fl_int_musclub_night with Fl_dissolve2
    $ Fl.say(Fl_r, "Чувства обострились, мозг отдавал команду на включение режима резерного питания, а руки наливались кровью.")
    $ Fl.say(Fl_r, "Я встал и собрался духом. Теперь я был готов отомстить. {w}Нет даже не так. Я теперь жил лишь одной мыслью о мести. {w}Пионерам, Богу, что закинул меня в этот ад.")
    $ Fl.say(Fl_r, "Мне хотелось лично выпотрошить тело того, кто стоит за всем этим. {w}Стереть существование всей грязи пионерлагеря.")
    $ Fl.say(Fl_r, "Теперь я смог лицезреть настоящую сторону лагеря. {w}Тёмную сторону этого «райского» местечка.")

    $ Fl.PlaySound("Fl_open_door_1", 1, 0, False)
    scene bg Fl_ext_musclub_night2 with Fl_dissolve1
    $ Fl.say(Fl_r, "Выйдя на улицу, и взглянув на могилу пионерки, я мысленно поблагодарил, после чего вслух поклялся Мику.")
    $ Fl.say(Fl_pi, "Я лично найду ту мразь, которая за этим всем стоит и прикончу.{w} Прикончу самым ужасным способом... и отомщу за тебя.")
    $ Fl.say(Fl_r, "Конечно, этот способ был негуманным, но меня больше это не волновало.")
    $ Fl.say(Fl_th, "Никто не останется в живых...")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause (2.5)
    $ Fl.PlayMusic("Fl_hydrogen", 1, 3)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Подходя к площади, я услышал музыку, которая играла совсем близко.")

    scene bg Fl_blink_square_party 
    show Fl_dust_full
    with Fl_dissolve1
    $ Fl.say(Fl_r, "Они даже не скрывают своё веселье...")
    $ Fl.say(Fl_r, "Одна моя часть пыталась активировать стоп-кран, вторая же не желала слушать никого и ничего, намереваясь услышать что-то другое вместо музыки. {w}Ответы? {w}А может вопли и хруст костей?")
    $ Fl.say(Fl_r, "Они просто отдыхали... {w}Наслаждались своим превосходством над куклами, играясь с ними из цикла в цикл...")
    $ Fl.say(Fl_r, "Но я видел всё иначе.")
    $ Fl.StopMusic(3)

    $ Fl.Pause (1.5)
    $ Fl.PlayMusic("Fl_acidspeed", 1, 3)
    $ Fl.say(Fl_r, "Подходя к площади, пионеры, замечая меня, начали испытывать разные эмоции.")
    $ Fl.say(Fl_r, "Кто-то начал улыбаться, кто-то стал подходить ближе с серьёзными намерениями...")
    $ Fl.say(Fl_r, "Но все они прекрасно понимали, что я чужак.")
    $ Fl.say(Fl_r, "Четверо кровожадных убийц смотрели на меня, как я неспеша, посмеиваясь подхожу к ним.")
    $ Fl.say(Fl_pib, "Забавно, не так ли? Вы же тоже любите убивать, насиловать и отрезать головы?")
    $ Fl.say(Fl_pib, "Я ведь прав?")
    $ Fl.say(Fl_r, "Я начал громко и истерично хохотать.")

    show pi normal with Fl_fast

    $ Fl.say(Fl_pior, "А я погляжу тебе весело.")
    $ Fl.say(Fl_r, "Начал один.")

    show pi normal with Fl_fast
    $ Fl.Pause (0.1)
    show pi smile with Fl_fast:
        left

    $ Fl.say(Fl_pior, "Да, я смотрю у нас новый гость! {w}Добро пожаловать!")
    $ Fl.say(Fl_r, "Саркастично прикрикнул второй.")

    hide pi smile with Fl_fast
    $ Fl.Pause (0.1)
    show pi smile with Fl_fast

    $ Fl.say(Fl_pior, "Может расскажешь, чего это тебе так весело?")
    $ Fl.say(Fl_pib, "Ребята... {w}мне весело, потому что сейчас... {w}вы превратитись в кучку трупов, вот почему!")
    $ Fl.say(Fl_r, "Ненормально-весёлый голос, которым я говорил, был пугающим.")
    $ Fl.say(Fl_pior, "Да неужели?")

    hide pi smile with Fl_fast

    $ Fl.say(Fl_r, "Он ухмыльнулся, заходя заспину, в то время как другие решили взять меня в кольцо.")
    $ Fl.say(Fl_pior, "Удачи на новом ци-икле-е-е!")
    $ Fl.say(Fl_r, "Безмозглые клоны бросились на меня со всех сторон, немного хихикая.")
    $ Fl.say(Fl_pib, "Тогда начнём!", _with=hpunch)
    $ Fl.HideScreens(_with=Fl_fast)
    jump disco


label disco:
    $ Fl.PlayMusicFrom("<from 34 to 72>", "Fl_acidspeed", 1, 0)
    scene bg Fl_blink_square_diskach1
    $ Fl.Pause (2.5)
    scene bg Fl_blink_square_diskach2
    call screen Fl_disco_qte(randint(0, 6), 0.8, "disco_lose") with vpunch
    jump disco_2




label disco_2:
    call screen Fl_disco_qte(randint(0, 6), 0.9, "disco_lose") with Fade(0.10, 0.20, 0.10, color="990000")
    jump disco_3

label disco_3:
    call screen Fl_disco_qte(randint(0, 6), 0.8, "disco_lose") with hpunch
    jump disco_4

label disco_4:
    call screen Fl_disco_qte(randint(0, 6), 0.8, "disco_lose") with Fade(0.15, 0.10, 0.0, color="ffffff")
    jump disco_5

label disco_5:
    call screen Fl_disco_qte(randint(0, 6), 0.9, "disco_lose") with vpunch
    jump disco_6

label disco_6:
    call screen Fl_disco_qte(randint(0, 6), 0.8, "disco_lose") with Fade(0.10, 0.20, 0.10, color="990000")
    jump disco_win




label disco_lose:
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Неожиданно, пионер ударил меня в солнечное сплетение и я начал задыхаться...")
    $ Fl.say(Fl_r, "Вылавливая момент, все остальные яростно накинулись на меня, начиная избивать руками и ногами.")
    $ Fl.say(Fl_r, "Из носа шла кровь, рука была полностью в крови, а организм пытался высвободиться от собственной крови, пытаясь выплюнуть её через рот.")
    $ Fl.say(Fl_r, "Было больно, но я знал, что против четверых такое ничтожество, как я, которое не смогло защитить даже одного, ничего не сможет противопоставить...")
    $ Fl.say(Fl_r, "Удар в челюсть с ноги, и я начинаю терять контроль над своим разумом.{w} Он прекращает выполнять свои команды, а глаза сами собой начинают закрываться.")
    $ Fl.say(Fl_th, "На новый цикл?..")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2
    jump pi_say3


label pi_say3:
    $ Fl.Pause (5.0)
    show text "{font=font/Fl_mainmenu.ttf}{size=55}И куда ты собрался?{/size}{/font}"
    with Fl_dissolve1

    $ Fl.Pause (3.0)
    show text "{font=font/Fl_mainmenu.ttf}{size=55}Я не позволю тебе просто так слиться.{/size}{/font}"
    with Fl_dissolve1

    $ Fl.Pause (3.0)
    show text "{font=font/Fl_mainmenu.ttf}{size=55}Поэтому будь добр, избавься от этого отродья!{/size}{/font}"
    with Fl_dissolve1
    jump disco




label disco_win:
    $ Fl.StopMusic(7)
    $ Fl.PlayAmbience("Fl_camp_center_night", 1, 4)
    scene bg Fl_blink_square_party with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Жестокая битва закончилась абсолютным погромом пионеров.")
    $ Fl.say(Fl_r, "На меня было жалко смотреть: весь ободранный, в пыли и грязи, я шёл куда-то, где, мне казалось, ещё существует способ отдохнуть.")
    $ Fl.say(Fl_r, "Кровь стекала по моим рукам... {w}Лицо было всё в крови тех самых обычных «советских пионеров».")
    $ Fl.say(Fl_r, "Всё тело ныло, отзываясь адской болью.")
    $ Fl.say(Fl_r, "Любому будет ясно, что против четвертых мне было не устоять, но во мне играл безумный азарт, да и практики было много...")
    $ Fl.say(Fl_r, "Главная площадь была изуродована. {w}Побитые лавки, лужицы крови... {w}Картину завершали огни от гирлянд, освещающие всё это красочными цветами.")
    $ Fl.say(Fl_r, "Я продолжил следовать в место, где смогу со спокойной совестью отдохнуть.")
    $ Fl.say(Fl_th, "Пляж ведь неплохое место{mn} Песок, вода...")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(5)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.DayTime("night", "night")


    $ Fl.Pause (6.0)
    $ Fl.PlayAmbience("Fl_boat_station_night", 1, 4)
    scene bg Fl_ext_beach_night 
    show Fl_dust_full
    with Fl_dissolve3
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "По мере приближения к морю всё яснее был слышен неумолкающий ни на минуту шум беспокойных волн.")
    $ Fl.say(Fl_th, "Красиво... {w}И спокойно...")
    $ Fl.say(Fl_r, "Я долго восхищался пейзажом водной глади под светом луны. {w}Пока вдали на песке не заметил женский силуэт...")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Рядом со мной сидела девушка в коричневом платье с кашатоновым цветом волос. Она смотрела прямо на меня своими жёлтыми, словно янтарного оттенка, глазами. {w}На её лице читалось сочувствие.")
    $ Fl.say(Fl_r, "Я не знал как давно она вот так сидела возле меня, видно слишком увлёкся, смывая кровь своих рук.")
    $ Fl.say(Fl_kuv, "Правда тут красиво?")
    $ Fl.say(Fl_r, "Тихо сказала она, нисколечки не смущаясь моего внешнего вида.")
    $ Fl.say(Fl_r, "Непроронив ни слова, я молча сидел и смотрел в даль. {w}Странная незнакомка мало меня сейчас интересовала.")
    $ Fl.say(Fl_kuv, "...Мне вот нравится пляж и лес, там всегда можно побыть наедине с собой, поразмышлять о своём. Ты так не думаешь?")
    $ Fl.say(Fl_th, "Думаю{mn} А о чём я сейчас думаю? {w}Наверное о чём нибудь глубоком? {w}А может о грёзах несбывшегося будущего? {w}Не знаю.")
    $ Fl.say(Fl_r, "Внутри было холодно и мерзко.")
    $ Fl.say(Fl_kuv, "Ты не особо разговорчивый, да?")
    $ Fl.say(Fl_r, "Поникнув, задала свой вопрос девушка.")
    $ Fl.say(Fl_pi, "Кто ты?")
    $ Fl.say(Fl_r, "С трудом выдавил из себя я.")

    $ Fl.Pause (2.0)
    $ Fl.say(Fl_r, "Девушка молчала. Она просто печальным взглядом смотрела на луну. {w}Это пробудило во мне интерес к незнакомке.")
    $ Fl.say(Fl_kuv, "Ты правда хочешь знать?")
    $ Fl.say(Fl_r, "Сказала девушка с грустью на лице.")
    $ Fl.say(Fl_th, "Хочу ли я знать? {w}Наверное. Правда я уже сам не знаю чего я хочу...")
    $ Fl.say(Fl_pi, "Да.")
    $ Fl.say(Fl_r, "Внутренее любопытсво ответило за меня.")
    $ Fl.say(Fl_r, "Девушка медленно встала, луна отразилась в её глазах, а ночной свет озарил её мягкую улыбку.")

    show uv smile d2 n with Fl_dissolve1

    $ Fl.say(Fl_uv, "Меня зовут - Юля. {w}И я - бог этого мира.")
    $ Fl.HideScreens()


    show Fl_prolog_dream
    $ Fl.Pause(1.0)
    hide Fl_prolog_dream

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Что?")
    $ Fl.say(Fl_r, "От её слов, мне стало дурно. Всё тело сковал страх, а голова жутко загудела.")

    show Fl_vignette2 with hpunch
    $ Fl.Master(Fl_bghorrorflicker)
    $ Fl.say(Fl_r, "Я схватился за голову. {w}Боль в висках усиливалась. {w}В глазах темнело. {w}Сознание отключалось.")
    $ Fl.say(Fl_th, "Бог? {w}Вот как...")

    show uv sad d1 n with Fl_fast
    $ Fl.say(Fl_uv, "Что с то{break}")
    $ Fl.HideScreens()
    scene bg Fl_black with vpunch
    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    $ Fl.StopAmbience(4)


    $ Fl.Pause(8.0)
    $ Fl.DayTime("rain", "night")


    $ Fl.PlayAmbience("Fl_rain", 1, 7)
    $ Fl.PlayMusic("Fl_developers_music", 1, 7)
    scene cg Fl_dead_gg_wosp_light 
    $ persistent.Fl_photo_pallery_19 = True
    show Fl_rain_hard_left
    with Fl_dissolve5
    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Холодный и непрекращающийся ливень, заглушал всё вокруг.")
    $ Fl.say(Fl_r, "Я лёжа на земле, наблюдал как капли отскакивают от поверхности. {w}Мне осталось немного...")
    $ Fl.say(Fl_r, "По моему лицу стекала алая жидкость, одним словом моя кровь. {w}От меня не осталось и живого места, все конечности ныли, а некоторые я даже не чувствовал.")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_r, "Никто не мог предсказать такой конец. {w}Никто...")
    $ Fl.say(Fl_r, "Автобус на котором мы собирались добраться до райцентра, попал в аварию...")
    $ Fl.say(Fl_r, "Корчась от боли я попытался отыскать взглядом Кристину. И мне это удалось. {w}Она висела меж салоном и лобовым стеклом.")
    $ Fl.say(Fl_r, "Кровавое тело моей девушки, заставило меня резко вскочить с жутким криком отчаяния.")
    $ Fl.say(Fl_gg, "КРИСТИНА!", _with=hpunch)
    $ Fl.say(Fl_r, "Но не успел я подняться, как моё тело сразу же упало в холодную лужу.")
    $ Fl.say(Fl_gg, "НЕТ! КРИСТИНА!", _with=hpunch)
    $ Fl.say(Fl_r, "Пионерка не отвечала, а продолжала находиться в том же положении.")
    $ Fl.say(Fl_r, "Я начал ползти к ней. Малейшее движение отзывалось жуткой болью, но я продолжал.")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_gg, "Кристина?")

    $ Fl.Pause(1.0)
    $ Fl.say(Fl_r, "Но произошло то чего я больше всего на свете боялся...")
    $ Fl.say(Fl_gg, "Н-нет{mn} Нет...")
    $ Fl.say(Fl_gg, "Этого н-не м-может быть...")
    $ Fl.say(Fl_r, "Я упал на мокрый асфальт. {w}Из моих глаз потекли слёзы.")
    $ Fl.say(Fl_th, "Как такое могло произойти? {w}ПОЧЕМУ НЕ Я?")
    $ Fl.say(Fl_r, "Вдали послышались приглушённое шлёпанье по лужам. Кто-то приближался.")
    $ Fl.say(Fl_r, "Я медленно поднял голову в сторону звуков.")
    $ Fl.say(Fl_r, "На крыше автобуса был силуэт. Из-за того что мне в глаза попала кровь оттенок окружающего мира исказился и мне было тяжело определить кому именно этот силуэт принадлежит.")
    $ Fl.say(Fl_th, "Женщина?")
    $ Fl.say(Fl_r, "Фигура с длинными волосами была одета в платье - единственная моя зацепка, которая разрушила все мои сомнения.")
    $ Fl.say(Fl_gg, "К-кто ты?")
    $ Fl.say(Fl_kuv, "Бог - этого мира.")
    $ Fl.say(Fl_gg, "Зачем ты здесь?")
    $ Fl.say(Fl_kuv, "Мне было скучно поэтому я решила немного прогуляться.")
    $ Fl.say(Fl_r, "В голосе девушки читалось недовольство, ей явно было скучно вести диалог с полуживым трупом.")
    $ Fl.say(Fl_gg, "Бог{mn} Бог!")
    $ Fl.say(Fl_gg, "Ты же можешь спасти её, правда?")
    $ Fl.say(Fl_kuv, "Могу...")
    $ Fl.say(Fl_r, "Глубоко внутри во мне зародилась надежда. Эта надежда, дала своего рода выброс адреналина. Я немного поднялся, чтобы лучше разглядеть фигуру.")
    $ Fl.say(Fl_kuv, "Но я не хочу.")
    $ Fl.say(Fl_gg, "Что? Почему?")
    $ Fl.say(Fl_kuv, "Это не в моих интересах спасать её. Она мертва, смирись.")
    $ Fl.say(Fl_th, "Нет - нет. Этого не может быть...")
    $ Fl.say(Fl_gg, "Но ты же бог! Чего тебе стоит спасти одну жизнь?")
    $ Fl.say(Fl_kuv, "И что с того? Меня не волнует жизнь жалких людишек.")
    $ Fl.say(Fl_r, "Я не верил своим ушам. {w}Я бы никогда не поверил бы что бог этого прекрасного рая окажется бесчувственным наблюдателем, неболее.")
    $ Fl.say(Fl_r, "Девушка встала и развернулась. Продолжать общение со мной она была не намерена.")
    $ Fl.say(Fl_gg, "Т-тогда{mn}")
    $ Fl.say(Fl_gg, "Я отдам тебе всё что ты пожелаешь! {w}Я готов на всё, только спаси её!")
    $ Fl.say(Fl_r, "Бог остановился и медленно повернулся в мою сторону.")
    $ Fl.say(Fl_kuv, "Вот как. {w}Тогда это всё меняет.")
    $ Fl.say(Fl_r, "Я противясь ноющей боли поднялся на ноги. Балансируя я смотрел ей прямо в её жёлтые глаза, на которые падали каштанового цвета локаны.")
    $ Fl.say(Fl_kuv, "Тогда ты не против если я заберу твою душу в своё подчинение?")
    $ Fl.say(Fl_gg, "Я согласен. {w}Это малая жертва за её жизнь.")
    $ Fl.say(Fl_kuv, "Пускай будет по-твоему...")
    $ Fl.say(Fl_r, "Девушка протянула руку. {w}А я недолго думая протянул свою.")

    $ Fl.Pause(2.5)
    $ Fl.say(Fl_r, "Наверное вы ожидали, что сейчас что-то произойдёт, яркая вспышка света или тёмная аура вокруг меня, забирающая мою душу. Но нет. Ничего. Я просто упал не в силах терпеть эту адскую боль.")
    $ Fl.say(Fl_kuv, "Ты ещё пожалеешь об этом...")
    $ Fl.say(Fl_r, "Тихо произнёс бог.")
    $ Fl.say(Fl_th, "Да так и есть. Но другого выбора у меня не было иначе она бы умерла. {w}Я бы не простил себя, если такой лучик света погас из-за меня. {w}Из-за моей беспомощности...")
    
    show Fl_prolog_dream with Fl_dissolve1
    $ Fl.say(Fl_r, "Силуэт божетсва расстворился за занавесом дыма и дождя.")

    $ Fl.ShowBlink() 
    $ Fl.say(Fl_r, "Глаза закрылись сами по себе. Перед тем как издать последний вздох, я увидел, как пальцы Кристины задёргались...")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1 
    $ Fl.HideBlink() 
    $ Fl.StopAmbience(4)


    $ Fl.Pause(8.0)
    $ Fl.DayTime("night", "night")


    scene bg Fl_ext_beach_night
    show Fl_dust_full
    with Fl_dissolve3
    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Вовзращаясь к реалиям, мне наконец-то удалось собрать мозаику из своих воспоминаний воедино.")
    $ Fl.say(Fl_r, "Пережить всё это вновь было такое себе удовольствие, но теперь всё закончилось.")
    $ Fl.HideScreens(_with=Fl_fast)


    scene Fl_ext_camp_entrance_night_vision
    show Fl_smoke
    show Fl_entrance_night_vision_layer
    show Fl_ext_camp_entrance_night_vision_uvao 
    with Fl_flash
    $ Fl.Pause(1.0)

    show Fl_prolog_dream with Fl_dissolve2
    $ Fl.Pause(2.0)
    scene bg Fl_black with Fl_dissolve1

    $ Fl.Pause(1.0)
    scene bg Fl_ext_beach_night
    show Fl_dust_full
    with Fl_fast
    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Теперь я вспомнил всё...")
    $ Fl.say(Fl_th, "Бог этого мира - маленькая девочка. {w}Девочка, которая подарила мне путёвку в ад с гордым названием «Совёнок».")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_th, "Боги и правда очень жестоки.")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_th, "И я вас ненавижу...")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_r, "Я рассмеялся.")
    $ Fl.say(Fl_th, "А забавно получилось. Я всё время проклинал тебя, а теперь даже не знаю что делать.")
    $ Fl.say(Fl_th, "Значит пионерлагерь был всего лишь дешёвым капканом, который заманивал в свои лапы наивных, таких как я, а после отбирал всё и игрался с ними, словно куклами, дергая за ниточки.")
    $ Fl.say(Fl_th, "Да уж бог этого мира и правда {b}НЕВЕРОЯТЕН{/b}! {w}ГЕНИЙ, МАТЬ ВАШУ!")
    $ Fl.say(Fl_r, "Я продолжал издавать тихие смешки.")

    show uv sad d1 n with Fl_fast

    $ Fl.say(Fl_uv, "Ян, ты в порядке?")
    $ Fl.say(Fl_th, "Хахаха. В порядки ли я? {w}Ты издеваешь надо мной?")
    $ Fl.say(Fl_th, "Ты, забрала меня в этот ад. {w}Подарила надежду, любовь. {w}Создала иллюзии... {w}А после разрушила всё в один миг.")
    $ Fl.say(Fl_th, "Да, конечно, я в порядке! {w}Лицемерка!")

    show uv smile d2 n with Fl_dissolve1

    $ Fl.say(Fl_uv, "Ясно. Значит ты всё вспомнил...")
    $ Fl.say(Fl_r, "Внутри меня всё пылало. Я испытывал каждую секунду спектр эмоций. {w}То хотелось плакать, то смеяться, то впасть депрессию...")
    $ Fl.say(Fl_th, "Ненавижу{mn} Как же я ненавижу этот мир!")
    $ Fl.say(Fl_r, "Девушка медленно протянула руку. На её лице читалась добрая улыбка.")

    show Fl_vignette3 with Fl_flash
    $ Fl.DayTime("kira", "night")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    hide uv smile d2 n with vpunch

    $ Fl.say(Fl_pib, "Я НЕНАВИЖУ ТЕБЯ!", _with=hpunch)
    $ Fl.say(Fl_r, "Я грубо отказался от доброго жеста девушки, ударив её сильно по щеке.")
    $ Fl.say(Fl_pib, "Дважды я на это не куплюсь!", _with=hpunch)
    $ Fl.say(Fl_r, "Юля посмотрела на меня испуганным взглядом. Её глаза блеснули, но она не проронила ни слезинки.")
    $ Fl.say(Fl_r, "Я же в очередной раз потеряв контроль над своим телом, схватил двумя руками девушку за горло и опустил в воду.")
    $ Fl.say(Fl_pib, "Из-за тебя! {w}Из-за тебя!")
    $ Fl.say(Fl_pib, "Из-за тебя все они...")
    $ Fl.say(Fl_r, "В порыве эмоция, я не мог связать свою мысль. На этот раз мной двигало не безумие, а отчаяние.")
    $ Fl.say(Fl_r, "Юля царапала мои руки, в попытках ослабить хватку вокруг шеи. {w}Её глаза были наполнены самым что ни на есть настоящим ужасом.")
    $ Fl.say(Fl_th, "Тогда, ты могла спасти её, но ты посчитала что, спасение чей-то жизни - это скучно!")
    $ Fl.say(Fl_th, "Для тебя мы всего лишь игрушки, куклы в твоём маленьком спектакле{mn} Все наши страдания из-за тебя!")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_r, "На поверхность воды, поднималось всё больше пузырей. {w}Девушка всем видом молила, чтобы я остановился. {w}Но я только сильнее сжимал её горло.")
    $ Fl.say(Fl_th, "Прощай. Надеюсь ты заберёшь пионерлагерь с собой прямо в ад!")
    $ Fl.StopMusic()


    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    scene bg Fl_black with Fl_flash_red

    $ Fl.AttackScreens(True)
    $ Fl.say(Fl_pib, "ААААААА!", _with=hpunch)
    $ Fl.say(Fl_r, "Ощутив жгую боль на лице, я заорал что есть силы. {w}От собственного рёва у меня заложило уши.")
    $ Fl.say(Fl_r, "В тот же миг по лицу начала стекать тёплая жидкость алого цвета.")
    $ Fl.say(Fl_th, "Кровь? {w}Чем же она меня так рубанула?!")
    $ Fl.say(Fl_th, "Камнем? {w}Ракушкой? {w}Нет явно чем-то другим.")
    $ Fl.say(Fl_r, "Отойдя от болевого шока, я наконец-то смог открыть свои глаза.")
    $ Fl.say(Fl_r, "И обомлел...")

    scene bg Fl_ext_beach_night
    show Fl_dust_full
    show uv rage d1
    show Fl_vignette
    with Fl_flash2

    $ Fl.PlayMusic("Fl_danger", 1, 4)
    $ Fl.say(Fl_r, "Перед моими глазами стояла Юля. {w}Всё в том же коричневом платье. Но уже на её голове красовалась пара кошачих ушей и хвост.")
    $ Fl.say(Fl_uv, "Ну и какого это, когда причиняют боль тебе?")
    $ Fl.say(Fl_r, "Я только сейчас заметил на её пальцах длинные когти, которыми скорее всего она мне нанесла фатальный урон по лицу.")
    $ Fl.say(Fl_th, "Саваринеко? {w}Да вы <бл*ть> издеваетесь?!")
    $ Fl.say(Fl_th, "Я конечно понимал, что бог этого мира будет иметь силы выходящие за гранью науки, но чтобы он был гибридом кошки и человека...")
    $ Fl.say(Fl_pib, "Хочу задать тебе тот же вопрос, киса!")
    $ Fl.say(Fl_r, "Я моментально сократил между нами дистанцию.")
    $ Fl.say(Fl_r, "Замах.")

    with Fl_flash_fast
    scene bg Fl_blink_square_party
    show Fl_dust_full
    show Fl_vignette
    with vpunch

    $ Fl.say(Fl_r, "И сразу же отскочил назад.")
    $ Fl.say(Fl_th, "Что это было?")
    $ Fl.say(Fl_r, "Я быстро оглянулся. {w}Песок сменился на бетон, а пейзаж пляжа на уже родную мне площадь с неизвестным Гендой.")
    $ Fl.say(Fl_th, "Это она нас сюда перенесла?")
    $ Fl.say(Fl_r, "Я одарил девушку удивлённым взглядом.")
    $ Fl.say(Fl_pib, "Твоих рук дело?")
    $ Fl.say(Fl_r, "Неко расплылась в улыбке. Она весело захихикала, гордясь своей выходке.")
    $ Fl.say(Fl_th, "Понятно{mn} Чего ещё стоило ожидать от бога...")
    $ Fl.say(Fl_uv, "Может ты прекратишь это? {w}Пока не поздно.")
    $ Fl.say(Fl_pib, "Прекратить? О чём это ты?")
    $ Fl.say(Fl_r, "Я широко улыбнулся.")
    $ Fl.say(Fl_pib, "Я ещё даже не начинал.")
    $ Fl.say(Fl_pib, "С чего вдруг такая забота? {w}Тебе ведь дела нет до жителей твоего мира.")
    $ Fl.say(Fl_r, "От улыбки девушки не осталось и следа.")
    $ Fl.say(Fl_pib, "Ты хоть знаешь сколько раз я тебя умолял?")
    $ Fl.say(Fl_pib, "Сколько просил о помощи?! {w}ЧТОБЫ ТЫ СПАСЛА МЕНЯ?!")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_pib, "Сколько раз проклинал тебя...")
    $ Fl.say(Fl_uv, "В этом только твоя вина! Нечего меня винить!")
    $ Fl.say(Fl_pib, "Тогда скажи мне, какого это наблюдать сверху как кто-то страдает? Какого это дёргать за ниточки, словно мы обычные марионетки?")
    $ Fl.say(Fl_r, "Неко заскрипела зубами, обнажая свои когти.")
    $ Fl.say(Fl_pib, "Что правда в глаза колит?")
    $ Fl.say(Fl_uv, "Я{mn} я{mn} Я ненавижу вас людей! {w}И тебя я тоже ненавижу!")
    $ Fl.say(Fl_r, "Она дрожала. Слова давались с трудом, но она старалась из-за всех сил взять себя в руки.")
    $ Fl.say(Fl_uv, "По сравнению со мной люди ещё те чудовища!")
    $ Fl.say(Fl_r, "В мгновение ока неко совершила кувырок, собираясь нанести удар сверху.")

    $ Fl.AttackScreens()
    $ Fl.say(Fl_r, "Я отпрыгнул на добрых пару метров.")
    $ Fl.say(Fl_th, "Как забавно, теперь мы оба хотим убить друг друга.")
    $ Fl.StopMusic(4)

    $ Fl.say(Fl_r, "На главной площади лагеря назревала битва двух монстров. Они смотрели друг на друга хищным взглядом. Цель была едина - остаться одному из них в живых, оставив на всегда свои разногласия.")
    $ Fl.say(Fl_pib, "Тогда начнём!")

    $ Fl.PlayMusicFrom("<from 0 to 122>", "Fl_black_stripe_woho", 1, 2)
    $ Fl.Pause(1.5)
    $ Fl.say(Fl_r, "Неко словно сорвалась с цепи, по скорости она явно превосходила меня. Мне с трудом приходилось избегать град атак.")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.say(Fl_r, "Выждав момент, я со всей силы ударил в живот неко с ноги.")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.say(Fl_r, "Не став не терять ни секунды я пропечатал ещё раз с ноги. Но неко среагировала быстрее и мой удар пришёлся умывальнику.")
    $ Fl.say(Fl_r, "Из-за того что кровь со лба попала в правый глаз. Частично вся правая сторона стала своего рода слепой зоной для меня. {w}Поэтому я не смог быстро среагировать на когти, устремлённые прямо в область живота.")
    $ Fl.say(Fl_th, "Чёрт!")
    $ Fl.say(Fl_r, "Кое-как мне удалось избежать атаки, отделавшись всего лишь царапиной.")
    $ Fl.say(Fl_uv, "Ты и правда чудовище...")
    $ Fl.say(Fl_r, "В ответ я лишь оскалился.")
    $ Fl.say(Fl_r, "Я приготовился к следующей атаки.")
    $ Fl.say(Fl_r, "Неко неслась с растопыренными руками. Что дало мне идеально совершить удар с правой руки по лицу.")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.Pause(0.3)
    $ Fl.PlaySound("Fl_bones_breaking", 1, 0, False)
    $ Fl.say(Fl_pib, "Что?{break2}")

    show Fl_blood_eff with Fl_flash_red
    $ Fl.AttackScreens(True)
    $ Fl.say(Fl_pib, "ААААААА!!!", _with=hpunch)
    $ Fl.say(Fl_r, "Я завопил от адской боли, что моментально пронеслась по всему телу. {w}Я потерял равновесие и мне пришлось опереться на всё тот же умывальник.")
    $ Fl.say(Fl_r, "Я сжимал праву конечность. {w}Кровь фонтаном шла из логтя. Всё что было ниже локтевой ямки отсуствовало.")
    $ Fl.say(Fl_th, "Как же больно <с*ка>!")
    $ Fl.say(Fl_r, "Мне ещё ни разу не отрывали конечность. {w}Боль была невыносима, настолько что сознание с каждой секундой затухало. Но адреналин и безумие не давали мне отключиться.")
    $ Fl.say(Fl_r, "Я перевёл взгляд через спину на неко. Она вальяжно выкинула мою правую руку в кусты.")
    $ Fl.say(Fl_pib, "Хаххаахах. А ты хороша!")
    $ Fl.say(Fl_r, "Безумие вновь взяло моё тело и разум под контроль, заглушая адскую боль.")
    $ Fl.say(Fl_uv, "Т-тц.")
    $ Fl.say(Fl_r, "Цокнув, неко вновь сократила дистанцию между нами. {w}Её когти вновь направились в мою сторону.")
    $ Fl.say(Fl_r, "Но какая-то неведомая сила управляла мной. Вся картина перед глазами залилась красной пеленой. {w}Я потерял контроль над собой окончательно.")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.say(Fl_r, "Я закружился и совсей силы с вертушки нанёс сильный удар слевой ноги. Девушка аж подлетела в воздух от такого удара.")
    $ Fl.say(Fl_r, "Я смеялся совершая очередной удар.")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.say(Fl_r, "Апперкот слевой. {w}Ещё один удар слевой прямо в лицо.")
    if persistent.Fl_dictionary_10 == False:
        $ Fl.PodskDict()
    $ persistent.Fl_dictionary_10 = True
    $ Fl.say(Fl_r, "Никто ведь не говорил, что я правша так ведь? {w}Я с рождения {i}амбидекстр{/i}.")
    $ Fl.say(Fl_r, "Я поднял девушку за волосы.")
    $ Fl.say(Fl_th, "Что за?!")
    $ Fl.say(Fl_r, "Прямо на моих глазах, все травмы что я нанёс неко, заживали у меня прямо на глазах.")
    $ Fl.say(Fl_uv, "Ты и правда думал, что сможешь убить меня.")
    $ Fl.say(Fl_r, "Заскрипев зубами, я собирался разбить голову девушки.")
    $ Fl.say(Fl_r, "Неко выставила руку.")

    $ Fl.PlaySound("Fl_bones_breaking", 1, 0, False)
    with hpunch

    $ Fl.AttackScreens(True)
    $ Fl.say(Fl_r, "После чего меня откинуло невидимой волной и впечатало прямо в памятник.", _with=hpunch)

    with Fl_flash_red
    $ Fl.say(Fl_r, "Послышался хруст костей. {w}Множество ребёр было сломано. {w}А левая часть тела больше меня не слушалась.")
    $ Fl.say(Fl_r, "Чудовище, что величает себя Богом, наклонилось.")
    $ Fl.say(Fl_uv, "Это было глупо.")
    $ Fl.say(Fl_r, "Я рассмеялся, но сразу притих.")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_th, "Я проиграл... {w}Хах, забавно...")
    $ Fl.say(Fl_th, "У меня не было и шансов уничтожить самого создателя этого лагеря, на что я только надеялся.")
    $ Fl.say(Fl_th, "Просто моё безумие оказалось бессильным, против разрушительной силы богов.")
    $ Fl.say(Fl_uv, "Но знаешь, я удивлена. {w}Будучи нулевым ты сражался слишком хорошо.")
    $ Fl.say(Fl_pib, "Н-нулевым?")
    $ Fl.say(Fl_uv, "Не прикидывайся дураком! Ты знаешь о чём идёт речь.")
    $ Fl.say(Fl_th, "Нет, я не знаю! {w}Я ничего не знаю об этом месте и о его странных обитателях!")
    $ Fl.say(Fl_uv, "Ладно, не важно...")
    $ Fl.say(Fl_r, "Юля подняла и направила руку на мою ногу.")
    $ Fl.say(Fl_uv, "Ты говорил, что этот мир для тебя ад, так почему бы мне не показать тебе настоящий {b}ад{/b}!")

    $ Fl.PlaySound("Fl_bones_breaking", 1, 0, False)
    with Fl_flash_red
    $ Fl.say(Fl_r, "После чего моя нога сама по себе изогнулась в неестественное положение. {w}Кости хрустнули.", _with=hpunch)

    show Fl_prolog_dream with Fl_dissolve1
    $ Fl.say(Fl_r, "Я в очередной раз закричал от боли. Перед глазами начало всё плыть. Я готов был в любой момент отключиться.")

    hide Fl_prolog_dream with Fl_dissolve1
    $ Fl.say(Fl_uv, "Нет, я тебе не позволю так быстро умереть, ты будешь чувствовать боль, пока мне не надоест!")
    $ Fl.say(Fl_r, "По телу пробежали мурашки. {w}Глаза неко ярко засветились, на её лице не промелькнуло не единой эмоции, она игралась со мной с каменным лицом.")
    $ Fl.say(Fl_r, "Почему то перед глазами всплыл образ, той девочки в платье, что сидела на пляжу и с улыбкой на лице любовалась луной.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1
    $ Fl.StopMusic(4)


    $ Fl.Pause(3.5)
    scene bg Fl_blink_square_party
    show Fl_dust_full
    show Fl_vignette
    show Fl_blood_eff 
    with Fl_dissolve2

    $ Fl.PlayAmbience("Fl_camp_center_night", 1, 4)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Она продолжала ломать конечность за конечностью. {w}Кричать не было сил, я молча смотрел в её кошачьи глаза и злобно проклинал её и весь этот жалкий мир иллюзий.")
    $ Fl.say(Fl_pib, "Х-хв{mn} Х-хватит!")
    $ Fl.say(Fl_r, "Девушка остановилась, её зрачки вновь стали прежними.")
    $ Fl.say(Fl_r, "Она медленно наклонилась, поставив левую руку на мою грудь как опору.")
    $ Fl.say(Fl_uv, "Ладно. С тебя достаточно.")
    $ Fl.say(Fl_uv, "Прощай, Ян. Мне жаль, но твои страдания только начинаются.")
    $ Fl.say(Fl_pib, "Хахах. Как только начнётся цикл, я тебя найду!")
    $ Fl.say(Fl_uv, "Не начнётся.")
    $ Fl.say(Fl_r, "Сказала девушка, недрогнув ни одной мышцей лица.")
    $ Fl.say(Fl_th, "Что?")

    with Fl_flash
    scene bg Fl_black with Fl_flash_red
    $ Fl.say(Fl_r, "Но я не успел узнать, что имела виду девушка с кошачьими ушками в коричневом платье. {w}Одним быстрым движением, она пробила мне грудную клетку, оставив навсегда в царстве вечной тьмы и пустоты.")
    $ Fl.HideScreens(_with=Fl_dissolve2)
    $ Fl.StopAmbience(5)
    scene bg Fl_black with Fl_dissolve3





    $ Fl.Pause(8.5)

    scene Fl_q_66_3 with Fl_dissolve2
    show Fl_q_66_layer with Fl_effect_down1
    show Fl_q_66_text3 with Fl_dissolve1
    $ Fl.Pause (4.5)

    scene bg Fl_black with Fl_dissolve2
    $ Fl.Pause (7.5)



    
    scene cg Fl_vurtal with Fl_dissolve5
    $ persistent.Fl_photo_pallery_20 = True


    $ Fl.DayTime("rain", "night")
    $ Fl.Save("Dls Одиночка:Глава 2")
    $ Fl.Pause (2.5)

    $ Fl.PlayMusic("Fl_ost_yuki_hayashi", 1, 6)
    $ Fl.ShowScreens(_with=Fl_dissolve2)
    $ Fl.say(Fl_r, "Никто не способен дать точный ответ на вопросы: «Что нас ждёт после смерти?», «Существуют ли ад и рай?», «Правда ли нас ждёт свет в конце тоннеля или после смерти всех нас поджидает кромешная тьма?»")
    $ Fl.say(Fl_r, "Но почти каждый может ответить лишь одно: «Я не хочу умирать!». Эти слова может сказать, даже человек с мёртвой душой.")
    $ Fl.say(Fl_r, "Каждый, в последние минуты своей жизни, начинает по настоящему ценить то время, которое ему было подарено богом или кем-то ещё. Однако, сей вопрос уже затрагивает веру, а я не хочу её касаться.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Если говорить обо мне. То я полностью смог убедиться, что никакого обещанного света я не вижу. Просто густая мгла, но я могу отчётливо увидеть себя в ней.")
    $ Fl.say(Fl_th, "Может это и есть мой ад?")
    $ Fl.say(Fl_th, "Бесконечность с огромным количеством мыслей в голове - чем же это не ад?")
    $ Fl.say(Fl_r, "Слово бесконечность вызвало у меня улыбку.")

    $ Fl.Pause (2.0)
    $ Fl.say(Fl_r, "Наверное, у вас возник вопрос: «Неужели ты действительно доволен концом своей жалкой биографии?»")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_th, "Мой ответ - {w}Да! Конечно!")
    $ Fl.say(Fl_r, "Я сам выбрал такой путь, это решение не было ложью! {w}На то была моя воля!")
    $ Fl.say(Fl_th, "Ведь на этом мои старые страдания закончились. {w}И начинаются новые...")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_th, "Хах, забавно{mn} Всего за пару дней человек, который был жестоким убийцей, пожертвовал собой, ради одной куклы. {w}А точнее девочки, {b}живой{/b} и {b}настоящей{/b}... {w}Назвать её куклой, у меня язык не поворачивается!")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_th, "Ха-ха. А я уже говорил, что любой мир похож на игру?")
    $ Fl.say(Fl_th, "Наверное многие подумают, что глупо сравнивать реальный мир с какими-то играми, но вы сами подумайте!")
    $ Fl.say(Fl_th, "Почти все игры ассоциируются с реальностью. {w}Взять к примеру шахматы.")
    $ Fl.say(Fl_r, "На первый взгляд, игра довольно простая, но её уровень сложности меняется в зависимости от твоего оппонента. В жизни всё так же, сильнейший всегда будет доминировать над теми, кто его слабее.")
    $ Fl.say(Fl_r, "Нет, я не привожу в пример правила дикой природы, где сильнейшие особи - руководят своей стаей, а остальные боятся их и не могут им перечить. Под сильнейшим, я подразумеваю - человека, который способен адаптироваться к любым, пусть даже и непредсказуемым жизненным условиям.")
    $ Fl.say(Fl_r, "Так же любого человека можно рассмотреть как допустим, пешку на игровом поле. {w}Потому что, у каждого человека есть свой жизненный путь, и в конце мы можем сами выбрать, кем станем, начиная от простой фигуры, заканчивая ферзём.")
    $ Fl.say(Fl_th, "Жаль я так и остался простой пешкой...")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_th, "Хах, всё же это и правда похоже мой ад. {w}Вся эта философия меня точно скоро с ума сведёт!")

    show Fl_vignette with Fl_dissolve2
    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Свет вокруг меня начал понемногу затухать, позволяя моему телу погрузиться в тягучую темноту.")
    $ Fl.say(Fl_th, "Неужели я попал в чистилище? И всё это время, я ждал когда мне озвучат приговор силы свыше?")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_th, "Силы свыше{mn} Боги...")
    $ Fl.say(Fl_r, "Кто же такие на самом деле Боги? {w}Наверное создатели всего живого и неживого? {w}Да возможно так и есть.")
    $ Fl.say(Fl_r, "Но я считаю Бог - это одна из главных отмазок человечества!")
    $ Fl.say(Fl_r, "Если мы чего-то достигли, то благодарим Бога, а если терпим неудачу, то виним в этом тоже Бога. {w}Мы вечно что-то просим у него в надежде, что наши мольбы дойдут до всевышнего.")
    $ Fl.say(Fl_th, "Какой же бред!")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_th, "Что касается меня, то я ненавижу Богов, они просто создали нас ради забавы, для них мы простые бесдушные куклы...")
    $ Fl.say(Fl_r, "Кому-то всё, а кому-то ничего...")
    $ Fl.say(Fl_th, "Эта ненависть умрёт вместе со мной. И возможно когда-нибудь мои страдания ощутят Боги на себе.")
    $ Fl.say(Fl_th, "А пока{mn}")

    show Fl_prolog_dream with Fl_dissolve1
    $ Fl.say(Fl_r, "Пространство вокруг меня, начало отдавать помехами старого телевизора.")
    $ Fl.say(Fl_r, "Но где-то посреди всей этой ряби, мне удалось заметить слабый белый огонёк, который стремительно приближался ко мне.")
    $ Fl.say(Fl_th, "Интересно... {w}Неужели это и есть тот самый свет в конце тоннеля?")
    $ Fl.StopMusic(7)
    $ Fl.HideScreens(_with=Fl_dissolve2)
    scene bg Fl_black with Fl_dissolve3


    $ Fl.Pause (7.5)
    scene bg Fl_palata_loner with Fl_dissolve4
    $ Fl.Pause (1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.PlayMusic("Fl_dead_city", 1, 6)
    $ Fl.say(Fl_r, "Я очнулся в комнате украшенную серыми стенами. За окном была ночь, а на против кто-то сидел.")
    $ Fl.say(Fl_r, "Быстро осознав всё происходящее, я понял что нахожусь в палате.")

    $ Fl.AttackScreens(True)
    $ Fl.say(Fl_r, "Я попытался встать, но я был крепко привязан к больничной койке.")
    $ Fl.say(Fl_th, "Какого?!", _with=hpunch)
    $ Fl.say(Fl_r, "Мои руки и ноги были крепко прикованы ремнями.")
    $ Fl.say(Fl_r, "А всё моё тело было в окровавленных бинтах.")
    $ Fl.say(Fl_r, "Моё тело начало подбрасывать, я пытался вырваться из оков, что тем самым привлёк внимание человека, который сидел рядом с койкой.", _with=vpunch)
    $ Fl.say(Fl_park, "Эй! Он очнулся! {w}Живо зови {b}его{/b}!")
    $ Fl.say(Fl_r, "Я мигом перестал дёргаться и бросил взгляд в сторону дверного проёма, где находился ещё один неизвестный.")
    $ Fl.say(Fl_r, "Что примечательно, все они были одеты в медицинский халаты.")
    $ Fl.say(Fl_th, "Стоп. А что если я... {w}Вернулся обратно?!")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_th, "Обратно в свой мир?")
    $ Fl.say(Fl_r, "В голове сразу появилась новая теория. {w}В неё входил тот факт, что возможно после того как меня сбил автобус, я впал в кому. {w}А что такое развитие событий весьма вероятно!")
    $ Fl.say(Fl_r, "Тогда всё что произошло и всё что я пережил не больше чем самообман, чтобы мозг не скучал, пока моё сознание не вернётся в тело...")
    $ Fl.say(Fl_th, "Но тогда бы мои раны зажили...")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_th, "Хотя я ведь не могу знать точно сколько я пролежал в коме, может всего навсего пару дней. {w}Я не должен судить по времени исходя из жизни в том злосчастном пионер лагере.")
    $ Fl.say(Fl_r, "Я лежал и пялился в потолок. Много мыслей посейщало мою голову.")
    $ Fl.say(Fl_r, "В коридоре послышался топот пары шагов, приближающиеся к моей палате.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause (3.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "В дверях появился мужик, которого я видел раньше, и ещё неизвестная мне фигура.")
    $ Fl.say(Fl_r, "Всё тот же медицинский халат, слабая щетина на лице, неуложенные волосы, средней длины и очки, в которых отражался свет от ламп, в которых нельзя было разглядеть его глаза...")
    $ Fl.say(Fl_r, "Фигура в халате подошла ко мне.")
    $ Fl.say(Fl_r, "Теперь вблизи мне удалось разглядеть что скрывало преломление света. {w}Один глаз смотрел на меня стеклянным зрачком, а другой и вовсе был зажмурен.")
    $ Fl.say(Fl_th, "Жопой, чую что это <нихр*на> не мой лечащий врач!")
    $ Fl.say(Fl_pi, "Кто ты?")
    $ Fl.say(Fl_park, "Сразу на ты, что ещё требовалось ожидать от {b}того кто отрёкся от своего имени{/b}.")
    $ Fl.say(Fl_r, "Такой ответ меня не устроил, поэтому я молча продолжил пилить взглядом своего таинственного собеседника.")
    $ Fl.say(Fl_park, "Ну что ты? Хватит так на меня смотреть, я ведь не сделал ничего плохого.")
    $ Fl.say(Fl_park, "Для начала я думаю стоит представиться.")
    $ Fl.say(Fl_par, "Я - доктор {b}Парки{/b}.")
    $ Fl.say(Fl_th, "Парки? {w}Серьёзно?")
    $ Fl.say(Fl_r, "Было не трудно догадаться, что доктор - очередной странный тип, которого мне довелось повстречать за последнюю неделю.")
    $ Fl.say(Fl_par, "У тебя наверное куча вопросов ко мне?")
    $ Fl.say(Fl_pi, "Так и есть.")
    $ Fl.say(Fl_par, "Что ж{mn} Тогда начну по порядку.")
    $ Fl.say(Fl_r, "Доктор поправил указательным пальцем очки, после чего присел на стул, скрестив ноги.")
    $ Fl.say(Fl_par, "Наверное тебя сейчас мучает вопрос, что же произошло с тобой на самом деле, после битвы с Богом?")
    $ Fl.say(Fl_r, "В качестве ответа, я молча кивнул.")
    $ Fl.say(Fl_par, "Ну скажем так, ты проиграл. Юля тебе сделала большую дыру в груди и на этом ваш поединок был закончен.")
    $ Fl.say(Fl_r, "Я опустил взгляд. Живот был весь в бинтах и жгутах.")
    $ Fl.say(Fl_par, "Но тебе повезло! {w}В ту ночь мои колеги успели спасти тебя. Пришлось правда тебя немного по частям собирать...")
    $ Fl.say(Fl_r, "Доктор усмехнулся и указал на мою правую руку.")
    $ Fl.say(Fl_r, "Она была так же вся в бинтах, даже пальцы были аккуратно перемотаны.")
    $ Fl.say(Fl_pi, "Дай угадаю, а потом ты воскресил меня с помощью молнии?")
    $ Fl.say(Fl_r, "Раздался слабый смешок.")
    $ Fl.say(Fl_par, "Я похож на доктора франкенштейна?")
    $ Fl.say(Fl_pi, "А имя Парки тебя не смушает?")
    $ Fl.say(Fl_par, "И то верно.")
    $ Fl.say(Fl_r, "На мгновение в палате повисла мёртвая тишина.")
    $ Fl.say(Fl_pi, "Может ты расскажешь, за чем я здесь и для чего ты меня вытащил с того света? Явно не просто так.")
    $ Fl.say(Fl_par, "На самом деле я был поражён, то как ты бросил вызов самому богу! {w}Нет, правда. Будучи ничтожно слабым, ты смог противостоять ей!")
    $ Fl.say(Fl_par, "Поэтому позволь задать тебе вопрос...")
    $ Fl.say(Fl_r, "Сказал доктор безэмоционально.")
    $ Fl.say(Fl_par, "Если бы у тебя была сила равная Юли, хотел ли ты отомсить ей?")
    $ Fl.say(Fl_par, "Да или нет? {w}Любой из этих вариантов может координально изменить твою дальнейшую судьбу, так что подумай хорошенько!")
    $ Fl.say(Fl_r, "Я рассмеялся.")
    $ Fl.say(Fl_th, "Сила равная богу? {w}Да вы издеваетесь!")
    $ Fl.say(Fl_pi, "Глупый вопрос...")
    $ Fl.say(Fl_pi, "Конечно да! {w}Я готов на всё что угодно лишь бы заставить эту ушастую страдать!")
    $ Fl.say(Fl_pi, "Она забрала меня в этот пионерский ад! {w}Из-за неё мне приходилось каждый раз наблюдать за одинаковыми событиями, переживать одну и ту же неделю из раза в раз!")
    $ Fl.say(Fl_pi, "Мой ответ - {b}да{/b}! И только да!")
    $ Fl.say(Fl_r, "Доктор широко улыбнулся. Такой ответ его явно устроил. {w}Линзы на его очках вновь сверкнули.")
    $ Fl.say(Fl_par, "Отлично! {w}Ты не перестаешь меня удивлять!")
    $ Fl.say(Fl_r, "Доктор развёл руками, после чего встал и пошёл на выход. {w}За дверю ждали другие рабочие в халатах.")
    $ Fl.say(Fl_par, "Можете приступать.")
    $ Fl.say(Fl_pi, "Эй! Постой!")
    $ Fl.say(Fl_par, "Скоро увидимся, {b}новенький{/b}.")
    $ Fl.say(Fl_r, "Сделав акцент на последнем слове, он скрылся в тёмноте коридора.")
    $ Fl.say(Fl_r, "Пару работников подошли ко мне. У одного из них был приличного размера шприц с бледным содержимым.")
    $ Fl.say(Fl_r, "Я начал брыкаться в надежде вырваться из беспомощной ситуации. {w}Бесполезно...")
    $ Fl.say(Fl_pi, "Что это?!")
    $ Fl.say(Fl_pi, "Я спросил, что это <бл*ть> такое!", _with=hpunch)
    $ Fl.say(Fl_r, "Но мужчина в халате никак не реагировал на мои вопросы, а молча вёл содержимое шприца.")

    with Fl_flash
    $ Fl.say(Fl_r, "В тот же миг жуткая боль пронесла по моему телу. Я крепко стиснул зубы чтобы не закричать, вены вспухли. Я сжал свои руки в кулаки, так что ногти впились в кожу.", _with=vpunch)
    $ Fl.say(Fl_th, "Что ты мне вколол, мра...")

    scene bg Fl_black with Fl_dissolve1
    $ Fl.say(Fl_r, "Резко моё тело обмякло и не в силах сопротивляться, я закрыл глаза. {w}Я отключился, оставив своё тело беззащитным в этой странном месте.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(4)
    $ Fl.Pause (10.5)



    $ Fl.DayTime("kira", "day")


    $ Fl.PlayMusic("Fl_silver_lights", 1, 7)
    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 4)
    scene bg Fl_int_bus
    show Fl_dust_full
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Я неподвижно сижу в салоне Икаруса.")
    $ Fl.say(Fl_r, "Пылинки взмывают вверх и падают вниз в узком луче света, падающем через полуприкрытые шторки.")
    $ Fl.say(Fl_r, "Лениво слежу взглядом за ними.")
    $ Fl.say(Fl_r, "Ведь даже {b}я{/b}, который знает почти всё, не знает {b}всего{/b}.")
    $ Fl.say(Fl_r, "Я не знаю, те ли это пылинки, что были в прошлый повтор.")
    $ Fl.say(Fl_r, "В окно стучат. И ещё раз.")
    $ Fl.say(Fl_r, "Кажется, моё спокойное времяпровождение подходит к концу.")
    $ Fl.say(Fl_th, "Интересно, что будет на этот раз?")
    $ Fl.say(Fl_pib, "Может начать сегодня с пилы? Или с топора?")
    $ Fl.say(Fl_th, "Так странно, что моя внешность, мой голос не меняются. Абсолютно. {w}Как, впрочем, и у всех окружающих.")
    $ Fl.say(Fl_th, "Или же меняется, просто я не помню как выглядел раньше? {w}Наверное{mn}")

    show kt smile pioner1 with Fl_dissolve1

    $ Fl.say(Fl_r, "В автобус легко запрыгнула девушка. Голубоглазка. Метр 68, спортивного телосложения. Крайне надоедливого нрава. Я даже не смотрел в её сторону.")
    $ Fl.say(Fl_th, "Что же стало с Толяном?")
    $ Fl.say(Fl_th, "Хех. Оказывается если долго засиживать в автобусе этот дегенерат уходит обратно в лагерь и жалуется вожатой, что никто не приехал.")
    $ Fl.say(Fl_th, "И тут на вырочку(ну или решать проблемы за «справочником») вызвается помощница вожатой.")
    $ Fl.say(Fl_th, "Хотя ладно что-то я палку перегнул из всех кукол Толян был самым живым, его можно споить и пойти на такие авантюры...")
    $ Fl.say(Fl_r, "Попытался продолжить наблюдение за пылинками, но тем уже передалась беспокойность активистки. Я вздохнул.")
    $ Fl.say(Fl_r, "И перевёл взгляд на «Правильную» - спросил:")
    $ Fl.say(Fl_pib, "Ты куришь?")

    show kt surprise pioner1 with Fl_fast

    $ Fl.say(Fl_ka, "Ч-что?..")
    $ Fl.say(Fl_pib, "Ты хочешь сигарету? Они лежат во-он там, в бардачке.")
    $ Fl.say(Fl_ka, "Но{mn}")
    $ Fl.say(Fl_r, "И послушно повернулась в ту сторону.")
    $ Fl.say(Fl_r, "Зря. Впрочем, она всегда попадается первой(после Толяна конечно).")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    show kt surprise pioner1 at Fl_punch

    $ Fl.say(Fl_r, "Я не глядя схватил за волосы пионерку. Развернув пионерку я совсей силы ударил ей в живот. Та же закряхтела и упала на землю.")
    $ Fl.say(Fl_pib, "Я просто хочу помогать вожатой вместо тебя! Разве я столь многого прошу?")

    $ Fl.say(Fl_r, "Благодаря длинным волосам пионерки, я обмотал их вокруг её шеи и начал душить.")

    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    $ Fl.say(Fl_r, "Труп куклой шлепнулся между сидений. Кукла она и есть...")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(4)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause(3.5)

    scene bg Fl_ext_bus_kt_dead
    show Fl_light_c 
    with Fl_dissolve1

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Я вышел из салона автобуса, оставляя жертву болтаться на импровизированной петле.")
    $ Fl.say(Fl_th, "Ну что, куда теперь?")

    $ Fl.PlaySound("Fl_keys_rattle", 1, 0, False)

    $ Fl.say(Fl_r, "Я вспомнил, что сегодня мне определённо нужны инструменты, и довольно звякнул только что приобретёнными ключами.")

    scene bg Fl_ext_camp_entrance_day
    show Fl_light_c 
    with Fl_dissolve2

    $ Fl.say(Fl_r, "Прошёл сквозь ворота лагеря.")

    scene bg Fl_sklad_day
    show Fl_light_c 
    with Fl_dissolve2

    $ Fl.say(Fl_r, "Не спеша прогулялся до склада.")
    $ Fl.say(Fl_r, "Там нашлось всё, что мне нужно. Ведь иначе уже не бывает.")
    $ Fl.say(Fl_r, "Я подобрал свою котомку, обдумывая, куда направляться теперь...")
    $ Fl.HideScreens(_with=Fl_dissolve1)

    $ Fl.Pause(2.5)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Выбирая, куда бы мне сегодня пойти, я прислушался к лагерю вокруг.")
    $ Fl.say(Fl_r, "Щебетание птиц... Стрёкот каких-то там насекомых... которых нет.")
    $ Fl.say(Fl_r, "Я склонился над, а потом и вовсе стал на колени рядом с лужайкой. Медленно провёл рукой по траве.")
    $ Fl.say(Fl_r, "Она тихонько шуршит и колышется. Живая, безразличная, сочно-зелёная. Безмятежная. Всё как всегда...")
    $ Fl.say(Fl_r, "Созерцание травы, которой всё равно, настроило на философский лад.")

    scene bg Fl_ext_sky_day with Fl_dissolve1
    $ Fl.PlayMusic("Fl_story_of_the_whole_thing", 1, 5)
    $ Fl.say(Fl_r, "Я философски предался философским размышлениям о смысле бытия и вообще. В частности, моего...")
    $ Fl.say(Fl_r, "Курить не хотелось. Я сощурился и попытался рассмотреть смысл бытия на небе, но...")
    $ Fl.say(Fl_r, "Мысли хаотично метались в моей черепной коробке, и я сдался.")
    $ Fl.say(Fl_r, "Философствовать, валяясь в пыли под сараем, не выходит. Тут слишком много травы, пыли и сараев. Слишком ярко и позитивно, слишком много света и зелени!")
    $ Fl.say(Fl_r, "Сердце подсказало идти туда, где меня поймут. Где поддержат, где утешат.")
    $ Fl.say(Fl_pib, "Давненько я не был в библиотеке!")

    scene bg Fl_sklad_day
    show Fl_light_c 
    with Fl_dissolve1

    $ Fl.say(Fl_r, "Отряхнув колени, я, зацикленный на мыслях о книгах, скрылся из виду.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(4.0)

    scene bg Fl_ext_library_day
    show Fl_light_c 
    with Fl_dissolve1

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Наконец-то я смогу побыть в тишине. Встретится лицом к лицу с теми кто меня по-настоящему понимает.")

    $ Fl.PlaySound("Fl_open_door_1", 1, 0, False)
    scene bg Fl_int_library_day with Fl_dissolve1

    $ Fl.say(Fl_r, "Войдя внутрь, я окунулся в приятную прохладу.")
    $ Fl.say(Fl_r, "Дверь с грохотом ударилась об стенку.")
    $ Fl.say(Fl_th, "Эх, как же тут хорошо!")
    $ Fl.say(Fl_r, "Сейчас я, наконец, смогу пообщаться с кем-то, не обделенным интеллектом!")
    $ Fl.say(Fl_r, "С кем-то, кто разделит со мной тоску этим вечером! С кем-то, достойным моего полного внимания!")
    $ Fl.say(Fl_r, "Тут раздался скрипучий голос:")
    $ Fl.say(Fl_mzp, "Что за шум?! Здесь библиотека вообще-то!")

    show mz angry pioner2 with Fl_fast

    $ Fl.say(Fl_r, "Библиотекарша выползла из-за стола, послеповато щурясь, несмотря на очки. {w}Потом её взгляд упал на меня:")
    $ Fl.say(Fl_mzp, "А это ещё что за фанат Кино?! Здесь вам не концерт! Соблюдайте...")
    $ Fl.say(Fl_r, "Я сполна насладился пронзающими мозг ржавыми переливами её голоса.")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    show mz angry pioner2 at Fl_punch

    $ Fl.say(Fl_r, "И молча ударил кулаком в лицо.")
    $ Fl.say(Fl_r, "Это насекомое не достойно моего внимания.")
    $ Fl.say(Fl_r, "Под ногой хрустнули линзы. Я пинками закатил бессознательную брюнетку под её же стол.")
    $ Fl.say(Fl_r, "А затем, потянувшись, развёл руки широко-широко, будто обнимая всю книжную коллекцию.")
    $ Fl.say(Fl_pib, "Как я рад вас видеть, товарищи писатели.")
    $ Fl.say(Fl_r, "Книги ответили одобрительным шуршанием.")
    $ Fl.say(Fl_r, "Я бодро прошёлся между полками, проводя пальцем по корешкам. Кажется даже на ощупь, прикрыв глаза, могу сказать, какая именно книга, кто автор, на какой странице лучший момент, сколько в ней опечаток...")
    $ Fl.say(Fl_r, "Я схватил ближайшую книгу и плюхнулся на ближайший стул.")
    $ Fl.say(Fl_r, "Это оказалась «Над пропастью во ржи».")
    $ Fl.say(Fl_r, "Я тяжело вздохнул.")
    $ Fl.say(Fl_r, "Бесспорно, история замечательная.")
    $ Fl.say(Fl_r, "Но, сколько бы я не читал её, каждый раз уверяюсь в мысли, что у главного героя крыша поехала почти как у меня, и он в скором времени станет маньяком.")
    $ Fl.say(Fl_r, "Не. Мне надо отвлечься от неизбежности лагеря, а не изобретать новые вариации убийств.")
    $ Fl.say(Fl_r, "Я уважительно выкинул Сэлинджера за спину, вскочил со стула и принялся копаться в книгах.")
    $ Fl.say(Fl_r, "Следующая книга оказалась «Понедельник начинается в субботу» Стругацких.")
    $ Fl.say(Fl_r, "Потом швырнул её в сторону. У меня, мать его, каждый день понедельник.")
    $ Fl.say(Fl_r, "Достоевский полетел вслед за Стругацкими.")
    $ Fl.say(Fl_th, "Чёрт.")
    $ Fl.say(Fl_r, "Я замер посреди зала. {w}Ну конечно! Вот Лем мне будет кстати!")
    $ Fl.say(Fl_r, "Я быстро сориентировался между полок и нашёл «Солярис».")

    $ Fl.PlaySound("Fl_stuk_dver", 1, 0, False)
    $ Fl.StopMusic(3)

    $ Fl.say(Fl_r, "С чувством качественно проделанной работы, я, довольный собой, собрался было усесться и погрузиться в чтение, как раздался стук.")
    $ Fl.say(Fl_th, "Да <бл*ть>!")
    $ Fl.say(Fl_r, "Я вразвалочку добрался до двери, взял книгу под мышку и напустил на себя строгий вид. {w}Распахнул дверь.")

    $ Fl.PlaySound("Fl_open_door_1", 1, 0, False)
    scene bg Fl_ext_library_day
    show Fl_light_c 
    show al surprise pioner1
    with Fl_dissolve1

    $ Fl.say(Fl_al, "Женя, при... О.")
    $ Fl.say(Fl_r, "Я сурово глядел на неё сверху вниз.")
    $ Fl.say(Fl_pib, "О?")
    $ Fl.say(Fl_al, "Э?")

    show al scared pioner1 with Fl_fast

    $ Fl.say(Fl_pib, "Прошу прощения, но ни «О», ни «Э» не являются достаточно важными причинами, чтобы меня беспокоить. Всего плохого.")

    show al angry pioner1 with Fl_fast

    $ Fl.say(Fl_al, "А?")

    $ Fl.PlaySound("Fl_open_door_1", 1, 0, False)
    scene bg Fl_int_library_day with hpunch

    $ Fl.say(Fl_r, "Я молча закрыл дверь, но вернуться, к книге, конечно же, не смог.")
    $ Fl.say(Fl_r, "В дверь яростно забарабанили.")

    $ Fl.PlaySound("Fl_knock_door_closed_hard1", 1, 0, False)
    $ Fl.say(Fl_al, "Эй, ты вообще кто такой?! Открой быстро дверь!")
    $ Fl.say(Fl_th, "<П*зда> тебе!")

    $ Fl.PlaySound("Fl_open_door_1", 1, 0, False)
    scene bg Fl_ext_library_day
    show Fl_light_c 
    with Fl_dissolve1

    $ Fl.say(Fl_r, "Я подорвался к двери, собираясь решить всё одним ударом.")
    $ Fl.say(Fl_r, "Но пионерке повезло, она сразу же отскочила в сторону.")

    show al angry pioner2 with Fl_fast

    $ Fl.say(Fl_al, "Где Женя?!")
    $ Fl.say(Fl_pib, "Спит.")
    $ Fl.say(Fl_al, "А ты кто?")
    $ Fl.say(Fl_pib, "Дед Пихто!")
    $ Fl.say(Fl_al, "Ах ты...")
    $ Fl.say(Fl_r, "Рыжая бестия сжала кулаки.")
    $ Fl.say(Fl_al, "Ты новенький? Ну и шутки у тебя дурацкие.")
    $ Fl.say(Fl_r, "Я страдальчески поднял очи горе.")
    $ Fl.say(Fl_r, "Потом шагнул к раздражителю и коротко врезал под дых.")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    show al surprise pioner2 at Fl_punch

    $ Fl.say(Fl_r, "Оставлять её здесь одну было опасно. Иначе мне опять придётся вырезать весь лагерь - а мне лень.")
    $ Fl.say(Fl_r, "Я закинул тушу себе на плечо и зашёл внутрь.")

    $ Fl.PlaySound("Fl_open_door_1", 1, 0, False)
    scene bg Fl_int_library_day with Fl_dissolve1

    $ Fl.say(Fl_r, "Под столом явно становилось тесновато.")
    $ Fl.say(Fl_r, "Я сел за стол библиотекарши, достал книгу и...")

    $ Fl.PlaySound("Fl_stuk_dver", 1, 0, False)
    $ Fl.say(Fl_th, "Вы <бл*ть> издеваетесь?!", _with=hpunch)
    $ Fl.say(Fl_r, "Я встал. Я подошёл. Я открыл.")

    $ Fl.PlaySound("Fl_open_door_1", 1, 0, False)
    scene bg Fl_ext_library_day
    show Fl_light_c 
    show ss normal pioneer3
    with Fl_dissolve1

    $ Fl.say(Fl_ssp, "Привет... Ой, а Женя есть?")
    $ Fl.say(Fl_r, "Я качнул головой.")
    $ Fl.say(Fl_ssp, "А когда вернётся?")
    $ Fl.say(Fl_r, "Я занёс кулак.")

    show ss surprise pioneer3 with Fl_fast

    $ Fl.say(Fl_ssp, "Н-ну, раз Жени н-нет, я п-пойду тогда...")

    $ Fl.PlaySound("Fl_open_door_1", 1, 0, False)
    scene bg Fl_int_library_day with Fl_dissolve1

    $ Fl.say(Fl_r, "Открыл книгу страницу за страницу и моё раздражение потихоньку спало.")
    $ Fl.say(Fl_r, "Сколько бы я раз её не читал было интересно словно первый раз.")

    $ Fl.PlaySound("Fl_open_door_1", 1, 0, False)
    $ Fl.say(Fl_pib, "Твою мать!", _with=vpunch)

    show un scared pioneer2 with Fl_fast

    $ Fl.say(Fl_r, "Я метнул книгу в возникшую на горизонте Лену.")

    show un sad pioneer2:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 1 ypos 0.8
    with vpunch

    $ Fl.say(Fl_r, "«Солярис» поставил пионерке хедшот, та осела на пол.")
    $ Fl.say(Fl_r, "Вскочив, я швырнул в стену стул, перевернул стол, пнул взвизгнувшую рыжую по мягкому месту и, наконец, заорал, запрокинув голову:")
    $ Fl.say(Fl_pib, "ДАЙТЕ МНЕ ПРОСТО ПОЧИТАТЬ ВАШУ МАТЬ КНИГУ!!!", _with=hpunch)
    $ Fl.say(Fl_r, "Тяжело дыша, я остановил взгляд на другой любительнице книг.")

    show un sad pioneer2:
        anchor (0.5, 0.5)
        pos (0.5, 0.8)
        ease 3 xpos 0.2

    $ Fl.say(Fl_r, "Она пискнула и попыталась отползти, как сильная и независимая гусеница.")
    $ Fl.say(Fl_pib, "Вот скажи мне, что ты тут забыла?!")

    show un cry pioneer2 with Fl_fast

    $ Fl.say(Fl_lnd, "Ст... С-стенгазету д-де-лала.")
    $ Fl.say(Fl_r, "Я выпрямился. И задумался.")
    $ Fl.say(Fl_th, "Может, уйти отсюда в тень, в лес?")
    $ Fl.say(Fl_th, "Но в библиотеке именно атмосфера так ценна для меня, а не конкретная книга. {w}Та самая атмосфера, которую эти твари калечат.")
    $ Fl.say(Fl_th, "Я просто хочу побыть один, разве это так трудно?")

    hide un cry pioneer2 with Fl_fast

    $ Fl.say(Fl_r, "Вырубив каждую пионерку, я закинул их в погреб под библиотекой.")
    $ Fl.say(Fl_pib, "Больше мне здесь делать нечего. Пойду лучше поем!")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2



    $ Fl.Pause(4.5)
    $ Fl.DayTime("kira", "sunset")



    scene bg Fl_ext_musclub_sunset
    show Fl_light_c 
    with Fl_dissolve1

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Перекусив стрепнёй из столовки, я решил всё же расшевелить себя и пойти в музклуб. Поднять своё музыкальное образование, так сказать.")
    $ Fl.say(Fl_th, "Забавно, что только музыка могла противостоять моему одиночеству...")
    $ Fl.say(Fl_r, "Музклуб всегда обладал необычной энергетикой, воздействующей на моё безумие. Даже его хозяйка была терпима, когда что-то играла.")
    $ Fl.say(Fl_th, "Но из всех кукол японка была наверное самой наивной. Убийство её это отдельный вид исскуства.")
    $ Fl.HideScreens(_with=Fl_fast)


    $ Fl.PlaySound("Fl_open_door_1", 1, 0, False)
    scene bg Fl_int_musclub_sunset_blood with Fl_flash

    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Перед глаза появилась ужасная картина.")

    $ Fl.PlayMusicFrom("<from 0 to 96>", "Fl_paris", 1, 3)
    $ Fl.say(Fl_r, "Стены музклуба были запачканы кровью. На полу была огромная лужа крови. А в углу комнаты валялся голый труп японки.")
    $ Fl.say(Fl_th, "Какого{mn}")
    $ Fl.say(Fl_r, "Мои ноги подкосились, я схватился за голову.")
    $ Fl.say(Fl_th, "Нет-нет. Я точно помню, что не убивал её!")
    $ Fl.say(Fl_th, "Меня сегодня даже близко у музклуба не было!")
    $ Fl.say(Fl_r, "Я посмотрел под ноги. Сумки с инструментами не наблюдалось.")
    $ Fl.say(Fl_th, "Действительно... Я ведь её оставил в библиотеке, но что тогда здесь произошло?")
    $ Fl.say(Fl_r, "Могли ли куклы такое сделать? Убить своего товарища? {w}Бред.")
    $ Fl.say(Fl_pib, "А что если в лагере объявился ещё один убийца?")
    $ Fl.say(Fl_r, "Силуэт за окном послужил мне ответом. {w}В сторону леса уверенной походкой шёл пионер.")
    $ Fl.say(Fl_th, "Что-то слишком ты целенаправлен для декорации...")
    $ Fl.say(Fl_r, "Я решил проследить за таинственной фигурой.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(4)
    $ Fl.StopMusic(4)
    scene bg Fl_black with Fl_dissolve2



    $ Fl.Pause(5.5)
    $ Fl.DayTime("kira", "night")


    $ Fl.PlayAmbience("Fl_camp_center_night", 1, 4)
    scene bg Fl_ext_path_dark
    show Fl_dust_full
    with Fl_dissolve3

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Пионер всё глубже и глубже скрывался в темноте. {w}Шли мы очень долго. Казалось, что пионер не просто куда-то идёт, а наоборот что-то ищет.")

    scene bg Fl_ext_old_building_night
    show Fl_dust_full
    with Fl_dissolve2

    $ Fl.say(Fl_r, "В конце концов он зашёл в заброшенный лагерь.")
    $ Fl.say(Fl_th, "Это не кукла{mn} Куклы обходят это место стороной и без переменной «гг» они не зайдут внутрь(исключение Толян - он там по сценарию ошивается).")
    $ Fl.say(Fl_r, "Я медленно подкрался к окну.")
    $ Fl.say(Fl_r, "Пионер сидел на ступеньках. В его руках была сигарета.")
    $ Fl.say(Fl_r, "За время слежки руки пионера были спрятаны в карманах, поэтому я пропустил главную деталь - его руки были в крови.")
    $ Fl.say(Fl_th, "Наверное стоит пойти познакомиться! {w}Никаких «наверное» будь смелее!")

    scene bg Fl_int_old_building_night with vpunch

    $ Fl.PlayMusic("Fl_karma", 1, 5)
    $ Fl.AttackScreens(True)
    $ Fl.say(Fl_r, "Дверь содрогнула от удара и упала на пол.")
    $ Fl.say(Fl_pib, "Упс... Извиняюсь...")
    $ Fl.say(Fl_pib, "Чего это я? Точно!")
    $ Fl.say(Fl_pib, "Эй, я тебя раньше тут не видел, ты наверное новенький? Давай {b}дружить{/b}!")
    $ Fl.say(Fl_r, "Пионер в начале сильно удивился и метался взглядом, то на дверь, то на меня.")
    $ Fl.say(Fl_r, "А потом широко улыбнулся. Встал.")
    $ Fl.say(Fl_pior, "Дружить говоришь. Ну давай...")
    $ Fl.say(Fl_r, "В руках пионера сверкнул кухонный нож.")
    $ Fl.say(Fl_pior, "Но боюсь, дружба со мной тебе не пойдёт на пользу!")
    $ Fl.say(Fl_r, "Я внимательно осмотрел своего нового знакомого. {w}Длинные волосы. {w}Пионерская форма. {w}Глаза, которые скрывает чёлка. {w}И больная улыбка.")
    $ Fl.say(Fl_th, "Брат! {w}Брат по безумию, как же я рад!")
    $ Fl.say(Fl_th, "Жаль конечно что сейчас ты умрёшь... В этом лагере должен быть только один дьявол!")
    $ Fl.say(Fl_r, "Но что-то мне не давало покоя, пионер больше смахивал на дефектную куклу, чем на безумца вроде меня.")
    $ Fl.say(Fl_r, "Но зачем он убил японку? {w}Френдлифаер какой-то получается...")
    $ Fl.say(Fl_pib, "Какой сейчас год?")
    $ Fl.say(Fl_pior, "О чём ты?")
    $ Fl.say(Fl_pib, "Тогда можешь рассказать что-то из своего прошлого до лагеря?")
    $ Fl.say(Fl_pior, "И почему это я должен тебе что-то рассказывать?!")
    $ Fl.say(Fl_th, "Кукла{mn}")
    $ Fl.say(Fl_pib, "Эх, походу мы не подружимся, {b}пионер{/b}.")
    $ Fl.say(Fl_pior, "Ой, правда. Какая жалость! Плак-плак.")
    $ Fl.say(Fl_r, "Пионер покривлялся, а после сжав нож сильнее двинулся в мою сторону.")
    $ Fl.say(Fl_pib, "Не стоит.")
    $ Fl.say(Fl_r, "Но пионер не послушался.")
    $ Fl.say(Fl_r, "Взмах ножа. {w}Мимо.")
    $ Fl.say(Fl_r, "Удар с ноги. {w}Ещё раз мимо.")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.say(Fl_r, "Удар в лицо. {w}Попадание. {w}Задел перила и они стреском развалились.")
    $ Fl.say(Fl_th, "Силён, но таким меня не возьмёшь.")
    $ Fl.say(Fl_r, "Пионер вытянул нож к моему лицу.")
    $ Fl.say(Fl_r, "Я схватил его руку и совсей силы ударил локтем по изгибу.")

    $ Fl.PlaySound("Fl_bones_breaking", 1, 0, False)
    $ Fl.say(Fl_r, "Приятный хруст эхом отразился от ветхих стен прошлого.")
    $ Fl.say(Fl_r, "Желание убивать вновь вернулись ко мне. Мои вены пульсировали, а глаза залились кровью.")

    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    $ Fl.say(Fl_r, "Нож оказался в начале в моих руках, а после в глазном отверстии пионера.")
    $ Fl.say(Fl_r, "Раздался боли раздирающий крик, пионер скорчился. На моём лице появилась счастливая мина.")
    $ Fl.say(Fl_pib, "Хахах. А кто-то мне говорил, что дружба не пойдёт на пользу! {w}Дружба - это волшебство!")
    $ Fl.say(Fl_pib, "Знаешь не люблю когда мне врут!")

    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    $ Fl.say(Fl_r, "Я вонзил нож в щеку пионера.")
    $ Fl.say(Fl_pib, "Хахахаха. Кто-то уже обмочился. Давай, сделай мне что-то, мусор!")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(4)
    $ Fl.StopMusic(4)

    $ Fl.Pause(2.0)
    scene bg Fl_pyst_ch with Fl_dissolve2



    $ Fl.DayTime("prologue", "night")


    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Это было моё первое знакомство с «пионерами». Тогда я не осознавал, что ими кто-то управляет. Кто-то пострашнее меня...")
    $ Fl.say(Fl_r, "С тех самых пор ничего не изменилось. {w}С каждым циклом от меня оставалось всё меньше и меньше человечности. Новые извращенные способы убийств. Суициды от скуки и т.д..")
    $ Fl.say(Fl_r, "Трудно было сказать для кого на самом деле лагерь был адом. Для {u}меня{/u} или для {u}них{/u}...")
    $ Fl.HideScreens(_with=Fl_dissolve2)
    scene bg Fl_black with Fl_dissolve2



    $ Fl.DayTime("rain", "night")


    $ Fl.Pause (7.5)
    scene bg Fl_palata_loner with Fl_dissolve4
    $ Fl.Pause (1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.PlayMusic("Fl_dead_city", 1, 6)
    $ Fl.say(Fl_r, "Пробуждение оказалось не из приятных. На душе был какой-то осадок, который сжимал мою грудь, словно тисками.")
    $ Fl.say(Fl_r, "Меня окружили уже знакомые серые стены больничной палаты. Если так можно назвать это место(что на самом деле я очень сомневаюсь).")
    $ Fl.say(Fl_r, "На этот раз мои руки и ноги не были связаны, поэтому я мог спокойно ими двигать.")
    $ Fl.say(Fl_th, "Странно...")
    $ Fl.say(Fl_r, "Я перевёл взгляд в сторону окна.")
    $ Fl.say(Fl_r, "За толстым слоем стекла расплывался как молоко туман, скрывая красоту ночного неба. {w}Из-за атмосферного явления, я не смог разглядеть ничего примечательного, чтобы определить своё местонахождение.")
    $ Fl.say(Fl_r, "Я повернул голову на 180 градусов.")
    $ Fl.say(Fl_r, "Возле моей койки сидел и увлечённо читал книгу «мой лечащий врач».")
    $ Fl.say(Fl_th, "Визит к Минотавру. Георгий и Аркадий Вайнеры...")
    $ Fl.say(Fl_th, "Знакомый детектив, вроде бы одна из первых книг, которую я решил прочитать в библиотеке пионерлагеря.")
    $ Fl.say(Fl_r, "Доктор медленно перевёл взгляд на меня, всё так же жмуря один глаз.")
    $ Fl.say(Fl_par, "Проснулся наконец.")
    $ Fl.say(Fl_r, "Мужчина тепло улыбнулся и отложил книгу.")
    $ Fl.say(Fl_r, "Я приподнялся, приняв сидячее положение я заметил что на мне нет ни единой царапинки.")
    $ Fl.say(Fl_th, "Странно, цикл не перезапускался, тогда почему моё тело вернулось в норму?")
    $ Fl.say(Fl_th, "Или это всё его проделки...")
    $ Fl.say(Fl_r, "Я грозно посмотрел на доктора, который до сих пор одарял меня заботливой улыбкой. {w}Материнской улыбкой.")
    $ Fl.say(Fl_th, "Что это ещё за «дружелюбная» мина?")
    $ Fl.say(Fl_th, "Думаешь, я не чувствую как от тебя несёт фальшу?")
    $ Fl.say(Fl_r, "Я бы не сказал, что за все эти годы смог научиться видеть людей на сквозь, на их настоящие лица за масками... Но человек сидящий напротив меня, даже не пытался скрыть свою маску, он просто демонстрировал её мне.")
    $ Fl.say(Fl_par, "Точно! Ты наверное проголодался. Можешь взять на столе сендвичи.")
    $ Fl.say(Fl_r, "На столе лежала тарелка с треугольным пропитанием. Обратив на неё внимание, по помещению разнеслись запахи ветчины и сыра.")
    $ Fl.say(Fl_pi, "Я пожалуй откажусь.")
    $ Fl.say(Fl_r, "Края губ доктора поднялись, после чего он достал банку холодного кофе и пачку сигарет.")
    $ Fl.say(Fl_par, "И от этого тоже?")
    $ Fl.say(Fl_r, "Желания брать что-то от этого лицемера не было, но выбора не было.")
    $ Fl.say(Fl_r, "Открыв банку, я принюхался. {w}И сделал небольшой глоток.")
    $ Fl.say(Fl_par, "Неволнуйся оно не отравлено. Было бы глупо с моей стороны тебя спасти, а потом убить.")
    $ Fl.say(Fl_r, "Моя паранойя отступила, и я сделал ещё глоток попутно доставая заветный свёрток из пачки дорогих сигарет.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause (1.5)
    $ Fl.PlaySound("Fl_zazigalka", 1, 0, False)
    $ Fl.Pause (2.0)
    $ Fl.PlaySound("Fl_smoking", 1, 0, False)
    $ Fl.Pause (2.5)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_pi, "Может ты наконец-то расскажешь для чего весь этот спектакль? {w}Вопросы, воскрешение, чудо исцеление, для чего это всё?")
    $ Fl.say(Fl_par, "Допрос{mn} Хех ну, можешь задавать любой вопрос, а я постараюсь {b}честно{/b} ответить.")
    $ Fl.say(Fl_th, "Хах. Что-то я сомневаюсь, что тебе свойственно понятие «честность»!")
    $ Fl.say(Fl_pi, "Что такое на самом деле детский пионерлагерь «Совёнок»?")
    $ Fl.say(Fl_par, "Этот пионерлагерь - мир грёз одной маленькой девочки.")
    $ Fl.say(Fl_pi, "Мир грёз Юли?")
    $ Fl.say(Fl_par, "Да, это она создала этот мир. {w}Она создала крупную межпространственную аномалию, поэтому можно назвать это место частилищем заблудших душ.")
    $ Fl.say(Fl_par, "Как ты успел понять, что первоначально «Совёнок» преподносит себя как идеальный рай, а после искажается до неузнаваемости за время нахождения попаданца.")
    $ Fl.say(Fl_pi, "Есть ли выход отсюда?")
    $ Fl.say(Fl_r, "Сразу задал я следующий вопрос, который мучал меня уже долгие годы.")
    $ Fl.say(Fl_par, "Есть. {w}Первый - умереть по-настоящему, а второй - если тебе позволит уйти сама Юля.")
    $ Fl.say(Fl_pi, "Что значит умереть {b}по-настоящему{/b}?")
    $ Fl.say(Fl_r, "Доктор поправил очки и, слегка наклонив голову, ответил.")
    $ Fl.say(Fl_par, "Ты ведь и сам знаешь ответ на свой вопрос.")
    $ Fl.say(Fl_th, "Знаю ответ...")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_th, "Интересно, можно ли считать настоящей смертью, если твой убийца сам Бог? {w}Наверное да, мои самоубийства не сработали, а куклы слишком слабы чтобы убить меня.")
    $ Fl.say(Fl_pi, "Я понял к чему ты клонишь. Моя смерть от рук Юли?")
    $ Fl.say(Fl_par, "Бинго!")
    $ Fl.say(Fl_r, "Я закинул окурок в пустую банку кофе и погрузился в размышления, опираясь на новых фактах от доктора.")
    $ Fl.say(Fl_th, "Смерть засчитывается от рук «живых», но как тогда определить кто настоящий, а кто нет? У лагеря много марионеток, которые неспособны меня убить. {w}Или всё же способны?")
    $ Fl.say(Fl_th, "Как же задолбало в этом говне разбираться...")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_th, "Живые должны отличаться от обычных кукл. Но как? {w}Внешне? {w}Характером? {w}Сознанием? {w}Воспоминаниями о прошлых циклах? {w}А может всем сразу? Как те двое...")
    $ Fl.say(Fl_pi, "Почему в лагере существуют куклы и пионеры, которые помнят о циклах?")
    $ Fl.say(Fl_par, "Куклы{mn} Пионеры{mn} А я понял о чём ты.")
    $ Fl.say(Fl_par, "Ты имеешь виду иных, а точнее сказителей лагеря.")
    $ Fl.say(Fl_pi, "Иные, сказители. Обязательно давать замудрённые названия?")
    $ Fl.say(Fl_par, "Прости, но так намного легче, да и я учёный, а в науке без терминов никак.")
    $ Fl.say(Fl_pi, "Как скажешь...")
    $ Fl.say(Fl_par, "И так, сказители/иные - это пионеры с особым даром, способные влиять на реальность Совёнка.")
    if persistent.Fl_dictionary_11 == False:
        $ Fl.PodskDict()
    $ persistent.Fl_dictionary_11 = True
    $ Fl.say(Fl_par, "Знаешь, своего рода {i}псионика{/i} из вашего мира, но в разы опаснее.")
    $ Fl.say(Fl_par, "Сказитель обладает уникальной способностью, которая выходит за грань понимания и логики.")
    $ Fl.say(Fl_par, "Если говоря проще, то это пионеры со сверхспособностями. {w}Каждый из них прожил в этом лагере огромное количество циклов.")
    $ Fl.say(Fl_pi, "Но если опираться на твои слова, то Сказитель должен быть обделён высоким интелектом иначе сила поглотит его и он сойдёт с ума.")
    $ Fl.say(Fl_par, "Ты прав, так оно и есть. Среди сказителей есть гении, а есть полные безумцы, как ты.")
    $ Fl.say(Fl_th, "Безумцы{mn} Ну да похоже на правду, та чёкнутая с ножом, тому подтверждение.")
    $ Fl.say(Fl_pi, "Вот только если мы сравниваем псиоников и сказителей, то разве это не единичные случаи, почему тогда в таком маленьком мире их столько? Откуда вообще берутся способности?")
    $ Fl.say(Fl_par, "А ты упорный, всё хочешь до сути докопаться!")
    $ Fl.say(Fl_par, "Изначально вы все попаданцы и не являетесь частью этого мира. Вы небольше чем жертвы попавшие в этот мир из вне.")
    $ Fl.say(Fl_par, "Способности, да всё просто, как ты видишь тут все обитатели куклы, а вы единственные над кем лагерь не имеет контроль. Все живые, способны влиять на этот мир.")
    $ Fl.say(Fl_th, "Ложь.")
    $ Fl.say(Fl_r, "Доктор явно что-то скрывал, до этого момента он пытался хоть как-то объяснить теоритически. Но сейчас казалось что он выстроил свой ответ на ходу, стараясь утаить важные детали.")
    $ Fl.say(Fl_pi, "Ты что-то недоговариваешь не так ли?")
    $ Fl.say(Fl_r, "Улыбка доктора пропала с лица, он слегка нахмурился, но в тот же миг снова натянул свою фальшивую улыбку.")
    $ Fl.say(Fl_par, "Прости но более подробный ответ затрагивает когнитивную нейробиологую, думаю ты мало чего из этого поймёшь.")
    $ Fl.say(Fl_th, "Хах, а я оказался прав.")
    $ Fl.say(Fl_pi, "А я пожалуй послушаю.")
    $ Fl.say(Fl_th, "В своё время я изучил все книжки научной тематики в небольшой советской библиотеке.")
    $ Fl.say(Fl_r, "Доктор старался скрыть раздражение, что заставило меня ухмыльнуться.")
    $ Fl.say(Fl_th, "Ну что ты теперь скажешь, после того как тебя поймали спаличным.")
    $ Fl.say(Fl_par, "А ты не так прост, каким кажешься на первый взгляд, не зря ты мне приглянулся.")
    $ Fl.say(Fl_par, "По какой-то причине после попадания в этот мир, у всех попаданцев меняется слегка строение организма, так же появляются необычные свойства мозга.")
    $ Fl.say(Fl_par, "Ты не задумывался, почему после перезапуска, твоё тело возвращется в исходное состояние, но не до конца.")
    $ Fl.say(Fl_pi, "Что ты имеешь ввиду?")
    $ Fl.say(Fl_par, "Все предыдушие знания и опыт сохраняются на новом цикле. По этой причине ты можешь без проблем использовать мышечную память, держа в руках оружие, и подавлять боль, хотя по факту твоё тело впервые получает такого рода урон, но по какой-то причине ты не испытываешь боль, как в первый раз.")
    $ Fl.say(Fl_par, "Ты понимаешь к чему я клоню? {w}У всех живых строение мозга и нервов отличается от обычных людей. {w}И расскрыть весь свой потенциал можно только со временем. Поэтому все сказители прожили не один десяток циклов, а то и сотней.")
    $ Fl.say(Fl_pi, "И сколько всего таких индивидов в лагере?")
    $ Fl.say(Fl_par, "Шесть.")
    $ Fl.say(Fl_r, "Он протянул мне какой-то документ, где была напечатана таблица с тремя столбцами.")
    $ Fl.say(Fl_r, "Повсей видимости это был список тех {b}самых{/b} пионеров.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause (2.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "{u}Номер{/u}: P-01. {u}Кодовое имя{/u}: Кукловод. {u}Номер искажения{/u}: 1.")
    $ Fl.say(Fl_r, "{u}Номер{/u}: U-66. {u}Кодовое имя{/u}: Тихоня. {u}Номер искажения{/u}: 2.")
    $ Fl.say(Fl_r, "{u}Номер{/u}: A-56. {u}Кодовое имя{/u}: Синдром. {u}Номер искажения{/u}: 3.")
    $ Fl.say(Fl_r, "{u}Номер{/u}: L-87. {u}Кодовое имя{/u}: Деформация / Импостер / Королева. {u}Номер искажения{/u}: 4.")
    $ Fl.say(Fl_r, "{u}Номер{/u}: R-34. {u}Кодовое имя{/u}: Псионик. {u}Номер искажения{/u}: 5.")
    $ Fl.say(Fl_th, "{mn}")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_pi, "Ты сказал, что их шесть, но тут только пять.")
    $ Fl.say(Fl_par, "Да, ты прав.")
    $ Fl.say(Fl_r, "Доктор ухмыльнулся, сложив руки, он задорно сказал.")
    $ Fl.say(Fl_par, "Потому что шестой это {b}ты{/b}! Q-66! {w}Твой рейтинг искажения: 6.")
    $ Fl.say(Fl_th, "Что...")
    $ Fl.say(Fl_th, "Да вы <бл*ть> прикалываетесь, теперь я один из этих тварей, каким образом я там очутился?!")
    $ Fl.say(Fl_pi, "Что ещё за рейтинги и почему у нас какие-то номера, как у подопытных?")
    $ Fl.say(Fl_par, "Рейтинг это какое место занимает тот или иной сказитель по силе. А номера, ну у оружия есть же аббревиатура, вот и у вас она тоже имеется.")
    $ Fl.say(Fl_par, "Но ты не переживай сказители между собой обращаются к друг другу по кодовому имени. Они сами его придумывают или его им даруют коллективно.")
    $ Fl.say(Fl_par, "Мне интересно какое имя будет у тебя.")
    $ Fl.say(Fl_th, "Я тебе что подопытный? {w}Может ты мне ещё штрих код набьёшь...")
    $ Fl.say(Fl_par, "Кстати в прошлом цикле ты столкнулся с двумя сказителями. {w}С Тихоней U-66. {w}И Кукловодом P-01.")
    $ Fl.say(Fl_th, "Да мне прям <п*здец> как везёт! Столкнуться с первыми сказителями, которые оказались номер один и номер два по силе!")
    $ Fl.say(Fl_th, "Так значит тебя зовут Кукловод, да...")
    $ Fl.say(Fl_th, "Хахаха. При следующей встречи, я тебя заставлю играть в барби из тел твоих же шавок!")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_th, "Тихоня{mn} Я уже слышал это имя. Так к ней обращался Кукловод.")
    $ Fl.say(Fl_th, "Судя по их разговору, не похоже что они за одно, скорее самый главный среди сказителей это Кукловод и он господствует над другими.")
    $ Fl.say(Fl_th, "Да уж, мне предстоит сразиться с самим дьяволом...")

    $ Fl.Pause (2.0)
    $ Fl.say(Fl_pi, "Знаешь, я вот тут сижу и не понимаю одного. {w}Какая выгода тебе была спасать меня?")
    $ Fl.say(Fl_par, "Я хочу чтобы Бог этого мира погиб и тогда лагерь падёт вместе с ним. Больше никто не пострадает, никто не испытает тот же ад, что и ты.")
    $ Fl.say(Fl_r, "Я недоверчиво покосился на доктора. {w}По необъяснимой причине я не верил в добрые побуждения этого человека, он явно что-то недоговаривает и мотивы у него вовсе другие.")
    $ Fl.say(Fl_par, "Я и не жду от тебя доверия, но это и правда единственная причина твоего воскрешения. Я верю что ты тот кому по силам одолеть Юлю.")
    $ Fl.say(Fl_pi, "Тогда почему ты сам не убьёшь её?")
    $ Fl.say(Fl_par, "Потому что я здесь застрял, она не выпускает меня за порог лаборотории.")
    $ Fl.say(Fl_r, "Взяв книжку в руки, доктор встал и направился к выходу.")
    $ Fl.say(Fl_par, "Ладно, я пожалуй оставлю тебя. Скоро ты вернёшься обратно. {w}Надеюсь ещё встретимся.")
    $ Fl.say(Fl_pi, "Постой!")
    $ Fl.say(Fl_r, "Доктор остановился в проёме и бросив взгляд через плечо принялся меня слушать.")
    $ Fl.say(Fl_pi, "А если бы я тогда ответил {b}нет{/b}?")
    $ Fl.say(Fl_r, "Ухмылка.")
    $ Fl.say(Fl_par, "Тогда бы я тебя убил, вколол кое-что другое.")
    $ Fl.say(Fl_par, "Как я и сказал, от твоего ответа решалась судьба: или смерть или перерождение в сказителя под номером Q-66. {w}Вот как-то так.")
    $ Fl.say(Fl_th, "Вот как, у меня был шанс положить конец своей биографии или положить конец аду происходящему вокруг...")
    $ Fl.say(Fl_pi, "Хахах. Да кто же ты на самом деле?")
    $ Fl.say(Fl_par, "Обычный учёный.")
    $ Fl.say(Fl_r, "Мы оба улыбнулись.")
    $ Fl.say(Fl_par, "А чуть не забыл! {w}Будь осторожен, смерть от сказителя - разрушает твоё бессмертие.")
    $ Fl.say(Fl_par, "А теперь позволь мне откланяться. На все остальные вопросы, ты должен найти ответы сам.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause (2.0)
    scene bg Fl_palata_loner with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Оставшись на едине, я лёжа на кровати начал размышлять над словами безумного учёного.")
    $ Fl.say(Fl_th, "Этот мир -  всего лишь иллюзия. Фантазия девочки с кошачьими ушами...")
    $ Fl.say(Fl_th, "Этот мир - ловушка, которая захлопывается не сразу, а постепено, чтобы не спугнуть свою жертву. {w}Но так ли это?")
    $ Fl.say(Fl_th, "Я отчётливо помню как Юля протягивала мне свою крошечную руку, она звалал меня сюда. {w}Но за чем?")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_th, "Найдёшь ответы говоришь? {w}Ладно будь по вашему. Я сыграю в ваши игры, потешу вашу гордость!")
    $ Fl.say(Fl_th, "Но сперва я хочу отыскать недопионеров. Я хочу увидеть, как они страдают. {w}Я всего-то хочу мести.")
    $ Fl.say(Fl_th, "Мне предстоит совершить ещё больше зла, чтобы положить конец его новым корням.")
    $ Fl.say(Fl_th, "Интересно, какой силой владеет каждый сказитель...")

    show Fl_prolog_dream with Fl_dissolve1
    $ Fl.say(Fl_r, "Это была моя последняя мысль, перед тем как у меня разболелась голова. {w}Картина потеряла чёткость, пространство исказилось, стены плыли, комната наделилась красивыми зигзагами.")
    $ Fl.say(Fl_r, "Сил и желания сопротивляться не было. Ведь я понимал что меня ждёт дальше...")
    $ Fl.say(Fl_th, "Новый цикл.")
    $ Fl.HideScreens(_with=Fl_dissolve2)
    scene bg Fl_black with Fl_dissolve3
    $ Fl.StopMusic(5)


    $ Fl.Pause (8.5)


    $ Fl.DayTime("nightmare", "night")
    scene Fl_int_bus_red with Fl_dissolve3
    $ Fl.PlayMusic("Fl_snare", 1, 6)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Я как-то засиделся, что ли.")
    $ Fl.say(Fl_r, "Надо бы развеяться. {w}Повеселиться...")
    $ Fl.say(Fl_r, "Хотя какое к черту веселье, я хочу вырваться отсюда.")
    $ Fl.say(Fl_th, "СЛЫШИТЕ?! ВЫПУСТИТЕ МЕНЯ! {w}ПОЖАЛУЙСТА!!!")
    scene bg Fl_black with Fl_dissolve1

    $ Fl.Pause (2.5)
    $ Fl.say(Fl_r, "Я уже и не помню как здесь было раньше...")
    $ Fl.say(Fl_r, "Не знаю, кто я такой - среди сотен масок потерялось и мое лицо, да, лицо, мое лицо{mn}")
    $ Fl.say(Fl_r, "Не помню, в прошлом я или в будущем. Да и разве кто-нибудь станет винить меня? Хахахах, нет, конечно, ведь никого тут и нет!")

    scene Fl_ext_sea_red with Fl_effect_6
    $ Fl.say(Fl_r, "Такое странное чувство, будто кто-то только что стер мою память. Будто я был где-то в другом месте{mn} с кем-то.")
    $ Fl.say(Fl_r, "И в тоже время я точно знаю, что в лагере я уже{mn} целую вечность.")
    $ Fl.say(Fl_th, "Я схожу с ума. {w}Нет я уже давно сошёл! А весь этот мир вместе со мной!")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1


    scene Fl_int_bus_red with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Хм, какую из моих масок я давно не использовал?")
    $ Fl.say(Fl_r, "Я выбрал ту, которую повторял только три или четыре десятка раза.")
    $ Fl.say(Fl_r, "Хотя это ложь, и я знаю это.")
    $ Fl.say(Fl_r, "Я просто не помню.")

    scene Fl_ext_bus_red with Fl_effect_6
    $ Fl.say(Fl_r, "Я хочу провести этот день{mn}")
    $ Fl.say(Fl_sin, "В стиле старого доброго ультранасилия.")
    $ Fl.say(Fl_r, "Я и не помню уже, кто это сказал или откуда эта фраза. Просто говорю, чтобы хоть что-то сказать. Чтобы не оставаться в тишине наедине со своими мыслями лишнюю секунду, не молчать, не позволять этим вездесущим маленьким существам проникать мне в голову.")
    $ Fl.say(Fl_r, "Я не хочу слышать утробные звуки и жужжание этих тварей...")
    $ Fl.say(Fl_r, "Лагерь находился у меня прямо за спиной. {w}Он ждал от меня действий. Всегда ждал. {w}Он словно верный пёс всегда поджидает у автобуса, а в конце широко расскрывает пасть и терзает до состояния бесформенной плоти.")
    $ Fl.say(Fl_r, "Я вспоминаю про хронологию событий, про свою легенду. И иду к воротам.")

    scene Fl_ext_camp_entrance_red with Fl_dissolve2
    $ Fl.say(Fl_r, "Я не смотрю на часы, лагерь сам говорит мне, когда что произойдет.")
    $ Fl.say(Fl_r, "Громкое жужжание наполняет воздух. Оно проникает мне под одежду, под кожу, поднимается по костям моих ног к голове. Мириады мелких мыслей-паразитов залезают мне в глаза, в рот и, наконец, в мозг.")
    $ Fl.say(Fl_r, "Лагерь сделает свой ход через секунд{mn} тридцать{mn} десять{mn} две{mn}")

    show Fl_sl_fly

    $ Fl.say(Fl_sin, "Эй, приветик! Как дела? {w}Мне говорили, что тебя Славя зовут? Ну полное имя Славяна, ну ты поняла.")
    $ Fl.say(Fl_r, "Губы улыбаются сами собой, руки жестикулируют, а глаза прикрывают пряди волос. Я нахожу некую отраду в том, чтобы отыгрывать свою роль максимально достоверно. Это одна из немногих вещей, которые еще способны меня радовать.")
    $ Fl.say(Fl_r, "Я беру безликую фигуру под руку и веду прямой дорогой к тому месту, где я когда-то жил.")
    $ Fl.say(Fl_th, "А жил ли я вообще когда-нибудь?")
    $ Fl.say(Fl_th, "Или же просто имитировал жизнь жалким существованием падшего ангела, полубога, изгнанного из рая и подвергнутого полному личностному разложению.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause (2.0)
    scene Fl_ext_house_of_mt_red with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Двигаясь сквозь годы, будущее и прошлое, вхожу в здание в форме треугольной призмы. Я делаю ход своей единственной черной фигурой.")

    scene Fl_int_house_of_mt_red with Fl_dissolve2
    $ Fl.say(Fl_r, "Воздухе витал смрад, ярко выраженный запах гнилой плоти ударил мне прямо в нос. Но моё тело никак не отреагировало, рвотный позыв давно меня перестал мучить ещё несколько сотен циклов назад.")
    $ Fl.say(Fl_r, "Я остался стоять у входа совсем один и наблюдал. За нечто, что породил лагерь и мой воспалённый мозг.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1

    $ Fl.Pause (2.5)
    scene bg Fl_pyst_red_nightmare with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Что такое время? Что такое «сейчас»? Если ты заперт в отрезке времени и двигаешься, ммм, как грызун{mn} в колесе?")
    $ Fl.say(Fl_r, "Что есть «сейчас» для грызуна? Я могу быть неделей позже, годом раньше - это ничего не меняет, ведь я нахожусь внутри системы отсчета. Учёта. Подсчёта. Чёткость, да, чёткость мне нужна.")
    $ Fl.say(Fl_r, "Может быть, я мог бы ответить на свой же вопрос, если бы знал, что есть лагерь за пределами лагеря. Я предполагаю это. Он не может не быть. Ведь лагерь не может быть один! Это целая система из параллельных реальностей!")
    $ Fl.say(Fl_r, "Однако мне абсолютно неизвестно, каков он. Возможно, «снаружи» другое время. Или снаружи больше насекомых. Фууу!")
    $ Fl.say(Fl_r, "Сейчас день? {w}Или же ночь? Ночь, прочь, очь, мочь, дочь, дочь! Ахаха{mn} Почему-то это смешно.")
    $ Fl.say(Fl_r, "Я вижу сон или это происходит со мной на самом деле? А что-то разве происходит? Я вижу один и тот же дом. Гром. Фон? Сон?")
    $ Fl.say(Fl_r, "Может быть, я вовсе и не пионер{mn} Но кто тогда?")

    $ Fl.Pause (2.5)
    $ Fl.say(Fl_r, "Я не хочу уходить из своего пионера. Из своего домика! Я не могу представить себя где-то помимо лагеря.")
    $ Fl.say(Fl_r, "В голове будто несколько голосов. Один кричит нелепицу, а второй с пугающим хладнокровием задаёт вопросы. Опросы. Кроссы. Кроссы?")
    $ Fl.say(Fl_r, "Я даже представить не могу мир вне «Совенкa». Имя, имя, имя{mn} Имя! {w}Я даже его не помню!")
    $ Fl.say(Fl_r, "Хотя если бы сейчас мне предложили выход от сюда, я бы с ужасом убежал.")

    $ Fl.Pause (2.5)
    $ Fl.say(Fl_r, "Но ведь никакого выхода не существует{mn} Я знаю это. {w}Я просто обманываю себя надеждой, что есть кто-то живой, кроме меня. Что я еще не узнал все секреты этого лагеря.")
    $ Fl.say(Fl_r, "Насекомые, насекомые, вокруг слишком много насекомых! Они жужжат в голове, жужжат, жужжат, но я не могу оставить свою голову, ведь она без меня не выживет, нет-нет. Это наказание, да? Будьте вы прокляты. И будьте вы горды мной!")
    $ Fl.HideScreens(_with=Fl_dissolve2)
    scene bg Fl_black with Fl_dissolve3
    $ Fl.StopMusic(5)


    $ Fl.DayTime("night", "night")


    $ Fl.Pause (7.5)
    scene bg Fl_int_musclub_night with Fl_dissolve3
    $ Fl.Pause (1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.PlayMusic("Fl_schwerelos", 1, 6)
    $ Fl.say(Fl_r, "И вновь все вернулось на круги своя. {w}Прошло ещё пару десятков циклов. Похожие одни на другие.")
    $ Fl.say(Fl_r, "Я немного прибавил громкости на телефоне и продолжил слушать музыку. Вести монолог в тишине было очень трудно.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Вечность, состоящая из повторяющихся событий.")
    $ Fl.say(Fl_th, "Не все так просто, да? {w}Пришло время для чего-то большего, чем просто циклы.")
    $ Fl.say(Fl_r, "Слова меня из прошлого засели у меня в голове.")
    $ Fl.say(Fl_r, "А к слову так оно и есть, после моей реабилитации лагерь потерпел изменения. {w}Начиная с того, что теперь я живу в музклубе, а так же его новый хозяин. Заканчивая тем что... {w}Мику больше я не встречал ни в одном цикле.")
    $ Fl.say(Fl_r, "Не осталось ни следа от существования жизнерадостной пионерки. Только пустой и грязный музклуб, который меня встречал в начале каждого цикла.")
    $ Fl.say(Fl_th, "Неужели ты была настоящая{mn}")
    $ Fl.say(Fl_r, "Я дотронулся до половиц под роялем.")
    $ Fl.say(Fl_th, "Здесь мы впервые познакомились.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Тот цикл определённо изменил координально не только меня, но и сам лагерь.")
    $ Fl.say(Fl_r, "Сценарий слегка отклонился, но не настолько сильно.")
    $ Fl.say(Fl_r, "В каждом новом цикле, я становился заведущим музкружка. {w}Жил. {w}Завтракал, обедал, ужинал. {w}Спал. {w}Только здесь я ощущал себя в безопасности. Только здесь моя душа ощущала покой.")
    $ Fl.say(Fl_th, "Поэтому только музыка заставляет меня оставить реальность далеко позади.")
    
    $ Fl.Pause (2.0)
    $ Fl.say(Fl_r, "Хватит. {w}Тошно, от этих соплей.")
    $ Fl.say(Fl_r, "На самом деле я всё это время не сидел сложа руки, я искал ответы и зацепки.")
    $ Fl.say(Fl_r, "Доктор был прав, этот мир и правда небольше чем простая подделка. Если изучить каждый сантиметр этого места, то можно много чего интересного найти.")
    $ Fl.say(Fl_r, "Например я понял, что этот лагерь был скопирован скорее всего с моего мира, но подделка есть подделка, отсюда и беруться некоторые отклонения по типу Генды.")
    $ Fl.say(Fl_r, "Моя жизнь в лагере превратилась в рутину из поисков ответов и вечного нахождения в музкружке.")
    
    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Так же мне удалось кое-что узнать о моём чудо спасении.")
    $ Fl.say(Fl_r, "Я аккуратно дотронулся до шеи, мои пальцы легли на прямоугольное устройство.")
    $ Fl.HideScreens(_with=Fl_fast)
    $ Fl.StopMusic(2)


    $ Fl.DayTime("day", "day")

    $ Fl.Pause (1.5)
    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 2)
    scene bg Fl_int_house_of_mv_day
    show mv normal pioner2
    with pixellate
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_mv, "Ян, а что это такое у тебя на шее?")
    $ Fl.say(Fl_th, "А? О чём она?")
    
    hide mv normal pioner2 with Fl_dissolve1

    $ Fl.say(Fl_r, "Я открыл дверцу шкафа и посмотрел в зеркало, которое находилось с внутренней стороны.")
    $ Fl.say(Fl_pi, "Какого?!", _with=hpunch)
    $ Fl.say(Fl_r, "На моей шеи было что-то наподобие чокера, он крепко обхватывал мою шею, но почему-то не вызывал дискомфорт. Наверное по этой причине я и не заметил его раньше.")
    $ Fl.say(Fl_r, "От самого чокера выходило два провода, похожие на наушники, они заканчивались в области задних лимфоузлов и уходили куда-то под кожу. {w}А справа находилась небольшая прямоугольная коробка.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(2)


    $ Fl.Pause (1.5)
    $ Fl.PlayMusic("Fl_schwerelos", 1, 4)
    scene bg Fl_int_musclub_night with pixellate
    
    $ Fl.DayTime("night", "night")

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Я долго пытался понять, что это за устройство на моей шее. И в итоге пришёл к выводу, что это какой-то аппарата жизнедеятельности и без него я бы щас тут не сидел и не слушал музыку.")
    $ Fl.say(Fl_r, "Но это неединственное что изменилось в моей внешности.")
    $ Fl.say(Fl_r, "В области груди у меня огромный шрам. Шрам, который оставил мне Бог этого мира после нашей дуэли.")
    $ Fl.say(Fl_r, "А ещё на голове появилась небольшая прядь седых волос.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Что насчёт сказителей. {w}Тут всё намного сложнее, с тех самых пор меня никто не навещал, а я так и не нашёл способа найти их сам.")
    $ Fl.say(Fl_r, "Порой в голове всплывает та самая карта в старом корпусе. Её содержимое смахивало на отметки различных секторов, возможно это и есть ключ к нахождению других пионеров.")
    $ Fl.say(Fl_r, "Жаль я не обладаю феноменальной памятью. Тогда бы я мог её перенести на лист бумаги.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Главная цель моя была всё та же - отомстить и уничтожить всё зло этого мира.")
    $ Fl.say(Fl_th, "Хахах. Забавно это слышать от жестокого убийцы. {w}От того, кто намеренно заставлял всех вокруг страдать и смеялся жертвам прямо в лицо.")
    $ Fl.StopMusic(4)

    $ Fl.Pause (1.0) 
    $ Fl.say(Fl_r, "Я остановил музыку на телефоне и отложил его в сторону.")
    $ Fl.say(Fl_r, "Закончив настраивать бас-гитару и подключив её к усилитилю, я встал и откинул волосы назад.")
    $ Fl.say(Fl_th, "Как же всё <за*бало>, пора немного вскипятить кровь.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.PlayMusic("Fl_nirvana_smells", 1, 4)
    $ Fl.Master(Fl_screen_attack_bg)
    $ Fl.Pause (5.5)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Мои пальцы быстро перебирали струны чудо инструмента. {w}Моё тело двигалось само по себе, мотая головой и подпрыгивая я старался попадать в ритм.")
    $ Fl.say(Fl_r, "На моём лице была широкая улыбка.")
    $ Fl.say(Fl_r, "После смерти Мику я полностью отдался музыке. Долгие, утомительные тренировки и я наконец-то довёл свою игру до совершенства.")
    if persistent.Fl_dictionary_12 == False:
        $ Fl.PodskDict()
    $ persistent.Fl_dictionary_12 = True
    $ Fl.say(Fl_th, "{i}Повеяло юностью{/i}!")
    $ Fl.say(Fl_r, "Несмотря на то что музклуб был около леса и мою игру никто не может услышать, мне было глубоко плевать поэтому я прибавил ещё звук.")
    $ Fl.say(Fl_r, "Я продолжал агресивно перебирать струны медиатром и качать головой в ритм. Сейчас для меня существует только музыка, только она имела значение в этом мире.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.Pause (4.0)


    scene Fl_pause
    with Fl_effect_time_pause

    $ Fl.Pause (3.5)
    scene bg Fl_black with Fl_dissolve2
    $ Fl.StopMusic(3)
    $ Fl.Pause (2.0)


    $ Fl.PlayAmbience("Fl_camp_center_night", 1, 5)
    scene bg Fl_int_musclub_night with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Через несколько часов я оставил инструмент в покое.")
    $ Fl.say(Fl_r, "Стрелки на часах давно зашли за 3 часа ночи. Скоро мне предстоит встретить рассвет.")
    $ Fl.say(Fl_th, "Который уже посчёту{mn}")
    $ Fl.say(Fl_r, "Спать не хотелось от слова совсем. А может я просто уже забыл какого это чувствовать желание окунуться в объятия морфея...")
    $ Fl.say(Fl_r, "Но вопреки всему я решил прилечь на холодный пол.")
    $ Fl.say(Fl_r, "Я уставился в потолок.")
    $ Fl.say(Fl_r, "И незаметно для самого себя заснул.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(3)
    $ Fl.ShowBlink()


    $ Fl.DayTime("day", "day")

    $ Fl.Pause (8.5)
    scene Fl_int_musclub_rain:
        zoom 5 rotate 90 xpos -1.47 ypos -1.0 
        ease 2 zoom 5 rotate 90 xpos -1.46 ypos -1.0 
        ease 5 zoom 2.0 rotate 2 xpos -0.5 ypos -2.0 
        ease 2 zoom 2.0 rotate -1 xpos -0.49 ypos -1.75 
        ease 1 zoom 2.0 rotate 0 xpos -0.5 ypos -1.70  
    show Fl_int_musclub_rain3:
        zoom 5 rotate 90 xpos -1.47 ypos -1.0 alpha 1.0 
        ease 2.3 zoom 5 rotate 90 xpos -1.46 ypos -1.1 alpha 0.25 
        ease 4.9 zoom 2.0 rotate 2 xpos -0.51 ypos -2.0 alpha 0.75 
        ease 2 zoom 2.0 rotate -1 xpos -0.5 ypos -1.75 alpha 0.25 
        ease 1 zoom 2.0 rotate 0 xpos -0.5 ypos -1.70 alpha 0.75 
        ease 1 zoom 2.0 rotate 0 xpos -0.5 ypos -1.70 alpha 0.0 
        ease 1 zoom 2.0 rotate 0 xpos -0.5 ypos -1.70 alpha 0.75 
        ease 1 zoom 2.0 rotate 0 xpos -0.5 ypos -1.70 alpha 0.0 
        ease 1 zoom 2.0 rotate 0 xpos -0.5 ypos -1.70 alpha 0.75 
        ease 1 zoom 2.0 rotate 0 xpos -0.5 ypos -1.70 alpha 0.0 
        ease 1 zoom 2.0 rotate 0 xpos -0.5 ypos -1.70 alpha 0.75  

    $ Fl.PlayAmbience("Fl_rain_vn", 1, 7)
    $ Fl.ShowUnblink()
    $ Fl.Pause (10.5)
    $ Fl.ShowBlink()
    $ Fl.Pause (3.5)
    scene Fl_int_musclub_rain2
    show Fl_rain_hard_left
    show Fl_int_musclub_rain
    $ Fl.ShowUnblink()


    $ Fl.Pause (2.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.HideBlink()
    $ Fl.HideUnblink()
    $ Fl.say(Fl_r, "Холод, который не сравнится с привычной жарой. {w}Стук капель дождя об поверхности и запах сырости. Заставили меня медленно открыть глаза.")
    $ Fl.say(Fl_r, "Со временем звук капель становился всё отчётливее и громче.")
    $ Fl.say(Fl_r, "С недовольной миной я протёр глаза и уставился в окно.")
    $ Fl.say(Fl_th, "Дождь, забавно{break2}")
    $ Fl.say(Fl_pi, "ДОЖДЬ!", _with=hpunch)

    $ Fl.AttackScreens(True)
    $ Fl.say(Fl_r, "Я вскочил и нервно начал тереть глаза.")
    $ Fl.say(Fl_r, "Глаза начали краснеть и отзываться зудом, но картина по прежднему была та же. {w}За окном: сильный ливень, лужи и всё это в нашем {b}солнечном{/b} пионерлагере!")
    $ Fl.say(Fl_r, "Тогда я решил выбежать на улицу.")
    $ Fl.HideScreens(_with=Fl_fast)
    scene bg Fl_black with Fl_effect_3


    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)

    
    $ Fl.PlayAmbience("Fl_rain", 1, 3)
    scene Fl_ext_musclub_rain
    show Fl_rain_hard_left
    with Fl_effect_3
    
    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Снаружи выглядело всё так же, как и за окном.")
    $ Fl.say(Fl_r, "Стоя в луже, я рассмеялся. На моём лице нарисовалась улыбка. {w}Было трудно понять, что именно она выражала. Наверное радость или отчаяние, от недопонимания происходящего.")
    $ Fl.say(Fl_r, "Я прыгал по лужам, ловил капли дождя ртом. Никогда в жизни бы не подумал, что буду так рад дождю.")
    $ Fl.say(Fl_r, "Хотя чего ещё ожидать от человека, который уже столько лет не видел дождя. {w}Только дикость и детскую радость.")
    $ Fl.say(Fl_r, "Наверное со стороны я выгляжу как маленький ребёнок. {w}Хотя так оно и есть.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause(4.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Мне потребовалось какое-то время чтобы вернуться в реальность.")
    $ Fl.say(Fl_r, "Я встал напротив музклуба и смотрел на стекавшие по стеклу капли дождя.")
    $ Fl.say(Fl_th, "Почему? {w}Почему именно сейчас впервые пошёл дождь?")
    $ Fl.say(Fl_th, "Неужели это какой-то знак? {w}Прошлый раз пропали звуки, а в этот раз пошёл дождь?")
    $ Fl.say(Fl_r, "Бросив на последок, я развернулся и отправился в глубь лагеря.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(4.0)
    scene Fl_ext_houses_rain:
        Fl_walking3 
    show Fl_rain_hard_left
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Хлюпанье луж под ногами отдавалось по всему лагерю. {w}Пионеры торопились, кто в домик, кто до ближайщего убежища от дождя. Я же, промокший до нитки, шёл неспеша. Холодный ветер вызывал слабую дрожь, но меня это мало беспокоило.")
    $ Fl.say(Fl_r, "Я просто шёл. {w}Куда? {w}Не знаю{mn}")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause(2.0)
    scene Fl_ext_square_rain:
        Fl_walking3 
    show Fl_rain_hard_left
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "В своём мире я обожал дождь, капли дождя всегда успокаивали и расслабляли. От вдохновения меня так и расспирало, а работа становилась в разы приятнее.")
    $ Fl.say(Fl_r, "Но сейчас меня больше посейщали мрачные мыслы. Я ждал чего-то плохого. {w}Такие изменения заставляли вспомнить события того самого цикла с моей аквамариновой пионеркой.")
    $ Fl.say(Fl_th, "Интересно от чего происходят такие перемены? Мои действия явно тут не при чём{mn}")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause(2.0)
    scene Fl_ext_house_of_mt_rain
    show Fl_rain_hard_left
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Блуждая по лагерю, я вышел к треугольному домику.")
    $ Fl.say(Fl_th, "Мой старый дом. Всё так изменилось.")
    $ Fl.say(Fl_r, "Дождь придал этому месту иной окрас, серые оттенки обесцветили пышные кусты сирени, стены домика с трудом можно было назвать зелёными.")
    $ Fl.say(Fl_r, "Оставив эту мрачную картину, я двинулся дальше.")
    $ Fl.say(Fl_r, "Сзади послышались быстрые шаги в мою сторону.")
    $ Fl.say(Fl_mv, "Ян, подожди!")

    show mv smile hood1 with Fl_dissolve1

    $ Fl.say(Fl_mvv, "Оглох что-ли? Еле тебя догнала.")
    $ Fl.say(Fl_r, "Передо мной стояла вожатая с милой улыбкой на лице. Но меня сейчас волновало не это...")
    $ Fl.say(Fl_th, "Ого, в этом месте у кукол есть и другая одежда.")
    $ Fl.say(Fl_r, "Я с интересом разглядывал пастельное худи вожатой. Было не привычно лицезреть на других что-то помимо пионерской формы.")

    show mv laugh hood2 with Fl_fast

    $ Fl.say(Fl_mvv, "Нет, ну точно оглох.")
    $ Fl.say(Fl_pi, "Вы что-то хотели?")
    $ Fl.say(Fl_r, "Без капли интереса спросил я.")

    show mv smile hood1 with Fl_fast

    $ Fl.say(Fl_mvv, "Ян, зайди ко мне переоденься, а то простудишься.")
    $ Fl.say(Fl_th, "Переодеться? Во что? {w}Разве мне не идёт этот костюм клоуна с красной петлёй на шее?")
    $ Fl.say(Fl_pi, "Хорошо.")
    $ Fl.say(Fl_r, "Вопреки всем своим разногласиям, я решил молча послушаться вожатую. События и диалоги во время дождя мне были неизвестны и их тоже не помешало бы изучить.")

    hide mv smile hood1 with Fl_dissolve1

    $ Fl.say(Fl_r, "Оставив меня одного мокнуть под дождём, вожатая вспешке удалилась.")
    $ Fl.say(Fl_r, "Я не стал долго думать и зашёл внутрь моего бывшего домика.")
    $ Fl.HideScreens(_with=Fl_fast)
    scene bg Fl_black with Fl_effect_4


    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)

    $ Fl.PlayAmbience("Fl_rain_vn", 1, 3)
    scene Fl_int_house_of_mt_rain2
    show Fl_rain_hard_left
    show Fl_int_house_of_mt_rain
    with Fl_effect_4
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Внутри оказалось намного теплее, чем снаружи. Но было непривычно темно для раннего утра.")
    $ Fl.say(Fl_r, "На кровати меня встретила аккуратно сложенная чёрная толстовка.")
    $ Fl.say(Fl_th, "Хах. И откуда вожатая её раздобыла? {w}Может это её? {w}Или конфисковала у пионера? {w}Или неужели лагерь позаботился, чтобы я вдруг не заболел?")
    $ Fl.say(Fl_r, "Последняя мысль заставила меня слегка рассмеяться. Ведь и правда искать какую-либо логику было глупо.")
    $ Fl.say(Fl_r, "Скинув с себя мокрую рубашку, я схватил толстовку и встал напротив зеркала.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause(1.5)
    scene Fl_int_house_of_mt_rain2
    show Fl_rain_hard_left
    show Fl_int_house_of_mt_rain
    with Fl_dissolve1

    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_pi, "Хах. А не плохо сидит.")
    $ Fl.say(Fl_r, "Как и ожидалось одёжка было точно моего размера и сидела на мне идеально.")
    $ Fl.say(Fl_r, "Я бросил свою мокрую одежду на спинку стула.")
    $ Fl.say(Fl_r, "Накинув капюшон на голову, я отправился дальше исследовать сиверкий лагерь.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(4.0)
    $ Fl.PlayAmbience("Fl_rain", 1, 3)
    scene Fl_ext_dining_hall_away_rain
    show Fl_rain_hard_left
    with Fl_dissolve2

    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Столовая. {w}Пионеры как обычно толпились возле прохода.")
    $ Fl.say(Fl_th, "Война войной, а обед по расписанию.")
    $ Fl.say(Fl_r, "Процетировав слова Фридриха Первого, я зашёл в столовую в целях взять свою порцию.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    scene Fl_ext_dining_hall_near_rain 
    show Fl_rain_hard_left
    with Fl_dissolve1
    $ Fl.Pause(2.0)
    scene bg Fl_black with Fl_dissolve2

    $ Fl.Pause(4.0)
    scene Fl_ext_boathouse_rain
    show Fl_rain_hard_left
    with Fl_dissolve2

    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "И вот я сижу в полном одиночестве. {w}В правой руке - треугольный пакет кефира, в левой - булка. {w}Ничего другого на вынос не дают.")
    $ Fl.say(Fl_r, "Я молча ел и смотрел куда-то вдаль, то на остров, то на дорожные пути.")
    $ Fl.say(Fl_r, "Сделав очередной глоток, я задумался.")
    $ Fl.say(Fl_th, "Куда именно идёт этот поезд? {w}В предыдущих циклах я пытался узнать. А однажды мне даже удалось сесть на него... Но стоило ему только тронуться и проехать минут пять, как я сразу вырубился и вновь очнулся в салоне икаруса.")
    $ Fl.say(Fl_th, "Может это действительно ещё один из способов покинуть этот лагерь. {w}Только он не предназначен для меня{mn}")
    $ Fl.say(Fl_r, "Мимо пристани проходили пионеры, кто бежал в укрытие от дождя, кто гулял в дождивике или с зонтиком, но никто не обращался внимания на меня.")
    $ Fl.say(Fl_th, "После моего возвращения я сильно изменился.")
    $ Fl.say(Fl_th, "Я перестал убивать кукол, хоть и не сразу. Конечно, иногда всё же мне сносило крышу и я вновь устраивал кровавую бойню. {w}Безумие - это неотъемлемая часть меня.")
    $ Fl.say(Fl_th, "Причинять боль куклам больше не приносило никакого удовольствия.")
    $ Fl.say(Fl_th, "Сейчас же мною движет только желание мести. {w}Только оно принесёт мне удовольствие и долгожданный покой.")

    $ Fl.PlayMusicFrom("<from 0 to 149>", "Fl_oldcamp", 1, 5)
    $ Fl.say(Fl_r, "Неожиданно я ощутил на себе чей-то пристальный взгляд прямо за спиной.")
    $ Fl.say(Fl_r, "Я резко повернулся на 180 градусов и успел уловить чей-то скрывающийся силуэт.")
    $ Fl.say(Fl_pi, "Так-так, а кто тут у нас такой любопытный?")
    $ Fl.say(Fl_r, "Звук брызгов луж отдалялся.")
    $ Fl.say(Fl_r, "Не став терять ни минуты я пустился в погоню за сталкером.")
    $ Fl.HideScreens(_with=Fl_fast)
    $ Fl.Master(Fl_run_fast)
    $ Fl.Pause(1.5)

    scene Fl_ext_path_rain:
        Fl_run_fast
    show Fl_rain_hard_left
    with Fl_fast
    $ Fl.Pause(1.5)

    scene Fl_ext_houses_rain:
        Fl_run_fast
    show Fl_rain_hard_left
    with Fl_fast
    $ Fl.Pause(1.0)

    scene Fl_ext_clubs_rain:
        Fl_run_fast
    show Fl_rain_hard_left
    with Fl_fast
    $ Fl.Pause(1.0)

    scene Fl_ext_no_bus_rain:
        Fl_run_fast
    show Fl_rain_hard_left
    with Fl_fast
    $ Fl.Pause(0.5)

    scene Fl_ext_no_bus_rain
    show Fl_rain_hard_left
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Покинув лагерь, я резко вертел головой в разные стороны.")
    $ Fl.say(Fl_pi, "Где он?!", _with=hpunch)
    $ Fl.say(Fl_r, "Я осметрел землю под ногами, никаких следов не было.")
    $ Fl.say(Fl_th, "Привиделось? {w}Вряд ли{mn} Моё шестое чувство никогда меня не подводит.")
    $ Fl.say(Fl_r, "Есть только два варината. {w}Тот кто наблюдал всё же смог где-то скрыться. {w}Или я просто побежал за обычным пионером из лагеря.")
    $ Fl.say(Fl_pi, "Тц. Очередная загадка, какая уже посчёту? Сотая? Или тысячная?!")
    $ Fl.say(Fl_r, "Пнув со злости камень, я принял решение вернуться в лагерь.")
    $ Fl.say(Fl_r, "Кто бы то ни был, его здесь нет. Природная для лагеря аномалия встала на сторону неизвестного.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(5)
    $ Fl.StopAmbience(5)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(8.5)


    $ Fl.DayTime("night", "night")


    scene bg Fl_bynker with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.PlayMusic("Fl_detroit", 1, 7)
    $ Fl.say(Fl_r, "Сидя на двухэтажной койке, я немного приуныл с сигаретой в зубах.")
    $ Fl.say(Fl_r, "Очередные поиски не увенчались успехом.")
    $ Fl.say(Fl_r, "Что же я забыл в бункере под старым корпусом? {w}Ищу ответы для чего может понадобиться помещение под лагерем, которое максимум может вместить человек десять, а то и меньше.")
    $ Fl.say(Fl_r, "Я почесал шею.")
    $ Fl.say(Fl_r, "Мой ошейник на шее тоже не давал мне покоя. {w}Я до сих пор не знаю что это такое. {w}Может предмет поддерживающий мою жизнь. {w}А может и предмет, который может её прервать в любой момент с большого расстояния...")
    $ Fl.say(Fl_r, "Я перерыл всю бумажную волокиту, но так ничего и не нашёл. Единственное место, которое я оставил без должного внимания - бункер, здесь я и узнал, что этот лагерь существовал и в моём мире...")

    $ Fl.Pause (2.0)
    $ Fl.say(Fl_r, "Я посмотрел на маленький монитор на стене, над «столом». Этот монитор был частью компьютера.")
    $ Fl.say(Fl_r, "Система защищена каким-то паролем. {w}Но прикол в том, что подобрать пароль можно не больше трёх раз, потом система блокируется и всплывает экран смерти.")
    $ Fl.say(Fl_r, "Умно.")
    $ Fl.say(Fl_r, "Интересно сколько раз я подбирал код? {w}Много{mn} Очень много.")
    $ Fl.say(Fl_r, "Но если есть пароль, значит должен быть и код? {w}Довольно просто, правда?")
    $ Fl.say(Fl_r, "Я уныло поднял взгляд на разбросанные бумаги. Кода не было, как и новых ответов.")
    $ Fl.say(Fl_th, "Пора возвращаться. {w}Без электричества здесь делать нечего.")
    $ Fl.say(Fl_r, "По сценарию свет в бункер поступает только на третий день. В тот же день, когда Толян пропадает на целые сутки.")
    $ Fl.say(Fl_th, "Интересно. Может попробовать как-то этого дауна с собой взять...")
    $ Fl.say(Fl_th, "Хахах. Да не, бред! Толян, да включает электричество в бункере{mn} Да с его интелектом только суицид пластиковой вилкой светит!")

    $ Fl.Pause (2.0)
    $ Fl.say(Fl_th, "Хотя глупо было полагать, что из-за дождя ответы сами по себе появяться и весь лагерь заденут колоссальные изменения.")
    $ Fl.say(Fl_th, "И правда, просто аномалия...")
    $ Fl.say(Fl_r, "На последок я нажал на кнопку питания на корпусе, но он не подал никаких признаков жизни.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(4)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause (5.0)
    $ Fl.PlayAmbience("Fl_rain", 1, 5)
    scene Fl_ext_square_rain_night
    show Fl_rain_hard_left
    with Fl_dissolve2
    
    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Оказавшись на поверхности меня ожидала та же картина что и с утра.")
    $ Fl.say(Fl_pi, "Льёт как из ведра...")
    $ Fl.say(Fl_th, "Где-то я уже слышал это выражение{mn} В своём прошлом или в книжке вычитал, не помню.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(3.5)
    $ Fl.PlayAmbience("Fl_rain_vn", 1, 3)
    scene Fl_musclub_rain with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Сидя на полу, я смотрел в окно пока настраивал гитару.")
    $ Fl.say(Fl_r, "Возле меня лежала тетрадка «Композиции Хатсунэ Мику».")
    $ Fl.say(Fl_th, "Это всё что от тебя осталось...")
    $ Fl.say(Fl_r, "Прошло уже немало циклов с тех пор как я нашёл эту тетрадку. В каждом цикле я заучивал ровно одну новую композию. Это стало своего рода стимулом ждать следующий цикл.")

    $ Fl.Pause (2.5)
    $ Fl.say(Fl_r, "В какой-то момент я отбросил гитару в сторону и собирался сломать ногой рояль, но остановился.")

    $ Fl.Pause (2.0)
    $ Fl.say(Fl_th, "Мне нужно найти ответы и отомстить...")
    $ Fl.say(Fl_th, "Тогда чем я мать его сейчас занимаюсь!", _with=hpunch)
    $ Fl.say(Fl_r, "В этот раз без жертв не обошлось, я кинул стул в другой конец комнаты и тот разлетелся на щепки.")
    $ Fl.say(Fl_r, "Мне хотелось выпустить пар, хотелось что-то сломать. {w}Или кого-то...")

    $ Fl.Pause (2.0)
    $ Fl.say(Fl_r, "Лагерь стёр существование Мику, никто её больше не мог вспомнить. Никто{mn} Даже музклуб, забыл о своей хозяйке.")

    $ Fl.Pause (2.0)
    $ Fl.say(Fl_r, "Что такое существование? {w}Это когда ты можешь говорить, есть, ходить и т.д.. {w}Или это когда тебя могут видеть другие?")
    $ Fl.say(Fl_r, "Солипсиизм, да? Отрицание объективной реальности?")
    $ Fl.say(Fl_r, "Всё что видит перед глазами человек является восприятие реальности. Сама реальность - это то что мы видим. {w}Тогда может другие её не правильно воспринимают? Они сами исскажают «исстиную» реальность.")
    $ Fl.say(Fl_r, "Тогда может и никакой тетрадки вовсе не существует? Она только материальна для меня?")
    $ Fl.say(Fl_r, "Получается каждый человек живёт в другой реальности? И мы просто обладаем одинаковыми точками соприкосновения?")
    $ Fl.say(Fl_r, "Интересно, если коллективно перестать верить в существование кого-то, он сможет исчезнуть? {w}Теоретически это тульпа, но в обратную сторону. {w}Тогда может наше существование это простой глюк мозга другого человека?")
    $ Fl.say(Fl_th, "Забавно{mn}")

    $ Fl.PlaySound("Fl_stuk_dver", 1, 0, False)
    $ Fl.say(Fl_r, "Мои размышления прервал отчётливый стук в дверь.")

    $ Fl.PlaySound("Fl_stuk_dver", 1, 0, False)
    $ Fl.say(Fl_r, "Стуки повторились уже более настойчиво.")
    $ Fl.say(Fl_th, "Кого это там ко мне принесло?")

    $ Fl.PlaySound("Fl_stuk_dver", 1, 0, False)
    $ Fl.say(Fl_d, "По... П-пожалу-уйста к-кто-нибудь от... о-откройте!", _with=hpunch)
    $ Fl.say(Fl_r, "Раздался по ту сторону знакомый женский голос.")
    $ Fl.say(Fl_th, "А день я погляжу полон сюрпризов, а ты уже нос повесил!")
    $ Fl.say(Fl_r, "Дождевое отклонение от сценария заставили меня открыть дверь незнакомке.")

    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
    show an cry hood2 with vpunch
    $ Fl.Pause (0.8)
    hide an cry hood2 with Fl_fast

    $ Fl.AttackMaster()
    $ Fl.say(Fl_r, "Внутрь влетела Аня(вроде так её звали). {w}На мгновение она засветила своими зарёванными глазами, а после крепко прижалась ко мне.")
    $ Fl.say(Fl_th, "Какого?!")

    $ Fl.PlayMusic("Fl_sunset_mik", 1, 5)
    $ Fl.say(Fl_r, "Пионерка дрожала как осиновый лист. {w}Женский плач начал резать уши.")
    $ Fl.say(Fl_th, "И как это понимать?")

    $ Fl.AttackMaster(True)
    $ Fl.say(Fl_r, "Я попытался отстранить девушку, но она только сильнее сжала меня в своих объятиях. Плач усилился.")
    $ Fl.say(Fl_pi, "Эй!")
    $ Fl.say(Fl_r, "Моё возмущение не затронуло пионерку. Она просто плакала и дрожала. У неё была истерика.")
    $ Fl.say(Fl_th, "И что вы прикажите мне с ней делать?")
    $ Fl.say(Fl_pi, "Прекрати.")
    $ Fl.say(Fl_pi, "Успокойся! И перестань плакать.")
    $ Fl.say(Fl_r, "Игнор.")
    $ Fl.say(Fl_r, "Я дотронулся до плеч пионерки.")
    $ Fl.say(Fl_r, "Она медленно подняла на меня свой опухщий взгляд.")

    show an cry hood2 with Fl_dissolve1

    if persistent.Fl_dictionary_13 == False:
        $ Fl.PodskDict()
    $ persistent.Fl_dictionary_13 = True
    $ Fl.say(Fl_r, "Шмыг. И ещё один. {w}Девушка тряслась и старалась восстановить дыхание, её грудь с бешенной скоростью качала воздух, будто она боролась с {i}гипоксией{/i}.")
    $ Fl.say(Fl_pi, "Что случилось?")
    $ Fl.say(Fl_r, "Задал вопрос с привычными нотками безразличия.")
    $ Fl.say(Fl_an, "А{mn} А{mn} Ар{mn} Т-та...")

    hide an cry hood2 with Fl_fast

    $ Fl.say(Fl_r, "Девушка снова завыла, ещё пуще прежднего.")
    $ Fl.say(Fl_th, "Мда{mn} Чувствую это надолго.")
    $ Fl.say(Fl_pi, "Ты можешь хоть что-то внятное сказать или так и будешь рыдать?!", _with=hpunch)
    $ Fl.say(Fl_r, "Я давно уже перестал чувствовать сострадание, слишком уж долго я пробыл в эмоцианальной пытке. Да и какие манеры, когда ты общаешься с бездушной куклой. Хотя и ты сам неменее бездушная машина...")
    $ Fl.say(Fl_an, "С-са{mn} С-саша{mn} А-а{mn} Артём{mn} О-они{mn} Они...")
    $ Fl.say(Fl_an, "{b}М-мертвы{/b}!")
    $ Fl.say(Fl_r, "От услышанного меня словно током ударили. Зрачки уменьшились, а губы слегка разжались.")
    $ Fl.say(Fl_th, "Мертвы? {w}Это значит...")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_th, "В лагере объявился сказитель!")
    $ Fl.say(Fl_th, "Точно! Всё как и в том цикле. {w}Аномалия - ввиде пропажи звуков природы и отклонение от сценария повседневной истории «Каникулы в Совёнке».")
    $ Fl.say(Fl_r, "Внутри меня разыгралось множество противоречивых чувств. Стоило ли радоваться или впасть в безумие и рвануть встречать незванного гостя? А может сохранять хладнокровие?")
    $ Fl.say(Fl_r, "Но все эти эмоции сошлись на нет, уступив свою победу - жажде мести.")
    $ Fl.say(Fl_pi, "Где это произошло?")
    $ Fl.say(Fl_an, "{mn}В к-клуб-бах. Я н-нашла и-их тр... т-трупы т-там. Я шл...")
    $ Fl.say(Fl_r, "Одной локации мне было достаточно. Я встал и пошёл в сторону двери.")
    $ Fl.say(Fl_an, "П-подожди ты к-куда?!")

    $ Fl.AttackScreens()
    $ Fl.say(Fl_r, "Пионерка схватила меня за край толстовки.")
    $ Fl.say(Fl_pi, "Сиди здесь тихо и никому дверь не открывай, поняла?")
    $ Fl.say(Fl_r, "Кинул я, глядя через спину суровым взглядом прямо в блестящие глаза девушки.")
    $ Fl.say(Fl_an, "Ты собираешься пойти ТУДА?!")
    $ Fl.say(Fl_r, "Сказала девушка без единой запинки.")
    $ Fl.say(Fl_r, "Ну конечно, только псих пойдёт глядеть на трупы, пока их автор разгуливает по лагерю. {w}И это я.")
    $ Fl.say(Fl_pi, "Я спрашиваю ты поняла?")
    $ Fl.say(Fl_r, "Глаза девушки округлились. Она точно ожидало другого исхода, но позволила себе отпустить меня и молча кивнуть.")
    $ Fl.HideScreens(_with=Fl_fast)
    scene bg Fl_black with Fl_effect_3


    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)

    
    $ Fl.PlayAmbience("Fl_rain", 1, 3)
    scene Fl_ext_musclub_rain_night
    show Fl_rain_hard_left
    with Fl_effect_3
    
    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.StopMusic(6)
    $ Fl.say(Fl_r, "А сам я вышел на улице, оставив эмоцианально нестабильную девушку одну в музклубе, в окружении тёмного леса.")
    $ Fl.say(Fl_r, "На моём лице была широкая улыбка.")
    $ Fl.say(Fl_th, "Прекрасно, наконец-то сегодня кто-то у нас умрёт!")
    $ Fl.say(Fl_r, "Былая жажда и безумие начали возвращаться ко мне. Мои мысли были заполнены жуткими картинами ультранасилия.")
    $ Fl.say(Fl_r, "И вот с такой довольной лыбой, я медленно не спеша направился в сторону клубов, напевая какой-то старый мотивчик.")
    $ Fl.HideScreens(_with=Fl_dissolve1) 
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause (4.5)
    scene Fl_ext_clubs_rain_night
    show Fl_rain_hard_left
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_pi, "А вот и конечная.")
    $ Fl.say(Fl_r, "В предвкушении чего-то ужасного, я без колебаний открыл широко дверь.")
    $ Fl.HideScreens(_with=Fl_fast)
    scene bg Fl_black with Fl_fast

    $ Fl.StopAmbience(3)
    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)

    scene bg Fl_int_clubs_blood_night with Fl_flash
    $ Fl.Pause (2.0)
    $ Fl.say(Fl_r, "Передо мной предстала картина настоящей бойни. Всё помещение было залито кровью. И уже знакомый сладковатый запах ударил мне в нос.")
    $ Fl.say(Fl_r, "Окна и занавески тоже были залиты красным оттенком, поэтому внешнему источнику света было не по силам создать чёткое представление всего происходящего.")
    $ Fl.say(Fl_r, "Наступив на что-то мягкое, я дошёл до переключателя.")

    $ Fl.PlaySound("Fl_switch", 1.0, 0, False)
    scene bg Fl_int_clubs_blood_night_light with Fl_flash
    $ Fl.Pause(1.5)
    $ Fl.PlayMusic("Fl_levantation", 1, 5)
    $ Fl.say(Fl_r, "{mn}")
    $ Fl.say(Fl_r, "Даже такой убийца как я на мгновение потерял дар речи. {w}Почти каждый сантиметр комнаты был в крови жертв. Лампочка тоже преломляла свет в аллый(своего рода бюджетная rgb-лента).")
    $ Fl.say(Fl_r, "Тело Артёма было привязано к стулу. Множество точных и несмертельных ранений было на туше пионера. Убийца явно обладает хирургической точностью.")
    $ Fl.say(Fl_r, "Если бы не кудрявые волосы, я даже не смог бы опознать пионера. Его лицо было изуродовано. Отсуствовал нос, глаза и губы. А на щеках была ровно вырезана улыбка.")
    $ Fl.say(Fl_r, "Артём и Саня - не разлей вода. {w}Поэтому искать его брата акробата долго не пришлось, он так же был привязан к стулу.")
    $ Fl.say(Fl_r, "Седового пионера я узнал сразу, на его лице отсуствовали разве что очки. {w}Но парень сберечь остальное не смог. На стуле сидел лишь его торс и голова, другие части тела отсуствовали.")
    $ Fl.say(Fl_r, "Я бросил взгляд в сторону длинного следа крови, который ввёл в кладовку.")
    $ Fl.say(Fl_r, "Приоткрыв слегка дверь, я нашёл недостоющие детали к конструктору под названием «Саня».")
    $ Fl.say(Fl_r, "Руки и ноги качались на верёвках, которые свисали с потолка.")
    $ Fl.say(Fl_r, "Оставив двух пионеров наслаждаться ремонтом их клуба, я решил вооружиться.")
    $ Fl.say(Fl_r, "В моих руках появилась отвёрка.")
    $ Fl.say(Fl_th, "Как в старые добрые.")

    $ Fl.PlaySound("Fl_switch", 1.0, 0, False)
    scene bg Fl_int_clubs_blood_night with Fl_flash
    $ Fl.say(Fl_r, "Выключив свет, я покинул «скотобойню».")
    $ Fl.HideScreens(_with=Fl_fast)
    scene bg Fl_black with Fl_dissolve1
    $ Fl.StopMusic(4)

    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)

    $ Fl.Pause (2.5)
    $ Fl.PlayAmbience("Fl_camp_center_night", 1, 5)
    scene bg Fl_ext_clubs_night
    show Fl_dust_full
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Дождь прекратился.")
    $ Fl.say(Fl_r, "Я присел на ступенки под козырьком. Хотелось насладиться прохладой после дождя.")
    if persistent.Fl_dictionary_14 == False:
        $ Fl.PodskDict()
    $ persistent.Fl_dictionary_14 = True
    $ Fl.say(Fl_r, "{i}Петрикор{/i} - мне был незнаком, ну по крайне мере я забыл что это такое. Запах жизнедеятельности микроорганизмов, живущих в земле расслаблял.")
    $ Fl.say(Fl_r, "Я смотрел вдаль, играя со своими воображаемыми ночными монстрами - кустами и тенями.")
    $ Fl.say(Fl_d, "Давно не виделись.")
    $ Fl.say(Fl_r, "Я безмолвно перенаправил взгляд к источнику звука.")

    scene cg Fl_heads_off with Fl_effect_2
    $ persistent.Fl_photo_pallery_21 = True
    $ Fl.PlayMusic("Fl_danger", 1, 5)

    $ Fl.say(Fl_r, "Возле фонаря стояла Тихоня. Её пионерская форма была запачкана кровью.")
    $ Fl.say(Fl_r, "Я опустил взгляд чуть ниже. Две обезображенных головы смотрели прямо на меня. {w}Я без понятия кому они принадлежал, скорее всего низщим нпс, которые в лагере заполняют пустое пространство.")
    $ Fl.say(Fl_th, "А вот и автор изящного ремонта в клубах парней.")
    $ Fl.say(Fl_lnt, "Н-н-н-у-у ты даже не попривествуешь меня?")

    scene bg Fl_ext_clubs_night
    show Fl_dust_full
    with Fl_dissolve1

    $ Fl.say(Fl_r, "Я медленно встал.")
    $ Fl.say(Fl_pi, "Дай угудаю, твоих рук дело?")
    $ Fl.say(Fl_r, "Я указал большим пальцем за спину.")
    $ Fl.say(Fl_r, "Красные глаза пионерки сверкнули, она ухмыльнулась.")
    $ Fl.say(Fl_lnt, "Ян, ты глупые вопросы задаёшь. Или ты настолько тупой что не можешь сложить один плюс один?")
    $ Fl.say(Fl_th, "Сочтём как да.")
    $ Fl.say(Fl_r, "Пионерка кинула головы в меня.")
    $ Fl.say(Fl_r, "Я увернулся и на мгновение потерял её из виду.")
    $ Fl.say(Fl_th, "Куда она делась?!")
    $ Fl.say(Fl_lnt, "Я не довольна тобой, милый.")

    show ln smile with Fl_fast:
        fright

    $ Fl.say(Fl_r, "Справа в метре от меня стояла Тихоня. Её пара красных глаз отражали свет луны, тем самым насыщая зрачки прелестным кровавым оттенком.")

    show ln smile:
        ease 2.0 zoom 1.4 yalign 0.5 xalign 0.98

    $ Fl.say(Fl_r, "Тихоня медленно приблизилась ко мне и начала осматривать. Я делал тоже самое. {w}Я пытался вспомнить, как выглядела она в том цикле, когда стояла возле Кукловода.")
    $ Fl.say(Fl_th, "Я уверен она не настоящая, вероятно клон.")
    $ Fl.say(Fl_th, "Такой же клон, что и тогда в шахтах.")
    $ Fl.say(Fl_lnt, "Ого Ян, а ты изменился. Волосы покрасил, приоделся и ошейник нацепил.")
    $ Fl.say(Fl_lnt, "О-{w=0.5}о-{w=0.5}о. {w=1.0}У меня возникла идея, как я могу его использовать!")
    $ Fl.say(Fl_r, "В глазах Тихони загорелся огонёк.")
    $ Fl.say(Fl_lnt, "Я могу сделать из тебя верную собачку, а потом мы вдоволь повеселимся в крова...")
    $ Fl.say(Fl_pi, "Сигарету будешь?")
    $ Fl.say(Fl_r, "Спросил я больше для того, чтобы дать себе передышку перед тем что будет дальше.")
    $ Fl.say(Fl_lnt, "Буду, Ян. После всего, что между нами было, это очень мило с твоей стороны, онии-сан! {w=1}Ня!")
    $ Fl.say(Fl_r, "Я пропускал мимо ушей, весь её психоделический бред.")
    $ Fl.say(Fl_r, "Молча достал две сигареты, одной затянулся. Из полукруга света, который будто бы потускнел, на меня смотрели мои персонализированные грехи.")
    $ Fl.say(Fl_r, "Она взяла сигарету ртом и подала знак, что ей нужна зажигалка.")
    $ Fl.say(Fl_r, "Я кинул ей огниво.")
    $ Fl.say(Fl_r, "Стоило ей только поднести пламя к сигарете, как...")

    $ Fl.StopMusic()
    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    $ Fl.AttackScreens(True)
    scene bg Fl_ext_clubs_night
    show Fl_dust_full
    with vpunch

    $ Fl.say(Fl_r, "Как я резким движение ударил отвёрткой, собираясь проткнуть нижнюю челюсть Леночке.")
    $ Fl.say(Fl_r, "Но фиолетоволосая пионерка легко парировала атаку, будто ожидала чего-то подобного.")
    $ Fl.say(Fl_r, "Она сделала пару тяжек и выкинула сигарету.")

    show ln smile with Fl_fast:
        fright

    $ Fl.say(Fl_lnt, "Ян, ты правда думал что я так легко попадусь? {w}Глупенький!")
    $ Fl.say(Fl_r, "Она наиграно сделала грустуную мордашку.")
    $ Fl.say(Fl_pi, "Тц!")
    $ Fl.say(Fl_lnt, "Ну чего ты расслабь булки, сладкий!")
    $ Fl.say(Fl_r, "Меня перекосило от последнего слова.")
    $ Fl.say(Fl_pi, "Что ты знаешь об этом месте?")
    $ Fl.say(Fl_lnt, "Тоже самое что и ты. Ну можеть чу-чуть больше - совсем всё!")
    $ Fl.say(Fl_pi, "Тогда может начнём всё с начала и ты мне поделишься информацией, дорогая?")
    $ Fl.say(Fl_r, "Я ухмыльнулся.")
    $ Fl.say(Fl_r, "Тихоня затихла(забавная тавтология получилась).")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_lnt, "С радостью! Но есть одно «но».")
    $ Fl.say(Fl_lnt, "Я {w}на {w}тебя {w}обиделась!")
    $ Fl.say(Fl_r, "Тихоня издевательски улыбнулась.")
    $ Fl.say(Fl_lnt, "Ты во мне собирался сделать дырку отвёрткой, бака!")
    $ Fl.say(Fl_pi, "Действительно, что-то я уже подзабыл.")
    $ Fl.say(Fl_r, "Я крепко сжал отвёртку.")
    $ Fl.say(Fl_pi, "Тогда ты мне не нужна, мы расстаёмся!")
    $ Fl.say(Fl_lnt, "Семейные ссоры - это я люблю!")

    show ln smile knife with Fl_fast

    $ Fl.say(Fl_r, "Пионерка достала огромный нож, больше похожий на тесак.")
    $ Fl.say(Fl_r, "С него начала капать кровь. {w}Свежая.")
    $ Fl.say(Fl_lnt, "Ян, будь добр, развлеки даму.")

    hide ln smile knife with Fl_fast

    $ Fl.say(Fl_r, "Пионерка скрылась с моего поле зрения.")
    $ Fl.say(Fl_r, "Удар!{break}")
    jump lena_vs


label lena_vs:
    $ Fl.PlayMusicFrom("<from 85 to 267>", "Fl_MoonDeity_NEON_BLADE", 1, 2)
    scene bg Fl_ext_clubs_night
    show Fl_dust_full
    call screen Fl_lent_qte(randint(0, 6), 0.8, "lena_vs_lose") with vpunch
    jump lena_vs_2




label lena_vs_2:
    call screen Fl_lent_qte(randint(0, 6), 0.9, "lena_vs_lose") with Fade(0.10, 0.20, 0.10, color="990000")
    jump lena_vs_3

label lena_vs_3:
    call screen Fl_lent_qte(randint(0, 6), 0.8, "lena_vs_lose") with hpunch
    jump lena_vs_4

label lena_vs_4:
    call screen Fl_lent_qte(randint(0, 6), 0.8, "lena_vs_lose") with Fade(0.15, 0.10, 0.0, color="ffffff")
    jump lena_vs_5

label lena_vs_5:
    call screen Fl_lent_qte(randint(0, 6), 0.9, "lena_vs_lose") with vpunch
    jump lena_vs_6

label lena_vs_6:
    call screen Fl_lent_qte(randint(0, 6), 0.8, "lena_vs_lose") with Fade(0.10, 0.20, 0.10, color="990000")
    jump lena_vs_win




label lena_vs_lose:
    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    with Fl_flash_red
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "У меня начало темнеть в глазах. Сдавило горло. Я опустил голову вниз, к земле, буравя взглядом землю.")
    $ Fl.say(Fl_th, "Ненавижу её нож!")
    $ Fl.say(Fl_r, "Из живота ручьём пошла кровь, я упал на колени. Живот был вспорот.")
    $ Fl.say(Fl_lnt, "Ты скучный.")
    $ Fl.say(Fl_lnt, "А я так в тебя понадеялась.")
    $ Fl.say(Fl_r, "Тихоня развела руками.")
    $ Fl.say(Fl_pi, "Д-да п-пошла т... ты, т-тварь!")

    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    scene bg Fl_black with vpunch
    $ Fl.say(Fl_r, "В тот же миг, я услышал свист и нож пробил мою черепную коробку.")
    $ Fl.HideScreens(_with=Fl_dissolve2)
    jump pi_say4


label pi_say4:
    $ Fl.Pause (5.0)
    show text "{font=font/Fl_mainmenu.ttf}{size=55}Понимаю о чём ты думаешь.{/size}{/font}"
    with Fl_dissolve1

    $ Fl.Pause (3.0)
    show text "{font=font/Fl_mainmenu.ttf}{size=55}Эта стерва с хвостиками и правда бесит.{/size}{/font}"
    with Fl_dissolve1

    $ Fl.Pause (3.0)
    show text "{font=font/Fl_mainmenu.ttf}{size=55}Поэтому будь добр, убей её!{/size}{/font}"
    with Fl_dissolve1
    jump lena_vs




label lena_vs_win:
    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Сколько бы я не наносил ударов в секунду она с лёгкость их парировала. А тем временем я пару раз чуть головы не лишился.")
    $ Fl.say(Fl_th, "Это она стала сильнее за это время или я слабее?")
    $ Fl.say(Fl_r, "Действительно нынешняя Лена была намного сильнее, чем та из шахт.")

    $ Fl.StopMusic(4)
    show ln smile knife with Fl_fast:
        cright

    $ Fl.say(Fl_lnt, "Ян, ты такой слабый. Твои действия легко предугадать.")
    $ Fl.say(Fl_lnt, "Ты думаешь ты один прочитал книгу по обороне? {w}И{w}ди{w}от.")
    $ Fl.say(Fl_th, "Она права я двигаюсь слишком предсказуемо, но я слишком напряжён!")
    $ Fl.say(Fl_th, "Перемещения Тихони непредсказуемы, а ещё эта нечеловеческая скорость. {w}Так нечестно вообще-то!")

    show mir normal pioner3 with Fl_fast:
        fleft

    $ Fl.say(Fl_r, "Неожиданно на дороге появилась пионерка с пепельными волосами(не могу вспомнить её имя). {w}Она в начале посмотрела на меня, потом на Лену.")
    
    show mir fear pioner3 with Fl_dissolve1
    
    $ Fl.say(Fl_r, "Её взгляд упал на тесак.")
    $ Fl.say(Fl_r, "Тихоня посмотрела на пионерку и хищно улыбнулась.")

    hide mir fear pioner3 with Fl_fast

    $ Fl.say(Fl_r, "Пионерка тут же среагировала и с криками рванула прочь.")

    hide ln smile knife with Fl_fast

    $ Fl.say(Fl_r, "Но было уже поздно, Тихоня в мгновение ока оказалась перед ней.")
    $ Fl.say(Fl_th, "Да как она это делает?!")
    $ Fl.say(Fl_r, "Лена заломала руку пионерке и подставила ей нож у горла.")
    $ Fl.HideScreens()


    scene cg Fl_mik
    show Fl_prolog_dream
    with Fl_fast
    $ Fl.Pause(0.7)

    scene bg Fl_ext_clubs_night
    show Fl_dust_full
    with Fl_fast

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Перед глазами всплыло то чего не хотелось бы вспоминать.")
    $ Fl.say(Fl_lnt, "Эй, дорогой, сдавайся. Иначе я её убью.")
    $ Fl.say(Fl_r, "Я не сдержался.")
    $ Fl.say(Fl_pi, "Пх-хахах. Ты серьёзно? Решила мне угрожать куклой? Совсем дура?")
    $ Fl.say(Fl_r, "На её лице нарисовалась мерзкая улыбка.")
    $ Fl.say(Fl_lnt, "И это мне говорит человек, который недавно сам оплакивал куклу?")
    $ Fl.say(Fl_th, "{mn}")
    $ Fl.say(Fl_lnt, "Я всё видела, Ян. {w}Как твоя японочка пустила фонтан крови из артерии, а ты ревел как мальчишка над её трупом.")
    $ Fl.say(Fl_r, "Она громко засмеялась и уставила свой хищный взгляд прямо на меня.")
    $ Fl.say(Fl_lnt, "Знаешь, я ведь сама хотела её убить прямо на твоих глазах, или нет даже хуже{mn} Но {b}он{/b} опередил меня.")
    $ Fl.say(Fl_lnt, "Хотя влюбится в куклу после того что ты с ней делал. Ты и правда безумец.")
    $ Fl.say(Fl_pi, "Ххахах.")
    $ Fl.say(Fl_lnt, "Прости я не слышу можешь погромче.")
    $ Fl.say(Fl_pi, "<С*ка>...")


    $ Fl.DayTime("kira", "night")


    $ Fl.PlayMusicFrom("<from 85 to 267>", "Fl_MoonDeity_NEON_BLADE", 1, 4)
    $ Fl.say(Fl_pib, "АХАХАХ. КАКАЯ ЖЕ ТЫ ТУПАЯ <С*КА>!", _with=hpunch)
    $ Fl.say(Fl_r, "Я залился безумным хохотом. {w}Пионерка с пепельными волосами затряслась ещё сильнее. В её глазах отразился монстр, похлеще того, который поднёс лезвие холодного оружия к горлу.")
    $ Fl.say(Fl_lnt, "Милый, неужели ты вернулся! Я так рада. Я так соскучилась по твоему безумию.")
    $ Fl.say(Fl_r, "Адреалин начал зашкаливать. Началась ломка, я хотел убивать, хотел превратить из пионерки фарш или того хуже.")
    $ Fl.say(Fl_pib, "Не недооценивай меня!")
    $ Fl.say(Fl_pib, "Сейчас ты составишь кампанию тем двоим.")
    $ Fl.say(Fl_r, "Собеседница поняла на что я намекаю, переведя взгляд на здание клубов.")
    $ Fl.say(Fl_lnt, "Правда, как жаль ведь тогда она ум{break2}")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    with hpunch
    $ Fl.say(Fl_r, "Но я не дал ей договорить. {w}Я быстро сократил дистанцию и со всей силы ударил с ноги пионерку с пепельными волосами. Удар был настолько сильный что пионерка отлетела на пару метров.")
    $ Fl.say(Fl_r, "Тихоня пробыв пару секунд в замешательстве приняла решение направить тесак в мою сторону, но было поздно.")

    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    $ Fl.say(Fl_r, "Я вонзил отвёрку ей в плечо. И схватив за волосы, ударил её головой об фонарный столб.")
    $ Fl.say(Fl_r, "Даже не пискнув Тихоня крутанулась на 180 градусов с тесаком. Лезвие прошло в пару сантиметров от моего лица, но я не дрогнул.")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.AttackScreens()
    $ Fl.say(Fl_r, "Моей контроатакой был сильный удар в поддых.")
    $ Fl.say(Fl_r, "Лезвие ножа изменило траекторию и всё же зацепило меня.")
    $ Fl.say(Fl_r, "Ещё один удар и я не успел уклониться. {w}Закрыв лицо руками, на предплечье появилась красная линия и горячие капли начали обжигать кожу.")
    $ Fl.say(Fl_r, "В фазе безумия я наконец-то мог поспевать за движениями Тихони и сражаться не через защиту.")
    $ Fl.say(Fl_r, "Безумный смех и свист оружий заполнил всё вокруг.")
    $ Fl.say(Fl_r, "Стоило Тихоне открыться, как я схватился за рукоять отвёртки и дёргнул её под таким углом, что раздался хруст костей.")
    $ Fl.say(Fl_pib, "Хрусь!")
    $ Fl.say(Fl_r, "Тихоня не проронила ни звука.")
    $ Fl.say(Fl_th, "Странно{mn} Она вообще боль чувствует?")
    $ Fl.say(Fl_r, "Необращая внимания на странности моего оппонента, я вложил всю силу в удар и откинул пионерку в стену здания клубов.")
    $ Fl.say(Fl_r, "Она сползла вниз и упала головой вниз.")
    $ Fl.say(Fl_r, "Под Тихоней образовалась приличная лужа крови, грудь больше не двигалась.")

    $ Fl.StopMusic(3)
    $ Fl.say(Fl_r, "Я наклонился чтобы точно убедиться, что пионерка мертва.")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_th, "Не дышит.")
    $ Fl.say(Fl_pib, "Всё кончено.")
    $ Fl.say(Fl_lnt, "Ты так думаешь?")
    $ Fl.say(Fl_pib, "Что{break}")

    with Fl_flash_red
    $ Fl.AttackScreens()
    $ Fl.PlayMusic("Fl_inquiry", 1, 5)
    $ Fl.say(Fl_pib, "ААААААА!", _with=vpunch)
    $ Fl.say(Fl_r, "Я схватился за щеку, которую только что укусила «мёртвая» Тихоня.")
    $ Fl.say(Fl_pib, "Почему ты жива?")
    $ Fl.say(Fl_lnt, "Хахаха. Тебя очень легко провести знаешь ли. {w}Я просто задержала дыхание и ты сразу повёлся.")
    $ Fl.say(Fl_lnt, "Хотя если ты решил бы проверить пульс, то точно погиб!")
    $ Fl.say(Fl_r, "Я не мог поверить своим глазам. Раны Тихони были серьёзными, она потеряла много крови, но продолжала стоять как ни в чём не бывало.")
    $ Fl.say(Fl_lnt, "Ян, а ты поразительно умеешь расположить к себе даму!")
    $ Fl.say(Fl_lnt, "Но к сожалению игры кончились, я разочарована в тебе. Ты худший сказитель с каким я только дралась.")
    $ Fl.say(Fl_r, "Я заскрипел зубами, держа правую щеку, которая начинала сильно ныть.")
    $ Fl.say(Fl_lnt, "Но знаешь, почему-то мне не хочется тебя убивать, ты милый, красивый. {w}Ты и правда мне нравишься. И я хочу чтобы ты был только моим!")
    $ Fl.say(Fl_pib, "Эй, ответь твоя же способность клонирование?")
    $ Fl.say(Fl_r, "Прервал я монолог Тихони.")
    $ Fl.say(Fl_lnt, "Бинго! {w}А ты как думаешь, почему я до сих пор стою на ногах?")
    $ Fl.say(Fl_th, "Значит я был прав с самого начала...")
    $ Fl.say(Fl_th, "Но каким образом она им управляет? {w}Может она прячеться где-то в кустах или в домике засела? {w}Как-то же она посылает клону команды!")
    $ Fl.say(Fl_lnt, "Прости меня, сладкий, но нам пора прощаться!")
    $ Fl.say(Fl_r, "Тихоня снова пропала с полезрения.")
    $ Fl.say(Fl_th, "Где она?!", _with=hpunch)

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    scene bg Fl_black with hpunch
    $ Fl.say(Fl_r, "Но ломать голову над этим вопросом мне не пришлось. {w}Я почувствовал дикую боль в области затылка, в глазах всё погасло.")
    $ Fl.say(Fl_r, "Я дотронулся до шеи и случайно задел устройство, раздался какой-то писк. Шум врезался в уши и я наконец-то коснулся ушибленного места.")

    scene bg Fl_ext_clubs_night
    show Fl_dust_full
    show Fl_vignette2
    with Fl_dissolve2

    $ Fl.say(Fl_r, "Пелена пропала, но дикая боль осталась и звон в ушах не давал мне покоя.")
    $ Fl.say(Fl_lnt, "Не вырубился. {w}Ох, Ян, сегодня точно не твой день. Тебе придётся потерпеть.")
    $ Fl.say(Fl_r, "Тихоня появилась перед моим лицом словно скример из дешёвого хоррора.")
    $ Fl.say(Fl_r, "Лезвие тесака устремилось прямо в меня.")
    $ Fl.say(Fl_th, "Чёрт! Я не успею!", _with=hpunch)
    $ Fl.say(Fl_r, "Направив все свои силы в ноги, я постарался отскочить назад на сколько это возможно.")
    $ Fl.HideScreens()


    scene bg Fl_ext_houses_night2
    show Fl_dust_full
    show Fl_vignette2
    with hpunch

    $ Fl.AttackMaster(True)
    $ Fl.say(Fl_r, "Но что-то пошло не так. Меня отбросила на добрых пару десятков метров.", _with=Fl_flash_red)
    $ Fl.say(Fl_r, "Моей опорой, которая остановила полёт, оказалась стена дома.")
    $ Fl.say(Fl_th, "Что это мать его было?!", _with=hpunch)
    $ Fl.say(Fl_r, "Кое-как мне удалось удержать равновесие на своих двоих. {w}Пару сломанных рёбер и боль по всему телу - результат моего столкновения.")
    $ Fl.say(Fl_r, "Я бросил взгляд вперёд. {w}Отсюда едва можно было разглядеть здание клубов.")
    $ Fl.say(Fl_th, "Это же с какой силой меня должно было откинуть?!")
    $ Fl.say(Fl_r, "В дали что-то блеснуло.")
    $ Fl.say(Fl_th, "Что за...")
    $ Fl.say(Fl_r, "Я резко отпрыгнул в сторону.")
    with hpunch

    $ Fl.PlaySound("Fl_distanceknifehit", 1, 0, False)
    with Fl_flash_red
    $ Fl.say(Fl_r, "И снова дикая боль.")
    $ Fl.say(Fl_r, "Меня вновь откинуло в сторону с бешенной силой, на этот раз я влетел в рядом стоящую скамейку.")
    $ Fl.say(Fl_r, "Подо мной валялись доски и щепки. По всей видимости это была та самая скамейка в которую я секунду назад влетел.")
    $ Fl.say(Fl_th, "Что со мной происходит?!", _with=hpunch)
    $ Fl.say(Fl_r, "Мне стало по-настоящему страшно. Я не понимал что со мной происходит, тело будто перестало меня слушать.")
    $ Fl.say(Fl_r, "Каждое движение было слишком быстрое и невероятно энергичное. Словно я вот-вот готов взорваться от такого количества энергии, а тело пытается от неё избавиться.")
    $ Fl.say(Fl_th, "Блеск, точно!")
    $ Fl.say(Fl_r, "Этот блеск - был ничем иным, как блики света на острие металла.")
    $ Fl.say(Fl_r, "Я бросил взгляд в сторону торчащего из стены предмета.")
    $ Fl.say(Fl_th, "Отвёрка, серьёзно?")
    $ Fl.say(Fl_lnt, "Хаха. Ян, что это было? Хахах.")
    $ Fl.say(Fl_lnt, "Ты в тайне учился летать или как ты объяснишь представление, которое ты тут устроил?")

    show ln shadow with Fl_dissolve1:
        cleft

    $ Fl.say(Fl_r, "В свете фонаря появилась знакомая фигура с двумя хвостиками.")
    $ Fl.say(Fl_r, "Страх охватил меня ещё сильнее. Я больше был не в силах дать отпор Тихоне. Она может и не чувствовала боль, а вот я наоборот старался не закричать.")
    $ Fl.say(Fl_lnt, "Ладно, думаю теперь ты от меня всё равно не сбежишь. Поэтому{mn} Я сегодня добрая, разрешаю задать тебе один вопрос, сладенький.")
    $ Fl.say(Fl_r, "Мне было сейчас далеко не до её вопросов. Но это был мой шанс протянуть время и придумать как спасти свою задницу.")
    $ Fl.say(Fl_r, "Но так же эта была возможность пойти ва-банк, поставив на кон всё и услышать ответ на вопрос который меня мучал уже множество циклов.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    jump lent_vibor


label pi_say5:
    $ Fl.Pause (5.0)
    show text "{font=font/Fl_mainmenu.ttf}{size=55}Мда...{/size}{/font}"
    with Fl_dissolve1

    $ Fl.Pause (3.0)
    show text "{font=font/Fl_mainmenu.ttf}{size=55}Пароль ты будешь спрашивать у себя от архива «Домашка»{/size}{/font}"
    with Fl_dissolve1

    $ Fl.Pause (3.0)
    show text "{font=font/Fl_mainmenu.ttf}{size=55}А теперь вернись обратно и хорошо подумай!{/size}{/font}"
    with Fl_dissolve1
    jump lent_vibor


label lent_vibor:
    scene bg Fl_ext_houses_night2
    show Fl_dust_full
    show Fl_vignette2
    show ln shadow:
        cleft
    with Fl_dissolve1

    if lnt_v == 1:
        menu:
            "В каких ты отношениях с Кукловодом":
                $ Fl.ShowScreens(_with=Fl_fast)
                $ Fl.say(Fl_lnt, "Неужели ты ревнуешь? Ян, это так мило с твоей стороны.")
                $ Fl.say(Fl_r, "Я сделал серьёзное лицо, демонстрируя что такой ответ меня не устраивает.")
                $ Fl.say(Fl_lnt, "Ладно не обижайся. Между нами ничего нет, честно!")
                $ Fl.say(Fl_lnt, "На самом деле Кукловод - это загадка, никто не знает откуда он взялся и сколько за его спиной прожитых циклов.")
                $ Fl.say(Fl_lnt, "А что касается меня с ним. {w}Всё что между нами есть - только факт что мы сказители и мы ненавидим друг друга.")
                $ Fl.say(Fl_pib, "Что между вами произошло?")
                $ Fl.say(Fl_lnt, "А вот это, Ян...")
                
                show ln smile knife:
                    ease 1.0 zoom 1.4 yalign 0.5 xalign 0.2

                $ Fl.say(Fl_r, "Пионерка оказалась в полметра от меня.")
                $ Fl.say(Fl_lnt, "Уже второй вопрос, а мы так не договаривались!")
                $ Fl.say(Fl_lnt, "Прощай, милый!")
                $ Fl.say(Fl_pib, "Прощай, {b}дорогая{/b}!")

            "Какого цвета на тебе трусы":
                $ Fl.ShowScreens(_with=Fl_fast)
                $ Fl.StopMusic(3)
                $ Fl.say(Fl_lnt, "{mn}")
                $ Fl.say(Fl_r, "Тихоня резко замерла и замолчала.")
                $ Fl.say(Fl_r, "Именно такой реакции я и добивался задавая такой идиотский вопрос девушке(мы же не в каком-то аниме с фансервисом!).")
                $ Fl.say(Fl_r, "Пока Лена сломалась, я принялся размышлять что мне делать дальше. Подыхать от рук Бога это одно, а от ненормальной пионерки с закосом под яндеру мне не хотелось!")
                
                $ Fl.PlayMusic("Fl_watch_dees", 1, 0)
                $ Fl.say(Fl_lnt, "Чёрные кружева.")
                $ Fl.say(Fl_pib, "А?")
                $ Fl.say(Fl_th, "А вот это неожиданно...")
                $ Fl.say(Fl_lnt, "Знаешь они довольно сексульные. Если хочешь я могу тебе их показать?")
                $ Fl.say(Fl_lnt, "Но плата за просмотр будет высока.")
                $ Fl.say(Fl_pib, "Пожалуй откажусь.")
                $ Fl.say(Fl_lnt, "Вот как.")
                $ Fl.StopMusic(2)

                show ln smile knife:
                    ease 1.0 zoom 1.4 yalign 0.5 xalign 0.2

                $ Fl.PlayMusic("Fl_inquiry", 1, 5)
                $ Fl.say(Fl_r, "Пионерка оказалась в полметра от меня.")
                $ Fl.say(Fl_lnt, "Очень жаль.")
                $ Fl.say(Fl_r, "Я ухмыльнулся.")
                $ Fl.say(Fl_th, "Попалась!")


            "Пароль от компьютера в бункере":
                $ Fl.ShowScreens(_with=Fl_fast)
                $ Fl.say(Fl_lnt, "Пароль от компьютера{mn} Аааа. Я поняла о чём ты.")
                $ Fl.say(Fl_lnt, "Прости, но какой правильный пароль я не знаю.")

                hide ln shadow with Fl_fast

                $ Fl.say(Fl_r, "Тихоня снова пропала с поле зрения.")
                $ Fl.say(Fl_pib, "Стой! Ты ведь обещала, что ответишь на мой вопрос!")
                $ Fl.say(Fl_lnt, "А я и ответила!")
                $ Fl.say(Fl_r, "Я хотел было возразить, но было поздно.")
                scene bg Fl_black with Fl_flash_red 

                $ Fl.say(Fl_r, "Одним быстрым движение и пионерка разрубила мою голову пополам.")
                $ lnt_v -= 1
                $ Fl.HideScreens(_with=Fl_dissolve2)
                jump pi_say5


    else:
        menu:
            "В каких ты отношениях с Кукловодом":
                $ Fl.ShowScreens(_with=Fl_fast)
                $ Fl.say(Fl_lnt, "Неужели ты ревнуешь? Ян, это так мило с твоей стороны.")
                $ Fl.say(Fl_r, "Я сделал серьёзное лицо, демонстрируя что такой ответ меня не устраивает.")
                $ Fl.say(Fl_lnt, "Ладно не обижайся. Между нами ничего нет, честно!")
                $ Fl.say(Fl_lnt, "На самом деле Кукловод - это загадка, никто не знает откуда он взялся и сколько за его спиной прожитых циклов.")
                $ Fl.say(Fl_lnt, "А что касается меня с ним. {w}Всё что между нами есть - только факт что мы сказители и мы ненавидим друг друга.")
                $ Fl.say(Fl_pib, "Что между вами произошло?")
                $ Fl.say(Fl_lnt, "А вот это, Ян...")

                show ln smile knife:
                    ease 1.0 zoom 1.4 yalign 0.5 xalign 0.2

                $ Fl.say(Fl_r, "Пионерка оказалась в полметра от меня.")
                $ Fl.say(Fl_lnt, "Уже второй вопрос, а мы так не договаривались!")
                $ Fl.say(Fl_lnt, "Прощай, милый!")
                $ Fl.say(Fl_pib, "Прощай, {b}дорогая{/b}!")

            "Какого цвета на тебе трусы":
                $ Fl.StopMusic(3)
                $ Fl.ShowScreens(_with=Fl_fast)
                $ Fl.say(Fl_lnt, "{mn}")
                $ Fl.say(Fl_r, "Тихоня резко замерла и замолчала.")
                $ Fl.say(Fl_r, "Именно такой реакции я и добивался задавая такой идиотский вопрос девушке(мы же не в каком-то аниме с фансервисом!).")
                $ Fl.say(Fl_r, "Пока Лена сломалась, я принялся размышлять что мне делать дальше. Подыхать от рук Бога это одно, а от ненормальной пионерки с закосом под яндеру мне не хотелось!")
                
                $ Fl.PlayMusic("Fl_watch_dees", 1, 0)
                $ Fl.say(Fl_lnt, "Чёрные кружева.")
                $ Fl.say(Fl_pib, "А?")
                $ Fl.say(Fl_th, "А вот это неожиданно...")
                $ Fl.say(Fl_lnt, "Знаешь они довольно сексульные. Если хочешь я могу тебе их показать?")
                $ Fl.say(Fl_lnt, "Но плата за просмотр будет высока.")
                $ Fl.say(Fl_pib, "Пожалуй откажусь.")
                $ Fl.say(Fl_lnt, "Вот как.")
                $ Fl.StopMusic(2)

                show ln smile knife:
                    ease 1.0 zoom 1.4 yalign 0.5 xalign 0.2

                $ Fl.PlayMusic("Fl_inquiry", 1, 5)
                $ Fl.say(Fl_r, "Пионерка оказалась в полметра от меня.")
                $ Fl.say(Fl_lnt, "Очень жаль.")
                $ Fl.say(Fl_r, "Я ухмыльнулся.")
                $ Fl.say(Fl_th, "Попалась!")



    scene bg Fl_ext_clubs_night
    show Fl_dust_full
    show Fl_vignette2
    with hpunch
    $ Fl.StopMusic(4)
    $ Fl.Pause (1.0)
    $ Fl.say(Fl_lnt, "Ч-что? Л-люби... Любимый...")
    $ Fl.say(Fl_r, "Тихоня выронила из рук нож и напоследок протянула руку к моему лицу.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Клон Лены окончательно погиб.")
    $ Fl.say(Fl_r, "Я оставил торчать кол в Тихоне, а сам попятился назад.")
    $ Fl.say(Fl_r, "В тот момент, пока Тихоня отвечала на мой поставленный вопрос, я незаметно спрятал заострённый кусок доски от скамейки, которую разнёс на куски.")
    $ Fl.say(Fl_r, "Примерно поняв, что происходит с моим телом, я решил этим воспользоваться и совершить рывок, выставив спрятаный кол вперёд, как только Лена сократит дистанцию.")
    $ Fl.say(Fl_r, "Но даже я такого неожидал, тело Тихони впечаталась в стену, а кол слёгкостью пробил грудную клетку.")
    $ Fl.HideScreens(_with=Fl_dissolve1)



    $ Fl.DayTime("night", "night")


    $ Fl.Pause (2.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Окончательно убедившись, что Тихоня больше не решит воскреснуть, я медленно сполз по ступенькам.")
    $ Fl.say(Fl_r, "Каждый шаг давался с трудом, я до сих пор не контролирую своё тело и могу в любой момент опять куда-то влететь. {w}Не хватало ещё так глупо умереть, после того что мне пришлось пережить этой ночью.")
    $ Fl.say(Fl_r, "Моё внимание привлёк красный огонёк отрожающийся в большой луже.")
    $ Fl.say(Fl_r, "Я присел чтобы лучше рассмотреть что послужило источником красной точки.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Источником оказалось устройство на моей шее.")
    $ Fl.say(Fl_th, "Но как...")
    $ Fl.say(Fl_r, "Я вспомнил момент битвы. Когда я коснулся шеи и услышал какой-то писк.")
    $ Fl.say(Fl_th, "Так это был он!")
    $ Fl.say(Fl_th, "Но каким образом?! Я же тчательно осмотрел его и не нашёл никаких кнопок питания, почему он включился? Включился именно сейчас?!")
    $ Fl.say(Fl_r, "Я начал шупать устройство в том же месте, что и во время сражения с Тихоней.")

    $ Fl.Pause (2.0)
    $ Fl.say(Fl_r, "Звук вновь повторился и лампочка перестала светиться. {w}Переключатель оказался с тыльной стороны ошейника, если конечно можно так сказать, потому что никакой выпуклости я не почувствовал, устройство было максимально гладким.")
    $ Fl.say(Fl_r, "Меня словно током ударило. {w}Что если мои странные способности и резкие полёты рук ошейника?")
    $ Fl.say(Fl_r, "Я медленно поднялся.")
    $ Fl.say(Fl_pi, "Ну была не была!")

    $ Fl.AttackMaster(True)
    $ Fl.say(Fl_r, "Я резко отскочил назад.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Ничего. {w}Обычный прыжок без полётов и столкновений в стену.")
    $ Fl.say(Fl_pi, "Что же ты на самом деле со мной сделал, учёный недоделанный!")
    $ Fl.say(Fl_r, "Я бросил взгляд на пионерку с пепельным цветом волос.")
    $ Fl.say(Fl_r, "Она лежала без сознания, но я на всякий случай решил убедиться жива ли она.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_th, "Пульс есть.")
    $ Fl.say(Fl_r, "На шее пионерки был слабый порез. Тихоне всё же удалось задеть её.")
    $ Fl.say(Fl_r, "Я расстегнул пуговицы рубашки.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_th, "Всё в порядке. Внутреннего кровотечения нет.")
    $ Fl.say(Fl_pi, "Прости{mn} Мне пришлось ударить тебя. Иначе сейчас бы я извинялся перед трупом.")
    $ Fl.say(Fl_r, "Не знаю зачем я попросил прощения у куклы. {w}Ведь мои слова для неё всё равно ничего не значат, после того что я со всеми ими делал.")
    $ Fl.say(Fl_r, "Наверное я это сказал, чтобы потешить себя и не забивать голову бессполезным состраданием к бездушным куклам.")
    $ Fl.say(Fl_pi, "Пора идти.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause (4.0)
    scene bg Fl_ext_medstation_night_light
    show Fl_dust_full
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Сквозь окна пробивался свет и мне пришлось скрываться меж деревьями чтобы добраться до двери незамеченным.")
    $ Fl.say(Fl_r, "Я аккуратно положил сероволосую пионерку у двери. {w}И постучался.")

    $ Fl.PlaySound("Fl_stuk_dver", 1, 0, False)
    $ Fl.Pause (2.0)
    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
    $ Fl.say(Fl_r, "Медсеста выглянула наружу. Заприметив пионерку, она сразу же ринулась на помощь.")
    $ Fl.say(Fl_th, "Теперь ты будешь в порядке.")
    $ Fl.say(Fl_r, "Прихрамывая, я отправился в музклуб.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause (4.0)
    scene bg Fl_ext_musclub_night
    show Fl_dust_full
    with Fl_dissolve2
    $ Fl.PlayMusic("Fl_day1_mi", 1, 4)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Тело ныло, каждый шаг давался с трудом. Не таких последствий я ожидал от сражения...")
    show Fl_prolog_dream
    $ Fl.Pause(1.0)
    hide Fl_prolog_dream
    scene bg Fl_int_musclub_night with Fl_dissolve2

    $ Fl.Pause (2.0)
    $ Fl.say(Fl_mip, "Ян, ты в порядке?")

    show mi sad pioneer5 with Fl_dissolve1

    $ Fl.Pause (2.0) 
    scene bg Fl_int_musclub_night
    show Fl_prolog_dream
    $ Fl.Pause(1.0)
    hide Fl_prolog_dream

    show an sad hood2 with Fl_dissolve1

    $ Fl.say(Fl_anp, "Что произошло? Ян, ответь.")

    show an sad hood2 with moveinleft:
        fright

    $ Fl.say(Fl_r, "Я молча прошёл мимо девушки.")

    hide an sad hood2 with Fl_fast

    $ Fl.say(Fl_anp, "Эй! Ты меня вообще слышишь?")
    $ Fl.say(Fl_r, "Взяв из кладовки все медикаменты, которые я украл в первый же день из медпункта, я снял с себя толстовку.")
    $ Fl.say(Fl_anp, "Ты что творишь, извра...")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_anp, "Ян, почему у тебя кровь{mn} и{mn} на тебе нет живого места...")
    $ Fl.say(Fl_r, "Я продолжал игнорировать куклу.")
    $ Fl.say(Fl_r, "Всё моё тело было в синиках, порезах и гематомах. Так же были и другие серьёзные травмы, сломанные рёбра в некоторых местах и вывернутые пальцы.")
    $ Fl.say(Fl_anp, "Ян!")
    $ Fl.say(Fl_pi, "Что?!")
    $ Fl.say(Fl_r, "Гаркнул я на куклу.")

    show an cry hood2 with Fl_dissolve1:
        fright

    $ Fl.say(Fl_anp, "Ч-что с тобой п-произошло, прошу с-скажи... я... я хочу знать. {w}Расскажи мне пожалуйста...")
    $ Fl.say(Fl_r, "Из глаз пионерки текли слёзы. Она смотрела прямо на меня. Ей было страшно...")
    $ Fl.say(Fl_pi, "Длинная история... Возвращайся лучше домой, это была трудная ночь. Тебе стоит отдохнуть.")
    $ Fl.say(Fl_anp, "Но{mn} Но там же...")
    $ Fl.say(Fl_pi, "Лагерю больше ничего не угрожает. Поэтому иди домой, я всё равно не обязан тебе что-то объяснять.")
    $ Fl.say(Fl_r, "Пионерка собиралась что-то сказать, но передумала.")

    hide an cry hood2 with Fl_dissolve1

    $ Fl.say(Fl_r, "Опустив голову, она направилась к выходу.")
    $ Fl.say(Fl_anp, "Спасибо{mn} Я верю тебе...")

    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
    $ Fl.say(Fl_r, "Я резко повернулся в сторону проёма, но пионерки уже не было. Она быстро расстворилась за границей света фонаря.")

    $ Fl.StopMusic(4)
    $ Fl.say(Fl_r, "Вздохнув и стиснув зубы, я принялся оказывать себе медицинскую помощь.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.PlaySound("Fl_pause_time", 1.0, 2, False)
    scene Fl_pause
    with Fl_effect_time_pause

    $ Fl.Pause (3.5)
    scene bg Fl_black with Fl_dissolve2
    $ Fl.Pause (1.5)

    scene bg Fl_ext_musclub_night
    show Fl_dust_full
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.PlayMusic("Fl_piano_believe_me", 1, 6)
    $ Fl.say(Fl_r, "И вот я в полном одиночестве сидел на ступеньках весь в бинтах и слипшихся от крови волос, курил последнюю сигарету(череда событый израсходовала мой недельный запас).")
    $ Fl.say(Fl_r, "Слова благодарности не выходили из моей головы.")
    $ Fl.say(Fl_r, "Я посмотрел на пространство слева от себя.")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_pi, "Как же мне вас не хватает... {w}Кристина... {w}Мику...")
    $ Fl.say(Fl_r, "Моё воображение нарисовала двух пионерок, которые тепло улыбаются мне и всячески стараются подбодрить. {w}Пионерок - существование которых лагерь стёр навсегда.")
    $ Fl.say(Fl_th, "Возможно могло быть всё иначе...")
    $ Fl.say(Fl_th, "Мне бы не пришлось страдать от одиночества.")
    $ Fl.say(Fl_th, "Я бы не сошёл с ума, став монстром ликующего в море крови.")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_th, "Но что случилось то случилось. {w}Как бы не было трудно осозновать, но у меня есть цель к которой я должен идти вверх с поднятой головой!")
    $ Fl.say(Fl_r, "Мой путь принесёт ещё больше боли и страданий, да и наврядли я останусь человеком. Но я хотя бы смогу их сделать чуточку счастливее. Где бы они не были, они будут спокойны...")
    $ Fl.say(Fl_r, "Этот цикл частично расскрыл мне занавес.")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_r, "Теперь я знаю что устройство на шее непростая безделушка. {w}Способность Тихони - клонирование.")
    $ Fl.say(Fl_r, "Мне нужно только отыскать настоящую Тихоню, которая создает клонов. {w}Хотя да, задача не настолько простая чтобы использовать слово «только».")
    $ Fl.say(Fl_r, "Но впервую очередь я обязан понять, как работает это странное устройство. {w}Если я научусь им пользовать, то смогу дать отпор сказителю, а пока лишь грубой силы и безумию не победить людей выходящих за грань реальности.")
    $ Fl.say(Fl_th, "Хотя людьми их точно не назовёшь...")
    $ Fl.say(Fl_pi, "Моя цель уничтожить всю тьму лагеря и отомстить за вас обеих.")
    $ Fl.say(Fl_r, "Я снова перевёл взгляд в ту сторону, где мозг дорисовывал дорогих мне пионерок.")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_r, "Выкинув сигарету в кусты, я накинул на себя толстовку.")

    $ Fl.StopMusic(4)
    scene bg Fl_night_sky_lager with Fl_dissolve2

    $ Fl.say(Fl_r, "Я поднял голову высоко-высоко вверх. Луна с звёздами одарили меня своим взором.")
    $ Fl.say(Fl_pi, "Что ж пора идти дальше...")
    $ Fl.StopAmbience(6)
    $ Fl.HideScreens(_with=Fl_dissolve2)
    scene bg Fl_black with Fl_dissolve3



    $ Fl.DayTime("rain", "rain")


    $ Fl.Pause(9.5)
    scene bg Fl_ext_square_night
    show Fl_dust_full
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.PlayMusic("Fl_demo_amb", 1, 6)
    $ Fl.say(Fl_r, "Площадь заполнила небольшая компания гостей.")
    $ Fl.say(Fl_r, "В самом углу на скамейке сидела девушка в пионерской форме. Её фиолетовые хвостики забавно подпрыгивали.")
    $ Fl.say(Fl_liz, "Тихоня, а что ты читаешь?")
    $ Fl.say(Fl_r, "Спросила девушка с растёгнутой рубашкой, выставляя свой белый бюстгальтер на показ. Её волосы красного, словно пламя, оттенка развивались на ветру.")
    $ Fl.say(Fl_lnt, "Унесённые ветром.")
    $ Fl.say(Fl_r, "Лениво ответила фиолетоволосая девушка.")
    $ Fl.say(Fl_lnt, "И будь добра отойди, ты своими бедонами мне свет от фонаря закрываешь.")
    $ Fl.say(Fl_liz, "Праааавда. Как скажешь.")
    $ Fl.say(Fl_r, "После чего на землю полетели осколки от лампочки.")
    $ Fl.say(Fl_liz, "Нет света - нет проблем.")
    $ Fl.say(Fl_r, "Пионерка отложила книгу и быстрым движением руки поднесла нож к горлу девушки.")
    $ Fl.say(Fl_lnt, "Да я погляжу ты у нас самая умная, да?")
    $ Fl.say(Fl_qu, "Заткнитесь! Вас сюда не ради этого позвали!")
    $ Fl.say(Fl_r, "Девушки повернули голову.")

    scene cg Fl_lip_on_bench_1 with Fl_dissolve2
    $ persistent.Fl_photo_pallery_22 = True

    $ Fl.say(Fl_r, "На другом конце площади невозмутимо сидела ещё одна девушка.")
    $ Fl.say(Fl_r, "В отличие от тех двоих на ней не было пионерской формы. {w}Чулки, рваная юбка и открытый вверх. Такой наряд сильно выделялся в атмосфере обычного пионерлагеря.")
    $ Fl.say(Fl_r, "Пионерка с хвостиками опустила нож и села обратно. Сложно было сказать, что остудило её пыл, слова девушки в странном наряде или же собственная воля.")

    scene bg Fl_ext_square_night
    show Fl_dust_full
    with Fl_dissolve2

    $ Fl.say(Fl_r, "Помимо представительниц женского пола было ещё два гостя. {w}Парень с белыми волосами. {w}И парень с повязкой на глазу.")
    $ Fl.say(Fl_r, "Первый был так же одет в пионерскую форму. Оперевшись на статую Генды, он окинул на всех свой тяжёлый взгляд.")
    $ Fl.say(Fl_r, "Второй носил длинную мантию. Он лениво наблюдал за ночным небом. Происходящее вокруг его мало бесспокоило.")
    $ Fl.say(Fl_liz, "Походу кто-то не торопиться.")
    $ Fl.say(Fl_qu, "Ему не помещало бы хоть немного пунктуальности.")
    $ Fl.say(Fl_tul, "Может кто-то объяснит на кой чёрт нас тут всех собрали?")
    $ Fl.say(Fl_lnt, "Ну у нашего Кукловода есть новость.")

    $ Fl.StopMusic(4)
    $ Fl.PlaySound("Fl_shagi", 1.0, 0, False)

    $ Fl.say(Fl_r, "Вдали раздались медленные шаги.")
    $ Fl.say(Fl_r, "Пара светящих глаз приближались в сторону площади. Тем самым прервав все разговоры гостей.")

    $ Fl.PlayMusic("Fl_demo_amb", 1, 6)
    $ Fl.say(Fl_r, "В центре площади остановился парень лет 20-25 с растрёпанными волосами. Его глаза подобно уличным фонарям светились ярким жёлтым пламенем.")
    $ Fl.say(Fl_setk, "Отлично все в сборе.")
    $ Fl.say(Fl_liz, "Явился не запылился! Знаешь, мог бы и раньше прийти. И где твои куклы, жалкие пионеришки?")
    $ Fl.say(Fl_setk, "Сегодня их присутствие ни к чему.")
    $ Fl.say(Fl_r, "Холодно ответил парень.")
    $ Fl.say(Fl_setk, "И так думаю можно начинать наше собрание.")
    $ Fl.say(Fl_r, "В тот же миг, все уставились на него.")
    $ Fl.say(Fl_setk, "Сегодня я собрал всех вас, потому что у меня есть важное объявление.")
    $ Fl.say(Fl_setk, "В лагере объявился новый сказитель под кодовым номером Q_66.")
    $ Fl.say(Fl_liz, "О, так у нас новенький? А что у него за способность, а прозвище уже есть?")
    $ Fl.say(Fl_tul, "Почему ты его тогда не позвал на это дурацкое собрание?")
    $ Fl.say(Fl_r, "Атмосфера была накалённая. Всем присуствующим явно не понравилось что их собрали в одном месте против их воли.")
    $ Fl.say(Fl_setk, "Потому что он не один из нас.")
    $ Fl.say(Fl_setk, "Q_66 хочет убить каждого из нас.")
    $ Fl.say(Fl_qu, "Как дерзко.")
    $ Fl.say(Fl_tul, "Хах, правда что-ли? Да кем он себя возомнил? Хочет убить всех нас, пускай только попробует!")
    $ Fl.say(Fl_liz, "Забавненько!")
    $ Fl.say(Fl_r, "Каждый начал комментировать данные слова, только девушка с фиолетовыми хвостиками и парень с повязкой на глазу молчали в сторонке.")
    $ Fl.say(Fl_setk, "Поэтому раз он объявил охоту на нас. Я объявляю охоту на него.")
    $ Fl.say(Fl_qu, "Я правильно понимаю, ты хочешь чтобы мы убили его?")
    $ Fl.say(Fl_setk, "Да, я хочу чтобы вы избавились от него.")
    $ Fl.say(Fl_liz, "Стоп, а с чего это вдруг ты тут раскомандывался? Почему это ты нам указываешь что нам делать?")
    $ Fl.say(Fl_r, "Парень поднял голову вверх. Глядя на всех окружающих тяжёлым взглядом, он усмехнулся.")
    $ Fl.say(Fl_setk, "Потому что в сравнении со мной вы мелкие сошки.")
    $ Fl.say(Fl_setk, "Во-вторых благодаря мне многие из вас приобрели способности.")
    $ Fl.say(Fl_setk, "А в-третьих вы все мои куклы. Для вас свобода - неболее чем мираж.")
    $ Fl.say(Fl_setk, "В любой момент, я могу вас уничтожить.")
    $ Fl.say(Fl_r, "На площади воцарила мёртвая тишина. Никто не осмелился возразить Кукловоду.")
    $ Fl.say(Fl_setk, "А теперь, господа, предлагаю разойтись. На этом наше собрание закончено.")
    $ Fl.StopMusic(5)
    $ Fl.HideScreens(_with=Fl_dissolve2)
    scene bg Fl_black with Fl_dissolve3


    $ Fl.DayTime("night", "night")


    $ Fl.Pause(9.5)


    scene bg Fl_ext_polyana_night
    show Fl_dust_full
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.PlayMusic("Fl_story_of_the_whole_thing", 1, 6)
    $ Fl.say(Fl_r, "Шёл очередной цикл в пионерлагере.")
    $ Fl.say(Fl_r, "Мне понадобилось немного циклов чтобы освоить способности чудо прибора на моей шее.")
    $ Fl.say(Fl_r, "Как оказалось он и правда увеличивал мои физические способности. И если научится их контролировать, то даже скорость Тихони не сравнится с моей.")
    $ Fl.say(Fl_r, "По-мимо необычной силы прибора, я кое-что обнаружил новое!")
    $ Fl.say(Fl_r, "После того, как я использовал в бою свой ошейник, в каждом цикле в бункере я находил небольшой блок питания.")
    $ Fl.say(Fl_r, "Как оказалось, этот блок питания своего рода аккамулятор для моего устройства на шее.")
    $ Fl.say(Fl_r, "Мне пришлось немного повозиться, чтобы понять как снять старый и заменить на новый.")
    $ Fl.say(Fl_r, "Теория о том что это аппарат жизнедеятельности никуда не пропала. {w}Стоило мне снять аккамулятор с шеи, как тут же мои руки начинали трястись и ноги подкашивались. Всё тело казалось мне не подъёмным.")
    $ Fl.say(Fl_th, "Чёртов доктор, мог бы для начала объяснить как пользоваться этим устройством, а не делать из меня машину для убийств.")
    $ Fl.say(Fl_r, "Чтобы полностью приспособиться к моей силе мне пришлось многое пережить. {w}Я падал на смерть, {w}ломал кости об ближайщие строения, {w}в месиво разбивал кулаки.")
    
    $ Fl.Pause(2.0)
    $ Fl.say(Fl_r, "Что насчёт Тихони?")
    $ Fl.say(Fl_r, "С недавних пор её визиты зачастились.")
    $ Fl.say(Fl_r, "Каждый раз лагерь терпел изменения. То дождь хлынет, то туман всё окутает в свои объятия.")
    $ Fl.say(Fl_r, "Я не знаю сколько клонов мне пришлось убить за всё время. Я уже давно сбился со счёта. {w}Они теперь для меня не представляют никакой угрозы.")
    $ Fl.say(Fl_pi, "Эх, много чего произошло, в меня стреляли и{mn} я упал в лужу...")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_r, "Отложив лопату в сторону, я посмотрел на бездыханное тело Тихони.")
    $ Fl.say(Fl_pi, "Чего же ты добиваешься на самом деле?..")
    $ Fl.say(Fl_r, "Я скинул очередного клона в яму, которую вырыл только что.")
    $ Fl.say(Fl_r, "Присыпав сверху землёй и откинув лопату в кусты, я с чувством выполненного долга отправился в музклуб.")
    $ Fl.StopMusic(5)
    $ Fl.say(Fl_th, "Завтра меня ждёт очередной новый цикл.")
    $ Fl.HideScreens(_with=Fl_dissolve2)
    scene bg Fl_black with Fl_dissolve3



    $ Fl.DayTime("sunset", "sunset")


    $ Fl.Pause(7.5)


    scene bg Fl_int_musclub_sunset with Fl_dissolve3
    $ Fl.PlayMusic("Fl_pacefic", 1, 5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Почти 6 часов утра, очередное начало бесчисленного рассвета.")
    $ Fl.say(Fl_r, "Лагерь ещё спал, пока мои пальцы перебирали струны акустической гитары в попытках сыграть правильно композицию.")
    $ Fl.say(Fl_th, "Интересно, в этом цикле Тихоня снова появится?")
    $ Fl.say(Fl_r, "Я задумался.")
    $ Fl.say(Fl_th, "А как хорошо я знаю Лену?")
    $ Fl.say(Fl_th, "Всё что мне известно - Лена была обычным пионером, как и я. {w}Она из второго отряда, в начале смены вступила в Клуб рисования и поэзии.")
    $ Fl.say(Fl_th, "Она была куклой, как и все здешние пионеры. Тогда каким образом она смогла выбраться из оков лагеря?")
    $ Fl.say(Fl_th, "И много ли таких кукол, которые помнят?")
    $ Fl.say(Fl_pi, "А ведь я Мику тоже воспринимал, как куклу...")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_r, "Если говорить уже о нынешней Лене - Тихоне, то за время истребления клонов, я лучше анализировал её способность.")
    $ Fl.say(Fl_r, "1:Один цикл - один клон. {w}2:Клон не чувствует боли. {w}3:Клона можно убить только уничтожив мозг или сердце. {w}4:Клон обладает отличной ловкостью, его движения слишком быстрые.")
    $ Fl.say(Fl_th, "Но этих данных всё равно мало!")
    $ Fl.say(Fl_th, "Почему клон Тихони может телепортироваться, как она постоянно находит меня в каждом цикле?")
    $ Fl.say(Fl_th, "Телепортацией обладает не только Лена, но другие сказители. Каким-то образом они способные перемещаться между лагерями...")


    $ Fl.PlaySound("Fl_dinner_horn_processed", 1, 0, False)
    $ Fl.StopMusic(3)
            
    $ Fl.Pause(2.0)
    $ Fl.say(Fl_r, "Неожиданно из динамиков по всему лагерю разнёсся горн.")
    $ Fl.say(Fl_r, "Маленькая стрелка настенных часов показывала 10 минут седьмого утра.")
    $ Fl.say(Fl_pi, "Что-то тут не так, горн должен прозвучать только через два часа, не раньше!")
    $ Fl.say(Fl_r, "Отложив гитару подальше, я вышел наружу.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2



    $ Fl.DayTime("day", "day")


    $ Fl.Pause(4.5)
    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 4)
    scene bg Fl_ext_houses2_day:
        Fl_walking3
    show Fl_light_c 
    with Fl_effect_2 
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Чем ближе я подходил к центру лагеря, тем больше пионеров на своём пути я встречал.")
    $ Fl.say(Fl_r, "С каждым шагом, из домиков всё больше вываливалось заспанных лиц.")
    $ Fl.say(Fl_r, "Я медленно плёлся за потоком.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(2.5)
    scene bg Fl_ext_square_day
    show Fl_light_c 
    with Fl_effect_2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "В конце концов я оказался на площади.")
    $ Fl.say(Fl_r, "Оглядев всех вокруг, картина перед глазами оставляла желать лучшего. {w}Все пионеры переглядывались друг на друга и шушукались о своём, пока вожатые отрядов с обеспокоиными лицами что-то обсуждали между собой.")
    $ Fl.say(Fl_th, "Отклонение в цикле? {w}Снова Тихоня явилась?")
    $ Fl.say(Fl_r, "Изменения сценария меня уже не удивляли, а наоборот стали своего рода сигналом перед боем с Леной.")
    $ Fl.say(Fl_r, "Закончив своё совещание, вожатые попросили свои отряды построиться.")
    $ Fl.say(Fl_r, "Я же предпочёл занять место на близстоящей скамейке. В такой суматохе даже парень в чёрной толстовке не шибко выделяется среди толпы.")
    $ Fl.say(Fl_r, "Началась перекличка. {w}Из нашего отряда отсуствовало 4 человека: {w}Я, Аня, Алиса, Катя.")
    $ Fl.say(Fl_th, "Помощница вожатой не явилась на линейку? Странно{mn} Эта активистка не из тех, кто может ослушаться приказу старших.")
    $ Fl.say(Fl_th, "А то что рыжих подружек нет в наличие - ничего удивительного, для них прогулять линейку по расписанию раз плюнуть, не говоря уже про незапланированную в такую рань.")
    $ Fl.say(Fl_r, "Вожатая ещё раз провела перекличку, но никто из отсуствующих так и не появился.")
    $ Fl.say(Fl_mvv, "...Ладно, придёться начать без них...")
    $ Fl.say(Fl_mvv, "И так, отряд, внимание! Просьба сделать максимальную тишину!")
    $ Fl.say(Fl_mvv, "С сегодняшнего дня по лагерю никто один не гуляет. {w}Уходить в лес и за территорию ворот тоже запрещено! {w}После отбоя чтобы никто не выходил на улицу, иначе сразу домой отправим. Если вдруг приспичит в туалет ночью, то ходим парами.")
    $ Fl.say(Fl_mvv, "Дверь и окна на ночь обязательно закрываем! {w}А главное после того как прозвенит горн все встречаемся у столовой, будет каждый раз перекличка, никто в столовую раньше вермени не зайдёт и не выйдет.")
    $ Fl.say(Fl_r, "Развалившись на скамейке, я внимательно слушал речь вожатой и с каждой минутой атмосфера накалялась.")
    $ Fl.say(Fl_r, "Все эти ограничения не могли появится из воздуха. Какой-то мотив побудил вожатых отречь пионеров от полной свободы в стенах пионерлагеря.")
    $ Fl.say(Fl_r, "На вопросы по типу: «А что случилось?», «Почему так внезапно?» и т.д. Вожатые просто игнорировали.")
    $ Fl.say(Fl_r, "Неожиданно из толпы кто-то заорал.")
    $ Fl.say(Fl_ktv, "Пожар! Пожар!", _with=hpunch)
    $ Fl.say(Fl_r, "Худощавый парнишка указывал в сторону где в воздух поднимался чёрный, как смоль, клуб дыма.")
    $ Fl.say(Fl_r, "На площади началась паника. Вожатые тоже закопошились.")
    $ Fl.say(Fl_r, "Я ещё раз внимательно присмотрелся к источнику дымовой завесы и ужаснулся.")
    $ Fl.StopAmbience(2)

    $ Fl.PlayMusic("Fl_inquiry", 1, 3)
    $ Fl.say(Fl_pi, "Твою мать! В той же стороне находится музклуб!", _with=hpunch)
    $ Fl.say(Fl_r, "Быстро нашупав кнопку питания на шее, я пулей рванул к музкружку.")
    $ Fl.HideScreens(_with=Fl_fast)


    scene bg Fl_ext_houses_day with Fl_dspr
    scene bg Fl_ext_musclub_fire
    show Fl_light_c  
    with Fl_dspr
    $ Fl.Pause(2.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Прямо на моих глазах горел весь мой мир, пламя быстрыми движениями охватывало мою вселенную как снаружи, так и внутри. Каждый сантиметр покрывался сажей.")
    $ Fl.say(Fl_r, "Мне приходилось смотреть на всё это через марево пламени.")
    $ Fl.say(Fl_r, "Я сделал глубокий вдох и побежал навстречу моим грёзам. Грёзам, сохраняющие мой покой и рассудок, стимул жить...")

    scene bg Fl_black with Fl_flash

    $ Fl.say(Fl_r, "Попав внутрь музкружка, я пытался найти самое дорогое что у меня осталось.")

    $ Fl.Pause(3.0)
    $ Fl.say(Fl_pi, "Нашёл! Я НАШЁЛ!", _with=hpunch)
    $ Fl.say(Fl_r, "Знатно надышавшись углекислым газом, я уже направился к выходу, не так уверенно, как минуту тому назад.")
    $ Fl.StopMusic(4)
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause(5.5)
    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 4)
    scene bg Fl_ext_square_day
    show Fl_light_c 
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Я сидел на скамейке и рассматривал тетрадь с композициями аквамариновой пионерки. {w}Пожар частично успел подпалить уголки листов, но я вовремя успел его потушить.")
    
    $ Fl.Pause(2.0)
    $ Fl.say(Fl_r, "На площади не было ни души, часть пионеров сейчас пытались потушить пожар, часть вожатых побежали в администрацию, а что насчёт остальных - без понятия, у меня сейчас свои мысли в голове.")
    $ Fl.say(Fl_th, "Всё сгорело{mn} Остался только тлен и руины...")
    $ Fl.say(Fl_r, "Я схватился за голову.")

    $ Fl.PlayMusic("Fl_cheel", 1, 5)
    $ Fl.say(Fl_th, "Тот кто решил поджечь музклуб, точно знал что я в нём живу! Не трудно было догадаться кто это мог сделать...")
    $ Fl.say(Fl_th, "Хотя не стоит так быстро делать какие-то выводы. {w}Возможно в лагере объявился новый сказитель...")
    $ Fl.say(Fl_th, "Потому что Тихоня предпочитает именно поединок и тихие способы убийств не её конёк.")
    $ Fl.say(Fl_th, "Тогда каковы были его мотивы. {w}Убить меня, в надежде что я внутри? {w}Или же объявить о своём присутствие?")
    $ Fl.say(Fl_r, "Я ещё раз посмотрел на потрёпанную тетрадь и убрал её в карман толстовки.")
    $ Fl.say(Fl_pi, "Что это?")
    $ Fl.say(Fl_r, "В кармане толстовки оказался кусок бумаги.")
    $ Fl.say(Fl_pi, "Записка.")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_th, "Привет, Q-66! Не против поиграть в детектива? Надеюсь что нет... {w}Дело: У тебя есть три подозреваемых, но только один из них виновен! Твоя цель найти кто именно. У тебя есть на это ровно сутки. P.S. Шанса на ошибку нет)")
    $ Fl.say(Fl_pi, "Три подозреваемых?")
    $ Fl.say(Fl_r, "Я вспомнил линейку.")


    scene bg Fl_ext_square_day
    $ Fl.DayTime("prologue", "prologue")
    show Fl_light_c 
    show Fl_prolog_dream
    with Fl_flash
    $ Fl.say(Fl_r, "Началась перекличка. Из нашего отряда отсуствовало 4 человека: {u}Я, Аня, Алиса, Катя.{/u}")


    scene bg Fl_ext_square_day
    $ Fl.DayTime("day", "day")
    show Fl_light_c 
    with Fl_flash
    $ Fl.say(Fl_th, "Аня, Алиса, Катя - сомневаюсь чтобы хоть одна из них смогла бы поджечь музкружок. {w}Но других подозреваемых нет.")
    $ Fl.say(Fl_th, "А если даже и смогли, то с какой целью куклам потребовалось поджигать лагерь?")
    $ Fl.say(Fl_th, "Стоп! А что если одна из них...")
    $ Fl.say(Fl_pi, "Не кукла!")
    $ Fl.say(Fl_th, "Мику ведь тоже оказалась живой, настоящей.")
    $ Fl.say(Fl_th, "Если это так, то думаю живой вполне может оказаться Аня. В одном из циклов она вела себя не как обычно и выражала эмоции, более человечно что-ли...")
    $ Fl.say(Fl_th, "Но если это так, то Аня - сказитель? {w}Ведь автор записки точно одна из девушек круга подозреваемых.")

    $ Fl.PlaySound("Fl_dinner_horn_processed", 1, 0, False)
    $ Fl.StopMusic(3)
            
    $ Fl.Pause(2.0)
    $ Fl.say(Fl_r, "Из динамиков разнёся горн, который уже звал пионеров на трапезу.")
    $ Fl.say(Fl_th, "Отлично там и отыщем наших прогульщиц.")
    $ Fl.StopAmbience(3)
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(5.0)
    $ Fl.PlayAmbience("Fl_dining_hall_full", 1, 4)
    scene bg Fl_int_dining_hall_people_day with Fl_effect_2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Как говорила вожатая с утра, перед едой нас ждала перекличка. {w}Но трёх нужных мне девиц не наблюдалось.")
    $ Fl.say(Fl_th, "Хотя логично, что если их не было на линейки, то они не знают про новое правило приёма пищи.")
    $ Fl.say(Fl_r, "Вожатая очень сильно нас задержала и уже многие пионеры поели, но остались на своих местах. Ещё одно правило гласило, что уходить из столовой раньше времени тоже нельзя.")
    $ Fl.say(Fl_r, "В нашем отряде началась забастовка, все были возмущенны, почему они должны голодать из-за некоторых. Вожатой ничего другого не оставалось как отпустить пионеров к раздаче, против голодных кукол она была бессильна.")
    $ Fl.say(Fl_r, "Подождав когда толкучка на раздаче прекратится, я взял свою порцию и отправился за столик где сидело больше всего человек.")
    $ Fl.say(Fl_r, "Я медленно ел и слушал разговоры окружающих, было интересно как события в лагере повлияли на кукол и изменится ли их поведение, диалоги и прочее.")

    $ Fl.Pause(3.0)
    $ Fl.say(Fl_r, "Но за пару минут подслушивания и{mn2} ничего!")
    $ Fl.say(Fl_th, "Эти безмозглые декорации на что-то хоть способны, кроме то как просто ходить, жрать и спать?!")
    $ Fl.say(Fl_r, "Я долго возмущался и моё желание вырезать бездушных тварей сидящих за столиками росло с каждой секундой.")
    $ Fl.say(Fl_r, "Но неожиданно моим ушам удалось зацепить один интересный диалог двух пионерок сзади.")

    show Fl_vignette with Fl_dissolve1
    $ Fl.PlayMusic("Fl_powerless", 1, 5)
    $ Fl.say(Fl_mirk, "Ты слышала, говорят в лесу сегодня ночью труп девушки нашли?")
    $ Fl.say(Fl_mip, "Правда?!")
    $ Fl.say(Fl_mirk, "Ага!")
    $ Fl.say(Fl_mip, "А где нашли его?")
    $ Fl.say(Fl_mirk, "Возле ворот лагеря. Вроде какая-то пионерка с зелёными волосами нашла тело. Не помню из какого отряда.")
    $ Fl.say(Fl_mip, "Жесть... А из какого отряда была девушка, чей труп обнаружили?")
    $ Fl.say(Fl_mirk, "Дай вспомнить{mn} Точно! Пионерка с фиолетовыми хвостиками из второго отряда.")
    $ Fl.say(Fl_r, "От услышанного я чуть не подавился.")
    $ Fl.say(Fl_th, "ЧТО?! Пионерка с фиолетовыми волосами хвостиками?! Тихоня?!", _with=vpunch)
    $ Fl.say(Fl_r, "Только сейчас я осознал всю серьёзность ситуации.")
    $ Fl.say(Fl_th, "По мою душу пришёл новый сказитель. И довольно сильный сказитель, раз он так легко рассправился с клоном Лены. {w}Ещё он поджёг здание музкружка в попытках убить меня или привлечь моё внимание. {w}А самое главное сказитель один из трёх пионерок с которыми мне приходиться проживать рядом каждый цикл.")
    $ Fl.say(Fl_r, "Я отложил вилку и попытался переварить всё что происходит в далеко необычном цикле.")
    hide Fl_vignette with Fl_dissolve1

    $ Fl.say(Fl_r, "Но стоило мне только погрузиться в себя, как на пороге нарисовалась пионерка с голубыми волосами. {w}Катя.")
    $ Fl.say(Fl_th, "А вот и первый подозреваемый.")
    $ Fl.say(Fl_r, "Вожатая тут же перехватила её прямо у входа. {w}По мимике вожатой можно сразу догадаться, что та отчитывала помощницу за отсутствие на линейке.")
    $ Fl.say(Fl_r, "Пионерка виновато опустила голову и молча соглашалась со всем что было выдвинуто против её.")
    $ Fl.say(Fl_r, "Утихомирив свой пыл, вожатая отпустила Катю. Пионерка вяло с грустной миной на лице пошла к раздаче.")
    $ Fl.say(Fl_r, "Стоило ей присесть за дальний столик, как я медленной и уверенной походкой отправился прямо к ней.")
    $ Fl.StopMusic(3)
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.Pause(3.0)


    $ Fl.PlayAmbience("Fl_dining_hall_full", 1, 4)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_pi, "Я подсяду?")

    show kt sad pioner1 with Fl_dissolve1

    $ Fl.say(Fl_r, "Без какого-либо энтузиазма девушка молча кивнула.")
    $ Fl.say(Fl_r, "Меня мало волновало её эмоциальное состояние, мне нужны были только, интересующие меня, ответы. Поэтому я сразу же начал.")
    $ Fl.say(Fl_pi, "Тебя на линейке не было. Как-то это несвойственно для помощницы вожатой.")
    $ Fl.say(Fl_r, "Пионерка тяжело вздохнула.")
    $ Fl.say(Fl_ka, "И ты туда же... {w}Решил меня тоже отчитать?")
    $ Fl.say(Fl_ka, "Я проспала{mn}")
    $ Fl.say(Fl_r, "Недожидаясь моего ответа, продолжила пионерка.")
    $ Fl.say(Fl_ka, "У меня будильник сломался.")

    show kt sad1 pioner1 with Fl_dissolve1

    $ Fl.say(Fl_ka, "И как я могла не услышать горн{mn}")
    $ Fl.say(Fl_r, "Катя окончательно повесила нос. Казалось, что она вот вот заплачет.")
    $ Fl.say(Fl_pi, "Ты слышала про новые правила?")
    $ Fl.say(Fl_ka, "Да. {w}Марина Владимировна сказала, что у нас в лесу появились дикие звери и пока не решат что с ними делать, лучше всем придерживаться новым правилам.")
    $ Fl.say(Fl_th, "Дикие звери. {w}Хах. А можно ли считать сказителей за диких зверей?")
    $ Fl.say(Fl_r, "Я пытался зацепиться хоть за что-то в словах пионерки, чтобы собрать нужную информацию для анализа дальнейщего приговора.")
    $ Fl.say(Fl_r, "Катя была сегодня сама не своя. Её внешний вид был какой-то другой, неухоженный что ли.")
    $ Fl.say(Fl_ka, "Марина Владимировна сказала, что тебя тоже не было на линейке. Можешь скажешь почему?")
    $ Fl.say(Fl_pi, "А я разве обязан посейщать её?")
    $ Fl.say(Fl_pi, "Я не участвую в жизни лагеря. Да и не являюсь помощницей вожатой чтобы посещать такие нудные мероприятия.")

    show kt normal pioner1 with Fl_dissolve1

    $ Fl.say(Fl_r, "Лицо Кати на мгновение изменилось, приняв осуждающий вид.")

    show kt smile pioner1 with Fl_dissolve1

    $ Fl.say(Fl_ka, "В этом весь ты, одиночка нашего лагеря.")

    hide kt smile pioner1 with Fl_dissolve1

    $ Fl.say(Fl_r, "Я решил было закончить на этом допрос, но в конце выкинул следующее:")
    $ Fl.say(Fl_pi, "Говорят у ворот сегодня нашли труп девушки. {w}Вроде бы он принадлежал Тихоне, Лене из второго отряда.")
    $ Fl.say(Fl_r, "Катю аж передёрнуло.")
    $ Fl.say(Fl_ka, "Кто тебе такое рассказал?!")
    $ Fl.say(Fl_pi, "Да так, пионерские сплетни за трапезой.")
    $ Fl.say(Fl_ka, "Я обязательно спрошу об этом у вожатой!")
    $ Fl.say(Fl_r, "Пионерка ещё что-то хотела у меня спросить, но я уже стоял у выхода. {w}Дело голубоволосой пионерки было закрыто. Теперь стоило взять показание у других подозреваемых.")
    $ Fl.say(Fl_r, "Я не нуждался в разрешение вожатой, поэтому нарушив одно из правил я покинул столовую раньше времени.")
    $ Fl.StopAmbience(3)
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(4.5)
    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 4)
    scene bg Fl_ext_house_of_dv_day
    show Fl_light_c 
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Второй подозреваемый не заставил себя долго ждать.")
    $ Fl.say(Fl_r, "Красноволосая садистка капошилась с замком собственного домика.")
    $ Fl.say(Fl_th, "Третья подозреваемая вроде бы Алиса. {w}А мне сегодня везёт.")
    $ Fl.say(Fl_r, "Когда-то я рассказывал про дуэт рыжих. И так вышло что живут они в одном домике. Если я нашёл Аню, значит где-то недалеко бродит Алиса.")
    $ Fl.say(Fl_r, "Пока я пытался найти в полезрения вторую рыжую бестию, Аня уже разобралась с замком.")
    $ Fl.say(Fl_pi, "Почему правила нарушаем?")

    show an serious pioner2 with Fl_dissolve1

    $ Fl.say(Fl_r, "Пионерка недовольно глянула на меня. Но после изучения меня с ног до головы, она улыбнулась.")

    show an smile pioner1 with Fl_dissolve1

    $ Fl.say(Fl_an, "А это ты новенький. Я думала Маринка решила меня отчитать.")
    $ Fl.say(Fl_r, "Стоило пионерке сменить позу, как сразу же мои глаза выхватили её забинтованную руку.")
    $ Fl.say(Fl_pi, "Где пораниться успела?")
    $ Fl.say(Fl_r, "Спросил я, демонстрационно указав глазами, на что упал мой взгляд.")
    $ Fl.say(Fl_an, "Какой любознательный.")
    $ Fl.say(Fl_pi, "Тогда позволь задать тебе другой вопрос, где ты была рано утром?")
    $ Fl.say(Fl_an, "Тогда позволь повторить, ты слишком любознательный.")
    $ Fl.say(Fl_r, "Пионерка демонстрировала свою доминирующую сторону садизма, хотела выбесить своего собеседника. {w}Но на лице у меня не проскользнуло никакой эмоции, я продолжал с каменным лицом задавать вопросы.")
    $ Fl.say(Fl_pi, "Скажу прямо, кто-то поджог музклуб. И этот кто-то, тот кого не было на линейке.")

    show an smile pioner2 with Fl_dissolve1

    $ Fl.say(Fl_an, "И ты решил в детектива поиграть?")
    $ Fl.say(Fl_pi, "Я всю жизнь играю в детектива, мне не привыкать.")
    $ Fl.say(Fl_pi, "Так что может объяснишь, почему у тебя на руке ожоги?")
    $ Fl.say(Fl_an, "С чего ты так решил, может я просто поранилась?")
    $ Fl.say(Fl_pi, "У тебя вся рука в бинтах. Да и если бы ты просто поранилась, то не стала бы сама наносить повязку на руку, а обратилась лучше в медпункт.")

    show an serious pioner1 with Fl_dissolve1

    $ Fl.say(Fl_an, "Если ты такой умник и всё знаешь, зачем тогда этот допрос устраиваешь?")
    $ Fl.say(Fl_an, "Я просто обожглась! Когда... {w}Заваривала себе чай!")
    $ Fl.say(Fl_r, "Я решил не докапываться больше до руки пионерки.")
    $ Fl.say(Fl_pi, "Ты не знаешь, где сейчас находится Алиса?")
    $ Fl.say(Fl_an, "Не знаю, наверное к умывальникам пошла. {w}А что решил и ей допрос устроить?")
    $ Fl.say(Fl_r, "Я ухмельнулся.")
    $ Fl.say(Fl_pi, "Да так волнуюсь чтобы твою подружку дикие звери не сожрали.")

    show an angry pioner2 with Fl_dissolve1

    $ Fl.say(Fl_an, "Какие ещё дикие звери?! {w}Совсем больной?!", _with=vpunch)
    $ Fl.say(Fl_pi, "Мне откуда знать. Вожатая на линейке сделала новые правила безопасности, потому что у нас завелись дикие звери на территории лагеря.")

    hide an angry pioner2 with Fl_dissolve1

    $ Fl.say(Fl_r, "Я развернулся. {w}Пионерка поступила точно так же. Повозмущалась, а после рванула в сторону умывальников.")
    $ Fl.say(Fl_th, "Может стоит пойти за ней?")
    $ Fl.say(Fl_th, "Хотя нет. Так будет не интересно. Да и если она виновна или её подруга, то Аня точно обведёт меня вокруг пальца.")
    $ Fl.say(Fl_r, "У меня был план, как быстро найти пионерку.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(4.5)
    scene bg Fl_ext_admin_day
    show Fl_light_c 
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Сидя на крыше административного корпуса лагеря, я высматривал вторую рыжую подозреваемую.")
    $ Fl.say(Fl_r, "Отчасти весь лагерь был, как на ладони, что упрощало мои поиски.")
    $ Fl.say(Fl_r, "После множества циклов с тренировками, с помощью моего устройства забраться на крышу не вызывало никаких проблем. {w}Но покорить прыжком крышу заброшенного корпуса я до сих пор не смог.")
    
    $ Fl.Pause(2.5)
    
    $ Fl.say(Fl_r, "Время шло{mn}")
    $ Fl.say(Fl_pi, "Да где же ты прячешься...")
    $ Fl.say(Fl_th, "Если рассуждать здраво, то ни один пионер после новостей не стал бы гулять в лесу. {w}Но в лагере её нигде нет.")
    $ Fl.say(Fl_th, "Тогда тут одно из двух. {w}Или она в столовой или же прячется в одном из домиков.")
    $ Fl.say(Fl_r, "Проходящие мимо пионеры бросали на меня удивлённый взгляд. Я был открыт - мог кто-то из вожатых поднять шумиху.")
    $ Fl.say(Fl_r, "Но в данный момент меня это мало беспокоило, да и я всегда готов кому угодно закрыть рот. {w}Раз и навсегда.")
    $ Fl.say(Fl_r, "Мой взгляд зациклился на обломках музклуба.")
    $ Fl.say(Fl_th, "А если так посудить. То почему никто не заикнулся про пожар сегодня утром, прямо во время линейки?")
    $ Fl.say(Fl_th, "Вожатые придумали отмазку про диких животных. {w}Ладно труп девушки этим можно объяснить, но пожар?")
    $ Fl.say(Fl_th, "Волки спичками баловались?!")
    $ Fl.say(Fl_r, "Данные размышления завели меня в бреш вопросов без ясного ответа. В голове крутилось множество догадок, но они не поддавались логике. Да и нужна ли логика в этом мире?")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(3.0)
    scene bg Fl_ext_admin_day
    show Fl_light_c 
    with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "И вот моё ожидание вознаградилось. У пристани быстрой походкой целеустремлённо вышагивала моя потеряшка.")
    $ Fl.say(Fl_th, "Ну наконец-то!")

    $ Fl.PlayMusic("Fl_Interlude", 1, 6)
    $ Fl.say(Fl_r, "Но кое-что меня смутило. {w}Лодок было на одну меньше раньше...")
    $ Fl.say(Fl_th, "Что она забыла на другом берегу?!")
    $ Fl.say(Fl_th, "Что-то тут не чисто...")
    $ Fl.HideScreens(_with=Fl_fast)


    scene bg Fl_ext_houses_day with Fl_dspr
    scene bg Fl_ext_square_day with Fl_dspr
    scene bg Fl_ext_boathouse_day
    show Fl_light_c  
    with Fl_dspr
    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Пионерка с опаской оглядывалась вокруг. Она от кого-то скрывалась, хотела остаться незмеченной.")
    $ Fl.say(Fl_pi, "Не меня случаем ищешь?")

    show al surprise pioner1 with vpunch

    $ Fl.say(Fl_r, "От неожиданности пионерка подскочила.")
    $ Fl.say(Fl_al, "Кто здесь?!")
    $ Fl.say(Fl_r, "Наши взгляды пересеклись.")

    show al normal pioner2 with Fl_dissolve1

    $ Fl.say(Fl_al, "А это ты - новенький. Зачем так людей пугаешь?")
    $ Fl.say(Fl_pi, "Да я просто гулял и заметил тебя, решил поздароваться.")

    show al smile pioner2 with Fl_dissolve1

    $ Fl.say(Fl_al, "Ну приветик, тогда.")

    hide al smile pioner2 with Fl_dissolve1

    $ Fl.say(Fl_r, "Одарила меня мягкой улыбкой пионерка и постаралась скрыться с пристани.")
    $ Fl.say(Fl_pi, "А можно задать тебе вопрос?")

    show al normal pioner2 with Fl_dissolve1

    $ Fl.say(Fl_al, "Какой?")
    $ Fl.say(Fl_pi, "Что ты делала на том берегу?")
    $ Fl.say(Fl_r, "Указав глазами в начале на лодку, потом на соседний остров, задал вопрос я.")

    show al smile pioner1 with Fl_dissolve1

    $ Fl.say(Fl_al, "Гуляла, а что?")
    $ Fl.say(Fl_pi, "А ты не слышала про новые правила лагеря?")

    show al serious pioner1 with Fl_dissolve1

    $ Fl.say(Fl_al, "Нет{mn}")
    $ Fl.say(Fl_pi, "Ах точно, их же рассказывали на линейки. Прости.")
    $ Fl.say(Fl_r, "С натянутой улыбкой сказал я, принимая виноватый вид.")
    $ Fl.say(Fl_r, "Пионерка это заметила и настрожилась ещё сильнее.")
    $ Fl.say(Fl_th, "Клюнула. Пора начать наш допрос.")
    $ Fl.say(Fl_pi, "Говорят в лагере маньяк завёлся, вчера вот труп нашли. Вот вожатые и ввели новые правила, чтобы все держались вместе и никто не пострадал, пока ведётся расследование.")
    
    show al surprise pioner1 with vpunch

    $ Fl.say(Fl_al, "Маньяк?! Как так?! О боже...", _with=vpunch)
    $ Fl.say(Fl_r, "Рыжую охватил страх. {w}Такая реакция могла легко снять её из подозреваемых, но я не останавливался...")
    $ Fl.say(Fl_pi, "Ещё с утра кто-то поджог музклуб, возможно это рук тоже того маньяка.")
    $ Fl.say(Fl_al, "Музклуб? Ты же в нём живёшь!")

    show al sad pioner2 with Fl_dissolve1

    $ Fl.say(Fl_al, "Ты как? Хоть не пострадал?")
    $ Fl.say(Fl_th, "Какая забота. Интересно играешь со мной или правда переживаешь?")
    $ Fl.say(Fl_pi, "Я в порядке. Я в тот момент на линейке был.")

    show al smile pioner2 with Fl_dissolve1

    $ Fl.say(Fl_al, "Фух. Вожатая что-то сказала насчёт пожара и где теперь ты жить будешь?")
    $ Fl.say(Fl_pi, "Нет. Но она, как и все остальные вожатые, ищет виновника.")
    $ Fl.say(Fl_pi, "И тут такое дело, из нашего отряда только тебя не было на линейке, да и вообще никто тебя не видел целый день. Уже скоро обед кстати.")
    $ Fl.say(Fl_pi, "Позволь поинтересоваться, где ты была всё это время и прошлой ночью?")
    $ Fl.say(Fl_r, "Да мне пришлось соврать немного, но мне нужно было посмотреть как она оправдается на эту ложь.")

    show al serious pioner2 with Fl_dissolve1

    $ Fl.say(Fl_r, "Лицо девушки в миг приобрело серьёзный настрой. Она одарила меня своим хмурым, недовольным взглядом и пошла в наступление.")
    $ Fl.say(Fl_al, "Ты считаешь, что во всём виновата я?")
    $ Fl.say(Fl_pi, "Возможно. {w}Скрыть труп на острове не такая уж плохая идея, а поднять в это время суматоху, чтобы протащить незаметно его до пристани, тот ещё план гения.")

    show al angry pioner2 with Fl_dissolve1

    $ Fl.say(Fl_al, "Ты больной?!", _with=hpunch)
    $ Fl.say(Fl_al, "У каждого убийцы имеется мотив! Зачем мне кого-то убивать и прятать его тело, после того, как его уже нашли?!")
    $ Fl.say(Fl_pi, "Мотив? Действительно мотива я не знаю.")
    $ Fl.say(Fl_pi, "Но может тогда скажешь где ты была ночью?")
    $ Fl.say(Fl_r, "Продолжил давить морально на пионерку я.")
    $ Fl.say(Fl_al, "А может ты в начале скажешь где ты был прошлой ночью?! Может это ты тот самый маньяк!")
    $ Fl.say(Fl_th, "Перевела стрелку, ну ладно будет тебе ответ.")
    $ Fl.say(Fl_pi, "Без проблем. Я баловался музыкальными инструментами, а после вымотался и лёг спать. {w}Теперь твоя очередь.")
    $ Fl.say(Fl_al, "А я после душа отправилась к себе и там пообщалась с Аней, а после легла спать. Доволен?")
    $ Fl.say(Fl_r, "Я решил дальше врать. Рыжая начала себя очень агрессивно вести и если она правда сказитель, то должна в любую секунду наброситься на меня.")
    $ Fl.say(Fl_pi, "А мне Аня сказала, что ты посреди ночи куда-то ушла, а с утра тебя даже не видела.")
    $ Fl.say(Fl_al, "Ты даже Аню успел допросить, горе детектив.")

    hide al angry pioner2 with Fl_dissolve1

    $ Fl.say(Fl_al, "Я не хочу продолжать этот бессмысленный диалог. Не подходи ко мне больше, псих!")
    $ Fl.StopMusic(5)
    $ Fl.say(Fl_r, "Алиса ушла, а я остался стоять в сметение.")
    $ Fl.say(Fl_pi, "И каким образом я должен найти сказителя?!")
    $ Fl.say(Fl_th, "Они ведут и отвечают как куклы. Это типичный защитный механизм, когда кукла не понимает как реагировать когда ей начинают угрожать обвинениями.")
    $ Fl.say(Fl_r, "Я подняв взгляд наверх. Но ответ с неба не упадёт, а значит нужно разбираться с этим самому. Осталось полдня для финального ответа.")
    $ Fl.say(Fl_th, "Стоит понаблюдать за их поведением до конца дня.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(4)
    scene bg Fl_black with Fl_dissolve2



    $ Fl.DayTime("night", "night")


    $ Fl.Pause(6.5)
    scene bg Fl_int_library_night2 with Fl_dissolve2
    $ Fl.PlayMusic("Fl_detroit", 1, 5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Прошло достаточно времени до того, как лагерь окружила мгла.")
    $ Fl.say(Fl_r, "Сидя в библиотеке и разглядывая книжную полку, я размышлял. {w}Скоро мне придётся сделать вердикт палача, обрушить божью кару за все грехи на одну из пионерок.")
    $ Fl.say(Fl_r, "Но я не знал{mn} {w}Я запутался, {w}я размышлял, {w}но боялся ошибиться. Боялся сделать неправильный шаг в этой игре детектива.")
    $ Fl.say(Fl_th, "А что мы имеем?")
    $ Fl.say(Fl_th, "Катя - меньше всего подозрений. Её ответы на вопросы идеальны, да и она единственная кто целый день жил в лагере обычной жизнью.")
    $ Fl.say(Fl_th, "С самого утра она была подавлена, всё валилось с рук. Она допустила ошибку, после чего к ней сразу начали относиться иначе. {w}Потерять доверие страшная штука.")
    $ Fl.say(Fl_th, "Аня - могла бы стать подозреваемой на первом месте.")
    $ Fl.say(Fl_th, "Перебинтованная рука, уклончивость от ответов, агрессивный настрой. Не говоря уже про то, что в лагере она провела весь день в здание «Клубы». Её рыжая подружка мало беспокоила. Она просто проводила время с парнями.")
    $ Fl.say(Fl_th, "Но среди трёх подозреваемых она вела себя более живой. А в данный момент это только усугубляет её положение.")
    $ Fl.say(Fl_th, "Алиса - вот главный подозреваемый!")
    $ Fl.say(Fl_th, "В допросе она постоянно пыталась перевести тему, агрессивно отвечала, а главное усердно старалась не попадать в моё полезрение.")
    $ Fl.say(Fl_r, "Я проверил соседний остров, но так ничего и не обнаружил.")
    $ Fl.say(Fl_r, "Действия Алисы слишком не логичны, а у кукол есть свой сценарий. Пионерка нарушала все правила, дарованные ей пионерлагерем.")
    $ Fl.say(Fl_r, "Я схватился за голову.")
    $ Fl.say(Fl_pi, "Почему <бл*ть> так сложно?!")
    $ Fl.say(Fl_pi, "Я уже сыт по горло загадками, накой чёрт ты мне ещё их подкидываешь?!", _with=hpunch)
    $ Fl.say(Fl_r, "Крикнул я в пустоту.")
    $ Fl.say(Fl_r, "Мои слова были адресованы сказителю, что затеял игру в Шерлока.")

    $ Fl.Pause(2.5)
    $ Fl.say(Fl_th, "А что если подозреваемых двое? Или вовсе трое?")
    $ Fl.say(Fl_r, "Меня словно осенило.")
    $ Fl.say(Fl_th, "Точно! Я ведь даже не подумал, какая способность может быть у этого сказителя.")
    $ Fl.say(Fl_th, "Что если мне нужно найти сказителя не куклу. А в кукле сказителя?")
    $ Fl.say(Fl_th, "Может среди этих пионерок вообще никто не виноват и они просто куклы. {w}В полне логично, что он может вселиться в одну из подозреваемых или принять её облик...")
    $ Fl.say(Fl_pi, "Нет, слишком просто{mn} Да и сути дела не меняет в таком случае тогда подозреваемого может не быть вовсе или все разом. Шансы на успех уменьшаются.")
    $ Fl.say(Fl_r, "Настольные часы показывали без десяти двенадцать.")
    $ Fl.say(Fl_r, "Я включил устройство на своей шее.")
    $ Fl.say(Fl_th, "Не знаю, что будет если время выйдет или я дам неправильный ответ. Так что я должен быть готов к худшему исходу.")
    $ Fl.say(Fl_pi, "Пора дать ответ...")
    $ Fl.StopMusic(3)

    $ Fl.say(Fl_r, "Мою речь прервал уже хорошо знакомый запах.")
    $ Fl.say(Fl_r, "Медленными шажками я направился к источнику.")
    $ Fl.say(Fl_r, "Сладковатый запах привёл меня прямиком к дверце погреба. {w}После чего решил заглянуть внутрь.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    scene bg Fl_int_library_cellar_day with Fl_dissolve2
    $ Fl.Pause(4.0)
    $ Fl.PlayMusic("Fl_levantation", 1, 4)
    $ Fl.say(Fl_r, "Какого?!", _with=hpunch)
    $ Fl.say(Fl_r, "На мешках с провизией лежала{mn} {w}Катя...")
    $ Fl.say(Fl_r, "Точнее сказать, её бездыханное тело. Вся рубашка была пропитана кровью. На лице был шок. Её убили очень быстро и неожиданно, вероятнее всего со спины...")
    $ Fl.say(Fl_th, "Значит всё это время она была мертва, тогда...")
    $ Fl.say(Fl_kt, "Да уж, неудобно вышло.")
    $ Fl.HideScreens(_with=Fl_fast)


    scene bg Fl_int_library_night2
    show kt normal pioner1 
    with Fl_fast


    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Я моментально повернулся к источнику.")
    $ Fl.say(Fl_r, "Передо мной стояла Катя и косилась в сторону погреба.")
    $ Fl.say(Fl_ka, "Ян, уже поздно. Ты разве забыл про новые правила в лагере?")
    $ Fl.say(Fl_pi, "Кто ты?")

    show kt sad pioner1 with Fl_dissolve1

    $ Fl.say(Fl_ka, "Ты в порядке? Ты весь побледнел.")

    hide kt sad pioner1 with Fl_dissolve1

    $ Fl.say(Fl_r, "Я ещё раз заглянул в погреб периферическим зрением.")
    $ Fl.say(Fl_th, "Что?..")
    $ Fl.say(Fl_r, "Тело пропало, а все следы крови просто испарились. В погребе лежали только мешки.")
    $ Fl.say(Fl_th, "Показалось? {w}Нет такое показаться не может, да и запах. Да и куда делось тело и почему я больше не чувствую запах трупа?")
    $ Fl.say(Fl_th, "Ответ очевиден...")

    show kt sad pioner1 with Fl_dissolve1

    $ Fl.say(Fl_r, "Мой тяжёлый взгляд пал на пионерку, которая секунду назад в моих глазах была мертвой.")
    $ Fl.say(Fl_pi, "Я ещё раз спрошу, кто ты?")
    $ Fl.say(Fl_ka, "Ян, ты меня пугаешь.")
    $ Fl.say(Fl_pi, "Ты проиграла как только я обнаружил труп. Спасибо, теперь я точно уверен в своём ответе.")

    show kt laugh pioner1 with Fl_dissolve1

    $ Fl.say(Fl_ka, "Нет, игра ещё не закончена. Я хочу послушать ход твоих мыслей.")
    $ Fl.say(Fl_r, "Сказитель быстро сдался и больше не пытался подражать Катю, он решил продолжить свою игру.")
    $ Fl.say(Fl_ka, "У тебя осталось ровно 4 минуты. Успеешь меня убедить?")
    $ Fl.say(Fl_r, "Я мог бы решить всё куда быстрее, убив её. Но я не знаю, что у неё за способность и что произойдёт когда я нарушу правила или время выйдет, поэтому я решил дать то чего хотел сказитель.")
    $ Fl.say(Fl_pi, "Ладно, играем до конца.")
    $ Fl.say(Fl_pi, "Очевидно, что самые мутные в этой всей ситуации Аня и Алиса. Они и становятся главными подозреваемыми. И тут будет работать 50 на 50.")
    $ Fl.say(Fl_pi, "Но если сравнивать двух рыжих, то Алиса вела себя куда подозрительнее, чем её подруга. Значит она выдвигается вперёд и занимает первое место.")
    $ Fl.say(Fl_pi, "Вот только подозреваемых трое. Тогда почему рассматриваем только двоих? {w}Правильно, потому что у третьего самое железное алиби!")
    $ Fl.say(Fl_pi, "Только{mn} Обычно тех кого ты не рассматриваешь и являются преступниками. Поэтому в Кате я был уверен на 20 процентов.")
    $ Fl.say(Fl_pi, "Я очень сильно зациклился на поведении других, что убрал одну подозреваемую. Я не детектив, чтобы разбираться в таких делах, да и не нужно мне это. Поэтому я решил пойти ва-банк и выбрать Катю.")

    show kt tender pioner1 with Fl_dissolve1

    $ Fl.say(Fl_ka, "Ты сейчас серьёзно? Решил выбрать того, кто был вообще не в зоне подозрения. И дать ответ в котором ты уверен на 20 процентов?!")
    $ Fl.say(Fl_pi, "Да, но благодаря тебе, проценты поднялись.")
    $ Fl.say(Fl_r, "Я усмехнулся. Было странное чувство будто всё происходящее мне нравилось и я получал невероятные ощущения. {w}Это и есть азарт? Хотя азартом это не назовёшь, ведь тебе решать умрёт виновный или простой человек...")
    
    show kt laugh pioner1 with Fl_dissolve1

    $ Fl.say(Fl_ka, "Ты и правда просто нечто!")
    $ Fl.say(Fl_ka, "Поздравляю ты побе...")
    $ Fl.say(Fl_pi, "Может покажешь свой настоящий облик?")
    $ Fl.say(Fl_ka, "О чём это ты?")
    $ Fl.say(Fl_r, "В голосе Кати слушался задор, её забавляло включать дурочку. Она широко улыбалась и хихикала.")
    $ Fl.say(Fl_pi, "Это же твоя часть способности, принимать чужой облик, так ведь?")

    show kt smile pioner1 with Fl_dissolve1

    $ Fl.say(Fl_ka, "Блин, ну так не интересно. {w}Хотя соглашусь, я устала ходить в образе этой девицы. Она такааая скучная...")

    hide kt smile pioner1 with Fl_dissolve1

    $ Fl.StopMusic(4)
    $ Fl.PlayAmbience("Fl_camp_center_night", 1, 5)

    $ Fl.say(Fl_r, "Это были последние слова сказителя в образе Кати. Теперь я увидел истинный облик своего врага.")
    $ Fl.HideScreens(_with=Fl_dissolve1)

    show liz pioner smile with Fl_dissolve2
    $ Fl.Pause(1.0)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_liz87, "Приятно познакомиться, я сказитель L-87, Импостер.")
    $ Fl.say(Fl_r, "Сказителем оказалась красноволосая девушка. Наряд у неё был слишком вызывающим. {w}Растёгнутая рубашка, демонстрировала её белый лифчик всем. Не застёгнутая юбка, тоже демонстрировала такого же цвета трусы.")
    $ Fl.say(Fl_r, "Кулон на её шее игриво заманивал посмотреть в область ниже глаз. Девушка полностью не стыдилась своего наряда, да и зачем это всё, ведь это последнее что увидит её жертва.")

    show liz pioner surprise2 with Fl_dissolve1
    $ Fl.Pause(1.0)
    show liz pioner mean with Fl_dissolve1

    $ Fl.say(Fl_r, "На лице Импостера, появилась ухмылка. Я догадывался откуда она у неё появилась...")
    $ Fl.say(Fl_liz, "Нравится?")
    $ Fl.say(Fl_liz, "Знаешь, я немного изголодалась, почему бы...")

    show liz pioner4 desire with Fl_dissolve1

    $ Fl.say(Fl_liz, "...тебе не взять награду. Я могу осуществить любые твои фантазии если пожелаешь!")
    $ Fl.say(Fl_r, "Одной рукой она обхватила грудь и медленно начала её мазать, давая чёткий зелёный свет на «совместное чтение книг».")
    $ Fl.say(Fl_th, "Достала!")

    hide liz pioner4 desire with Fl_fast

    $ Fl.AttackScreens()
    $ Fl.say(Fl_r, "Я моментально сократил дистанцию. Схватив за горло девушку, я прижал её к книжной полке.")
    $ Fl.say(Fl_liz, "Так ты любишь по-жёстче?")
    $ Fl.say(Fl_r, "Её рука упала мне на торс, плавным движением она скользила всё ниже.")
    $ Fl.say(Fl_r, "На что я только сильнее её впечатал в стену.")
    $ Fl.say(Fl_pi, "Хватит! {w}Для чего это всё? Зачем ты вообще в мой лагерь пришла?!", _with=hpunch)
    $ Fl.say(Fl_liz, "Я дам тебе... {w}Всё что пожелаешь.")
    $ Fl.say(Fl_r, "Гнев всё сильнее охватывал разум. Я не понимал что происходит и чего мне дальше ожидать. Но я хотел получить хоть какие-то ответы от этой садистки.")
    $ Fl.say(Fl_th, "Я бы мог просто убить её, но продолжаю играть у неё на поводу. {w}Как брошенный котёнок, жду помощи, ответов...")
    $ Fl.say(Fl_pi, "Ради чего ты устроила это всё? Чего ты добиваешься? Моего внимания?")
    $ Fl.say(Fl_liz, "Твоего внимания?")
    $ Fl.say(Fl_r, "Она громко рассмеялась.")
    $ Fl.say(Fl_liz, "Мне просто было скучно, вот я и решила развлечься!")
    $ Fl.say(Fl_liz, "А слухи про тебя не врут, ты и правда заботишься о куклах. Что ты вообще в них нашёл?")
    $ Fl.say(Fl_th, "Ради забавы{mn}")
    $ Fl.say(Fl_pi, "Понятно. Ты такая же как они.")
    $ Fl.say(Fl_pi, "У меня больше нет к тебе вопросов!")
    $ Fl.say(Fl_r, "Не раздумывая, я занёс удар в область живота. Я собирался поступить с ней так же, как она поступила с Катей, оставить гнить её тело в погребе.")
    $ Fl.say(Fl_r, "Одного моего удара хватило бы, чтобы пробить её тело насквозь.")
    $ Fl.say(Fl_r, "На лице девушки нарисовалась улыбка до ушей.")
    $ Fl.say(Fl_r, "Раздался звук устройства.")
    $ Fl.say(Fl_th, "Что? Оно выключилось?")
    $ Fl.say(Fl_r, "Я ещё раз посмотрел на неё. Улыбка стала ещё шире.")

    $ Fl.PlayMusic("Fl_hydrogen", 1, 4)
    $ Fl.say(Fl_r, "Стоило сократить дистанцию, как тут же перед лицом промелькнуло лезвие ножа.")
    $ Fl.say(Fl_r, "Но что-то пошло не по плану и я врезался в книжный шкаф. Не успел я осознать происходящее, как мне прилетел удар с правой ноги. Но я успел схватить ногу и увидеть все прелести под юбкой девушки.")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.AttackScreens()
    $ Fl.say(Fl_th, "Да какого хрена тут происходит?!")
    $ Fl.say(Fl_r, "Каким-то образом удар достиг меня, но нанесли мне его с левой ноги.")
    $ Fl.say(Fl_th, "Я же отчётливо видел что удар был с правой!")
    $ Fl.say(Fl_r, "Времени на размышлений не было, сказитель сделал свой ход, к моему лицу стремительно приближался нож.")
    $ Fl.say(Fl_r, "Снова увернулся неудачно, я не мог контролировать своё тело.")
    $ Fl.say(Fl_th, "Устройство же выключилось, тогда почему моё тело в том же состоянии что и с включённым?!")
    $ Fl.say(Fl_th, "А что если оно и вовсе не выключалось?..")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_r, "Но было уже поздно, девушка сидела на мне верхом и приставила нож к моей шее.")
    $ Fl.say(Fl_th, "Труп который исчез на глазах, {w}запах, {w}звук устройства, {w}удар справой.")
    $ Fl.say(Fl_th, "Теперь я всё понял. Её способность не принимать чужой облик...")
    $ Fl.Pause(1.5)
    $ Fl.StopMusic(5)

    $ Fl.say(Fl_r, "Я бы и дальше лежал, анализируя над своими ошибками, как вдруг девушка убрала нож и встала.")
    $ Fl.say(Fl_liz, "Ты слаб.")
    $ Fl.say(Fl_liz, "Как тебе вообще в голову взбрело сразиться с богом?")
    $ Fl.say(Fl_pi, "Почему ты не убила меня?")

    show liz pioner me with Fl_dissolve1

    $ Fl.say(Fl_liz, "У меня встречный вопрос к тебе?")
    $ Fl.say(Fl_th, "Почему? {w}А ведь действительно я же быстрее её и слёгкостью мог пробить ей грудную клетку. Но не стал...")
    $ Fl.say(Fl_liz, "Ты ведь уже понял в чём заключается моя сила?")
    $ Fl.say(Fl_r, "Я медленно привстал.")
    $ Fl.say(Fl_pi, "Да. {w}Ты способна искажать пространноство, заставить человека видеть то что хочешь.")
    $ Fl.say(Fl_pi, "Поэтому всё это время я не замечал труп в погребе и не чувствовал трупный запах.")

    show liz pioner surprise2 with Fl_dissolve1

    $ Fl.say(Fl_pi, "Звук устройства, я подумал что оно выключилось, но ты заставила меня так думать. А твои удары. Ты же изначально била с левой ноги, но меня заставила думать, что он был с правой.")

    show liz pioner2 acrimony with Fl_dissolve1

    $ Fl.say(Fl_liz, "Как же быстро ты всё понял!")
    $ Fl.say(Fl_liz, "Теперь то ты понимаешь, что я тебе не враг?")
    $ Fl.say(Fl_pi, "Не враг? Ты сейчас серьёзно?")
    $ Fl.say(Fl_pi, "С чего я должен верить тебе?")
    $ Fl.say(Fl_liz, "Может с того, что я могу дать тебе ответы?")

    show liz pioner4 ardor with Fl_dissolve1

    $ Fl.say(Fl_liz, "А ещё тебе без девушки не выжить, кто ещё сможет уталить твои похотливые желания?")
    $ Fl.say(Fl_r, "И снова она пыталась меня возбудить. Будь я прежним человеком, то с радостью принял её предложение, ведь любой задрот о таком может только мечтать.")
    $ Fl.say(Fl_r, "Но я уже не прежний и не человек вовсе.")
    $ Fl.say(Fl_pi, "Мне нужны ответы. А потом можешь возвращаться обратно в свой лагерь.")

    show liz pioner4 calm with Fl_dissolve1

    $ Fl.say(Fl_liz, "Вот блин...")

    show liz pioner2 discontent3 with Fl_dissolve1

    $ Fl.say(Fl_liz, "...ты импотент что ли?")
    $ Fl.say(Fl_liz, "Ладно, что именно тебя интересует?")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ v = 0
    jump task_start


label task_start:
    $ Fl.PlayMusic("Fl_demo_amb", 1, 4)
    if v < 4:
        menu:
            "Кто такой Кукловод?":
                $ Fl.ShowScreens(_with=Fl_dissolve1)
                $ Fl.say(Fl_r, "Я решил пойти с козыря. Ведь из всех сказителей он интересовал меня больше всего.")
                $ Fl.say(Fl_liz, "Кукловод, а что тебя с ним связывает?")
                $ Fl.say(Fl_pi, "У нас с ним так сказать личные проблемы.")
        
                show liz pioner smile with Fl_dissolve1

                $ Fl.say(Fl_liz, "Я погляжу мальчики у нас повздорили!")
                $ Fl.say(Fl_liz, "Про Кукловода мне мало что известно. Он у нас за главного.")
                $ Fl.say(Fl_pi, "За главного? Так значит ты работаешь с ним за одно, одна из его шаек?")
        
                show liz pioner3 discontent4 with Fl_dissolve1

                $ Fl.say(Fl_liz, "Нет конечно! Я не собираюсь слушать команды этого нарциса!")
                $ Fl.say(Fl_liz, "Тебе ведь известно, что среди сказителей он номер 1?")
                $ Fl.say(Fl_pi, "Да.")
                $ Fl.say(Fl_pi, "Неужели он и правда настолько силён?")
                $ Fl.say(Fl_r, "В голове промелькнула та ночь. {w}Его пионеры готовы были умереть лишь бы не предать Кукловода. Да и сам Кукловод обращался со своими подчинёнными как с мусором, бездушными куклами, которые можно выкинуть в любой момент за любую ошибку.")
                $ Fl.say(Fl_th, "Что же ты за монстр, что пионеры готовы умереть, лишь бы не ощутить твою кару?")
        
                show liz pioner scorn with Fl_dissolve1

                $ Fl.say(Fl_liz, "Ни кто не знает. Те кто ему переступали дорогу уже мертвы.")
                $ Fl.say(Fl_liz, "Только Тихоне известно что-то о его силе.")
                $ Fl.say(Fl_th, "Тихоня? {w}Этот персонаж до сих пор для меня загадка. Её способность обычные клоны, тогда почему она не боится номера один и даже спокойно перешла ему дорогу?")
                $ Fl.say(Fl_liz, "Кукловод правозгласил себя вторым богом этого мира. Он считает, что ему нет равных.")
                $ Fl.say(Fl_pi, "Тогда почему он не может убить Тихоню? Почему он к ней относится иначе, даже от части боится её?")
        
                show liz pioner2 discontent3 with Fl_dissolve1
        
                $ Fl.say(Fl_liz, "Потому что она бессмертна. Логично же!")
                $ Fl.say(Fl_pi, "Бессмертна?")
                $ Fl.say(Fl_r, "Слова красноволосой девушки меня насторожили.")
                $ Fl.say(Fl_liz, "Тихоня такая же, как Кукловод. О ней мало что известно. Только что её способность это клоны. А ещё если ей перейти дорогу она может найти тебя в любом лагере ещё раньше, чем начнётся твой цикл.")
                $ Fl.say(Fl_liz, "Кукловод её боится, потому что она полностью не предсказуемая и может разрушить все его планы. От Тихони можно избавиться, найдя её оригинал. Своего рода администратора всех её созданных клонов.")
                $ Fl.say(Fl_th, "Я никогда не задумывался, но действительно, я уже привык сражаться против её клонов. Но ни разу у меня не возникал вопрос, как она так быстро находит меня в новом цикле и почему её клоны всегда разные...")
                $ Fl.say(Fl_th, "Если я собираюсь избавиться от Тихони, то нужно убить оригинал. Вот только каким образом я его найду? Даже Кукловод до сих пор не смог его найти...")
                $ Fl.say(Fl_pi, "Ты сказала у Кукловода есть планы? Я видел какую-то карту с секторами. Что он ищет?")
        
                show liz pioner me with Fl_dissolve1

                $ Fl.say(Fl_liz, "Не что, а кого.")
                $ Fl.say(Fl_liz, "Он собирается уничтожить бога этого мира.")
                $ Fl.say(Fl_liz, "Его цель подчинить весь лагерь себе. Стать новым богом лагеря.")
                $ Fl.say(Fl_pi, "Стать Богом?!")
        
                show liz pioner discontent2 with Fl_dissolve1
        
                $ Fl.say(Fl_liz, "Ага. Кукловод очень сильный и думает, что с его силой он способен убить даже бога.")
                $ Fl.say(Fl_th, "Я видел на что способна Юля. Более того, она бессметрна. Её смертельные раны заживали прямо на моих глазах, а сила сравнима с моим устройством.")
                $ Fl.say(Fl_pi, "Он правда в это верит?")
                $ Fl.say(Fl_liz, "Я не знаю, я не видела силу Кукловода в действии.")
                $ Fl.HideScreens(_with=Fl_dissolve1)

                $ v += 1
                jump task_start


            "Почему ты убила Тихоню?":
                show liz pioner2 smile2 with Fl_dissolve1
        
                $ Fl.ShowScreens(_with=Fl_dissolve1)
                $ Fl.say(Fl_liz, "Потому что она могла испортить все мои планы на тебя.")
                $ Fl.say(Fl_pi, "Каким образом ты смогла одолеть Тихоню?")
                $ Fl.say(Fl_liz, "Ну она так мило дожидалась тебя у остановки и я просто не смогла сдержаться чтобы не пырнуть её прямо в сердце.")
                $ Fl.say(Fl_th, "Странно{mn} Тихоня обладает инстинктом убийцы, как и я. Она бы смогла почувствовать присуствие Импостера. Что-то тут не так либо с Тихоней, либо в словах Импостера.")
        
                show liz pioner scorn with Fl_dissolve1
        
                $ Fl.say(Fl_liz, "Да и эта стерва того заслуживает!")
                $ Fl.say(Fl_liz, "Корова с большими дойками, строит из себя няшу стесняшу. Бесит!")
                $ Fl.say(Fl_r, "Меня мало интересовали личные проблемы между девушками, поэтому я решил сменить тему.")
                $ Fl.HideScreens(_with=Fl_dissolve1)

                $ v += 1
                jump task_start


            "Кто такой доктор Парки?":
                show liz pioner surprise2 with Fl_dissolve1

                $ Fl.ShowScreens(_with=Fl_dissolve1)
                $ Fl.say(Fl_liz, "Доктор кто? Что за тупое прозвище?")
                $ Fl.say(Fl_pi, "Он сам так представился. Ты про него что-то знаешь?")
                $ Fl.say(Fl_liz, "Я без понятия кто это такой. Впервые слышу это имя...")
                $ Fl.say(Fl_th, "Интересно. {w}Доктор всё знает о сказителях, но о нём другие ничего не знают.")
                $ Fl.say(Fl_th, "Ты не так уж и прост я погляжу!")

                show liz pioner me with Fl_dissolve1
        
                $ Fl.say(Fl_liz, "Я правда не знаю о ком ты. Но могу сказать, что в этом мире есть куда больше странных персонажей.")
                $ Fl.HideScreens(_with=Fl_dissolve1)

                $ v += 1
                jump task_start


            "Что тебе известно о Боге этого мира?":
                $ Fl.ShowScreens(_with=Fl_dissolve1)
                $ Fl.say(Fl_liz, "Это я тебя должна спрашивать!")
        
                show liz pioner2 acrimony with Fl_dissolve1
        
                $ Fl.say(Fl_liz, "Ты единственный кто из сказителей встречался лично с богом этого мира.")
                $ Fl.say(Fl_th, "Единственный кто встречался с богом? {w}Неужели это правда?")
                $ Fl.say(Fl_th, "Тогда почему она решила встретиться именно со мной? Что в тот вечер она хотела мне сказать? Зачем помогла вспомнить все встречи с ней и открыла глаза на правду о моём попадании в этот лагерь?")
                $ Fl.say(Fl_r, "Невольно в моей голове засела мысль, что осталные сказители тоже мало что знают о лагере и что их знания такие же поверхностные, как у меня.")
                $ Fl.say(Fl_pi, "А ты помнишь, как оказалась в лагере?")
        
                show liz pioner smile with Fl_dissolve1
        
                $ Fl.say(Fl_liz, "Неа, да и какая разница.")
                $ Fl.HideScreens(_with=Fl_dissolve1)


                $ v += 1
                jump task_start


    else:
        menu:
            "Зачем ты мне помогаешь?":
                $ Fl.ShowScreens(_with=Fl_dissolve1)
                $ Fl.say(Fl_liz, "Ты знал, что на тебя объявлена охота?")
                $ Fl.say(Fl_pi, "Уже? Быстро однако. Это у вас такой обычай в кругу сказителей?")
                $ Fl.say(Fl_r, "На моём лице нарисовалась ухмылка.")
                $ Fl.say(Fl_liz, "Нет, такое впервые.")
                $ Fl.say(Fl_liz, "Обычно когда появляется новенький Кукловод об этом просто докладывает.")

                show liz pioner scorn with Fl_dissolve1
        
                $ Fl.say(Fl_liz, "Но в этот раз всё изменилось. Он сказал, что ты собираешься нас всех убить, и поэтому от тебя нужно избавиться.")
                $ Fl.say(Fl_r, "По библиотеке разнёся смешок, его инициатором был я.")
                $ Fl.say(Fl_pi, "Это правда. Я правда собираюсь уничтожить всех сказителей.")
        
                show liz pioner me with Fl_dissolve1
        
                $ Fl.say(Fl_liz, "Но это невозможно. Если бы я сражалась с тобой в серьёз ты бы погиб.")
                $ Fl.say(Fl_liz, "Я слышала о тебе и о том как ты бросил вызов богу и то что ты без способностей смог победить клон Тихони. Ты даже толпу пионеров смог раскидать собствеными силами.")
                $ Fl.say(Fl_liz, "Так почему теперь ты стал таким слабым?")
                $ Fl.StopMusic(5)

                $ Fl.say(Fl_pi, "О чём ты?")
                $ Fl.say(Fl_r, "Моя улыбка сошла на нет, внутри появилось какое-то странное чувство...")
                $ Fl.say(Fl_liz, "Посуди сам, ты эмоцианально не стабилен, тобой движет отчаяние глубоко внутри ты начал бояться, бояться неизвестности.")
                $ Fl.say(Fl_liz, "А ещё это устройство на твоей шее. Стоило тебе подумать что она выключилось, как ты сразу запаниковал.")
                $ Fl.say(Fl_liz, "Ты боишься умереть, больше мысль о смерти не приносит тебе азарт. Как давно ты впадал в состояние безумия или просто хлоднокровно убивал ради забавы?")
                
                $ Fl.PlayMusic("Fl_neytral_ishod", 1, 4)
                $ Fl.say(Fl_r, "Я застыл. Мой пульс участился. Мысли и воспоминания подобно карусели начали крутиться в моей голове.")
                $ Fl.say(Fl_th, "Она{mn} {w}Она права, с каждым своим промахом, я из раза в раз впадал в отчание, сдавался. Моя жизнь превратилась в сплошные поиски ответов и тренировок на куклах Тихони.")
                $ Fl.say(Fl_th, "Я выгорал каждый цикл, запирался от несправедливости и наигрывал какую-то мелодию из тетрадки что оставила мне Мику.")
                $ Fl.say(Fl_th, "Все мои битвы превратились в самоуверенное сражение с силой сказителя, я забыл о том на что способен я сам.")
                $ Fl.say(Fl_liz, "Знаешь почему я помогаю тебе на самом деле?")
                $ Fl.say(Fl_r, "Спросила она, но я не решился поднять взгляд на неё. Взгляд в котором читался мой страх и осознание реальности.")
        
                show liz pioner2 smile2 with Fl_dissolve1
        
                $ Fl.say(Fl_liz, "Потому что у тебя единственного есть цель. {w}И ты наверное единственный, кто сможет узнать правду и остановить Кукловода.")
        
                show liz pioner offense with Fl_dissolve1
        
                $ Fl.say(Fl_liz, "Но если ты не придёшь в себя. То я лично убью тебя!")
        
                hide liz pioner offense with Fl_fast

                jump task_over



label task_over:
    $ Fl.ShowScreens(_with=Fl_dissolve1)

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.AttackScreens()
    $ Fl.say(Fl_r, "Импостер со всей силы врезала мне с ноги.")
        
    show Fl_vignette with Fl_fast
    $ Fl.say(Fl_r, "Из носа пошла кровь, но я продолжил лежать и смотреть в пустоту.")
    $ Fl.say(Fl_r, "Мои мысли были жалкими, а признавать свои слабости ещё более жалко.")
    $ Fl.say(Fl_th, "Почему я не убил её? {w}Что с моим поведением? {w}Почему я вновь ощущаю себя Яном?")
    $ Fl.say(Fl_th, "Яну ни за что не одолеть сказителей. Моя человечность, страх... {w}Только став Пионером, я смог избавиться от всего, мной двигало безумие и ненависть, а сейчас я страдаю, но чем?")
    
    $ Fl.Pause (2.0)
    $ Fl.say(Fl_th, "Когда я снова начал становится человеком?")
    $ Fl.say(Fl_th, "Когда перестал убивать ради забавы? {w}Или куда раньше?")
    $ Fl.say(Fl_th, "Может смерть от руки бога породила во мне страх?")
    $ Fl.say(Fl_th, "Ведь если ты сильный и непобедимый, всегда в мире найдётся кто-то сильнее тебя. Это баланс природы, всегда существуют хищники по-крупнее...")
    $ Fl.say(Fl_r, "Я сжал нотную тетрадь.")
    $ Fl.say(Fl_th, "Я не смог её отпустить. До сих пор...")
    $ Fl.say(Fl_th, "Музклуб стал моим убежищем. Только он скрывал меня от страшного внешнего мира.")
    $ Fl.say(Fl_liz, "Долго будешь приходить в норму? А то я уже немного устала ждать.")
    $ Fl.say(Fl_th, "Да какая разница, просто убью её и вновь продолжу свой путь один. {w}Или же нет?")
    $ Fl.say(Fl_r, "Я поднял свой взгляд на красноволосую девицу.")
    $ Fl.say(Fl_r, "По-мимо кулона, за которым находилась преграда к женскому сердцу, я увидел руку.")
    $ Fl.say(Fl_r, "Девушка протягивала мне руку и ухмылялась.")
    $ Fl.say(Fl_th, "Может она сможет провести меня в ад и указать правильный путь?")
    hide Fl_vignette with Fl_fast
        
    $ Fl.say(Fl_r, "Запихнув все свои размышления куда по-дальше, я встал, проигнорировав руку помощи.")
    $ Fl.StopMusic(4)
        
    show liz pioner scorn with Fl_dissolve1
        
    $ Fl.say(Fl_pi, "Я в норме, хватит уже на меня глазеть.")
        
    show liz pioner smile with Fl_dissolve1
        
    $ Fl.say(Fl_liz, "Отлично! Тогда идём.")
    $ Fl.say(Fl_pi, "Куда?")
    $ Fl.say(Fl_r, "В моём голосе вновь появилась нота равнодушия.")
        
    show liz pioner6 seduces with Fl_dissolve1
        
    $ Fl.say(Fl_liz, "Пойдём я покажу тебе кое-что...")
    $ Fl.say(Fl_r, "Нежным голосом сказала девушка, вновь играя своим телом.")
    $ Fl.say(Fl_pi, "Идём.")
        
    show liz pioner4 calm with Fl_dissolve1
        
    $ Fl.say(Fl_liz, "Правда? {w}Ты всё же согласился на интим?")
    $ Fl.say(Fl_pi, "А в твой сценарий такой ответ не входил?")
    $ Fl.say(Fl_r, "Голос снова был безжизненным, но я смог даже улыбнуться.")
        
    show liz pioner2 discontent3 with Fl_dissolve1
        
    $ Fl.say(Fl_liz, "Ну просто, я думала ты по парням после стольких отказов, ну ты сам пони...")
    $ Fl.say(Fl_r, "Не став её слушать, я просто отправился на выход.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.PlaySound("Fl_open_door_2", 1, 0, False)
    scene bg Fl_black with Fl_dissolve1

    $ Fl.Pause (3.0)
    scene bg Fl_ext_library_night
    show Fl_dust_full
    with Fl_dissolve2


    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Ночь как всегда была прекрасной. Больше это место не казалось мне пустой оболочкой. Ведь что мне известно об этом месте? {w}Именно - ничего!")
    $ Fl.Master(Fl_bg_zoom_th(1.0, 1.35, 1.5, 0.5, 0.6, 0.5, 0.75))
    $ Fl.Pause (2.0)
    
    $ Fl.say(Fl_r, "Я присел на лавочку и закурил. День был слишком насыщенным.")
    $ Fl.say(Fl_th, "Пришло время заполнить свою пустоту едким токсином.")
        
    $ Fl.Pause (2.0)
    $ Fl.say(Fl_liz, "И долго ты будешь меня динамить?")
        
    show liz pioner3 discontent4 with Fl_dissolve1:
        zoom 0.85 yalign 0.5 xalign 0.98
        
    $ Fl.say(Fl_r, "Молча протянув пачку сигарет, девушка приняла моё предложение и села рядом.")
        
    hide liz pioner3 discontent4 with Fl_dissolve1
        
    $ Fl.say(Fl_r, "Взяв пример с меня, Импостер затянулась.")
    $ Fl.say(Fl_r, "И сразу закашляла.")
    $ Fl.say(Fl_pi, "Никогда раньше не курила?")
    $ Fl.say(Fl_r, "Вытерев слёзы, она ответила.")
    $ Fl.say(Fl_liz, "Как вы курите эту гадость?")
    $ Fl.say(Fl_r, "На что я лишь молча ухмельнулся.")
        
    $ Fl.Pause (2.5)
        
    $ Fl.say(Fl_liz, "Почему ты начал курить?")
    $ Fl.say(Fl_pi, "Почему говоришь?..")
    $ Fl.say(Fl_pi, "Знаешь, наверное ни один курильщик тебе не сможет дать на этот вопрос точный ответ.")
    $ Fl.say(Fl_liz, "Что такого есть в сигаретах, что без них прям никак нельзя?")
    $ Fl.say(Fl_pi, "Они успокаивают, дают умиротворение, а в суровой реальности его довольно сложно ощутить.")
    $ Fl.say(Fl_liz, "Сколько же глубоких мыслей, я не могу. Сказал бы просто - чтобы выглядеть круто!")
    $ Fl.say(Fl_pi, "Что за логика малолетки?")
    $ Fl.say(Fl_th, "Если так подумать, то нам всегда твердили, что никотин сокращает жизнь и даже губит людей. {w}Но так ли это на самом деле?")
    $ Fl.say(Fl_th, "Человек в любом случае умрёт рано или поздно и порой далеко не из-за вредных привычек.")
    $ Fl.say(Fl_th, "Вредные привычки - одна из миллионых причин смерти человека, но она слишком ничтожна в сравнение с другими...")
        
    $ Fl.Pause (2.0)
        
    $ Fl.say(Fl_liz, "Ты ещё долго? Я уже спать хо...")
    $ Fl.say(Fl_r, "Не закончив свою речь, девушка зазевала в подтверждение своих слов.")
    $ Fl.say(Fl_liz, "Вот зачем я выбрала помощницу вожатой, столько работы...")
    $ Fl.say(Fl_liz, "Убивать не так утомляет, как работа!")
    $ Fl.say(Fl_liz, "Так что пошли уже.")
    $ Fl.say(Fl_pi, "Куда?")
    $ Fl.say(Fl_liz, "В другой лагерь конечно!")
    $ Fl.say(Fl_liz, "Или ты собрался оставаться в этом лагере с душными правилами?")
    $ Fl.say(Fl_th, "В другой лагерь?")
    $ Fl.say(Fl_th, "Точно. Сказители же могут перемещаться меж лагерями.")
    $ Fl.say(Fl_th, "Отличная возможность увидеть эту телепортацию в действие.")
    $ Fl.say(Fl_th, "Но в начале...")
    $ Fl.say(Fl_pi, "Хорошо, но мне для начала нужно кое-куда заскочить.")
    $ Fl.say(Fl_r, "Импостер вопросительно на меня посмотрела.")
    $ Fl.say(Fl_pi, "Ты можешь меня переместить к музклубу?")
    $ Fl.say(Fl_liz, "Подожди-подожди! Во-первых прыжки между лагерями - это тебе не телепортация. Мы можем только перемещаться из одного лагеря в другой, а не появляться в любом месте где захотим.")
    $ Fl.say(Fl_liz, "А во-вторых, зачем тебе туда? Здание сгорело.")
    $ Fl.say(Fl_r, "Я вздохнул. Не знаю, что меня больше растроило, тот факт что музклуба больше нет или то что я неправильно понял способность перемещения.")
    $ Fl.say(Fl_pi, "Ладно, тогда по старинке.")
    $ Fl.Master(Fl_bg_zoom_otd(1.35, 1.0, 1.5, 0.6, 0.5, 0.75, 0.5))
        
    $ Fl.Pause (2.0)
    $ Fl.say(Fl_pi, "Ты идёшь?")
    $ Fl.say(Fl_r, "Девушка вяло встала с лавочки и покосилась на меня. Идея идти куда-то пешком ей явно не нравилась.")
    $ Fl.say(Fl_pi, "Запрыгивай.")
    $ Fl.say(Fl_liz, "Что?")
    $ Fl.say(Fl_pi, "Просто запрыгни мне на спину.")
    $ Fl.say(Fl_r, "Импостер ещё сильнее покосилась на меня, но послушно выполнила то о чём я попросил.")
    $ Fl.say(Fl_liz, "И что дальше?")
    $ Fl.say(Fl_r, "Я включил устройство.")
    $ Fl.say(Fl_pi, "Держись!")
    $ Fl.HideScreens(_with=Fl_dissolve1)
        

    scene bg Fl_ext_square_night_party2 with Fl_dspr
    scene bg Fl_ext_houses_night with Fl_dspr
    scene bg Fl_ext_path2_dark
    show Fl_dust_full
    with Fl_dspr
        
    $ Fl.Pause (1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "И вновь я оказался здесь.")
    $ Fl.say(Fl_pi, "Приехали.")
    $ Fl.say(Fl_r, "Но девушка не хотела меня отпускать, её руки слишком сильно были напряженны. Она вцепилась в меня очень сильно.")
    $ Fl.say(Fl_liz, "Что это было?!")
    $ Fl.say(Fl_pi, "Как ты могла уже понять, моё устройство усиливает физические возможности. {w}Ноги в том числе.")
    $ Fl.say(Fl_r, "Кое-как расцепив руки, Импостер слезла с меня и слегка пошатнулась.")
    $ Fl.say(Fl_liz, "Ты же вроде хотел в музклуб, тогда что мы тут делаем?")
        
    $ Fl.PlayMusic("Fl_reeducated", 1, 4)
    $ Fl.say(Fl_r, "Я обернулся.")
    $ Fl.say(Fl_r, "От здания и правда ничего не осталось, слошные руины...")
    $ Fl.say(Fl_r, "Что-то сжалось внутри. {w}Это место было пристанищем для нас двоих{mn} Теперь же от него ничего не осталось, как и от нас{mn}")
    $ Fl.say(Fl_r, "Наверное сейчас мой разум смахивал на эти обломки, перед глазами.")
    $ Fl.say(Fl_r, "Мои глаза тоже когда-то были охвачены ярким пламенем, но пламя давно потухло и остались лишь пустые зрачки, в которых можно увидеть только остатки моей человечности...")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Я сделал шаг вперёд, Импостер последовала вслед за мной.")
    $ Fl.say(Fl_th, "Тут я тебя в ту ночь похоронил...")
    $ Fl.say(Fl_th, "Пришло время отпустить тебя. {w}Надеюсь сейчас ты счастлива и в безопасности.")
    $ Fl.say(Fl_th, "Этот мир был для тебя слишком жесток{mn}")
    $ Fl.say(Fl_r, "Достав тетрадь и зажигалку, я поджёг то что сохраняло мой рассудок, {w}то что не позволяло превратиться в чудовище, {w}то что объясняло ради чего я жил.")
    $ Fl.say(Fl_r, "Моя попутчица хотела что-то возразить, но быстро передумала, переведя печальный взгляд на меня, потом на догорающую тетрадь.")
    $ Fl.say(Fl_pi, "Идём.")
    $ Fl.say(Fl_liz, "Ты уверен?")
    $ Fl.say(Fl_pi, "Да. {w}Я обязан был это сделать.")
    $ Fl.say(Fl_pi, "Кстати, я забыл представиться.")
    $ Fl.say(Fl_q6, "Мой кодовый номер Q-66!")
    $ Fl.say(Fl_r, "Этой ночью, я похоронил Пионера. {w}Пионер погиб в ту самую ночь, когда умерла Мику. Но я был так слаб, что не мог отпустить ни её, ни себя...")
    $ Fl.say(Fl_r, "Импостер права. Ни Ян, ни Пионер не смогут выжить в тёмной стороне Совёнка. {w}Я должен был давно принять себя{mn} тот факт, что я сказитель, такой же монстр, как они.")
    $ Fl.say(Fl_liz, "Приятно познакомиться, но я предпочту называть тебя по имени.")
    $ Fl.say(Fl_r, "Улыбка вновь вернулась на лице девушки.")
    $ Fl.say(Fl_r, "Она вновь запрыгнула мне на спину.")
    $ Fl.say(Fl_q6, "Ты что творишь?")
    $ Fl.say(Fl_liz, "Как что? Отправляю нас в другой лагерь!")
    $ Fl.say(Fl_q6, "А запрыгивать на меня зачем?")
    $ Fl.say(Fl_liz, "Ой, ну не бухти!")
    $ Fl.say(Fl_r, "Я хотел уже было возразить, как вдруг...")
    $ Fl.StopMusic(4)
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.Pause (1.0)
    

    $ Fl.PlaySound("Fl_vzhuh", 1, 0, False)
    scene bg Fl_black with Fl_flash
    $ Fl.Pause (0.5)
    scene bg Fl_ext_path2_dark
    show Fl_dust_full
    with Fl_flash
        
    $ Fl.Pause (1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Произошла какая-то странная вспышка, а после мы снова оказались на том же месте.")
    $ Fl.say(Fl_th, "Мы в другом лагере?")
    $ Fl.say(Fl_r, "Мой взгляд опустился чуть ниже. {w}Никакого пепелища после тетради под ногами не было.")
        
    scene bg Fl_ext_musclub_night
    show Fl_dust_full
    with Fl_effect_right1
        
    $ Fl.say(Fl_r, "Позади меня стояло целое и невредимое здание музклуба.")
    $ Fl.say(Fl_liz, "Здорово, правда?")
    $ Fl.say(Fl_q6, "Так это и есть то самое перемещение из одного лагеря в другой?")
    $ Fl.say(Fl_liz, "Ага, оно самое!")
    $ Fl.say(Fl_r, "Только сейчас я почувствовал странное ощущение. {w}Тело было слишком воздушным, а в области лёгких встал ком. Сердце биение замедлилось.")
    $ Fl.say(Fl_th, "Неужели побочный эффект от прыжка?")
    $ Fl.say(Fl_th, "Хотя было бы глупо надеяться, что от такого фокуса ты останешься цел и невредим.")
    $ Fl.say(Fl_liz, "А теперь идём спать.")
    $ Fl.say(Fl_q6, "С начала слезь с меня.")
    $ Fl.say(Fl_liz, "Неа, ты теперь моя лошадка. Иго-иго, вперёд мой верный конь!")
    $ Fl.say(Fl_r, "Я резко сделал наклон, от чего девушка полетела на землю.")
    $ Fl.say(Fl_liz, "Какого...", _with=hpunch)
        
    show liz pioner3 angry2 with Fl_dissolve1
        
    $ Fl.say(Fl_liz, "Какого чёрта ты творишь?!")
    $ Fl.say(Fl_r, "Я молча пошёл по тропинке.")
        
    hide liz pioner3 angry2 with Fl_dissolve1
        
    $ Fl.say(Fl_liz, "Игнорируешь?!")
    $ Fl.say(Fl_liz, "Да постой ты!")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(4)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause (3.5)
    scene bg Fl_ext_dom_night
    show Fl_dust_full
    with Fl_dissolve2
    $ Fl.PlayMusic("Fl_day_2", 1, 4)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Под нескончаемую болтовню Импостера, мы наконец-то дошли до какого-то домика. Он казался мне до боли знакомым или даже родным, но я не мог вспомнить почему.")
    $ Fl.say(Fl_r, "Девушка не стала ждать, когда я что-то скажу, а молча устремилась к двери.")
    $ Fl.say(Fl_r, "Закончив копошиться с дверным замком, она проскользнула внутрь. {w}Я последовал её примеру.")
    $ Fl.HideScreens(_with=Fl_fast)
    $ Fl.PlaySound("Fl_open_door_2", 1.0, 0, False)
    scene bg Fl_black with Fl_effect_4


    $ Fl.Pause(2.5)

    scene bg Fl_int_house_yan_night with Fl_effect_4

    $ Fl.Pause(1.0)

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Внутри было всё как обычно, типичный пионерский домик коих тут однообразных десяток.")
    $ Fl.say(Fl_r, "Я бросил взгляд на зеркало.")
    $ Fl.say(Fl_th, "И снова это безжизненное тело смотрит на меня{mn}")
    $ Fl.say(Fl_r, "Пустые глаза оценивали мою внешность, но чем дольше они это делали, тем меньше оставалось в них жизни.")
    $ Fl.say(Fl_r, "Я закрыл дверцу шкафчика и посмотрел на свою соседку.")
    $ Fl.say(Fl_r, "Она от души потянулась, после чего начала раздеваться.")
        
    show liz nude discontent2 with Fl_dissolve1
        
    $ Fl.say(Fl_liz, "Всё я готова!")
    $ Fl.say(Fl_r, "И вновь девушка не переставала меня удивлять своим распутным характером. {w}Раздевшись догола, она смотрела на меня и демонстрировала все свои красоты.")
    $ Fl.say(Fl_q6, "К чему?")
    
    show liz nude me with Fl_dissolve1
        
    $ Fl.say(Fl_liz, "Ко сну конечно!")
    $ Fl.say(Fl_liz, "Я всегда сплю голая и мне плевать есть в комнате мужчина или нет!")
    $ Fl.say(Fl_th, "Странно, не было даже ни одной шутки про интим. На неё не похоже, видно и правда устала.")
    $ Fl.say(Fl_q6, "Будь по твоему.")
    
    hide liz nude me with Fl_dissolve1
    $ Fl.Master(Fl_bg_zoom_th(1.0, 1.35, 1.5, 0.5, 0.15, 0.5, 0.7))
        
    $ Fl.Pause(2.0)
    $ Fl.say(Fl_r, "Я прилёг на кровать.")
    $ Fl.say(Fl_liz, "Ты прям так спать будешь?")
    $ Fl.say(Fl_r, "Речь явно была о моей одежде.")
    $ Fl.say(Fl_q6, "Да.")
    $ Fl.say(Fl_r, "Сухо ответил я и повернулся лицом к стенке.")
    $ Fl.say(Fl_r, "После стольких ночовок в музклубе я перестал снимать с себя одежду. Меня обычно просто вырубало и я засыпал на холодном полу.")
    $ Fl.say(Fl_liz, "Ну и ладно, зануда.")
    $ Fl.say(Fl_r, "Девушка легла рядом со мной. Ничего не заставило меня ждать, чтобы высказать своё негодование.")
    $ Fl.say(Fl_q6, "Хватит уже ко мне липнуть! В доме есть и вторая кровать.")
    $ Fl.say(Fl_liz, "А мне здесь нравится!")
    $ Fl.say(Fl_q6, "Тогда я могу занять другую.")
    $ Fl.say(Fl_r, "Сказал я и демонстративно приподнялся.")
    $ Fl.say(Fl_liz, "Ладно, одиночка, я ухожу!")
    $ Fl.say(Fl_r, "Импостер встала и грозно протопала к своей кровати.")
    $ Fl.say(Fl_liz, "И{mn} Поспи хорошенько пожалуйста. Я не собираюсь тебя убивать во сне, поэтому нечего всю ночь лежать и пялиться в стену.")
    $ Fl.say(Fl_r, "Я посмотрел в сторону второй кровати. {w}Девушка лежала лицом к стене, пытаясь принят удобную позу для сна.")
    $ Fl.ShowBlink()
        
    $ Fl.Pause(1.5)
    $ Fl.say(Fl_r, "Поверив на слово, я отвернулся к стенке и закрыл глаза.")
    $ Fl.say(Fl_th, "Вот я и покинул свой лагерь.")
    $ Fl.say(Fl_th, "В голове не складывается всё происходящее. {w}Цикл полного абсурда.")
        
    $ Fl.Pause(1.5)
    $ Fl.say(Fl_th, "И что дальше?")
    $ Fl.say(Fl_th, "Сегодня объединился с сказителем, а завтра с богом начну дружить?")
    $ Fl.say(Fl_r, "«У тебя есть цель...» - глупая причина для того чтобы мне помогать. {w}Помогать тому, кого даже не знаешь...")
    $ Fl.say(Fl_th, "Я тебя просто использую, а потом делай что хочешь...")
        
    $ Fl.Pause(1.5)
    $ Fl.say(Fl_r, "Шея начала зудеть.")
    $ Fl.say(Fl_th, "Каждый цикл в моём лагере был сменный аккамулятор для моего устройства. Найду ли я его здесь?")
    $ Fl.say(Fl_th, "Очень в этом сомневаюсь.")
    $ Fl.say(Fl_th, "Скорее всего этот безумный учёный знает в каком лагере я живу и каким-то образом отправлял мне припаску.")
    $ Fl.say(Fl_th, "Но если я начну путешествовать по лагерям, то смогу ли обнаружить аккамулятор вновь?")
    $ Fl.say(Fl_r, "Я не знал сколько держит заряд моё устройство, потому что в начале каждого цикла производил замену блока.")
    $ Fl.say(Fl_th, "Плеееевать, достало уже это всё. Лучше лягу спать и не буду забивать свою голову вопросами, хотя бы во сне!")
    $ Fl.StopMusic(4)
    $ Fl.HideScreens(_with=Fl_dissolve2)
        
    scene bg Fl_black
    $ Fl.HideBlink()
    $ Fl.Pause(7.0)
    $ Fl.DayTime("rain", "rain")
        

    $ Fl.PlayMusic("Fl_Bad Dream Coma - Flat from 41", 1, 6)
    scene bg Fl_black_flash with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Задумывались ли вы хоть раз о мире?")
    $ Fl.say(Fl_r, "Почему он так красив, богат сочным спектором ярких красок. {w}Почему он такой светлый и безобиден?")
    $ Fl.say(Fl_r, "Почему порой мир так идиалезируют, скрывая обратную сторону этой загадочной вселенной что мы живём?")
    $ Fl.say(Fl_r, "А может это не мы его идеалезируем, а мир сам так решил себя преподнести...")
    $ Fl.say(Fl_r, "Многие проклинают свой мир, считаю его виноватым во всём.")
    $ Fl.say(Fl_r, "Мечтают попасть в другой, чтобы больше не видеть старый. Считают его жестоким и несправедливым...")
        
    scene bg Fl_workshop_outside_ruined 
    show Fl_prolog_dream
    with Fl_dissolve2
    $ Fl.say(Fl_r, "Я побывал в двух мирах. И не хочу оставаться ни в одном из них!")
    $ Fl.say(Fl_r, "Почему же людям так сложно угадить? {w}Чего же тогда на самом деле они хотят? {w}Что для них сделал мир не так?")
    $ Fl.say(Fl_r, "Задумался я, прогуливаясь по руинам моего ада, который уже не казался таким страшным. Который умер вместе со мной...")
    $ Fl.say(Fl_r, "Наверное многие его считают не справедливым из-за устроенной системы в нём.")
    $ Fl.say(Fl_r, "Ведь это несправедливо, когда в мире есть уникальные или особенные люди, а ты простой и обычный.")
    $ Fl.say(Fl_r, "Почему же мир так поступает? {w}Почему кому-то всё, а кому-то ничего?")
    $ Fl.say(Fl_r, "У каждого своя роль, возможно крикнет любой, что я не выбирал судьбу в этом мире, он сделал это за меня!")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause(2.5)
    scene bg Fl_houses_ruined 
    show Fl_prolog_dream
    with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "В мире так заведено, кто-то жертва, а кто-то охотник.")
    $ Fl.say(Fl_r, "Но что было бы, если все стали равны? {w}Все были уникальными или простыми людьми? {w}Как бы мир изменился?")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_r, "Никак{mn}")
    $ Fl.say(Fl_r, "Став однородной серой массой, мир не исправишь.")
    $ Fl.say(Fl_r, "Человечество навсегда бы потеряло понятие - индивид. Личность стало бы общее понятие для всех, а не для каждого.")
    $ Fl.say(Fl_r, "Мы бы стали частью кода, системой, которая работает идеально, без сбоев, но и без производительности.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause(2.5)
    scene bg Fl_library_outside_ruined 
    show Fl_prolog_dream
    with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Но даже в самой идеальной системе, может произойти ошибка, которая разрушит механизм мрачного и серого мира.")
    $ Fl.say(Fl_r, "Найдётся тот, кто решит засиять и выбраться из плена ада равенства. Он решит, что не хочет быть как все, хочет быть особенным. И он будет не один, таких ошибок мира будет много.")
    $ Fl.say(Fl_r, "Мир не может быть безупречным. {w}Любой мир{mn}")
    $ Fl.say(Fl_r, "Интересно, а рай можно считать таким миром?..")
    $ Fl.say(Fl_r, "Всегда легко выдумать идилию мира, но редко кто понимает, что это всего лишь грёзы и даже в них существует брешь.")
    $ Fl.say(Fl_r, "Я тоже был наивный и верил в чудо{mn2} Совёнок - моё чудо на яву, так считал я.")
    $ Fl.say(Fl_r, "И во что теперь мой идеальный мир превратился?")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause(2.5)
    scene bg Fl_medical_point_inside_ruined 
    show Fl_prolog_dream
    with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Я считаю любой мир страдает только от его обитателей в нём. Мы же сами и портим его, создаём неравенство, разделям друг друга на классы, колечим то что так сильно проклинаем.")
    $ Fl.say(Fl_r, "Вдовль осмотрев лагерь, на меня напала тоска.")
    $ Fl.say(Fl_th, "Во что же мы превратили это место...")
    $ Fl.StopMusic(4)
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2



    $ Fl.Pause(5.5)
    $ Fl.DayTime("day", "day")
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_kt, "Ян! Ян! Вставай!")
    $ Fl.say(Fl_r, "Кто-то активно бил меня в грудь. {w}Утро началось явно не с кофе, но не менее бодрящее.")
    scene bg Fl_int_house_yan_day:
        zoom 1.3 yalign 0.6 xalign 0.23
    $ Fl.ShowUnblink()
    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 4)
    $ Fl.say(Fl_r, "Ещё не до конца открыв глаза, я поймал кулак, который совершал очередной удар в грудь.")
    $ Fl.say(Fl_liz, "Встал наконец!")
    $ Fl.say(Fl_r, "Сверху меня сидела Импостер и улыбалась. Я уже научился игнорировать белый лифак, что светился каждую секунду в кадре.")
    $ Fl.say(Fl_q6, "А ты всё не прекращаешь ко мне липнуть...")
    $ Fl.say(Fl_liz, "Бу-бу-бу. Псих!")
    $ Fl.say(Fl_liz, "Я уверена каждый бы парень хотел чтобы его так будили!")
    $ Fl.say(Fl_r, "Я опустил голову обратно, переведя взгляд на потолок.")
    $ Fl.say(Fl_th, "Возможно, давно я ни с кем не находился рядом...")
    $ Fl.say(Fl_liz, "Всё, идём.")
    $ Fl.say(Fl_q6, "Куда?")
    $ Fl.say(Fl_liz, "Кушать конечно! Я за ночь сильно проголодалась, а ты всё дрыхнешь.")
    $ Fl.say(Fl_r, "Лениво глянул на будильник.")
    $ Fl.say(Fl_th, "6:45")
    $ Fl.say(Fl_q6, "Столовая ещё закрыта.")
    $ Fl.say(Fl_liz, "Ну вот, будем самые первые и в очереди стоять не придётся.")
    $ Fl.say(Fl_r, "Красноволосая бесия и не планировала отступать, стояла на своём до конца.")
    scene bg Fl_int_house_yan_day at Fl_bg_zoom_otd(1.3, 1, 2.5, 0.23, 0.5, 0.6, 0.5, 1, 1)
    $ Fl.Pause(2.0)
    $ Fl.say(Fl_r, "Приподняв её ногами, я освободился из плена, оставив кровать с девушкой позади.")
    $ Fl.say(Fl_q6, "Пошли.")
    $ Fl.HideScreens(_with=Fl_fast)
    $ Fl.PlaySound("Fl_open_door_2", 1.0, 0, False)
    scene bg Fl_black with Fl_effect_4


    $ Fl.Pause(2.5)

    scene bg Fl_ext_dom_day 
    show Fl_light_c
    with Fl_effect_4

    $ Fl.Pause(1.0)

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Несмотря на яркий солнечный свет, с утра чувствовалась небольшая прохлада. {w}Но именно она и давала свежесть для парочки жаворонков.")
    
    show liz pioner2 smile2 with Fl_dissolve1

    $ Fl.say(Fl_r, "А вот и второй жаворонок выпал из гнезда.")

    hide liz pioner2 smile2 with Fl_dissolve1

    $ Fl.say(Fl_r, "Я молча направился в столовую.")
    $ Fl.say(Fl_liz, "Ты куда?")
    $ Fl.say(Fl_q6, "В столовую.")
    $ Fl.say(Fl_r, "Как всегда немногословно.")
    $ Fl.say(Fl_liz, "А умыться? Ты так и будешь весь день ходить как бомж?")

    show liz pioner2 discontent3 with Fl_effect_left1

    $ Fl.say(Fl_q6, "Ты сейчас серьёзно?")
    $ Fl.say(Fl_th, "Да что с ней такое? {w}Мы не в том мире, чтобы заботиться о повседневных обязанностях.")

    show liz pioner me with Fl_dissolve1

    $ Fl.say(Fl_liz, "Боже, как ты дожил до своих лет?")

    show liz pioner mean with Fl_dissolve1

    $ Fl.say(Fl_liz, "Щас холодной водичкой быстро тебе мозги на место вставим.")

    hide liz pioner mean with Fl_dissolve1
    $ Fl.AttackMaster()
    $ Fl.say(Fl_r, "Пионерка быстро оказалась у меня за спиной, после чего повисла, обхватив меня ногами.")
    $ Fl.say(Fl_liz, "Поехали!")
    $ Fl.say(Fl_th, "Я тебе что ездовая лошадь что ли{mn}")
    $ Fl.say(Fl_q6, "Конечная. Дальше пешком.")
    $ Fl.say(Fl_r, "После того как я ущипнул её в бок. Она тут же слезла с меня.")
    $ Fl.say(Fl_liz, "Козёл!")
    $ Fl.say(Fl_r, "Она обиженно отвернулась и быстрым шагом направилась в сторону умывальников.")
    $ Fl.say(Fl_r, "Но её обида не продлилась и минуты. {w}Пройдя пару метров, Импостер встала и начала меня поторапливать.")
    $ Fl.say(Fl_th, "Я её точно прибью когда-нибудь...")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(4.5)

    scene bg Fl_ext_washstand_day
    show Fl_light_c
    with Fl_dissolve2

    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Шли мы в тишине. По всей видимости Импостер обиделась на меня всерьёз.")
    $ Fl.say(Fl_r, "За столько циклов я уже и забыл что в мире существует вот такие беседы ни о чём, просто чтобы составить компанию. {w}Так что растраиваться из-за тишины я не намерен.")

    scene bg Fl_ext_washstand2_day
    show Fl_light_c
    with Fl_dissolve1

    $ Fl.say(Fl_th, "Давненько мы с тобой не виделись.")
    $ Fl.say(Fl_r, "Обычно с себя кровь я смывал на пляже или на пристане. Поход к умывальникам для меня являлось редкостью.")

    $ Fl.PlaySound("Fl_water_sink_open", 1, 0, False)
    $ Fl.say(Fl_r, "Я не стал тратить много усилий и времени на утренние процедуры. Один раз набрал воды и плеснул себе в лицо.")
    $ Fl.PlaySound("Fl_water_sink_close", 1, 0, False)
    $ Fl.say(Fl_r, "В голове всплыли воспоминания, как впервые решил воспользоваться советским умывальником. Тогда я чуть не закричал от ледяной воды. {w}Вода холодная, а воспоминания тёплые...")

    scene bg Fl_ext_washstand_day
    show Fl_light_c
    with Fl_effect_right2

    $ Fl.say(Fl_r, "Отойдя от умывальника, я не обнаружил пионерку.")
    $ Fl.AttackScreens()
    $ Fl.say(Fl_liz, "Бу-у!")
    $ Fl.say(Fl_q6, "Твою ж!", _with=hpunch)
    $ Fl.say(Fl_r, "Вокруг шеи пронёся дикий холод.")

    $ Fl.PlaySound("Fl_smeh_sn", 1, 0, False)

    show liz pioner2 smile2 with Fl_dissolve1

    $ Fl.say(Fl_liz, "А кто говорил, что холод ему нипочём?")
    $ Fl.say(Fl_th, "Откуда она эту воду взяла с самого северного-полюса?!")
    $ Fl.say(Fl_liz, "Привык уже к холодной воде из умывальников?")
    $ Fl.say(Fl_q6, "Ага, за столько циклов трудно не забить на какую-то там воду из крана.")
    $ Fl.say(Fl_liz, "Тогда почему сейчас тебе она показалась очень холодной?")
    $ Fl.say(Fl_r, "Я задумался...")

    $ Fl.Pause(3.0)
    $ Fl.say(Fl_q6, "Снова твоих рук дело?")

    show liz pioner2 discontent3 with Fl_dissolve1

    $ Fl.say(Fl_liz, "А я что? {w}Я ничего...")
    $ Fl.say(Fl_th, "Её способность слишком сильная. {w}Визуальные искажения, так ещё и тактильные глюки.")
    $ Fl.say(Fl_th, "Если так подумать, то она может сделать так что жертва умрёт от болегого шока от обычного пореза.")
    $ Fl.say(Fl_th, "Тут моя грубая сила бессильна{mn}")

    show liz pioner me with Fl_dissolve1

    $ Fl.say(Fl_liz, "Ой, ну всё! Снова он витает в облаках.")

    show liz pioner smile with Fl_dissolve1

    $ Fl.say(Fl_liz, "Но правда моя способность удивительная?")
    $ Fl.say(Fl_r, "Импостер была очень горда собой. Ухмылка так и не спадала с её лица.")
    $ Fl.say(Fl_q6, "Там вроде кто-то есть хотел?")

    hide liz pioner smile with Fl_dissolve1

    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(4.5)

    scene bg Fl_ext_dining_hall_near_day
    show Fl_light_c
    with Fl_dissolve2

    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Как и ожидалось столовая была закрыта.")
    $ Fl.say(Fl_q6, "И что теперь будем делать, мисс голодная?")
    $ Fl.say(Fl_liz, "Ждать, скоро прозвучит горн.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(2.5)
    $ Fl.PlaySound("Fl_dinner_horn_processed", 1, 0, False)
    $ Fl.Pause(2.0)

    scene bg Fl_ext_dining_hall_near_day
    show Fl_light_c
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Успев выкурить сигарету, мы всё же дождались горна.")
    $ Fl.say(Fl_r, "Импостер не стала ждать и сразу схватилась за ручку двери.")
    $ Fl.say(Fl_q6, "Она ещё закры{break}")
    $ Fl.say(Fl_r, "Но не успел я договорить, как девушка уже зашла внутрь.")
    $ Fl.say(Fl_th, "Это как так?")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2
    $ Fl.StopAmbience(3)


    $ Fl.Pause(2.0)
    $ Fl.PlayAmbience("Fl_dining_hall_empty", 1, 4)
    scene bg Fl_int_dining_hall_day with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Впервые мне довелось лицезреть пустую столовую после горна. Голодных пионеров не было, все столы пусты - выбирай любой.")
    $ Fl.say(Fl_r, "Хотя насчёт голодных пионеров я ошибся. Один уже сидел у окна с двумя порциями еды.")
    $ Fl.say(Fl_th, "Когда она уже успела нам еду взять?")
    
    show Fl_chair3
    show liz pioner smile:
        xalign 0.5
        Fl_pris2
    with Fl_dissolve1
    $ Fl.say(Fl_liz, "Я булочку у тебя уже конфисковала, чай может тоже потом заберу. Так что не зевай!")
    $ Fl.say(Fl_q6, "А ты шустрая. Снова твоя магия?")
    $ Fl.say(Fl_liz, "Неа, просто люблю поесть.")
    $ Fl.say(Fl_q6, "Это заметно.")
    $ Fl.say(Fl_r, "Сказал я и нехотя притянул к себе тарелку с кашей.")

    show liz pioner3 angry2 with Fl_dissolve1

    $ Fl.say(Fl_liz, "Ты на что это намекаешь?!")
    $ Fl.say(Fl_r, "Я молча усмехнулся в ответ и перешёл к трапезе.")

    show liz pioner discontent2 with Fl_dissolve1

    $ Fl.say(Fl_r, "Импостер обиженно отвернулась от меня.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(3)


    $ Fl.Pause(1.5)
    scene bg Fl_int_dining_hall_people_day
    show Fl_chair3
    show liz pioner discontent2:
        xalign 0.5
        parallel:
            ypos 0.07
    with Fl_dissolve3

    $ Fl.PlayAmbience("Fl_dining_hall_full", 1, 4)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Долго насладиться завтраком в тишине не вышло. Уже через минут 5 столовая приняла свой обычный облик - шумные пионеры и занятые столы.")
    $ Fl.say(Fl_q6, "Слушай, а ничего что мы даже у вожатой не были? {w}Мы в теории не приехали сюда.")

    show liz pioner scorn with Fl_dissolve1

    $ Fl.say(Fl_liz, "А это обязательно?")
    $ Fl.say(Fl_liz, "Привыкай, так всегда когда перемещаешься между лагерями.")
    $ Fl.say(Fl_liz, "Да и какая разница. Окружающие нас не видят же.")
    $ Fl.say(Fl_r, "Я вопросильно взглянул на пионерку. Последние слова меня очень заинтересовали.")

    show liz pioner smile with Fl_dissolve1

    $ Fl.say(Fl_liz, "Я заставила окружающих видеть нас, как пионерок из второго отряда.")
    $ Fl.say(Fl_th, "Интересно. {w}Получается я мог столкнуться с Импостером ещё раньше? Просто не знал, что это она в образе другой куклы.")
    $ Fl.say(Fl_th, "Правда игра в детектива сказала - что так оно и есть.")
    $ Fl.say(Fl_q6, "И кого ты изображаешь на этот раз?")
    $ Fl.say(Fl_liz, "Лену. А ты Таня.")
    $ Fl.say(Fl_q6, "Какая ещё Таня?")
    $ Fl.say(Fl_r, "Она лишь больше улыбнулась, а я остался без ответа.")
    $ Fl.say(Fl_th, "Никак не могу понять, как её способность работает на самом деле. Кажется всё довольно просто, но если капнуть глубже, то механизм этой способности вызывает сплошной хаус в голове.")
    $ Fl.say(Fl_q6, "Как тебе удаётся полностью перевоплощаться в других?")
    $ Fl.say(Fl_q6, "Это же нужно знать о человеке всё? Строение, фигуру, вес, точный рост и так далее.")

    show liz pioner surprise2 with Fl_dissolve1

    $ Fl.say(Fl_liz, "Ты о чём вообще? {w}Откуда я это знаю, да и зачем мне это нужно. Я бы ещё не хранила в голове все параметры кукол.")
    $ Fl.say(Fl_q6, "Тогда каким образом ты идеально превращаешься в других?")

    show liz pioner me with Fl_dissolve1

    $ Fl.say(Fl_liz, "Да ни в кого я не превращаюсь!")
    $ Fl.say(Fl_liz, "Я просто делаю так чтобы человек меня в образе другого видел. Сейчас же ты видишь меня такой какая я есть.")
    $ Fl.say(Fl_th, "Действительно{mn} Что-то я об этом не подумал.")
    $ Fl.say(Fl_th, "Искажение пространства - искажает и само восприятие окружающих. Значит она может сама выбрать, кто попадёт под влияние силы, а кто нет.")
    $ Fl.say(Fl_r, "За последнее время моё осознание очень резко изменилось о лагере. Было трудно поверить, что сказители и правда существуют и спокойно принять их способности.")

    show liz pioner mean with Fl_dissolve1

    $ Fl.say(Fl_r, "Пока я размышлял, девушка неожиданно переменилась в лице. У неё появилась ехидная ухмылка.")
    $ Fl.say(Fl_th, "Сейчас точно что-то ляпнет{mn}")
    $ Fl.say(Fl_liz, "Я кстати могу тебе и показать любую девушку в лагере обнажённую.")
    $ Fl.say(Fl_liz, "Могу даже Тихоню показать в любом нижнем белье что ты захочешь.")
    $ Fl.say(Fl_th, "Не подвела чуйка. Ляпнула как обычно.")
    $ Fl.say(Fl_q6, "Нет спасибо. Переживу как-то без этого.")

    show liz pioner2 discontent3 with Fl_dissolve1
    $ Fl.Pause(1.0)
    show liz pioner2 smile2 with Fl_dissolve1

    $ Fl.say(Fl_liz, "Так и знала, что тебе больше мои сиськи понравились!")
    $ Fl.say(Fl_th, "Ляпнула х2{mn}")
    $ Fl.say(Fl_q6, "Мне стоит это как-то комментировать?")
    $ Fl.say(Fl_r, "Спросил я с каменным лицом.")

    show liz pioner smile with Fl_dissolve1

    $ Fl.say(Fl_liz, "Да не стесняйся! Можешь потрогать их в любой момент, я разрешаю.")
    $ Fl.say(Fl_th, "Тут все пионерки поехавшие? Что Тихоня со своими наклонностями яндере, то эта со своими хентай сценами...")

    show liz pioner scorn with Fl_dissolve1

    $ Fl.say(Fl_liz, "Ладно, я поела. Теперь можем идти.")
    $ Fl.say(Fl_q6, "И куда на этот раз?")
    $ Fl.say(Fl_liz, "Будем учить тебя перемещаться между лагерями. Или ты планируешь здесь засесть навечно, как в своём лагере?")
    $ Fl.say(Fl_r, "Предложение было очень внезапным. Такой жест я никак не мог ожидать.")
    $ Fl.say(Fl_r, "Но отказываться было грех от такого. Сидеть на одном месте ни к чему не приведёт.")

    scene bg Fl_int_dining_hall_people_day with Fl_dissolve1

    $ Fl.say(Fl_q6, "Тогда идём.")
    $ Fl.say(Fl_r, "Пионерка поддержала эту идею и быстро отнесла подносы с едой. После чего мы покинули столовую.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2
    $ Fl.StopAmbience(3)


    $ Fl.Pause(4.0)
    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 4)
    scene bg Fl_ext_boathouse_day
    show Fl_light_c
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Нашим местом для тренировок стала пристань. Довольно малолюдное место, не хотелось лишний раз притворяться куклой.")
    $ Fl.say(Fl_q6, "Что от меня требуется?")
    $ Fl.say(Fl_liz, "Ну смотри. Для начала ты должен примерно понимать, как происходит прыжок между лагерями.")
    $ Fl.say(Fl_q6, "Всмысле примерно? Ты сама не знаешь точно, как это работает?")
    $ Fl.say(Fl_liz, "Да знаю я! {w}Просто у всех это происходит по разному, но есть схожая деталь.")
    $ Fl.say(Fl_r, "Девушка села на край причала, свесив ноги в сторону воды.")
    $ Fl.say(Fl_liz, "Понимаешь, перед тем как совершить прыжок ты должен чётко представить, как пространноство вокруг тебя меняется, словно в подсознании ты в другом лагере. Ну вот, будто что-то вокруг не так, что-то изменилось.")
    $ Fl.say(Fl_th, "С такими объяснениями будет тяжко...")
    $ Fl.say(Fl_liz, "Не корчи такую рожу. Сейчас всё поймёшь!")
    $ Fl.say(Fl_r, "Не оставила без внимания мой скептический взгляд пионерка.")
    $ Fl.say(Fl_liz, "Кхм.. Так о чём я?")
    $ Fl.say(Fl_liz, "Точно! {w}Многие сказители научились прыжкам совсем случайно, кто-то во сне, кто-то стоило ему закрыть глаза, а кто-то в критической ситуации или в сильном стрессе.")
    $ Fl.say(Fl_liz, "Но каждый из них перед своей телепортацией представлял будто всё вокруг в лагере меняется, они мысленно перемещали себя в другое место, там где их нет.")
    $ Fl.say(Fl_th, "Представить что ты в другом месте силой мыслей. Я точно не в фентази мире? Это слишком даже для меня.")
    $ Fl.say(Fl_th, "Хотя всё здесь стало слишком для меня.")
    $ Fl.say(Fl_r, "Импостер резко встала и подбежала ко мне. Одарив меня улыбкой, она схватила меня за руку.")
    $ Fl.say(Fl_liz, "Давай попробуй!")
    $ Fl.say(Fl_q6, "А держаться за руки обязательно?")
    $ Fl.say(Fl_r, "Возмутился я.")
    $ Fl.say(Fl_liz, "Ты сейчас не контролируешь своё перемещение. Вдруг тебя куда-то унесёт далеко, а мне тебя дурака искать потом тысячу лет?")
    $ Fl.say(Fl_th, "Даже такое может быть?")
    $ Fl.say(Fl_q6, "Ладно, мне нужно просто представить как я оказываюсь в другом лагере?")
    $ Fl.say(Fl_liz, "Ага. Закрывай глаза, так будет проще.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(5.0)
    scene bg Fl_ext_boathouse_day
    show Fl_light_c
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Не знаю сколько я уже стою у пристони и жмурю глаза, но безрезультатно. {w}С каждой секундой моё терпение кончалось, мне казалось это слишком глупым, стоять и в голове картинки придумывать.")
    $ Fl.say(Fl_r, "Пионерка отпустила мою руку и завозмущалась:")
    $ Fl.say(Fl_liz, "Всё хватит на сегодня, это бесполезно!")
    $ Fl.say(Fl_r, "Импостер молча села на причал и смотрела в воду. {w}Со стороны казалось что ей был очень важен мой результат и в моей неудаче винила себя.")
    $ Fl.say(Fl_r, "Я присел рядом.")
    $ Fl.say(Fl_q6, "А какого это перемещаться между лагерями?")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_liz, "Это страшно{mn}")
    $ Fl.say(Fl_r, "Наши взгляды пересеклись. Она говорила в серьёз.")

    $ Fl.PlayMusic("Fl_reeducated", 1, 4)
    $ Fl.say(Fl_liz, "Извини что накричала. Я ничем не лучше тебя в прыжках.")
    $ Fl.say(Fl_liz, "Многие из сказителей умеют перемещаться в определённый лагерь, который им нужен. А я могу только в рандомный.")
    $ Fl.say(Fl_liz, "Помнишь ты рассказывал, что видел у Кукловода карту с секторами вроде?")
    $ Fl.say(Fl_q6, "Помню.")
    $ Fl.say(Fl_liz, "Лагеря и правду делятся на типы. {w}Есть обычные, как этот и твой. {w}Есть и пустышки, там нет ни единой живой души. {w}А есть опасные для жизни, где ты не знаешь чего ожидать и в какой момент твоей жизни грозит опасность.")
    $ Fl.say(Fl_th, "Вот оно что. Поэтому она взяла меня за руку.")
    
    $ Fl.Pause(1.5)
    $ Fl.say(Fl_th, "Интересно в каком из типов лагеря живёт Неко богиня?")
    $ Fl.say(Fl_r, "Я перевёл взгляд на воду, всматриваясь как колеблется дно лодки.")
    $ Fl.say(Fl_liz, "У каждого сказителя тоже есть свой лагерь - это тот в который ты попал после попадание в «Совёнок».")
    $ Fl.say(Fl_th, "Тогда понятно откуда взялись частые визиты Тихони. Я жил в своём лагере, там меня было легко обнаружить.")
    $ Fl.say(Fl_th, "Даже не так. {w}Вероятнее всего после нашей первой встречи она решила ещё раз проверить и убедиться в том же я лагере или нет. И если она способна перемещаться куда она хочет, то прийти в гости в мой лагерь не проблема.")
    $ Fl.say(Fl_q6, "А тебе выпадал шанс оказаться в опасном лагере?")
    $ Fl.say(Fl_liz, "Да{mn} Он был наполнен густым туманом. Там не было ни еды, ни воды. Первая ночь прошла спокойно, но последующие дни стоило стемнеть, как начинался бесконечный вой горна и туман усиливался, спать было невозможно.")
    $ Fl.say(Fl_q6, "Почему просто не телепортировалась в другой лагерь?")
    $ Fl.say(Fl_liz, "Не знаю. Что-то блокировало перемещение, сколько бы я не пыталась, но постоянно открывала глаза в злосчастном тумане...")
    $ Fl.say(Fl_liz, "Я пробыла в этом аду целых три цикла, пока в один из дней не приехал автобус. Только там я смогла совершить прыжок и оказаться в нормальном лагере.")
    $ Fl.say(Fl_th, "Значит не всё так просто, прыгнешь не туда и ты можешь застрять навечно в каком-то лагере.")

    $ Fl.PlaySound("Fl_dinner_horn_processed", 1, 0, False)
    $ Fl.Pause(2.0)
    $ Fl.StopMusic(4)
    $ Fl.say(Fl_r, "Стоило горну о себе дать знать, как пионерка тут же вскочила и вновь засияла.")
    $ Fl.say(Fl_liz, "Пошли кушать!")
    $ Fl.say(Fl_q6, "Мы же уже завтракали.")
    $ Fl.say(Fl_r, "Я особо не нуждался в еде, ведь в каждом цикле организм приходил в норму и принимать пищу на регулярной основе я не видел смысла.")
    $ Fl.say(Fl_r, "Но Импостер не разделяла мои мысли.")
    $ Fl.say(Fl_liz, "И что? Как можно отказываться от еды! Что что, а готовят здесь очень вкусно!")
    $ Fl.say(Fl_q6, "Тогда можешь взять мою порцию, я не голоден.")
    $ Fl.say(Fl_r, "Девушка хотела возразить, но я её перебил:")
    $ Fl.say(Fl_q6, "Да и мне нужно кое-что проверить.")
    $ Fl.say(Fl_liz, "Я могу пойти с то{break}")
    $ Fl.say(Fl_q6, "Это личное. И поспеши, а то все места займут.")
    $ Fl.say(Fl_r, "Сделав хитрый взгляд, она молча ушла. Остался только я и пристань.")
    $ Fl.say(Fl_th, "Пора кое-что проверить.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(3)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(4.5)
    $ Fl.PlayAmbience("Fl_catacombs", 1, 4)
    scene bg Fl_bynker_light with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Бункер тоже изменился. Электричество работало даже без пропажи Толяна. Но вероятность, что сейчас тот самый день никто не отменял.")
    $ Fl.say(Fl_r, "Что же привело меня в катакомбы старого лагеря?")
    $ Fl.say(Fl_r, "Беспокойство насчёт аккамулятора для моего устройство не покидало меня. Шанс того что он существует в других лагерях крайне мал.")
    $ Fl.say(Fl_th, "Третий шкафчик справа{mn}")

    $ Fl.Pause(2.5)
    $ Fl.say(Fl_q6, "Странно...")
    $ Fl.say(Fl_th, "В этом лагере он тоже есть.")
    $ Fl.say(Fl_r, "Я был удивлён и с опаской разглядывал маленький блок питания в руках.")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_th, "Раньше он никогда не появлялся в бункере. Я это прекрасно знаю. Большую часть времени, когда не хотелось убивать проводил именно тут.")
    $ Fl.say(Fl_th, "Я думал, что после моего перерождения в сказителя безумный учёный каким-то образом отправлял в мой лагерь этот аккамулятор, но что-то не сходится.")
    $ Fl.say(Fl_th, "Почему это устройство находится в каждом лагере?")
    $ Fl.say(Fl_th, "Варианта всего два.")
    $ Fl.say(Fl_th, "За мной следят. {w}Либо каким-то образом доктор повлиял на сам лагерь и теперь он в каждом цикле обновляет новый предмет.")
    $ Fl.say(Fl_r, "Этих два варианта ввели меня в ступор. {w}С одной стороны если за мной следят, то с какой целью? А другой, если доктор и правда смог повлиять на сам лагерь, то кто он на самом деле?")
    $ Fl.say(Fl_r, "Быстро озираясь по сторонам, я принял решение покинуть бункер.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(3)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.DayTime("night", "night")


    $ Fl.Pause(6.5)
    $ Fl.PlayAmbience("Fl_camp_center_night", 1, 4)
    scene bg Fl_ext_boathouse_alt_night
    show Fl_dust_full
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.PlayMusic("Fl_titr2", 1, 4)
    $ Fl.say(Fl_r, "Лагерь погряз во мраке. Обычное явление.")
    $ Fl.say(Fl_r, "День пролетел быстро, как любой другой, оставляю за собой восспоминания. Всё как обычно.")
    $ Fl.say(Fl_r, "Я стоял у забора пристани и смотрел на другой берег. Когда-то это место мне показала Кристина. {w}Но и это осталось лишь воспоминанием минувших дней.")
    $ Fl.say(Fl_r, "Достав из кармана то из-за чего я ломаю голову весь день, молча потушил сигарету.")
    $ Fl.say(Fl_th, "Интересно, а если я не заменю аккамулятор начнётся ли новый цикл для меня?")
    $ Fl.say(Fl_r, "Серые тучи неспеша проплывали мимо моих размышлений. Никто не мог дать мне ответ. Природа способна удивлять и демонстрировать свои красоты, природа нас обеспечивает всем, но и она не все сильна.")
    $ Fl.say(Fl_r, "После того как мы с Импостером разошлись, я больше её не видел.")
    $ Fl.say(Fl_th, "Интересно, зачем она на самом деле здесь? {w}Не понимаю её, идти против Кукловода. Ради чего?")
    $ Fl.say(Fl_r, "В этом лагере я научился самому главному, недоверять никому и не подпускать других к себе близко. Совёнок слишком жесток для счастья и дружбы.")
    
    $ Fl.Pause(3.5)
    $ Fl.say(Fl_q6, "...")
    $ Fl.say(Fl_r, "Сзади раздались тихие шаги.")
    $ Fl.say(Fl_r, "Весь лесной пейзаж вдали загородила булка в упаковке.")
    $ Fl.say(Fl_liz, "Поешь хоть.")
    $ Fl.say(Fl_r, "Я молча взял булку и повернулся.")

    show liz pioner scorn with Fl_dissolve1

    $ Fl.say(Fl_th, "Нашла меня всё таки.")

    show liz pioner offense with Fl_dissolve1

    $ Fl.say(Fl_liz, "Мне долго ждать?")
    $ Fl.say(Fl_q6, "Чего?")
    $ Fl.say(Fl_liz, "Чего-чего... Ешь давай, я для кого на ужин выпросила остатки, чтобы один придурок поел?")
    $ Fl.say(Fl_th, "Ты мне что мамочка, указывать что мне делать?")
    $ Fl.say(Fl_q6, "Я не голоден.")
    $ Fl.say(Fl_r, "Съязвил я и облокатился на перила забора.")

    show liz pioner3 angry2 with Fl_dissolve1

    $ Fl.say(Fl_liz, "Да я в тебя эту булку силой сейчас запихаю!")
    $ Fl.say(Fl_q6, "Ну попробуй...")

    show liz pioner me with Fl_dissolve1
    $ Fl.Pause(1.0)
    hide liz pioner me with Fl_dissolve1

    $ Fl.say(Fl_r, "Девушка вошла в ярость, но тут же остыла и просто встала рядом.")
    $ Fl.say(Fl_r, "Привычная ухмылка пропала с её лица, она с пустым лицом смотрела вдаль.")

    $ Fl.Pause(1.0)
    $ Fl.say(Fl_th, "Бесит...")
    $ Fl.say(Fl_r, "Я распаковал булку.")

    $ Fl.Pause(2.5)
    $ Fl.say(Fl_liz, "Где ты пропадал весь день?")
    $ Fl.say(Fl_r, "Задала вопрос пионерка всё так же неотрываясь от просмотра ночного пейзажа.")
    $ Fl.say(Fl_q6, "Мне нужно было кое-что проверить.")
    $ Fl.say(Fl_r, "Тяжёлый вздох.")
    $ Fl.say(Fl_liz, "Я тебя по всему лагерю искала. И это вся твоя отмазка?")
    $ Fl.say(Fl_q6, "А что ты хотела услышать?")
    $ Fl.say(Fl_liz, "Хоть немного о тебе...")
    $ Fl.say(Fl_r, "Я насторожился.")
    $ Fl.say(Fl_liz, "Например, что это такое?")
    $ Fl.say(Fl_r, "Оставаясь в том же положении, пионерка подняла руку, в которой находился аккамулятор для устройства.")
    $ Fl.say(Fl_th, "Какого{break2}")
    $ Fl.say(Fl_r, "В карманах было пусто.")
    $ Fl.say(Fl_q6, "Когда ты{break2}")
    $ Fl.say(Fl_liz, "Когда ты услышал мои шаги, ты быстро спрятал что-то в карман.")
    $ Fl.say(Fl_liz, "А потом решила выждать момент с булкой.")
    $ Fl.say(Fl_r, "Я облокотился на перила и откинул голову назад.")
    $ Fl.say(Fl_th, "Не отстанет же...")
    $ Fl.say(Fl_q6, "Это аккамулятор от моего устройства. В моём лагере он появлялся каждый цикл.")
    $ Fl.say(Fl_liz, "И ты решил проверить найдёшь ли ты его здесь...")
    $ Fl.say(Fl_r, "Импостер покрутила зарядник и наконец-то повернулась в мою сторону.")
    $ Fl.say(Fl_liz, "Что будет если его не заменить?")
    $ Fl.say(Fl_q6, "Не знаю. Я каждый цикл его заменял.")
    $ Fl.say(Fl_liz, "Знаешь, мне кажется эта безделушка тебе вовсе не нужна.")
    $ Fl.say(Fl_r, "Я с опаской быстро перевёл взгляд на пионерку, которая до сих пор спокойно крутила аккамулятор в руке.")
    $ Fl.say(Fl_th, "Не нужен? Да я себя полудохлым чувствовал стоило аккамулятор вытащить!")
    $ Fl.say(Fl_q6, "Отдай сюда!")
    $ Fl.say(Fl_r, "Девушка лишь молча сменила руку чтобы я не смог выхватить устройство.")
    $ Fl.say(Fl_liz, "Ты говоришь, что он появляется в каждом новом цикле. Но что он тогда делает здесь? В этом лагере?")
    $ Fl.say(Fl_liz, "Да и не похоже это на какой-то там аккамулятор, больше на обычный блок схемы в красивой обёртке.")
    $ Fl.say(Fl_liz, "Самый простой способ тебя усадить в камеру для опытов, просто создать иллюзию - что ты можешь умереть.")
    
    $ Fl.Pause(2.0)
    $ Fl.say(Fl_th, "А она права. Что если доктор не хотел чтобы я покинул свой лагерь и оставался там.")
    $ Fl.say(Fl_th, "Звучит логично. {w}Превратить мой лагерь в арену, чтобы посмотреть выживу ли я после встречи с любым сказителем. Вот почему Кукловод так спокойно дал указ убить меня, если Тихоня меня нашла, то и другие найдут легко.")
    $ Fl.say(Fl_r, "Пока я размышлял, девушка бросила устройство на землю и со всей силы ударила ногой по нему.")
    $ Fl.say(Fl_q6, "Ты что творишь, дура?!", _with=hpunch)
    $ Fl.say(Fl_r, "Аккамулятор разлетелся на куски.")
    $ Fl.say(Fl_liz, "Хах. Я была права!")
    $ Fl.say(Fl_r, "Радостно воскликнула Импостер и отдала мне аккамулятор.")
    $ Fl.say(Fl_liz, "Видишь обычная блок схема, нет никакого аккамулятора внутри. Он никогда и не мог разрядиться.")
    $ Fl.say(Fl_th, "И правда...")
    $ Fl.say(Fl_r, "Сам блок был обычной микросхемой. Он скорее исполнял роль процесса, как в компьютере. Никаким зарядным устройством не являлась моя находка в бункере.")
    $ Fl.say(Fl_q6, "А если бы ты ошиблась?")
    $ Fl.say(Fl_liz, "Ну у меня был шанс на успех 50 процентов, больше чем у тебя тогда с подозреваемыми! Вот я и рискнула.")
    $ Fl.say(Fl_th, "Ты что дура?! Решила поверить в удачу?!")
    
    $ Fl.Pause(2.0)
    $ Fl.say(Fl_th, "Хотя она права, я же поступил точно так же, а ведь мог и умереть если не повезло с ответом.")
    $ Fl.say(Fl_r, "Я улыбнулся.")
    $ Fl.say(Fl_liz, "Да и не оставила бы я тебя умирать! Прыгнули бы на поиски в другой лагерь.")
    $ Fl.say(Fl_r, "Импостер тоже улыбнулась в ответ.")
    $ Fl.say(Fl_th, "Мы оба придурки, верим в чудо и рискуем.")
    $ Fl.say(Fl_q6, "Зачем?")
    $ Fl.say(Fl_liz, "А?")
    $ Fl.say(Fl_q6, "Зачем ты мне помогаешь? Что тебе даст это?")
    $ Fl.say(Fl_r, "Брови девушки нахмурились, она была зла и печальна одновременно.")
    $ Fl.say(Fl_liz, "Мы сказители, каждый из нас считает себя особенным, живой личностью среди кукол.")
    $ Fl.say(Fl_liz, "Поэтому мне решать помогать тебе или нет. И я не обязана слушать приказы других.")
    $ Fl.say(Fl_liz, "Мне просто с тобой весело! Считай у нас взаимопомощь, ясно?!")
    $ Fl.say(Fl_th, "Взаимопомощь. Вероятно так и есть. {w}Мы просто обмениваемся знаниями и выживаем в этом безумие двоём.")
    $ Fl.say(Fl_th, "Я с ней пока мне это выгодно, а у неё свои тараканы. Пока не потеряем интерес к друг другу можно и повозиться с ней.")
    $ Fl.say(Fl_q6, "Ясно. Но больше так не делай, поняла?")
    $ Fl.say(Fl_liz, "Живём то всего один раз, надо в жизни попробовать всё, даже сломать эту фиговину что ты нашёл в бункере!")
    $ Fl.say(Fl_q6, "Один раз говоришь?")
    $ Fl.say(Fl_r, "Мы оба не сдержали смех. Такие слова явно не относились к нам, кто заперт в бессмертном круге летнего курорта в Совёнке.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(5)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(5.5)
    scene bg Fl_ext_boathouse_alt_night
    show Fl_dust_full
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Где-то вдалике начало светать. Лагерь готовился к своему пробуждению, запускать однотипный сценарий его жителей.")
    $ Fl.say(Fl_r, "Сложно сказать сколько сейчас на часах и сколько мы провели времени просто молча любуясь пейзажем.")
    $ Fl.say(Fl_r, "Но всему свойственно заканчиваться.")
    $ Fl.say(Fl_liz, "Может пойдём спать, скоро светать будет?")
    $ Fl.say(Fl_r, "Я бы мог возразить как обычно, но в итоге поддержал идею.")
    $ Fl.say(Fl_r, "Возможно за столько циклов моё вечное напряжение утихло и такая вещь как сон не казалась мне бесполезной.")
    $ Fl.say(Fl_q6, "Идём.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(3.5)

    scene bg Fl_ext_dom_night
    show Fl_dust_full
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Дом. {w}До сих пор не привык.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(4)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(2.0)

    scene bg Fl_int_house_yan_night with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Как и вчера Импостер снова сняла с себя всю одежду и сразу легла в кровать.")
    $ Fl.say(Fl_th, "Даже приставь не будешь?")
    $ Fl.say(Fl_r, "Молча подошёл к кровати. {w}Повторил всё как в прошлом сценарии - лёг спать в одежде.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_int_house_of_un_ceiling_rain with Fl_effect_down1


    $ Fl.Pause(2.5)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Но кто просто так мне даст погрузиться в мир грёз?")
    $ Fl.say(Fl_r, "Лицезрея люстру я пытался собраться с мыслями, что было крайне сложно. Неизвестность - был мой самый главный враг.")
    $ Fl.say(Fl_th, "Кто же я на самом деле?")
    $ Fl.say(Fl_th, "Я знал Яна, знал Пионера. {w}Но мне ничего неизвестно о нынешнем себе.")
    $ Fl.say(Fl_th, "Столько пустоты, столько вопросов, прям персанаж загадка. А я просто пассажир этого с виду мертвецкого тела.")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_th, "Аккамулятор оказался всего лишь приманкой, чтобы я не сбежал. {w}Интересно, что на самом деле у меня за способность?")
    $ Fl.say(Fl_th, "Ошейник на моей шеи точно не моя способность. У каждого сказителя свой талант, который он может использовать без всяких устройств.")
    $ Fl.say(Fl_th, "Тогда для чего мне вживили это устройство?")

    $ Fl.Pause(3.0)
    $ Fl.say(Fl_th, "Достало{mn}")
    $ Fl.say(Fl_r, "Я продолжил молча пялиться в потолок, пытался избежать мыслей и вопросов, которые изурядно надоели всем.")
    $ Fl.say(Fl_r, "Слева от меня послышалась возня.")
    $ Fl.say(Fl_liz, "Ян...")
    $ Fl.say(Fl_q6, "Что?")
    $ Fl.say(Fl_liz, "Спокойной ночи.")
    $ Fl.say(Fl_r, "Девушка не оставила без внимания, мою бессоницу.")
    $ Fl.say(Fl_q6, "Ага.")
    scene bg Fl_black with Fl_dissolve2

    $ Fl.say(Fl_r, "После чего я повернулся в сторону стенки и сжался калачиком.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause(6.0)
    $ Fl.DayTime("day", "day")
    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 4)
    scene bg Fl_ext_boathouse_day
    show Fl_light_c
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "С момента когда я познакомился с Импостер прошло 3 цикла. {w}За это время между нами многое поменялось, я уже привык к вечному прилипанию и постоянным похождениям в столовую. Один раз даже дошло до кражи конфет.")
    $ Fl.say(Fl_r, "Характер у неё сущий кошмар, гиперактивность так и разрывала максимальную шкалу моего негодования. Она же куда проще свыклась с моим серьёзным характером, к моему молчанию и пустому взгляду.")
    $ Fl.say(Fl_liz, "Господи ты безнадёжен.")
    $ Fl.say(Fl_r, "Из моего монолога вытащил недовольный голос девушки.")
    $ Fl.say(Fl_th, "Прошло столько времени, а совершить прыжок в другой лагерь у меня так и неполучилось...")
    $ Fl.say(Fl_liz, "Я сколько раз тебе говорила, не думай ты о всякой ерунде сконцентрируйся на мысли, как переносишься в другое место!")
    $ Fl.say(Fl_q6, "Проще сказать, чем сделать.")

    show liz pioner3 angry2 with Fl_dissolve1

    $ Fl.say(Fl_r, "Она не оценила мой настрой. {w}И так постоянно, мои неудачи вызывали в ней злость, а моё равнодушие парировалось фразей: «Чувствую себя, твоей мамой!».")

    show liz pioner discontent2 with Fl_dissolve1

    $ Fl.say(Fl_liz, "Когда-нибудь ты сможешь совершить прыжок в любом случае.")

    show liz pioner mean with Fl_dissolve1

    $ Fl.say(Fl_liz, "Но я сделаю всё возможное, чтобы «Когда-нибудь» у тебя произошло раньше!")
    $ Fl.say(Fl_th, "И откуда у неё столько самоуверенности?")
    $ Fl.say(Fl_r, "В отличие от меня у Импостер всегда был оптимистичный настрой. {w}Что не скажешь про меня.")
    $ Fl.say(Fl_r, "Я придерживался взгляду на мир - реализму. Я не верил в лучшее, но и не думал, что всё плохо. Просто оценивал свои возможности и цели.")
    $ Fl.say(Fl_th, "Может поэтому до сих пор стою здесь, в этом же лагере?")

    show liz pioner smile with Fl_dissolve1

    $ Fl.say(Fl_liz, "Яяяян...")
    $ Fl.say(Fl_r, "Эту ухмылку я узнаю из тысячи. {w}Вариантов всего два.")
    $ Fl.say(Fl_q6, "Я не пересплю с тобой.")

    show liz pioner me with Fl_dissolve1

    $ Fl.say(Fl_liz, "Я и не собиралась...")
    $ Fl.say(Fl_q6, "Снова хочешь есть?")

    show liz pioner smile with Fl_dissolve1

    $ Fl.say(Fl_liz, "Ты не представляешь, я такой голодный!")
    $ Fl.say(Fl_th, "Кто бы сомневался{mn}")
    $ Fl.say(Fl_q6, "Иди, я не голоден.")

    show liz pioner me with Fl_dissolve1

    $ Fl.say(Fl_liz, "Снова он за своё. Опять весь день где-то проподать будешь?")
    $ Fl.say(Fl_r, "Но моим ответом стала тишина.")

    hide liz pioner me with Fl_dissolve1

    $ Fl.say(Fl_liz, "Ну и ладно, твою порцию я тоже съем тогда!")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_r, "Пионерка ушла, оставив меня одного.")
    $ Fl.say(Fl_r, "Ей не привыкать, со мной такое постоянно. Я не мог заставить себя чувствовать рядом с ней в полной безопасности.")
    $ Fl.say(Fl_r, "За это время мне удалось узнать её получше. Она даже втянула меня на пару дней в обычную повседневную суматоху.")
    $ Fl.say(Fl_r, "Правда закончилось это тем что нас заперли в разных домах и не выпускали наружу, чтобы мы ещё какой пакости не сделали. А это мы могли - то столовую взломали ночью, то генду разукрасили, устроили концерт посреди ночи и т.д.")
    $ Fl.say(Fl_r, "Но чудачка она знатная.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(4)
    scene bg Fl_black with Fl_flash


    $ Fl.DayTime("night", "night")
    $ Fl.Pause(2.0)
    scene bg Fl_int_house_of_mt_night2 with Fl_effect_1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Я лежал на кровати в доме Вожатой. {w}После нашего баловства, Вожатая нас расселила, Импостер осталась у нас, а я переехал к Вожатой.")
    $ Fl.say(Fl_r, "На часах перевелало за полночь. Вожатая куда-то вышла, вероятнее всего в уборную.")
    $ Fl.say(Fl_r, "Я же сделав вид спящего, подождал когда она уйдёт и вновь принялся просто лежать.")
    $ Fl.say(Fl_r, "Но неожиданно в окно постучали.")
    $ Fl.say(Fl_th, "Кого это к нам занесло?")
    $ Fl.say(Fl_r, "Я встал с кровати, включил устройство и подошёл к окну.")
    $ Fl.say(Fl_th, "Что эта дура забыла в такое время и почему не спит до сих пор?!", _with=hpunch)
    $ Fl.say(Fl_r, "Справа из окна на меня глазели два хитрющих глаза с привычной для меня ухмылкой.")
    $ Fl.say(Fl_q6, "Ничего интересного.")
    $ Fl.say(Fl_r, "Сказал я вслух и собирался было лечь обратно.")
    $ Fl.say(Fl_liz, "Эй, ты чего игноришь?! Открой окно!")
    $ Fl.say(Fl_q6, "Спать иди, хватит уже с меня приключений. И почему бы тебе не зайти через дверь?")
    $ Fl.say(Fl_liz, "Она закрыта!")
    $ Fl.say(Fl_th, "Точно мы ведь наказаны. {w}Импостера вожатая решила не заперать, а вот меня на ночь она наоборот заперает. Даже сейчас ушла и закрыла дверь на замок.")
    $ Fl.say(Fl_q6, "Значит иди спать.")
    $ Fl.say(Fl_r, "Я лёг обратно, но стуки в окно не прекращались.")
    $ Fl.say(Fl_th, "Ну всё, хана тебе!", _with=vpunch)
    $ Fl.say(Fl_r, "Резко подскочив, я отпёр ставни и распахнул окно.")
    $ Fl.say(Fl_r, "Но не успел, я что либо предпренять, как Импостер залезла внутрь.")

    show liz nude discontent2 with Fl_dissolve1

    $ Fl.PlayMusic("Fl_niles_blues", 1, 4)
    $ Fl.say(Fl_r, "Голая{mn}")
    $ Fl.say(Fl_q6, "Ты что сдурела совсем?! Ты так по лагерю шла?!")
    if persistent.Fl_dictionary_15 == False:
        $ Fl.PodskDict()
    $ persistent.Fl_dictionary_15 = True
    $ Fl.say(Fl_th, "Ты {i}эксгибициониистка{/i} что ли?!")
    $ Fl.say(Fl_th, "Ладно при мне раздеваться, но разгуливать голышом{mn}")

    show liz nude me with Fl_dissolve1

    $ Fl.say(Fl_liz, "Ну я легла спать, а потом никак уснуть не могла...")

    show liz nude smile with Fl_dissolve1

    $ Fl.say(Fl_liz, "А потом решила к тебе зайти, как знала, что не спишь!")
    $ Fl.say(Fl_q6, "Это тут причём?! Я спросил, почему ты сейчас голышом передо мной!")

    show liz nude me with Fl_dissolve1

    $ Fl.say(Fl_liz, "Да не кричи ты на меня. Я же всегда сплю голая, вот и не спалось мне говорю же.")
    $ Fl.say(Fl_r, "Я прикрыл лицо рукой.")
    $ Fl.say(Fl_th, "Это <п*здец>...")

    hide liz nude me with Fl_dissolve1

    $ Fl.say(Fl_liz, "Ооо, так вы тут с вожатой развлекались без меня.")
    $ Fl.say(Fl_q6, "С чего вдруг такие выводы?")
    $ Fl.say(Fl_r, "У меня уже не было сил бороться с ней.")
    $ Fl.say(Fl_liz, "Ну и сиськи у неё, как корова!")
    $ Fl.say(Fl_r, "Я поднял взгляд, Импостер как ни в чём не бывало осматривала лифчик вожатой и возмущалась.")
    $ Fl.say(Fl_q6, "Вожатая может прийти в любой момент, ты это понимаешь?")
    $ Fl.say(Fl_liz, "Аахахах, так вот как тебя пробить на эмоции?")
    $ Fl.say(Fl_th, "Я и правда слишком эмоционально себя веду. {w}Но я не хочу лишний раз вырезать целый лагерь. Такая выходка станет последней каплей вожатой.")
    $ Fl.say(Fl_liz, "Как думаешь мне идёт?")
    $ Fl.say(Fl_r, "Импостер приложила бюстгалтер вожатой к груди, одновременно позируя передо мной.")
    $ Fl.say(Fl_q6, "Ты изде{break}")
    $ Fl.say(Fl_mvv, "Вы{mn2} Вы{mn}")
    $ Fl.say(Fl_mvv, "ВЫ ОБА ВООБЩЕ АХРЕНЕЛИ?!", _with=hpunch)
    $ Fl.say(Fl_r, "Как по закону жанра неожиданно в этой сцене появилась вожатая.")
    $ Fl.say(Fl_th, "Собственно о чём я и предупреждал...")
    $ Fl.StopMusic(4)
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_flash


    $ Fl.DayTime("day", "day")
    $ Fl.Pause(2.5)
    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 4)
    scene bg Fl_ext_boathouse_day
    show Fl_light_c
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Конец этой забавной истории - Импостер просто схватила меня и совершила прыжок в другой лагерь.")
    $ Fl.say(Fl_th, "Резни удалось избежать. {w}В тот момент я готов был убить каждого кто меня достал и её в том числе!")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_th, "Интересно, как в другом лагере Импостер смогла раздобыть точно такой же наряд, как у неё?")
    $ Fl.say(Fl_th, "Скорее всего она тоже полностью не расскрывает свои тайны. {w}Так что недоверие - это у нас взаимно.")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_r, "Перерыв на воспоминания подошёл к концу и я решил идти к своей цели до конца.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause(3.5)
    scene bg Fl_ext_boathouse_sunset
    show Fl_light_c
    with Fl_dissolve3

    $ Fl.Pause(4.5)
    $ Fl.PlayAmbience("Fl_camp_center_night", 1, 7)
    $ Fl.DayTime("night", "night")
    scene bg Fl_ext_boathouse_night
    show Fl_dust_full
    with Fl_dissolve3


    $ Fl.Pause(2.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Весь день ушёл на бессмысленные попытки совершить прыжок в другой лагерь.")
    $ Fl.say(Fl_th, "Просто представить как я переношусь в другое место? {w}Как всё пространоство меняется? {w}Это ведь несложно?")
    $ Fl.say(Fl_th, "Тогда почему у меня <с*ка> ничего не получается?!", _with=hpunch)
    $ Fl.say(Fl_r, "Я был измотан, хотелось просто что-то сломать, убить себя чтобы перезапустить цикл, тем самым прокричать: «Вот чем вам не перемещение?!».")
    $ Fl.say(Fl_r, "Я молча сполз по стене на землю.")
    $ Fl.say(Fl_liz, "Снова ты здесь.")

    show liz pioner smile with Fl_dissolve1

    $ Fl.say(Fl_q6, "Я никуда и не уходил.")
    $ Fl.say(Fl_r, "Сейчас меньше всего на свете, хотелось видеть эту извращенку.")

    show liz pioner surprise2 with Fl_dissolve1

    $ Fl.say(Fl_liz, "Ты просто целый день тут сидел?")
    $ Fl.say(Fl_q6, "Тебе то какое дело?")

    show liz pioner3 angry with Fl_dissolve1

    $ Fl.say(Fl_liz, "Только не говори, что ты тренировал прыжки в одиночку?")
    $ Fl.say(Fl_r, "Злость накипала, меня начинало накрывать и сносить голову. Желание выместить злость было слишком сильным, поэтому я просто промолчал.")

    show liz pioner3 angry2 with Fl_dissolve1

    $ Fl.say(Fl_liz, "Ты совсем идиот?! {w}Я же тебя предупреждала, что это слишком опасно!")
    $ Fl.say(Fl_q6, "Зачем оно тебе? Ты же видишь, что это бесполезно. {w}Я буду первым сказителем, что не может совершать прыжки, здорово же!")

    show liz pioner me with Fl_dissolve1

    $ Fl.say(Fl_liz, "Скажу прямо, у тебя выбора нет. Можешь бросить попытки и сидеть в этом лагере, но тогда ты никогда не найдёшь бога этого мира и Кукловода в том числе.")
    $ Fl.say(Fl_liz, "Или же наконец-то поверишь во всей этот бред, что тебя окружает. И сможешь осуществить свои цели.")
    $ Fl.say(Fl_r, "Гнев начал утихать, а рассудок возвращался в норму.")
    $ Fl.say(Fl_q6, "Поверить в бред...")

    show liz pioner scorn with Fl_dissolve1

    $ Fl.say(Fl_liz, "Взгляни вокруг. Здесь всё иллюзия и обман. Только мы настоящие.")
    $ Fl.say(Fl_liz, "А теперь взгляни на это с точки зрения сказителя, ничего ведь не меняется, всё кажется таким же бредом, разве нет?")
    $ Fl.say(Fl_q6, "Понятно. Мы и есть мироздатели.")

    show liz pioner2 smile2 with Fl_dissolve1

    $ Fl.say(Fl_liz, "Ну раз ты всё понял, то пошли. Сегодня было очень жарко, надо бы в баню сходить отмыться.")
    $ Fl.say(Fl_th, "Не могу понять, почему она настолько беззаботная. То речь умную толкает с серьёзным настроем, то сразу переключается на что-то левое с довольной улыбкой.")

    show liz pioner smile with Fl_dissolve1

    $ Fl.say(Fl_liz, "Тебе тоже не помешает, весь день тут на солнце стоял.")
    $ Fl.say(Fl_q6, "Пойдём.")
    $ Fl.say(Fl_liz, "А тебя с каждым разом всё легче уговорить.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(4.0)
    scene bg Fl_ext_bathhouse_night
    show Fl_dust_full
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.PlayMusic("Fl_day_2", 1, 6)
    $ Fl.say(Fl_r, "Старая, но крепкая избушка радостно нас встретила. {w}Сама баня находилась на опушке леса.")
    $ Fl.say(Fl_r, "Баней можно было пользоваться только вечером или ночью. Обычно в такое время вожатые отправляют парней из старших отрядов топить баню.")
    $ Fl.say(Fl_r, "У меня же с этим местом дурные воспоминания. Оно было предозначено для идеального насилия с пионерками ночью.")
    $ Fl.say(Fl_r, "Аж передёрнуло.")
    $ Fl.say(Fl_r, "Мы же не стали тянуть и зашли внутрь.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(4)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(2.0)
    scene bg Fl_int_bathhouse with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Внутри оказалось очень душно. Как не странно...")
    $ Fl.say(Fl_r, "Пока я витал в облаках, Импостер уже почти сняла всю одежду.")
    $ Fl.say(Fl_th, "Ей только дай повод...")
    $ Fl.say(Fl_liz, "Ну ты долго? Или ты прям в одежде решил принять душ?")
    $ Fl.say(Fl_r, "Я не разделял рвения раздеваться при девушке, особенно при такой.")
    $ Fl.say(Fl_liz, "Или ты стесняяяешься?")
    $ Fl.say(Fl_th, "Хотя какая мне разница, всё равно чувства стыда мне незнакомо.")
    $ Fl.say(Fl_r, "Быстрыми движениями я оголил своё тело, но трусы остались на мне.")
    $ Fl.say(Fl_liz, "Ты ни разу в бане не был? Надо всю одежду снять и это не обсуждается!")
    $ Fl.say(Fl_q6, "А ты я погляжу так и ждёшь когда я разденусь?")
    $ Fl.say(Fl_liz, "Да не стыдись ты размера, это ведь не главное!")
    $ Fl.say(Fl_th, "Как будто меня это волнует.")
    $ Fl.say(Fl_r, "Последний элемент одежды полетел в кучку.")
    $ Fl.say(Fl_liz, "И чего ты тогда стеснялся, не понимаю...")
    $ Fl.say(Fl_r, "Взгляд пионерки зафиксировался в одной точке, не трудно догадаться в какой именно.")
    $ Fl.say(Fl_q6, "Иди к чёрту!")
    $ Fl.say(Fl_r, "После чего я схватил полотенце и прошёл внутрь.")
    $ Fl.say(Fl_r, "Импостер проследовала за мной, попутно говоря, что-то по типу: «Да ладно тебе, не обижайся» и т.д..")
    $ Fl.say(Fl_r, "Я же развалился на досках и откинул голову назад.")
    $ Fl.say(Fl_th, "И правда здорово в бане. Почему я раньше просто так сюда не ходил?")

    $ Fl.Pause(4.0)
    $ Fl.say(Fl_r, "Полностью раслабиться не удалось, Импостер постоянно косилась на меня.")
    $ Fl.say(Fl_q6, "Что?")
    $ Fl.say(Fl_liz, "Это после встречи с богом?")
    $ Fl.say(Fl_r, "Задала мне вопрос она и взглядом указала на область груди, где красовался огромный шрам.")
    $ Fl.say(Fl_q6, "Ага, эта стерва пробила мне грудную клетку, не понятно почему я до сих пор жив.")
    $ Fl.say(Fl_liz, "Ты спрашивал про какого-то доктора П{mn} П{mn}")
    $ Fl.say(Fl_q6, "Парки.")
    $ Fl.say(Fl_liz, "Что за идиотское прозвище?")
    $ Fl.say(Fl_q6, "Хех, тут я с тобой согласен. Но мне кажется просто он типичный безумный учёный, таким простительно.")
    $ Fl.say(Fl_liz, "Это точно.")
    $ Fl.say(Fl_r, "Девушка улыбнулась мне в ответ.")
    $ Fl.say(Fl_liz, "Получается то что ты живой, заслуга этого доктора?")
    $ Fl.say(Fl_q6, "Что-то типо того. Не знаю как, но он меня с того света вытащил.")
    $ Fl.say(Fl_liz, "С кем ты только не пересекался. Ты прям магнит для чудаков.")
    $ Fl.say(Fl_q6, "Ага. Но тогда бы тебя не встретил.")
    $ Fl.say(Fl_liz, "И что это должно значить? Ты считаешь меня странной?!")
    $ Fl.say(Fl_q6, "Ну я просто так не раздеваюсь перед незнакомцем и не предлагаю интим услуги.")
    $ Fl.say(Fl_r, "Съязвил я, после чего сразу получил ответку.")

    $ Fl.AttackMaster(True)
    $ Fl.say(Fl_r, "Импостер кинула в меня мыло и закричала.")
    $ Fl.say(Fl_liz, "Да как ты мог такое сказать, козёл?!", _with=hpunch)
    $ Fl.say(Fl_r, "Почему то мне это подняло настроение. Очередная глупая сценка, но мне было весело.")
    $ Fl.say(Fl_liz, "Не ценит меня...")
    $ Fl.say(Fl_r, "Импостер надула щёки и отсела от меня подальше.")
    $ Fl.say(Fl_th, "Если убрать тот факт что она сказитель и спокойно может убить кого захочет из-за скуки, то я бы посчитал её обычной девушкой. Со своими приколами конечно, но обычной заботливой и хорошей девушкой.")
    $ Fl.HideScreens(_with=Fl_dissolve1)

    $ Fl.Pause(4.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_q6, "Кстати.")
    $ Fl.say(Fl_liz, "Я с тобой не разговариваю!")
    $ Fl.say(Fl_th, "Серьёзно? Ещё обижается?")
    $ Fl.say(Fl_q6, "Снова ведёшь себя как дура?")
    $ Fl.say(Fl_liz, "Это и близко не похоже на извинения!")
    $ Fl.say(Fl_q6, "Ладно пофиг.")
    $ Fl.say(Fl_liz, "Пофиг?! {w}Как можно быть таким чёрствым?!", _with=hpunch)
    $ Fl.say(Fl_th, "Просто мне лень подыгрывать твоему спектаклю...")
    $ Fl.say(Fl_liz, "Ладно, что ты хотел сказать? Но я обижена так и знай!")
    $ Fl.say(Fl_th, "Быстро же ты сдалась.")
    $ Fl.say(Fl_q6, "Что мы планируем делать дальше? Просто жить обычной жизнью в лагере и иногда выбираться на тренеровки по прыжкам?")
    $ Fl.say(Fl_liz, "А что ты ещё предлагаешь? {w}Всё равно искать в лагере ответы бессмысленно.")
    $ Fl.say(Fl_liz, "Ответы нужно искать в лагерях находящихся в области опасного сектора или в лагерях других сказителей. Здесь ничего кроме компьютера с неизвестным паролем нет.")
    $ Fl.say(Fl_q6, "Ты знаешь про компьютер?")
    $ Fl.say(Fl_liz, "Ну конечно. Я уже столько лагерей верх дном перевернула в поисках ответов, ты даже не представляешь.")
    $ Fl.say(Fl_liz, "Этот лагерь я тоже весь осмотрела - ничего, пусто.")
    $ Fl.say(Fl_q6, "Получается в каждом лагере что мы были, ты искала ответы?")
    $ Fl.say(Fl_liz, "А ты думал, что я просто развлекаюсь с куклами и в столовой живу?")
    $ Fl.say(Fl_q6, "Ну да.")
    $ Fl.say(Fl_liz, "Ну всё! Я с тобой теперь точно не разговариваю!")
    $ Fl.say(Fl_r, "В очередной раз Импостер обиделась на меня. Хотя мне было не понять, как можно обижаться из-за ерунды. Может просто я перестал понимать чувства других...")
    $ Fl.say(Fl_th, "Всё это время она искала ответы вместе со мной. {w}Может она и правда не имеет никаких скрытых мотивов и решила помочь мне?")
    $ Fl.say(Fl_th, "Не хочу сближаться ни с кем. Но сейчас будет глупо брезгать ей, когда она столько для меня делает, даже если я об этом не просил.")
    $ Fl.say(Fl_q6, "Извини.")
    $ Fl.say(Fl_liz, "Что ты сейчас сказал? Мне же не послышалось?")
    $ Fl.say(Fl_r, "И снова эта ухмылка на её лице.")
    $ Fl.say(Fl_liz, "Можешь ещё раз повторить?")
    $ Fl.say(Fl_r, "Я лишь вздохнул и подошёл к душу, чтобы наконец-то помыться.")
    $ Fl.StopMusic(4)

    $ Fl.Pause(3.0)
    $ Fl.say(Fl_r, "После долгого раслябляющего душа, я хотел было идти на выход, но красноволосая суккубша решила просто так это не оставлять.")

    $ Fl.PlayMusic("Fl_newolgatheme", 1, 4)
    $ Fl.say(Fl_liz, "Яяян, хочешь я тебе спинку потру?")
    $ Fl.say(Fl_q6, "Мы тебе в аниме что ли?")
    $ Fl.say(Fl_liz, "Да ладно тебе, у тебя спина широкая, а я хочу всего лишь помочь.")
    $ Fl.say(Fl_th, "Знаю я твою помощь...")
    $ Fl.say(Fl_q6, "Ладно, не отстанешь же.")
    $ Fl.say(Fl_r, "Я сел на стул, а Импостер радостная встала у меня за спиной с мочалкой.")
    $ Fl.say(Fl_th, "Если она что-то выкинет - я её прибью!")
    $ Fl.say(Fl_r, "Неожиданно спиной я ощутил что-то мягкое. И это что-то явно не мочалка...")
    $ Fl.say(Fl_q6, "Сиськи убери.")
    $ Fl.say(Fl_liz, "Какая разница чем спину тереть.")

    $ Fl.AttackScreens()
    $ Fl.say(Fl_r, "В тот же миг, я оказался за спиной Импостер и ударил по голове.")
    $ Fl.say(Fl_liz, "Ай! Больно ведь!", _with=vpunch)
    $ Fl.say(Fl_q6, "Жду тебя дома.")
    $ Fl.say(Fl_r, "Теперь была моя очередь сделать вид, что я обиделся и молча уйти. Для профилактики, чтобы не расслаблялась.")
    $ Fl.StopMusic(3)
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(8.0)
    $ Fl.DayTime("rain", "rain")

    $ Fl.PlayMusic("Fl_atmosphere", 1, 6)
    scene bg Fl_bynker_pr
    show Fl_dust_full
    show Fl_prolog_dream 
    with Fl_dissolve3
    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "В богом забытом месте эхом разносились шаги неизвестного.")
    $ Fl.say(Fl_r, "Наверное затхлый воздух и серые стены этого места не выдержит никто. {w}Никто кроме фигуры в белом халате.")
    $ Fl.say(Fl_unk2, "Подождите!")
    $ Fl.say(Fl_r, "Фигура замерла.")
    $ Fl.say(Fl_unk1, "Что-то случилось?")
    $ Fl.say(Fl_r, "Вторая взволнованная фигура остановилась и продолжила нарушать тишину подземелья.")
    $ Fl.say(Fl_unk2, "Пару минут назад мы обнаружили её. Она была замечена в 3 секторе.")
    $ Fl.say(Fl_unk1, "Отличные новости! Вы закончили настраивать оборудование?")
    $ Fl.say(Fl_unk2, "Да{mn} Но нам не на ком испытать его. Поэтому мы не знаем, как оно поведёт себя во время эксперимента.")
    $ Fl.say(Fl_unk1, "Так даже лучше, вот и испробуем его на ней.")
    $ Fl.say(Fl_r, "Атмосфера накалялась, тот кому принадлежал голос, был слишком беззаботен и не испытвал ни капельки страха. Казалось само жуткое место находится в его власти.")
    $ Fl.say(Fl_unk2, "Нам стоит эту новость передать ____?")
    $ Fl.say(Fl_unk1, "Нет, я сам ему передам. Лучше всё подготовьте для процедуры и найдите ремни покрепчее.")
    $ Fl.StopMusic(5)
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve3


    $ Fl.Pause(6.0)
    $ Fl.DayTime("day", "day")
    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 4)
    scene bg Fl_ext_boathouse_day
    show Fl_light_c
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Шестой цикл проживания с Импостер подходил к концу. Тренировки продолжались и сегодня не стало исключением.")
    $ Fl.say(Fl_liz, "Так, закрой глаза и представ...")
    $ Fl.say(Fl_q6, "Да-да, я помню.")
    $ Fl.say(Fl_r, "Девушка взяла меня за руку.")
    $ Fl.ShowBlink()
    $ Fl.Pause(1.0)

    $ Fl.say(Fl_th, "Представить что всё вокруг меняется. {w}Представить будто я переношусь в другое место. Зацепиться за то, что может измениться, заставить всё вокруг выглядеть иначе...")
    $ Fl.say(Fl_th, "Давай, у тебя должно получиться!")

    $ Fl.Pause(4.0)
    $ Fl.PlaySound("Fl_vzhuh", 1, 0, False)
    $ Fl.Pause(2.0)
    with hpunch
    $ Fl.say(Fl_r, "Неожиданно пионерка набросилась на меня в объятья.")
    $ Fl.say(Fl_q6, "Ты что тво{break}")
    $ Fl.say(Fl_liz, "У ТЕБЯ ПОЛУЧИЛОСЬ!", _with=vpunch)
    $ Fl.say(Fl_th, "Что?..")

    scene bg Fl_ext_library_day
    show Fl_light_c
    $ Fl.ShowUnblink()

    $ Fl.Pause(2.5)
    $ Fl.say(Fl_r, "Я не мог поверить своим глазам... {w}Всё вокруг изменилось, вместо пристани перед глазами красовалось здание библиотеки.")
    $ Fl.say(Fl_th, "Получилось{mn2}")
    $ Fl.say(Fl_liz, "А я говорила, что у тебя всё получится!")
    $ Fl.say(Fl_q6, "Нет это бред какой-то...")
    $ Fl.say(Fl_liz, "Тогда попробуй ещё раз и сам увидишь!")

    $ Fl.ShowBlink()
    $ Fl.Pause(2.0)
    $ Fl.PlaySound("Fl_vzhuh", 1, 0, False)

    scene bg Fl_ext_no_bus
    show Fl_light_c
    $ Fl.ShowUnblink()

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_r, "Пейзаж вновь изменился. Стоя у ворот лагеря меня начала переполнять. {w}Радость?")
    $ Fl.say(Fl_q6, "Получилось{mn} Получилось!")
    $ Fl.say(Fl_liz, "Теперь ты убедился?")

    $ Fl.ShowBlink()
    $ Fl.say(Fl_r, "Я вновь зажмурил глаза.")
    $ Fl.say(Fl_liz, "Ты опять планируешь совершить прыжок?!")
    $ Fl.say(Fl_liz, "Ян, стой!")
    $ Fl.say(Fl_r, "Но слова пролетали мимо ушей, я не мог поверить что смог сделать невозможное. Словно ребёнок я бежал похвастаться матери тому чему научился.")

    $ Fl.PlaySound("Fl_vzhuh", 1, 0, False)
    $ Fl.Pause(2.5)
    $ Fl.PlaySound("Fl_vzhuh", 1, 0, False)
    $ Fl.Pause(2.0)
    $ Fl.PlaySound("Fl_vzhuh", 1, 0, False)

    scene bg Fl_ext_boathouse_day
    show Fl_light_c
    $ Fl.ShowUnblink()
    $ Fl.Pause(2.0)
    $ Fl.say(Fl_q6, "Как же это круто!")
    $ Fl.say(Fl_r, "Но в глазах Импостера отражалось всё иначе, она смотрела на меня с тревогой.")

    $ Fl.PlaySound("Fl_head_heartbeat", 1, 2, True)
    show Fl_rage with Fl_dissolve1

    $ Fl.say(Fl_r, "Неожиданно на меня накатила адская головная боль, тело стало ватным.")
    $ Fl.say(Fl_liz, "Ян!")

    show Fl_vignette with Fl_dissolve2
    $ Fl.say(Fl_th, "Что со мной?")
    $ Fl.say(Fl_r, "Я не мог больше стоять на ногах, моё тело окончательно перестало меня слушать.")

    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    scene bg Fl_black with vpunch
    $ Fl.HideUnblink()
    $ Fl.say(Fl_th, "Больно{mn} {w}Голова расскалывается.")
    $ Fl.say(Fl_r, "Импостер что-то мне кричала, но каждое слово доставляло мне ужасную боль.")
    $ Fl.say(Fl_th, "Хочу спать{mn2}")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(4)


    $ Fl.Pause(5.5)
    $ Fl.DayTime("night", "night")
    scene bg Fl_int_aidpost_lamp with Fl_dissolve3
    $ Fl.Pause(2.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Моё пробуждение оказалось в рамках койки, местного медпункта.")
    $ Fl.say(Fl_r, "За окном было темно, что означало - я про лежал целый день здесь, а может и не день...")
    $ Fl.say(Fl_th, "Как я здесь оказался?")
    $ Fl.say(Fl_r, "Я хотел было встать...")
    with Fl_flash

    $ Fl.PlayMusic("Fl_super_vk", 1, 5)
    $ Fl.say(Fl_r, "Но получил сильную подщёчину.")
    $ Fl.say(Fl_liz, "Идиот! Ненавижу!")
    $ Fl.say(Fl_th, "И ты здесь...")
    $ Fl.say(Fl_r, "Я хотел уже съязвить, что делаю в принципе на регулярной основе. Но лицо девушки заставило меня замолчать. Оно было красное, злость через которую пробивалась печаль и радость одновременно.")
    
    $ Fl.AttackScreens()
    $ Fl.say(Fl_r, "Импостер кинулась в объятия.")
    $ Fl.say(Fl_liz, "Почему ты никогда меня не слушаешь?..")
    $ Fl.say(Fl_liz, "Я же просила тебя остановиться.")
    $ Fl.say(Fl_r, "И тут я вспомнил, как без остановки совершал прыжки, после чего свалился и отключился.")
    $ Fl.say(Fl_th, "Это она меня доставила в медпункт?")
    $ Fl.say(Fl_th, "Сколько она тут просидела...")
    $ Fl.say(Fl_liz, "Ненавижу тебя. {w}Ненавижу когда всем плевать, на то что я делаю. {w}Почему я должна переживать за...")
    $ Fl.say(Fl_q6, "С-спасибо.")
    $ Fl.say(Fl_r, "Как давно я не говорил это простое, но столь важное слово?")
    $ Fl.say(Fl_r, "Я положил ладонь на макушку девушки.")
    $ Fl.say(Fl_r, "Она хотела что-то сказать, наверное даже в очередной раз отругать, но вместо этого только крепче меня сжала и подтянула голову к моей ладони.")
    $ Fl.HideScreens(_with=Fl_dissolve1)

    $ Fl.Pause(4.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_q6, "Ну всё хватит, вставай.")
    $ Fl.say(Fl_r, "На моё удивление пионерка послушалась и не начала истерить.")

    show liz pioner me with Fl_dissolve1

    $ Fl.say(Fl_liz, "Ты же понимаешь, почему ты здесь оказался?")
    $ Fl.say(Fl_q6, "Ага. Из-за прыжков.")
    $ Fl.say(Fl_liz, "Теперь ты понимаешь, какова цена этих прыжков? {w}Наша жизненная энергия.")
    $ Fl.say(Fl_liz, "Чем больше прыжков ты за короткий период совершаешь, тем сильнее они отражаются на тебе.")
    $ Fl.say(Fl_th, "...")

    show liz pioner scorn with Fl_dissolve1

    $ Fl.say(Fl_liz, "Хотя я удивлена, что с первого раза ты перенёс аж пять прыжков. У меня больше трёх не получилось сделать.")

    show liz pioner smile with Fl_dissolve1

    $ Fl.say(Fl_liz, "Ты вообще человек?")
    $ Fl.say(Fl_q6, "Не знаю...")

    show liz pioner discontent2 with Fl_dissolve1

    $ Fl.say(Fl_liz, "Это был риторический вопрос.")

    show liz pioner smile with Fl_dissolve1

    $ Fl.say(Fl_liz, "Дурак.")

    hide liz pioner smile with Fl_dissolve1

    $ Fl.say(Fl_r, "Импостер села на край койки.")
    $ Fl.say(Fl_q6, "Сколько я здесь пролежал?")
    $ Fl.say(Fl_liz, "Недолго, до вечера всего лишь. {w}Но я думала, что после такого ты не очнёшься два дня минимум.")
    $ Fl.say(Fl_th, "Походу большое количество прыжков действительно слишком опасно.")
    $ Fl.say(Fl_q6, "Что теперь будешь делать?")
    $ Fl.say(Fl_liz, "Ты о чём?")
    $ Fl.say(Fl_q6, "Перемещаться между лагерями я научился, больше тебя ничего здесь не держит.")
    $ Fl.say(Fl_liz, "И? {w}Наши тренировки ещё не закочились между прочим!")
    $ Fl.say(Fl_liz, "Физически ты слишком силён, но стоит тебе наткнуться на сказителя у которого способность связана с контролем разума - ты проиграешь.")
    $ Fl.say(Fl_th, "Я не могу свободно сражаться с ней из-за её способности, во время сражения она заставляет меня видеть иллюзии.")
    $ Fl.say(Fl_th, "С Тихоней таких проблем нет.")
    $ Fl.say(Fl_th, "Я действительно бессилен против контроля. Во время сражения нет осознания действительно ли ты сражаешься со сказителем или иллюзий что он создал у тебя в голове...")
    $ Fl.say(Fl_liz, "Поэтому с сегодняшнего дня мы переходим на второй уровень тренировок. Научим тебя избегать контроля, чтобы ты всем жару задал!")
    $ Fl.say(Fl_q6, "{mn}")
    $ Fl.say(Fl_q6, "Что за бред?")
    $ Fl.say(Fl_q6, "Кто вообщем в здравом уме научит врага сражаться против своей же способности. Я же тогда могу запросто тебя убить!")
    $ Fl.say(Fl_liz, "Не можешь. {w}И я не считаю тебя своим врагом, не потому что считаю себя сильной, а просто ты мне друг.")
    $ Fl.say(Fl_liz, "Если ты называешь дружбу между сказителями бредом - то не забывай ты недавно поверил в бред и смог освоить прыжки!")
    $ Fl.say(Fl_th, "Почему она улыбается?..")
    $ Fl.say(Fl_r, "Я был повержен, мой мозг кипел. Хотелось кричать. И я кричал, глубоко внутри кричал от непонимания.")
    $ Fl.say(Fl_th, "Убить всех сказителей - вот моя цель. Но почему я теперь сомневаюсь?")
    $ Fl.say(Fl_liz, "Если тебе так будет легче, то я просто хочу насолить напышенным идиотам. Я буду делать то что я хочу, а не что мне прикажут.")
    $ Fl.say(Fl_th, "Снова стоит на своём.")
    $ Fl.say(Fl_liz, "И своим выбором я довольна.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(4)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(5.5)
    $ Fl.PlayAmbience("Fl_rain_vn", 1, 4)
    scene bg Fl_int_aidpost_lamp with Fl_dissolve2
    $ Fl.Pause(2.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Погода изменилась. Общение нас разлучило с потоком времени, а тем временем за окном уже тарабанил дождь.")
    $ Fl.say(Fl_liz, "Эх, время уже позднее, я рада что ты поделился многим, но пора уже спать.")
    $ Fl.say(Fl_r, "Немного информации о моих циклах и жизни - была малая плата за помощь Импостер.")
    $ Fl.say(Fl_q6, "Ты права.")
    $ Fl.say(Fl_r, "Я попытался встать, но картина перед глазами тут же расплылась.")
    $ Fl.say(Fl_th, "Ничего себе последствия после моей выходки.")
    $ Fl.say(Fl_liz, "Тебе нельзя вставать!")
    $ Fl.say(Fl_liz, "Сегодня ты ночуешь здесь, а я домой пойду.")
    $ Fl.say(Fl_r, "Ухмылка. {w}Очередная гениальная фраза.")
    $ Fl.say(Fl_liz, "Но я могу остаться если ты хочешь.")
    $ Fl.say(Fl_q6, "Ладно.")
    $ Fl.say(Fl_r, "Глаза девушки расширились.")
    $ Fl.say(Fl_liz, "Ууу, сильно тебе конечно в голову отдало после прыжков.")
    $ Fl.say(Fl_liz, "Ну раз ты не против...")
    $ Fl.say(Fl_q6, "При одном условии. Ты будешь спать в одежде.")
    $ Fl.say(Fl_r, "Пионерка, уже снимая с себя одежду, сделала обиженное лицо.")
    $ Fl.say(Fl_liz, "Ладно, импотент.")
    $ Fl.say(Fl_q6, "И когда Виола решит меня проведать?")
    $ Fl.say(Fl_liz, "Насчёт этого не волнуйся, я сказала, что сама посижу с тобой.")
    $ Fl.say(Fl_th, "Ага, а сама только что собиралась идти домой дрыхнуть.")

    $ Fl.PlaySound("Fl_switch", 1, 0, False)
    scene bg Fl_int_aidpost_night_nolight with Fl_dissolve1
    $ Fl.say(Fl_r, "Импостер легла скраю кровати, предварительно выключив свет.")
    $ Fl.say(Fl_liz, "Ян, расскажи ещё что нибудь...")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve3
    $ Fl.StopAmbience(4)


    $ Fl.Pause(6.5)
    scene bg Fl_night_sky_lager
    show Fl_dust_full
    with Fl_dissolve2
    $ Fl.PlayMusic("Fl_pacefic", 1, 5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Подходил конец десятого цикла наших совместных приключений с Импостер.")
    $ Fl.say(Fl_r, "Время пролетело незаметно, как и началось.")
    $ Fl.say(Fl_r, "За это время я стал в разы сильнее. {w}Начиналось всё с тренировок прыжков между лагерями, а закончилось избиванием меня, пока я не научился отличать контроль от реальности.")
    $ Fl.say(Fl_r, "Я очень сильно продвинулся, наверное потому что был не один?..")
    $ Fl.say(Fl_r, "Не знаю, но с Импостер я поверил в себя, наверное сама судьба подкинула такого мозговыносителя с извращенскими наклонностями.")
    $ Fl.say(Fl_r, "Я поднял руку вверх.")
    $ Fl.say(Fl_th, "За столько циклов аккамулятор не разрядился - это правда оказалась уловка чтобы держать меня на цепи. Но...")
    $ Fl.say(Fl_th, "Какая моя настоящая сила? {w}За столько циклов с Импостер и её рассказов, невольно задумался над этим вопросом.")
    $ Fl.say(Fl_liz, "Вот ты где!")
    $ Fl.say(Fl_r, "Моим размышлениям пришлось уйти на перерыв, не сказать, что я сильно и растроился.")
    $ Fl.say(Fl_q6, "Снова в столовой была?")
    $ Fl.say(Fl_liz, "Да почему ты сразу думаешь, раз меня нет рядом - значит ем?!")
    $ Fl.say(Fl_q6, "У тебя след от кефира на губах.")
    $ Fl.say(Fl_liz, "Где?")
    $ Fl.say(Fl_r, "Избавившись от улик, Импостер легла рядом.")
    $ Fl.say(Fl_liz, "Ты не всегда должен быть прав, знаешь?")
    $ Fl.say(Fl_q6, "Знаю, но кто тебя на место ещё поставит, лгунья?")
    $ Fl.say(Fl_r, "Ждать подщёчину долго не пришлось. {w}Точнее удар с ноги по ноге.")
    $ Fl.say(Fl_r, "Теперь я видел настоящие действия пионерки и слёгкость уклонился от кармы за мои слова.")
    $ Fl.say(Fl_r, "Девушке осталось лишь молча принять поражение.")
    $ Fl.say(Fl_liz, "Снова размышлял?")
    $ Fl.say(Fl_q6, "Ага, как угадала?")
    $ Fl.say(Fl_liz, "Потому что стоит тебе пропасть из виду, ты сразу сидишь с каменным лицом и что-то себе в башке придумываешь.")
    $ Fl.say(Fl_th, "Ладно один один, ответила той же монетой.")

    $ Fl.Pause(3.0)
    $ Fl.say(Fl_q6, "Спасибо, за помощь. Ты мне правда сильно помогла.")
    $ Fl.say(Fl_liz, "Ян, насчёт этого...")
    $ Fl.say(Fl_r, "Слова дрожали. {w}Хочет сказать что-то важное?")
    $ Fl.say(Fl_liz, "Если вдруг тебе придётся продолжить свой путь в одиночку, ни в коем случае не смей останавливаться. Иди только вперёд.")
    $ Fl.say(Fl_th, "С чего вдруг она о таком заговорила?")
    $ Fl.say(Fl_liz, "Ты должен дойти до конца, слышишь?")
    $ Fl.say(Fl_q6, "Само собой.")
    $ Fl.say(Fl_q6, "И к чему это? Решила меня бросить?")
    $ Fl.say(Fl_liz, "Ещё чего! {w}А кто тебе мозги на место будет вставлять?")
    $ Fl.say(Fl_th, "Да уж, мозги ты мне можешь как вставить, так и вынести.")
    $ Fl.say(Fl_liz, "Помни, все люди - дыкие звэри!")
    $ Fl.say(Fl_r, "Улыбка сама по себе проявилась на моём лице.")
    $ Fl.say(Fl_q6, "Я запомню.")

    $ Fl.Pause(2.5)
    $ Fl.say(Fl_liz, "Наши давно уехали?")
    $ Fl.say(Fl_q6, "Ага, наш отряд уехал самым последним, в обед.")
    $ Fl.say(Fl_th, "Цикл должен был обновиться как только на небе появятся первые лучи солнца. И вновь мы встретим ворота лагеря, сидя в салоне Икаруса.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(4)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(7.0)
    $ Fl.DayTime("rain", "night")
    $ Fl.PlayAmbience("Fl_camp_center_night", 1, 4)
    scene bg Fl_int_house_yan_night with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Приближался рассвет. Ещё немного и для нас наступит 11 цикл.")
    $ Fl.say(Fl_r, "Наступил бы...")
    $ Fl.say(Fl_r, "Я подошла к кровати, на которой у самой стены сжавшись в клубок спал Ян.")
    $ Fl.say(Fl_th, "Прости меня{mn}")
    $ Fl.say(Fl_th, "Я научила тебя чему смогла.")
    $ Fl.say(Fl_th, "Но{mn} Не могу остаться с тобой. Рано или поздно через меня на тебя выйдут другие.")
    $ Fl.say(Fl_th, "Не хочу чтобы ты из-за меня рисковал своей жизнью...")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_th, "Знаешь, а я ведь солгала тебе тогда.")
    $ Fl.say(Fl_th, "В тот день Тихони не было. Её труп был всего лишь иллюзией.")
    $ Fl.say(Fl_th, "Мне просто хотелось посмотреть, хватит ли тебе смелости сразиться со мной.")
    $ Fl.say(Fl_r, "На глазах начали появляться слёзы.")
    $ Fl.say(Fl_th, "Почему я плачу? {w}Что со мной не так?")
    $ Fl.say(Fl_th, "Почему мне так грустно, почему так тяжело уйти?")
    $ Fl.say(Fl_r, "До нового цикла оставались считанные минуты.")
    $ Fl.say(Fl_liz, "Прощай, Ян. Надеюсь когда-нибудь мы ещё встретимся...")
    $ Fl.HideScreens(_with=Fl_dissolve2)
    $ Fl.StopAmbience(4)
    scene bg Fl_black with Fl_dissolve3


    $ Fl.Pause(8.5)
    $ Fl.PlayAmbience("Fl_rain", 1, 3)
    scene Fl_ext_house_of_mt_rain_night_light
    show Fl_rain_hard_left
    with Fl_dissolve2
    $ Fl.PlayMusic("Fl_titr2", 1, 4)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Несмотря на сильный ливень, красный светлечок сигареты и не думал гаснуть вопреки суровому явлению природы.")
    $ Fl.say(Fl_th, "И как я до такого опустилась?")
    $ Fl.say(Fl_r, "Бросив сигарету в лужу, я подняла голову вверх.")
        
    scene Fl_sky_rain_nht with Fl_dissolve1

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_liz, "Наверное не стоило его оставлять одного...")
    $ Fl.say(Fl_r, "Капли дождя приятным холодком обжигали кожу, стараясь смыть с моего лица тоску.")
    $ Fl.say(Fl_th, "Я уверена, что с ним всё будет в порядке!")
        
    scene Fl_ext_house_of_mt_rain_night_light
    show Fl_rain_hard_left
    with Fl_dissolve1
        
    $ Fl.say(Fl_liz, "Пойду лучше к платформе.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(4.0)

    scene bg Fl_train_rain
    show Fl_rain_hard_left
    with Fl_effect_6
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Поезд стоял как ни в чём не бывало. {w}Хотя его обнаружить можно довольно редко - он приходит не в каждом цикле.")
    $ Fl.say(Fl_th, "Может взять и уехать? Убежать отсюда как можно дальше!")
    $ Fl.say(Fl_r, "Мне была не свойствена печаль, но почему то именно сейчас мне было неспокойно.")
    $ Fl.say(Fl_liz, "Боже ну чего ты распереживалась так, дурёха?! {w}Влюбилась что ли?", _with=hpunch)
    $ Fl.say(Fl_r, "Я рассмеялась.")
        
    $ Fl.Pause(2.5)
    $ Fl.say(Fl_th, "Дурак он всё таки{mn}")
    $ Fl.say(Fl_th, "Надеюсь ты хоть немного будешь скучать по мне.")
    $ Fl.say(Fl_r, "Улыбка сама по себе нарисовалась на моём лице.")
    $ Fl.StopMusic(4)
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1
        
    $ Fl.Pause(5.0)

    scene bg Fl_train_rain
    show Fl_rain_hard_left
    with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Разглядывая горизонт, моё тело резко сковал ужас.")
    $ Fl.PlayMusic("Fl_Darren Curtis - It's In The Fog Part 2", 1, 4)
        
    show Fl_vignette2 with Fl_dissolve1
        
    $ Fl.say(Fl_r, "Появилось отчётливое ощущение, что сзади меня кто-то стоял. {w}Но смелости повернуться в сторону наблюдателя не было, тело не слушалось.")
    $ Fl.say(Fl_kt, "Довольно редкое явление. Дождь, так ещё поезд. {w}Ты так не считаешь?")
    $ Fl.say(Fl_r, "Я решила не отвечать гостю.")
    $ Fl.say(Fl_kt, "Не против если я присоединюсь?")
    $ Fl.say(Fl_r, "Пересилив страх, я всё же решила увидеть незванного гостя.")

    show set_pust at fleft with Fl_dissolve2
        
    $ Fl.Pause(1.5)
    $ Fl.say(Fl_th, "Кукловод?..")
    $ Fl.say(Fl_th, "Что он тут делает?")
    $ Fl.say(Fl_r, "Кукловод бросил взгляд на поезд, задумался, а после продолжил:")
    $ Fl.say(Fl_setk, "Как тебе новенький?")
    $ Fl.say(Fl_liz, "Новенький?")
    $ Fl.say(Fl_setk, "Да, Q-66, ты достаточно времени с ним провела чтобы сложить о нём своё мнение. {w}Так как он тебе?")
    $ Fl.say(Fl_th, "К чему этот допрос?!")
    $ Fl.say(Fl_liz, "Почему я должна тебе отвечать?")
    $ Fl.say(Fl_setk, "Помнишь, что я говорил всем вам?")
    $ Fl.say(Fl_liz, "Да{mn}")
    $ Fl.say(Fl_setk, "Тогда ты сама должна понимать, что сотрудничать со мной куда выгоднее.")
    $ Fl.say(Fl_setk, "Поэтому можешь мне рассказать всё что ты узнала за эти 10 циклов?")
    $ Fl.say(Fl_th, "Откуда он знает точное количество циклов что мы провели с Яном?!")
    $ Fl.say(Fl_r, "С каждой секундой паника росла. Хоть Кукловод и говорил спокойным голосом, но казалось будто каждое его слово это отсчёт до чего-то очень страшного.")
        
    $ Fl.Pause(2.0)
    $ Fl.say(Fl_th, "Я должна хоть что-то ему рассказать, иначе{mn} {w}Не знаю что иначе со мной будет.")
    $ Fl.say(Fl_liz, "Всё как ты говорил, он планирует убить каждого сказителя.")
    $ Fl.say(Fl_liz, "Странный очень и почти не разговорчивый.")
    $ Fl.say(Fl_setk, "Воот как. {w}Но почему он тебя тогда не убил?")
    $ Fl.say(Fl_liz, "Не знаю. Он слаб на самом деле, мне просто было его жалко убивать...")
    $ Fl.say(Fl_r, "Кукловод вновь молча отвернулся. На его лице не было эмоций. Сложно было понять, верит он мне или нет.")
    $ Fl.say(Fl_setk, "Про меня он что-то спрашивал?")
    $ Fl.say(Fl_liz, "Да он пытался узнать про силы каждого сказителя и больше всего интересовался тобой и Тихоней.")
    $ Fl.say(Fl_liz, "Она каждый цикл на него нападала.")
    $ Fl.say(Fl_setk, "Странно что он до сих пор тогда живой...")
    $ Fl.say(Fl_th, "Что?")
    $ Fl.say(Fl_r, "Было трудно разобрать что сказал Кукловод, его голос звучал очень тихо.")
    $ Fl.say(Fl_th, "Может не стоило упоминать Тихоню...")
    $ Fl.say(Fl_setk, "Ты узнала у него что-то про встречу с богом?")
    $ Fl.say(Fl_liz, "Нет он ничего не рассказывал про него. А бог в этом мире реально существует?")
    $ Fl.say(Fl_r, "Солгала я, но вовремя отвела от своей лжи вопросом, скосив под дурочку.")
    $ Fl.say(Fl_setk, "Да, но тебя всё равно он волновать не должен, ты же с ним никак не связана, {w}{b}иллюзия{/b}.")
    $ Fl.say(Fl_liz, "{mn2}")
    $ Fl.say(Fl_setk, "Какой силой владеет Q-66?")
    $ Fl.say(Fl_liz, "Усиление физических способностей.")
    $ Fl.say(Fl_setk, "Ясно. {w}Довольно глупая способность.")
    $ Fl.say(Fl_r, "Сказал он и посмотрел пронзительно весёлым взглядом казалось прямо в душу. Яркий жёлтый огонёк в его глазах затягивал в бездну, всё тело мякло.")
    $ Fl.say(Fl_setk, "Он ещё не научился перемещаться между лагерями?")
    $ Fl.say(Fl_liz, "Нет, так бы он скорее всего последовал за мной или уже вовсю искал Тихоню.")

    hide set_pust with Fl_dissolve1
        
    $ Fl.say(Fl_r, "Кукловод развернулся и зашагал, бросив на последок:")
    $ Fl.say(Fl_setk, "Спасибо, я узнал всё что хотел.")
    $ Fl.say(Fl_liz, "Постой!")
    $ Fl.say(Fl_r, "Он остановился и повернул голову на 30 градусов, из-за чего было видно только его губы.")
    $ Fl.say(Fl_liz, "Почему ты так сильно интересуешься им? Зачем сразу приказал его убить?")
    $ Fl.say(Fl_setk, "{mn2}")
    $ Fl.say(Fl_r, "Кукловод долго молчал, а после сильно оскалился и развенулся. {w}Я хотела заставить его ответить, но он просто, как чёрная дымка, растворился в воздухе.")
    $ Fl.say(Fl_th, "Чёрт!", _with=hpunch)
    $ Fl.say(Fl_liz, "Никогда с ним лично не встречалась...")
    $ Fl.say(Fl_r, "Мне захотелось как можно скорее покинуть это место.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1
        
    $ Fl.Pause(2.0)

    scene Fl_ext_houses_rain_night:
        Fl_run
    show Fl_rain_hard_left
    show Fl_vignette2
    with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Мне пришлось ускориться, паника не собиралась покидать меня.")
    $ Fl.say(Fl_th, "Он же ушёл, так почему у меня до сих пор чувство, что вот-вот что-то да должно случиться?!")
    $ Fl.say(Fl_r, "Я заглядывала в окна домов. Мне казалось, что за мной наблюдают из темноты.")
    $ Fl.say(Fl_liz, "Мне страшно?")

    $ Fl.StopMusic(7)
    scene Fl_ext_houses_rain_night
    show Fl_rain_hard_left
    with Fl_dissolve2

    $ Fl.say(Fl_liz, "Нет! Я же убийца в конце концов, чего я должна бояться?!", _with=hpunch)
    $ Fl.say(Fl_r, "Паника немного отступила и я перешла на ходьбу.")
    $ Fl.say(Fl_r, "Целенаправленно идти не было для меня никакого смысла, поэтому ноги сами меня повели куда захотели.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(4.0)
    scene Fl_squere_rain_night
    show Fl_rain_hard_left
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Выйдя на площадь меня ждал сюрприз. {w}Слева от Генды кто-то сидел.")
    $ Fl.say(Fl_th, "Странно обычно куклы во время дождя прячутся...")
    $ Fl.say(Fl_th, "Стоп! {w}Я столько гуляла по лагерю, но мне ни разу никто не повстречался на пути...")
    $ Fl.say(Fl_th, "Если это лагерь призрак, то кто тогда сидит на лавочке?")
    $ Fl.say(Fl_r, "Этот лагерь становится с каждой секундой всё интереснее и интереснее. Интрига больше не пугала, а наоборот заставляла меня пылать.")
    $ Fl.say(Fl_r, "Шаг. {w}Ещё один. {w}Два-три...")

    $ Fl.Pause(2.5)
    $ Fl.say(Fl_r, "Картина полностью прояснилась. Таинственным гостем оказалась пионерка с фиолетовыми хвостиками. Она молча читала книжку, полностью игнорируя дождь. Не трудно было догадать кто передо мной сидел.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause(2.0)
    scene cg Fl_un_book
    $ persistent.Fl_photo_pallery_24 = True
    show Fl_rain_hard_left
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Я подошла к Лене поближе. Отличить пионерку от Тихони трудно, поэтому нужно быть всегда настороже.")
    $ Fl.say(Fl_liz, "Что читаешь?")
    $ Fl.say(Fl_r, "Уставившись в книгу, пионерка никак не отреагировала.")
    $ Fl.say(Fl_liz, "Знаешь, в такой ливень чтение на свежем воздухе не лучшая затея. {w}Библиотекарша будет в ярости если с книгой что-то случится.")
    $ Fl.say(Fl_ln, "Сколько бы я не читала романтики, никогда не понимала любовный треугольник.")
    $ Fl.say(Fl_r, "Неожиданно заговорила Лена.")
    $ Fl.say(Fl_ln, "Почему никто не может понять, что одной из девушек будет больно. {w}Девушка, которая в конце концов будет отвергнута, а все её чувства просто растопчат, страдает.")
    $ Fl.say(Fl_ln, "Но читателю наплевать, они поддерживают в такой ситуации главную героиню. Им нет дела до второсортной героини, что тоже жаждит любви от главного героя.")
    $ Fl.say(Fl_ln, "Читателя наоборот будет раздражать, что она вертится вокруг парня. {w}А после раздражения, читатель начнёт ненавидеть девушку, что мешает развитию отношениям между главными героями.")
    $ Fl.say(Fl_ln, "Но разве она виновата, что писатель заточил её в этот треугольник, заставил любить? Страдать из-за собственных чувств?")
    $ Fl.say(Fl_r, "Пионерка встала.")
    $ Fl.HideScreens(_with=Fl_dissolve1)

    scene Fl_squere_rain_night
    show Fl_rain_hard_left
    with Fl_dissolve2
    show ln smile rain with Fl_dissolve1

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_ln, "Тебе не кажется это несправедливым?")
    $ Fl.say(Fl_r, "На меня уставился хищный взгляд зелёного оттенка, казалось внутри него была лишь пустота, но суженные зрачки заставляли его пылать.")
    $ Fl.say(Fl_th, "Тихоня...")
    $ Fl.say(Fl_r, "Из всех сказителей меня больше всего раздражал только один - Тихоня. Несностный характер, безумное вырожение лица и явные признаки шизофрении - так можно было описать этот тихий омут.")
    $ Fl.say(Fl_th, "Так и хочется прибить эту <с*чку>!")
    $ Fl.say(Fl_liz, "А говорят чтение полезно, вот как крышу снесло бедной Тихоне.")
    $ Fl.say(Fl_r, "Для пушего эффекта я покрутила пальцем возле виска.")
    $ Fl.say(Fl_r, "Пионерка усмехнулась, но моё замечание мало её волновало.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(4)
    scene bg Fl_black with Fl_dissolve1

    $ Fl.Pause(2.0)
    $ Fl.PlayMusic("Fl_inquiry", 1, 6)
    scene cg Fl_un_knife:
        subpixel True
        truecenter
        yalign 0.85
        zoom 1.26
        ease 8.5 yalign 0.1 zoom 1.0
    with Fl_dissolve2
    $ persistent.Fl_photo_pallery_25 = True

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_ln, "А теперь, как ты думаешь. Кто из нас второсортная героиня в этой истории?")
    $ Fl.say(Fl_r, "В руках Тихони появился нож.")
    $ Fl.say(Fl_r, "Казалось весь лагерь стих, размышляя над вопросом фиолетового безумия.")
    $ Fl.say(Fl_ln, "Прааавильно! {w}{b}ТЫ!{/b}")
    $ Fl.say(Fl_liz, "Думаешь? А мне кажется Ян обделил вниманием как раз таки тебя.")
    $ Fl.say(Fl_liz, "Лично у меня с ним всё хорошо.")
    $ Fl.say(Fl_r, "Звук дождя окончательно пропал, как только его заполнил дикий хохот.")
    $ Fl.say(Fl_r, "Оскал Тихони стал только шире.")
    $ Fl.say(Fl_ln, "Наивная. {w}Очевидно же, чтобы разорвать любовный треугольник нужно убрать третьего лишнего.")
    $ Fl.say(Fl_ln, "Ты думаешь, что потрясти голой задницей и своими сиськами достаточно чтобы стать главной героиней?!")
    $ Fl.say(Fl_th, "Ревнивая <с*ка>!")
    $ Fl.say(Fl_r, "Напряжение нарастало с каждой секундой. Результат этого разговора был весьма очевиден, но он как раз таки и закипал кровь в жилах.")
    $ Fl.say(Fl_liz, "Тебя продинамили, а ты сразу истерику закатываешь!")
    $ Fl.say(Fl_ln, "Знаешь, я впервые так сильно в кого-то влюбилась. И я не позволю другим отбирать моего любимого.")
    $ Fl.say(Fl_ln, "Поэтому...")
    $ Fl.StopMusic(4)

    $ Fl.say(Fl_r, "Нож в руках девушки сжался сильнее.")
    $ Fl.say(Fl_ln, "Умри, шлюха!")

    $ Fl.PlayMusicFrom("<from 66 to 265>", "Fl_snake_eyes", 1, 3)
    scene Fl_squere_rain_night:
        Fl_avtobus_move
    with vpunch
    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    $ Fl.Pause(1.0)
    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    $ Fl.AttackScreens()
    $ Fl.say(Fl_r, "Сорвавшись с цепи, Тихоня нанесла пару ударов холодным орудием.")
    $ Fl.say(Fl_th, "Быстрая...")
    $ Fl.say(Fl_r, "Ловким движением я вытащила нож и в ту же секунду отразила удар.")
    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)

    $ Fl.say(Fl_th, "Думаешь, против искажения реальности сможешь выстоять?!")
    $ Fl.say(Fl_r, "Пионерка словно прочитала мои мысли и ускорилась.")
    $ Fl.say(Fl_r, "Тихоня рассекала воздух каждым своим движением, казалось что ни одна капля дождя не попадала на неё.")
    $ Fl.say(Fl_r, "Я замахнулась.")
    $ Fl.say(Fl_r, "Увернуться от ножа аппоненту не составило труда. {w}Как никак поспеть за Тихоней невозможно, она слишком быстрая.")
    $ Fl.say(Fl_th, "Только вот нож у меня в другой руке.")
    $ Fl.say(Fl_r, "На лице расплылась ухмылка, после чего...")
    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)

    $ Fl.say(Fl_th, "Что?!", _with=hpunch)
    $ Fl.say(Fl_r, "Пионерка облизнула лезвие ножа и ухмельнулась.")
    $ Fl.say(Fl_th, "Как она могла заметить эту атаку? Я же исказила реальность!")
    $ Fl.say(Fl_ln, "Продолжим?")
    $ Fl.say(Fl_r, "Отбросив все свои размышления я сократила дистанцию.")

    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    with vpunch
    $ Fl.Pause(1.0)
    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    $ Fl.AttackScreens()
    $ Fl.say(Fl_th, "Где она?")
    $ Fl.say(Fl_r, "После безрезультатных разменов ударов, Тихоня просто исчезла с моего полезрения.")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_th, "Сзади!")
    $ Fl.say(Fl_r, "Исказив реальность, я отпрыгнула, оставив в глазах противника свою иллюзию.")
    $ Fl.say(Fl_th, "Давай убей меня, а после я снесу твою голову!")
    $ Fl.say(Fl_r, "Неожидано меня охватила паника.")
    $ Fl.say(Fl_r, "Тихоня чётко следила не за иллюзией, а за мной. {w}После чего раскрутилась и кинула нож прямо в меня.")
    $ Fl.say(Fl_th, "Что{break}")
    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.AttackScreens()
    $ Fl.Pause(1.5)

    $ Fl.say(Fl_r, "Кое-как мне удалось не лишиться головы.")
    $ Fl.say(Fl_r, "По щеке медленно стекала струя крови.")
    $ Fl.say(Fl_liz, "А я тебя недооценила!")
    $ Fl.say(Fl_ln, "А моя оценка сходится, всё как я и предполагала.")
    $ Fl.say(Fl_r, "Она улыбнулась.")
    $ Fl.say(Fl_th, "{mn}")
    $ Fl.say(Fl_liz, "Тогда ты допустила погрешность...")
    $ Fl.say(Fl_r, "Схватив нож, я в прямом смысле рассыпалась на осколки.")
    $ Fl.say(Fl_r, "Я создала иллюзию клонов.")
    $ Fl.say(Fl_th, "Попробуй угадать где настоящая!")

    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.say(Fl_liz, "Я тут!")
    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.say(Fl_liz, "Неа, не угадала.")
    $ Fl.PlaySound("Fl_hits", 1, 0, False)
    $ Fl.say(Fl_r, "Пионерка не могла засечь меня, что мне позволяло наносить град атак. Искажение реальности невозможно было победить.")
    $ Fl.say(Fl_r, "Так я считала...")
    $ Fl.say(Fl_ln, "Ахахах, ты прям как таракан, бегаешь туда сюда. Интересно если тебе отрубить голову, сколько ты сможешь прожить?")
    $ Fl.PlaySound("Fl_hits", 1, 0, False)

    show Fl_blood_eff with Fl_flash_red
    $ Fl.AttackScreens()
    $ Fl.say(Fl_th, "Больно{mn}")
    $ Fl.say(Fl_r, "Из моего левого запясьтя торчало лезвие, кончик которого находился почти у моей шеи.")
    $ Fl.say(Fl_th, "Мне её не победить, нужно уходить...")

    $ Fl.AttackScreens()
    $ Fl.say(Fl_r, "Я со всей силы отолкнула Тихоню назад.")
    $ Fl.say(Fl_r, "Лезвие ножа выскользнуло из моего запястья. В тот же миг из запястья хлынула кровь, образовав огромную лужу под ногами.")
    $ Fl.StopMusic(3)
    $ Fl.say(Fl_r, "Я рванула прочь.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black_flash with Fl_effect_6


    $ Fl.Pause(3.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_liz, "Здесь я в безопасности...")
    $ Fl.say(Fl_r, "Вокруг меня была лишь сплошная пустота. {w}Это измерение создано мной.")
    $ Fl.say(Fl_r, "Моя способность искажение реальности, я могу заставить любого видеть искажение, а самой оставаться в нормальной реальности.")
    $ Fl.say(Fl_r, "Но это место нечто иное. {w}По сути я полностью уничтожаю своё существование для других, никто не может меня видеть и чувствовать, но одновременно и для меня никто не существует.")
    $ Fl.say(Fl_r, "Создание пустоты я использую в очень редких случаях, чтобы просто выжить.")
    $ Fl.say(Fl_liz, "Почему{mn}")
    $ Fl.say(Fl_liz, "Почему моя способность не работает на ней?!", _with=hpunch)
    $ Fl.say(Fl_r, "Моя левая рука больше не функционировала, я продолжала истекать кровью.")
    $ Fl.say(Fl_liz, "Чудовище...")
    $ Fl.say(Fl_ln, "Эй! Мне вообще-то обидно!")

    show Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_liz, "Ч-чт-то{mn}")
    $ Fl.say(Fl_r, "Меня начало трясти, всё моё тело заключил в холодные объятия страх - ужас...")
    $ Fl.say(Fl_th, "Не может быть{mn}")
    $ Fl.say(Fl_r, "Мой разум отказывался верить в происходящее.")
    $ Fl.say(Fl_r, "Я медленно повернулась назад...")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    
    $ Fl.Pause(1.5)
    show ln shadow with Fl_dissolve2
    $ Fl.PlayMusic("Fl_bloodwork", 1, 6)
    $ Fl.Pause(3.0)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_ln, "Приииивет.")
    $ Fl.say(Fl_th, "Нет{mn} это не может быть, это мне просто кажется!")
    $ Fl.say(Fl_th, "Никто не может попасть в это измерение кроме меня!")
    $ Fl.say(Fl_th, "{b}НИКТО!{/b}", _with=hpunch)
    $ Fl.say(Fl_ln, "Это и была твоя скрытая сила?")
    $ Fl.say(Fl_ln, "Сбежать в страхе как брошенная псина?")
    $ Fl.say(Fl_liz, "Хахаахахах.")
    $ Fl.say(Fl_th, "Теперь я поняла! Как же я раньше не смогла до этого догадаться?")
    $ Fl.say(Fl_liz, "Хахаахахах.")
    $ Fl.say(Fl_ln, "Веселишься и без меня? Я тоже хочу присоединиться к твоему веселью.")
    $ Fl.say(Fl_liz, "Так ты невосприимчима к контролю. Вот почему Кукловод до сих пор не может тебя одолеть.")
    $ Fl.say(Fl_r, "Мой голос больше не дрожал. {w}Штиль прошёл, осталось лишь идеально кристальная водная гладь.")
    $ Fl.say(Fl_liz, "Мои иллюзии ни разу не сработали по той же причине.")
    $ Fl.say(Fl_liz, "Просто в твоей голове пустота.")
    $ Fl.say(Fl_r, "Тихоня захлопала.")
    $ Fl.say(Fl_ln, "Даааа! Вот именно, я так рада, что ты всё поняла!")
    $ Fl.say(Fl_ln, "Но как тебе эта информация теперь поможет?")
    $ Fl.say(Fl_r, "Только сильнее оскалилась Тихоня.")
    $ Fl.say(Fl_liz, "Прощай, Тихоня!")
    $ Fl.say(Fl_ln, "Что{break}")

    scene bg Fl_black with vpunch
    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    with hpunch
    $ Fl.Pause(0.7)
    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    with vpunch
    $ Fl.Pause(0.7)
    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    $ Fl.Pause(2.0)

    scene Fl_squere_rain_night
    show Fl_rain_hard_left
    with Fl_dissolve2
    $ Fl.Pause(1.5)
    $ Fl.say(Fl_r, "Пустота развеялась, продемонстрировав следующую картину.")
    $ Fl.say(Fl_r, "В свете фонарей красовалась уже давно опостылевшая площадь лагеря. Но в данный момент что-то изменилось, развеело скуку привычного места.")
    $ Fl.say(Fl_r, "Капли дождя отскакивали от поверхности, хаотично разбросанных ножей. Они не достигли своей цели. Или же...")
    $ Fl.say(Fl_r, "В самом центре стояла девушка с фиолетовыми волосами. {w}Из её тела торчало несколько ножей.")
    $ Fl.say(Fl_ln, "Вносить иллюзию в реальность?")
    $ Fl.say(Fl_ln, "Забавно{mn}")
    $ Fl.say(Fl_liz, "Если мои иллюзию не работают на тебе, то почему бы не изменить саму реальность? Создать например всё что я захочу?")
    $ Fl.say(Fl_ln, "Как жаль, что даже это не помогло.")
    $ Fl.say(Fl_r, "Тихоня выровнялась в полный рост, после чего вытащила все ножи из своего тела.")
    $ Fl.say(Fl_th, "Не попала...")
    $ Fl.say(Fl_th, "Как Ян и говорил, только удар в голову или сердце может её убить.")
    $ Fl.say(Fl_th, "Плевать, я сравняю с землёй эту пустышку.")
    $ Fl.say(Fl_ln, "Ты правда думала, что меня так просто убить?")
    $ Fl.say(Fl_ln, "{b}ДУРА!{/b}", _with=hpunch)
    $ Fl.say(Fl_r, "В ту же секунду пионерка совершила рывок. Уклониться от атаки без последствий было нереально.")
    $ Fl.say(Fl_r, "На моём лице в тот же миг расплылась ухмылка.")
    $ Fl.say(Fl_liz, "Сдохни уже пожалуйста.")

    $ Fl.StopMusic(3)
    $ Fl.AttackScreens(True)
    $ Fl.PlaySound("Fl_gun", 1, 0, False)
    $ Fl.Pause(1.5)
    $ Fl.HideScreens(_with=Fl_dissolve1)

    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    $ Fl.Pause(1.5)
    $ Fl.PlayAmbience("Fl_rain", 1, 5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Во время ливня свойственно ударить грому. {w}Но вместо оглушительного природного явления прогремел выстрел.")
    $ Fl.say(Fl_liz, "Вот и всё{mn}")
    $ Fl.say(Fl_r, "Я бросила пистолет на землю.")
    $ Fl.say(Fl_r, "Мёртвое тело Лены больше не внушало страха. И я медленно подняла свой взгляд на небо.")
    $ Fl.StopAmbience(5)
    $ Fl.Pause(1.5)

    scene bg Fl_night_sky_lager with Fl_effect_3
    $ Fl.Pause(1.5)
    $ Fl.say(Fl_r, "Погода немного прояснилась, дав звёздный час для полной луны.")
    $ Fl.say(Fl_r, "Боль утихла, а на душе было хорошо. Я никогда в жизни так не улыбалась. Но почему?")
    $ Fl.say(Fl_r, "Наверное я просто мысленно представила как он меня хвалит и восхищается моей силой...")
    $ Fl.say(Fl_th, "Я знала, что не смогу убить Тихоню ножами, поэтому сразу же готовилась к следующей атаке.")
    $ Fl.say(Fl_th, "Даже моё вмешательство в реальность не всесильное, как может показаться на первый взгляд. {w}Чтобы создать какой-то предмет мне нужно тчательно знать как он устроен и из чего состоит.")
    $ Fl.say(Fl_th, "Поэтому у меня ушло так много времени на создание пистолета. Если бы я допустила ошибку в работе механизмов и составе пуль, то сейчас не лицезрела труп Тихони.")
    $ Fl.Pause(1.5)
    $ Fl.say(Fl_th, "Я так устала, но я большая молодец!")
    $ Fl.say(Fl_th, "А мы ведь похожи! {w}Я тоже пережила встречу с двумя сильными сказителями за одну ночь!")
    $ Fl.say(Fl_liz, "Вот если в следующий раз его встречу обязательно похвастаюсь!")
    $ Fl.Pause(1.5)
    $ Fl.say(Fl_r, "Я долго любовалась звёздами, опасность больше мне не угрожала и можно было просто насладиться моментом перед прыжком в другой лагерь.")
    $ Fl.say(Fl_th, "Что-то я проголодалась{mn}")
    $ Fl.say(Fl_liz, "Решено! {w}Поем и сразу в путь.")
    $ Fl.say(Fl_liz, "Так где тут у на{break}")

    $ Fl.PlaySound("Fl_gun", 1, 0, False)
    $ Fl.Pause(2.5)
    show Fl_blood_eff with Fl_dissolve4
    $ Fl.PlaySound("Fl_head_heartbeat", 1.0, 0, True)
    $ Fl.Master(Fl_head_heartbeat)
    $ Fl.say(Fl_th, "Что?", cps=5)
    $ Fl.say(Fl_liz, "Кхе.")
    $ Fl.say(Fl_r, "Я кашлянула кровью, после чего в глазах медленно начало всё плыть.")
    $ Fl.say(Fl_ln, "Ты и правда думала, что я тебя отпушу после того как ты заигрывала с Яном?")
    $ Fl.say(Fl_r, "В голове всё перемешалось, я не могла осознать реальность. {w}Реальность что окрасилась в кровавый цвет.")
    $ Fl.say(Fl_th, "Почему она жива? {w}Я разве её не убила?")

    scene bg Fl_black with vpunch
    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    $ Fl.say(Fl_r, "Мои тело обмякло и я упала на холодный асфальт, хотя откуда мне было знать холодный он или же холодело всё внутри меня...")
    $ Fl.say(Fl_r, "Но это падение вернуло чёткость картины.")
    $ Fl.say(Fl_r, "Возле памятника стояла Тихоня с пистолетом в руке. На ней не было следов борьбы, она стояла в чистой форме, а главное сухой.")
    $ Fl.say(Fl_r, "И тут я поняла...")
    $ Fl.say(Fl_th, "Это новый клон{mn}")
    $ Fl.say(Fl_th, "Почему? {w}Один цикл - один клон?")
    $ Fl.say(Fl_th, "Тогда как?!", _with=hpunch)
    $ Fl.say(Fl_r, "Мне хотелось просто закричать от досады.")
    $ Fl.Pause(2.5)
    $ Fl.say(Fl_th, "Я проиграла{mn}")
    $ Fl.say(Fl_ln, "Почему не создашь бинт например или сверхмедицину чтобы исцелить свою рану?")
    $ Fl.say(Fl_ln, "Ах, точно! Ты же не можешь, твои мысли сейчас путаются и ничего ты создать не можешь!")
    $ Fl.say(Fl_r, "Площадь заполнил смех полный нотами садизма и удовольствия.")
    $ Fl.say(Fl_th, "Догадалась, тварь{mn}")
    $ Fl.say(Fl_ln, "Но у меня хорошие новости. {w}Я не задела важных органов. Поэтому смерть будет долгой и мучительной, скорее всего ты захлебнёшься в собственной крови.")
    $ Fl.say(Fl_r, "Смех повторился.")
    $ Fl.say(Fl_th, "Уйди уже. Оставь меня просто в покое{mn}")
    $ Fl.say(Fl_r, "Будто прочитав мои мысли, пионерка развернулась и ушла.")
    $ Fl.StopSound(2)
    $ Fl.HideScreens(_with=Fl_dissolve2)
    $ Fl.Pause(5.5)


    $ Fl.PlayMusic("Fl_important_negotiations", 1, 7)
    scene cg Fl_lisa_in_darkness_1 with Fl_dissolve3
    $ persistent.Fl_photo_pallery_23 = True
    $ Fl.ShowScreens(_with=Fl_dissolve2)
    $ Fl.say(Fl_th, "Вот и всё.")
    $ Fl.say(Fl_r, "С каждой секундой меня бросало в дрожь. {w}Очень холодно...")
    $ Fl.say(Fl_r, "Боли не было, но холод внутри. Это было ужасно и мерзко.")
    $ Fl.say(Fl_th, "Я такая наивная.")
    $ Fl.say(Fl_r, "Всю свою жизнь я была пустышкой. {w}Подделкой, что создал один человек.")
    $ Fl.say(Fl_r, "Люди часто вспоминают прошлое, цепляются за него. Но у меня его попросту не было. Я с рождения или правильнее сказать с создания была безчувственной машиной для убийств.")
    $ Fl.say(Fl_r, "Только садизм и страх других могли заполнить мою пустоту, так я могла обрести себя, заставить других знать о моём существовании.")

    $ Fl.Pause(2.5)
    $ Fl.say(Fl_r, "Но когда я встретила Яна. {w}Что-то изменилось{mn} {w}Я изменилась.")
    $ Fl.say(Fl_r, "Глядя на него, у меня появился новый выбор в жизни.")
    $ Fl.say(Fl_r, "Убийства ничего не решат, убивать ради удовольствия - просто бессмысленное занятие. Он убивал только ради мести. У него была цель...")
    $ Fl.say(Fl_r, "Все мы очень давно потеряли смысл жизни, обратились к ультранасилию, лишь бы не сойти с ума.")
    $ Fl.say(Fl_r, "Я тоже хотела найти ответы на все свои вопросы или даже покинуть это место, но существую ли я за пределами этого пионерлагеря? Иллюзия...")
    $ Fl.say(Fl_r, "Он не раздумывал, а просто шёл к целе, его жизнь потеряла смысл, но он боролся. {w}А я сдалась.")
    $ Fl.say(Fl_r, "Я хотела стать как он. В нём нашла спасение. И в первые моё сердце забилось чаще не только во время убийства.")

    scene cg Fl_lisa_in_darkness_2 with Fl_dissolve3
    $ Fl.Pause(2.0)
    $ Fl.say(Fl_th, "Не смей умирать, злюка!")
    $ Fl.say(Fl_th, "Я уверена всё у тебя получится.")

    scene cg Fl_lisa_in_darkness_3 with Fl_dissolve3
    $ Fl.say(Fl_th, "Я люблю тебя, Ян. Ты единственный кто не относился ко мне как к кукле{mn}")
    $ Fl.say(Fl_r, "Я улыбалась, боль больше меня не беспокоила. {w}Наконец-то отдых.")
    $ Fl.say(Fl_th, "Так хочется спать{mn}")
    $ Fl.say(Fl_r, "Краем глаза я заметила силуэт. Он сильно напоминал мне Яна.")
    $ Fl.say(Fl_r, "Из последних сил, я попыталась разглядеть предсмертный образ в далеке.")
    $ Fl.say(Fl_th, "Ты пришёл!")
    $ Fl.StopMusic(4)

    $ Fl.say(Fl_q6, "Так хотелось его увидеть перед смертью?")
    $ Fl.say(Fl_r, "В тот же миг глаза Яна загорелись жёлтым пламенем.")
    $ Fl.say(Fl_th, "Кукловод!")
    $ Fl.say(Fl_setk, "Угадала.")
    $ Fl.say(Fl_liz, "Ч-что тебе н-нужно?")
    $ Fl.say(Fl_setk, "У меня к тебе выгодное предложение.")
    $ Fl.HideScreens(_with=Fl_dissolve2)

    $ Fl.Pause(1.5)
    scene bg Fl_black
    show set_pust
    with Fl_dissolve2

    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve2)
    $ Fl.PlayMusic("Fl_razg_zn", 1, 5)
    $ Fl.say(Fl_setk, "Я сохраню твою жизнь, но взамен ты будешь делать всё что я тебе скажу.")
    $ Fl.say(Fl_setk, "Но предупреждаю, я парень требовательный.")
    $ Fl.say(Fl_r, "Последние слова он произнёс шёпотом.")
    $ Fl.say(Fl_liz, "Д-да пошёл т-ты!")
    $ Fl.say(Fl_setk, "Что ж{mn} Очень жаль.")
    with hpunch

    $ Fl.say(Fl_r, "В ту же секунду моё тело подлетело.")
    $ Fl.say(Fl_r, "Я висела в воздухе, мои руки и ноги приняли положение, как на распятие креста.")
    $ Fl.say(Fl_setk, "Тебе не показалось странным, что ты до сих пор жива?")
    $ Fl.say(Fl_r, "Спросил Кукловод и покосился на вверх.")
    $ Fl.say(Fl_r, "Вокруг меня свисали тонкие светящиеся нити.")
    $ Fl.say(Fl_th, "Что это такое?!")
    $ Fl.say(Fl_setk, "Какой смысл был в предательстве? Я же ведь предупреждал, что будет если посмеете меня ослушаться.")
    $ Fl.say(Fl_r, "Тут меня словно током ударило. Всё сошлось: ответы, нити.")
    $ Fl.say(Fl_th, "Получается тогда, он даже меня не слушал. Он просто рылся в моей голове чтобы получить ответ на свой вопрос.")
    $ Fl.say(Fl_liz, "Теперь понятно почему тебя прозвали Кукловодом. {w}Ты играешься с нами как с куклами.")
    $ Fl.say(Fl_liz, "Можешь контролировать тело, разум, заставлять выполнять приказы даже если не хотим.")
    $ Fl.say(Fl_liz, "Это ты мне хотел предложить за мою жизнь? {w}Чтобы я стала твоей куколкой?")
    $ Fl.say(Fl_r, "Но Кукловод не ответил. Он отвернулся.")
    $ Fl.say(Fl_setk, "Ты хотя бы поняла, почему проиграла Тихоне?")
    $ Fl.say(Fl_liz, "О чём ты?")
    $ Fl.say(Fl_setk, "Неудивительно, что кукле вроде тебя сложно думать самой.")
    $ Fl.say(Fl_liz, "Заткнись!", _with=hpunch)
    $ Fl.say(Fl_setk, "Прости прости, ты же не любишь когда к тебе так обращаются, иллюзия.")
    $ Fl.say(Fl_r, "Внутри меня начинало всё закипать, злость переполняла меня.")
    $ Fl.say(Fl_liz, "Проиграла и проиграла, что с того? Не зря же она номер 2!")
    $ Fl.say(Fl_r, "Кукловод ухмыльнулся. Он этого и ждал - увидеть в моих глазах гнев.")
    $ Fl.say(Fl_setk, "Наверное ты как и остальные, думаете что способность Тихони это простые клоны?")
    $ Fl.say(Fl_setk, "Отчасти это правда, она способна создавать множество кукол. Если я актёр этого театра, то она как раз отвечает за реквизит.")
    $ Fl.say(Fl_th, "Что он несёт?")
    $ Fl.say(Fl_setk, "Тебя ведь удивило, откуда взялся второй клон в одном цикле?")
    $ Fl.say(Fl_liz, "Да, но я уже догадалась, что она специально вбила в мысль всем, что может создавать один клон в цикле.")
    $ Fl.say(Fl_setk, "Дааа, это так. Жаль только ты такая же дура, как и Q-66.")
    $ Fl.say(Fl_th, "Да сколько можно уже?!")
    $ Fl.say(Fl_liz, "Удиви почему!")
    $ Fl.say(Fl_setk, "Он же тебе рассказывал, как мы с ним познакомились. И в том цикле, до встречи со мной, на Q-66 напал страшный клон Тихони. {w}А теперь подумай, если он её убил, тогда почему он видел Тихоню со мной?")
    $ Fl.say(Fl_liz, "{mn}")
    $ Fl.say(Fl_setk, "Дошло на конец?")
    $ Fl.say(Fl_setk, "Вы сами себе внушили эту мысль, а Тихоня только подыграла.")
    $ Fl.say(Fl_setk, "И на последок, клонами Тихони нельзя контролировать, собственно поэтому ни я, ни ты, никто не может управлять её разумом и наши силы не работают на клонах.")
    $ Fl.say(Fl_liz, "{mn}")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_liz, "Мне вот интересно. Ты так охотишься за Яном{mn} Тебе ведь известно какая у него сила на самом деле?")
    $ Fl.say(Fl_setk, "Да.")
    $ Fl.say(Fl_th, "Как-то просто ты ответил, даже не распинался.")
    $ Fl.say(Fl_setk, "Ладно, я устал. Что скажешь на последок?")
    $ Fl.say(Fl_liz, "Так ты его боишься! {w}А я то думаю, почему ты сразу так сподхватился, как появился новый сказитель.")
    $ Fl.say(Fl_liz, "Такому жалкому нарцисту, как ты не победить его. Хотя ты и сам это прекрасно понимаешь.")
    $ Fl.say(Fl_liz, "Он в начале убьёт всех сказителей, а после придёт за тобой.")
    $ Fl.say(Fl_setk, "Ты права, его сила это нечто. {w}Но стоит ему узнать о своей силе и он труп.")
    $ Fl.say(Fl_liz, "С тобой спорить без полезно, ты ничего вокруг себя не видишь, кроме своих марионеток и власти.")

    $ Fl.StopMusic(4)
    $ Fl.say(Fl_liz, "Мои последние слова? Хм{mn}")
    $ Fl.say(Fl_liz, "Больше я не иллюзия, потому что я нашла то ради чего я жила и ради чего готова сейчас умереть.")
    $ Fl.say(Fl_setk, "Вот как.")
    $ Fl.say(Fl_setk, "Прощай, {w}Лиза.")
    $ Fl.say(Fl_r, "Кукловод провёл рукой. А дальше...")
    scene bg Fl_black with hpunch 
    $ Fl.AttackScreens()
    $ Fl.say(Fl_r, "Меня разорвало на двое, верхняя часть тела отделилась от нижней и я безвольно свалилась в пустоту.")
    $ Fl.say(Fl_r, "Боли не было, как и сожалей. {w}Только улыбка на лице сопуствовала в непроглядной мгле. Где вот-вот должен был зародиться слабый светлячок моего конца.")
    
    $ Fl.Pause(1.5)
    $ Fl.say(Fl_r, "Больше я не боюсь, больше нет иллюзии существования.")
    
    $ Fl.Pause(1.5)
    $ Fl.say(Fl_r, "В этом мире есть один человек, в чьих воспоминаниях - я бессмертна...")
    $ Fl.HideScreens(_with=Fl_dissolve2)




    $ Fl.Pause(8.0)
    $ Fl.DayTime("day", "day")
    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 4)
    scene bg Fl_ext_aidpost_day
    show Fl_light_c
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Устал уже говорить сколько циклов прошло. Просто - много, точное количество всё равно ничего не даст.")
    $ Fl.say(Fl_r, "Продолжал свой путь я уже в одиночестве. Всё вернулось в своё русло, в самое начало, в стандарт. {w}Ведь это история одиночки.")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_r, "За последнее время я совершил огромное количество прыжков в другие лагеря, но ничего найти не удалось. Мне нужно было узнать, как попасть в другие сектора.")
    $ Fl.say(Fl_r, "Моё перемещение это рандом, но ни разу мне так и не повезло. Сплошные мирные лагеря с игрой в пионеров.")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_r, "Частое использование прыжков отразилось на мне, без включённого ошейника сил почти нет. Мне нужно было восстановиться для дальнейшего путешествия.")
    $ Fl.say(Fl_r, "Собственно по этой причине, я иду заполнять сраный обходной лист.")
    $ Fl.say(Fl_th, "Когда последний раз я заполнял его уже и не помню...")
    $ Fl.say(Fl_q6, "Ладно нужно потерпеть всего один цикл, поиграть в пионера.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1

    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
    scene bg Fl_int_aidpost_day with Fl_effect_1

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Где эта совратительница пионеров?")
    $ Fl.say(Fl_r, "Почему то я решил обратиться так ссылаясь на то, как я медсестру впервый раз запомнил.")
    $ Fl.say(Fl_th, "Неужели ушла куда-то, да ещё утром?")
    $ Fl.say(Fl_csk, "Пионер, разве вас стучаться не учили?")
    $ Fl.say(Fl_r, "Неожиданно раздался голос позади меня.")
    $ Fl.say(Fl_th, "Явилась, не за пылилась.")
    $ Fl.say(Fl_csk, "Что-то беспокоит или по какому поводу пришёл?")
    $ Fl.say(Fl_r, "Спросила медсестра, медленно направляясь занять своё рабочее место.")
    $ Fl.say(Fl_q6, "Мне бы обходной заполнить.")
    $ Fl.say(Fl_csk, "Обходной{mn} Ты уверен, а может?")
    $ Fl.say(Fl_r, "Медсестра припустила верх халата.")
    $ Fl.say(Fl_th, "Что-то я не помню такого в сценарии. Что за хрень она несёт?")
    $ Fl.say(Fl_csk, "У тебя есть какие-то вопросы про лагерь. {w}Или сказетели тебя больше интересуют?")

    $ Fl.PlayMusic("Fl_no_tresspassing", 1, 4)
    $ Fl.say(Fl_th, "Да я погляжу у нас тут что-то интересное намечается.")
    $ Fl.say(Fl_q6, "Ты кто такая?")
    $ Fl.say(Fl_csk, "Как же быстро ты снял маску добряка.")
    $ Fl.say(Fl_r, "Медсестра достала бутылку вина и закинула одну ногу на другую.")
    $ Fl.HideScreens(_with=Fl_dissolve1)

    scene cg Fl_viola_not_wine with Fl_dissolve2
    $ persistent.Fl_photo_pallery_26 = True
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_csk, "Если интересно, то оставь свой обходной и присядь на койку.")
    $ Fl.say(Fl_q6, "Я пожалуй постою.")
    $ Fl.say(Fl_csk, "Как тебе будет угодно, Пионер. Или тебя лучше называть Q-66?")
    $ Fl.say(Fl_th, "Мы и дальше будем закидывать интрижки?")
    $ Fl.say(Fl_q6, "Обращайся как хочешь, мне плевать. Но ты не ответила на мой вопрос.")
    $ Fl.say(Fl_cs, "Я - Виола, как ты мог забыть меня, пионер?")
    $ Fl.say(Fl_th, "Медсестру действительно так звали, но я не помню чтобы она спокойно общалась не по сценарию и что-то знала о циклах и прочем.")
    $ Fl.say(Fl_cs, "Не волнуйся, я не враг. Да и способностей у меня никаких нет.")
    $ Fl.say(Fl_q6, "Откуда ты знаешь обо мне и почему твоя память не стирается?")
    $ Fl.say(Fl_cs, "Из-за способности L-87, Королевы.")
    $ Fl.say(Fl_cs, "Поэтому я не такая как все и помню все свои циклы. {w}Но у меня самой нет никаких способностей.")
    $ Fl.say(Fl_th, "Ещё одна встреча со сказителем если можно так сказать вообще.")
    $ Fl.say(Fl_th, "И что это за способность, что она из куклы превратила в живого человека?")
    $ Fl.say(Fl_q6, "Это она тебе рассказала обо мне и других сказителях?")
    $ Fl.say(Fl_cs, "Отчасти да.")
    $ Fl.say(Fl_q6, "Что значит «отчасти»?")
    $ Fl.say(Fl_cs, "Я из нулевого периода.")
    $ Fl.say(Fl_r, "Я замер, новая неизвестная информация вогнала меня в ступор.")
    $ Fl.say(Fl_cs, "По глазам вижу что ты не понимаешь о чём речь. Походу доктор Парки тебе ничего не рассказал.")
    $ Fl.say(Fl_q6, "Откуда ты...")
    $ Fl.say(Fl_cs, "Давай по порядку, пионер.")
    $ Fl.say(Fl_cs, "Ты знал, что лагерь поделён на периоды. И в каждом периоде свои ключевые персонажи и свои события.")
    $ Fl.say(Fl_cs, "Нулевой период - время когда лагерь существовал в нашем мире, когда он не успел стать аномалией. Тогда ещё бог этого мира был человеком.")
    $ Fl.say(Fl_cs, "Первый период - тогда лагерь стал отдельным миром с циклами и т.д. В нём жили все пионеры из нулевого цикла, их забрало вместе с созданием этого мира.")
    $ Fl.say(Fl_cs, "Второй период - новые обитатели лагеря. Скажем так новое поколение, жителей прошлых периодов почти не осталось. И ты живёшь и попал сюда во второй период.")
    $ Fl.say(Fl_q6, "Получается сказители могут быть из разных периодов?")
    $ Fl.say(Fl_cs, "Всё верно. В нулевом периоде сказителей нет. Но вот в первом уже присуствуют. Ключевой фигурой первого периода стал Семён Персунов - сказитель под псевдонимом Синдром.")
    $ Fl.say(Fl_cs, "Совет на будущее, если вдруг встретишь его или попадёшь в его лагерь, срочно убегай, не смей даже в бой входить. Его сила некотролируемая и слишком опасная.")
    $ Fl.say(Fl_q6, "Кто ещё из первого периода?")
    $ Fl.say(Fl_cs, "Твоя сталкерша - Тихоня, она тоже из того периода. {w}Ещё псионик. Это все те кто не смог выбраться из лагеря.")
    $ Fl.say(Fl_q6, "Ты настолько долго тут застряла?")
    $ Fl.say(Fl_cs, "Ну как видишь пережила два поколения уже.")
    $ Fl.say(Fl_q6, "Но если ты не сказитель, почему ты осталась здесь?")
    $ Fl.say(Fl_cs, "Потому что из-за меня появился бог этого мира. Ты знал, что это доктор Парки создал этого бога?")
    $ Fl.say(Fl_th, "Что? {w}Это бред какой-то, зачем превращать из человека в бога, а потом желать убить его.")
    $ Fl.say(Fl_th, "Совесть замучила что ли?!")
    $ Fl.say(Fl_cs, "Под старым корпусом в СССР вели какие-то эксперименты. Как говорил доктор Парки работали над каким-то там лекарством. Тогда за круглую сумму я согласилась помочь и отдала ему мед. книжки всех пионеров.")
    $ Fl.say(Fl_cs, "Я не знала что он использует их для поиска лучшего кандидата для эксперимента.")
    $ Fl.say(Fl_cs, "Я отказалась выбраться из этого мира, так как не заслуживаю выхода. От части из-за меня люди попадают сюда и не могут выбраться, превращаясь в психов и чудовищ. Из-за меня бог мира стал таким.")
    $ Fl.say(Fl_th, "Помогла безумному учёному создать чудовище. Да уж...")
    $ Fl.say(Fl_th, "Насколько тут лор продуман. Куклы умеет хорошо скрывать нужную информацию...")
    $ Fl.say(Fl_q6, "А в каком периоде появился Кукловод?")
    $ Fl.say(Fl_cs, "Тут интереснее. {w}Вы появились с ним в один период. Он может старше тебя на пару сотен циклов, но тоже молодой сказитель.")
    $ Fl.say(Fl_q6, "Каким образом он стал номером один тогда? Как так быстро смог узнать всё об этом мире?!")
    $ Fl.say(Fl_cs, "Никто не знает. И прости я не могу говорить о Кукловоде.")
    $ Fl.say(Fl_th, "Не может говорить? {w}Кто же он такой, что про него ничего неизвестно толком и другие не хотят даже обсуждать тебя.")
    $ Fl.say(Fl_q6, "Ладно, тогда не буду затрагивать тему.")
    $ Fl.say(Fl_q6, "Ты знаешь где получить ответы о лагере? Твоя королева их находит же где-то.")
    $ Fl.say(Fl_cs, "Тебе нужно искать их в других секторах. Чем выше уровень сектора, тем ближе он к правде о том что случилось в нулевом периоде.")
    $ Fl.say(Fl_th, "Вот как. Осталось только понять, как попасть в другой сектор...")
    $ Fl.say(Fl_cs, "Знаешь, ты можешь прямо сейчас переломить ход истории.")
    $ Fl.say(Fl_q6, "О чём ты?")
    $ Fl.say(Fl_cs, "Если ты сейчас поторопишься и окажешься на пристане, то сможешь всё изменить.")
    $ Fl.say(Fl_r, "Я уставился серьёзным взглядом, но на Виолу это никак не повлияло, а молча допила бокал.")
    $ Fl.say(Fl_cs, "Не волнуйся это не подстава, да и решать только тебе.")
    $ Fl.say(Fl_th, "Что такого может произойти на пристане?")

    $ Fl.StopMusic(4)
    $ Fl.say(Fl_q6, "Я подумаю. А пока пожалуй откланяюсь.")
    $ Fl.say(Fl_cs, "Береги себя, пионер.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1

    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
    scene bg Fl_ext_aidpost_day 
    show Fl_light_c
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Пристань может изменить ход истории?")
    $ Fl.say(Fl_r, "Сомнения были, но потерять возможность продвинуться к своей цели слишком дорого мне обойдётся. В этот раз сомнения потерпели крах.")
    $ Fl.say(Fl_q6, "Пора изменить ход этой истории!")
    $ Fl.HideScreens(_with=Fl_dissolve2)
    scene bg Fl_black with Fl_dissolve2



    $ Fl.Pause(5.5)
    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 4)
    scene bg Fl_ext_boathouse_day
    show Fl_light_c
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Что же ты задумала, ведьма.")
    $ Fl.say(Fl_r, "Каждый мой шаг отдавался прямо в голове. Напряжение сковывало.")
    $ Fl.say(Fl_th, "Никакого отдыха...")
    $ Fl.say(Fl_q6, "И что здесь должно произойти?")
    $ Fl.say(Fl_r, "Вдруг из дома на пристани раздались довольно громкие звуки.")
    $ Fl.say(Fl_th, "Посмотримка...")
    $ Fl.say(Fl_r, "Но не успел я ступить и шагу, как округу заполнил женский крик.")
    $ Fl.say(Fl_d, "УМОЛЯЮ НЕ НАДО!", _with=hpunch)
    $ Fl.say(Fl_d, "КТО НИБУДЬ ПОМОГИТЕ!", _with=hpunch)
    $ Fl.say(Fl_r, "На моём лице появилась жуткая ухмылка.")
    $ Fl.HideScreens(_with=Fl_dissolve2)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(5.5)
    scene bg Fl_int_warehouse3_day with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_pior, "Эй, эй. Не рыпайся, мы всего лишь развлечемся.")
    $ Fl.say(Fl_pior, "Слушай, а ты уверен? Нам за это ничего не будет?")
    $ Fl.say(Fl_pior, "Да не парься, Кукловод попросил её привести живой. Что плохого если мы её немного накажем?")
    $ Fl.say(Fl_d, "Прошу, не надо...")
    $ Fl.say(Fl_pior, "Она же сказитель, вдруг...")
    $ Fl.say(Fl_pior, "Да что она нам сделает то? {w}Она не контролирует свои силы, поэтому не применит их на нас!")
    $ Fl.say(Fl_r, "Слёзы сами по себе начали стекать по лицу.")
    $ Fl.say(Fl_th, "Хватит. {w}Просто убейте меня уже, не надо издеваться...")
    $ Fl.say(Fl_pior, "Тогда ладно!")
    $ Fl.say(Fl_r, "Один из пионеров подошёл ко мне и начал медленно проводить рукой по телу.")
    $ Fl.say(Fl_pior, "Хватит прелюдий!")
    $ Fl.say(Fl_r, "Я сопротивлялась, но было бесполезно, мои руки были сильно схвачены.")
    $ Fl.say(Fl_th, "Почему всё так вышло...")

    $ Fl.PlaySound("Fl_table_hit", 1, 0, False)
    $ Fl.AttackScreens(True)
    with vpunch
    $ Fl.PlayMusic("Fl_danger", 1, 6)
    $ Fl.say(Fl_r, "Неожиданно дверь просто вылетела. Удар был настолько сильный, что от двери ничего не осталось.")
    $ Fl.say(Fl_th, "Ч-что?..")
    $ Fl.say(Fl_kt, "Я вам не помешал?")
    $ Fl.say(Fl_r, "В дверном проёме стоял парень в чёрной толстовке. Длинные тёмные волосы скрывали что-то на его шее. Кожа была бледной, как у мертвеца.")
    $ Fl.say(Fl_r, "Он бросил взгляд в мою сторону.")
    $ Fl.say(Fl_r, "Этот взгляд поглощал всё вокруг, очень строгий, но одновременно пустой.")
    $ Fl.say(Fl_r, "Теперь я смогла разглядеть устройство на его шее и изредка мигающий красный огонёк.")
    $ Fl.say(Fl_th, "Не может быть{mn} Это он{mn}")
    $ Fl.say(Fl_th, "Почему именно он?!")
    $ Fl.say(Fl_pior, "Слыш, ты кто такой?")
    $ Fl.say(Fl_q6, "А ваш директор цирка не рассказал?")
    $ Fl.say(Fl_pior, "Ты чё несёшь?")
    $ Fl.say(Fl_r, "Один из пионеров достал нож и попытался ударить со спины.")
    $ Fl.say(Fl_th, "Они его просто отвлекают!")
    $ Fl.say(Fl_r, "Пионер набросился на Q-66.")
    $ Fl.say(Fl_r, "Но в тот же миг, сказитель молча ударил по швабре что лежала у его ног. Швабра подлетела и оказалась в руках парня. После чего...")

    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    $ Fl.say(Fl_r, "Он одним ударом проткнул на сквозь пионера.")
    $ Fl.say(Fl_r, "Пионеры замерли, глядя как их товарищ выплёвывает водопад крови.")
    $ Fl.say(Fl_pior, "Ублюдок, ты за это ответишь!")
    $ Fl.say(Fl_r, "Второй пионер с криком побежал на Q-66.")
    $ Fl.say(Fl_r, "Но стоило ему сократить дистанцию, как сказитель резко выставил ладонь в его сторону.")
    $ Fl.say(Fl_r, "Пионера размазало об стенку.", _with=hpunch)
    $ Fl.say(Fl_th, "Что это за чудовище{mn}")
    $ Fl.say(Fl_q6, "Да уж{mn} Даже клоны Тихони могут чем-то удивить.")
    $ Fl.say(Fl_q6, "А об такой мусор как вы не хочется и руки пачкать.")
    $ Fl.say(Fl_pior, "К-кто т-ты та-акой?")
    $ Fl.say(Fl_th, "Ещё живой?")
    $ Fl.say(Fl_r, "У стены лежал пионер, с его лба стекала кровь, а руки дрожали.")
    $ Fl.say(Fl_q6, "Да какая разница кто? Ты мне вот что скажи.")
    $ Fl.say(Fl_r, "В руках Q-66 появилась отвёртка.")
    $ Fl.say(Fl_r, "Он сел на корточки и подставил отвёртку к ноге пионера.")
    $ Fl.say(Fl_q6, "Ты что-то знаешь о карте секторов?")
    $ Fl.say(Fl_th, "Что-то тут не так...")
    $ Fl.say(Fl_r, "В панике мой взгляд метался из стороны в сторону. Ощущение что чего не хватает впилось как пиявка в мою голову.")
    $ Fl.say(Fl_th, "Был ещё один пионер!", _with=hpunch)
    $ Fl.say(Fl_r, "Стоило мне вспомнить об этом, как в ту же секунду за спиной Q-66 появился один из слуг Кукловода.")
    $ Fl.say(Fl_r, "В панике мне было страшно издать какой либо звук, но в данный момент мой голос приобрёл свободу.")
    $ Fl.say(Fl_d, "Сзад{break}")

    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    $ Fl.AttackScreens()
    $ Fl.say(Fl_r, "Не успев моргнуть и глазом, пол окрасился в ещё более алый оттенок. {w}Кровь медленно расползалась по поверхности, оставляя след жизни.")
    $ Fl.say(Fl_th, "Что{mn}")
    $ Fl.say(Fl_r, "Третий пионер лежал на полу с широко открытыми глазами. Вся его шея была разодрана - это и послужило причиной смерти.")
    $ Fl.say(Fl_q6, "Господи, вас чему то жизнь учит? {w}Ты серьёзно решил напасть со спины, как сделал твой товарищ?")
    $ Fl.say(Fl_q6, "Ты совсем идиот?! {w}На что ты надеялся, что у тебя такой номер прокатит?!", _with=hpunch)
    $ Fl.say(Fl_r, "Кричал на труп Q-66, в руках держа окровавленную отвёртку.")
    $ Fl.say(Fl_th, "Как он так быстро среагировал?")
    $ Fl.say(Fl_r, "Ещё раз осмотрев шею трупа, мысли пошли ходуном.")
    $ Fl.say(Fl_th, "Да что это за скорость такая? {w}Ему хватила доля секунды чтобы убить противника о котором он даже не знал!")
    $ Fl.say(Fl_r, "Страх сковал моё тело, в голове была только одна мысль «БЕЖАТЬ!».")

    $ Fl.Pause(2.5)
    $ Fl.say(Fl_r, "Но тело было не согласно с моими мыслями. Оно желало увидеть что будет дальше.")
    $ Fl.say(Fl_q6, "И так, вернёмся к моему вопросу.")
    $ Fl.say(Fl_r, "Последний пионер замычал, он пытался отползти, но стена его не пускала.")
    $ Fl.say(Fl_q6, "Ты что-то знаешь о карте секторов?")
    $ Fl.say(Fl_r, "Словно в дикой природе, раненая добыча пыталась найти пути отхода от хищника.")
    $ Fl.say(Fl_q6, "Не заставляй меня ждать.")
    $ Fl.say(Fl_r, "С равнодушием сказал парень в толстовке и поднёс отвёртку к глазу пионера.")
    $ Fl.say(Fl_q6, "Или ты хочешь закончить как твои товарищи, Пионер?")
    $ Fl.say(Fl_th, "Почему он говорит подобные вещи таким спокойным голосом?")
    $ Fl.say(Fl_pior, "З-знаю...")
    $ Fl.say(Fl_q6, "Говори чётче, нечего нюни пускать.")
    $ Fl.say(Fl_pior, "Карта секторов - её создал Кукловод, он путешествует по лагерям, а после распределяет посещённый лагерь в сектор.")
    $ Fl.say(Fl_q6, "Как попасть в другой сектор?")
    $ Fl.say(Fl_r, "Ответа не последовало. {w}Допрос не закончился - за нарушение правил идёт наказание.")

    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    $ Fl.say(Fl_pior, "ААААА!", _with=hpunch)
    $ Fl.say(Fl_r, "Сказитель вонзил отвёртку пионеру в локоть.")
    $ Fl.say(Fl_pior, "П-поезд...")
    $ Fl.say(Fl_q6, "Подробнее.")
    $ Fl.say(Fl_pior, "Перейти в другой сектор можно через поезд.")
    $ Fl.say(Fl_pior, "Как только поезд тронется, начинает клонить в сон. За этот промежуток времени нужно успеть совершить прыжок в другой лагерь, тогда тебе удаться перескочить в другой сектор.")
    $ Fl.say(Fl_q6, "Вы трое сюда так же попали?")
    $ Fl.say(Fl_pior, "Д{break2}")
    $ Fl.StopMusic(6)
    $ Fl.say(Fl_r, "Пионер резко замолчал. Его глаза расширились и выступили слёзы.")
    $ Fl.say(Fl_r, "После чего он выплюнул собственный язык.")
    $ Fl.say(Fl_q6, "Какого?!")
    $ Fl.say(Fl_r, "Парня не на шутку это удивило. {w}Что касается меня, я начала бесшумно плакать, всё происходящее сильно давило на психику.")
    $ Fl.say(Fl_r, "Но сцена не закончилась, пионер резким движение схватился обеими руками за горло, пытаясь себя задушить. Его вены по всему телу вспухли.")
    $ Fl.say(Fl_r, "Пионер глазами молил о помощи, его страх смотрел прямо на Q-66.")

    $ Fl.Pause(3.0)
    $ Fl.say(Fl_th, "Он мёртв...")
    $ Fl.say(Fl_r, "Сказитель выбросил отвёртку и молча удалился.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause(3.0)
    scene bg Fl_int_warehouse3_day with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Контроль над телом вернулся.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_fast


    $ Fl.Pause(1.5)
    scene bg Fl_ext_houses2_day
    show Fl_light_c
    with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Не понимая что мной движет, я выбежала наружу. Жуткая сцена не выходила из моей головы.")
    $ Fl.say(Fl_r, "Но я хотела его остановить...")
    $ Fl.say(Fl_r, "Сказитель медленно отдалялся. Я решила действовать.")
    $ Fl.say(Fl_d, "Постой.")
    $ Fl.say(Fl_r, "Парень даже не шелохнулся, шёл дальше.")
    $ Fl.say(Fl_d, "Подожди!")
    $ Fl.say(Fl_r, "Результат тот же, он шёл дальше. Казалось что в данный момент парень был в другом месте, всё что происходило вокруг него не имело никакого смысла и роли.")
    $ Fl.say(Fl_d, "Да остановись ты уже!", _with=hpunch)
    $ Fl.say(Fl_r, "Парень замер.")
    $ Fl.say(Fl_th, "Что я творю?!", _with=hpunch)
    $ Fl.say(Fl_th, "Совсем дура что ли?!", _with=hpunch)
    $ Fl.say(Fl_th, "Ты же видела что он сделал с пионерами. Тебя ведь предупреждали что он слишком опасен!")
    $ Fl.say(Fl_r, "После моего акта безрасудства, Q-66 медленно повернулся.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(2.5)
    scene cg Fl_gg_bol:
        subpixel True
        truecenter
        yalign 0.85
        zoom 1.18
        ease 8.5 yalign 0.1 zoom 1.0
    show Fl_light_c
    with Fl_dissolve2
    $ persistent.Fl_photo_pallery_27 = True
    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Только вблизи мне удалось разглядеть его полностью.")
    $ Fl.say(Fl_r, "Пустой взгляд, казалось он поглощал все лучи красок жизни, словно бездна - оставляющая вокруг себя ничего. Взгляде не было ни боли, ни радости, ни печали, даже злости...")
    $ Fl.say(Fl_r, "Натуральная седая пряд развеивалась на ветру, изредка раскрывая взор на точно такую же пустую бездну.")
    $ Fl.say(Fl_r, "Рука сама по себе вытянулась, хотелось дотронуться до него, забрать печаль, что сломала человека.")
    $ Fl.say(Fl_r, "В виду детской наивности или чудачества, я была сама не своя. Но почему то, страх пропал. Уже было плевать что передо мной стоит уже далеко не человек.")
    $ Fl.say(Fl_th, "Ведь я знаю что с тобой они сделали...")
    $ Fl.say(Fl_q6, "Чего тебе, малявка?")
    $ Fl.say(Fl_r, "Грубый голос вернул меня в реальность.")
    $ Fl.say(Fl_q6, "Ты же одна из сказителей?")
    $ Fl.say(Fl_d, "Д-да...")
    $ Fl.say(Fl_r, "Такой коротки ответ его не устроил и он тут же потерял интерес.")
    $ Fl.say(Fl_d, "Прошу, можно пойти с тобой?")
    $ Fl.say(Fl_q6, "Чё?")
    $ Fl.say(Fl_th, "Он всегда такой грубый?!")
    $ Fl.say(Fl_d, "Я хочу пойти с тобой!")
    $ Fl.say(Fl_r, "Мой голос больше не дрожал, строгий взгляд был направлен прямо на Q-66.")
    $ Fl.say(Fl_q6, "Нет, ты мне не нужна.")
    $ Fl.say(Fl_d, "Почему?!")
    $ Fl.say(Fl_q6, "Я не собираюсь нянчиться с тобой.")
    $ Fl.say(Fl_d, "Я могу быть полезной!")
    $ Fl.say(Fl_q6, "Слушай, я работаю один, ясно?")
    $ Fl.say(Fl_d, "Но тебе ведь нужна помощь!")
    $ Fl.say(Fl_r, "Парень озлобился.")
    $ Fl.say(Fl_q6, "Пойти со мной, тоже самое что спуститься в ад. {w}Я не собираюсь хоронить ещё кого-то.")
    $ Fl.say(Fl_th, "...")
    $ Fl.say(Fl_q6, "В следующий раз будь осторожна.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2

    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Сказитель молча развернулся и ушёл.")
    $ Fl.say(Fl_th, "Даже ты мне не стал помогать{mn}")
    $ Fl.StopAmbience(4)
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause(7.5)
    scene bg Fl_ext_platform_train
    show Fl_light_c
    with Fl_dissolve2
    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Стоя на платформе, я закурил.")
    $ Fl.HideScreens(_with=Fl_dissolve1)

    $ Fl.Pause (1.5)
    $ Fl.PlaySound("Fl_zazigalka", 1, 0, False)
    $ Fl.Pause (2.0)
    $ Fl.PlaySound("Fl_smoking", 1, 0, False)
    $ Fl.Pause (2.5)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.PlayMusic("Fl_buckethead_angel_monster", 1, 7)
    $ Fl.say(Fl_th, "Какая удача, поезд был на месте. Значит те придурки прибыли совсем недавно.")

    $ Fl.PlaySound("Fl_smoking", 1, 0, False)
    show Fl_vignette with Fl_dissolve2
    $ Fl.say(Fl_r, "Но мысли мои были далеко не связаны с поездом...")
    $ Fl.say(Fl_th, "Как так вышло, что сказителем стала маленькая девочка? На вид ей лет 14-15...")
    $ Fl.say(Fl_r, "Я схватился за голову.")
    $ Fl.say(Fl_q6, "Она застряла здесь точно так же. И судя по всему давно.")
    $ Fl.say(Fl_th, "Я не хотел поворачиваться...")
    $ Fl.say(Fl_q6, "Даже если она что-то и знала об этом месте, я не могу позволить быть ей рядом со мной.")

    $ Fl.Pause (2.0)
    $ Fl.say(Fl_q6, "Слишком много людей умерло, находясь возле меня...")
    $ Fl.say(Fl_r, "Я потушил сигарету.")
    $ Fl.say(Fl_th, "Старая ведьма это имела виду под «Изменить ход истории»? Спасти малявку от толпы пионеров?")

    $ Fl.Pause (2.0)
    $ Fl.say(Fl_q6, "Может всё же стоило её взять с собой?")
    $ Fl.say(Fl_th, "{mn}")
    $ Fl.say(Fl_th, "Нет! Я правильно поступил, что оставил её. Это для её же блага.")

    $ Fl.Pause (2.0)
    $ Fl.say(Fl_r, "Перед глазами всплыла картина с пионером.")
    $ Fl.say(Fl_th, "Он явно не сам принял решение убить себя. {w}В его глазах чётко отражалась мольба о помощи.")
    $ Fl.say(Fl_th, "Это было одно из наказаний Кукловода за предательство?")
    $ Fl.say(Fl_th, "Каким образом он узнаёт если его планируют предать?")
    $ Fl.say(Fl_q6, "Хотя в любом случае я бы его убил, за меня просто выполнили мою работу.")
    hide Fl_vignette with Fl_dissolve2
    $ Fl.say(Fl_r, "Не став отягивать, я направился к поезду.")
    $ Fl.StopMusic(5)
    $ Fl.say(Fl_q6, "Посмотрим куда меня перенесёт на этот раз.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2



    $ Fl.Pause(8.0)
    $ Fl.DayTime("night", "night")
    scene bg Fl_train_rain
    show Fl_smoke
    with Fl_dissolve2
    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Я всё выполнил, как сказал пионер.")
    $ Fl.say(Fl_r, "Насущая картина меня поразила. Вокруг был туман и тишина, {w}мёртвая тишина.")
    $ Fl.say(Fl_th, "Это и есть тот самый другой сектор?")
    $ Fl.say(Fl_r, "Всё выглядело иначе. Лагерь не ждал гостей, он всем видом отталкивал незванных путников. Казалось не туман пытался скрыть лагерь от меня, а меня от лагеря. А что будет если он меня заметит?")
    $ Fl.say(Fl_r, "Впервые за долгое время, я всматривался в каждый уголок, концентрация была на высоте.")
    $ Fl.say(Fl_r, "Под ногами раздался шелест.")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_q6, "Газета?")
    $ Fl.say(Fl_r, "Борясь с белой дымкой, я заметил на платформе тонну лежащей макулатуры.")
    $ Fl.say(Fl_th, "Обычные советские новости...")
    $ Fl.say(Fl_r, "Отбросив куда подальше клочёк бумаги, я краем глаза зацепил лавочку.")
    $ Fl.say(Fl_r, "Вдали был чей-то силуэт. {w}В мёртвой тишине писк устройства прозвучал подобно сирене.")
    $ Fl.HideScreens(_with=Fl_dissolve1)

    $ Fl.Master(Fl_bg_zoom_e(1.0, 1.2, 2.0, 0.5, 0.65))
    $ Fl.Pause(2.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Стоило мне приблизиться, как силуэт принял своё истинное очертание - человеческое.")
    $ Fl.say(Fl_th, "Это ещё что за пассажир?")

    $ Fl.Pause(2.0)
    show Fl_vignette2 with Fl_dissolve2
    $ Fl.PlayMusic("Fl_title", 1, 5)
    $ Fl.say(Fl_r, "Это и правда был человек. Был... {w}На лавочке распластался труп, всё его тело почернело, а вены налились ярко-синим оттенком.")
    $ Fl.say(Fl_q6, "Довольно свежий.")
    $ Fl.say(Fl_r, "Оставив увиденное без комментариев, я решил двинуться дальше изучать это место.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2

    $ Fl.Pause(4.5)
    scene bg Fl_ext_houses_night2:
        Fl_walking1
    show Fl_smoke
    show Fl_vignette2
    with Fl_dissolve2
    $ Fl.Pause(2.0)
    scene bg Fl_black with Fl_dissolve2

    $ Fl.Pause(4.5)
    scene bg Fl_ext_house_gr_night
    show Fl_smoke
    show Fl_vignette2
    with Fl_dissolve2
    $ Fl.Pause(1.5)
    scene bg Fl_black with Fl_dissolve1

    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
    scene bg Fl_int_house_of_sl_night2
    show Fl_vignette2
    with Fl_dissolve2
    $ Fl.PlaySound("Fl_shagi", 1.0, 0, False)

    $ Fl.Pause(3.5)
    scene bg Fl_black with Fl_dissolve1
    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)

    $ Fl.Pause(4.0)
    scene bg Fl_int_house_sn_vk_night
    show Fl_vignette2
    with Fl_dissolve2
    $ Fl.PlaySound("Fl_scrip_krovati", 1.0, 0, False)
    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Небольшая прогулка дала много информации. {w}Весь лагерь был укутан туманом, редкие фонари кое-как поддерживали видимость во мраке. Но тишина, каждый шаг, каждый мой звук нарушал покой этого места.")
    $ Fl.say(Fl_r, "Сидя на кровати, я играл в гляделки с трупом, что принял туже позицию как и я на соседней койке.")
    $ Fl.say(Fl_th, "Здесь повсюду трупы, причём очень свежие.")
    $ Fl.say(Fl_th, "Вся картина напоминала зачистку - когда начинается новый цикл безумец, как я, убивает всех жителей и превращает лагерь в кладбище.")
    $ Fl.say(Fl_q6, "Вот только...")
    $ Fl.say(Fl_q6, "Какого чёрта ты тут забыл?")
    $ Fl.say(Fl_r, "Моим соперников гляделок был Пионер.")
    $ Fl.say(Fl_th, "Забавно, что на платформе труп принадлежал тоже Пионеру.")
    $ Fl.say(Fl_th, "Кто-то или что-то убивает тех кто забрёл в этот лагерь.")
    $ Fl.say(Fl_r, "Викинув сигарету, я решил продолжить своё расследование.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(5)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(5.5)
    scene bg Fl_ext_aidpost_night
    show Fl_smoke
    show Fl_vignette2
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Трупы на пути не переставали редеть и привели они меня к единственному месту где борятся за жизнь.")
    $ Fl.say(Fl_th, "Звуки так и не появились.")
    $ Fl.say(Fl_r, "Причина по которой я выбрал медпункт - найти что-то полезное, желательно бинты и прочий ассортимент для окозания первой помощи.")
    $ Fl.PlaySound("Fl_bush_leaves", 1.0, 0, False)

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_th, "{mn}")
    $ Fl.say(Fl_th, "Это ещё что за приколы?")
    $ Fl.say(Fl_r, "Я повернулся к источнику звука, но в тумане было невозможно разглядеть нарушителя тишины.")
    $ Fl.say(Fl_th, "Кто-то решил поиграть в прятки?")
    $ Fl.say(Fl_r, "Отбросив концентрацию на кустах, я пошёл по сценарию, рассписанному в голове.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
    scene bg Fl_int_medstation
    show Fl_vignette2
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_q6, "Забавно.")
    $ Fl.say(Fl_r, "Первое что меня удивило, наличие света в помещение. Куда бы я не заглядывал свет не работал.")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_th, "Это ещё что?")
    $ Fl.say(Fl_r, "На полке с препоратами аккуратно в ряд были расставлены различные шприцы.")
    $ Fl.say(Fl_th, "Тут что-то не чисто. {w}Ладно трупы, но кому понадобилось делать запасы разных препоратов в шприцах?")
    $ Fl.say(Fl_r, "Я присел за стол.")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_th, "Куда я попал? {w}Неужели лагеря других секторов настолько отличаются. Это уже не пионерлагерь, а какой-то сайлент хилл...")

    $ Fl.PlaySound("Fl_bush_leaves", 0.6, 0, False)
    $ Fl.say(Fl_q6, "Какого?!", _with=hpunch)
    $ Fl.say(Fl_r, "Я бросил взгляд в окно. Из стороны леса вновь раздался какой-то шорох.")
    $ Fl.say(Fl_r, "Но вновь туман скрывал источник звука.")
    $ Fl.say(Fl_th, "Простым совпадением это не назовёшь, тут явно какая-то чертовщина происходит.")
    $ Fl.say(Fl_r, "Неожиданно в лицо попал ещё один источник света.")
    $ Fl.say(Fl_r, "Оказалось, резким движением я зацепил клавиатуру и дисплей компьютера ожил.")
    $ Fl.say(Fl_r, "Не знаю что меня смутило больше, тот факт что везде нет света за то компьютер работает или то что старинная машина не издаёт никакого звука.")
    $ Fl.say(Fl_q6, "Посмотрим.")

    $ Fl.Pause(2.5)
    $ Fl.say(Fl_r, "Лучше своё любопытство, я оставил при себе. На экране большими буквами было написано: {w}«Q-66 Статус: Прибыл».")
    $ Fl.say(Fl_r, "Кроме моего имени, были в списке и другие, но имели иной статус: «Устранены».")
    $ Fl.say(Fl_th, "Это мать твою что такое?!")
    $ Fl.say(Fl_r, "Лагерь знал, что я прибуду, он ждал меня. Или же кто-то другой ждал гостей...")

    $ Fl.PlaySound("Fl_switch", 0.6, 0, False)
    scene bg Fl_int_aidpost_night_nolight
    $ Fl.say(Fl_r, "Неожиданно свет пропал. Даже у такого психа как я началась паника.")
    $ Fl.say(Fl_th, "Надо отсюда выбираться, я зашёл слишком далеко.")
    $ Fl.say(Fl_r, "Паника взяла надо мной контроль. {w}Я не знал кто мой истинный враг, каждый мой шаг подобен прогулке по тонкому льду.")

    $ Fl.PlaySound("Fl_switch", 0.6, 0, False)
    scene bg Fl_int_medstation_zombie with Fl_fast
    $ Fl.say(Fl_th, "{mn}")
    $ Fl.say(Fl_r, "Свет вновь разогнал мрак. {w}И то что его скрывало...")
    $ Fl.say(Fl_r, "Меня окружала не одна пара глаз. Природное явление немного сбавило обороты и я отчётливо мог разглядеть кому принадлежали маленькие красные светлячки.")
    $ Fl.say(Fl_r, "Множество различных человеческих фигур, они просто стояли и смотрели на меня, а я на них.")
    $ Fl.say(Fl_r, "Игра в гляделки окончена. {w}Я рванул к двери.")

    $ Fl.PlaySound("Fl_table_hit", 0.6, 0, False)
    scene bg Fl_black with vpunch
    $ Fl.say(Fl_r, "Дверь слетела с петель. Медленным шагом я вышел на крыльцо, после чего медленно повернулся в сторону леса...")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.DayTime("rain", "night")
    $ Fl.Pause(2.5)
    scene cg Fl_forest_zombie
    show Fl_vignette2
    with Fl_dissolve2
    $ persistent.Fl_photo_pallery_28 = True
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.PlayMusic("Fl_Noel-SunMedicine", 1, 6)
    $ Fl.say(Fl_r, "Теперь я во всей красе мог наблюдать за своими надзирателями.")
    $ Fl.say(Fl_r, "На первый взгяд обычные пионеры, но выглядили они не как люди, казалось вместо лиц у них маски когда-то давно живых людей. Но больше всего они напоминали внешнее на Тихоню, которую я встретил в цикле с Мику.")
    $ Fl.say(Fl_th, "Клоны? {w}Нет создать столько клонов невозможно, тогда кто или что стоит передо мной. Не ходячие же мертвецы!")
    $ Fl.say(Fl_r, "Меня очень сильно удивило, что они почти все были безоружны. Но ключевое слово «почти».")
    $ Fl.say(Fl_th, "Откуда они раздобыли обрез в детском лагере?")
    $ Fl.say(Fl_r, "Но времени на размышления больше не было. Нечто, что отдалёно напоминало пионеров, ожили. Их рот растянулся до ушей, а глаза засветились.")
    $ Fl.say(Fl_q6, "Ахахаах, с нечестью я ещё не сражался!")
    $ Fl.say(Fl_r, "Стоило нечести рвануть в мою сторону, как я тут же подпрыгнул в воздух.")

    $ Fl.AttackMaster(True)
    $ Fl.say(Fl_r, "И со всей силы размазал о землю голову пионерки с обрезом. Она даже не успела прицелиться, как встретилась лицом к лицу с холодной землёй.", _with=hpunch)
    $ Fl.say(Fl_th, "Проверенный метод, не знаешь слабости врага - сноси ему башку или вырывай сердце.")
    $ Fl.say(Fl_r, "Другой пионер сократил со мной дистанцию и замахнулся рукой.")
    $ Fl.say(Fl_r, "Теперь мне была понятна причина отсуствие какого-либо орудия, на пальцах пионеров были длинные и острые ногти.")
    $ Fl.say(Fl_r, "Их движения были довольно быстрее, поэтому нанести серьёзные повреждения когтями не составило бы никакого труда.")

    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    $ Fl.AttackMaster(False)
    $ Fl.say(Fl_r, "Я быстро подобрал кусок деревяшки и воткнул прямо в грудь нечести.")
    $ Fl.say(Fl_th, "Неужели вот эти твари убили всех попаданцев?")
    $ Fl.say(Fl_r, "Следующая жертва ринулась на меня индентично предыдущей.")
    $ Fl.say(Fl_r, "Схватив её за волосы, я резко сменил траекторию. Тем самым выставив тело пионерки вперёд.")

    $ Fl.PlaySound("Fl_gun", 1, 0, False)
    $ Fl.say(Fl_r, "Голову пионера разорвало и тело замертво упало на землю. Я же перевёл взгляд на стрелка.")
    $ Fl.say(Fl_q6, "Думаешь, я настолько тупой и не услышал за спиной звук затвора?")
    $ Fl.say(Fl_r, "Тварь лишь оскалилась в ответ. После чего они все резко забеги вокруг. Их силуэты растворялись за деревьями и было трудно отследить всех и сразу.")
    $ Fl.say(Fl_th, "Что они задумали.")
    $ Fl.say(Fl_r, "Тут же из кустов на меня набросилась пионерка.")
    $ Fl.say(Fl_r, "Я ждал чего-то подобного, поэтому тут же подобрал целый обрез с первого убитого трупа.")

    $ Fl.PlaySound("Fl_gun", 1, 0, False)
    $ Fl.say(Fl_r, "Голова пионерки превратилась в фарш.")
    $ Fl.PlaySound("Fl_bush_leaves", 0.6, 0, False)
    $ Fl.say(Fl_r, "Но расслабляться было рано...")
    $ Fl.PlaySound("Fl_gun", 1, 0, False)
    $ Fl.say(Fl_th, "Решили сменить тактику и нападь по несколько?")
    $ Fl.say(Fl_r, "Выкинув двустволку в кусты, я подготовился к низкому старту.")
    $ Fl.PlaySound("Fl_bush_leaves", 0.6, 0, False)
    $ Fl.HideScreens(_with=Fl_dissolve1)


    scene bg Fl_ext_forest_day_rainy
    show Fl_vignette2
    with Fl_fast
    scene bg Fl_ext_forest2_day_rainy
    show Fl_vignette2
    with Fl_fast
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_q6, "Надо найти какое-то оружие, против толпы на одних кулаках далеко не уедешь.")
    $ Fl.PlaySound("Fl_bush_leaves", 0.6, 0, False)
    $ Fl.say(Fl_th, "Да вы издеваетесь, я же далеко свалил от них!")
    $ Fl.say(Fl_r, "Лес позади меня был спокойный, но звук нарастал. Твари умнели с каждой минутой.")
    $ Fl.say(Fl_r, "Но я не зря сменил локацию. На открытой площади легче следить за каждым...")
    $ Fl.say(Fl_r, "Не успел я обрадоваться, как перед глазами промелькнул силуэт.")
    $ Fl.say(Fl_th, "Что{break}")
    $ Fl.say(Fl_r, "Перед глазами пронеслись когти, кое-как мне удалось увернуться.", _with=hpunch)
    $ Fl.AttackMaster(False)
    $ Fl.say(Fl_q6, "Тцц...")
    $ Fl.say(Fl_r, "Я рано раслабился, за первой атакой последовала вторая. Увернуться не получилось, сделав блок я избежал прямого урона и ударил в ответ по лицу пионерке.")
    $ Fl.say(Fl_th, "Раны от когтей глубокие...")
    $ Fl.say(Fl_r, "Вокруг поляны повыползало множество пионеров, некоторые были мне уже знакомы, а некоторых вижу впервые.")
    $ Fl.say(Fl_r, "Они сильно отличались от тех что я увидел впервые. У кого-то была серая кожа, у кого-то белые зрачки... А других сложно даже с человеком сравнить - просто обезображенные трупы.")
    $ Fl.say(Fl_q6, "По мою душу пришли?")
    $ Fl.say(Fl_r, "Я ухмыльнуся.")
    $ Fl.say(Fl_q6, "Давайте нападайте, я с радостью превращу вас в фарш!")
    $ Fl.say(Fl_r, "Нечесть толпой рванула ко мне.")
    $ Fl.say(Fl_r, "Что я только не делал, использовал деревяшки в роли кола, использовал самих пионеров в роли живого щита, дрался в рукопашку, но количество тварей росло.")
    $ Fl.say(Fl_q6, "<С*ка>.", _with=hpunch)
    $ Fl.say(Fl_r, "Я бросил взгляд на свою ногу. Пионерка широко раскрыла свой чёрный рот и захохотала.")
    $ Fl.say(Fl_r, "Из моей ноги торчал шприц. В голову сразу словно током ударило воспоминание.")
    $ Fl.say(Fl_th, "Препораты в медпункте!")
    $ Fl.AttackMaster(False)
    $ Fl.say(Fl_r, "Сделав замах ногой, я отбил другую тварь и отцепил ту что воткнула мне шприц.")
    $ Fl.say(Fl_th, "Хреново, я не знаю что за препорат она мне ввела! Да и через сколько он подействует.")
    $ Fl.say(Fl_th, "Надо сваливать, с каждой минутой пионеров становится только больше.")
    $ Fl.say(Fl_r, "На меня резко напала усталость.")

    $ Fl.AttackMaster(False)
    $ Fl.say(Fl_r, "Нечесть будто просекла фишку и ещё одна пионерка воткнула в меня шприц, мне удалось не дать ей ввести препорат.")
    $ Fl.say(Fl_q6, "Кх!", _with=hpunch)
    $ Fl.say(Fl_r, "Другая пионерка вцепилась зубами в ключицу.")
    $ Fl.say(Fl_th, "Как же вы достали!")
    $ Fl.say(Fl_r, "Со злости я воткнул пальцы в чёрные глазницы твари, в тот же момент по руке потекла её кровь. Только вот пионерка никак не отреагировала.")
    $ Fl.say(Fl_th, "Она не чувствует боли?")
    $ Fl.say(Fl_th, "Неужели{break}")

    $ Fl.AttackMaster(False)
    $ Fl.Pause(2.0)
    $ Fl.StopMusic(5)
    show Fl_prolog_dream with Fl_dissolve2
    $ Fl.say(Fl_r, "Я не знаю сколько шприцов вогнали в моё тело...")
    $ Fl.say(Fl_r, "Но продолжать бой я не мог.")
    $ Fl.say(Fl_th, "Осталось только сбежать в другой лагерь. {w}Надо сконцентрироваться{mn}")

    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    scene bg Fl_black with vpunch
    $ Fl.say(Fl_r, "Последний шприц был введён прямо в шею. Он не оставил мне никаких шансов на побег.")
    $ Fl.say(Fl_th, "Интересно если я сейчас умру, то засчитается ли данная смерть от рук живых...")
    $ Fl.HideScreens(_with=Fl_dissolve2)


    $ Fl.Pause(8.0)
    scene bg Fl_black_flash2 with Fl_dissolve3
    $ Fl.ShowScreens(_with=Fl_dissolve2)
    $ Fl.PlayMusic("Fl_sayonara", 1, 5)
    $ Fl.say(Fl_r, "Интересно, сколько шансов на ошибку дано человеку? И как узнать количество зарание?")
    $ Fl.say(Fl_r, "У каждого своё количество или кто-то нам назначает?")
    $ Fl.Pause(1.5)
    $ Fl.say(Fl_r, "Нет. {w}Все люди в своей жизни постоянно ошибаются, каждый может поступить неправильно или сказать не то. А шансы нам дают окружающие. Мы можем простить небольшую ошибку, а можем навеки оставить злобу за непростительную ошибку.")
    $ Fl.say(Fl_r, "Но самая фатальная ошибка - ошибка которая стоит чей-то жизни...")
    $ Fl.Pause(1.5)
    $ Fl.say(Fl_r, "Сколько я таких совершил? Сколько моих ошибок повлекли за собой горе и страдание других?")
    $ Fl.Pause(2.5)
    $ Fl.say(Fl_r, "Я не хотел...")
    $ Fl.say(Fl_r, "Извинения уже ничего не исправят, как и не вернут всё что я разрушил словами, поступками.")
    $ Fl.say(Fl_r, "Мне надо{mn2} Просто идти дальше, доказать что я осознал ошибку, избежать её вновь, не прятаться как трус...")
    $ Fl.say(Fl_r, "Если я не способен защитить то что мне дорого, то смысл от всех чувств что я дарил человеку, смысл от приятных воспоминаний. Если своей слабостью отвернулся от других.")
    $ Fl.say(Fl_r, "Слабость это никогда ты не можешь, а когда ты даже не пытался.")
    $ Fl.say(Fl_r, "Многие могут сказать: «Прости, ничем помочь не могу», даже не попытавшись что-то сделать. Почему мы порой так хлоднокровно поступаем с дорогими людьми.")
    $ Fl.say(Fl_r, "Эгоисты? {w}Возможно.")
    $ Fl.say(Fl_r, "Все мы как ни крути эгоисты, мы пытаемся в первую очередь подумать о своём благополучие и это нормально, мы же не обязаны играть в героев.")
    $ Fl.say(Fl_r, "Интересно, герой это кто? Тот кто может откинуть своё я, жизнь ради другого, рискнуть всем лишь бы защитить, помочь кому-то, даже если он не знает этого человека?")
    $ Fl.say(Fl_r, "Тогда кто я в этой истории? {w}Точно уж не герой.")
    $ Fl.say(Fl_r, "Наверное такой же эгоист, что пытается защитить себя. Хотя защита окружающих от себя можно назвать героизмом?")
    $ Fl.Pause(2.5)
    $ Fl.say(Fl_r, "Надо идти. {w}Но куда?")
    $ Fl.HideScreens(_with=Fl_dissolve2)
    $ Fl.StopMusic(5)
    scene bg Fl_black with Fl_dissolve3


    $ Fl.Pause(6.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Моё пробуждение оказалось не из приятных, тело было ватным и каждое слабое движение сопровожалось стонами.")
    $ Fl.say(Fl_th, "Чёрт, где я?")
    $ Fl.say(Fl_r, "Я пытался поднять голову и открыть глаза, но тщетно.")
    $ Fl.say(Fl_th, "Почему я себя так хреново чувствую будто после пьянки?")
    $ Fl.say(Fl_r, "Моё ёрзанье привлекло чьё то внимание.")
    $ Fl.say(Fl_d, "О, дорогой, ты уже очнулся?")
    $ Fl.say(Fl_th, "Этот голос я узнаю из тысячи...")
    $ Fl.say(Fl_r, "Приложив максимум усилий, я наконец-то смог поднять голову и открыть глаза.")
    $ Fl.HideScreens(_with=Fl_dissolve1)

    $ Fl.Pause(3.5)
    scene cg Fl_loner_lena with Fl_dissolve2
    $ persistent.Fl_photo_pallery_29 = True
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Тихоня...")
    $ Fl.PlayMusic("Fl_ploho", 1, 5)
    $ Fl.say(Fl_r, "Девушка сидела на мне верхом, то и дело играясь с ножом в руках. Выглядела она нормально, разве что всё с той же дибильной ухмылкой и неменее идиотской озвучкой текста.")
    $ Fl.say(Fl_r, "Очнулся я сидя на стуле, мои руки были крепко связаны.")
    $ Fl.say(Fl_th, "Вот почему мне было так сложно двигаться.")
    $ Fl.say(Fl_lnt, "А ты довольно крепкий, понадобилось аж четыре лошадиной дозы снотворного чтобы тебя вырубить.")
    $ Fl.say(Fl_th, "Так вот что за препораты были у тех мертвецов. {w}Мертвецов{mn}")
    $ Fl.say(Fl_q6, "Что ты сделала с теми мертвецами?")
    $ Fl.say(Fl_lnt, "Да ничего, это же я отправила их за тобой.")
    $ Fl.say(Fl_th, "Значит эти мертвецы действительно рук Тихони. {w}Лица похожие как у того клона в шахте, не чувствуют боли, довольно просто догадаться.")
    $ Fl.say(Fl_q6, "Каким образом ты управляла ими если твоя способность клоны?")
    $ Fl.say(Fl_lnt, "И-и-и-и?")
    $ Fl.say(Fl_q6, "Что и?! Среди мертвецов были и другие пионеры, не только Лены.")
    $ Fl.say(Fl_lnt, "Хи-хи, ты такой глупыш. Я могу создавать клоны не только похожие на меня.")
    $ Fl.say(Fl_r, "Я замолчал.")
    $ Fl.say(Fl_lnt, "Ты хоть раз задумывался, как я создаю клонов, милый?")
    $ Fl.say(Fl_th, "{mn}")
    $ Fl.say(Fl_q6, "Из трупов?..")
    $ Fl.say(Fl_lnt, "Ты такой молодец, милый!")

    $ Fl.AttackScreens()
    $ Fl.say(Fl_r, "Тихоня набросилась на меня в объятия.")
    $ Fl.say(Fl_r, "Я сразу же попытался её отцепить, но верёвки не позволи мне это сделать.")
    $ Fl.say(Fl_q6, "Отцепись!")
    $ Fl.say(Fl_lnt, "Оу, снова этот злобный взгляд. Он мне так нравится, смотри на меня так почаще.")
    $ Fl.say(Fl_r, "За столько встреч с этой ненормальной я уже привык к бреду что она несла.")
    $ Fl.say(Fl_q6, "Тогда какое нафиг это клонирование если ты просто поднимаешь мёртвых?")
    $ Fl.say(Fl_lnt, "Подумай сам, куда легче создать марионетку из трупа. Мне всего лишь нужно убить кого-то своими руками и я могу ими управлять.")
    $ Fl.say(Fl_th, "Значит вот какое условие нужно для создание клона, смерть от руки Тихони.")
    $ Fl.say(Fl_q6, "Постой, разве смерть от живого не влечёт за собой стирания тебя из этого мира?")
    $ Fl.say(Fl_lnt, "Дорогой, мы говорим с тобой о куклах, а им смерть от наших рук не страшна.")
    $ Fl.say(Fl_q6, "Но среди кукол были Пионеры.")
    $ Fl.say(Fl_lnt, "Так они такие же куклы, ты не знал?")
    $ Fl.say(Fl_r, "Я с недопонимаем глянул на Тихоню.")
    $ Fl.say(Fl_lnt, "Оооо, ты значит ещё не знаешь всей правды. Очень печально.")
    $ Fl.say(Fl_q6, "Ты издеваешь надо мной?!")
    $ Fl.say(Fl_lnt, "Не кипятись, тебе не зачем всё знать, главное что ты сейчас рядом со мной, милый.")
    $ Fl.say(Fl_q6, "Не отходи от темы!")
    $ Fl.say(Fl_lnt, "Ой, точно мы же про клонов говорили.")
    $ Fl.say(Fl_th, "Тц, стерва!")
    $ Fl.say(Fl_lnt, "Теперь ты понимаешь, как я тебя постоянно находила? Я зарание убивала Лену и ждала тебя.")
    $ Fl.say(Fl_q6, "Сколько Лен находятся под твоим контролем?")
    $ Fl.say(Fl_lnt, "Много, очень много.")
    $ Fl.say(Fl_lnt, "А ещё знаешь очень удобно создавать клонов из трупов, мёртвые не чувствуют боли.")
    $ Fl.say(Fl_r, "И тут я кое-что понял.")
    $ Fl.say(Fl_q6, "Мёртвые всего лишь оболочка{mn} Поэтому на них может не действовать контроль?")
    $ Fl.say(Fl_lnt, "Дааа, все клоны обладают моим разумом и используют мои знания и навыки. Я могу лишь ограничить их, если само тело было слишком слабое.")
    $ Fl.say(Fl_th, "Теперь понятно почему Кукловод её одолеть не может. С такой способностью можно вечно скрываться, а клоны выступят в роли пешек.")
    $ Fl.say(Fl_q6, "Зачем ты снова последовала за мной?")
    $ Fl.say(Fl_lnt, "Хахахах, я за тобой и не следовала. Это ведь ты пришёл в мой лагерь.")
    $ Fl.say(Fl_th, "Всмысле? {w}Это её лагерь?")
    $ Fl.say(Fl_lnt, "Ты сам совершил прыжок в мой лагерь.")
    $ Fl.say(Fl_q6, "Стоп-стоп, твой же лагерь почти невозможно найти?!")
    $ Fl.say(Fl_lnt, "Дорогой, любой лагерь возможно найти если постараться или повезению. Вот некотрых везунчиков ты уже успел заметить.")
    $ Fl.say(Fl_r, "Я вспомнил трупы, что преследовали меня на протяжение всего исследования странного лагеря.")
    
    $ Fl.Pause(2.5)
    $ Fl.say(Fl_q6, "Компьютер{mn}")
    $ Fl.say(Fl_lnt, "Ммм?")
    $ Fl.say(Fl_q6, "Компьютер в медпункте, это ведь список всех кто попал в твой лагерь до меня?")
    $ Fl.say(Fl_lnt, "Да, я заранее знаю кто посетит мой лагерь, поэтому обычно никто живой из него не выбирается. Следовательно и не знают в каком лагере я нахожусь.")
    $ Fl.say(Fl_q6, "Заранее? Разве список не вручную настраивается?")
    $ Fl.say(Fl_lnt, "Хех, ты такой забавный. Какой мне смысл вести этот список самой. Список обновляется каждый цикл и отображает кто появится в моём лагере.")
    $ Fl.say(Fl_th, "Что за чушь? Каким образом доисторическое железо может делать такие вычисления и предсказывать будущее?!")
    $ Fl.say(Fl_q6, "Я не понимаю...")
    $ Fl.say(Fl_lnt, "Не волнуйся, милый. Я и сама не знаю как он работает. Я получила эту штуковину от Парки.")
    $ Fl.say(Fl_th, "Доктор Парки!", _with=hpunch)
    $ Fl.say(Fl_r, "Чем чаще я слышал данное имя, тем больше злоси во мне закипало. Каждая новая информация о нём расскрывала его тёмную сущность.")
    $ Fl.say(Fl_q6, "Так ты с ним тоже связана, это он тебе эту силу дал?!")
    $ Fl.say(Fl_lnt, "А ты ревнуешь?")
    $ Fl.say(Fl_r, "Спросила Тихоня шёпотом возле моего уха.")
    $ Fl.say(Fl_r, "Но моё выражение лица чётко дало ей понять, что мне сейчас не до шуток.")
    $ Fl.say(Fl_lnt, "Нет, не связана. {w}Он сам мне предложил такую услугу, но ничего взамен не попросил.")
    $ Fl.say(Fl_th, "Ничего не попросил взамен? {w}Благодетель фигов...")
    $ Fl.say(Fl_th, "{mn2}")
    $ Fl.say(Fl_q6, "Если это твой лагерь, получается передо мной настоящая ты?")
    $ Fl.say(Fl_lnt, "Ян, я всегда была настоящей, разве {b}подделка{/b} может по-настоящему так сильно любить?")
    $ Fl.say(Fl_q6, "Я имею ввиду ты та, что создаёшь всех клонов.")
    $ Fl.say(Fl_lnt, "Аааа, ты об этом{mn}")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_lnt, "Возможно.")
    $ Fl.say(Fl_r, "Она одарила меня тёплой улыбкой, после чего продолжила диалог.")
    $ Fl.say(Fl_lnt, "Ну всё хватит с тебя вопросов. Теперь моя очередь задать вопросы тебе.")
    $ Fl.say(Fl_q6, "Мне?")
    $ Fl.say(Fl_th, "Какие могут быть вопросы в мою сторону у этой ненормальной.")
    $ Fl.say(Fl_lnt, "Я же сказала, никаких вопросов больше.")
    $ Fl.say(Fl_q6, "Знаешь, я устал. И не собираюсь отвечать на твои вопросы.")
    $ Fl.say(Fl_r, "Пионерка сделала удивлённое выражение лица.")
    $ Fl.say(Fl_q6, "Я собираюсь покинуть твой дурдом. {w}Убить тебя, а после по{break2}")
    $ Fl.say(Fl_lnt, "Ты никуда не пойдёшь!", _with=hpunch)
    $ Fl.say(Fl_r, "Я замер, Тихоня смотрела на меня пустым взглядом и подняла нож.")
    $ Fl.say(Fl_lnt, "Прости, не хотела тебя пугать.")
    $ Fl.say(Fl_lnt, "Зачем тебе куда-то уходить, Ян?")
    $ Fl.say(Fl_lnt, "Тебе не нужно знать правду о лагере, а вдруг с тобой что-то случиться?!")
    $ Fl.say(Fl_lnt, "Ты останешься со мной, я смогу тебя защитить. Никто не обидет моего Яна. Никто...")
    $ Fl.say(Fl_th, "{mn}")
    $ Fl.say(Fl_q6, "Остаться с тобой до конца своих дней?")
    $ Fl.say(Fl_lnt, "Да! {w}Я ради тебя сделаю что угодно!", _with=hpunch)
    $ Fl.say(Fl_th, "{mn}")
    $ Fl.say(Fl_r, "Я оскалился.")
    $ Fl.say(Fl_q6, "Тогда{mn}")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_q6, "Иди нахер, больная сучка!")
    $ Fl.say(Fl_q6, "Остаться с тобой? Да я лучше сдохну, чем проведу остаток дней на привязи чёкнутой Яндеры!")
    $ Fl.say(Fl_lnt, "{mn2}")
    $ Fl.StopMusic(5)
    $ Fl.say(Fl_r, "Тихоня затихла, её руки задрожали.")
    $ Fl.say(Fl_lnt, "Тогда{mn2}")
    $ Fl.say(Fl_lnt, "Тогда{mn}")
    show Fl_vignette with Fl_dissolve2
    $ Fl.say(Fl_lnt, "{color=#f00}Я УБЬЮ ТЕБЯ.{/color}")

    $ Fl.PlayMusic("Fl_no_tresspassing_remix", 1, 4)
    $ Fl.say(Fl_r, "Раздался слабый смешок, за ним же последовал продолжительный, после чего он перерос в громкий и истеричный.")
    $ Fl.say(Fl_lnt, "{color=#f00}УБЬЮ!{/color}", _with=hpunch)
    $ Fl.say(Fl_lnt, "{color=#f00}УБЬЮ!{/color}", _with=hpunch)
    $ Fl.say(Fl_lnt, "{color=#f00}УБЬЮ ТЕБЯ, ЯН!{/color}", _with=hpunch)
    $ Fl.say(Fl_r, "Тихоня повторяла одно и тоже вновь и вновь, заливаясь безумным смехом. Её зрачки были полностью пусты, в них отображалось - нет не безумие, а полный ужас, который охватил всё тело.")
    $ Fl.say(Fl_lnt, "{color=#f00}Ты правда думаешь, что я спокойно тебя отпущу.{/color}")
    $ Fl.say(Fl_q6, "Знаешь, было бы неплохо.")
    $ Fl.say(Fl_r, "Мой спокойный тон только сильнее сводил с ума пионерку.")
    $ Fl.say(Fl_lnt, "{color=#f00}Я тебе не нужна{mn}{/color}")
    $ Fl.say(Fl_lnt, "{color=#f00}АХАХАХАХ!{/color}", _with=hpunch)
    $ Fl.say(Fl_lnt, "{color=#f00}Раз я тебе не нужна, то и ты никому не достанешься!{/color}")
    $ Fl.say(Fl_lnt, "{color=#f00}Я убью тебя, только так смогу сохранить тебя, не дать другим украсть тебя у меня.{/color}")
    $ Fl.say(Fl_th, "У неё окончательно поехала крыша.")

    $ Fl.PlayMusic("Fl_no_tresspassing_remix2", 1, 4)
    $ Fl.Master(Fl_bghorrorflicker)
    $ Fl.say(Fl_r, "Тихоня подняла нож вверх.")
    $ Fl.say(Fl_lnt, "{color=#f00}Ты навсегда будешь моим!{/color}")
    $ Fl.say(Fl_r, "Замах.")
    $ Fl.say(Fl_th, "Давай, почти же!")
    $ Fl.say(Fl_r, "С самого пробуждения я пытался выпутаться из оков. Но развязать такое количество крепких узлов было проблемотично.")
    $ Fl.say(Fl_th, "А она всё предусмотрела. Выключила устройство, связала очень крепко нескольким количеством верёвок.")
    $ Fl.say(Fl_r, "Но Тихоня не заставила долго ждать, немного сменив траекторию ножа она устремила его прямо на меня.")
    $ Fl.say(Fl_th, "Готово!", _with=hpunch)
    $ Fl.say(Fl_r, "У меня было время чтобы нажать на устройство и прикончить её одним ударом.")
    $ Fl.say(Fl_r, "Вот только падение стула я никак не ожидал.")
    $ Fl.say(Fl_r, "Инстинкт самосохранения моментально сработал и я отвлёкся, а мозг пытался как-то минимизировать ущерб от падения, позабыв про сумашедшую с ножом.")
    $ Fl.say(Fl_th, "Да твою же!", _with=hpunch)
    $ Fl.PlaySound("Fl_knifehit", 1, 0, False)
    scene bg Fl_black with vpunch
    $ Fl.say(Fl_r, "Но не успел, я среагировать, как нож вонзился в правую ключицу.")
    $ Fl.say(Fl_th, "<С*ка>!", _with=vpunch)
    $ Fl.say(Fl_r, "Я попытался вскочить, но Тихоня сверху тут же надавила на новоиспечённую рану.")
    $ Fl.say(Fl_r, "Боль прошлась по всему телу, в данной ситуации было невозможно подняться.")
    $ Fl.say(Fl_lnt, "{color=#f00}Этот раз я не промохнусь. {w}Твоё сердце будет принадлежать только мне!{/color}")
    $ Fl.say(Fl_q6, "Да хрен тебе, поехавшая!")
    $ Fl.say(Fl_r, "Я брыкался, но не смог скинуть Тихоню с себя. Тело сильно ослабло, а вот силе пионерке наоборот не занимать.")
    $ Fl.say(Fl_r, "Очередной замах.")
    $ Fl.say(Fl_th, "Я не помру здесь, я должен...")
    $ Fl.say(Fl_kt, "Тебе здесь не место.")

    $ Fl.PlaySound("Fl_vzhuh", 1, 0, False)
    $ Fl.StopMusic(4)
    $ Fl.say(Fl_r, "Прямо на моих глазах Тихоня пропала.")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_r, "Передо мной стоял парень в мантии. Он убрал вытянутую руку обратно.")
    $ Fl.say(Fl_q6, "Что ты сделал? Почему не убил её?!")
    $ Fl.say(Fl_kt, "Она ненастоящая.")
    $ Fl.say(Fl_th, "Ненастоящая{mn} в её то лагере и ненастоящая?..")
    $ Fl.say(Fl_r, "Фигура приблизилась, после чего присела на корточки.")
    $ Fl.say(Fl_q6, "Кто ты такой?")
    $ Fl.say(Fl_kt, "Неважно кто я. Как я и сказал: «Тебе здесь не место.»")
    $ Fl.say(Fl_r, "Человек в мантии положил мне руку на плечо.")
    $ Fl.say(Fl_r, "В ту же секунду я потянулся к устройству...")

    $ Fl.PlaySound("Fl_vzhuh", 1, 0, False)
    $ Fl.say(Fl_r, "Но не успел.")
    $ Fl.HideScreens(_with=Fl_fast)

    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    scene Fl_desolation_bl 
    show Fl_vignette3
    with vpunch
    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Не успел я понять что вообще произошло, как больно рухнул на холодный бетон.")
    $ Fl.say(Fl_r, "Тело в очередной раз заныло. За всё это время я так и не смог нормально отдохнуть. Прыжки, сражение, снотворное ещё и сражение с нелучшим исходом сильно отразилось на мне.")
    $ Fl.say(Fl_th, "Да сколько можно{mn2} Дайте хотя бы передохнуть!")
    $ Fl.say(Fl_r, "Перспективы лежать на полу не было. Собравшись с силами, я встал.")
    $ Fl.HideScreens(_with=Fl_dissolve1)

    $ Fl.Pause(1.0)
    scene Fl_desolation_anim with Fl_dissolve3

    $ Fl.Pause(1.0)
    $ Fl.PlayAmbience("Fl_catacombs", 1, 4)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Встать удалось, тем самым усилив кровотечение раны, которую оставила в знак любви Тихоня.")
    $ Fl.say(Fl_r, "Оперевшись о стену, я принялся рыться по карманам.")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_th, "Да где эти чёртовы бинты?!", _with=hpunch)
    $ Fl.say(Fl_r, "И только сейчас я заметил, что с момента пробуждения на мне была пионерская форма.")
    $ Fl.say(Fl_q6, "Эта чёкнутая меня в пионера вырядила?!")
    $ Fl.say(Fl_r, "Я снял рубашку. Использовав подручное средство, в данном случае - пионерский галстук, перевязал крепко рану. Обработать было нечем. Зажигалка осталась вместе с бинтами в моей одежде.")
    $ Fl.say(Fl_r, "Накивнув на себя рубашку, я наконец-то решил осмотреться.")
    $ Fl.say(Fl_th, "Что это за место?")
    $ Fl.say(Fl_r, "Отдалёно напоминало бункер, но структура и размеры удивляли. Огромное количество металических дверей, напоминающие тюремные. Стены тоже имели странные очертание, выкрашенные в два цвета - белый и зелёный, как подъезд.")
    $ Fl.say(Fl_r, "Внутри камер, было темно. Сами двери не открыть.")
    $ Fl.say(Fl_q6, "Всё это время нечто подобное находилось в лагере?")
    $ Fl.say(Fl_r, "За дверьми располагался коридор.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(4.5)
    scene bg Fl_int_tunnel:
        Fl_walking1
    with Fl_dissolve2
    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Коридор больше напоминал катакомбы под старым корпусом.")
    $ Fl.say(Fl_th, "А может я действительно нахожусь под заброшенным корпусом?")
    $ Fl.say(Fl_r, "Лампы проложили мне путь, но впереди лишь густая тьма. Как и то что меня ожидает впереди.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.Pause(1.5)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(4.5)
    scene bg Fl_int_tunnel_with_door with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Минув сотню ламп, сбоку туннеля нарисовалась приоткрытая металическая дверь с вентилем.")
    $ Fl.say(Fl_r, "Думать долго не пришлось.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.PlaySound("Fl_open_door_mines_metal", 1, 0, False)
    $ Fl.Pause(2.5)
    scene bg Fl_int_laboratory with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Внутри оказалось всё куда интереснее.")
    $ Fl.say(Fl_q6, "Лаборатория?")
    $ Fl.say(Fl_r, "Глаза метались пытаясь зацепить каждую деталь, начиная с пробирок на полках, микроскопа, заканчивая различной радио техникой.")
    $ Fl.say(Fl_th, "Это ты мне хотел показать?")
    $ Fl.say(Fl_r, "Обратился я к неизвестному в мантии.")
    $ Fl.say(Fl_r, "Я разгуливал по лабораторной, вытирая пыль пальцами.")
    $ Fl.say(Fl_q6, "А Совёнок до сих пор способен удивлять.")
    $ Fl.say(Fl_r, "Неожиданно мои пальцы столкнулись с листами.")
    $ Fl.say(Fl_r, "Я взял в руки небольшую стопку листов. {w}Записи напоминали чей-то дневник.")
    $ Fl.HideScreens(_with=Fl_dissolve1)

    $ Fl.Pause(2.5)
    $ Fl.PlayMusic("Fl_Cyperpunk 2077 - Arasaka Clinic", 1, 5)
    show Fl_vignette3 
    show Fl_prolog_dream
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Deus.")
    $ Fl.say(Fl_th, "В этом году запустился наш проект. Очень удачно мы заприметили старую лабораторию в детском пионерлагере «Совёнок». Скрыть наши исследования не составило труда.")
    $ Fl.say(Fl_th, "А ещё можно было найти добровольцев, которые смогут послужить в советской науке.")
    $ Fl.say(Fl_th, "Честно когда начались смены в лагере я растроился. Младшие отряды никак не подходили на роль испытуемых. И половина лета прошла за исследованиями и способом улучшить наш проект.")
    $ Fl.say(Fl_th, "Точно я ведь не представился. {w}А нет, не хочу представляться, уверен моё настоящее имя вам не нужно знать. Да и я уверен на всех сто что проект удатся, тогда и раскрою свою личность.")
    $ Fl.say(Fl_th, "Так о чём это я? {w}Точно, наш провал спасла последняя смена. В этот раз приехали два старших отряда. Пионерам было по 17-18 лет.")
    $ Fl.say(Fl_th, "Теперь у нас точно получится!")
    $ Fl.say(Fl_th, "{mn2}")
    $ Fl.say(Fl_th, "Для выборов кандидатов я решил обратиться к местной медсестре - Виолетте Коллайдер. Она согласилась нам помочь и отдала медкарточки каждого пионера из страших отрядов.")
    $ Fl.say(Fl_th, "К сожалению идеальных кандидатов было всего четверо. Один из первого отряда и трое из второго.")
    $ Fl.say(Fl_th, "Как упоминалось ранее, это добровольное соглашение участвовать в нашем проекте. Кандидатам полагалось очень солидное вознаграждение за помощь в науке.")
    $ Fl.say(Fl_th, "Первый кандидат согласился и мы провели его в нашу лабораторию.")
    $ Fl.say(Fl_th, "Но никому не объяснялось что именно их ждёт. Всё что было известно - помощь в науке медицины и пара процедур.")
    $ Fl.say(Fl_th, "{mn2}")
    $ Fl.say(Fl_th, "Нас постиг провал. После двух экспериментов пионер потерял связь с реальностью. Парень не мог говорить, не мог самостоятельно ходить. Он будто умер внутри, осталась лишь пустая оболочка.")
    $ Fl.say(Fl_th, "Продолжать эксперименты было бессмысленно.")
    $ Fl.say(Fl_th, "Вожатые старших отрядов и директор всё знали, поэтому когда пионер вернулся обратно они за ним ухаживали какое-то время, но очень быстро сдались и позвонили родителям чтобы его забрали.")
    $ Fl.say(Fl_th, "Увидев сына, они пригрозили что подадут в суд на лагерь, но было бесполезно. Я был слишком важной персоной, только поэтому директор лагеря согласился сотрудничать, я дал взамен ему защиту и слово, что всю ответственность беру на себя.")
    $ Fl.say(Fl_th, "Было жаль парня. Я правда не хотел чтобы такое произошло. Неужели мы где-то ошиблись?")
    $ Fl.say(Fl_th, "{mn2}")
    $ Fl.say(Fl_th, "Со вторым кандидатом было всё намного лучше. Пионерка смогла зайти куда дальше и даже появился какой-то результат.")
    $ Fl.say(Fl_th, "Её прогресс дал нам надежду. Ещё немного и мы бы сделали прорыв в науке!")
    $ Fl.say(Fl_th, "{mn2}")
    $ Fl.say(Fl_th, "Мне трудно писать, рука дрожит. Я не могу поверить...")
    $ Fl.say(Fl_th, "Сегодня должен был пройти очередной эксперимент. Но с самого начала пошла череда странностей. Пионерка жаловалась на мигрени в последние дни и бессоницы. Я списал всё на побочные эффекты от процедур и провёл её в комнату.")
    $ Fl.say(Fl_th, "Господи, лучше бы я тогда отложил процедуры. Мне трудно описать что произошло, но я постараюсь.")
    $ Fl.say(Fl_th, "После очередного эксперимента всё было хорошо, пионерка лишь попросила какие-то таблетки от головы. Я попросил помощника поискать что-то в шкафу, но стоило мне отвернуться как произошло следующее.")
    $ Fl.say(Fl_th, "Истошный крик девочки, а после она крепко схватилась за голову.")
    $ Fl.say(Fl_th, "Я сразу же к ней подбежал. И прямо на моих глазах она начала царапать себе лицо...")
    $ Fl.say(Fl_th, "Я пытался её остановить, но это было бесполезно, она толкнула меня и не с силой обычной хрупкой девушки.")
    $ Fl.say(Fl_th, "А после она начала наносить себе больше увечий и кричать: «Уйдите из моей головы. Они повсюду!»")
    $ Fl.say(Fl_th, "От ужаса я так и не смог пошевелиться, в конце концов девушка лежала на полу в собственной луже крови. Её лицо было изуродовано, а шея вскрыта собственными ногтями.")
    $ Fl.say(Fl_th, "Простите, я не могу больше писать это...")
    $ Fl.say(Fl_th, "{mn2}")
    $ Fl.say(Fl_th, "Смерть пионерки выдали за нападение диких зверей, её тело пришлось вывезти глубоко в лес у ближайщей деревушки от лагеря. Местные и известили милицию о трупе в лесу.")
    $ Fl.say(Fl_th, "По данным девушка сама сбежала из лагеря и пыталась совершить такое неоднократно, поэтому вину вожатой второго отряда решили сгладить, да и я об этом позаботился.")
    $ Fl.say(Fl_th, "Шли бессонные ночи, но наконец-то я понял в чём была ошибка тогда. Я не хотел останавливаться, я был слишком близок. Поэтому в лаборатории появился третий кандидат.")
    $ Fl.say(Fl_th, "Им являлся парнишка довольно крепкого телосложения, а все его показатели были идеальные. Теперь точно всё должно получиться.")
    $ Fl.say(Fl_th, "Точнее должно было...")
    $ Fl.say(Fl_th, "Пионер развивался куда быстрее, но в конечном счёте сошёл с ума. У него развилась шизофрения и другие психические наклонности. Я был зол, очень зол.")
    $ Fl.say(Fl_th, "От парня мы так же избавились, спихнув его обратно родителям.")
    $ Fl.say(Fl_th, "Оставался последний кандидат, её я решил оставить на крайний случай. Причиной тому стали показатели, среди других претендентов они были хуже всего.")
    $ Fl.say(Fl_th, "{mn2}")
    $ Fl.say(Fl_th, "Я не верил своим глазам, среди всех остальных пионерка выдерживала все процедуры и явных побочных эффектов не наблюдалось.")
    $ Fl.say(Fl_th, "Смена близилась к концу, поэтому я участил эксперименты. Каждый из них приводил меня всё ближе к цели. Я был счастлив, что не сказать о пионерке.")
    $ Fl.say(Fl_th, "Она просила уменьшить количество экспериментов, так как ей больно и трудно отходить от них.")
    $ Fl.say(Fl_th, "Но какое мне дело до какой-то девчонки. Я был близок к цели!")
    $ Fl.say(Fl_th, "Она хотела отказаться от участия, но мне повезло. У неё был только отец и жили они в нищите. Отец работал на нескольких работах и почти не виделся с дочкой.")
    $ Fl.say(Fl_th, "Я ей пообещал, что вытащу её семью из нищиты. Работа, машина, квартира, лучшее образование - всё это если она сыграет свою роль. Ведь тогда она сможет видиться чаще со своим папочкой.")
    $ Fl.say(Fl_th, "Когда она молча согласилась на продолжение экспериментов, я стал проводить их ещё больше. Но пионерка вновь начала умолять меня остановить это, но я устал...")
    $ Fl.say(Fl_th, "На этот раз я проводил её до своей лаборатории. Закрыл за собой дверь, после чего дал ей сильной подщёчины.")
    $ Fl.say(Fl_th, "Теперь я не говорил, что она получит взамен. Я угрожал ей, что если она откажется, то отец лишится работы и возможности куда-то устроиться, а всё имущество будет конфисковано.")
    $ Fl.say(Fl_th, "В её заплаканных глазах читался страх. Я осознал что творю, но было поздно. Мы почти достигли то чего хотели. Такой рывок в науке стоит любых жертв...")
    $ Fl.say(Fl_th, "{mn2}")
    $ Fl.say(Fl_th, "Пионерка медленно превращалась в ходячий труп, она почти не ела, много спала и каждый раз проходила эксперименты. Ей уже было не больно, она молча их проходила и демонстрировала результат, а после уходила.")
    $ Fl.say(Fl_th, "Сегодня должен быть день отъезда, поэтому я обязан провести финальный эксперимент...")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(5)
    $ Fl.Pause(1.5)
    hide Fl_vignette3 
    hide Fl_prolog_dream
    with Fl_dissolve2


    $ Fl.Pause(2.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Запись оборвалась. Это был последний листок.")
    $ Fl.say(Fl_th, "Решил не упоминать свого имени... {w}Доктор Парки?")
    $ Fl.say(Fl_th, "Старая ведьма говорила правду, она действительно помогла безумному учёному достичь своего.")
    $ Fl.say(Fl_th, "{mn}")
    $ Fl.say(Fl_th, "Последняя испытуемая была пионеркой из первого отряда...")
    $ Fl.say(Fl_q6, "Юля...")
    $ Fl.say(Fl_r, "Мне трудно было представить через что в прошлом прошла Богиня этого мира. Но ответ был близок, достаточно было найти того кто превратил её в чудовище.")
    $ Fl.say(Fl_r, "Почему достаточно? {w}Я уверен что такого места не существует в других лагерях, а значит Парки тоже здесь находится.")
    $ Fl.say(Fl_r, "Ответы находились здесь. Я сразу же принялся оглядывать все существующие бумаги и записки.")

    $ Fl.Pause(2.5)
    $ Fl.say(Fl_r, "В поле зрения попал приоткрытый ящик в столе.")
    $ Fl.say(Fl_q6, "А тут что у нас?")
    $ Fl.say(Fl_r, "Внутри ящика лежали документы. {w}Всё о сказителях...")
    $ Fl.say(Fl_th, "Это я?")
    $ Fl.say(Fl_r, "На самом верху стопки лежал документ с моими данными.")
    $ Fl.say(Fl_th, "Номер: Q-66. Настоящее имя: Ян. Прозвище: - .")
    $ Fl.say(Fl_r, "Но кое-что меня зацепило сильнее всего.")
    $ Fl.say(Fl_th, "Способнос{break2}")
    with vpunch
    $ Fl.say(Fl_r, "Резко мои ноги подкосили и я в последний момент успел удержаться рукой за поверхность стола.")
    $ Fl.say(Fl_q6, "Кх!", _with=hpunch)
    $ Fl.say(Fl_r, "В ту же секунду я испытал адскую боль. Её причиной послужила рука, на которую я совершил опору.")
    $ Fl.say(Fl_r, "Из ключицы хлынула кровь. Рана вновь открылась, рука затряслась.")

    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    show Fl_prolog_dream with vpunch
    $ Fl.say(Fl_th, "Что твою мать со мной происходит?!", _with=hpunch)
    $ Fl.say(Fl_r, "Я окончательно свалился на пол, стопка листов разлетелась.")
    scene bg Fl_black with Fl_dissolve2
    $ Fl.StopAmbience(4)
    $ Fl.say(Fl_r, "Листы и серая плитка - последнее что я увидел перед тем как отключился.")
    $ Fl.HideScreens(_with=Fl_dissolve2)


    $ Fl.Pause(9.0)
    $ Fl.DayTime("prologue", "night")
    $ Fl.PlayAmbience("Fl_bizzard_outside", 0.8, 2)
    $ Fl.Pause(9.0)
    scene bg Fl_ext_entrance_winter
    show Fl_snow at Fl_linear_effects_repeat(0.7, 0.75, 0.7, 0.75, 0.25, 0.3, 0.25)
    with Fl_dissolve3
    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Я стоял у ворот Совёнка. Моё удивление засыпала метель. Каждая снежинка резала кожу лица.")
    $ Fl.say(Fl_r, "Мне удалось словить на ладонь снежинку, но она тут же растаяла оставив холодный след и небольшую лужу.")
    $ Fl.say(Fl_q6, "Как так вышло?")
    $ Fl.say(Fl_r, "Попытка вспомнить что случилось не увенчалась успехом, а пальто на мне ещё сильнее вводило меня в ступор.")
    $ Fl.say(Fl_th, "Неужели цикл перезапустился?")
    $ Fl.say(Fl_r, "Возникла одна из теорий в моей голове. {w}Если совершить прыжок в конце цикла, то спокойно можно всё перезапустить.")
    $ Fl.say(Fl_q6, "Зима{mn2} Как же давно я тебя не видел.")
    $ Fl.say(Fl_r, "Было трудно описать словами свои чувства и эмоции, я словно впервые попал в пионерлагерь и вновь стою у ворот и чего-то жду.")
    $ Fl.say(Fl_th, "Или кого-то...")
    $ Fl.say(Fl_r, "Неожиданно на лице расплылась тёплая улыбка.")
    $ Fl.say(Fl_th, "Помню как тут впервые познакомился с Толяном.")
    $ Fl.say(Fl_r, "Но улыбка тут же пропала.")
    $ Fl.say(Fl_th, "Что же я натворил. Почему так вышло, что из всего отряда остался я один...")
    $ Fl.say(Fl_r, "С отвращением я поплёлся ко входу. В этот раз меня уже никто не встретит. И уже никогда...")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(3.5)
    scene bg Fl_ext_houses_winter
    show Fl_snow at Fl_linear_effects_repeat(0.7, 0.75, 0.7, 0.75, 0.25, 0.3, 0.25)
    with Fl_dissolve2
    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "За столько лет меня уже было невозможно чем-то удивить в лагере, но снежный пейзаж поистине завораживает.")
    $ Fl.say(Fl_r, "Холод меня мало волновал, да и старое пальто хоть немного, но справлялось с морозом.")
    $ Fl.say(Fl_th, "Интересно, как там сейчас в моём мире?")
    $ Fl.say(Fl_r, "На меня нахлынули воспоминания былых дней, когда я ещё был живой. Как я жил, знакомых, школу, родителей...")
    $ Fl.say(Fl_th, "Родители{mn2} Хех, наверное скорбят по мне. Это даже лучше, что они не могут увидеть во что их сын превратился.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(3.5)
    scene bg Fl_ext_dining_hall_near_winter
    show Fl_snow at Fl_linear_effects_repeat(0.7, 0.75, 0.7, 0.75, 0.25, 0.3, 0.25)
    with Fl_dissolve2
    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Ноги сами меня привели к веранде столовой.")
    $ Fl.say(Fl_r, "Снег всё смог преобразить. Лагерь заиграл новыми красками, но отсуствие зелени не сделало это место менее ярким и насыщенным.")
    $ Fl.say(Fl_r, "Вдаваясь в детали, я резко замер.")
    $ Fl.say(Fl_r, "За спинкой лавочки было видно, что я здесь не один.")
    $ Fl.say(Fl_r, "Два хвостика задорно подрагивали от холода. {w}Но не простые хвостики, а самого необычного цвета.")
    $ Fl.say(Fl_th, "Аквамариновый...")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_th, "Это невозможно.")
    $ Fl.say(Fl_q6, "М- {w}М- {w}М...")
    $ Fl.say(Fl_r, "Мой голос дрожал, к горлу подкатил ком, я словно потерял дар речи от того что видел перед собой.")
    $ Fl.say(Fl_q6, "М- {w}Ми...")
    $ Fl.say(Fl_r, "Аквамариновые хвостики резко замерли и та кому они принадлежали обернулась в мою сторону.")

    $ Fl.PlayMusic("Fl_snowfall", 1, 5)
    $ Fl.say(Fl_r, "Девушка на секунду замерла, но тут же улыбнулась мне.")

    $ Fl.AttackScreens(True)
    $ Fl.say(Fl_r, "После чего подорвалась и побежала прямо ко мне. Заключив меня в объятия, она тихо проговорила:")
    $ Fl.say(Fl_mi, "Ян, это правда ты?")
    $ Fl.say(Fl_th, "Это какой-то бред, нереально...")
    $ Fl.say(Fl_q6, "М-Мику?")
    $ Fl.say(Fl_q6, "Нет-нет, ты же...")
    $ Fl.say(Fl_r, "Я оттолкнул пионерку от себя.")
    $ Fl.say(Fl_q6, "Ты же умерла тогда.")
    $ Fl.say(Fl_r, "Девушка на время опустила голову. {w}После чего подняла и с улыбкой на лице ответила:")
    $ Fl.say(Fl_mi, "Ага{mn} Та самая ночь. {w}Когда меня убил один из пионеров...")
    $ Fl.say(Fl_mi, "Я помню, тогда ты ушёл и велел мне остаться и никому не открывать, но меня нашли. Видно я плохо пряталась.")
    $ Fl.say(Fl_th, "Как{mn} {w}Как она может о таком говорить с такой невинной улыбкой на лице?!")
    $ Fl.say(Fl_mi, "Я помню, как ты пытался убедить пионера что можно поступить иначе, можно измениться. Что жестокость не выход, как бы не было тяжело.")
    $ Fl.say(Fl_mi, "Ян, ты плачешь?")
    $ Fl.say(Fl_th, "Плачу?")
    $ Fl.say(Fl_r, "Я провёл ладонью по лицу. На них остался след влаги.")
    $ Fl.say(Fl_th, "Это правда она.")

    $ Fl.AttackMaster()
    show Fl_belizna_eff with Fl_dissolve1
    $ Fl.say(Fl_r, "Я крепко обнял Мику, так сильно что чувствовал весь холод её хрупкого тельца.")
    $ Fl.say(Fl_q6, "Прости меня.")
    $ Fl.say(Fl_mi, "За что ты извиняешься?")
    $ Fl.say(Fl_q6, "В ту ночь... Я не смог спасти тебя, я был слишком слаб, чтобы защитить тебя от этого мрачного мира.")
    $ Fl.say(Fl_mi, "Всё в порядке, сейчас же я жива. И за столько циклов ты всё же нашёл меня.")
    $ Fl.say(Fl_q6, "Точно!")
    hide Fl_belizna_eff with Fl_dissolve1
    $ Fl.say(Fl_r, "Отпустив Мику, я быстро снял с себя пальто.")
    $ Fl.say(Fl_q6, "Держи.")
    $ Fl.say(Fl_r, "Пионерка с удивлением посмотрела на меня, а когда до неё дошло, то сразу мне возразила.")
    $ Fl.say(Fl_mi, "Ну уж нет! Я не хочу чтобы ты рядом дрожал от холода!")
    $ Fl.say(Fl_q6, "Тогда что ты предлагаешь?")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(3.5)
    scene bg Fl_ext_houses_winter
    show Fl_snow at Fl_linear_effects_repeat(0.7, 0.75, 0.7, 0.75, 0.25, 0.3, 0.25)
    with Fl_dissolve2
    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "В итоге Мику ничего лучше не придумала, как укрыться вдвоём под одним пальто.")
    $ Fl.say(Fl_r, "Не то чтобы я возражал, но идти согнувшись было как-то не очень. Да и из-за этого нас двоих это сильно тормозило. Хотя куда мне торопиться.")
    $ Fl.say(Fl_r, "Мику на фоне что-то рассказывала о себе. Из раза в раз пар поднимался в воздух, а мне лишь оставалось с интересом и улыбкой слушать всё что говорит аквамариновое чудо.")
    $ Fl.say(Fl_mi, "А ты изменился.")
    $ Fl.say(Fl_r, "Я грустно опустил голову вниз.")
    $ Fl.say(Fl_mi, "Прости прости, я не хотела тебя обидеть! Просто седина и странная штука на твоей шее не даёт мне покоя.")
    $ Fl.say(Fl_q6, "А ты об этом.")
    $ Fl.say(Fl_q6, "Много чего произошло...")
    $ Fl.say(Fl_r, "Между нами повисла неловкая тишина.")

    $ Fl.Pause(2.5)
    $ Fl.say(Fl_mi, "Когда будешь готов, я с радостью тебя выслушаю!")
    $ Fl.say(Fl_r, "От улыбки Мику на душе стало тепло. В моих кристально чистых зрачках создавалась искра - надежда на яркое пламя, сила которой мне так не хватало.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(3.5)
    scene bg Fl_house_of_mt_day_winter
    show Fl_snow at Fl_linear_effects_repeat(0.7, 0.75, 0.7, 0.75, 0.25, 0.3, 0.25)
    with Fl_dissolve2
    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "На нашем пути показался домик вожатой. Окружение немного изменилось. Вместо привычного шезлонга с велосипедом, в снегу стояли лыжи и санки.")
    $ Fl.say(Fl_q6, "А у вожатой случайно нет тёплой одежды?")
    $ Fl.say(Fl_mi, "Нет, я здесь всё обыскала и ничего не нашла. Ещё тут каждое здание заперто, поэтому мне когда-то с трудом довелось обыскать каждый домик.")
    $ Fl.say(Fl_th, "Странно, неужели Мику каждый цикл приходилось бороться с холодом в одной пионерской форме?")
    $ Fl.say(Fl_r, "Мику взяла меня за руку и потащила дальше.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(3.5)
    scene bg Fl_ext_musclub_day_winter
    show Fl_snow at Fl_linear_effects_repeat(0.7, 0.75, 0.7, 0.75, 0.25, 0.3, 0.25)
    with Fl_dissolve2
    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Шагая по заснеженной дорожке и слушая хруст снега под ногами, мы молча подходили к музклубу.")
    $ Fl.say(Fl_th, "Наше с ней укрытие...")
    $ Fl.say(Fl_r, "Пионерка остановилась и ласково посмотрела мне прямо в глаза.")
    $ Fl.say(Fl_mi, "Ян, тебя что-то беспокоит?")
    $ Fl.say(Fl_r, "Мику широко улыбнулась. {w}Её улыбка была словно, 8 чудо света.")
    $ Fl.say(Fl_mi, "Не волнуйся, я ведь рядом!")
    $ Fl.say(Fl_th, "{mn2}")
    $ Fl.say(Fl_q6, "Всё в порядке.")
    $ Fl.say(Fl_r, "Но на моём лице улыбки не появилось.")
    $ Fl.say(Fl_mi, "Янечка, пошли уже в музклуб!")
    $ Fl.say(Fl_r, "С этими словами пионерка вырвалась с нашего мехового убежища в сторону музклуба.")
    $ Fl.say(Fl_mi, "Ну ты чего, встал как вкопанный? Замёрзнешь ведь!")
    $ Fl.StopMusic(4)
    $ Fl.Pause(1.5)
    $ Fl.say(Fl_q6, "Прости, я никуда с тобой не пойду.")
    $ Fl.say(Fl_r, "Улыбка тут же пропала с лица девушки.")
    $ Fl.say(Fl_q6, "Ты же ведь не Мику?")
    $ Fl.say(Fl_mi, "Ты о чём, Ян? Я ведь...")
    $ Fl.say(Fl_q6, "Да ты рассказывала про свою смерть, о воспоминаниях со мной, но ты не она.")
    $ Fl.say(Fl_q6, "Мне показалось слишком странным. Как хрупкая девушка смогла пережить столько циклов без тёплой одежды, без отопления, ведь это логично раз лагерь пустой, то и не настроен на то чтобы в нём кто-то жил, поэтому про электричество и прочие блага цивилизации можно забыть.")
    $ Fl.say(Fl_q6, "Любой человек в таких условиях умрёт от переохлождения или голода. Лагерь максимально не пригодный для жизни, если в нём нет кукол.")
    $ Fl.say(Fl_mi, "Но это возможно! В начале было всё так как ты описывал, но за столько циклов я научилась переживать целые циклы.")
    $ Fl.say(Fl_q6, "Тогда вторая странность.")
    $ Fl.say(Fl_q6, "За такой короткий промежуток времени ты всегда была такой какой я тебя помню, нет ты боялась отойти от сценария поведения из моих вопоминания.")
    $ Fl.say(Fl_q6, "А сейчас ты говоришь что действительно умирала из раза в раз. Ни один человек не способен сохранить своё «Я», после пережитого.")
    $ Fl.say(Fl_q6, "И ты серьёзно думаешь я поверю, что возможно прожить в холодном аду в придачу ещё и в полном одиночестве и ни капельки не измениться?")
    $ Fl.say(Fl_q6, "Но ты не изменилась.")
    $ Fl.say(Fl_q6, "И последнее что тебя выдало. {w}Мику никогда не обращалась ко мне уменьшительно ласкательно.")
    $ Fl.say(Fl_r, "Мику молча отвернулась и встала спиной ко мне на против входа в лес. {w}Она подняла голову вверх. Я надеялся до последнего.")
    $ Fl.say(Fl_mi, "Ты прав, твоя Мику умерла.")
    $ Fl.StopAmbience(5)
    $ Fl.Pause(1.5)
    scene bg Fl_ext_musclub_night3 with Fl_dissolve5
    $ Fl.say(Fl_r, "На моих глазах снег начал исчезать, а тьма словно куполом обрушилась на ясное небо.")
    $ Fl.say(Fl_r, "Мику медленно повернулась в мою сторону.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause(1.5)
    $ Fl.PlayMusic("Fl_psychoflashback", 1, 6)
    scene cg Fl_mi_dark with Fl_dissolve2
    $ persistent.Fl_photo_pallery_30 = True
    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Это была больше не Мику, нечто странное пилило меня двумя большими белыми фонариками вместо глаз. Тело потеряло физическую форму, превратившись в какую тёмную тень.")
    $ Fl.say(Fl_r, "Само окружение тоже потерпело изменение, лагерь сменил время года, а небо приобрело беззвёздное небо. Даже луна мало что могла осветить, казалось существо что стояло передо мной поглощало любой источник света.")
    $ Fl.say(Fl_mi, "Ведь это я отдал приказ убить её.")
    $ Fl.say(Fl_r, "Неожиданно заговорило оно.")
    $ Fl.say(Fl_th, "Отдал приказ...")
    $ Fl.say(Fl_q6, "Кукловод!", _with=hpunch)
    $ Fl.say(Fl_setk, "Эх, а я планировал тебя заточить в эту иллюзию до конца твоих дней. А ты даже и суток не продержался.")
    $ Fl.say(Fl_setk, "Быстро же ты раскусил подделку от реальности.")
    $ Fl.say(Fl_q6, "Что это за место?")
    $ Fl.say(Fl_setk, "Я же говорю, иллюзия.")
    $ Fl.say(Fl_q6, "Не строй из себя идиота, ты прекрасно понимаешь о чём.")
    $ Fl.say(Fl_q6, "Ты ведь сейчас тоже в той лаборатории?")
    $ Fl.say(Fl_setk, "Так вот о чём идёт речь. {w}Допустим, что с того? Придёшь, убьёшь меня?")
    $ Fl.say(Fl_r, "Я ухмыльнулся.")
    $ Fl.say(Fl_th, "Насколько же он самоуверен!")
    $ Fl.say(Fl_q6, "Это место - лаборатория доктора Парки? Это тебе имя уж должно быть знакомо.")
    $ Fl.say(Fl_setk, "Поздравляю, шерлок, ты стал чуть ближе к разгадке.")
    $ Fl.say(Fl_setk, "А теперь. {w}Раз ты тут, то я бы хотел узнать, каким образом тебя занесло сюда. Знаешь, незванным гостям никто не рад.")
    $ Fl.say(Fl_th, "{mn2}")
    $ Fl.say(Fl_setk, "Бесполезно, ещё никто не понял как именно всё работает. Поэтому думать о другом бессмысленно.")
    $ Fl.say(Fl_setk, "Но я удивлён, как ты сразу сообразил, что мой вопрос не нуждается прямого ответа словами.")
    $ Fl.say(Fl_r, "Кукловод был прав, после поставленного вопроса, я постарался думать о чём угодно лишь бы оно не было связано с последними событиями этого цикла.")
    $ Fl.say(Fl_setk, "Тебя перенёс сюда «Пустой». Неожидал я от него такого.")
    $ Fl.say(Fl_th, "Это прозвище того парня в мантии?")
    $ Fl.say(Fl_q6, "Теперь я начинаю понимать, что у тебя за способность и откуда такое прозвище.")
    $ Fl.say(Fl_setk, "Честно мне плевать. До тебя и другие догадывались, но это последнее что они узнали в своей жизни.")
    $ Fl.say(Fl_q6, "Раз ты здесь, то почему просто не убил меня, а заключил в иллюзию?")
    $ Fl.say(Fl_setk, "Не вижу смысла тратить время на очередной неудачный эксперимент, ты рано или поздно сам себя уничтожишь.")
    $ Fl.say(Fl_th, "Очередной неудачный эксперимент? О чём он вообще?")
    $ Fl.say(Fl_r, "Слова Кукловода словно эхом отдавались в моей голове. Я искринне не понимал о чём шла речь, а догадки сбивали ровное дыхание, выдавая мою слабость перед лжебогом.")

    show Fl_prolog_dream with Fl_dissolve2
    $ Fl.say(Fl_setk, "Упс, наше время подходит к концу. Скоро ты выберешься из иллюзии.")
    $ Fl.say(Fl_r, "Иллюзия начала искажаться, тьма сильнее охватывала всё вокруг, погружая в непроглядный мрак - пустоту.")
    $ Fl.say(Fl_setk, "Дам тебе совет. Получи здесь все ответы и возвращайся в свой лагерь.")
    $ Fl.say(Fl_q6, "Только через твой труп!")
    scene bg Fl_black with Fl_effect_6
    $ Fl.StopMusic(5)

    $ Fl.say(Fl_r, "В конце существо, напоминавшее Мику, ухмыльнулось, после чего иллюзия распала на части.")
    $ Fl.HideScreens(_with=Fl_dissolve2)


    $ Fl.Pause(6.5)
    $ Fl.DayTime("rain", "night")
    $ Fl.PlayAmbience("Fl_catacombs", 1, 4)
    scene bg Fl_int_laboratory with Fl_dissolve2
    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Очнулся я вновь в лаборатории. Всё выглядело точно так же, как до моей отключки.")
    $ Fl.say(Fl_r, "Кулак на левой руке был сильно сжат. Причиной тому послужило моё желание сохранить лист бумаги, на котором содержалась информация обо мне.")
    $ Fl.say(Fl_th, "Точно.")
    $ Fl.say(Fl_r, "Немного пристав, я подполз к столу и облокотился к нему спиной.")
    $ Fl.say(Fl_r, "Не став медлить, я вернулся на чём остановился.")
    $ Fl.say(Fl_th, "Q-66. Способность: {w}Хаус.")
    $ Fl.say(Fl_q6, "{mn}")
    $ Fl.say(Fl_r, "Я продолжил читать.")
    $ Fl.say(Fl_th, "Хаус - безграничная способность, носителю подвластно любое искажение реальности. Хаус - способен как создавать, так и уничтожать всё вокруг.")
    $ Fl.say(Fl_th, "Использование данной способности зависит только от Сказителя. Примечание, требуется огромная концентрация, своими мыслями носитель способен сделать что угодно.")
    $ Fl.say(Fl_q6, "<Нихрена> понятнее не стало.")
    $ Fl.say(Fl_q6, "Но Импостер была права, ошейник не являлся моей силой.")
    $ Fl.say(Fl_q6, "Только вот как теперь разобраться с той информацией что я получил о настоящей своей способности?")
    $ Fl.say(Fl_r, "Я потянулся в карман за пачкой сигарет. Но как ожидалось, карманы были пусты.")
    $ Fl.say(Fl_th, "Твою ж, Тихоня!")
    $ Fl.say(Fl_r, "Не сказать что я был огорчён, но сигареты помогли бы обмозговать информацию.")
    $ Fl.say(Fl_r, "Разочарованный я потянулся к остальным листам с данными о сказителях.")

    $ Fl.Pause(2.5)
    $ Fl.say(Fl_th, "Номер: R-34. Настоящее имя: Ульяна. Прозвище: Псионик.")
    $ Fl.say(Fl_q6, "А это разве не та малявка, к которой приставали пионеры на пристани?")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_effect_6


    $ Fl.Pause(4.0)
    scene bg Fl_int_laboratory with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Я перечитал много бумаг, как оказалось Парки много о чём не договаривал, сказителей больше чем шесть, включая меня.")
    $ Fl.say(Fl_r, "Но кое-что меня беспокоило намного сильнее, среди сказителей я не нашёл никакой информации о Кукловоде, его данных не было.")
    $ Fl.say(Fl_th, "Неужели ради этого ты заточил меня в иллюзию? Ты не хотел чтобы я узнал что-то о тебе...")
    $ Fl.say(Fl_th, "Но если Парки и Кукловод так долго хранили тайну о моей способности, то почему мои данные не пропали?")
    $ Fl.say(Fl_r, "И тут я кое-что вспомнил.")
    $ Fl.say(Fl_th, "Точно, я же до конца держался за лист с моими данными! Если Кукловод действительно был здесь, то понятно почему он не смог уничтожить записи обо мне.")
    $ Fl.say(Fl_r, "Остался последний листок. Данные этого Сказителя я уже знал. {w}Они принадлежали красноволосой извращенке.")
    $ Fl.say(Fl_q6, "Так твоё настоящее имя - Лиза.")
    $ Fl.say(Fl_r, "Я улыбнулся.")
    $ Fl.say(Fl_r, "Исследования не дали мне ничего нового. Но меня привлёк пункт в самом низу, его не было на прошлых листовках.")
    $ Fl.say(Fl_th, "Статус: Устранена.")
    $ Fl.say(Fl_r, "Рука сама по себе сжалась в кулак.")

    $ Fl.PlayMusic("Fl_doubled", 1, 5)
    $ Fl.say(Fl_q6, "Устранена{mn}")
    $ Fl.say(Fl_q6, "Это ведь ты её убил?")
    $ Fl.say(Fl_q6, "Так ведь?!", _with=hpunch)
    $ Fl.say(Fl_r, "Меня переполняла ярость, тот к кому я обращался явно слышал мой крик. Я чувствовал его ухмылку из тени.")
    $ Fl.say(Fl_q6, "Хочешь ещё присвоить мне смерть человека, за то что ему не повезло встретиться со мной?!", _with=hpunch)
    $ Fl.say(Fl_th, "Дура, зачем?! {w}Ради чего ты пошла против Кукловода?")
    $ Fl.say(Fl_q6, "Убью{mn}")
    $ Fl.PlaySound("Fl_table_hit", 1, 0, False)
    $ Fl.say(Fl_q6, "Слышишь, тварь?! Я убью тебя!", _with=hpunch)
    $ Fl.say(Fl_r, "Со злости я ударил по дверце шкафчика. Оттуда выпали ещё какие-то бумажки.")
    $ Fl.say(Fl_r, "Я молча их подобрал и принялся читать.")

    show Fl_vignette3 
    show Fl_prolog_dream
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Проект: Передача способности одного сказителя другому.")
    $ Fl.say(Fl_th, "Цель данного проекта извлечь силу одного сказителя и передать её другому. Данный эксперимент будет проводиться впервые, его результаты будут не предсказуемые. Вероятнее сегодня летальный исход для пациента А(подопытный).")
    $ Fl.say(Fl_th, "Пациент В(получатель новой силы) получит минимальные побочные эффекты при неудачи. {w}Начиная от невозможности использовать новую способность или повреждением разума, из-за чего возможна редкая потеря контроля своей силы.")
    $ Fl.say(Fl_th, "В худшем исходе, пациент В может потерять собственную способность. Но такое может произойти только в том случае если сам носитель слабый и не до конца разобрался со своей способностью.")
    $ Fl.say(Fl_th, "Пациентом А выступит R-34, Псионик. Пациентом В является P-01, Кукловод.")
    $ Fl.StopMusic(4)
    hide Fl_vignette3 
    hide Fl_prolog_dream
    with Fl_dissolve2

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_th, "{mn2}")
    $ Fl.say(Fl_th, "Собираетесь провести опыт с маленькой девочкой чтобы этот лжебог стал ещё сильнее.")
    $ Fl.say(Fl_th, "А я погляжу у тебя серьёзные намерения, Кукловод.")
    $ Fl.say(Fl_q6, "Вот только{mn}")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause(2.0)
    $ Fl.DayTime("kira", "night")
    $ Fl.PlayMusic("Fl_bloodwork", 1, 5)
    $ Fl.say(Fl_q66, "Я разрушу все ваши планы!", _with=vpunch)
    $ Fl.say(Fl_r, "Дикий хохот залился по всему помещению, казалось что он эхом разбегается по всему туннелу.")
    $ Fl.say(Fl_q66, "И вы говорите я чудовище? Я псих?")
    $ Fl.say(Fl_q66, "Тогда кто вы?! Ради своей цели проводите дикие опыты над детьми, а после выкидываете словно мусор в случае неудачи.")
    $ Fl.say(Fl_r, "Я подошёл к двери, схватив одной рукой край двери, я высунул голову в бесконечный тунель. Мой дикий взгляд метался из стороны в сторону.")
    $ Fl.say(Fl_q66, "Теперь моя очередь делать ход, я сотру вашу довольную ухмылку. Покажу вам прах ваших идеалов!")
    scene bg Fl_int_tunnel_with_door with vpunch

    $ Fl.say(Fl_r, "Выскочив в туннель, я включил устройство.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause(1.0)
    scene bg Fl_mine_elevator_down with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Туннель окозался довольно таки длинным. Но мне удалось очень быстро дойти до тупика.")
    $ Fl.say(Fl_q66, "Грузовой лифт?")
    $ Fl.say(Fl_r, "Недолго думая, я затарабанил по кнопке «Вверх», что располагалась слева от решётки.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.PlaySound("Fl_open_door_mines_metal", 1, 0, False)
    $ Fl.Pause(1.0)
    scene bg Fl_mine_elevator_up with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "После того как лифт оказался наверху, я уверенно зашагал в его сторону. Всё что я так долго искал, находилось в пресподне этого мира, оставалось лишь спуститься к тайне что покрыла мраком Совёнок.")
    $ Fl.say(Fl_q66, "Ну вот и мы вновь встретимся доктор Парки.")
    $ Fl.HideScreens(_with=Fl_dissolve2)
    scene bg Fl_black with Fl_dissolve3
    $ Fl.StopAmbience(4)
    $ Fl.StopMusic(5)


    $ Fl.Pause(8.5)

    scene Fl_q_66_4 with Fl_dissolve2
    show Fl_q_66_layer with Fl_effect_down1
    show Fl_q_66_text4 with Fl_dissolve1
    $ Fl.Pause (4.5)

    scene bg Fl_black with Fl_dissolve2
    $ Fl.Pause (7.5)


    $ Fl.DayTime("rain", "night")
    $ Fl.Save("Dls Одиночка:Глава 3")
    $ Fl.Pause (2.5)


    scene bg Fl_bynker_pr
    show Fl_vignette3 
    show Fl_prolog_dream
    with Fl_dissolve2
    $ Fl.PlayAmbience("Fl_catacombs", 1, 6)
    $ Fl.ShowScreens(_with=Fl_dissolve2)
    $ Fl.say(Fl_r, "В пустых коридорах раздавались быстрые шаги. Человек в белом халате бежал слишком быстро, задыхался.")
    $ Fl.say(Fl_r, "Шаги прекратились, дверь распахнулась за ней давно стоял и поджидал другой человек в халате.")
    $ Fl.say(Fl_r, "Человек в очках и зажмуренным одним глазом перевёл взгляд на бегуна.")
    $ Fl.say(Fl_unk1, "Тревога!")
    $ Fl.say(Fl_unk1, "Хе-хе{mn} пхе т-там...")
    $ Fl.say(Fl_r, "Речь была не закончена, её остановила игривая ухмылка персоны в очках.")
    $ Fl.say(Fl_par, "Я знаю. Он пришёл.")
    $ Fl.say(Fl_unk1, "Ч-что нам делать?!")
    $ Fl.say(Fl_par, "Ничего.")
    $ Fl.say(Fl_unk1, "Как ничего?!")
    $ Fl.say(Fl_par, "Как же любопытно{mn} Как далеко ты зайдёшь, дитя хауса?")
    $ Fl.say(Fl_r, "Гонец вздрогнул и пошатнулся назад.")
    $ Fl.say(Fl_par, "Если хочешь можем вместе понаблюдать что будет дальше.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(4)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.DayTime("kira", "night")
    $ Fl.Pause (3.5)
    $ Fl.PlayAmbience("Fl_elevator_inside", 1, 6)
    scene cg Fl_mine_inside_elevator at Fl_avtobus_move with Fl_dissolve5
    $ persistent.Fl_photo_pallery_31 = True

    $ Fl.ShowScreens(_with=Fl_dissolve2)
    $ Fl.say(Fl_r, "Меня преследовали две вещи: стук лифта об кривые стенки шахт и секунды ожидания.")
    $ Fl.say(Fl_r, "Я не знал, что чувствую в данный момент. Может злость, может страх, а может быть боль?")
    $ Fl.say(Fl_r, "Одно я знал точно. Чем глубже спускается лифт вниз, тем сильнее я теряю рассудок.")

    show Fl_prolog_dream
    $ Fl.say(Fl_liz, "Если вдруг тебе придётся продолжить свой путь в одиночку, ни в коем случае не смей останавливаться. Иди только вперёд.")
    hide Fl_prolog_dream
    $ Fl.say(Fl_q66, "{mn2}")
    show Fl_prolog_dream
    $ Fl.say(Fl_d, "Я хочу пойти с тобой!")
    hide Fl_prolog_dream
    show Fl_vignette2 with Fl_dissolve1
    $ Fl.say(Fl_q66, "{mn2}")
    show Fl_prolog_dream
    $ Fl.say(Fl_mi, "Ты прав, твоя Мику умерла.")
    hide Fl_prolog_dream
    show Fl_vignette3 with Fl_fast 
    hide Fl_prolog_dream
    $ Fl.say(Fl_q66, "{mn}")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(4)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause (2.5)
    $ Fl.PlaySound("Fl_open_door_mines_metal", 1, 0, False)
    scene bg Fl_koridor_ma_son_obr with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve2)
    $ Fl.say(Fl_q66, "{mn2} {w}{mn}")
    $ Fl.say(Fl_q66, "И так.")
    $ Fl.say(Fl_r, "Голоса в голове затихли. Мы с ним довольно славно побеседовали, я молчал - они меня ломали. От моих слов ничего не зависло, результат всё равно один...")
    $ Fl.PlayMusic("Fl_Faster_louder", 1, 7)
    $ Fl.say(Fl_q66, "Да я как пришествие рока!(Рагнарёк)")
    $ Fl.say(Fl_q66, "Иду убивать богов и лжебогов этого ада!")
    $ Fl.say(Fl_r, "В голове заиграла музыка, я ловил темп, нет даже не так - я приплясывал пока перед глазами пролетали пустые больничные палаты.")
    $ Fl.say(Fl_r, "Вдали послышался шум, что-то сломалось.")
    $ Fl.say(Fl_q66, "О-о-о-о туда нам надо!")
    $ Fl.AttackMaster(True)
    $ Fl.say(Fl_ul34, "Нет! ПРЕКРАТИТЕ, Я НЕ ХОЧУ!")
    $ Fl.say(Fl_ul34, "УМОЛЯЮ НЕ НАДО!", _with=hpunch)
    $ Fl.say(Fl_unk1, "Остановите её!")
    $ Fl.say(Fl_unk1, "R-34 потеряла контроль над силой!")
    $ Fl.say(Fl_unk2, "Срочно вколите ей препорат!")
    $ Fl.say(Fl_r, "Подобно машине я вписался чётко в поворот и вынёс металическую дверь, что та сжалась в двое.")
    $ Fl.PlaySound("Fl_open_door_mines_metal", 1, 0, False)
    scene bg Fl_palata_loner with vpunch
    $ Fl.say(Fl_q66, "Поздно!")
    $ Fl.say(Fl_unk1, "Что за{break}")
    $ Fl.AttackMaster()
    $ Fl.PlaySound("Fl_bones_breaking", 1, 0, False)
    $ Fl.say(Fl_r, "Первый докторишка упал с пробитой грудной клеткой.")
    $ Fl.say(Fl_r, "Быстро соорентировавшись в пространстве я сразу узнал это место. {w}Это была моя палата, где когда-то меня вытянули с того света.")
    $ Fl.say(Fl_r, "Только всё преобразилось, вокруг были раскиданы вещи, лежали осколки люминесцентных ламп.")
    $ Fl.say(Fl_r, "Я перевёл взгляд на рыжую пациентку.")
    $ Fl.say(Fl_th, "Ты постаралась?")
    $ Fl.say(Fl_r, "Пионерка мне не ответила, да и не смогла бы. Судя по всему ей успели что-то вколоть. Она лежала не подвижно, но вроде дышит.")
    $ Fl.say(Fl_q66, "Стоп, я слышал два голоса.")
    $ Fl.say(Fl_r, "Только было поздно, когда я это осознал. {w}Моё тело резко замерло. Я не мог пошевелиться.")
    $ Fl.say(Fl_th, "Это ещё что за приколы?")
    $ Fl.PlaySound("Fl_table_hit", 1, 0, False)
    $ Fl.AttackMaster(True)
    $ Fl.say(Fl_r, "В ту же секунду мне прилетел сильный удар табуреткой по голове. Настолько сильный, что табуретка разлетелась в щепки.")
    $ Fl.say(Fl_r, "Я немного пошатнулся. Адреналин закипел в моих жилах, от чего контроль к телу быстро вернулся.")
    $ Fl.say(Fl_r, "Выпрямившись, я сделал разворот на 180 градусов.")
    $ Fl.say(Fl_q66, "Правду говорят за двумя зайцами погонишься, ни одного не поймаешь. Правда одного я уже поймал.")
    $ Fl.say(Fl_r, "Мои слова звучали саркастично, а взгляд хотел было уставиться на труп пробитый насквозь...")
    $ Fl.say(Fl_r, "Как в мои глаза попал пустой шприц в руках доктора.")
    $ Fl.say(Fl_unk1, "Не сработало?!")
    $ Fl.say(Fl_q66, "Слышь, ты что мне вколол?")
    $ Fl.say(Fl_r, "Сократив дистанцию, тело в белом халате повисло в воздухе.")
    $ Fl.say(Fl_unk1, "Кха, зря{mn}")
    $ Fl.say(Fl_q66, "Да ну?")
    $ Fl.say(Fl_r, "Неожиданно двери прохода начали закрываться, металлический роллет стремительно опускался вниз.")
    $ Fl.say(Fl_th, "Какого?!", _with=hpunch)
    $ Fl.say(Fl_r, "Рука куклы в белом халате находилась на какой-то кнопке. Судя по всему она и служила своего рода защитным механизмом при тревоге.")
    $ Fl.say(Fl_r, "Быстро оценив ситуацию, дверь уже была на половину закрыта.")
    $ Fl.say(Fl_unk1, "Что? Ч-что ты делаешь?!", _with=vpunch)
    $ Fl.say(Fl_unk1, "А-А-АА-А-А-А!", _with=vpunch)
    $ Fl.say(Fl_q66, "Ты сам выбрал такую смерть!")
    $ Fl.say(Fl_r, "Я решил остановить роллет тушей в белом халате. Но даже это не помогло, подобно тискам - голову доктора начало сдавливать, послышался хруст в перемешку с его криками.")
    $ Fl.say(Fl_th, "У меня есть считанные секунды!", _with=hpunch)
    $ Fl.say(Fl_r, "Схватив пионерку с койки, я устремился к выходу...")
    $ Fl.PlaySound("Fl_open_door_mines_metal", 1, 0, False)
    $ Fl.StopMusic(5)
    $ Fl.say(Fl_r, "Только вот дверь моментально закрылась, разрубив парня пополам. Кровь массивными брызгами отпечаталась по всей комнате и на моём лице тоже.")
    $ Fl.say(Fl_r, "Множество ударов никак не поменяло ситуацию, дверь просто не поддавалась.")
    $ Fl.AttackScreens()
    $ Fl.say(Fl_q66, "Да из чего ты состоишь вообще?!")
    $ Fl.say(Fl_r, "Резко в комнате раздался звук потока газа. Источником данного звука послужили распылители на потолке.")
    $ Fl.AttackScreens()
    $ Fl.say(Fl_q66, "Да вы меня не перестаёте удивлять, мать вашу!")
    $ Fl.say(Fl_q66, "Кхе-кхе...")
    $ Fl.say(Fl_r, "Моё возмущение явно было не к месту. Стоило крупицам газа попасть мне в лёгкие, как я сразу тяжело закашлял.")
    $ Fl.say(Fl_th, "Не знаю, что это. Но лучше это не вдыхать.")
    $ Fl.say(Fl_q66, "Кхе-кхе...")
    show Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_r, "Вновь кашель. Вместе с кашлем пошла кровь. В глазах потемнело.")
    $ Fl.say(Fl_q66, "Да что это газ такой?!", _with=hpunch)
    $ Fl.say(Fl_ul34, "П-погл-лотитель{mn}")
    $ Fl.say(Fl_r, "Неожиданно задёргалась девушка на руках.")
    $ Fl.say(Fl_q66, "Хах, я погляжу ты жива.")
    $ Fl.say(Fl_q66, "Кхе-кхе...")
    hide Fl_vignette 
    show Fl_vignette2
    with Fl_dissolve1
    $ Fl.say(Fl_ul34, "Н-ниче-его не г-говори. Я с-сейчас.")
    $ Fl.say(Fl_r, "Пионерка выставила руку и пыталась сконцентрироваться. Её рука постоянно дёргалась, в таком состоянии собственную руку удеражать казалось непосильной задачей.")
    $ Fl.HideScreens(_with=Fl_fast)


    $ Fl.Pause (3.5)
    $ Fl.PlaySound("Fl_open_door_mines_metal", 1, 0, False)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Металлический рулет, который секунду назад преграждал нам путь с молниеносной скоростью взлетел вверх.")
    $ Fl.say(Fl_q66, "Эй! Не знаю каким чудом ты окрыла эту дверь, но ты справилась!")
    $ Fl.say(Fl_r, "Но девушка не ответила, её рука окончательно пала и веки вместе с ней.")
    $ Fl.say(Fl_q66, "Держись, мы выберемся отсюда.")
    $ Fl.say(Fl_q66, "Я тебе обещаю.")
    $ Fl.say(Fl_r, "Отхаркнув кровью, на ватных ногах я поплёлся к выходу.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause (4.0)
    $ Fl.PlayAmbience("Fl_catacombs", 1, 6)
    scene Fl_tunnel_anim 
    show Fl_vignette3
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "В глазах темнело, тело отказывалось слушать. Организм боролся с заразой, что распространилась по всему телу, задевая даже разум.")
    $ Fl.say(Fl_th, "Я должен найти выход{mn}")
    $ Fl.Master(Fl_bg_zoom_th(1.0, 1.35, 17.0, 0.5, 0.65, 0.5, 0.35))
    $ Fl.say(Fl_th, "В этот раз я смогу спасти хотя бы одну душу.")
    $ Fl.say(Fl_r, "Искать выход дальше под землёй не имело никакого смысла. Единственная надежда в данной ситуации это лифт, на котором я сюда прибыл.")
    $ Fl.say(Fl_r, "Раны от битв открылись, я продолжал кашлять кровью. Всё что от меня оставалось - это алые следы под ногами.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause (3.0)
    scene Fl_mine_elevator_blur
    show Fl_vignette3
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_q66, "Видишь, а ты переживала. Осталось всего лишь подняться. Кхе-кхе...")
    $ Fl.say(Fl_r, "Картина перед глазами полностью поплыла. Я больше не различал что происходило перед глазами. Всё превратилось в калейдоскоп предсмертной агонии. Под шипящий звук стен - казалось они меня осуждают.")
    $ Fl.say(Fl_th, "Всего пару шагов{mn} Я не могу сдаться, прошу тело потерпи ещё немного.")
    $ Fl.PlayMusic("Fl_buckethead_angel_monster", 1, 7)
    $ Fl.say(Fl_setk, "Ну и ну. Какая встреча.")
    $ Fl.say(Fl_th, "Я замер, после чего повернулся к источнику хорошо знакомого мне голоса.")
    $ Fl.say(Fl_q66, "Хах, как же без тебя. Подопытный В!")
    $ Fl.say(Fl_th, "Глаза полностью потеряли фокус, но даже без него я чувствовал эту мерзкую ухмылку этой твари.")
    $ Fl.say(Fl_setk, "Тебе помочь? Наверное тяжело её тащить в таком состоянии.")
    $ Fl.say(Fl_q66, "Не волнуйся, как нибудь справлюсь сам. Но за предложение спасибо!")
    $ Fl.say(Fl_setk, "Даже сейчас у тебя получаеться язвить.")
    $ Fl.say(Fl_setk, "Много же ты дров наломал, Ян. Не думаешь что пора остановиться?")
    $ Fl.say(Fl_q66, "О-о-о нет, я только разогреваюсь. Это только первая палка в колёса.")
    $ Fl.say(Fl_setk, "Отдашь мне девчонку и тебе всё расскажу. Помогу выбраться из лагеря.")
    $ Fl.say(Fl_setk, "Ты можешь всё перехватить в свою пользу, или пути назад у тебя не будет.")
    $ Fl.say(Fl_q66, "Ну допустим, на кой <х*р> она тебе сдалась?")
    $ Fl.say(Fl_setk, "У неё очень сильная способность, которая поможет мне одолеть бога.")
    $ Fl.say(Fl_setk, "Жаль только такая способность досталась бесполезному мусору.")
    $ Fl.say(Fl_r, "Я расмеялся. Мой хохот с нескончаемым кашлем содрагал стены, но мне было просто весело.")
    $ Fl.say(Fl_q66, "Боюсь спросить, а что если я откажусь? Убьёшь?")
    $ Fl.say(Fl_setk, "Значит твой ответ нет?")
    $ Fl.say(Fl_q66, "Какой догадливый мальчик! Не зря ты номер один!")
    $ Fl.say(Fl_setk, "Что ж, тогда{mn}")
    $ Fl.say(Fl_r, "Из темноты засветились жёлтые глаза, которые стемительно приближались ко мне.")
    $ Fl.say(Fl_q66, "Выкуси!", _with=vpunch)
    $ Fl.say(Fl_r, "Собрав последние силы, я одним движением сломал трубу у стены. В тот же момент помещение начало заполняться газом.")
    scene cg Fl_mine_inside_elevator 
    show Fl_entrance_night_vision_layer
    with vpunch
    $ Fl.say(Fl_r, "Вторым движением я влетел в лифт и быстро закрыл двери руками.")
    $ Fl.say(Fl_r, "Два жёлтых огонька слились с темнотой, погрузив всё во мрак люминесцентных ламп и шума газа.")
    $ Fl.say(Fl_r, "Состояние было плачевное, возможно даже критическое. Всё на что мне хватило сил это прижать пионерку к себе и закрыть своей окровавленной тушей.")
    scene bg Fl_black with Fl_dissolve2
    $ Fl.say(Fl_r, "Алые ручьи обжигали кожу, а ещё очень сильно убаюкивали.")
    $ Fl.HideScreens(_with=Fl_dissolve2)
    $ Fl.StopAmbience(5)
    $ Fl.StopMusic(6)


    $ Fl.DayTime("rain", "night")
    $ Fl.Pause (5.5)
    scene cg Fl_nekto
    show Fl_vignette2
    with Fl_dissolve3
    $ persistent.Fl_photo_pallery_32 = True
    $ Fl.PlayMusic("Fl_sayonara", 1, 5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Нечёткий, но такой ослепительный образ. Мягкая ладонь, развевающимися волосы - такой хрупкий и нежный образ.")
    $ Fl.say(Fl_r, "Жаль только иллюзия. Как и всё в этом мире...")
    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Что побуждает людей сражаться? Идти дальше, не опускать руки?")
    $ Fl.say(Fl_r, "Из раза в раз я падал, но находил силы идти дальше. Смирился или причина заложена намного глубже чем я думаю.")
    $ Fl.say(Fl_r, "Может это просто тяжкий груз ответственности, вины, кто его знает. Скольких я спас, стольких и похоронил.")
    $ Fl.say(Fl_r, "Образ перед глазами крепче схватил мою руку.")
    hide Fl_vignette2 with Fl_dissolve1
    $ Fl.say(Fl_r, "В этот раз я принял данный жест.")
    $ Fl.say(Fl_r, "Интересно какого это когда ты знаешь что скоро настанет твой конец? Многие же чувствуют что вот вот скоро умрут.")
    $ Fl.say(Fl_r, "Если бы все знали когда и почему умрут, как мир изменился бы?")
    $ Fl.Pause (1.5)
    $ Fl.say(Fl_r, "Бессмертный мир полный паранойи. Постоянное ожидание цепких лап смерти, бесчисленные попытки обмануть смерть. Вся жизнь превращается в борьбу, уцепиться за каждый миг жизни.")
    $ Fl.say(Fl_r, "Вечный страх и ожиданния, даже с такими знаниями судьбу нельзя перехитрить.")
    show Fl_belizna_eff with Fl_dissolve1
    $ Fl.say(Fl_r, "Я сделал шаг вперёд.")
    $ Fl.say(Fl_r, "Не знаю какой меня в итоге ждёт финал, да слава богу. Но я гордо принимаю свою попутчицу {w}- смерть.")
    $ Fl.say(Fl_r, "Весь этот монолог с женской фигурой послужил важным итогом - я нашёл себя.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(3)
    scene bg Fl_black with Fl_flash2


    $ Fl.Pause (6.5)
    show text "{color=#faa600}{size=45}Как жаль, ты оказался очередным неудачным экспериментом." with Fl_dissolve1
    $ Fl.Pause (2.5)
    hide text with Fl_dissolve1
    $ Fl.Pause (2.0)
    show text "{color=#faa600}{size=45}Прощай, Q-66..." with Fl_dissolve1
    $ Fl.Pause (3.5)
    scene bg Fl_black with Fl_dissolve2
    $ Fl.Pause (6.0)


    $ Fl.DayTime("night", "night")
    scene Fl_int_aidpost_night_lamplight2 with Fl_dissolve3
    $ Fl.Pause (1.0)
    $ Fl.ShowBlink()
    $ Fl.Pause (3.0)
    $ Fl.HideBlink()
    scene Fl_int_aidpost_night_lamplight2
    $ Fl.ShowUnblink()
    $ Fl.Pause (1.5)
    scene bg Fl_black with Fl_dissolve2
    $ Fl.HideUnblink()


    scene Fl_int_aidpost_night_lamplight2
    show Fl_vignette2
    with Fl_dissolve2
    $ Fl.Pause (1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Пусто. Ничего не хочется. {w}Даже осознать где я сейчас.")
    $ Fl.say(Fl_r, "Глаза открылись, но в голове было пусто. Я не осознавал где нахожусь, мыльная картина перед глазами - которую видел сотню раз, вижу словно впервые.")
    $ Fl.say(Fl_r, "В горле стал ком, очень сильно хотелось пить.")
    $ Fl.say(Fl_th, "Я должен встать.")
    show Fl_vignette3 with Fl_dissolve1
    $ Fl.say(Fl_r, "Картина перед глазами не становилась чёткой. Наоборот мой главный ориентир ухудшался.")
    $ Fl.say(Fl_th, "Я просто хочу глоток воды{mn}")
    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    $ Fl.HideScreens()
    scene bg Fl_black with hpunch


    $ Fl.Pause (5.5)
    scene bg Fl_int_infirmary with Fl_dissolve3
    $ Fl.Pause (1.0)
    $ Fl.ShowBlink()
    $ Fl.Pause (3.0)
    $ Fl.HideBlink()
    scene bg Fl_int_infirmary
    $ Fl.ShowUnblink()
    $ Fl.Pause (1.5)
    scene bg Fl_black with Fl_dissolve2
    $ Fl.HideUnblink()


    scene bg Fl_int_infirmary
    show Fl_vignette
    with Fl_dissolve2
    $ Fl.PlayAmbience("Fl_camp_center_night", 0.5, 5)
    $ Fl.Pause (1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Второе пробуждение. Такое чёткое, такое яркое... Но такое бессмысленное и ещё более непонятное.")
    $ Fl.say(Fl_th, "С каждым разом я всё переезжаю. Вижу уже и палата посолиднее стала.")
    hide Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_r, "Я привстал. Кое-как мне удалось занять сидячее положение, подперевшись к стене.")
    $ Fl.say(Fl_r, "Глаза метались, то на часы, то в окно. Всё казалось таким странным. {w}Спокойным?")
    $ Fl.say(Fl_r, "Мой взгляд опустился ниже, на собственное тело. Множество окровавленных бинтов, стёртые в кровь руки, порезы - одним словом живого места на мне не было.")
    $ Fl.say(Fl_th, "{mn2}")
    $ Fl.say(Fl_th, "Малявка!", _with=vpunch)
    $ Fl.AttackScreens(True)
    $ Fl.say(Fl_r, "В голове пробежали последние события, тело само рвануло вперёд, но что-то сдержало меня.")
    $ Fl.NormalScreens()
    $ Fl.say(Fl_ul34, "Вовремя я зашла.")
    $ Fl.say(Fl_ul34, "И куда ты собрался на этот раз?")
    $ Fl.say(Fl_r, "В проёме стояла малявка, она вытянула руку вперёд, прямо на меня.")
    $ Fl.say(Fl_th, "Телекинез{mn} Вот почему я не могу пошевелиться.")
    $ Fl.say(Fl_r, "Немного прихрамывая, пионерка поставила поднос с едой рядом с кроватью.")
    show Fl_food with Fl_fast
    $ Fl.say(Fl_ul34, "Есть хочешь?")
    $ Fl.say(Fl_r, "Пионерка перестала держать моё тело и я смог немного подвинуться. После чего жадно схватился за стакан с водой.")
    $ Fl.say(Fl_ul34, "За этим ты вчера ночью пополз?")
    $ Fl.say(Fl_r, "Наблюдая как я поглощаю воду, спросила с усталой улыбкой на лице малявка.")
    $ Fl.say(Fl_r, "Только сейчас я обратил внимание с какой болью ей далась эта слабая улыбка. Всё лицо девушки было в царапинах, руки и ноги были в таком же состоянии.")
    $ Fl.say(Fl_q6, "Прости.")
    $ Fl.say(Fl_ul34, "За что ты извиняешься?")
    $ Fl.say(Fl_r, "Пионерка заметила как я внимательно осматриваю все её раны.")
    $ Fl.say(Fl_ul34, "Ты просто был тяжёлый. Спасти ты меня спас, а вот доделывать работу пришлось мне!")
    $ Fl.say(Fl_q6, "Что тогда произошло?")
    $ Fl.say(Fl_ul34, "Так дайка подумать{mn} Ты что последнее помнишь?")
    $ Fl.HideScreens()


    $ Fl.PlaySound("Fl_vzhuh", 1, 0, False)
    scene Fl_mine_elevator_blur
    show Fl_prolog_dream at Fl_alpha(0.65)
    with Fl_flash_fast
    $ Fl.Pause (1.0)

    $ Fl.PlaySound("Fl_vzhuh", 1, 0, False)
    scene cg Fl_mine_inside_elevator 
    show Fl_prolog_dream at Fl_alpha(0.65)
    with Fl_flash_fast
    $ Fl.Pause (1.0)

    $ Fl.PlaySound("Fl_vzhuh", 1, 0, False)
    scene bg Fl_int_infirmary with Fl_flash
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_q6, "Встречу с кукловодом и как мы запрыгнули в лифт.")
    $ Fl.say(Fl_ul34, "{mn}")
    $ Fl.say(Fl_r, "Малявка на секунду замолчала, нахмурилась и грустно улыбнулась. Такой спектр эмоций ради одно слова{mn}")
    $ Fl.PlayMusic("Fl_razd", 1, 5)
    $ Fl.say(Fl_ul34, "Понятно.")
    $ Fl.say(Fl_th, "Ты сейчас блин серьёзно? Просто понятно?!")
    $ Fl.say(Fl_ul34, "А я помню, как проснулась в лесу. Сверху меня лежал ты.")
    $ Fl.say(Fl_ul34, "Ты крепко прижал меня всем телом. {w}Твои раны не переставали кровоточить, я пропиталась полностью твоей кровью.")
    $ Fl.say(Fl_ul34, "{mn}")
    $ Fl.say(Fl_r, "Из глаз пионерки потекли слёзы, но она не плакала. Эмоции работали отдельно, я увидел в этих невинных детских глаза самого себя.")

    scene bg Fl_int_house_of_mv_day:
        Fl_bg_zoom_th(1.0, 1.5, 0.0, 0.5, 0.2, 0.5, 0.55)
    show Fl_prolog_dream
    with Fl_fast
    $ Fl.say(Fl_r, "Достав из своего кармана телефон и посмотрев на него, из глаз начали идти слёзы.")
    $ Fl.say(Fl_r, "Нет, я не плакал, как обычные люди, надрываясь и, буквально, крича о том, как мне больно... {w}Нет.")
    scene bg Fl_int_infirmary with Fl_fast
    $ Fl.say(Fl_ul34, "Мои способности к тому времени полностью вернулись. И мне удалось тебя аккуратно отащить.")
    $ Fl.say(Fl_q6, "Почему просто не совершила прыжок?")
    $ Fl.say(Fl_ul34, "Если было всё так просто. Я не знаю, как ты в это место вообще попал!")
    $ Fl.say(Fl_q6, "А что с ним не так?")
    $ Fl.say(Fl_ul34, "Туда невозможно попасть обычным прыжком и выйти так же просто, как в любой точке лагеря.")
    $ Fl.say(Fl_ul34, "Вообщем, мне пришлось тебя далеко отащить и там уже сделать прыжок.")
    $ Fl.say(Fl_r, "Я положил ладонь на макушку рыжей пионерки. Даже такое простое движение мне давалось с трудом.")
    $ Fl.say(Fl_q6, "Спасибо, ты спасла меня.")
    $ Fl.Pause (1.5)
    $ Fl.say(Fl_ul34, "Это ты меня спас{mn} Уже дважды{mn}")
    $ Fl.say(Fl_q6, "Не надо было мне тогда тебя оставлять.")
    $ Fl.say(Fl_ul34, "Надо, сейчас ты в большой опасности из-за меня. Кукловод вернётся за мной{mn}")
    $ Fl.say(Fl_q6, "Да пофиг, пускай! Я устал убегать и отворачиваться от других.")
    $ Fl.say(Fl_r, "Малявка едва улыбнулась.")
    $ Fl.say(Fl_q6, "Почему ему так сильно понадобилась именно твоя способность?")
    $ Fl.say(Fl_ul34, "Ну всё хватит уже вопросов. Давай отдыхай, иначе второй прыжок ты не выдержишь!")
    $ Fl.say(Fl_q6, "А что ещё будет второй?!")
    $ Fl.say(Fl_r, "Наиграно удивился я, наверное это получилось со стороны забавно. {w}Забавно{mn}")
    $ Fl.say(Fl_ul34, "Ага, нам больше нельзя задерживаться ни в одном лагере больше одного цикла.")
    $ Fl.say(Fl_r, "Но мой задорный настрой пионерка не оценила.")
    $ Fl.say(Fl_th, "Как много она скрывает, но кое-что я хочу узнать прямо сейчас.")
    $ Fl.say(Fl_q6, "Тогда, в палате. Я спросил, что это за газ такой. Ты ответила: поглотитель.")
    $ Fl.say(Fl_q6, "Что такое поглотитель?")
    $ Fl.say(Fl_r, "Вздох, пионерка снова присела на краешек кровати.")
    $ Fl.say(Fl_ul34, "Разработка доктора Парки. Препорат, который может заглушать на время способности.")
    $ Fl.say(Fl_ul34, "Он действует как снотворное, но с дополнительным эффектом.")
    $ Fl.say(Fl_q6, "Заглушает нейроные связи с мозгом, чтобы сказитель потерял возможность использовать силу?")
    $ Fl.say(Fl_ul34, "Что-то вроде того.")
    $ Fl.say(Fl_r, "Ответила она устало и зевнула.")
    $ Fl.say(Fl_ul34, "Ладно, спокойной ночи. Если что вдруг я в соседней комнате.")
    $ Fl.say(Fl_q6, "Хорошо.")
    $ Fl.say(Fl_r, "Малявка ушла, оставив меня наедине с нетронутым подносом.")
    $ Fl.say(Fl_r, "Есть не хотелось. Я молчал ждал, когда соберусь и приду в себя. Сигареты бы ускорили процесс, но потерял ещё во время романтика с Тихоней.")
    $ Fl.StopMusic(5)
    $ Fl.say(Fl_th, "Плевать, лучше прилягу посплю. Надо быстрее восстановиться.")
    $ Fl.ShowBlink()
    $ Fl.say(Fl_r, "Восприятие мира почему-то сильно поменялось. Странный, но такой приятный покой. Шум сверчков, слабое дуновение ветра, шелест листвы - всё такое приятное и спокойное{mn}")
    $ Fl.HideScreens(_with=Fl_dissolve2)
    scene bg Fl_black
    $ Fl.StopAmbience(5)
    $ Fl.HideBlink()


    $ Fl.Pause (4.5)
    $ Fl.DayTime("day", "day")
    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1.0, 6)
    scene bg Fl_ext_aidpost_day:
        align (0.6, 0.55) zoom 1.3
    show Fl_light_c 
    with Fl_dissolve2
    $ Fl.Pause (1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Дым словно в танце тянулся к небу, с трудом так и непонятно откуда добытая сигарета тлела в моих руках.")
    $ Fl.say(Fl_q6, "Как же это прекрасно просто сесть на крыльце и покурить.")
    $ Fl.say(Fl_r, "Сидя на ступеньках в окровавленных бинтах я смотрел на округу. Ранее утро. В голове заиграли знакомые слова одной песни.")
    $ Fl.say(Fl_th, "Утренний рассвет. {w}Солнце поднималось над землёй.")
    $ Fl.say(Fl_th, "Просыпался лес, восхищаясь утренней зарёй.")
    $ Fl.say(Fl_th, "...Продолжение сна, дивная пара. Как божественна природа и проста{mn}")
    $ Fl.say(Fl_q6, "Ещё не пробудились петухи в деревнях! И рыбаков на озере пока не видать!")
    $ Fl.AttackScreens()
    $ Fl.say(Fl_ul34, "Один петух уже проснулся.")

    show us pioner yawn at left with Fl_dissolve1

    $ Fl.say(Fl_ul34, "Горшок, ты чего не спишь?")
    $ Fl.say(Fl_r, "Мой вокал и подтанцовку виде сигареты прервала рыжая пионерка.")
    $ Fl.say(Fl_q6, "Ты даже знаешь кто это такой?")

    show us pioner2 dontlike at left with Fl_fast

    $ Fl.say(Fl_ul34, "Конечно знаю! Я старше тебя вообще-то!")
    $ Fl.say(Fl_th, "А точно. Она же из первого периода.")
    $ Fl.say(Fl_th, "Период, когда появились первые сказители те кто когда-то просто жили в обычном мире, пока не заточились в лагере вместе с Юлей.")

    show us pioner grin at left with Fl_fast

    $ Fl.say(Fl_ul34, "Ну и чего ты задумался?")
    $ Fl.say(Fl_q6, "Думаю, как всё сложно. Слишком много информации{mn}")

    show us pioner sad at left with Fl_fast
    $ Fl.Pause (1.0)
    hide us pioner sad with Fl_fast

    $ Fl.say(Fl_ul34, "Ты как? Как себя чувствуешь?")
    $ Fl.say(Fl_r, "Малявка присела рядом и начала засыпать вопросами. Вопросы были разные, но для меня очень сложные.")
    $ Fl.say(Fl_q6, "Как я? Да сам не знаю, голова идёт кругом.")
    $ Fl.say(Fl_ul34, "Я про самочувствие, болван! То что ты сейчас ничего не понимаешь - это и так понятно.")
    $ Fl.say(Fl_q6, "Жить буду.")
    $ Fl.HideScreens(_with=Fl_fast)

    $ Fl.Pause (3.5)

    $ Fl.PlayMusic("Fl_mind_the_gap", 1, 4)
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Между нами повисла пауза. Пионерка не знала как завязать со мной диалог, а я просто думал об дурдоме, куда попал.")
    $ Fl.say(Fl_ul34, "Ты вчера интересовался почему Кукловод за мной охотится.")
    $ Fl.say(Fl_r, "Вопрос стальной хваткой вытащил меня из моих глубоких размышлений.")
    $ Fl.say(Fl_ul34, "Телекинез{mn} это не просто способность.")
    $ Fl.say(Fl_ul34, "Моя сила своего рода ручник.")
    $ Fl.say(Fl_r, "Малявка поглядывала на меня, но я не перебивал и молча внимательно слушал. Мои комментарии и встречные вопросы были излишни.")
    $ Fl.say(Fl_ul34, "По-мимо того, что я могу управлять силой мыслью. Телекинез так же служит защитным барьером, позволяет использовать способность на максимум без вреда психике и потери контроля.")
    $ Fl.say(Fl_ul34, "Кукловод не может использовать свою силу на всю. Есть большая вероятность, что он разрушит собственное сознание и станет сам куклой - просто оболочкой.")
    $ Fl.say(Fl_q6, "То есть, контроль заточит его сознание глубоко в себя? Потеряет связь с реальностью?")
    $ Fl.say(Fl_ul34, "Да. {w}Собственная способность его уничтожит.")
    $ Fl.say(Fl_ul34, "А если он получит мою способность он сможет контролировать свой разум на сто процентов.")
    $ Fl.say(Fl_q6, "Получается благодаря твоей способности он хотел разрушить предел своей силы?")
    $ Fl.say(Fl_ul34, "Не только{mn}")
    $ Fl.say(Fl_r, "Пионерка глубоко вздохнула. И посмотрела навверх. Я вновь просто слушал и ждал.")
    $ Fl.say(Fl_ul34, "Я ему нужна ещё из-за Юли. Через меня он сможет быстрее найти её.")
    show Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_q6, "Бог этого мира. Ты получается с ней тоже встречалась?")
    $ Fl.say(Fl_ul34, "И не раз. {w}Всё об этом месте я узнала от неё.")
    hide Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_ul34, "Смотри, ты словил джекпот! Спас ту, которая всё знает об этом месте.")
    $ Fl.say(Fl_r, "Рыжая пионерка слегка улыбнулась. По ней было видно, что она не хотела получить такую роль в этой истории. Быть носителем всей информации, защищать эту информацию, выживать{mn}")
    $ Fl.say(Fl_q6, "Должно же мне было наконец-то повезти!")
    $ Fl.say(Fl_q6, "То что мне пришлось узнать в той лаборатории{mn} Получается во всём виноват доктор Парки?")
    $ Fl.say(Fl_ul34, "Да. После удачного эксперимента с Юлей он не остановился. Как видишь теперь он создаёт вас - сказителей.")
    $ Fl.say(Fl_ul34, "Парки хочет создать сказителя, который по силе будет равен Юле или даже сильнее её.")
    $ Fl.say(Fl_q6, "Я уже это понял.")
    $ Fl.say(Fl_q6, "И этот сказитель Кукловод?")
    $ Fl.say(Fl_ul34, "Он всего лишь пробная попытка. Но очень сильная попытка.")
    $ Fl.say(Fl_r, "Малявка зевнула и потёрла глаза.")
    $ Fl.say(Fl_q6, "Не выспалась?")
    $ Fl.say(Fl_ul34, "Конечно! Кто шумел в медпункте, а потом на улице песни распевал?!")
    $ Fl.say(Fl_r, "Ухмылка. Я потрепал волосы пионерки.")
    $ Fl.AttackScreens()
    $ Fl.say(Fl_ul34, "Я тебе не маленькая!", _with=vpunch)
    $ Fl.AttackMaster()
    $ Fl.say(Fl_r, "После чего пионерка меня укусила за руку.")
    $ Fl.say(Fl_q6, "Чёрт! А ведёшься себя именно так!", _with=hpunch)
    $ Fl.say(Fl_r, "Посмотрев на злое личико пионерки, я вспомнил первую нашу встречу.")
    $ Fl.say(Fl_r, "Дикий ужас, попытка ухватиться хоть за кого-то. Кто смог бы её спасти от лап желтоглазой твари. Она не просила тогда о помощи, а молила.")
    $ Fl.say(Fl_ul34, "На самом деле мне нужно очень много времени на сон.")
    $ Fl.say(Fl_q6, "Поспать любишь, соня?")
    $ Fl.say(Fl_ul34, "Да нет же! Просто{mn}")
    $ Fl.say(Fl_ul34, "Просто мне приходиться контролировать свою способность даже во сне. Ужасно чутко сплю, почти всегда в полудрёме, а не полноценный сон.")
    $ Fl.say(Fl_q6, "Контролитровать, но зачем?")
    $ Fl.say(Fl_ul34, "Чтобы кукловод не взял контроль над моим телом и разумом. А там...")
    $ Fl.say(Fl_q6, "Он сможет вытащить информацию о Юле. Я знаю, он так ко мне в голову залез.")
    $ Fl.say(Fl_ul34, "Угу.")
    $ Fl.say(Fl_q6, "Тогда иди отдохни. Когда последний раз ты нормально отдыхала.")
    $ Fl.StopMusic(3)

    show us pioner smile at left with Fl_fast

    $ Fl.say(Fl_r, "Пионерка встала и хитро прихитро улыбнулась.")
    $ Fl.say(Fl_th, "Это ещё что за гримаса такая?")
    $ Fl.say(Fl_ul34, "Неожидала, что такой как ты психопат умеет проявлять заботу.")
    $ Fl.say(Fl_q6, "Этот психопат спас тебя между прочим.")

    show us pioner laugh at left with Fl_fast

    $ Fl.say(Fl_ul34, "Поплыл от моей милоты небось!")
    $ Fl.say(Fl_q6, "Иди спи уже!")

    show us pioner yawn at left with Fl_fast
    $ Fl.Pause (1.0)
    hide us pioner yawn with Fl_fast

    $ Fl.say(Fl_ul34, "Уееев, вот и пойду.")
    $ Fl.say(Fl_r, "Сказала малявка схватив ручку двери.")
    $ Fl.say(Fl_ul34, "Будь аккуратнее, ладно? Раны могут снова открыться.")
    $ Fl.say(Fl_ul34, "Не хочу тебя потом по всему лагерю искать{mn2}")
    $ Fl.say(Fl_q6, "Как скажешь.")
    $ Fl.HideScreens(_with=Fl_fast)

    $ Fl.Pause (2.5)

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "И я вновь остался на ступеньках один. Только звуки природы составляли мне компанию, поддерживали меня, пытались сохранить и без того потрёпанный рассудок.")
    $ Fl.say(Fl_th, "Пока мелкая спит, хочу кое куда сходить.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(6)
    scene bg Fl_black with Fl_dissolve2

    $ Fl.Pause (5.5)

    scene bg Fl_bynker_light with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Внутри бункера рассеивался свет, сценарий поменялся. Возможно по нашей вине, а может в лагере другой сюжет.")
    $ Fl.say(Fl_th, "Если так подумать, с Импостером мы проживали другой сценарий. События, диалоги, они отличались от моего лагеря.")
    $ Fl.say(Fl_th, "В начале я подумал из-за того что в лагере два сказителя, лагерь ловит глюк и ломается скрипт.")
    $ Fl.say(Fl_th, "Но что если лагеря в который мы совершали прыжок изначально имели другой сценарий?")
    $ Fl.say(Fl_r, "Из одних размышлений распускались дополнительные корни вопросов. Словно атомная реакция, быстро цепочка реагировала и подавала всё новые и новые сигнали для моих размышлений.")
    $ Fl.say(Fl_r, "Я включил кнопку питания. И старый советский монитор зарябил.")
    $ Fl.say(Fl_q6, "{mn2}")
    $ Fl.say(Fl_q6, "Deus.")
    $ Fl.say(Fl_q6, "{mn2}")
    $ Fl.PlayMusic("Fl_snare", 1, 4)
    $ Fl.say(Fl_r, "Чудо советской техники приняло пароль, продемонстрировав новейший интерфейс того времени.")
    $ Fl.say(Fl_q6, "Подошёл.")
    $ Fl.say(Fl_r, "Тело застыло, мне трудно было осознать, что я только что сделал.")
    $ Fl.say(Fl_r, "Почему-то в голове постоянно крутилось слово Дэус. Самое начало записок доктора Парки.")
    $ Fl.say(Fl_th, "Дэус - бог с латыни.")
    $ Fl.say(Fl_th, "Как страно. Если Парки хотел разработать сверхспособности, то почему проект называется \"Бог\"?")
    $ Fl.say(Fl_r, "Мои мысли создавали странную мглу, пучину мрака. Мне стало не по себе.")
    $ Fl.say(Fl_r, "Экран мерцал, мои руки не торопились освоить управление старой техники. Я стоял как вкопанный.")
    $ Fl.say(Fl_r, "Пересилив странную паранойю я медленно перемещался с помощью стрелок. Пока не остановился на пункте \"Отчёты\".")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_effect_6


    $ Fl.Pause (5.5)
    scene bg Fl_bynker_light with Fl_effect_6
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_q6, "Твою мать{mn}")
    $ Fl.say(Fl_r, "Отчёты своего рода были отцифрованными записками из бункера. Но более подробные.")
    $ Fl.HideScreens(_with=Fl_fast)


    $ Fl.DayTime("rain", "night")
    show Fl_vignette3 
    show Fl_prolog_dream
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_th, "Я не знаю что произошло. В ту ночь вся аппаратура дала сбой. Юля кричала. Но самое странное в её глазных яблоках не было ничего - они были кристально белые. А ещё светились{mn}")
    $ Fl.say(Fl_th, "В тот момент я радовался. Моя конечная цель была у меня почти в руках!")
    $ Fl.say(Fl_th, "Но аппаратура не слушалась, я не мог остановить процесс. Мне стало страшно, страшно всё потерять. И я рванул к ней.")
    $ Fl.say(Fl_th, "...")
    $ Fl.say(Fl_th, "Выхода нет. Мои предыдущие записи не имели смысла. Но кратко перескажу...")
    $ Fl.say(Fl_th, "Я очнулся в лаборатории. Помещение было в идеальном состоянии. Моя рабочая группа спокойно занималась своими делами, всё как обычно.")
    $ Fl.say(Fl_th, "...Никто не помнит Юлю, всех подопытных помнят, а её нет. Странно.")
    $ Fl.say(Fl_th, "Мне захотелось выйти наружу, на свежий воздух. Только вот планировка изменилась, я не могу никак найти выход...")
    $ Fl.say(Fl_th, "...Нашёл! Наконец-то лифт был найден.")
    $ Fl.say(Fl_th, "...")
    $ Fl.say(Fl_th, "Я не знаю, что происходит. Сажусь в лифт, еду и вновь просыпаюсь в том самом месте для проведения опытов. Снова рабочий коллектив, снова события повторяются.")
    $ Fl.say(Fl_th, "...Они не люди. Мои бывшие коллеги это нечто другое. Тот цикл когда еда закончилась всё показал... Это была страшная ночь. Бывшие товарищи начали убивать друг друга за запасы еды и воды.")
    $ Fl.say(Fl_th, "Не знаю сколько прошло месяц или два. {w}Мне удалось выжить, но почти никого не осталось. Приходиться скрываться, за дверью уже не люди.")
    $ Fl.say(Fl_th, "Вчера на моих глазах один из врачей поедал другого. Голод дошёл до степени канибализма. Они пожирали друг друга, не удалось обойти стороной даже повешенным или зарезанным суицидникам - они стали пищей.")
    $ Fl.say(Fl_th, "...")
    $ Fl.say(Fl_th, "Прошлой ночью я собрал всю волю в кулак и рванул к лифту. {w}Сел{mn2} И вновь очнулся на полу где проводились эксперименты.")
    $ Fl.say(Fl_th, "Утекло много воды и времени, пока я не встретил Юлю. Она пришла ко мне, её вид отличался - гибрид кошки и человека.")
    $ Fl.say(Fl_th, "Теперь это твоё проклятие, тебе не выбраться из этого места. Я уничтожу всё что ты породил, этот мир станет твоим адом! - сказала она после чего разорвала меня на части, медленно и мучительно.")
    $ Fl.say(Fl_th, "Моя лаборатория - мой же ад. И никуда мне не деться. Я хочу... хочу снова встретиться с Юлей. Хочу узнать результат своих опытов. Она ведь не человек, правда?")
    $ Fl.say(Fl_r, "Последующие записи были повреждены.")
    $ Fl.say(Fl_q6, "{mn}")
    hide Fl_vignette3 
    hide Fl_prolog_dream
    with Fl_dissolve2
    $ Fl.say(Fl_q6, "Я погляжу у тебя циклы намного интереснее!")
    $ Fl.StopMusic(0.5)
    $ Fl.PlaySound("Fl_ghost_voice", 1, 0, False)
    $ Fl.say(Fl_r, "Неожиданно слева за дверью послышался чей-то не человеческий тон.")
    $ Fl.say(Fl_q6, "Это ещё что за накал атмосферы?!", _with=hpunch)
    $ Fl.PlaySound("Fl_tv_noise", 1, 0, True)
    $ Fl.say(Fl_r, "Звук за дверью привлёк моё внимание, но в ту же секунду я перевёл взгляд на монитор. Экран заполнился помехами, а в центре экрана появилась надпись {w}\"Скрипт сломан\".")
    $ Fl.PlaySound("Fl_noise5", 1, 0, False)
    $ Fl.say(Fl_r, "Снова шум за дверью.")
    $ Fl.PlaySound("Fl_hit2", 1, 0, False)
    $ Fl.say(Fl_r, "Резкий удар в дверь. Стены вздрогнули")
    $ Fl.PlaySound("Fl_switch", 1, 0, False)
    scene bg Fl_bynker_dark
    $ Fl.say(Fl_r, "Электричество в бункере пропало, погрузив резко всё происходящее во тьму.")
    $ Fl.PlaySound("Fl_hit2", 1, 0, False)
    with vpunch
    $ Fl.say(Fl_q6, "Пора сматываться!")
    $ Fl.HideScreens(_with=Fl_fast)


    scene bg Fl_int_catacombs_entrance_new with hpunch
    $ Fl.Pause (1.5)
    scene bg Fl_ext_path_night 
    show Fl_dust_full
    with vpunch
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_q6, "Ночь?!", _with=hpunch)
    $ Fl.say(Fl_q6, "Прошло мать твою не больше 3 часов!", _with=hpunch)
    $ Fl.say(Fl_r, "В глазах читался ужас. Подобных аномалий я ещё не встречал. Глаза лихорадочно осматривали округу, а уши цеплялись за каждый шорох.")
    $ Fl.say(Fl_mi, "Ян?")
    $ Fl.say(Fl_q6, "Что?..")
    $ Fl.PlayMusic("Fl_medicating", 1, 4)
    $ Fl.say(Fl_r, "Из кустов медленно приближалась знакомая мне пионерка.")
    $ Fl.HideScreens(_with=Fl_fast)


    scene cg Fl_mi_gost 
    show Fl_dust_full
    with Fl_dissolve1_5
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Вот появились два хвостика. Напряжение нарастало. Внутри всё сжималось.")
    $ Fl.say(Fl_th, "Хватит, это всё ложь{mn}")
    $ Fl.HideScreens(_with=Fl_fast)


    scene cg Fl_mi_gost2 
    show Fl_dust_full
    with Fl_dissolve1_5
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Без единого звука ко мне приближалась Мику. {w}Её пустые чёрные, как смола, глаза погружали моё сознание в темноту.")
    show Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_r, "От неё исходил жуткий холод. Животный интерес или околелые от холода ноги не давали мне пошевелиться.")
    $ Fl.HideScreens(_with=Fl_fast)


    scene cg Fl_mi_gost3 with Fl_dissolve1_5
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "И вот я уже ощущаю мертвое холодное дыхание прямо перед собой. Оцепенение не проходит, я стал её марионеткой.")
    $ Fl.say(Fl_mi, "Ян, мне так страшно.")
    $ Fl.say(Fl_q6, "Мне <бл*ть> тоже.")
    $ Fl.say(Fl_th, "Каких только тварей не встретишь в этом месте.")
    $ Fl.say(Fl_mi, "Обними меня пожалуйста.")
    $ Fl.say(Fl_q6, "Знаешь, как-то в другой жизни, когда к тебе попаду. А пока у меня дела, извиняй!")
    scene cg Fl_mi_gost4 with Fl_fast
    $ persistent.Fl_photo_pallery_33 = True
    $ Fl.say(Fl_mi, "Ты думаешь, что заслуживаешь смерти чтобы оказаться рядом со мной?")
    $ Fl.AttackScreens(True)
    $ Fl.say(Fl_q6, "Кхе-кхе!")
    show Fl_vignette2 with Fl_fast
    $ Fl.Master(Fl_bghorrorflicker)
    $ Fl.say(Fl_r, "Горло крепко сжалось, резкая боль по всему телу. Я начал задыхаться, а то что притворялось Мику пилило меня своими яркими огоньками, которые загорелись в пустых глазницах.")
    $ Fl.say(Fl_mi, "Это твой ад и пора платить за все свои грехи. Мы будем тебя мучить так же как ты нас.")
    $ Fl.say(Fl_q6, "Что ты такое?")
    $ Fl.say(Fl_mi, "Я? {w}Всего лишь бездушная кукла, которую ты так любил убивать. Придавливал пионином, душил струнами, отрезал части тела, насиловал в разных местах.")
    $ Fl.say(Fl_r, "Боль усиливалась, но помимо физической появилась ещё и моральная. Сцены моего ультра насилия подобно хороводу крутились перед глазами.")
    $ Fl.say(Fl_q6, "Прости{mn2}")
    $ Fl.PlaySound("Fl_mi_laugh", 1, 0, False)
    $ Fl.say(Fl_mi, "Прости? Серьёзно?")
    $ Fl.say(Fl_mi, "Думаешь, такое чудовище, как ты заслуживает прощения?")
    $ Fl.say(Fl_r, "Я опустил голову.")
    $ Fl.say(Fl_q6, "Нет{mn}")
    $ Fl.say(Fl_mi, "Теперь наша очередь играть с тобой. Настало наше время циклов.")
    $ Fl.say(Fl_q6, "{mn}")
    $ Fl.say(Fl_r, "Пионерка медленно протягивала свои руки ко мне. Я резко поднял голову.")
    $ Fl.say(Fl_q6, "Нет, я сам решу когда закончится моё время циклов.")
    scene cg Fl_mi_gost2 with hpunch
    $ Fl.say(Fl_r, "После чего разрушив невидимую хватку, что сжимало моё горло, сделал рывок назад.")
    $ Fl.PlaySound("Fl_mi_laugh", 1, 0, False)
    $ Fl.say(Fl_mi, "Просто сбежишь?")
    $ Fl.say(Fl_mi, "Беги, прячься! Но мы достанем тебя!", _with=hpunch)
    $ Fl.Pause (1.2)
    $ Fl.say(Fl_mi, "Добро пожаловать в ад, Ян!", _with=Fl_dissolve1)
    $ Fl.say(Fl_q6, "Пошли к чёрту!")

    $ Fl.PlaySound("Fl_mi_laugh", 1, 0, False)
    scene bg Fl_hor_les_obr1
    show Fl_dust_full
    with Fl_effect_right1
    $ Fl.say(Fl_r, "Как опытный танцор, я крутанулся на 180 градусов. Сзади уже кто-то смог лицезреть мои изящные движения.")
    $ Fl.say(Fl_th, "Чёрт! Ещё одна?!")
    $ Fl.say(Fl_th, "Плевать, мне некогда с ними развлекаться. Надо как можно быстрее найти малявку!")
    $ Fl.StopMusic(2)
    $ Fl.HideScreens(_with=Fl_fast)


    scene bg Fl_ext_path2_night with Fl_dspr
    scene bg Fl_ext_houses_night2 with Fl_dspr
    scene bg Fl_ext_medstation_night_light
    show Fl_dust_full
    with Fl_dspr
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_q6, "Главное в этот раз не опоздать.")
    $ Fl.HideScreens()


    scene bg Fl_ext_musclub_night3 
    show Fl_prolog_dream
    with Fl_flash_fast
    $ Fl.Pause (0.4)
    $ Fl.PlaySound("Fl_open_door_kick", 1, 0, False)
    scene bg Fl_int_aidpost_lamp 
    show us pioner normal
    with vpunch

    $ Fl.Pause (0.85)
    show us pioner2 fear with vpunch

    $ Fl.ShowScreens(_with=Fl_dspr)
    $ Fl.AttackScreens()
    $ Fl.say(Fl_ul34, "Ян?!")
    $ Fl.say(Fl_ul34, "Где{break}")
    $ Fl.AttackScreens()
    $ Fl.say(Fl_q6, "Нам нужно срочно бежать!")
    show Fl_vignette with Fl_fast
    $ Fl.say(Fl_r, "Только сейчас я понял что вызвало испуг у пионерки.")
    $ Fl.say(Fl_r, "Я почувствовал как мои бинты становились влажными. Раны открылись, не успел я восстановится, как столько раз использовал силу ощейника - тело не выдержало.")

    show us pioner sad with Fl_fast

    $ Fl.say(Fl_ul34, "Хорошо, я поняла.")

    hide us pioner sad with Fl_dissolve1

    $ Fl.say(Fl_r, "Без лишних слов пионерка схватила меня за руку.")
    $ Fl.HideScreens(_with=Fl_fast)


    $ Fl.PlaySound("Fl_vzhuh", 1, 0, False)
    scene bg Fl_black with Fl_flash
    $ Fl.Pause (0.5)
    $ Fl.PlayAmbience("Fl_lake_shore_evening", 1, 2)
    scene bg Fl_ext_boathouse_sunset
    show Fl_light_c
    with Fl_flash

    $ Fl.DayTime("sunset", "sunset")
    $ Fl.say(Fl_r, "Силуэты за окном пропали. Вместо них легла водная гладь, разгар заката и свежий ветерок. Лагерь снова наполнился звуками.")
    $ Fl.say(Fl_r, "Малявка отпустила мою руку и достала бинты из кармана.")

    show us pioner2 dontlike with Fl_fast

    $ Fl.say(Fl_ul34, "Садись!")

    hide us pioner2 dontlike with Fl_dissolve1

    $ Fl.say(Fl_r, "Пионерка отошла в сторону и указала на край причала. Спорить с ней не хотелось, да и не было сил.")
    $ Fl.Pause (1.45)
    $ Fl.say(Fl_ul34, "Какого{mn}")
    $ Fl.say(Fl_q6, "Что там?")
    $ Fl.say(Fl_ul34, "Н-ничего{mn}")
    $ Fl.say(Fl_ul34, "Я сейчас, подожди. Надо рану обработать.")
    $ Fl.say(Fl_r, "Не став дожидаться пионерку, я подошёл к воде. Чёткость отражения так себе, но разглядеть можно.")
    $ Fl.Pause (1.45)
    show Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_r, "Теперь стало ясно что вызвало такое удивление у малявки. {w}По всему телу раны полученные в бою стали чёрные. Сквозь эти чёрные порезы сочилась медленно кровь.")
    $ Fl.say(Fl_q6, "Что это такое?")
    $ Fl.say(Fl_r, "Это не было похоже на заражение раны, это было что-то инородное.")
    $ Fl.say(Fl_q6, "Хах, походу это будет мой последний цикл.")
    show Fl_vignette2 with Fl_dissolve1
    $ Fl.say(Fl_r, "Вселенная будто услышала мою издёвку и в тот же момент мои ноги подкосились.")
    $ Fl.PlaySound("Fl_body_bump", 1, 0, False)
    $ Fl.HideScreens()
    scene bg Fl_black with hpunch
    $ Fl.ShowBlink()
    $ Fl.StopAmbience(5)

    $ Fl.Pause (7.5)
    $ Fl.HideBlink()
    $ Fl.ShowUnblink()

    $ Fl.DayTime("rain", "rain")

    scene bg Fl_int_mine_wallbreak 
    show Fl_interference_anim
    with Fl_dissolve3
    $ Fl.Pause (1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.PlayMusic("Fl_dead_city", 1, 5)
    $ Fl.say(Fl_r, "Перед глазами появилась следующая картина. {w}Я находился в какой-то шахте, повсюду разбросан уголь, а вдали лишь непроглядная мгла. Электричество должно быть, если судить по толстым кабелям, висящих на стенах шахты. Следовательно проблема с лампочкой.")
    $ Fl.say(Fl_th, "Заброшенная шахта под старым корпусом? {w}Почему я здесь?")
    $ Fl.say(Fl_r, "Я посмотрел на свои руки. {w}Я попытался посчитать сколько у меня пальцев, но задача оказалась непосильной.")
    $ Fl.say(Fl_th, "Понятно. Сон, значит.")
    $ Fl.HideUnblink()
    $ Fl.HideScreens(_with=Fl_dissolve1)


    scene bg Fl_int_mine_crossroad_lighter
    show Fl_interference_anim
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Не смотря на кромешную тьму, я уверенно шёл прямо. Эту шахту я знал, как своих пять пальцев(хотя я минуту назад их так и не смог посчитать).")
    $ Fl.say(Fl_r, "Наш друг со справкой любит здесь ошиваться, а мы потом его всем лагерем ищем.")
    $ Fl.say(Fl_th, "Направо... {w}Почему я это знаю?")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    scene bg Fl_int_mine_halt_lighter
    show Fl_interference_anim
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Я откуда-то знал конечную цель своего маршрута, но я не понимал зачем туда иду.")
    $ Fl.say(Fl_r, "Ноги сами меня вели, какая-то неведомая сила подталкивала меня вперёд.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    scene bg Fl_int_mine_door_lighter
    show Fl_interference_anim
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Интересно почему? {w}Может моё упорство смогло победить инстинкт самосохранения? {w}Или это выброс адреалина перед неизвестностью, скрывающейся за дверь?")
    $ Fl.say(Fl_r, "Перестав гадать, я дотронулся до ручки, после чего резко её опустил.")
    $ Fl.say(Fl_r, "Замок не издал ниединого звука, и это меня насторожило.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    scene bg Fl_int_mine_room_ligher
    show Fl_interference_anim
    with Fl_dissolve2

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Стоило мне зайти внутрь, как я тут же скривился. {w}Помещение, отдалённо похожее на пристанище алкашей и наркоманов, встретило меня своей нагнетающей обстановкой.")
    $ Fl.say(Fl_r, "Хоть глаза уже и привыкли к темноте, но без света внутри всё выглядело жутко.")
    $ Fl.say(Fl_r, "Метаясь глазами дабы зацепить хоть за что-то по-мимо мусора и надписей, я заметил чью-то фигуру в дальнем углу комнаты. {w}Свет туда не попадал, поэтому мне оставалось только надеется, что силуэт принадлежит человеку.")
    $ Fl.say(Fl_kvl, "Ну привет, Ян.")
    $ Fl.say(Fl_th, "Ян? Откуда он знает, как меня зовут?")
    $ Fl.say(Fl_r, "Фигура поднялась и начала двигаться в мою сторону.")
    $ Fl.say(Fl_r, "Я не двинулся, а терпеливо ждал фигуру. Почему-то мне казалось что это было и я поступил иначе.")
    $ Fl.say(Fl_kvl, "Ты не убегаешь?")
    $ Fl.say(Fl_r, "Неизвестный гость замер. Что-то спугнуло его в моём поступке.")
    $ Fl.say(Fl_th, "Я точно помню подобный сюжет{mn}")
    $ Fl.say(Fl_r, "Не ожиданно мне стало трудно дышать. {w}Я ощутил удушье.")
    $ Fl.say(Fl_r, "Тело почему-то не испытывало боль, просто дискомфорт.")
    $ Fl.say(Fl_kvl, "А раньше ты боялся.")

    show set_pust at left with Fl_dspr:
        alpha(0.45)
    $ Fl.Pause (0.1)
    $ Fl.StopMusic()


    $ Fl.DayTime("sunset", "sunset")

    $ Fl.PlayAmbience("Fl_lake_shore_evening", 1, 1)
    scene bg Fl_ext_boathouse_sunset
    show Fl_light_c
    show us pioner cry
    with vpunch
    $ Fl.say(Fl_ul34, "Ян!", _with=hpunch)
    $ Fl.AttackMaster()
    $ Fl.say(Fl_r, "Я резко подскочил. Но смоливые раны отозвались адской болью, никогда ранее не испытывал подобную боль - это точно необычные раны.")
    $ Fl.say(Fl_r, "Согнутый пополам я поднял голову вверх. Пионерка стояла в слезах.")
    $ Fl.say(Fl_th, "Что произошло? Вроде просто уснул{mn}")
    hide us pioner cry with Fl_fast
    $ Fl.AttackMaster()
    $ Fl.say(Fl_r, "Пионерка крепко обняла меня. Раны вновь зашипели, я еле держался.")
    $ Fl.say(Fl_ul34, "Живой!")
    $ Fl.say(Fl_r, "Она только крепче прижалась. Её слёзы смазывали кровь на моём теле, я же терпел.")
    $ Fl.say(Fl_q6, "Кхг. Живой, живой! Отпусти уже, малявка!")
    $ Fl.say(Fl_q6, "Больно же!")
    $ Fl.say(Fl_ul34, "Ой прости-прости я забыла.")

    show us pioner sad smile with Fl_dissolve1

    $ Fl.say(Fl_ul34, "Я тут лекарства принесла.")
    $ Fl.say(Fl_r, "В её руках красовались флагоны антисептиков с бинтами и обезболы.")
    $ Fl.say(Fl_q6, "Ты мне лучше скажи, что за цирк ты тут устроила?")

    show us pioner2 dontlike with Fl_fast

    $ Fl.say(Fl_ul34, "Это ты мне лучше скажи, что с тобой происходит!")
    $ Fl.say(Fl_ul34, "Тебя одного оставить нельзя, вечно где-то валяешься без сознания!")
    $ Fl.say(Fl_q6, "Валяюсь и валяюсь себе, устал.")

    show us pioner2 angry with Fl_fast

    $ Fl.AttackScreens()
    $ Fl.say(Fl_ul34, "Ты мне тут ещё поумничай!")

    show us pioner sad with Fl_fast

    $ Fl.say(Fl_ul34, "Когда я тебя нашла у тебя пульса не было{mn}")
    $ Fl.say(Fl_q6, "{mn}")
    $ Fl.say(Fl_th, "Я чуть не умер.")
    $ Fl.say(Fl_th, "Хах, столько всего пережил, с кем только не столкнулся и в итоге чуть не погиб такой глупой смертью от пары царапин.")

    hide us pioner sad with Fl_fast

    $ Fl.say(Fl_r, "Слова были излишни, поэтому просто молча сел обратно на пристань.")
    $ Fl.say(Fl_q6, "Давай доктор лечи.")
    $ Fl.say(Fl_r, "Даже сидя спиной я почувствовал возмущённое выражение лица малявки.")
    $ Fl.say(Fl_ul34, "Ты же видел свои раны?")
    $ Fl.say(Fl_r, "Я кивнул.")
    $ Fl.say(Fl_ul34, "Я смогу лишь остановить кровотечение. Но думаю эти раны не вылечить.")
    $ Fl.say(Fl_q6, "Ты что-то подобное раньше видела?")
    $ Fl.say(Fl_ul34, "Нет. {w}С таким я сталкиваюсь впервые.")
    $ Fl.say(Fl_q6, "И я{mn}")
    $ Fl.say(Fl_r, "Рассматривая свои руки, которые были покрыты этими чёрными ранами, я старался не забивать голову мыслями.")
    $ Fl.say(Fl_ul34, "Походу нам придётся задержаться тут. Единственная надежда на перезапуск цикла.")
    $ Fl.say(Fl_q6, "И сколько нам придётся здесь торчать?")
    $ Fl.say(Fl_ul34, "Не знаю, надо найти какую-то подсказку и узнать сколько дней осталось до конца смены.")
    $ Fl.say(Fl_q6, "А если надолго мы тут, думаешь переживём этот цикл?")
    $ Fl.say(Fl_ul34, "Другого варианта нет! Если совершим прыжок, то ты умрёшь!")
    $ Fl.say(Fl_th, "И то верно, моё тело не выдержит очередной прыжок.")
    $ Fl.say(Fl_th, "Риск слишком велик, лучше попробовать пережить этот цикл - выжить куда больше шансов.")
    $ Fl.say(Fl_ul34, "И, Ян, не используй больше свою способность. Ты же ей пользовался пока я спала так ведь?")
    $ Fl.say(Fl_q6, "Да я уже понял. Моё тело тоже не выдержит, как и прыжок.")
    $ Fl.say(Fl_ul34, "Ага{mn}")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause (3.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_ul34, "Готово.")
    $ Fl.say(Fl_r, "Пионерка отложила медикаменты и села рядом со мной, протянув таблетку обезболивающего.")
    $ Fl.say(Fl_q6, "Спасибо.")
    $ Fl.say(Fl_th, "Что-то последнее время я часто начал говорить это слово.")
    $ Fl.say(Fl_ul34, "Не за что.")
    $ Fl.say(Fl_ul34, "Теперь расскажешь, что в том лагере произошло. Почему так быстро стемнело и почему ты так ко мне рванул?")
    $ Fl.say(Fl_th, "Точно, я уже и забыл почему мы оказались здесь.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause (3.5)
    scene bg Fl_ext_boathouse_sunset
    show Fl_light_c
    with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_ul34, "Я первый раз слышу про пароль и секретные данные на компьютере под шахтами...")
    $ Fl.say(Fl_r, "Я всё в подробностях пересказал пионерке, что произошло в том лагере.")
    $ Fl.PlayMusic("Fl_ploho", 1, 4)
    show Fl_vignette2 with Fl_fast
    $ Fl.say(Fl_ul34, "Парки{mn} Он больной ублюдок.")
    $ Fl.say(Fl_ul34, "Парки продолжил этот проект уже в этом мире.")
    $ Fl.say(Fl_ul34, "Он через своих подчинённых искал людей, которые застряли в циклах. Изучал, анализировал. А после предлагал им силу.")
    $ Fl.say(Fl_ul34, "Ты не представляешь сколько людей потеряли связь как со своим миром, так и с этим.")
    $ Fl.say(Fl_q6, "Чтобы сделать кандидата по силе равного Юле?")
    $ Fl.say(Fl_r, "Малявка одобрительно кивнула.")
    $ Fl.say(Fl_ul34, "Всеми известный Кукловод - он же один из удачных результатов его проекта.")
    $ Fl.say(Fl_ul34, "И Кукловод не позволяет узнать другим о Парки. А ещё и близко не позволяет попасть в лагерь Парки.")
    $ Fl.say(Fl_ul34, "Он не хочет чтобы кто-то узнал о его способности хоть что-то. И ты понимаешь почему.")
    $ Fl.say(Fl_q6, "Потому что ей можно противостоять? А Парки ещё и как информатор.")
    $ Fl.say(Fl_ul34, "Кто знает. Даже я не знаю. Но{mn}")
    $ Fl.say(Fl_q6, "Что но?")
    $ Fl.say(Fl_ul34, "Неважно. Единственный человек, который знает на что способен Кукловод это Юля.")
    $ Fl.say(Fl_ul34, "Но думаю, да. Причина по которой единицы знают о Парки это информация о способности Кукловода.")
    $ Fl.say(Fl_q6, "Мне вот интересно. Если Юля знает его способность, а тот хочет её уничтожить. Почему она его не убьёт?")
    $ Fl.say(Fl_ul34, "Не знаю, но она делает всё возможное чтобы меня защитить от него.")
    $ Fl.say(Fl_th, "Интересно в каких же ты отношениях с богом?..")
    $ Fl.say(Fl_q6, "Ты настолько хорошо знаешь бога? И почему с такой злобой упоминаешь имя Парки?")
    $ Fl.say(Fl_r, "Я заметил это давно. Малявка не просто злилась на доктора, как на чудовище. У неё словно личная обида, глубокая.")
    $ Fl.say(Fl_r, "Злость будто не за себя и не за то что с ней пытался сделать Парки, а злость за Юлю?")
    $ Fl.say(Fl_ul34, "Давай об этом как-то в следующий раз.")
    $ Fl.say(Fl_q6, "{mn}")
    $ Fl.say(Fl_ul34, "Если у Кукловода предельно понятная способность. То что насчёт твоей, как ты думаешь?")
    $ Fl.say(Fl_q6, "Даже я ничего не понял.")
    $ Fl.say(Fl_th, "Хаус - безграничная способность, носителю подвластно любое искажение реальности. Хаус - способен как создавать, так и уничтожать всё вокруг.")
    $ Fl.say(Fl_th, "Использование данной способности зависит только от Сказителя. Примечание, требуется огромная концентрация, своими мыслями носитель способен сделать что угодно.")
    $ Fl.say(Fl_q6, "Хаус - способность без границ, своими мыслями носитель может сделать что угодно.")
    $ Fl.say(Fl_q6, "Вот сиди и думай теперь, что это значит.")
    $ Fl.say(Fl_ul34, "Какой балбес.")
    $ Fl.say(Fl_r, "Я стиснул зубы и бросил холодный взгляд на пионерку.")
    $ Fl.say(Fl_q6, "А что тут понятного, может делать что угодно? Что это что угодно?")
    $ Fl.say(Fl_ul34, "Всё.")
    $ Fl.say(Fl_r, "Я успокоился, как только в ответ на меня посмотрели такие же холодные глаза.")
    $ Fl.say(Fl_ul34, "Твоя сила ближе всего к силе{mn}")
    $ Fl.say(Fl_r, "Малявка резко оборвала предложение и это было не в первый раз.")
    $ Fl.say(Fl_ul34, "Вообщем, тугодум, ты можешь контролировать всё вокруг. Всё зависит только от того что ты хочешь.")
    $ Fl.say(Fl_q6, "Ну спа{break}")
    $ Fl.say(Fl_ul34, "Не перебивай!")
    $ Fl.say(Fl_ul34, "Если перевести на понятный тебе язык. Если ты понимаешь механизм работы какой-то способности ты можешь ей воспользоваться. Своей силой ты можешь спокойно управлять телекинезом, имитацией, создать что угодно.")
    $ Fl.say(Fl_ul34, "На что ещё способен хаус, как не разрушать правила и весь порядок в мире?")
    $ Fl.say(Fl_ul34, "А теперь ты понял?!")
    $ Fl.say(Fl_r, "Не смотря что внешне пионерка была ребёнком, она отчитывала меня как маленького.")
    $ Fl.say(Fl_r, "На конец-то я понял о чём шла речь.")
    $ Fl.say(Fl_q6, "Я могу скопировать любую силу сказителя?")
    $ Fl.say(Fl_ul34, "Да, если поймёшь, как она работает или создашь правильно свой механизм работы. Но да, всё верно.")
    $ Fl.say(Fl_q6, "Свой механизм? Получается, я могу создавать любую способность?")
    $ Fl.say(Fl_ul34, "У х{w}а{w}у{w}с{w}а нет границ. Ты можешь всё, всё к чему может прикоснуться твоё сознание.")
    $ Fl.say(Fl_th, "Импостер была права, моя сила не заключается в нечеловеческих физических возможностях.")
    $ Fl.say(Fl_th, "Взгляни, извращенка, какая у меня в итоге крутая способность.")
    $ Fl.say(Fl_ul34, "Рано скалишься. Ты ведь не знаешь, как ей пользоваться.")
    $ Fl.say(Fl_ul34, "А самое страшное в твоей способности, чем больше твой разум разрушает границ реальности, тем тяжелее тебе держать контроль.")
    $ Fl.say(Fl_q6, "И если я не справлюсь, то потеряю контроль и способность меня поглотит{mn}")
    $ Fl.say(Fl_r, "Я схватился за голову. Переваривать информацию было уже невыносимо. Каждое новое знание поглошало разум, рвало частицы мозга на части, оставляя только пробелы восприятия.")
    $ Fl.say(Fl_ul34, "Знаю, слишком много информации. Поэтому не хочу всё разом на тебя вывалить.")
    $ Fl.say(Fl_ul34, "И не унывай! {w}Помогу тебе разобраться со всем этим. С хаусами там всякими.")
    $ Fl.say(Fl_q6, "Каким образом?")
    $ Fl.say(Fl_ul34, "Заставлю ложки сгибать силой мысли и мешки с сахаром тоскать без рук.")
    $ Fl.say(Fl_q6, "Научишь пользоваться твоей способности?")
    $ Fl.say(Fl_r, "На её лице засияла улыбка. В ней было столько доброты.")
    $ Fl.say(Fl_th, "Как ты сохранила человечность в этом месте, чтобы так улыбаться?")
    $ Fl.say(Fl_ul34, "И с ранами твоими надо разобраться уже. Я думаю, то что ты тогда нашёл в бункере вызвало какой-то сбой на твой цикл.")
    $ Fl.StopMusic(3)
    hide Fl_vignette2 with Fl_dissolve1
    $ Fl.say(Fl_q6, "Разберёмся. Пошли уже узнавать сегодняшнее число.")
    $ Fl.say(Fl_r, "Я потянулся нажать кнопку на устройстве. Как пионерка злобно на меня посмотрела.")
    $ Fl.say(Fl_q6, "Да я шучу. Помню помню, никаких устройств.")
    $ Fl.say(Fl_r, "Пионерка встала, не сводя глаз, встала рядом в строй после чего мы отправились за поисками.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause (3.5)
    scene bg Fl_ext_houses2_sunset:
        Fl_walking3
    show Fl_light_c
    with Fl_dissolve1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Обезболы успели подействовать. Ноги стояли твёрдо, а походка уверено меня вела в нужное направление.")
    $ Fl.say(Fl_th, "Надеюсь в этом лагере календарь находится на месте.")
    $ Fl.say(Fl_th, "Интересно как он работал после того как я убивал всех жителей в лагере. Отметка календаря сдвигалась сама по себе?")
    $ Fl.say(Fl_ul34, "И куда ты идёшь?")
    $ Fl.say(Fl_q6, "А?")
    $ Fl.say(Fl_r, "Выдернули меня из тучь мыслей.")
    $ Fl.say(Fl_q6, "В творческий клуб, там же календарь.")
    $ Fl.say(Fl_ul34, "Не надо было тебя нагружать информацией. Вообще не соображаешь.")
    $ Fl.say(Fl_th, "Что-то я начинаю уже жалеть, что спас эту девку.")
    $ Fl.say(Fl_ul34, "Узнам ты дату и толку, будем жить в лесу? С твоими то ранами.")
    $ Fl.say(Fl_q6, "Предлагаешь объявить лагерю о нашем прибытие?")
    $ Fl.say(Fl_ul34, "Даааа. {w}Вот вспомни, как давно ты был обычным пионером?")
    $ Fl.say(Fl_th, "Хах. Интересно был из какого периода? {w}До циклов или когда начал всех вырезать?")
    $ Fl.say(Fl_q6, "Тогда пошли к вожатке.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(5)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause (5.5)
    scene bg Fl_blink_square_party 
    show Fl_dust_full
    with Fl_effect_4
    #Куклы из-за кук.
    #Fl_company под встречу с Леной
    #Fl_Clockwork Orange Music - Thriller Tension интригующая музыка под детектив можно
    #Fl_daredevil под моменты с Улей
    #Fl_piano_believe_me прощание с Улей








    














    #Прода
    $ Fl.StopAmbience(4)
    $ Fl.Pause (6.0)

    scene Fl_proda with Fl_dissolve2

    $ Fl.Pause (4.0)
    scene bg Fl_black with Fl_dissolve2
    $ Fl.PlayMusic("Fl_bitarik", 1, 4)
    scene Proda_8 with Fl_dissolve2

    $ Fl.Pause (3.0)
    scene Proda_3 with Fl_flash
    $ Fl.Pause (3.0)
    scene Proda_1 with Fl_flash
    $ Fl.Pause (3.0)
    scene Proda_2 with Fl_dissolve1
    $ Fl.Pause (3.0)
    scene Proda_4 with Fl_flash
    $ Fl.Pause (3.0)
    scene Proda_6 with Fl_flash
    $ Fl.Pause (3.0)
    scene Proda_5 with Fl_dissolve1
    $ Fl.Pause (3.0)
    scene Proda_7 with Fl_flash
    $ Fl.Pause (4.0)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause (5.0)
    scene Proda_layer_loner with Fl_dissolve3
    $ Fl.Pause (8.0)
    scene bg Fl_black with Fl_dissolve2


