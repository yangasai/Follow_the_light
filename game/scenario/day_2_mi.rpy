# -*- coding: ひきこもり -*-

label day_2_mi:
    $ Fl.Save("День2: Проснись и пой, теперь ты мой.")
    $ Fl.DayTime("sunset", "sunset")


    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 4)
    $ Fl.Pause(2.0)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Выключив наугад будильник, я как ни в чём не бывало лежал на кровати, сбросив себя одеяло, потому что было душно.")
    $ Fl.say(Fl_th, "Уже утро? {w}Как же не хочется никуда вставать. Ещё эта долбаная линейка...")
    $ Fl.say(Fl_r, "Глубоко внутри меня отозвался прогульщик, которым я успел стать за последний учебный год.")
    $ Fl.say(Fl_r, "Я повернул голову к стене в надежде сделать окружающие звуки по тише.")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_th, "Интересно Мику уже встала. Она вроде бы говорила, что часто просыпает линейку. {w}Везёт, она глава музкружка. Её никто не накажет за прогул, в отличие от меня.")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_th, "Мику...")
    $ Fl.say(Fl_r, "В голове всплыли воспоминания прошлой ночи.")
    $ Fl.say(Fl_r, "Я улыбнулся.")
    $ Fl.say(Fl_th, "Мы едва ли не поцеловались в первый же день... {w}Такого спидрана отношений я точно не ожидал.")
    $ Fl.say(Fl_th, "А ведь я так и ничего не ответил на её чувства, просто утешил не более.")
    $ Fl.say(Fl_th, "Поступил ли я правильно? {w}Не знаю...")
    $ Fl.say(Fl_th, "Но теперь Мику точно будет тяжело смореть в глаза. Каждый раз меня будет ждать грустный взгляд с надеждой на слова, которое так ожидает услышать эта девушка.")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_th, "Но что я чувствую к ней на самом деле? {w}Симпатию? {w}Возможно... {w}Нравится ли она мне? {w}Определённо.")
    $ Fl.say(Fl_th, "Люблю ли я её? {w}А вот это навряд ли. Мне не достаточно одного дня чтобы влюбится в человека...")
    $ Fl.say(Fl_th, "Для меня загадка, как Мику смогла в меня так быстро влюбиться. Я ведь ничем не примечательный человек, обычный самоуверенный придурок с похотливыми мыслями - кароче простой козёл.")
    $ Fl.say(Fl_r, "Вспоминая момент нашего поцелуя, мне почему-то стало тошно. {w}Тошно от того, как этим поцелуем я мог породить надежду на взаимные чувства у этой хрупкой пионерки. Я ведь мог обжечь её ложным порывом чувств куда сильнее, чем просто проигнорировав её прихоть...")
    $ Fl.say(Fl_th, "Ян, когда же ты наконец-то начнёщь думать головой, а не одним местом?!")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_th, "Надеюсь вчерашний инцедент не разрушит наши отношения, не хотелось бы мне поссориться с такой необычной особой.")
    $ Fl.say(Fl_th, "В Мику определённо что-то есть едакое, что меня к ней тянет.")

    $ Fl.Pause(1.0)
    $ Fl.say(Fl_th, "Ладно, хватит уже отлёживаться. Пора собираться на линейку. Нехватало мне ещё выслушивать лекцию о пунктуальности!")
    $ Fl.say(Fl_r, "С этими мыслями я наконец-то смог открыть глаза.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    scene bg Fl_int_house_of_mi_sunset
    $ Fl.ShowUnblink()
    
    $ Fl.Pause(2.0)
    $ Fl.Status("80")
    $ Fl.Status("normal", False)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Яркий солнечный свет заставил меня прищуриться из-за чего я чуть не свалился с кровати.")
    $ Fl.say(Fl_r, "В предыдущей жизни, я всегда занавешивал все окна плотными шторами. И жил в своей норе, как крот, укрываясь от любого лучика света. Поэтому такого рода пробуждение сработало на меня, как взорвавшая флешка перед самым носом.")
    $ Fl.say(Fl_r, "Потирая заспанные глаза, я медлено и неуверно начал натягивать на себя свою домашнюю одежду. К вожатой я так и неудосужился зайти.")

    $ Fl.Pause(2.5)
    $ Fl.say(Fl_th, "Так с одеждой покончено, а теперь...")
    $ Fl.say(Fl_r, "Но не успел я и мысль закончиться, как заметил что моя соседка уже давно не спит.")
    $ Fl.HideUnblink()
    $ Fl.HideScreens()
    $ Fl.Pause(1.0)


    show mi charmed pioneer3 with Fl_dissolve1

    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Мику сидела на своей кровати. На ней наблюдалось уже не нижнее бельё, а пионерская форма. Она сидела и куда-то пялилась в одну точку с пустым взглядом.")
    $ Fl.say(Fl_gg, "Эм, доброе утро?")
    $ Fl.say(Fl_r, "Неуверенно сказал я, в надежде вывести пионерку из транса или где она сейчас там витает.")
    $ Fl.say(Fl_r, "Но реакции на мои слова не последовало.")
    $ Fl.say(Fl_gg, "Мику?")
    $ Fl.Status("-10")
    $ Fl.say(Fl_r, "И вновь никакой реакции.")
    $ Fl.say(Fl_gg, "Мику, что ты делаешь?")

    show mi normal pioneer3 with Fl_dissolve1

    $ Fl.say(Fl_mi, "Я? Ничего. Просто смотрю, любуюсь.")
    $ Fl.say(Fl_r, "Встав с кровати, загадочно произнесла она.")
    $ Fl.say(Fl_gg, "А можно поинтересоваться чем?")

    show mi smile pioneer2 with Fl_fast

    $ Fl.Status("-10")
    $ Fl.say(Fl_mi, "Тобой! {w}Ты так мило спал!")
    $ Fl.say(Fl_th, "А вот это уже странно...")
    $ Fl.say(Fl_gg, "Хах. Ты что так с самого утра любовалась мной?")
    $ Fl.say(Fl_r, "В шутку задал вопрос я.")
    $ Fl.say(Fl_mi, "Да, а ты разве против?")

    $ Fl.Status("-10")
    $ Fl.say(Fl_gg, "{mn}")
    $ Fl.say(Fl_mi, "Ты такой лапочка, что прямо хочется укусить тебя.")

    show mi normal pioneer3 with Fl_fast

    $ Fl.say(Fl_mi, "Давай, я тебя укушу?")
    $ Fl.HideScreens()
    $ Fl.Status("-10")


    scene bg Fl_int_house_of_mi_sunset:
        Fl_brightness_scale_jpg("Fl_int_house_of_mi_sunset", -0.1)
    show mi normal pioneer3 f
    with hpunch
    $ Fl.Master(Fl_bghorrorflicker)

    $ Fl.AttackScreens(True)
    $ Fl.PlayMusic("Fl_no_tresspassing_remix", 1, 4)
    $ Fl.say(Fl_r, "От такого заявления я сразу отпрыгнул назад.")
    $ Fl.say(Fl_gg, "Мику прекращай! Это уже не смешно!")
    $ Fl.say(Fl_mi, "Укушу.")
    $ Fl.say(Fl_r, "Повторила Мику.")
    $ Fl.say(Fl_th, "Это что за странные эротические игры начались. {w}Если что я не препочитаю укусы во время...")
    $ Fl.say(Fl_mi, "Ну же Ян. Почему ты уходишь?")
    $ Fl.say(Fl_r, "Странным тоном сказала она.")

    show mi upset obs3 with Fl_fast

    $ Fl.say(Fl_r, "И подошла ближе.")
    $ Fl.say(Fl_r, "И я только сейчас заметил, что её зрачки сузились, как у долбаного психа.")

    $ Fl.Status("-15")
    $ Fl.Status("panic", False)
    $ Fl.say(Fl_th, "ТВОЮ МАТЬ! ЧТО У НЕЁ С ЗРАЧКАМИ!!!", _with=hpunch)
    $ Fl.say(Fl_mi, "Ян ты будешь только моим. {w}И никто тебя не тронет, обещаю!")
    $ Fl.say(Fl_r, "Я начал медленно отступать к двери.")

    show mi pity grin2 obs3 with Fl_fast

    $ Fl.say(Fl_mi, "А ты никуда не сбежишь...")

    show mi pity grin2 obs3:
        subpixel True
        ease 8.0 zoom 1.2 xalign 0.5 yalign 0.5
    show Fl_fogging
    with Fl_dissolve1

    $ Fl.PlayMusic("Fl_no_tresspassing_remix2", 1, 4) 

    $ Fl.say(Fl_r, "Мику тем временем снова начала приближаться.")
    $ Fl.say(Fl_th, "ДА ГДЕ ЭТА ЧЁРТОВА РУЧКА?!", _with=hpunch)

    show mi pity grin2 obs3:
        subpixel True
        ease 3.0 zoom 1.3 xalign 0.5 yalign 0.5

    $ Fl.say(Fl_r, "И вот Мику уже совсем рядом.")
    $ Fl.say(Fl_th, "Всё, нашёл.", _with=hpunch)
    $ Fl.say(Fl_r, "И я тут же распахнул дверь... {w}хотя... {w}нет...")

    $ Fl.Status("-5")
    $ Fl.Status("panic", False)
    $ Fl.say(Fl_th, "КАКОГО ХРЕНА ОНА ЗАПЕРТА!!!", _with=hpunch)
    $ Fl.say(Fl_th, "Мне <п*зда>...")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.PodskSave()
    
    $ Fl.Pause(3.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Это было последнее, о чём я подумал, прежде чем...")
    $ Fl.say(Fl_r, "Прежде чем вспомнил о ключах!", _with=hpunch)
    $ Fl.say(Fl_r, "Моя рука быстро нашупала нужные ключи. После чего я сразу же дрожащими руками попытался попасть в замочную скважину.")

    $ Fl.PlaySound("Fl_mi_laugh", 1, 0, False)
    $ Fl.say(Fl_mi, "Ян...")
    $ Fl.say(Fl_th, "<С*ка> да попади ты <бл*ть> в этот долбанный замок!", _with=hpunch)

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_r, "Наконец-то мне удалось сделать два оборота. Я открыл дверь и уже собирался сбежать, как вдруг...")

    $ Fl.AttackScreens(True)
    $ Fl.PlaySound("Fl_attack", 1, 0, False)
    $ Fl.say(Fl_r, "Мику схватила меня за плечо и начала затаскивать обратно внутрь.")
    $ Fl.HideScreens()
    jump mi_qte1




label mi_qte1:
    scene bg Fl_black
    $ Fl.Pause(1.0)
    $ time = 1

    call screen Fl_mod_timer1
    screen Fl_mod_timer1:
        add "qte_5_button_anim" xalign 0.5 yalign 0.5
        key "5" action [Hide("Fl_mod_timer1"), Jump("Fl_you_survive1")]
        timer 1.0 action Jump("Fl_you_death_house")
        timer 0.1 repeat True action If(time > 0, true=SetVariable('time', time - 0.1), false = [Hide('battletime')])
        bar:
            style "timebar"
            value time
            xalign 0.5 yalign 0.06



label Fl_you_death_house:
    scene bg Fl_black with Fl_flash_red
    $ Fl.StopMusic(3)
    $ Fl.StopAmbience(3)
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Но больше я не успел ничего сделать, так как она меня схватила... {w}а после...")
    $ Fl.say(Fl_r, "Ну, а что после - уже не важно, потому что это конец.")
    $ Fl.say(Fl_r, "Если бы думал я чуть быстрее, то было бы всё иначе...")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.Status("")
    jump game_over


label Fl_you_death_camp:
    scene bg Fl_black with Fl_flash_red
    $ Fl.StopMusic(3)
    $ Fl.StopAmbience(3)
    $ Fl.PlaySound("Fl_padenie1", 1.0, 0, False)
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Но потом она всё-таки умудрилась схватить меня набегу, и я тут же упал.")
    $ Fl.say(Fl_r, "Ну а после просто оглушила и потащила обратно в домик.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.Status("")
    jump game_over


label Fl_you_survive1:
    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
    scene bg Fl_ext_houses_sunset with Fl_flash:
        ease 2.0 zoom 1.2 xalign 0.5 yalign 0.58
    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Кое-как мне удалось вырватся с мёртвой хватки Мику и выбежать на улицу.")
    $ Fl.say(Fl_r, "Вот только пионерка не собиралась просто так меня отпускать.")
    $ Fl.say(Fl_mi, "Ян, подожди!")
    $ Fl.HideScreens()
    jump mi_qte2


label mi_qte2:
    scene bg Fl_black
    $ Fl.Pause(1.0)
    $ time = 1

    call screen Fl_mod_timer2
    screen Fl_mod_timer2:
        add "qte_8_button_anim" xalign 0.5 yalign 0.5
        key "8" action [Hide("Fl_mod_timer2"), Jump("Fl_you_survive2")]
        timer 1.0 action Jump("Fl_you_death_camp")
        timer 0.1 repeat True action If(time > 0, true=SetVariable('time', time - 0.1), false = [Hide('battletime')])
        bar:
            style "timebar"
            value time
            xalign 0.5 yalign 0.06


label Fl_you_survive2:
    scene bg Fl_ext_houses_sunset with Fl_flash:
        Fl_run_fast
    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Не оглядываясь назад, я бежал куда глаза глядят. Лишь бы подальше от Мику.")
    $ Fl.HideScreens()
    jump mi_qte3



label mi_qte3:
    scene bg Fl_black
    $ Fl.Pause(1.0)
    $ time = 1

    call screen Fl_mod_timer3
    screen Fl_mod_timer3:
        add "qte_2_button_anim" xalign 0.5 yalign 0.5
        key "2" action [Hide("Fl_mod_timer3"), Jump("Fl_you_survive3")]
        timer 1.0 action Jump("Fl_you_death_camp")
        timer 0.1 repeat True action If(time > 0, true=SetVariable('time', time - 0.1), false = [Hide('battletime')])
        bar:
            style "timebar"
            value time
            xalign 0.5 yalign 0.06


label Fl_you_survive3:
    scene bg Fl_ext_square_sunset with Fl_flash:
        Fl_run_fast
    $ Fl.Pause(1.5)
    jump mi_qte4



label mi_qte4:
    scene bg Fl_black
    $ Fl.Pause(1.0)
    $ time = 1

    call screen Fl_mod_timer4
    screen Fl_mod_timer4:
        add "qte_7_button_anim" xalign 0.5 yalign 0.5
        key "7" action [Hide("Fl_mod_timer4"), Jump("Fl_you_survive4")]
        timer 1.0 action Jump("Fl_you_death_camp")
        timer 0.1 repeat True action If(time > 0, true=SetVariable('time', time - 0.1), false = [Hide('battletime')])
        bar:
            style "timebar"
            value time
            xalign 0.5 yalign 0.06


label Fl_you_survive4:
    scene bg Fl_ext_dining_hall_near_sunset with Fl_flash:
        Fl_run_fast
    $ Fl.Pause(1.5)
    jump mi_qte5



label mi_qte5:
    scene bg Fl_black
    $ Fl.Pause(1.0)
    $ time = 1

    call screen Fl_mod_timer5
    screen Fl_mod_timer5:
        add "qte_4_button_anim" xalign 0.5 yalign 0.5
        key "4" action [Hide("Fl_mod_timer5"), Jump("Fl_you_survive5")]
        timer 1.0 action Jump("Fl_you_death_camp")
        timer 0.1 repeat True action If(time > 0, true=SetVariable('time', time - 0.1), false = [Hide('battletime')])
        bar:
            style "timebar"
            value time
            xalign 0.5 yalign 0.06


label Fl_you_survive5:
    scene bg Fl_playground_sunset with Fl_flash:
        Fl_run_fast
    $ Fl.Pause(1.5)
    jump mi_qte6



label mi_qte6:
    scene bg Fl_black
    $ Fl.Pause(1.0)
    $ time = 1

    call screen Fl_mod_timer6
    screen Fl_mod_timer6:
        add "qte_6_button_anim" xalign 0.5 yalign 0.5
        key "6" action [Hide("Fl_mod_timer6"), Jump("Fl_you_survive6")]
        timer 1.0 action Jump("Fl_you_death_camp")
        timer 0.1 repeat True action If(time > 0, true=SetVariable('time', time - 0.1), false = [Hide('battletime')])
        bar:
            style "timebar"
            value time
            xalign 0.5 yalign 0.06



label Fl_you_survive6:
    $ Fl.StopAmbience(3)
    $ Fl.StopMusic(4)
    $ Fl.Pause(3.5)
    jump day_2_mi_proda




label day_2_mi_proda:
    $ Fl.Save("День2: Больше странностей.")
    $ Fl.DayTime("day", "day")

    $ Fl.Pause(2.5)
    $ Fl.PlayAmbience("Fl_forest_day", 1.0, 4)
    scene bg Fl_ext_path_day
    show Fl_light_c
    with Fl_dissolve3

    $ Fl.AutoSave()
    $ Fl.Status("50")
    $ Fl.Status("tension", False)
    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Кое-как оторвавшись от Мику, я выбежал ко входу в лес.")
    $ Fl.say(Fl_r, "В области грудной клетки всё горело, хотелось выпленуть лёгкие и просто завалиться замертва, лишь бы сейчас не цепляться за каждую молекулу кислорода.")
    $ Fl.say(Fl_r, "Повертев головой на 360 градусов, я убедился, что погони больше нет. {w}Крехтя я присел у какого-то дерева.")

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_th, "Чёрт, зря я физ-ру прогуливал. Щас бы здесь не подыхал...")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause(2.0)
    $ Fl.Status("+10")
    $ Fl.Status("tension", False)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Переведя дух, я наконец-то смог успокоиться и здраво обдумать всё что со мной произошло.")

    $ Fl.PlayMusic("Fl_are_you_a_bully", 1, 5)
    $ Fl.say(Fl_th, "Что сейчас только что было? {w}Откуда у Мику появился такой наплыв «нежности»?")
    $ Fl.say(Fl_th, "Нет, я конечно ещё вчера заметил, что девица обладает необычным характером. Но то что было сейчас...")

    $ Fl.Pause(1.0)
    $ Fl.say(Fl_th, "Это просто <п*здец>...")

    $ Fl.Pause(2.0)

    $ Fl.say(Fl_r, "Сам не заметив того, я полез в карман шорт и вытащил оттуда пачку сигарет.")
    $ Fl.say(Fl_r, "В надежде, что никотин даст мне ясность ума, я закурил.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause (1.5)
    $ Fl.PlaySound("Fl_zazigalka", 1, 0, False)
    $ Fl.Pause (2.0)
    $ Fl.PlaySound("Fl_smoking", 1, 0, False)
    $ Fl.Pause (2.5)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Что же с ней не так? {w}Почему она так себя повела? {w}Что на неё нашло?!")
    $ Fl.say(Fl_r, "Никотин действительно мне помог, восстановив нервную систему. Теперь мне было намного проще рыться в воспоминаниях после моего пробуждения в домике Мику.")
    $ Fl.HideScreens()


    $ Fl.PlaySound("Fl_flashback", 1.0, 0, False)
    scene bg Fl_int_house_of_mi_sunset:
        Fl_brightness_scale_jpg("Fl_int_house_of_mi_sunset", -0.1)
    show mi pity grin2 obs3:
        zoom 1.3 xalign 0.5 yalign 0.5
    show Fl_prolog_dream
    with Fl_flash_fast

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_mi, "Ян ты будешь только моим. И никто тебя не тронет, обещаю!")
    $ Fl.HideScreens()


    $ Fl.PlaySound("Fl_flashback", 1.0, 0, False)
    scene bg Fl_ext_path_day
    show Fl_light_c
    with Fl_flash_fast

    $ Fl.Pause (1.5)
    $ Fl.PlaySound("Fl_smoking", 1, 0, False)
    $ Fl.Pause (1.5)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Её слова... {w}И этот безумный взгляд... {w}Неужели Мику...")
    $ Fl.say(Fl_kvl, "Яндере!")
    $ Fl.say(Fl_r, "Я резко повернул голову влево, а затем в право.", _with=hpunch)
    $ Fl.say(Fl_gg, "Кто здесь?!")
    $ Fl.say(Fl_r, "Спросил я, но кроме птиц, никто мне так и не ответил.")

    show Fl_fogging with Fl_dissolve1

    $ Fl.say(Fl_kvl, "Я здесь.")
    $ Fl.say(Fl_r, "Услышав вновь чей-то голос, я начал судорожно мотать головой в поиске источника звука. {w}Но снова без результатно.")
    $ Fl.say(Fl_gg, "Выходи! Хватит прятаться!")
    $ Fl.say(Fl_kvl, "Прости, но возможности у меня такой нет. Я только могу сидеть и лицезреть картинку, которая постоянно трясётся.")
    $ Fl.say(Fl_th, "Что?")
    $ Fl.say(Fl_r, "И только сейчас до меня начало доходить, что этот голос я слышу не откуда-то, а прямо у себя в голове.")
    $ Fl.say(Fl_th, "Телепатия?")
    $ Fl.say(Fl_kvl, "Ага. Если бы, но такой привелегией я не обладаю.")
    $ Fl.say(Fl_th, "Тогда?..")
    $ Fl.say(Fl_kvl, "Да, я внутри твоей головы.")
    $ Fl.say(Fl_gg, "{mn}")

    $ Fl.Pause (2.5)
    $ Fl.say(Fl_th, "Замечательно! Поздравляю, Ян, ты сошёл с ума, теперь уже тебе кто-то в башке отвечает. Просто замечательно!")
    $ Fl.say(Fl_kvl, "Ну тут ты не прав, сударь. Я не шизофрения, как ты успел подумать.")
    $ Fl.say(Fl_th, "А кто тогда?")
    $ Fl.say(Fl_kvl, "Кукловод.")
    $ Fl.say(Fl_th, "Кукловод?")
    $ Fl.say(Fl_kvl, "Да, кукловод. Меня назначили за тобой наблюдать и помогать тебе.")
    $ Fl.say(Fl_th, "А можно поинтересоваться в чём именно мне требуется помощь?")
    $ Fl.say(Fl_kvl, "Например дожить до конца смены.")

    $ Fl.Status("-10")
    $ Fl.say(Fl_r, "Слова голоса(или кукловода, без разницы) заставили меня напрячься.")
    $ Fl.say(Fl_th, "А мне что-то угрожает?")
    $ Fl.say(Fl_kvl, "Глупо задавать мне такой вопрос, после того как за тобой гналась Мику, явно не чтобы мило побеседовать.")
    $ Fl.say(Fl_r, "Внутри меня вновь начал бурлить адреналин, поэтому дабы успокоиться я сделал очередную тягу.")

    $ Fl.PlaySound("Fl_smoking", 1, 0, False)
    $ Fl.Pause (1.5)

    $ Fl.say(Fl_th, "Хорошо, я слушаю. Ты можешь объяснить, что случилось с Мику сегодня утром?")
    $ Fl.say(Fl_kvl, "Как ты успел заметить, с ней действительно что-то не так. Но спешу тебя разочаровать она не Яндере. Что-то схожее есть, но нет.")
    $ Fl.say(Fl_th, "Тогда раздвоение личности?")
    $ Fl.say(Fl_kvl, "Близко, но нет.")
    $ Fl.say(Fl_th, "Тогда что с ней?!")
    $ Fl.say(Fl_kvl, "Не знаю, но она явно опасна. Ведь из-за того что ты выбрал её и из-за вашей очень интересной ночи, меня назначили тебя защищать.")
    $ Fl.say(Fl_th, "И давно ты меня так охраняешь?")
    $ Fl.say(Fl_kvl, "С сегодняшнего утра.")
    $ Fl.say(Fl_th, "Тогда откуда ты знаешь про то что было ночью?")
    $ Fl.say(Fl_kvl, "Сударь, ты меня плохо слушал или что? Я ведь сказал, что нахожусь у тебя в голове. А значит я способен не только с тобой разговаривать, но и просматривать твои воспоминания.")
    $ Fl.say(Fl_th, "Понятно.")
    $ Fl.say(Fl_r, "Сухо ответил я и выбросил сигарету в ближайщие кусты.")
    $ Fl.say(Fl_r, "В данный момент я размышлял над словами голоса. «Ведь из-за того что ты выбрал её...» - что я сделал именно не так? {w}Разрешил ей сесть рядом? {w}Или согласился пойти с ней в музклуб? {w}А может потому что я вступил к ней в клуб?")
    $ Fl.say(Fl_r, "Вариантов было много, но главное заключение оставалось одно? {w}По вашему я должен был оставить Мику одну и забыть её после первого же знакомства, как делали все в этом лагере?")
    $ Fl.say(Fl_r, "Нет! Так не правильно! Я уже оставил одного человека и к чему меня это привело?")
    $ Fl.say(Fl_r, "Я бросил взгляд на повязку на моём запясте, под которой красовался уродливый порез.")

    $ Fl.Pause (1.5)
    $ Fl.say(Fl_th, "Скажи, голос. Что на самом деле твориться в этом месте? Почему я здесь?")
    $ Fl.say(Fl_kvl, "Не могу ответить на твой вопрос, ибо сам не знаю.")
    $ Fl.say(Fl_th, "Ясно, спасибо.")
    $ Fl.say(Fl_r, "Сарказм - вот на что я сейчас был способен в данной ситуации. {w}Вопросы сильно утомляли меня, а поиск ответов ещё сильнее.")
    $ Fl.say(Fl_r, "Я облокатился на ствол дерева и сразу же почувствовал боль в области затылка.")
    with Fl_flash_red

    $ Fl.say(Fl_gg, "Твою ж...", _with=hpunch)
    $ Fl.say(Fl_r, "Я дотронулся рукой до того места, где раздалась боль.")
    $ Fl.say(Fl_kvl, "А точно! Ты ведь не помнишь, как лёг спать, так ведь?")
    $ Fl.say(Fl_r, "После этих слов, перед глазами пролетели флешбеки.")
    $ Fl.HideScreens()


    $ Fl.PlaySound("Fl_flashback", 1.0, 0, False)
    scene bg Fl_int_house_of_mi_night
    show Fl_prolog_dream
    with Fl_flash_fast

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_gg, "Мику, я туда и обратно, ладно?")
    $ Fl.HideScreens()



    $ Fl.PlaySound("Fl_flashback", 1.0, 0, False)
    scene Fl_ext_houses_night_bl
    show Fl_vignette2
    show Fl_prolog_dream
    with Fl_flash_fast

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_kt, "{color=#f00}...Я защищу тебя ...я не позволю кому-то навредить тебе!{/color}", cps="25")
    $ Fl.HideScreens()


    $ Fl.Status("-5")
    $ Fl.PlaySound("Fl_flashback", 1.0, 0, False)
    scene bg Fl_ext_path_day
    show Fl_light_c
    show Fl_fogging
    with Fl_flash_fast

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Я пошёл проверить, кто стучал в дверь. А потом меня вырубили. {w}А дальше провал{mn}")
    $ Fl.say(Fl_th, "Ты знаешь, кто меня вырубил?")
    $ Fl.say(Fl_kvl, "Нет, но я знаю что произошло дальше.")
    $ Fl.say(Fl_r, "Голос сделал паузу, после чего символично покашлял и продолжил.")
    $ Fl.say(Fl_kvl, "Кхм-кхм. Чтобы не было лишных вопросов скажу сразу. Если ты в отключке или спишь, я всё равно могу слышать что происходит вокруг. Это так чтобы вопросов не возникло.")
    $ Fl.say(Fl_kvl, "А касательно твоей вылазки, то после того как ты потерял сознание, кто-то тебя поволок обратно в домик. Возможно это была сама Мику...")
    $ Fl.say(Fl_th, "Я вешу под 70 килограмм, как она меня в одиночку могла дотащить?")
    $ Fl.say(Fl_kvl, "Не знаю, но ты вспомни с какой силой тебя схватила Мику за плечо!")
    $ Fl.say(Fl_r, "С моим собеседником было трудно не согласиться, хватка у неё то что надо. Но то что хрупкая пионерка смогла дотащить здорово парня в дом, а потом ещё уложить на кровать, было за гранью моего понимая.")
    $ Fl.say(Fl_th, "И что потом?")
    $ Fl.say(Fl_kvl, "Не знаю. Как только ты пересёк порок домика, я будто выпал из твоего сознания и вернулся только сейчас.")
    $ Fl.say(Fl_r, "В рассказе голоса была не состыковка во времени, как мне показалось в начале. Но вспоминая в котором часу все эти стуки начались, я отбросил прочь сомнения.")
    $ Fl.say(Fl_th, "А кто именно тебя послал меня охранять?")
    $ Fl.say(Fl_kvl, "Мне запрещено об этом рассказывать.")
    $ Fl.say(Fl_th, "Понятно, ещё больше загадок, да?")
    $ Fl.say(Fl_r, "Но на мой вопрос ответа не последовало.")

    $ Fl.Pause (2.0)
    $ Fl.say(Fl_kvl, "Что планируешь делать дальше?")
    $ Fl.say(Fl_th, "Не знаю. {w}Наверное, пока постараюсь жить обычной жизнью, а там посмотрим. Для начала мне нужно разобраться, что происходит с Мику, да и в целом понять что хочет от меня этот мир. А там посмотрим.")
    $ Fl.say(Fl_kvl, "Понятненько. {w}Дам тебе совет, сударь, постарайся не впадать в панику и депрессию. В таком состоянии ты себя точно загонешь в могилу.")
    $ Fl.say(Fl_r, "Я ничего не ответил, а лишь кивнул в знак понимания, в надежде что мой собеседник сможет понять этот жест.")
    $ Fl.say(Fl_kvl, "Кстати, ты на линейку случаем не опаздываешь?")
    $ Fl.say(Fl_gg, "Точно! Линейка!", _with=hpunch)

    hide Fl_fogging with Fl_dissolve1
    $ Fl.StopMusic(3)

    $ Fl.say(Fl_r, "Я резко вскочил и направился в сторону площади.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2 
    $ Fl.StopAmbience(3)
    $ Fl.Pause(3.5)


    $ Fl.Save("День2: Линейка.")

    $ Fl.Pause(2.5)
    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1.0, 4)
    scene bg Fl_ext_square_day
    show Fl_light_c
    with Fl_effect_mosaic

    $ Fl.Pause(2.0)

    $ Fl.Status("80")
    $ Fl.Status("normal", False)
    $ Fl.AutoSave()
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Оказавшись на площаде, я увидел большое скопление пионеров разных возростов, а возле каждой небольшой кучки пионеров стояли вожатые, которые что-то рассказывали заспанным детям.")
    $ Fl.say(Fl_th, "Сонное царство какое-то, а не линейка.")
    $ Fl.say(Fl_r, "Не спеша перебирая своими двумя я направился к своему отряду.")
    $ Fl.HideScreens(_with=Fl_fast)

    $ Fl.Pause(1.0)
    show an smile pioner1 with Fl_dissolve1

    $ Fl.Pause(1.0)
    show an serious pioner1 with Fl_fast

    $ Fl.Pause(1.0)
    hide an serious pioner1 with Fl_dissolve1

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Проходя мимо, я наткнулся на Аню, которая что-то увлечённо рассказывала рыжеволосой незнакомке. Но заприметив меня, её улыбка сменилась на каменное лицо. С чего бы это?")
    $ Fl.say(Fl_th, "А точно, букет{mn}")
    $ Fl.say(Fl_th, "Совсем вылетело из головы. Теперь мне от этой садистки не отвертеться, будет ещё чем-то шантажировать за неподчинение, а может и нет. Просто расскажет вожатой, какой я матершийник.")
    $ Fl.say(Fl_r, "Встав в конце отряда, я начал слушать дальнейшие указания вожатой.")
    $ Fl.PlayMusic("Fl_bridge_over_stars", 1, 5)
    $ Fl.HideScreens(_with=Fl_fast)


    show mv smile pioner1 with Fl_dissolve1

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_mv, "Отлично, все в сборе! {w}Можно начинать.")
    $ Fl.say(Fl_mv, "Дорогие пионеры первого отряда, сегодня у нас по плану:")
    $ Fl.say(Fl_mv, "Завтрак. {w}Потом до 12 отдых. {w}После чего общественные работы.")
    $ Fl.say(Fl_mv, "А дальше у нас обед, ужин и делайте до отбоя что хотите. {w}Если что-нибудь эдакое решите выкинуть, то мешки с сахаром всегда ждут новых работников. Всем ясно?")
    $ Fl.say(Fl_r, "Со стороны пионеров послышалось очень вялое «Да». Видно не я один не выспался сегодня.")
    $ Fl.say(Fl_r, "Я повернул голову, чтобы хоть как-то не уснуть под скучную речь вожатой.")
    $ Fl.say(Fl_r, "Мой взгляд остановился на аквамариновой пионерки, которая заметив меня, мило улыбнулась и помахала мне рукой. {w}Я помахал ей в ответ.")
    $ Fl.say(Fl_th, "Вот же стоит нормальная, жизнерадостная Мику. Что же тогда на неё утром нашло?")
    $ Fl.say(Fl_th, "А может она просто решила подшутить? Если не ошибаюсь, когда я выбежал из домика её голос уже был обычным.")

    show Fl_fogging with Fl_fast
    $ Fl.say(Fl_kvl, "А ты не подумал, что она может просто играет на публику, а на самом деле уже планирует, как нашего Яна за ушко укусить?")
    $ Fl.say(Fl_th, "Вот только мне твоих комментарий тут не хватало.")
    $ Fl.say(Fl_kvl, "Ну-ну. Ты ещё вспомнишь мои слова, когда будешь ходить весь в укусах!")
    hide Fl_fogging with Fl_fast

    $ Fl.say(Fl_r, "Напоследок ещё раз бросив взгяд в сторону Мику, я вновь начал слушать вожатую.")
    $ Fl.say(Fl_mv, "На этом всё, можете идти.")
    $ Fl.say(Fl_r, "Но походу я всё пропустил.")

    hide mv smile pioner1 with Fl_dissolve1

    $ Fl.say(Fl_th, "И это всё? {w}Ради этого стоило так рано вставать?!")

    show mv normal pioner1 with Fl_dissolve1

    $ Fl.say(Fl_r, "Не успел я высказать своё негодование, как вожатая направилась в мою сторону.")
    $ Fl.say(Fl_mv, "Ян, ты почему ко мне вчера не зашёл после ужина?")
    $ Fl.say(Fl_gg, "А, да точно.", cps="28")
    $ Fl.say(Fl_r, "Сделал вид я будто только сейчас вспомнил об этой просьбе.")

    show mv smile pioner1 with Fl_fast

    $ Fl.say(Fl_mv, "Ты где хоть ночевал, бомжик наш?")
    $ Fl.say(Fl_th, "Это наверное какая-то фишка вожатой постоянно делать «комплименты» ссылаясь на мою бороду.")

    show Fl_fogging with Fl_fast
    $ Fl.say(Fl_kvl, "Хех, но ты правда смахиваешь на бомжа. Ты бы постригся что-ли, Сударь.")
    $ Fl.say(Fl_th, "И ты ту даже? И без вас знаю, что нужно сбрить это лохмотье на лице.")
    hide Fl_fogging with Fl_fast

    $ Fl.say(Fl_gg, "Я задержался вчера с Мику до поздна, вот и не стал вас тревожить ночью. {w}А ночевал я как раз у Мику.")
    $ Fl.say(Fl_mv, "У Мику значит...")

    show mv laugh pioner1 with Fl_fast

    $ Fl.say(Fl_mv, "Надеюсь, ты к ней не приставал?")
    
    show Fl_fogging with Fl_fast
    $ Fl.say(Fl_kvl, "Я нет, а вот Мику себя предлага, но я затворник девственник не воспользовался ситуацией!")
    hide Fl_fogging with Fl_fast

    $ Fl.say(Fl_gg, "Нет конечно! С чего бы вдруг мне к ней приставать?")

    show mv smile pioner1 with Fl_fast

    $ Fl.say(Fl_mv, "Ну-ну, знаю я вас подростков. Да и ты у нас вроде к этому питаешь излишний интерес, за тобой нужен глаз до глаз!")
    $ Fl.say(Fl_r, "Я ухмыльнулся.")
    $ Fl.say(Fl_th, "Ну да. А какое ещё впечатление должно было сложиться у вожатой обо мне, после того как я обсуждал её нижнее бельё с Толяном?")
    $ Fl.say(Fl_mv, "Ладно, вижу вы с Мику неплохо ладите, поэтому вот держи.")
    $ Fl.say(Fl_r, "Вожатая протянула мне уже знакомый ключ.")
    $ Fl.say(Fl_mv, "Будешь жить вместе с Мику.")
    $ Fl.say(Fl_gg, "Но это разве можно по правилам селить мальчика к девочке?")
    show mv normal pioner2 with Fl_fast

    $ Fl.say(Fl_mv, "Эх, конечно нельзя, но другого выбора нет. Или ты хочешь жить с Толей?")

    show Fl_fogging with Fl_fast
    $ Fl.say(Fl_kvl, "Но Мику очень попросила, выделить помещение где она сможет тебя кусать когда захочет!")
    hide Fl_fogging with Fl_fast

    $ Fl.Status("-20")
    $ Fl.Status("tension", False)
    $ Fl.say(Fl_gg, "Нет! Спасибо! {w}Мне страшно с этим чудиком пересекаться, а тут ещё жить с ним!")

    show mv smile pioner2 with Fl_fast

    $ Fl.say(Fl_mv, "Как я и думала!")
    $ Fl.say(Fl_mv, "А и ещё, Ян.")
    $ Fl.say(Fl_r, "Вместо ответа, я вопросительно поднял бровь. Я довольно частенько в своей жизни прибегаю к общению мимикой.")
    $ Fl.say(Fl_mv, "Только попробуй начать приставать к Мику! Я тебя потом лично отвезу в отделение милиции!")
    $ Fl.say(Fl_th, "Вновь она за своё. У неё пластину заело или что?")

    show Fl_fogging with Fl_fast
    $ Fl.say(Fl_kvl, "Ну теперь тебе это клеймо не смыть. Смирись, Сударь.")
    hide Fl_fogging with Fl_fast

    $ Fl.say(Fl_gg, "Марина Владимировна, я уже в который раз повторяю, что не приставал и не собирась ни кому приставать!")
    $ Fl.say(Fl_r, "На что вожатая молча ухмыльнулась.")
    $ Fl.say(Fl_r, "Тяжело вздохнув, я взял ключи от домика.")
    $ Fl.Item("key13")
    $ Fl.say(Fl_mv, "Позже ко мне зайди, я тебе ещё форму дам.")
    $ Fl.say(Fl_gg, "Да мне и без неё хорошо.")

    show mv smile pioner1 with Fl_fast

    $ Fl.say(Fl_mv, "Никто и не говорит, что плохо. Но правила есть правила.")
    $ Fl.say(Fl_th, "Вновь эти правила. Как же я их ненавижу!")
    $ Fl.say(Fl_th, "Я никогда не понимал почему люди обязаны жить по сценарию с ограничениями, в виде правил. Казалось, что мешает человеку жить так, как ему нравится. Ведь быть счастливым важнее всего, а порядок сильно сковывает...")
    $ Fl.say(Fl_th, "Но моя точка зрения не имеет никакого смысла в мире людей. {w}Если снять правила в обществе, то человечество обречено на гибель. Выйти за рамки огранечения могут только особые личности, но их так мало, что такие белые вороны ничего не решают в этой жизни. {w}Как собственно и я...")
    $ Fl.say(Fl_gg, "Ладно...")

    show Fl_fogging with Fl_fast
    $ Fl.say(Fl_kvl, "Эх столько пафоса, а в конце всё же принял неизбежное.")
    hide Fl_fogging with Fl_fast

    $ Fl.say(Fl_mv, "Ладно, я пойду. Ты главное завтрак не пропусти, а то ещё не хватало, чтобы из-за голода пионеры с ног начали валиться.")
    $ Fl.say(Fl_gg, "Не пропущу.")

    hide mv smile pioner1 with Fl_dissolve1

    $ Fl.say(Fl_mv, "И главное не забудь ко мне зайти!")
    $ Fl.say(Fl_r, "Бросила на последок вожатая и скрылась в сторону столовой.")
    $ Fl.say(Fl_th, "Так а теперь...")

    $ Fl.Status("-10")
    $ Fl.Status("anger", False)
    $ Fl.say(Fl_th, "ТЫ КАКОГО <ХР*НА> СВОИХ ПЯТЬ КОПЕЕК ВЕЗДЕ ПИХАЕШЬ? И ЧТО ЕЩЁ ЗА СУДАРЬ?!", _with=hpunch)

    show Fl_fogging with Fl_fast
    $ Fl.say(Fl_kvl, "Ну так прикольно ведь звучит! Разве нет?")
    $ Fl.say(Fl_th, "Слушай, я понимаю что тебе скучно, но тебя вроде бы послали охранять меня, а не комментировать всё происходящее!")
    $ Fl.say(Fl_th, "Думаешь, мне вот так просто было принять факт, что ты реально в моей голове, а не шизофрения. Хотя я до сих пор сомневаюсь!")
    $ Fl.say(Fl_kvl, "Да чего ты так взъелся? Я ведь просто хочу разбавить обстановку.")
    $ Fl.say(Fl_th, "Лучше бы ты помогал и давал дельные советы, а не шутил. {w}Шутить и я умею...")
    $ Fl.StopMusic(3)
    hide Fl_fogging with Fl_fast

    $ Fl.Status("tension", False)
    $ Fl.say(Fl_r, "Я тяжело вздохнул. На мои плечи упал очень тяжкий груз - загадок этого необычного мира СССР. {w}Казалось решил вопрос с перерождением, а взамен пришли новые.")

    scene bg Fl_ext_square_day:
        ease 2.0 zoom 1.5 xalign 0.03 yalign 0.8
    show Fl_light_c

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_r, "Я присел на лавочку, мне нужно было немного собраться с мыслями. Привести себя в порядок, в переносном смысле.")
    $ Fl.say(Fl_r, "Обработав всю информацию, я не понимал что мне с ней делать.")
    $ Fl.say(Fl_r, "Ночные стуки, странное поведение Мику, голос в голове... Что дальше? {w}Терминатор появится на площади? {w}Генда оживёт?")
    $ Fl.say(Fl_r, "Я посмотрел на ключ, который крепко сжимал в руке.")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_th, "Теперь я живу вместе с Мику. {w}Даже не знаю радоваться мне или плакать... Утрений инцедент явно отразился на моём мнение о пионерке.")
    $ Fl.say(Fl_r, "Глубоко внутри меня что-то подсказывало, что это может быть глупой и неудачной шуткой и Мику просто решила разыграть меня, но другие факторы разрушали данный миф.")
    $ Fl.say(Fl_th, "Может стоит у неё самой спросить, о том что с ней произошло?")
    
    show Fl_fogging with Fl_fast
    $ Fl.say(Fl_kvl, "А ведь это не плохая идея, сударь. Только нужно выяснить это как-то аккуратно. Что-то мне подсказывает, что она даже не помнит что сегодня было утром.")
    $ Fl.say(Fl_th, "Значит ты больше склонен к теории что у неё раздвоение личности?")
    $ Fl.say(Fl_kvl, "Типо того.")
    $ Fl.say(Fl_kvl, "А ты сам как считаешь?")
    $ Fl.say(Fl_th, "Не знаю. Я как видишь сам пытаюсь найти ответ, что с ней не так.")
    hide Fl_fogging with Fl_fast

    $ Fl.PlaySound("Fl_dinner_horn_processed", 1, 0, False)
    $ Fl.Pause(4.0)
    
    $ Fl.Status("+20")
    $ Fl.say(Fl_th, "Так ладно, нужно развеяться и подкрепиться. А там уже решу что делать дальше!")

    scene bg Fl_ext_square_day:
        zoom 1.5 xalign 0.03 yalign 0.8
        ease 1.0 zoom 1.0 xalign 0.5 yalign 0.5

    $ Fl.say(Fl_r, "С этими словами я направился в столовую, попутно убрав ключ в карман.")
    $ Fl.say(Fl_th, "Стоп! А второй ключ в моём кармане это... Мику?")
    $ Fl.say(Fl_th, "Ну теперь есть повод зайти к ней и заодно расспросить обо всём. {w}Но только после того, как поем!")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_effect_mosaic


    $ Fl.Pause(4.0)
    scene bg Fl_ext_dining_hall_near_day with Fl_effect_mosaic
    $ Fl.Pause(1.0)
    scene bg Fl_ext_dining_hall_near_day:
        ease 3.0 zoom 1.5 xalign 0.3 yalign 0.55
    $ Fl.Pause(3.5)
    $ Fl.PlaySound("Fl_open_door_2", 1, 0, False)
    $ Fl.StopAmbience(2)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Save("День2: Хотел нормально позавтракать...")


    $ Fl.Pause(2.0)
    $ Fl.PlayAmbience("Fl_dining_hall_full", 1, 4)
    scene bg Fl_int_dining_hall_people_day with Fl_dissolve2

    $ Fl.Pause(1.0)
    $ Fl.Status("70")
    $ Fl.Status("normal", False)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.AutoSave()
    $ Fl.say(Fl_r, "Еле протолкнув своё тело в дворной проём, меня встретила следующая картина.")
    $ Fl.say(Fl_r, "Как и вчера, почти все столики в столовой были заняты голодными пионерами.")
    $ Fl.say(Fl_th, "Голодающее поволжье, ей богу!")
    $ Fl.say(Fl_th, "Здесь что все караулят столовую или как за такой короткий промежуток времени свободных мест почти нет?!")

    show Fl_fogging with Fl_fast
    $ Fl.say(Fl_kvl, "Поверь всегда! Хоть сам карауль это место ты никогда самым первым в столовой не будешь.")
    $ Fl.say(Fl_kvl, "Кстати хочу тебя огорчить, но свободное место походу только за столиком у окна.")
    hide Fl_fogging with Fl_fast

    $ Fl.say(Fl_th, "Огорчить?")

    $ Fl.PlaySound("Fl_swipe", 1.0, 0, False)
    scene bg Fl_int_dining_hall_people_day:
        subpixel True
        zoom 1.0 xalign 0.5 yalign 0.5
        ease 1.5 zoom 1.55 xalign 0.97 yalign 0.4
    $ Fl.Pause(1.0)

    $ Fl.say(Fl_r, "После чего я бросил взгляд в сторону стола, за которым сидел и перчил компот Толик. {w}Значит грибы на нём никак не отразились, раз он тут сидит и <х*рнёй> страдает.")

    scene bg Fl_int_dining_hall_people_day:
        subpixel True
        zoom 1.55 xalign 0.97 yalign 0.4
        ease 1.5 zoom 1.0 xalign 0.5 yalign 0.5

    $ Fl.say(Fl_th, "Понятно... {w}Ну другого выбора у меня нет. {w}Есть жутко хочется. Я ведь вчера толком не поужинал!")
    $ Fl.say(Fl_r, "Я направился к раздаче.")
    $ Fl.HideScreens(_with=Fl_fast)


    $ Fl.Pause(2.0)
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "На завтрак оказалась манная каша с компотом и простая булочка.")

    $ Fl.Status("+20")
    $ Fl.Status("good", False)
    $ Fl.say(Fl_r, "Заприметив содержимое на подносе, желудок радостно заурчал. И у меня чуть ли не в буквальном смысле потекли слюни.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause(2.0)
    show Fl_chair3
    show to normal pioneer:
        xalign 0.5
        Fl_pris2
    with Fl_dissolve1
    $ Fl.Pause(1.0)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Даже не попривествовав Толяна, я сел за стол и сразу же вцепился в ложку.")
    $ Fl.PlayMusic("Fl_fighting_johnny_vincent", 1, 8)

    show to smile pioneer with Fl_fast

    $ Fl.say(Fl_to, "Ян, ты вернулся!")
    $ Fl.say(Fl_gg, "Здарова, дружище! Я как посмотрю, ты жив здоров. Как там дядя Харис?")

    show to cry pioneer with Fl_fast

    $ Fl.say(Fl_to, "Плохо, его в больницу отвезли.")
    $ Fl.say(Fl_to, "Сказали что у дяди Хариса сильное отравление.")
    $ Fl.say(Fl_r, "Ответил Толик с грустью на лице, даже глаза помокрели.")
    $ Fl.say(Fl_th, "Значит придурковатая улыбка и покерфейс не единственные его эмоции.")
    $ Fl.say(Fl_th, "А вот дядю Хариса реально жалко, земля ему пухом.")
    $ Fl.say(Fl_gg, "Ясно, ну надеюсь ему полег...")
    $ Fl.say(Fl_r, "Неуспел я договрить, как за спиной раздался чей-то возглас.")

    show to smile pioneer with Fl_fast

    $ Fl.say(Fl_kt, "О Толян дружище!")

    show msk smile shirt at left with moveinleft

    $ Fl.say(Fl_r, "Перед нами нарисовался какой-то парень с радостной лыбой. Лицо было трудно разглядеть из-за чёлки, которая скрывала его глаза. Что ещё было примечательно на нём была чёрная рубашка, а не пионерская форма.")
    $ Fl.say(Fl_th, "А это случайно не тот гг хентая, который сидел с Аней и седым?")
    $ Fl.say(Fl_r, "Я посмотрел на Толяна. Вместо грустной мины на его лице вновь всплыла улыбка.")

    show Fl_fogging with Fl_fast
    $ Fl.say(Fl_kvl, "Опа, а вот и новый персонаж в истории «Реинкарнация бомжа-девственника».")
    $ Fl.say(Fl_th, "Это ты типо название тайтла придумал, да?")
    $ Fl.say(Fl_kvl, "Ага, думаю оно идеально подходит для твоей истории.")
    $ Fl.say(Fl_th, "Да иди ты. Достали вы уже. Сбрею я эту бороду!")
    $ Fl.say(Fl_kvl, "Хе-хе.")
    hide Fl_fogging with Fl_fast

    $ Fl.say(Fl_to, "Миха, ты вернулся!")
    $ Fl.say(Fl_th, "Он что так каждому в лагере удивляется? {w}Меньше суток с ним виделись, а тут радости на лице было столько, что не передать словами. А теперь тоже самое с Михой.")

    hide  msk smile shirt with Fl_fast

    show Fl_chair3:
        xalign 0.85
    show to normal pioneer:
        ypos 0.07 zoom 1.0 xalign 0.85
    with moveinleft
    
    show Fl_chair2:
        xalign 0.05
    show msk smile shirt:
        xalign 0.05
        Fl_pris2
    with Fl_dissolve1

    $ Fl.say(Fl_r, "Толян немного подвнулся вправо, после чего Миха(так звали этого парня, если верить словам Толика) поставил поднос и уселся рядом с ним.")
    $ Fl.say(Fl_msk, "Я тебя тоже рад видеть приятель! Слышал ты вчера Хариса грибами <у*бал>?")

    show to cry pioneer with Fl_fast

    $ Fl.say(Fl_to, "Ага. Его в больницу отвезли.")
    $ Fl.say(Fl_r, "Толян снова поник. И мне стало любопытно.")
    $ Fl.say(Fl_gg, "Кто это вообще?")

    show msk grin shirt with Fl_fast

    $ Fl.say(Fl_msk, "Да местный повар, Харис Обдристайлович!")

    $ Fl.PlaySound("Fl_msk_laugh", 1, 0, False)
    $ Fl.say(Fl_msk, "Готовит тут свою фирменную аджику, а потом пионеры носятся по площади!")
    $ Fl.say(Fl_gg, "Кароче местный шаурмечник?")

    show msk happy2 shirt with Fl_fast

    $ Fl.say(Fl_msk, "<Бл*>, да он самый!")

    show msk smile shirt with Fl_fast

    $ Fl.say(Fl_msk, "Толян, братишка, ну ты чего?")
    $ Fl.say(Fl_to, "Дядю Хариса жалко.")
    $ Fl.say(Fl_msk, "Да лан тебе оклимается и вернётся. Ещё пару кошек притащит, потом такой шаверы навертит, что закачаешься!")

    show to happy pioneer with Fl_fast

    $ Fl.say(Fl_to, "Правда?")
    $ Fl.say(Fl_msk, "Конечно, дружище! Я тебе хоть раз <п*здел>?")

    show Fl_fogging with Fl_fast
    $ Fl.say(Fl_kvl, "Мда. Словарный запас у него очень большой. А какие слова культурные он знает.")
    $ Fl.say(Fl_th, "Не поспоришь. Мне интересно, как ему удалось Аниного шантажа избежать. {w}Она бы такую возможность не упустила никогда в жизни.")
    $ Fl.say(Fl_kvl, "Ну как ты успел заметить, ладят они походу не плохо. За одним столиком даже обедали.")
    hide Fl_fogging with Fl_fast

    show to smile pioneer with Fl_fast

    $ Fl.say(Fl_msk, "Кста, как тебя звать то?")
    $ Fl.say(Fl_r, "Прервал мой разговор с голосом, Михан.")
    $ Fl.say(Fl_gg, "Ян.")

    show msk grin shirt with Fl_fast

    $ Fl.say(Fl_msk, "Приколдесное имя! Буду звать тебя Янчиком!")
    $ Fl.say(Fl_r, "В прошлой жизни почти все знакомые так ко мне обращались. Поэтому такое коверканье имени я оценил и даже улыбнулся.")
    $ Fl.say(Fl_gg, "А ты Михан, как я пологаю?")
    $ Fl.say(Fl_msk, "Не просто Михан, а Михалыч Михайлович Михайлов Михайловавыч Первый. {w}Первый император юморной категории.")
    $ Fl.say(Fl_gg, "Ладно{mn}")
    $ Fl.say(Fl_r, "Михан взял стакан компота и поднял вверх.")

    show msk smile2 shirt with Fl_fast

    $ Fl.say(Fl_msk, "Ну бухнём за знакомство!")
    $ Fl.say(Fl_r, "На моём лице расплылась улыбка. Я тоже взял стакан компота и повторил все движения за Миханом.")
    $ Fl.say(Fl_gg, "За знакомство!")

    $ Fl.PlaySound("Fl_glasses_wine", 1, 0, False)
    $ Fl.say(Fl_r, "Мы чокнулись и отпили немного красной жижи, представляя что это что-то алкогольное.")

    show msk surprise shirt
    $ Fl.PlaySound("Fl_kashlja", 1, 0, False)
    $ Fl.say(Fl_msk, "<Бл*ть> это чё за <х*йня>! Почему компот перчённый? Там повара совсем <еб*нулись>?!", _with=hpunch)
    $ Fl.say(Fl_r, "Закричал чуть ли не на всю столовую Михан, вытирая слёзы и крехтя.")

    show to cry pioneer with Fl_fast

    $ Fl.say(Fl_to, "Миха, прости, это я поперчил думал тебе понравится.")

    show msk sad shirt with Fl_fast

    $ Fl.say(Fl_msk, "Толян, ты хоть предупреждай, когда собираешь сделать какую-то <х*рню>. Я же как ни как за тебя отвественность несу.")

    show Fl_fogging with Fl_fast
    $ Fl.say(Fl_kvl, "Так а вот это уже интересненько.")
    $ Fl.say(Fl_th, "Поддерживаю! {w}Мне теперь и самому интересно стало, что у них там за отношения такие.")
    hide Fl_fogging with Fl_fast

    $ Fl.say(Fl_gg, "В каком смысле ты несёшь за него отвественность?")

    show msk smile shirt with Fl_fast

    $ Fl.say(Fl_msk, "А, ну тип я его опекун или что-то в этом роде.")

    show Fl_fogging with Fl_fast
    $ Fl.say(Fl_kvl, "Интересно!")
    $ Fl.say(Fl_th, "Походу мы батю Толика нашли!")
    hide Fl_fogging with Fl_fast

    $ Fl.say(Fl_gg, "Опекун? {w}В каком смысле опекун? Неужели он твой брат?")

    show msk upset shirt with Fl_fast

    $ Fl.say(Fl_msk, "Ян, ты <еб*нутый>? {w}Какой <нах*й> брат, ты его видел?")
    $ Fl.say(Fl_r, "Получил я ответ от человека с очень большим литературным запасом.")

    show to smile pioneer with Fl_fast

    $ Fl.say(Fl_to, "Его назначили присматривать за мной, чтобы я не делал ничего странного.")

    show msk grin shirt with Fl_fast

    $ Fl.say(Fl_msk, "Ну как назначили. {w}Там просто Маринка предложила побыть опекуном его, я конечно в начале отказался...")
    $ Fl.say(Fl_msk, "Но как услышал, что можно <н*хрена> не делать, а только за этим чудиком присматривать, то согласился сразу на части «<н*хрена> не делать»!")

    show Fl_fogging with Fl_fast
    $ Fl.say(Fl_kvl, "Кого-то он мне на поминает...")
    $ Fl.say(Fl_th, "Нечего меня с ним сравнивать. Я вообще-то работал круглые сутки раньше!")
    $ Fl.say(Fl_kvl, "Ну это когда было.")
    $ Fl.say(Fl_th, "Цыц!")
    hide Fl_fogging with Fl_fast

    $ Fl.say(Fl_gg, "Вот как. Вожатой мало, Толяну ещё и опекуна подкинули.")
    $ Fl.say(Fl_mv, "Ян...")
    $ Fl.StopMusic(2)

    $ Fl.Status("-50")
    $ Fl.Status("stress", False)
    $ Fl.say(Fl_r, "Раздался сзади, словно гром среди ясного неба, голос вожатой.")
    $ Fl.say(Fl_r, "От неожиданности, я чуть ли не подпрыгнул.")

    show Fl_chair3:
        xalign 0.98
    show to normal pioneer:
        ypos 0.07 zoom 1.0 xalign 0.98
    with moveinleft
    
    show Fl_chair2:
        xalign 0.01
    show msk sad shirt:
        xalign 0.01 ypos 0.07 zoom 1.0
    with moveinright

    show mv laugh pioner2 with Fl_fast

    $ Fl.say(Fl_mv, "Прости-прости. Не хотела тебя напугать.")

    show mv smile pioner1 with Fl_fast

    $ Fl.say(Fl_mv, "Я тебе забыла утром дать обходной.")
    $ Fl.say(Fl_mv, "Вот держи, соберёшь все подписи и отдашь мне.")

    $ Fl.Status("+50")
    $ Fl.Status("good", False)
    $ Fl.say(Fl_r, "Сказала вожатая и протянула мне какой-то клочёк бумажки. На котором были записаны места и рядом люди, возможно те кто мне и должны подписать пустую графу рядом.")
    $ Fl.say(Fl_r, "{u}Медпункт{/u} – Виолетта Церновна Коллайдер. {w}{u}Клуб кибернетики{/u} – Демьяненко Александр. {w}{u}Музыкальный клуб{/u} – Хатсунэ Мику. {w}{u}Библиотека{/u} – Морозина Евгения. {w}{u}Клуб рисования и поэзии{/u} - Мирослава Добровольская. {w}{u}Спорт-клуб{/u} - Игорь Владимирович.")
    $ Fl.say(Fl_mv, "Ну всё не буду вас отвлекать.")

    hide mv smile pioner1 with Fl_dissolve1

    $ Fl.say(Fl_r, "После чего вожатая быстро удалилась из столовой, не забыв отнести свой поднос.")

    show Fl_chair3:
        xalign 0.85
    show to normal pioneer:
        ypos 0.07 zoom 1.0 xalign 0.85
    with moveinright
    
    show Fl_chair2:
        xalign 0.05
    show msk smile shirt:
        xalign 0.05 ypos 0.07 zoom 1.0
    with moveinleft

    $ Fl.Pause(1.0)
    $ Fl.say(Fl_gg, "Слушай, Михан, ты знаешь где находятся этими места?")
    $ Fl.say(Fl_msk, "Конечно, хоч могу с тобой сгонять?")
    $ Fl.say(Fl_gg, "Было бы неплохо.")

    show msk smile2 shirt with Fl_fast

    $ Fl.say(Fl_msk, "Толентий, ты с нами?")

    show to smile pioneer with Fl_fast

    $ Fl.say(Fl_r, "Вместо ответа Толик качнул головой, нацепив вновь придурковатую улыбку.")

    show msk evilsmile shirt with Fl_fast

    $ Fl.say(Fl_msk, "Тогда доедаем и шагом марш!")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(3)


    $ Fl.HideScreens(_with=Fl_dissolve1)

    $ Fl.PlaySound("Fl_pause_time", 1.0, 2, False)
    scene Fl_pause
    with Fl_effect_time_pause


    $ Fl.Pause (3.0)
    scene bg Fl_black with Fl_dissolve2
    $ Fl.Pause (1.0)

    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 5)
    scene bg Fl_ext_dining_hall_near_day
    show Fl_light_c
    with Fl_dissolve2


    $ Fl.Save("День2: Приключение с Михалычем и Толентием.")
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Когда с завтраком было поконченно, мы с Миханом и Толик вышли из столовой. {w}Миха сразу развалился на лавочке, а Толян стоял и тупил(как обычно в принципе).")
    $ Fl.say(Fl_gg, "И куда в начале пойдём?")
    $ Fl.say(Fl_msk, "В клубы. Они ближе всего, а там посмотрим.")
    $ Fl.say(Fl_r, "Миха встал и посмотрел прямо. После чего направился по дорожке, которая ведёт к воротам. А мы последовали за ним следом.")
    $ Fl.HideScreens(_with=Fl_fast)


    scene bg Fl_black with Fl_effect_3
    $ Fl.Pause (1.5)

    scene bg Fl_ext_clubs_day
    show Fl_light_c
    with Fl_effect_3

    $ Fl.Pause (1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Дойдя до конца, перед нами нарисовалось уже знакомое мне здание клубов, разве что Кати в этот раз нигде не видно.")

    show msk smile shirt with Fl_fast:
        left

    $ Fl.say(Fl_msk, "Так <бл*>. Я захожу первый вы за мной. Разговаривать тож буду я. Пацаны там прикольные, так что сто проц х*йню какую-то попросят взамен.")
    $ Fl.say(Fl_gg, "Ладно, давай заходи.")
    $ Fl.HideScreens()

    show msk smile shirt:
        subpixel True
        yalign 0.5 xalign 0.05
        ease 1.5 yalign 0.5 xalign 0.5

    $ Fl.Pause (1.5)
    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
    hide msk smile shirt with Fl_fast

    $ Fl.Pause (1.0)
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_th, "Ладно посмотрим, что там за пацаны такие. {w}Может даже подружимся, кто его знает.")
    $ Fl.HideScreens(_with=Fl_fast)
    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)


    scene bg Fl_black with Fl_effect_3
    $ Fl.Pause (1.5)

    scene bg Fl_int_clubs_male_day with Fl_effect_3
    $ Fl.Save("День2: Мужской клуб...")

    $ Fl.Pause (1.0)
    $ Fl.PlayMusic("Fl_smeshnoy_moment", 1, 4)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.AutoSave()
    $ Fl.say(Fl_r, "Как только я зашёл во внутрь, то сразу начал всё осматривать. Помещение оказалось своего рода мастерской или школьного кабинета труда.")

    scene bg Fl_int_clubs_male_day:
        zoom 1.0 xalign 1.0 yalign 0.5
        linear 2.0 zoom 2.0 xalign 1.0 yalign 0.5
    $ Fl.Pause (2.0)
    $ Fl.say(Fl_th, "Какие-то чертежи авиамоделей. {w}Неинтересно...")

    scene bg Fl_int_clubs_male_day:
        zoom 2.0 xalign 1.0 yalign 0.5
        linear 1.0 zoom 2.0 xalign 1.0 yalign 1.0
    $ Fl.Pause (1.0)
    $ Fl.say(Fl_th, "О даже кампухтер у них есть. {w}Надеюсь хоть косынку он потянет и не сгорит, под синим экраном.")

    scene bg Fl_int_clubs_male_day:
        zoom 2.0 xalign 1.0 yalign 1.0
        linear 1.0 zoom 3.0 xalign 1.0 yalign 0.0
    $ Fl.Pause (2.0)
    $ Fl.say(Fl_th, "Понятно... {w}Даже спрашивать не буду что это делает в здании науки СССР.")

    scene bg Fl_int_clubs_male_day:
        zoom 3.0 xalign 1.0 yalign 0.0
        linear 1.0 zoom 3.0 xalign 0.1 yalign 0.0
    $ Fl.Pause (1.0)
    $ Fl.say(Fl_r, "Самолёты, которые были сооружены по чертежам, виденные мной ранее.")
    $ Fl.say(Fl_th, "Они на божем духе держатся или что? {w}Кто додумался их вверх ногами повесить?")
    $ Fl.HideScreens(_with=Fl_fast)


    scene bg Fl_black with Fl_effect_3
    $ Fl.Pause (0.5)

    scene bg Fl_int_clubs_male_day
    show msk grin shirt:
        fright
    show art normal pioneer1:
        fleft
    show ss normal pioneer3
    with Fl_effect_3

    $ Fl.Pause (1.0)
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_msk, "Ну чё, здоров, поцаны! {w}Как тусуете?")

    show art smile pioneer1 with Fl_fast
    show ss smile pioneer1 with Fl_fast

    $ Fl.say(Fl_artp, "Какие люди! {w}За чем пожаловал, Мих?")
    $ Fl.say(Fl_r, "Первый завёл диалог с Миханом кудрявый парень с чёрными волосами. Внешнее он смахивал на человека еврейских кровей.")
    $ Fl.say(Fl_r, "Он кого-то мне напоминал, но вот кого - загадка, память то я частично утратил. {w}Но я догадываюсь, что на кого-то из моих одноклассников.")
    $ Fl.say(Fl_th, "Кстати нужно будет потом у моего Эго спросить, может он что-то скажет про моё стирание воспоминаний.")
    $ Fl.say(Fl_ssp, "Миха, сколько лет сколько зим!")
    $ Fl.say(Fl_r, "Теперь к разговор подключился уже второй парень с серыми волосами. На лице парня красовались очки, которые скрывали тёмно-красные глаза.")
    $ Fl.say(Fl_th, "Это ещё что за молодой Канеки?")
    $ Fl.say(Fl_msk, "Так. Знакомьтесь! {w}Это Янчик, топовый пацанчик!")
    $ Fl.say(Fl_msk, "Ян, вот этот заросший - Артём. {w}А вот этот молодой дедушка - Саня.")

    show ss upset pioneer1 with Fl_fast

    $ Fl.say(Fl_ss, "Да с рождения у меня такой цвет волос! Достали прикалываться!")

    show msk happy2 shirt with Fl_fast

    $ Fl.PlaySound("Fl_msk_laugh", 1, 0, False)
    $ Fl.say(Fl_msk, "Ну всё, Александр, извините. В вашем возрасте волноваться нельзя.")

    show art laugh pioneer3 with Fl_fast

    $ Fl.say(Fl_art, "Приятно познакомиться, Янчик! И добро пожаловать в наше пристанище беззакония. Здесь ты всегда можешь спряться от поручений Маринки и побазарить с мужиками!")
    $ Fl.say(Fl_r, "Сказал Артём с гордой улыбкой на лице и протянул мне руку.")
    $ Fl.say(Fl_th, "Вот в таких местах и зарождается мужская дружба.")

    show Fl_fogging with Fl_fast
    $ Fl.say(Fl_kvl, "Если ты планируешь сменить жанр своего тайтла на яой, то я повешусь.")
    $ Fl.say(Fl_th, "И каким образом?")
    $ Fl.say(Fl_r, "Я представил себе следующую картину. {w}Как шиза со слезами на глазах, лезет в петлю, а после поднимает голову вверх и смотрит на потолок с путым, бездушным взглядом. После чего мгновение и стул падает на пол...")
    $ Fl.say(Fl_kvl, "Что нибудь придумаю не переживай.")
    hide Fl_fogging with Fl_fast

    $ Fl.say(Fl_r, "Мы обменялись рукопожатием и к слову с Саней тоже.")
    $ Fl.say(Fl_gg, "Значит вы и есть те самые Саня и Артём, которых Катя вчера весь день искала?")

    show msk smile shirt with Fl_fast
    show art grin pioneer1 with Fl_fast
    show ss laugh pioneer1 with Fl_fast

    $ Fl.say(Fl_art, "Они самые!")
    $ Fl.say(Fl_ss, "Да, мы тут местные знаменитости!")
    $ Fl.say(Fl_r, "Я ухмыльнулся. Почему-то мне было очень весело и смешно от гордости местного криминала. {w}Возможно глядя на них я вспоминал себя в подростковом возрасте, такой же безбашенный авантюрист.")
    $ Fl.say(Fl_gg, "Я полагаю, вы тут весь лагерь на уши поднять можете.")

    show art smile pioneer1 with Fl_fast

    $ Fl.say(Fl_art, "Да запросто!")

    show msk happy shirt with Fl_fast

    $ Fl.say(Fl_msk, "Да ну? {w}Может напомнить кто тут батя криминала?")
    $ Fl.say(Fl_msk, "Только батя может материться прямо при вожатой, а потом бегать от неё по-всему лагерю!")
    $ Fl.say(Fl_msk, "Только батя может ходить не в пионерской форме по лагерю!")

    show art normal pioneer1 with Fl_fast

    $ Fl.say(Fl_art, "Мих, <х*ре> выпендриваться. Ты вчера весь вечер мешки с сахором таскал, кому ты тут лапшу вешаешь?")

    show msk sad shirt with Fl_fast

    $ Fl.say(Fl_msk, "Да я его весь схавал, а не отнёс, понял?!")

    show ss smile pioneer1 with Fl_fast

    $ Fl.say(Fl_r, "И начался спор века. {w}Парни пытались доказать кто из них более опасный в лагере.")

    show art normal pioneer1 with Fl_fast

    $ Fl.say(Fl_r, "А стоял и сдерживал смех. Всё происходящее напоминало мне детский сад не более.")

    show msk smile shirt with Fl_fast

    $ Fl.say(Fl_msk, "А, точно! Мы ведь здесь за обходным пришли.")
    $ Fl.say(Fl_gg, "Пацаны, можете подписать? А то вожатая не отстанет?")
    $ Fl.say(Fl_art, "Обходной? {w}А ты же новенький, точно.")

    show art smile pioneer1 with Fl_fast

    $ Fl.say(Fl_art, "Давай свою макулатуру.")
    $ Fl.say(Fl_r, "Порывшись по карманам, я нашёл свой обходной лист и протянул его Артёму.")
    $ Fl.say(Fl_art, "Сань, принеси ручку!")

    show ss upset pioneer1 with Fl_fast

    $ Fl.say(Fl_ss, "А чё я сразу? Сходи сам!")

    show art serious pioneer3 with Fl_fast

    $ Fl.say(Fl_art, "Саня, не ной, иди давай!")

    hide ss upset pioneer1 with Fl_dissolve1
    show art normal pioneer1 with Fl_fast

    $ Fl.say(Fl_r, "Саня тяжело вздохнул, но всё же не стал спорить с другом и пошёл в кладовку за ручкой.")

    $ Fl.Pause(3.0)

    show ss upset pioneer1 with Fl_dissolve1

    $ Fl.say(Fl_r, "Саню долго ждать не пришлось. Придя обратно к нам, Саня протянул ручку Артёму с недовольным лицом.")

    $ Fl.Pause(3.0)

    show art smile pioneer1 with Fl_fast
    $ Fl.say(Fl_art, "Держи.")
    $ Fl.say(Fl_r, "Поставив какую-то карлякую, а не подпись, Артём отдал мне обходной.")
    $ Fl.say(Fl_gg, "От души!")

    show ss smile pioneer1 with Fl_fast

    $ Fl.say(Fl_ss, "Ян, если что заходи, как время появится. Пообщаемся, может в картишки перекинимся, бухнём чего.")
    $ Fl.say(Fl_gg, "Ого, у вас и выпивка имеется? Откуда?")

    show art grin pioneer1 with Fl_fast

    $ Fl.say(Fl_art, "От верблюда. {w}Мы можем достать что угодно в этом лагере, а как уже секрет.")
    $ Fl.say(Fl_gg, "Всё с вами понятно, контробандой балуетесь.")
    $ Fl.say(Fl_r, "На моей ответ, парни только сильнее улбынулись, светясь прям от радости своему криминальному статусу.")
    $ Fl.say(Fl_gg, "Ладно, мы пойдём. Нужно ещё куча мест обойти.")

    show art smile pioneer1 with Fl_fast

    $ Fl.say(Fl_art, "Давайте пацаны, удачи!")
    $ Fl.say(Fl_ss, "Если что предложение в силе!")
    $ Fl.say(Fl_msk, "Окей, давайте! {w}Мы погнали!")

    hide msk smile shirt with Fl_fast

    $ Fl.say(Fl_r, "Распрощавшись с парнями, мы с Миханом вышли наружу.")
    $ Fl.HideScreens(_with=Fl_fast)
    $ Fl.StopMusic(3)
    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)


    scene bg Fl_black with Fl_effect_left2
    $ Fl.Pause (1.5)

    scene bg Fl_ext_clubs_day
    show Fl_light_c
    with Fl_effect_left2

    show msk smile shirt with Fl_fast

    $ Fl.Save("День2: Приключение с Михалычем и Толентием.")
    $ Fl.Pause (1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_msk, "Чё скажешь про пацанов?")
    $ Fl.say(Fl_gg, "Ну{mn} {w}Прикольные ребята, что могу ещё сказать. С такими явно не заскучаешь!")

    show msk grin shirt with Fl_fast

    $ Fl.say(Fl_msk, "Это да!")

    show msk serious shirt with Fl_fast

    $ Fl.say(Fl_msk, "Кста, а где Толян?")
    $ Fl.say(Fl_th, "Действительно.")
    $ Fl.say(Fl_r, "Мы переглянулись, после чего начали глазами искать нашего друга со справкой.")

    $ Fl.Pause (1.5)

    show to smile pioneer at Fl_fromtop_per(1300, 0.5):
        xalign 1.9 rotate -55.0 yalign 0.7

    
    $ Fl.say(Fl_to, "Ян, Миха, вот вы где!{break2}")

    show msk surprise shirt with vpunch

    $ Fl.Status("-30")
    $ Fl.Status("tension", False)
    $ Fl.say(Fl_gg, "<Бл*ть>, Толян!", _with=hpunch)
    $ Fl.say(Fl_r, "Наш друг со справкой появился справа довольно неожиданно, что и заставило нас с Михой подскочить.")

    show msk evilsmile shirt with Fl_fast

    $ Fl.Status("+30")
    $ Fl.Status("good", False)
    $ Fl.say(Fl_msk, "А вот и Толентий нашёлся. {w}Ты где был, мой друг?")

    hide to smile pioneer with Fl_fast

    $ Fl.Pause (1.0)

    show to normal pioneer with Fl_fast:
        xalign 0.99

    $ Fl.say(Fl_to, "Я вас искал. Я хотел вам кота показать, но вы куда-то пропали.")
    $ Fl.say(Fl_th, "Это моя вина... {w}Нужно было проследить, чтобы этот контуженный тоже зашёл.")
    $ Fl.say(Fl_msk, "<Бл*>, ну ты даёшь конечно, Толян!")

    show msk smile shirt with Fl_fast

    $ Fl.say(Fl_msk, "Ну давай показывай своего кота.")

    show to smile pioneer with Fl_fast

    $ Fl.say(Fl_r, "Толян поднял палец и указал прямо на предмет, лежащий возле кустов. Им оказался... {w}чей-то чёрный носок.")
    $ Fl.say(Fl_gg, "Мда{mn}")

    $ Fl.PlayMusic("Fl_fighting_johnny_vincent", 1, 0)
    show msk happy2 shirt with Fl_fast

    $ Fl.PlaySound("Fl_msk_laugh", 1, 0, False)
    $ Fl.say(Fl_msk, "АХАХАХ! {w}Ору, сук!")
    $ Fl.say(Fl_msk, "Толян, это <бл*ть> носок! Аахахах.")

    $ Fl.PlaySound("Fl_msk_laugh", 1, 0, False)
    $ Fl.say(Fl_msk, "АХАХААХАХА!", _with=hpunch)

    show msk evilsmile shirt with Fl_fast

    $ Fl.PlaySound("Fl_msk_laugh", 1, 0, False)
    $ Fl.say(Fl_msk, "Эй, Барсик, вставай <бл*ть> на работу пора! Ахахахахах!")

    hide msk evilsmile shirt with Fl_fast

    $ Fl.say(Fl_r, "Михан, прям конкретно начало расспирать от смеха, он начал подыгрывать Толяну и гладить носок, представляя его настоящим котом.")

    hide to smile pioneer with Fl_fast

    $ Fl.say(Fl_r, "К нему ещё подключился Толик и теперь этих два идиота угарали и общались с носком... {w}Да с носком...")
    $ Fl.say(Fl_r, "Все проходящие мимо пионеры начали коситься в нашу сторону осуждающим взглядом, а у кого-то и вовсе в глазах проскакивала нотка грусти и сожаления. {w}Наверное, в глазах других мы смахивали на троицу сбежавшую из психушки или с наркопритона.")
    $ Fl.say(Fl_gg, "Всё хватит уже дурью маяться, на нас уже косо смотрят.")

    show msk smile shirt with Fl_fast

    $ Fl.say(Fl_msk, "Ух, давно я так не ржал! {w}Толян это нечто, с ним не соскучишься.")
    $ Fl.say(Fl_th, "Это точно.")
    $ Fl.say(Fl_msk, "Толян, оставь Барсика в покое, пошли нам ещё Янчику бегунок нужно заполнить!")
    $ Fl.say(Fl_r, "Пионер с залысиной послушно оставил «Барсика» в покое и подошёл к нам с дурацкой лыбой.")

    show to smile pioneer with Fl_fast:
        xalign 0.99

    $ Fl.say(Fl_gg, "Так теперь нам нужно на спортплощадку.")
    $ Fl.say(Fl_r, "Поставил я следующую цель, прочитав второй пункт обходного листа.")
    $ Fl.say(Fl_msk, "Не слова больше! Шагам марш, <бл*>!")
    $ Fl.say(Fl_r, "Скомандовал наш навигатор, и мы двинулись в путь.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(3)
    $ Fl.StopAmbience(3)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(2.5)

    $ Fl.PlayAmbience("Fl_soccer_play_background", 1, 4)
    scene bg Fl_ext_playground_day 
    show Fl_light_c
    with Fl_dissolve2

    $ Fl.Pause(1.0)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.AutoSave()
    $ Fl.say(Fl_r, "Слушая байки Михалыча, под ногами бетон сменился на состриженную траву. Что гласило нам о том, что мы на месте.")
    $ Fl.say(Fl_r, "Спортплощадка представляла из себя, огромное футбольное поле с подобием трибуны, если так можно назвать парочку лавочек стоящих в ряд. И ещё парочку турнекетов стояло неподалёку.")
    $ Fl.say(Fl_r, "На поле во всю шла игра. Парни ловко крутились с мячом, перекатывая мяч то к одному игроку, то к другому. {w}Играли они довольно хорошо, каждый в поте лица старался обыграть своего опонента, делая трудные финты и придерживаясь какой-то стратегии, возможно придуманной заранее.")
    $ Fl.say(Fl_th, "Эх, молодость. Когда-то тоже так с ребятами во дворе играли.")

    show Fl_fogging with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Тоже нашёлся мне тут старый, тебе всего 19, а говоришь так будто вот-вот внуки должны приехать, сидя на кресле и читая газету.")
    $ Fl.say(Fl_th, "В душе я старый человек, я уже столько повидал в своей жизни, что мне уже на покой пора.")
    $ Fl.say(Fl_kvl, "Да-да. Расскажи.")
    $ Fl.say(Fl_th, "Отстань! Дай поностальгировать!")
    hide Fl_fogging with Fl_dissolve1

    show msk smile shirt with Fl_fast

    $ Fl.say(Fl_msk, "Так, Янчик, кароч смотри вон там раздевалка и кабинет физрука.")
    $ Fl.say(Fl_r, "Я направил взгляд куда указывал Михан. Справа от турников действительно находилось небольшое здание, напоминающее обычную коробку.")
    $ Fl.say(Fl_gg, "А ты не пойдёшь?")
    $ Fl.say(Fl_msk, "Не. У меня короч... {w}Проблемные отношения с физруком.")
    $ Fl.say(Fl_msk, "Так что я тут подожду, может щас на турничках чё нибудь поделаю.")
    $ Fl.say(Fl_gg, "Ладно, удачи, турникмен!")
    $ Fl.say(Fl_r, "И отправился в сторону огромной подсобки, по-другому снаружи здание не описать.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(3)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(4.5)

    scene bg Fl_int_sporthall_day with Fl_dissolve2

    $ Fl.Save("День2: Местный бодибилдер.")
    $ Fl.Pause(1.0)
    $ Fl.Status("80")
    $ Fl.Status("normal", False)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Обойдя всё здание вдоль и поперёк я не смог найти физрука. Остановил я свои поиски в каком-то спортзале. По-середине спортзала была натянута волейбольная сетка, а в самом углу шведская стенка с матами.")
    $ Fl.say(Fl_r, "Моё внимание привлёк мужчина крупного телосложения, который кричал на детей и свистел в свисток.")
    $ Fl.say(Fl_r, "Было не трудно догадаться, что это и был физрук пионерлагеря.")
    $ Fl.say(Fl_th, "Ну наконец-то, я уж думал вечность буду шляться по этим коридорам. А снаружи здание казалось маленьким...")
    $ Fl.HideScreens(_with=Fl_dissolve1)

    $ Fl.Pause(2.0)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_gg, "Извините.")
    
    $ Fl.PlayMusic("Fl_smeshnoy_moment", 1, 4)
    show ba em1 uniform with Fl_dissolve1

    $ Fl.say(Fl_ba, "Чего тебе?")
    $ Fl.say(Fl_r, "Отозвался светловолосый качок в спортивных штанах и в красной майке, на которой был изображён герб СССР в необычном дизайне.")
    $ Fl.say(Fl_gg, "Мне вот нужно обходной подписать.")

    show ba normal uniform with Fl_fast

    $ Fl.say(Fl_r, "Физрук прищурил глаза и посмотрел на меня с недоверием, а потом на обходной. А потом вновь на меня.")

    show ba smile uniform with Fl_fast

    $ Fl.say(Fl_ba, "Понятно, ну давай подпишу. А ты выбирай куда вступать будешь, а то совсем дрышь какой-то.")
    $ Fl.say(Fl_th, "Ага, обязательно! Мне же для полного счастья только спорта не хватает.")

    show Fl_fogging with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Ну тебе бы и правда не помещало хотя бы бегом заняться. Иметь отдышку от того что ты по кабинетам побегал это ненормально, Сударь.")
    $ Fl.say(Fl_th, "Я в своё время занимался спортом и накачал прессуху, сейчас оно мне зачем?")
    $ Fl.say(Fl_kvl, "Мда, всё с тобой понятно. Ну потом не жалуйся, когда в следующий раз от Мику будешь бежать и в глазах потемнеет.")
    hide Fl_fogging with Fl_dissolve1

    $ Fl.say(Fl_ba, "Держи, задохлик, свой обходной.")
    $ Fl.say(Fl_r, "Физрук протянул мне лист, на котором уже появилась вторая подпись. Вторая подпись значительно отличалась от первой, которую поставил Артём, она была ровной и аккуратной.")
    $ Fl.say(Fl_ba, "Ну что куда вступить решил? {w}Волейбол, футбол, атлетика? {w}Куда тебя записывать?")
    $ Fl.say(Fl_th, "{mn}")
    $ Fl.say(Fl_gg, "На шахматы.")

    hide ba smile uniform with Fl_fast

    $ Fl.say(Fl_r, "Ответил я сарказмом и скрылся из спортзала, оставив этого бугая позади.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(3)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(2.5)

    $ Fl.PlayAmbience("Fl_soccer_play_background", 1, 4)
    scene bg Fl_ext_playground_day 
    show Fl_light_c
    with Fl_dissolve2

    $ Fl.Pause(1.0)

    $ Fl.Save("День2: Приключение с Михалычем и Толентием.")
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Вернувшись на поле, я заметил двух турникменов: {w}Михана, который пытался подтянуться. И Толяна, который просто висел, как сопля на перекладине.")
    $ Fl.say(Fl_r, "Стоило мне подойти поближе, как Михан сразу же отлип от турникета и подошёл ко мне.")

    show msk smile shirt with Fl_fast:
        right

    $ Fl.say(Fl_msk, "Ну чё как прошло?")
    $ Fl.say(Fl_gg, "Да я задолбался искать физрука в этой конуре. А так нормально, подпись поставил.")
    $ Fl.say(Fl_msk, "Хорош!")
    $ Fl.say(Fl_gg, "Слушай, а что ты такого натворил, что физрука теперь боишься?")

    show msk serious shirt with Fl_fast

    $ Fl.say(Fl_msk, "А ты об этом...")

    $ Fl.Pause(1.5)

    show msk happy shirt with Fl_fast

    $ Fl.say(Fl_msk, "Кароч футбол играли. {w}Ну и я взял и <п*зданул> по мячу со всей силы, а он прямо в окно залетел физруку.")
    $ Fl.say(Fl_msk, "Ну а этот шкаф <бл*ть> погнался за мной.")
    $ Fl.say(Fl_gg, "И много у тебя таких инцидентов?")

    show msk evilsmile shirt with Fl_fast

    $ Fl.say(Fl_msk, "Ты даже не представляешь сколько!")
    $ Fl.say(Fl_r, "На лице Михе появилась злобная ухмылка, которая говорила всё за него.")

    show msk smile shirt with Fl_fast

    $ Fl.say(Fl_msk, "Ладно харэ лясы точить, погнали в кружок изо и чё то там ещё. А то обед не за горами!")
    $ Fl.say(Fl_r, "Я согласился. Потратить весь день на заполнение обходного не было ни малейшего желания. Хотелось уже быстрее с ним покончить и снять с себя оковы в виде обязаловки.")

    hide msk smile shirt with Fl_fast

    $ Fl.say(Fl_r, "Мы поспешили покинуть футбольное поле и орущих пионеров. Ну и конечно про Толяна мы не забыли, который до сих пор виснул на перекладине. {w}И как только у него руки не отвалились столько висеть, с его то весом...")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(3)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(3.0)

    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 4)
    scene bg Fl_ext_artroom_day
    show Fl_light_c
    with Fl_dissolve2

    $ Fl.Pause(1.0)

    $ Fl.Save("День2: Приучаем парней к творчеству.")
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "И вот мы оказались на месте. Если верить Михе, то сейчас перед нами стоит здание где пионеры создают исскуство.")
    $ Fl.say(Fl_r, "Снаружи здание имело сходство с музкружок. Главное отличие заключалось разве что в размере веранды. {w}Даже освещение было обделенно единственным фонарём, который стоял у пуской доски объявлений. И так же разположение где-то у входа в хвойную часть леса.")
    $ Fl.say(Fl_r, "Не став заострять внимание на картине перед глазами, мы с парнями зашли внутрь.")
    $ Fl.HideScreens(_with=Fl_fast)
    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
    scene bg Fl_black with Fl_effect_2


    $ Fl.Pause(2.5)

    scene bg Fl_int_editorial_day with Fl_effect_2

    $ Fl.Pause(1.0)

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "В помещении стояла мёртвая тишина. Мои ожидания увидеть большое количество людей не оправдались. Кроме Юрия Гагарина, мне не удалось найти кого-то.")
    $ Fl.say(Fl_r, "Я повернул голову в сторону столика на котором лежали друг на дружке какие-то записи.")
    $ Fl.say(Fl_r, "Подул лёгкий ветерок, открыв крошечную долю содержимого листов. {w}Это были своего рода черновики, перечёркнутый небрежно текст тому доказательство.")
    $ Fl.say(Fl_r, "Дальше что сильно бросалось в глаза, это стеллаж книг с короткими произведениями и сборником поэзии.")
    $ Fl.say(Fl_r, "В правом углу комнаты находился календарь.")

    $ Fl.PlaySound("Fl_walk2", 1, 0, False)
    scene bg Fl_int_editorial_day:
        ease 2.5 zoom 2.6 xalign 1.0 yalign 0.25

    $ Fl.say(Fl_r, "Я подошёл поближе чтобы посмотреть какое сегодня число и год.")


    $ Fl.Pause(1.5)

    $ Fl.say(Fl_th, "13 июля 1987 год.", cps="25")

    $ Fl.PlaySound("Fl_walk2", 1, 0, False)
    scene bg Fl_int_editorial_day at Fl_bg_zoom_otd(2.6, 1.0, 2.5, 1.0, 0.5, 0.25, 0.5)
    $ Fl.Pause(2.5)

    $ Fl.say(Fl_th, "Значит мой телефон действительно показывает дату и время этого места.")
    $ Fl.say(Fl_r, "Одной проблемой стало меньше, теперь я могу точно определить число и время. {w}Я вздохнул с облегчением.")
    $ Fl.say(Fl_r, "Год меня нисколечки не пугал. {w}Я умер и переродился это факт. В фентези мирах тоже был другой год и главного героя мало это заботило. Поэтому я поступлю как масса и просто приму к сведению.")
    $ Fl.say(Fl_r, "Только я заприметил мальберт, как в здание кто-то зашёл.")

    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)

    $ Fl.Pause(1.5)
    show mir normal pioner3 with Fl_dissolve1
    $ Fl.Pause(1.0)
    show mir surprise2 pioner3 with vpunch

    $ Fl.PlayMusic("Fl_doramami", 1, 4)
    $ Fl.say(Fl_mirk, "Ой!")
    $ Fl.say(Fl_r, "Возле двери появилась уже знакомая мне пионерка с пепельными волосами(правда имя которой я до сих пор не знаю).")

    show mir shy pioner3 with Fl_fast

    $ Fl.say(Fl_mirk, "Простите, я отошла по делам, не думала что кто-то зайдёт.")
    $ Fl.say(Fl_r, "Смущенно сказала пионерка, изображая виноватый вид.")
    $ Fl.say(Fl_gg, "Да ничего страшного.")

    $ Fl.Master(Fl_bg_zoom_th(1.0, 1.34, 1.5, 0.5, 0.27, 0.5, 0.4))
    $ Fl.say(Fl_r, "Я бросил внимание на двух охламонов, который чем-то занимались в конце стелажа.")

    show mir happiness pioner2 with Fl_fast

    $ Fl.say(Fl_mirk, "Ну так может скажешь, зачем пришёл?")
    $ Fl.say(Fl_r, "Мелодичный голос девушки заставил меня вновь переключиться на неё.")

    $ Fl.Master(Fl_bg_zoom_otd(1.34, 1.0, 1.5, 0.27, 0.5, 0.4, 0.5))
    $ Fl.Pause(1.5)

    $ Fl.say(Fl_gg, "Д-да прости. Мне бы вот обходной подписать.")

    show mir surprise pioner2 with Fl_fast

    $ Fl.say(Fl_mirk, "Ясно. Давай сюда.")
    $ Fl.say(Fl_r, "Пионерка тяжело вздохнула, явно ожидая от меня иного ответа.")
    $ Fl.say(Fl_r, "Без всякого энтузиазма она поставила подпись и отдала обходной мне.")
    $ Fl.say(Fl_gg, "Слушай, а почему здесь никого нет? Неужели никто не втупил в твой клуб?")

    show mir smile pioner3 with Fl_fast

    $ Fl.say(Fl_mirk, "С чего ты так решил?")
    $ Fl.say(Fl_r, "Я повертел головой рассматривая каждый угол, показывая тем самым пионерки почему я так решил.")

    show mir happiness pioner2 with Fl_fast

    $ Fl.PlaySound("Fl_smeh_kt", 1, 0, False)
    $ Fl.say(Fl_mirk, "Хахаха, понятно.")

    show mir smile pioner3 with Fl_fast

    $ Fl.say(Fl_mirk, "Ну ты ошибаешься, в клубе состоит пять человек. Просто они из второго отряда и у них сейчас пляжный день, вот!")
    $ Fl.say(Fl_gg, "Понятно...")

    show mir happiness pioner2 with Fl_fast

    $ Fl.say(Fl_mirk, "Кстати, может представишься, а то мне как-то некомфортно избегать обращений в речи?")
    $ Fl.say(Fl_th, "Точно, мы ведь до сих пор не знаем имён друг друга.")
    $ Fl.say(Fl_gg, "Ян, а тебя?")

    show mir smile pioner3 with Fl_fast

    $ Fl.say(Fl_mir, "Мира. Полное имя Мирослава, но можно просто Мира!")
    $ Fl.say(Fl_gg, "Необычное имя... Довольно редко такое встретишь.")
    $ Fl.say(Fl_mir, "Твоё тоже!")

    show mir shy pioner3 with Fl_fast

    $ Fl.say(Fl_mir, "Ян, а ты случайно не рисуешь? Или может писатель начинающий?")
    $ Fl.say(Fl_gg, "И то и другое, а почему спрашиваешь?")
    $ Fl.say(Fl_mir, "Ну как бы{mn} {w}Не хочешь вступить к нам в клуб?")
    $ Fl.say(Fl_r, "Пионерка почему-то спросила это довольно тихо и всячески старалась избежать зрительного контакта.")
    $ Fl.say(Fl_gg, "Прости, но меня уже в музклуб загребли. Второй кружок я точно не осилю...")
    $ Fl.say(Fl_th, "Правда я туда по своей воле вступил, но чтобы не обидеть Миру мне пришлось приврать.")

    show mir embarrassment pioner3 with Fl_fast

    $ Fl.say(Fl_mir, "Понятно...", cps="28")
    $ Fl.say(Fl_r, "Мира постаралась натянуть улыбку, но её глаза говорили сами за себя.")
    $ Fl.say(Fl_r, "Не зря ведь говорят, что глаза это отражение нашей души. {w}Интересно что мой пустой взгляд говорит обо мне...")
    $ Fl.say(Fl_r, "После смерти моей подруги, которой даже имени не знаю, моя мимика полностью изменилась.")
    if persistent.Fl_dictionary_3 == False:
        $ Fl.PodskDict()
    $ persistent.Fl_dictionary_3 = True
    $ Fl.say(Fl_r, "Проблема схожая частично на {i}алекситимию{/i}. {w}Чтобы передать свои настоящие эмоции мне приходиться напрягаться. Конечно бывают и исключения, когда эмоции как-то на автомате проскакивают на лице, но такое происходит довольно редко.")
    
    $ Fl.Pause(2.0)

    $ Fl.say(Fl_r, "Но годы идут, и старые раны проходят, взамен пустоте во мне зародилась злоба. Я прогнил, как большинство в современном обществе, а всё ради чего? {w}Чтобы выжить и не быть использованным, как старая детская игрушка.")
    $ Fl.say(Fl_r, "Гнев и злость - послужили мне реабилитацией в моей проблеме с мимикой. Жаль что именно эти эмоции закрыли мою пустоту в сердце...")
    $ Fl.say(Fl_gg, "Если у меня когда-нибудь появится свободное время ты же не будешь против, если я зайду к вам в гости?")

    show mir smile pioner3 with Fl_fast

    $ Fl.say(Fl_mir, "Конечно, нет! Таким, как ты, тут всегда будут рады!")
    $ Fl.say(Fl_r, "В глазах Миры заискрился огонёк. Видно мои слова подняли настроение ей, и это радовало!")

    show mir gnev pioner3 with Fl_fast

    $ Fl.say(Fl_mir, "Эй, вы! Вы что там делаете?!", _with=hpunch)
    $ Fl.say(Fl_r, "Неожиданно Мира повысила тон.")
    $ Fl.say(Fl_r, "Её слова были направлены на двух пионеров, которые стояли рядом с мольбертом.")
    $ Fl.say(Fl_r, "В руках Толика находилась кисточка. Он что-то начал усердно выводить в нижнем правом углу холста.")
    $ Fl.say(Fl_r, "Кружок... {w}Ещё один кружок... {w}И посередине... {w}овал...", cps="27")
    $ Fl.say(Fl_mir, "Что вы там рис{break}")

    show mir shock pioner3 with vpunch
    $ Fl.Pause(1.0)
    show mir gnev pioner3 with vpunch

    $ Fl.say(Fl_mir, "ВЫ ЧТО НАДЕЛАЛИ, {b}ДВА ИДИОТА{/b}!", _with=hpunch)
    $ Fl.say(Fl_th, "Да было не трудно догадаться, что именно нарисовал Толик.")

    $ Fl.PlaySound("Fl_msk_laugh", 1, 0, False)
    $ Fl.say(Fl_msk, "Толян, да у тебя талант. {w}Правда художник с тебя <х*ёвый>! ХАХАХАХА!")
    $ Fl.say(Fl_r, "На это заявление Толян лишь гордо поднял голову и радовался своему шедевру. То что этому контуженному пришло в голову нарисовать мужскую гениталию меня нисколечки не удивило.")

    show mir normal pioner3 with Fl_fast

    $ Fl.say(Fl_r, "Мира с серьёзным лицом повернулась ко мне.")
    $ Fl.say(Fl_r, "Почему-то от её взгляда я резко почувствовал себя виноватым. Ведь этих «Двух идиотов» привёл именно я.")
    $ Fl.say(Fl_r, "Я виновато пожал плечами и решил быстро разрулить данную ситуацию.")
    $ Fl.say(Fl_gg, "Так, пацаны, всё хватит дурью маяться! Пошли отсюда, подпись я уже получил.")
    $ Fl.say(Fl_th, "Да, я ничего лучше не придумал, кроме как слинять и не раздражать Миру тупыми выходками слабоумного товарища.")
    $ Fl.say(Fl_r, "Кое-как мне удалось их выпроводить на улицу. Строгий взгляд Миры сильно давил на меня, поэтому я старался всё сделать как можно быстрее.")

    $ Fl.Pause(1.0)

    $ Fl.say(Fl_gg, "Мира...")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    menu:
        "Промолчать":
            $ Fl.ShowScreens(_with=Fl_dissolve1)
            $ Fl.say(Fl_gg, "Ну мы пойдём. Было приятно поболтать с тобой.")

            hide mir normal pioner3 with Fl_dissolve1

            $ Fl.say(Fl_r, "В качестве ответа я получил:«Ага». После чего Мира ушла рассматривать испорченный холст.")
            $ Fl.say(Fl_r, "Я вышел из здания.")
            $ Fl.HideScreens(_with=Fl_dissolve1)


        "Извиниться":
            $ Fl.ShowScreens(_with=Fl_dissolve1)
            $ Fl.say(Fl_gg, "Ты уж прости этих двоих. Они просто...")
            $ Fl.say(Fl_mir, "Тебе та за что извиняться?")
            $ Fl.say(Fl_th, "Действительно. {w}Вроде бы за Толяном должен опекун его следить и извиняться сейчас должен тоже именно он, а не я...")
            $ Fl.say(Fl_gg, "Ну я же этих двоих притащил сюда.")

            show mir smile pioner3 with Fl_fast

            $ Fl.say(Fl_mir, "Решил принять удар на себя?")
            $ Fl.say(Fl_gg, "Нет... {w}То есть, да...")

            show mir happiness pioner2 with Fl_fast

            $ Fl.say(Fl_mir, "Не думала, что ты у нас такой взрослый.")
            $ Fl.say(Fl_gg, "И как ты к такому выводу пришла?")

            show mir smile pioner3 with Fl_fast

            $ Fl.say(Fl_mir, "Только взрослый может взять чью-то вину на себя, разве нет?")
            $ Fl.say(Fl_mir, "Он не только вправе нести отвественность за свои поступки, но и может нести отвественность и за чужие.")
            $ Fl.say(Fl_gg, "Или может я просто дурак, который ищет себе проблем...")
            $ Fl.say(Fl_mir, "Может быть, но я так не думаю!")
            $ Fl.say(Fl_r, "Былой гнев девушки куда-то испарился, а значит это можно принять за то, что она нас простила. Наверное...")
            $ Fl.say(Fl_mir, "От этих двоих я другого и не ожидала. Один у нас с приветом, а другой авантюрист с маленьким словарным запасом, вечно ему не сидится на месте!")
            $ Fl.say(Fl_th, "Вот какого она мнения о этих двоих. {w}Ну в принципе она права, характеристики им идеально подходят. Хоть я с Миханом мало знаком, но уже могу сделать такие же выводы про него, как эта пионерка.")
            $ Fl.say(Fl_r, "Я бы мог ещё обсудить с Мирой, что она считает о моих новых знакомых... Но парни ждать не будут, да и впервую очередь нужно все подписи собрать, а потом уже можно и болтать с кем угодно!")
            $ Fl.say(Fl_gg, "Ну я пойду, мне ещё обходной нужно дальше заполнять. И ещё раз прости, что так вышло.")
            $ Fl.say(Fl_mir, "Угу. Заходи как-нибудь, мы всегда будем тебе рады!")
            $ Fl.say(Fl_r, "Я кивнул на последок и направился к двери.")
            $ Fl.HideScreens(_with=Fl_dissolve1)


            $ Obs_mi += 1



    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
    $ Fl.StopMusic(3)
    scene bg Fl_black with Fl_dissolve1

    $ Fl.Pause(2.0)

    scene bg Fl_ext_artroom_day
    show Fl_light_c
    with Fl_dissolve2

    $ Fl.Pause(1.0)

    $ Fl.Save("День2: Приключение с Михалычем и Толентием.")
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "И вот я оказался снаружи. Виновники торжества стояли и тупо ходили кругами.")

    if Obs_mi == 1:
        show msk serious shirt with Fl_fast

        $ Fl.say(Fl_msk, "Ну наконец-то и полгода не прошло, чё так долго?")
        $ Fl.say(Fl_gg, "Да пришлось извиняться за выходку Толяна.")

        show msk smile shirt with Fl_fast

        $ Fl.say(Fl_msk, "Понятно, ну и как прошло?")
        $ Fl.say(Fl_gg, "Нормально, вроде бы она не в обиде.")

        show msk grin shirt with Fl_fast

        $ Fl.say(Fl_msk, "Ясн, тогда всё чики-пуки!")
        $ Fl.say(Fl_th, "Я значит за них расхлёбываюсь, а у них всё «чики-пуки»...")

        show msk smile shirt with Fl_fast

        $ Fl.say(Fl_msk, "Лан, чё стоим погнали в библиотеку.")
        $ Fl.say(Fl_gg, "Ну погнали.")
        $ Fl.say(Fl_msk, "Шагом марш, <бл*>!")


    else:
        $ Fl.say(Fl_r, "Заметив меня, Михан быстро подошёл ко мне.")

        show msk smile shirt with Fl_dissolve1

        $ Fl.say(Fl_msk, "Ну что Янчик, погнали в библиотеку? Храм знаний, так сказать.")
        $ Fl.say(Fl_r, "Я повернул голову назад, где находилось здание творческого кружка. В окне было видно, как Мира что-то делала, стоя у мольберта.")
        $ Fl.say(Fl_th, "Может нужно было хотя бы извиниться, а то не красиво как-то вышло...")

        show msk sad shirt with Fl_fast

        $ Fl.say(Fl_msk, "Алё, Ян, ты меня слушаешь?")
        $ Fl.say(Fl_r, "Мои размышления прервал мужской басс.")
        $ Fl.say(Fl_gg, "Да слышу я! Бери Толяна и пошли в библиотеку.")

        show msk smile shirt with Fl_fast

        $ Fl.say(Fl_msk, "Тогда, шагом марш, <бл*>!")


    $ Fl.say(Fl_r, "Повторил уже в который раз за день Михан одно и тоже предложение, после чего мы отправились в путь.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(2.5)

    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 4)
    scene bg Fl_ext_library_day
    show Fl_light_c
    with Fl_dissolve2

    $ Fl.Pause(1.0)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Храм знаний в пионерлагере представлял из себя коробку прямоугольной формы. В каждой стене было по три окна, а недалеко со входом находился умывалник.")
    $ Fl.say(Fl_r, "Рядом располагалось ещё какое-то здание, которое больше напоминало маленький склад.")
    $ Fl.say(Fl_r, "Сама же библиотека расположилась недалеко от входа в лес.")
    $ Fl.say(Fl_th, "В принципе типичная библиотека. У меня возле дома такая же была.")
    $ Fl.HideScreens(_with=Fl_fast)
    $ Fl.PlaySound("Fl_open_door_2", 1.0, 0, False)
    scene bg Fl_black with Fl_effect_4


    $ Fl.Pause(2.5)

    scene bg Fl_int_library_day with Fl_effect_4

    $ Fl.Pause(1.0)

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "Мы зашли, и я сразу начал всё изучать.")
    
    $ Fl.PlayMusic("Fl_your_bright_side", 1, 2)

    $ Fl.say(Fl_th, "Ну вроде библиотека, как библиотека...")
    $ Fl.say(Fl_th, "Хорошая, приятная атмосфера времён СССР, уютно, просторно. Удивительно, но нигде даже ни пылинки, ну и чистота. Правда душновато здесь немного, но тому причина наглухо закрытые окна. {w}А так вроде бы всё.")
    
    scene bg Fl_int_library_day:
        linear 2.0 zoom 2.0 xalign 0.0 yalign 0.4
    $ Fl.Pause(2.0)

    $ Fl.say(Fl_th, "Слава Советскому Союзу! За родину! За сталина! За мир! За коммунизм!")
    $ Fl.say(Fl_th, "Эх, где ж ты, Советский Союз?")

    show Fl_fogging with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Сдал Горабачёв твою родину американцам, чтоб тусоваться красиво!")
    if persistent.Fl_dictionary_4 == False:
        $ Fl.PodskDict()
    $ persistent.Fl_dictionary_4 = True
    $ Fl.say(Fl_r, "Процитировал голос финал песни известной рок-группы «{i}Пф{/i} - Родина Зовёт».")
    $ Fl.say(Fl_th, "Ага...")
    $ Fl.say(Fl_th, "Интересно, могло бы что-то сложиться иначе, был бы реально настоящий коммунизм?")
    $ Fl.say(Fl_kvl, "Слушай, Сударь. Скажу прямо.")
    $ Fl.say(Fl_r, "Вдруг заговорил внутренний голос.")
    $ Fl.say(Fl_kvl, "Тогда бы всё было также. Нашёлся бы ещё какой-нибудь президент, и всё, коммунизму конец. Да и люди...")
    $ Fl.say(Fl_th, "Знаю! Люди, какими были моральными уродами, такими бы и остались. {w}Коммунизм никак не смог бы избавить этот мир от бессердечных людей.")
    $ Fl.say(Fl_kvl, "Да это я и хотел сказать.")
    hide Fl_fogging with Fl_dissolve1

    scene bg Fl_int_library_day:
        zoom 2.0 xalign 0.0 yalign 0.4
        linear 1.0 zoom 3.0 xalign 0.37 yalign 0.5
    $ Fl.Pause(1.0)

    $ Fl.say(Fl_th, "А вот и сам бюст Ленина. {w}Ни пылинки даже.")

    scene bg Fl_int_library_day:
        zoom 3.0 xalign 0.37 yalign 0.5
        linear 1.0 zoom 3.0 xalign 0.6 yalign 0.5
    $ Fl.Pause(1.0)

    $ Fl.say(Fl_th, "Ну, и всякие плакаты. На этом можно закончить рум-тур.")
    $ Fl.HideScreens(_with=Fl_fast)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause(1.5)
    scene bg Fl_int_library_day with Fl_dissolve1
    show msk smile shirt with Fl_dissolve1

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_msk, "Чёт тихо как-то.")
    $ Fl.say(Fl_gg, "Ясное дело, что тихо. Библиотека, как никак.")

    show msk evilsmile shirt with Fl_fast

    $ Fl.say(Fl_msk, "Да не, я, в смысле, никакого храпа не слышно.")
    $ Fl.say(Fl_gg, "Храпа?")
    $ Fl.say(Fl_r, "Миха глазами указал в глубь библиотеки, где мирно посапывала тёмноволосая пионерка в очках.")

    show msk smile shirt with Fl_fast

    $ Fl.say(Fl_msk, "Так, лан возьми у неё печать, она на самом краю стола стоит, и поставь в графе «подпись».")
    $ Fl.say(Fl_gg, "Всмысле печать?")
    $ Fl.say(Fl_msk, "В прямом. Вместо росписи здесь ставится печать.")
    $ Fl.say(Fl_gg, "А, понял.")
    $ Fl.say(Fl_msk, "Правда, я тогда об этом не знал и вожатка спалила, что я все подписи подделал...")
    $ Fl.say(Fl_gg, "Тебе даже лень было обходной заполнить?")
    $ Fl.say(Fl_msk, "Да <нах*й> оно надо. Я чё ботан, чтобы с листочками бегать, пока в лагере столько красоток!")

    show Fl_fogging with Fl_dissolve1
    $ Fl.say(Fl_kvl, "От кого-то я уже это слышал...")
    $ Fl.say(Fl_th, "Ну так Михан дело говорит!")
    hide Fl_fogging with Fl_dissolve1

    hide msk smile shirt with Fl_fast

    $ Fl.say(Fl_r, "Я подошёл к столу и взял печать, после чего использовал её по назначению и поставил на место. {w}Разрешение конечно никто не стал спрашивать.")

    show msk evilsmile shirt with Fl_fast

    $ Fl.say(Fl_msk, "А теперь...")
    $ Fl.StopMusic(2)
    $ Fl.HideScreens(_with=Fl_fast)

    $ Fl.Pause(2.0)
    $ Fl.PlayMusic("Fl_that_man", 1, 2)

    show msk evilsmile shirt:
        subpixel True
        linear 4.0 xpos 0.8 
    $ Fl.Pause(3.0)

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "И вот Миха тихо к ней подходит на цыпочках с очень весёлой ухмылкой. {w}Явно что-то задумал.")
    $ Fl.say(Fl_r, "Прям-таки улыбается-улыбается.")
    $ Fl.HideScreens(_with=Fl_fast)


    show msk evilsmile shirt:
        subpixel True
        linear 4.0 xpos 0.2
    $ Fl.Pause(3.0)

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "И вот он уже дошёл до её рабочего места.")
    $ Fl.HideScreens(_with=Fl_fast)


    scene bg Fl_black with Fl_effect_left1
    $ Fl.Pause(0.5)

    $ persistent.Fl_photo_pallery_6 = True
    scene cg Fl_micu_lib with Fl_effect_right1

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "А библиотекарша тем временем тихонько сопела, неподозревая, что произойдёт дальше.")

    scene cg Fl_micu_lib:
        subpixel True
        zoom 1.0 xalign 0.5 yalign 0.5
        linear 2.0 zoom 2.0 xalign 0.5 yalign 0.5

    $ Fl.say(Fl_r, "Миха, медленно подносит свои губы к её уху.")
    $ Fl.say(Fl_r, "И улыбается самой хитрой улыбкой.")
    $ Fl.say(Fl_r, "А потом медленно...")
    
    $ Fl.StopMusic(4)

    $ Fl.say(Fl_r, "Спокойно... {w}Осторожно...")
    
    $ Fl.PlaySound("Fl_attack", 1, 0, False)
    $ Fl.say(Fl_r, "КАК ГАРКНЕТ!")
    $ Fl.HideScreens()

    scene cg Fl_micu_lib:
        subpixel True
        xalign 0.55 yalign 0.45 zoom 1.25
        linear 2.0 zoom 1.0 xalign 0.45 yalign 0.55
    $ Fl.Master(Fl_shake(10, 2.3))

    $ Fl.PlaySound("Fl_attack", 1, 0, False)
    $ Fl.say(Fl_msk, "РОТА ПОДЪЁМ, <БЛ*>!!!{break2}", _with=hpunch)
    $ Fl.HideScreens()


    scene bg Fl_black with Fl_effect_left1
    $ Fl.Pause(0.5)
    scene bg Fl_int_library_day with Fl_effect_right1

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_msk, "Янчик, прячься!", _with=hpunch)

    $ Fl.Status("-20")
    $ Fl.say(Fl_gg, "Чего? Всмысле? Куда?")
    $ Fl.say(Fl_r, "От неожиданности начал я засыпать вопросами Миху. На что он только схватил меня за шиворот футболки и потащил к стелажу.")

    scene bg Fl_int_library_day:
        ease 1.0 zoom 1.7 yalign 0.4 xalign 0.8

    $ Fl.Pause(1.0)
    $ Fl.PlayMusic("Fl_revenga", 1, 3)
    show mz angry pioner2 with Fl_dissolve1:
        fleft

    $ Fl.say(Fl_mzp, "КТО ЭТО СЕЙЧАС СДЕЛАЛ?!", _with=hpunch)

    show mz rage pioner2 with Fl_fast

    $ Fl.say(Fl_mzp, "СПРЯТАЛСЯ ЗНАЧИТ! А НУ ВЫХОДИ, Я ТЕБЯ ВИЖУ!!!", _with=hpunch)
    $ Fl.say(Fl_gg, "Поздравляю вы пробудили зло!")

    $ persistent.Fl_dostn_7 = True
    show Fl_dost_7_in_kod:
        xalign -1.0 yalign 0.7
    show Fl_dost_7_in_kod:
        ease 1.0 xalign 0.01
    $ Fl.Pause(0.5)
    $ Fl.PlaySound("Fl_achievement", 1, 0, False)
    $ Fl.Pause(1.5)
    hide Fl_dost_7_in_kod with dissolve
    
    $ Fl.say(Fl_r, "Шёпотом сказал я Михану. Теперь он казалось расстянул свою улыбку от уха до уха. Он явно ожидал чего-то такого и теперь радуется, пока за книжными полками хищным взглядом нас ищет библиотекарша.")
    $ Fl.say(Fl_mzp, "ТОЛЯ, А НУ ЖИВО ВЫЛАЗЬ, Я ТЕБЯ ВИЖУ!", _with=hpunch)
    $ Fl.say(Fl_r, "И только сейчас я вспомнил про Толика, который по всей видимости решил спрятаться вместе с нами, но он выбрал не лучшую позицю для засады. Может лицо флаг и смог скрыть, вот только ноги всё ещё беззащитны.")

    hide mz rage pioner2 with Fl_fast

    $ Fl.say(Fl_r, "Быстрым шагом, черноволосая пионерка сократила дистанцию и начала лупить Толика книжкой.")
    $ Fl.say(Fl_th, "Ну может хоть так Толику можно вбить какие-то знания.")
    $ Fl.say(Fl_msk, "Так теперь по-тихому сваливаем отсюда.")
    $ Fl.say(Fl_r, "И попытались по стелсу вылезти из нашего укрытия и добраться до выхода, но хищник в очках почуял движение за спиной и резко обернулся.")
    $ Fl.say(Fl_mzp, "А НУ СТОЯТЬ!!!", _with=hpunch)
    $ Fl.say(Fl_msk, "ВАЛИМ!", _with=hpunch)
    $ Fl.HideScreens()

    scene bg Fl_int_library_day at Fl_bg_zoom_otd(1.7, 1.0, 1.0, 0.8, 0.5, 0.4, 0.5)

    $ Fl.Pause(1.0)
    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)

    scene bg Fl_ext_library_day
    show Fl_light_c
    with vpunch

    $ Fl.ShowScreens()
    $ Fl.say(Fl_r, "Стоило нам только закрыть дверь, как в нашу сторону что полетело, скорее всего эта была та самая книжка, которой она лупила Толика.")
    $ Fl.say(Fl_r, "Отбежав на добрых сотню метров, мы решили немного отдышаться.")
    $ Fl.StopMusic(3)
    $ Fl.HideScreens(_with=Fl_dissolve1)

    $ Fl.Pause(2.5)
    $ Fl.Status("+10")
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.AutoSave()
    $ Fl.say(Fl_gg, "Да уж, больше я в библиотеку ни ногой.")

    show msk grin shirt with Fl_fast

    $ Fl.say(Fl_msk, "Понравилось?")
    $ Fl.say(Fl_gg, "Какой <бл*ть> понравилось, Миха? Она нас чуть не сожрала там!", _with=hpunch)

    show msk happy shirt with Fl_fast

    $ Fl.say(Fl_msk, "Так в этом весь и прикол, чел! Ты видел, как она взбесилась, как бешенный зверь, ё-моё!")
    $ Fl.say(Fl_gg, "Миха, а ты можешь уже как-то без своих приколов меня довести куда-то?")

    show msk smile shirt with Fl_fast

    $ Fl.say(Fl_msk, "Не, я же бог приколов! Без них я погибну!")
    $ Fl.say(Fl_th, "Скорее я погибну. {w}Я за это утро столько пережил, а этот придурок мне ещё проблем накидывает.")
    $ Fl.say(Fl_msk, "Лан, погнали в медпункт.")
    $ Fl.say(Fl_gg, "А Толяна спасать не будем?")

    show msk serious shirt with Fl_fast

    $ Fl.say(Fl_msk, "Толян...")
    $ Fl.say(Fl_r, "Миха посмотрел в сторону библиотеки и застыл.")

    $ Fl.Pause(3.0)

    show msk evilsmile shirt with Fl_fast

    $ Fl.say(Fl_msk, "Толян, земля тебе пухом!")
    $ Fl.say(Fl_gg, "{mn}")

    $ persistent.Fl_dostn_8 = True
    show Fl_dost_8_in_kod:
        xalign -1.0 yalign 0.7
    show Fl_dost_8_in_kod:
        ease 1.0 xalign 0.01
    $ Fl.Pause(0.5)
    $ Fl.PlaySound("Fl_achievement", 1, 0, False)
    $ Fl.Pause(1.5)
    hide Fl_dost_8_in_kod with dissolve

    $ Fl.say(Fl_th, "Ну что я ещё ожидал услышать от недопетросяна?")
    $ Fl.say(Fl_th, "Хотя по правде говоря, у меня самого нет желания идти и бороться с четырёхглазым монстром.")
    $ Fl.say(Fl_gg, "Ладно, пошли.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(2.5)

    scene bg Fl_ext_aidpost_day
    show Fl_light_c
    with Fl_dissolve2

    $ Fl.Pause(1.0)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_gg, "Мих, а разве это не здание творческого кружка?")
    $ Fl.say(Fl_msk, "Не, оно просто похоже. Посмотри наверх.")
    $ Fl.say(Fl_r, "Я поднял голову вверх и заметил главное отличие двух одинаковых зданий. На флаге был изображён красный, медицинский крест. {w}Но если бы не это маленькое отличие, то я бы точно будь один пропустил это место и провозился за поисками до самого вечера.")
    
    $ Fl.Pause(2.0)
    
    $ Fl.say(Fl_r, "Если так подумать, я никогда особо не заботился о своем здоровье. В детстве я побаивался врачей, в основном из-за уколов.")
    $ Fl.say(Fl_r, "Помню, как-то раз мама повела меня в поликлинику, обещая, что врач меня «только посмотрит». {w}Но, не тут-то было. Мне не просто устроили медосмотр, но и взяли у меня анализ крови и сделали укол в плечо.")
    $ Fl.say(Fl_r, "Ох и как же я дулся тогда! Мама даже купила мне игрушку, чтобы как-то меня задобрить. А я обиделся на нее и не говорил целый день. {w}Потом ещё начал тарелкой с едой кидаться, но подробности упустим...")
    $ Fl.say(Fl_th, "Да, нелегко, наверное, со мною было{mn} {w}Я ещё той истеричкой был...")
    $ Fl.say(Fl_r, "Ну а потом мне просто не нравилось торчать с пенсионерами в очередях. Я ненавидел поликлиники, по многим причинам. {w}К тому же после последнего переезда мне нужно было прикрепиться к новой поликлинике по месту жительства.")
    $ Fl.say(Fl_r, "Правда, поликлиника это ещё цветочки по сравнению с медкомиссией военкомата!")
    $ Fl.say(Fl_r, "Я с рождения родился долбанным колекой, с вечным бронхитом, мигренями и т.д. Перечислять долго, да и не вижу смысла. {w}Но добрые врачи из военкома закрыли на всё глаза, поставив категорию «А».")
    $ Fl.say(Fl_r, "Вот только мой шрам на запясьте подарил мне возможность откосить от одного года тюрьмы. Да и после этого шрама всплыл мой диагноз, который я лечил со своим терапевтом.")
    $ Fl.say(Fl_th, "Думали с меня что-то поиметь, а в итоге поимел их я!")
    
    $ Fl.Pause(2.0)
    
    $ Fl.say(Fl_r, "Оторвавшись от воспоминаний, я вернулся в реальность. Мне следовало получить заветную подпись. А заполнив этот долбаный клочёк бумажки, я смогу заниматься своими делами.")
    $ Fl.say(Fl_r, "Вытащив сложенный вчетверо обходной лист, который я положил в карман. Я подошел к двери и хотел было постучаться, как заметил, что Михан стоит на том же месте и ухмыляется.")
    $ Fl.say(Fl_gg, "Ты идёшь или как?")

    show msk smile shirt with Fl_fast:
        fleft

    $ Fl.say(Fl_msk, "Да, я тут постою.")

    show msk grin shirt with Fl_fast

    $ Fl.say(Fl_r, "Ответил он и натянул ещё сильнее ухмылку.")
    $ Fl.say(Fl_th, "Что-то тут не чисто...")
    $ Fl.say(Fl_gg, "Давай колись, что на этот раз ты натворил.")
    $ Fl.say(Fl_msk, "Ничего...")
    $ Fl.say(Fl_gg, "А что ржёшь тогда?")

    show msk happy shirt with Fl_fast

    $ Fl.say(Fl_msk, "Да просто...")
    $ Fl.say(Fl_msk, "А лан сам всё узнаешь, ты если что кричи я тебя спасу.")
    $ Fl.say(Fl_th, "Ничего не понял, но очень интересно.")

    hide msk happy shirt with Fl_fast

    $ Fl.say(Fl_r, "Нестав зацикливаться на приколах недопетросяна, я постучался.")

    $ Fl.PlaySound ("Fl_door_knock", 1, 0, False)
    $ Fl.Pause(2.5)

    $ Fl.say(Fl_csk, "Входите, открыто!")
    $ Fl.say(Fl_r, "Послышался женский голос изнутри. Я послушно потянул дверь на себя и шагнул внутрь.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.PlaySound("Fl_open_door_2", 1.0, 0, False)


    scene bg Fl_int_aidpost_day with Fl_flash

    $ Fl.Pause(1.5)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Дверь за мной закрылась. Я же окинул оценивающим взглядом новое для себя место. Здесь царили идеальная чистота и порядок. Я обратил внимание на две кушетки, одна из которых даже была с ширмой, которую можно было закрыть в случае надобности.")
    $ Fl.say(Fl_r, "Еще здесь был шкафчик с прозрачными стеклянными дверцами, внутри которых виднелись различного рода склянки и коробочки с препаратами. Впрочем, самое необходимое, скорее всего, хранилось у медсестры в ящиках стоявшего у окна стола.")
    $ Fl.say(Fl_r, "Пробежавшись взглядом по помещению еще раз, я заметил весы и интересную таблицу для проверки зрения.")
    $ Fl.say(Fl_th, "Ну-с проверим зрение.")

    scene bg Fl_int_aidpost_day:
        zoom 1.0 xalign 1.0 yalign 0.3
        linear 3.0 zoom 3.0 xalign 1.0 yalign 0.3

    $ Fl.Pause(5.0)
    $ Fl.say(Fl_r, "Седьмая строчка заставила меня удивиться. {w}То ли это сыграл чистый рандом расстановки букв, то ли это медсестра тут так прикалывается над детьми.")
    $ Fl.say(Fl_th, "Ладно, буду надеяться что у меня всё впорядке со зрением и это просто случайно такое слово вылезло.")

    scene bg Fl_int_aidpost_day at Fl_bg_zoom_otd(3.0, 1.0, 1.5, 1.0, 0.5, 0.3, 0.5)
    $ Fl.Pause(1.5)

    $ Fl.say(Fl_r, "Я мог бы и дальше вести описание медпункта, если бы не вмешалась медсестра.")

    $ Fl.PlayMusic("Fl_niles_blues", 1, 4)
    show cs normal with Fl_dissolve1

    $ Fl.say(Fl_csk, "Привет... пионер! Что-то болит?")

    $ Fl.Status("+20")
    $ Fl.say(Fl_r, "Я вытаращился на медсестру, которая была самым ярким экспонатом в этом помещении. {w}Чего стоил только ее белый халатик, в котором девушке с такой большой... кхм... «душой» явно было тесновато.")

    $ Fl.Status("+20")
    $ Fl.say(Fl_th, "<Них*я> себе! Это что за сокровище милфхантера?")
    $ Fl.say(Fl_th, "Если бы в военкомате была такая такая медсестра, я бы...")

    show Fl_fogging with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Сударь, притормози! И челюсь приподними, а то стоишь как дурак с открытым ртом, слюни пускаешь!")
    $ Fl.say(Fl_th, "Не ну ты видишь это?")
    $ Fl.say(Fl_kvl, "Да вижу я! У девушки довольная апетитная фигура и я полностью разделяю с тобой впечатление от увиденного, но нужно прийти в себя, а то ты сейчас выглядишь, как придурок!")

    $ Fl.Status("-20")
    $ Fl.say(Fl_th, "Блин точно!")
    hide Fl_fogging with Fl_dissolve1

    $ Fl.say(Fl_r, "Я никогда не фанател по девушкам с пышным бюстом. Но здесь не удержался и засмотрелся на вырез, что вызвало у Виолы лишь улыбку. Похоже, она привыкла к такой реакции. А может, специально не застегивала несколько пуговиц, чтобы эту реакцию вызывать.")
    $ Fl.say(Fl_th, "И именно я попался в её ловушку. {w}Но нужно отдать уважение пуговицам, которые каждый день совсех сил стараются удержать такое сокровище, чтобы его никто не увидел.")

    show cs smile with Fl_fast

    $ Fl.say(Fl_csk, "Что встал, пионер? Подходи.")

    show cs shy with Fl_fast

    $ Fl.say(Fl_csk, "Или лучше мне подойти, чтобы тебе было лучше видно?")

    show cs smile with Fl_fast

    if persistent.Fl_dictionary_17 == False:
        $ Fl.PodskDict()
    $ persistent.Fl_dictionary_17 = True
    $ Fl.say(Fl_r, "Кое-как мне удалось поднять свой взгляд наверх, где распологались глаза медсестры. {w}Я бы сказал, довольно красивые глаза, разного цвета. {w}Один синий, другой - необычного, почти красного, цвета. Кажется, это называется {i}гетерохромией{/i}.")
    $ Fl.say(Fl_gg, "З-здрасьте.")
    $ Fl.say(Fl_r, "Я был не в состоянии связать и двух слов. Настолько меня поразила здешняя медсестра.")

    show cs shy with Fl_fast

    $ Fl.say(Fl_cs, "Ты у нас Ян, новенький, верно? Меня зовут Виолетта Церновна, но для тебя просто Виола.")
    $ Fl.say(Fl_th, "Для тебя?..")

    show Fl_fogging with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Воу, а ты походу ей приглянулся.")
    $ Fl.say(Fl_th, "Да я сам в шоке, как оброзший бомж(по словам вожатой) может кому-то понравится.")
    $ Fl.say(Fl_kvl, "Ну ты там не зазнавайся, а то Мику ещё ревновать начнёт.")
    $ Fl.say(Fl_th, "Не напоминай!")
    hide Fl_fogging with Fl_dissolve1

    show cs smile with Fl_fast

    $ Fl.say(Fl_cs, "Да ты подходи, не бойся, пионер. Давай мы тебя осмотрим. {w}Садись на кушеточку.")
    $ Fl.say(Fl_r, "И я послушно сел на кушетку.")
    $ Fl.say(Fl_cs, "Раздевайся, пионер.")

    $ Fl.Pause (3.0)

    show cs shy with Fl_fast

    $ Fl.say(Fl_cs, "Штаны то зачем снимать было?")
    $ Fl.say(Fl_r, "Действительно, я зачем-то разделся до трусов и только щас понял, что ниже пояса у меня резко потяжелело.")
    $ Fl.say(Fl_r, "Я поспешил натянуть штаны обратно, пока Виола ничего не заметила.")

    show cs smile stethoscope with Fl_dissolve1

    $ Fl.say(Fl_r, "С помощью стетоскопа Виола начала слушать мои лёгкие. В следующий миг меня пронзило холодом.")

    $ Fl.Pause (3.0)

    $ Fl.say(Fl_r, "Наконец она закончила эту операцию и, убрав прибор, вновь предстала передо мной.")

    show cs sad with Fl_fast

    $ Fl.say(Fl_cs, "Курить вредно, пионер. Пожалей свои легкие. Да и сердечко у тебя что-то шалит.")
    $ Fl.say(Fl_gg, "А что с ним не так?")

    show cs smile with Fl_fast

    $ Fl.say(Fl_cs, "Да колотится как мотор.")
    $ Fl.say(Fl_gg, "И чья в этом по вашему вина?")
    $ Fl.say(Fl_cs, "А я то что? Я тебе только добра желаю.")
    $ Fl.say(Fl_th, "Странное у неё понятие добра...")
    $ Fl.say(Fl_cs, "Ладно, давай сюда свой обходной, ты же ведь из-за него здесь?")
    $ Fl.say(Fl_gg, "А да, точно! Сейчас.")
    $ Fl.say(Fl_th, "Из-за этой барышны, обходной вылетел из мой головы.")

    hide cs smile with Fl_fast

    $ Fl.say(Fl_r, "Виола достала маленькую ручку из грудного кармана и присев за стол начала аккуратно выводить свою подпись.")

    $ Fl.Pause (2.5)
    show cs smile with Fl_fast

    $ Fl.say(Fl_cs, "Держи.")
    $ Fl.say(Fl_r, "Я взял обходной. Виола как-то странно на меня посмотрела, после чего заявила.")

    show cs shy with Fl_fast

    $ Fl.say(Fl_cs, "У тебя сегодня, наверное, много дел. Приходи завтра, пионер. Начнем с тобой {i}настоящую терапию{/i}.")
    $ Fl.say(Fl_r, "В голове сразу же нарисовалась эта «настоящая терапия». В штанах снова стало тесно от моей бурной фантазии и слов Виолы.")
    $ Fl.say(Fl_r, "Задерживаться здесь было для меня опасно, подпись есть значит можно идти за последней! {w}Но вот предложение Виолы меня действительно заинтересовало.")
    $ Fl.say(Fl_gg, "До свидания.")

    show cs smile with Fl_fast

    $ Fl.say(Fl_cs, "До свидания, пионер. {w}Не болей.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(3)
    $ Fl.PlaySound("Fl_open_door_2", 1.0, 0, False)
    scene bg Fl_black with Fl_dissolve1

    $ Fl.Pause(2.0)

    scene bg Fl_ext_aidpost_day
    show Fl_light_c
    with Fl_dissolve2

    $ Fl.Pause(1.0)

    $ persistent.Fl_dostn_9 = True
    show Fl_dost_9_in_kod:
        xalign -1.0 yalign 0.7
    show Fl_dost_9_in_kod:
        ease 1.0 xalign 0.01
    $ Fl.Pause(0.5)
    $ Fl.PlaySound("Fl_achievement", 1, 0, False)
    $ Fl.Pause(1.5)
    hide Fl_dost_9_in_kod with Fl_dissolve1


    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_th, "И что это мать вашу было?")
    $ Fl.say(Fl_r, "Я подождал, пока возбуждение окончательно спадет. Не идти же в таком виде через весь лагерь.")
    $ Fl.say(Fl_r, "Но ко мне решил подойти дружище. Как не вовремя...")

    show msk evilsmile shirt with Fl_dissolve1

    $ Fl.say(Fl_msk, "Ну что, как прошло?")
    $ Fl.say(Fl_msk, "Хотя нет, можешь не говорить. {w}По лицу вижу, что медсеструха тебе понравилась!")
    $ Fl.say(Fl_gg, "Так ты всё знал и поэтому меня одного оставил?")
    $ Fl.say(Fl_msk, "Ага, скажем так подгон от Михалыча!")
    $ Fl.say(Fl_gg, "Ну подгон действительно хорош!")

    show msk grin shirt with Fl_fast

    $ Fl.say(Fl_msk, "Знал, что тебе понравится! С тебя должок!")
    $ Fl.say(Fl_gg, "За что?")

    show msk evilsmile shirt with Fl_fast

    $ Fl.PlaySound("Fl_msk_laugh", 1, 0, False)
    $ Fl.say(Fl_msk, "За просмотр <бл*>!")
    $ Fl.say(Fl_gg, "Всё с тобой ясно.")

    $ Fl.Pause(1.0)
    show msk smile shirt with Fl_fast

    $ Fl.say(Fl_msk, "Чё куда дальше там?")
    $ Fl.say(Fl_gg, "Музклуб остался.")
    $ Fl.say(Fl_msk, "О, вот там я ещё не был. Щас глянем чё там интересного!")
    $ Fl.say(Fl_gg, "Тогда шагом...")

    show msk evilsmile shirt with Fl_fast

    $ Fl.say(Fl_msk, "Марш <бл*ть>!", _with=hpunch)
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(2.0)

    scene bg Fl_ext_square_day
    show Fl_light_c
    with Fl_dissolve2

    $ Fl.PlayMusic("Fl_sunrise", 1, 4)
    $ Fl.Pause(1.0)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "Идя мимо площади, нам навстречу попалась вожатая, которая запреметив нас направилась в нашу сторону.")

    show mv normal pioner1 with Fl_dissolve1

    $ Fl.say(Fl_mv, "Пионеры, как это понимать? {w}Почему до сих пор не в форме?")

    $ Fl.Status("-40")
    $ Fl.say(Fl_r, "Которая тут же начала нас отчитывать.")

    show mv normal pioner1 with moveinright:
        left
    show msk sad shirt with Fl_fast:
        right

    $ Fl.say(Fl_msk, "А, это... {w}она порвалась просто.")
    $ Fl.say(Fl_r, "Михан ничего лучше не придумал, чем просто соврать.")
    $ Fl.say(Fl_mv, "И как ты умудрился её порвать?")
    $ Fl.say(Fl_msk, "Нууу...")
    $ Fl.say(Fl_r, "Задумался он.")
    
    show mv angry pioner1 with Fl_fast

    $ Fl.say(Fl_mv, "Что ну? Давай, отвечай на мой вопрос!")
    $ Fl.say(Fl_msk, "Бежал я такой, на ветку наткнулся и вот...")

    show mv normal pioner1 with Fl_fast

    $ Fl.say(Fl_mv, "Всё с тобой ясно. {w}Ян, а что ты скажешь в своё оправдание? Почему не зашёл ко мне за формой?")
    $ Fl.say(Fl_gg, "Марина Владимировна, обходной сам себя не заполнит.")
    $ Fl.say(Fl_r, "Я демонстранционно помахал листом бумаги.")

    show mv smile pioner2 with Fl_fast

    $ Fl.say(Fl_mv, "Точно.")

    show mv laugh pioner2 with Fl_fast

    $ Fl.Status("+20")
    $ Fl.say(Fl_mv, "Прости, что-то я запамятовала.")
    $ Fl.say(Fl_th, "Мда{mn} {w}Я тут значит бегаю по всему лагерю, чтобы заполучить все подписи, а она забыла...")

    show mv smile pioner1 with Fl_fast

    $ Fl.say(Fl_mv, "Ладно, тогда не буду вас задерживать. Но, Ян, не забудь после обеда ко мне зайти!")

    show mv normal pioner1 with Fl_fast

    $ Fl.say(Fl_mv, "И тебя это тоже касается!")
    $ Fl.say(Fl_r, "Последние слова были адресованы моему товарищу по несчастью.")

    hide mv normal pioner1 with Fl_fast
    show msk sad shirt with moveinright:
        center

    $ Fl.say(Fl_msk, "Как же она меня <за*бала>...")
    $ Fl.say(Fl_msk, "Пионер то, {w}пионер сё!")
    $ Fl.say(Fl_gg, "Да, жизнь не справедливая, везде правила.")

    hide msk sad shirt with Fl_fast

    $ Fl.say(Fl_r, "С этим заключением мы отправились в сторону музклуба, попутно жалуясь на порядок общества.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(2.0)

    scene bg Fl_ext_musclub_day
    show Fl_light_c
    with Fl_dissolve2

    $ Fl.Pause(1.0)

    $ Fl.Status("-40")
    $ Fl.Status("panic", False)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.AutoSave()
    $ Fl.say(Fl_r, "Чем ближе мы походили к храму музыки, тем отчётливее в голове проскакивали моменты из сегоднящнего утра.")
    $ Fl.say(Fl_r, "Внутри нарастала необъяснимая тревога. Идти вовсе не хотелось. {w}Меня облепила вязкое чувство паранойи, которое заставляло меня оглядывать по сторонам и представлять самые страшные фантазии моей воспалённой фантазии.")
    $ Fl.say(Fl_th, "Возможно я себя накручиваю... {w}Может, мне и правда всё просто показалось или это был глупый розыгрыш.")

    show Fl_fogging with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Сколько раз тебе повторять, что тебе ничего не показалось, всё было взаправду!")
    $ Fl.say(Fl_th, "Откуда такая уверенность?")
    $ Fl.say(Fl_kvl, "Опять ты за своё...")
    $ Fl.say(Fl_kvl, "Если так интересно узнать, то спроси у неё прямо о том что утром произошло.")
    $ Fl.say(Fl_th, "Так и сделаю.")
    hide Fl_fogging with Fl_dissolve1

    $ Fl.Status("+40")
    $ Fl.Status("normal", False)
    $ Fl.Save("День2: В гостях у Микуски.")
    $ Fl.say(Fl_r, "Оставив все опасения позади, я решил никого не слушать, ни свой инстинк самосохранения, ни внутреннего голоса.")
    $ Fl.HideScreens(_with=Fl_fast)
    $ Fl.StopMusic(3)
    scene bg Fl_black with blinds

    $ Fl.Pause(1.0)

    scene bg Fl_ext_musclub_verandah_day with blinds
    $ Fl.Pause(1.0)
    scene bg Fl_ext_musclub_verandah_day:
        subpixel True
        linear 2.0 zoom 1.3 xalign 0.6 yalign 0.4
    $ Fl.PlaySound("Fl_walk2", 1, 0, False)
    $ Fl.Pause(2.5)

    $ Fl.PlaySound("Fl_open_door_2", 1.0, 0, False)
    scene bg Fl_int_musclub_mattresses_day with Fl_flash:
        subpixel True
        zoom 1.4 xalign 0.5 yalign 0.5 alpha 1.0
        ease 5 zoom 1.0 xalign 0.5 yalign 0.5 alpha 1.0
            
    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.PlayMusic("Fl_doramaprosto4", 1, 4)
    $ Fl.say(Fl_r, "И вот я вновь, стоя за порогом, бегло осматриваю музкружок. {w}С вчерашнего дня здесь ничего не изменилось, даже чистота стояла такая же, видно Мику уже успела с утра прибраться.")
    $ Fl.say(Fl_r, "Но сейчас меня больше волновала сама хозяйка, нежели помещение. Ищя взглядом Мику, внутри нарастало беспокойство. {w}Девушки нигде не было.")

    show msk smile shirt with Fl_fast:
        right

    $ Fl.say(Fl_msk, "Ау! Есть кто живой?", _with=hpunch)

    $ Fl.PlaySound("Fl_piano_head_bump", 1.0, 0, False)
    $ Fl.AttackScreens(True)
    $ Fl.say(Fl_mi, "Ай!")
    $ Fl.say(Fl_r, "Раздалось из под рояля. {w}Громкий голос Михана напугал пионерку из-за чего та ударилась головой о дно клавишного гиганта.")

    show mi sad pioneer2 with Fl_dissolve1:
        left

    $ Fl.say(Fl_mi, "Тсс... Ауч...")
    $ Fl.say(Fl_r, "Мику стояла и потирала ушибленное место. Кажется она сильно стукнулась затылком, может даже шишка будет если ничего холодного не приложить.")

    show mi dontlike pioneer1 with Fl_fast

    $ Fl.say(Fl_mi, "Зачем так кричать? Можно ведь было просто поздороваться!")

    show mi shy pioneer1 with Fl_fast

    $ Fl.say(Fl_mi, "Ой, Янечка пришёл.")
    $ Fl.say(Fl_r, "В начале Мику начала негодовать нашей бескультурной манере, но заприметив меня на её лице сразу появился румянец.")
    $ Fl.say(Fl_gg, "Привет. Не сильно ушиблась?")
    $ Fl.say(Fl_r, "Решил поинтересоваться я. {w}Может утрений инцедент и оставил осадок к Мику, но вчерашнее времяпрепровождение сильно перевешивало моё отношение к пионерке в лучшую сторону.")

    show mi happy pioneer2 with Fl_fast

    $ Fl.say(Fl_mi, "Всё в порядке не волнуйся. Немножко болит, но думаю шишки не будет.")
    $ Fl.say(Fl_r, "В знак понимания я просто кивнул.")
    $ Fl.say(Fl_r, "Мику вела себя как обычно, никаких яндерных фразочек и суженных зрачков, только жизнерадостная и болтливая японка. {w}От чего на душе сразу стало спокойно.")

    show msk serious shirt with Fl_fast

    $ Fl.say(Fl_msk, "Это конечно всё очень интересно, но может ты наконец-то подпишишь свой обходной. А то скоро обед, я жрать хочу!")
    $ Fl.say(Fl_r, "Стоя права от меня, заговорил Михан с серьёзным видом.")
    $ Fl.say(Fl_gg, "Мику, можешь подписать обходной?")
    $ Fl.say(Fl_r, "Я протянул ей злосчастный листик из-за которого мне пришлось почти до самого обеда оббегать весь лагерь. {w}Ну хотя бы какой-то плюс от скитаний: местность узнал и друга себе нашёл.")

    show mi normal pioneer3 with Fl_fast

    $ Fl.say(Fl_mi, "Конечно! Я сейчас! Только за ручкой сбегаю и обратно!")

    $ Fl.PlaySound("Fl_run", 1, 0, False)
    show mi normal pioneer3 at Fl_bg_zoom_e(1.0, 1.0, 1.7, 0.05, -5.0, 0.35, 0.35)

    $ Fl.Pause(4.5)

    $ Fl.say(Fl_r, "Пока Мику упорхнула в кладовку, Михан подошёл к роялю.")

    hide msk serious shirt with Fl_fast

    $ Fl.say(Fl_msk, "Лан, пока она там возится, сыграну на этом хренетияно разок.")
    $ Fl.say(Fl_r, "Усевшись за табурет, он начал играть. {w}Точнее пытаться играть.")
    $ Fl.say(Fl_r, "Честно говоря, получалось у него...")

    $ Fl.PlayMusic("Fl_vzriv_mozga", 1, 3)
    $ Fl.PlaySound("Fl_attack", 1, 0, False)
    $ Fl.AttackScreens(True)
    $ Fl.Status("-20")
    $ Fl.say(Fl_r, "ПРОСТО УЖАСНО!")

    show Fl_vignette with Fl_flash_red

    $ Fl.say(Fl_r, "Звуки напоминали взрывы от бомбордировки, что жутко резало по ушам. Что вот-вот пойдёт кровь из барабанных перепонок.")

    show mi normal pioneer3 with easeinleft:
        left

    $ Fl.say(Fl_r, "И тут наконец Мику вернулась и...")

    show mi shocked pioneer1 with vpunch

    $ Fl.say(Fl_r, "Чуть не подпрыгнула от шока.")
    $ Fl.say(Fl_mi, "Что это за звуки?!")
    $ Fl.StopMusic(2)

    $ Fl.Pause(1.5)

    hide Fl_vignette with Fl_dissolve1
    show msk smile shirt with Fl_fast:
        right

    $ Fl.PlayMusic("Fl_doramaprosto4", 1, 4)
    $ Fl.say(Fl_msk, "Хе, это я так играю. Моя собственная композиция. {w}Называется - Взрыв Мозга.")

    $ Fl.PlaySound("Fl_mi_laugh", 1, 0, False)
    show mi laugh pioneer1 with Fl_fast

    $ Fl.say(Fl_mi, "Вау, да у тебя талант! Можешь потом меня научить как играть эту композицию?")

    show msk surprise shirt with Fl_fast

    $ Fl.say(Fl_msk, "Чё? {w}Всмысле?")

    $ Fl.Status("+20")
    $ Fl.say(Fl_r, "Миха явно ожидал немного другой реакции на его игру, поэтому слова Мику дали сбой в его голове.")
    $ Fl.say(Fl_gg, "Ладно, Мику, мы пойдём. Нужно ещё вожатую найти.")

    show mi sad pioneer2 with Fl_fast
    show msk smile shirt with Fl_fast

    $ Fl.say(Fl_msk, "Да, точняк! Погнали, Янчик, сдадим ей эту <х*йню>, а потом хавать пойдём.")
    $ Fl.say(Fl_mi, "Ладно...", cps="28")
    $ Fl.say(Fl_r, "На лице Мику появилась грусть, а глаза были переполнены печалью. Было очень трудно в них смотреть, казалось что мои слова для неё были словно иглы, которые пронзили её на сквозь.")

    hide mi sad pioneer2
    hide msk smile shirt 
    with Fl_fast

    $ Fl.say(Fl_r, "Михан положил мне руку через плечо и ещё раз попрощался с Мику. {w}И вот в такой странной позе мы отправились к выходу, но вдруг я почувствовал как мою футболку кто-то сзади потянул.")

    show mi pity grin2 pioneer3 with Fl_dissolve1

    $ Fl.say(Fl_r, "Этим кто-то оказалась Мику, которая легонько держала край моей футболки и мило смущалась.")
    $ Fl.say(Fl_mi, "Ян, ты не мог бы задержаться. {w}Пожа{w=0.05}а{w=0.05}а{w=0.05}а{w=0.05}а{w=0.05}алуйста.")

    show Fl_fogging with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Хмм. Интересненько. Неужели она ждёт утреннего продолжения? Щас будет нежно тебя покусывать, Сударь.")
    $ Fl.say(Fl_th, "Не спасибо, я пожалуй откажусь.")
    $ Fl.say(Fl_th, "Ну а если серьёзно, как думаешь ради чего она просит меня остаться с красным лицом?")
    $ Fl.say(Fl_kvl, "Очевидно, чтобы продолжить то на чём вы вчера ночью остановились.")
    $ Fl.say(Fl_th, "Понятно. Можно было даже не спрашивать...")
    hide Fl_fogging with Fl_dissolve1

    $ Fl.say(Fl_gg, "Хорошо.")

    show mi normal pioneer3 with Fl_fast

    $ Fl.say(Fl_r, "После чего Мику меня отпустила и одарила искренней улыбкой. Я не знаю почему согласился с ней остаться, возможно я просто не мог отказать девушке когда она так просит или просто хочу и дальше поиграть с огнём и узнать о странном поведении девушки утром.")
    $ Fl.say(Fl_r, "Миха убрал свою руку с моего плеча, поднял большой палец и сказал: «удачи», с прехитрой улыбкой, явно намекая на что-то. {w}И вышел наружу.")

    $ Fl.PlaySound("Fl_open_door_2", 1.0, 0, False)
    $ Fl.say(Fl_th, "И этот ту даже...")
    $ Fl.say(Fl_gg, "Мику, так ради чего ты меня решила задержать?")

    show mi look away pioneer3 with Fl_fast

    $ Fl.say(Fl_mi, "Ну{mn}")

    show mi joy pioneer3 with Fl_fast

    $ Fl.say(Fl_mi, "Я просто хотела тебя заманить в клуб.")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_th, "Вот хитрюга.")

    show mi sad pioneer2 with Fl_fast

    $ Fl.say(Fl_mi, "Ян, ты ведь сам говорил, что будешь посейщать клуб, а сам с самого утра куда-то убежал... А я всё ждала, когда ты ко мне зайдёшь. Совсем одна...")
    $ Fl.say(Fl_gg, "Точно, прости... Из-за обходного у меня не было времени к тебе зайти...")
    $ Fl.say(Fl_gg, "Мне очень жаль!")

    $ Fl.Master(Fl_bg_zoom_th(1.0, 2.0, 1.0, 0.5, 0.5, 0.5, 0.75))
    if persistent.Fl_dictionary_5 == False:
        $ Fl.PodskDict()
    $ persistent.Fl_dictionary_5 = True
    $ Fl.say(Fl_r, "Для пушего эффекта я сложил руки по бокам и опустил голову, тем самым изображая {i}Одзиги{/i}.")

    show mi despair2 pioneer3 with Fl_fast

    $ Fl.say(Fl_mi, "Ян, что ты делаешь?!", _with=hpunch)

    $ Fl.Pause(1.5)
    show mi shy pioneer1 with Fl_fast

    $ Fl.say(Fl_mi, "Прекрати, ты меня смущаешь!")
    $ Fl.say(Fl_gg, "Не прекращу, пока не простишь.")
    $ Fl.say(Fl_r, "Невыходя из ролли японского школьника, продолжал я.")

    show mi shy3 pioneer3 with Fl_fast

    $ Fl.say(Fl_mi, "Да прощаю я тебя, только перестань!")

    $ Fl.Master(Fl_bg_zoom_otd(2.0, 1.0, 1.0, 0.5, 0.5, 0.75, 0.5))
    $ Fl.say(Fl_r, "Я выпрямился обратно. {w}Сценка получилась очень забавная и сильно смутила Мику. А я остался довольным таким результатом. {w}Ведь смог угнаться за двумя зайцами сразу, загладить вину перед пионеркой и увидеть её милое личико, когда она впадает в краску.")

    show mi normal pioneer3 with Fl_fast

    $ Fl.say(Fl_mi, "Дурак!")
    $ Fl.say(Fl_r, "Я улыбнулся, но что-то беспокоило меня в словах Мику, которые она произнесла до этого.")

    $ Fl.StopMusic(4)
    $ Fl.say(Fl_th, "...А сам с самого утра куда-то убежал...")

    $ Fl.Pause (1.0)

    $ Fl.Status("-20")
    $ Fl.say(Fl_th, "Неужели она не помнит, что произошло сегодня утром и то как она себя вела, словно одержимая...")
    $ Fl.say(Fl_th, "Стоит ли у неё расспршивать об этом или может просто закрыть глаза на этот инцедент?")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    menu:
        "Спросить о странном поведении":
            $ Fl.ShowScreens(_with=Fl_dissolve1)
            $ Fl.PlayMusic("Fl_razg_zn", 1, 4)
            $ Fl.say(Fl_gg, "Мику, можно тебя кое о чём спросить?")
            $ Fl.say(Fl_mi, "Да конечно! Спрашивай о чём угодно. Я постараюсь ответить на любой твой вопрос!")
            $ Fl.say(Fl_th, "Ну была не была!")
            $ Fl.say(Fl_gg, "Мику, что с тобой сегодня произошло?")

            show mi upset pioneer3 with Fl_fast

            $ Fl.say(Fl_mi, "Ян, о чём ты говоришь? Что такое утром произошло?")

            $ Fl.Status("-10")
            $ Fl.say(Fl_th, "Неужели под дурочку косит? {w}Хотя по глазам и голосу нельзя сказать, что она врёт...")
            $ Fl.say(Fl_gg, "Ты очень странно себя вела. {w}В начале смотрела как я спал, а потом хотела укусить меня!")

            show mi dontlike pioneer1 with Fl_fast

            $ Fl.say(Fl_mi, "Ян, хватит уже. Это не смешно!")
            $ Fl.say(Fl_r, "Мой расспрос не дал никаких ответов, а наоборот только разозлил Мику. Она приняла серьёзное лицо со строгим взглядом. Её жгучий взор прожигал меня изнутри из-за чего было страшно смотреть в сторону пионерки.")
            
            $ Fl.Status("-10")
            $ Fl.say(Fl_th, "Чёрт, ничего не понимаю... Голос нужна твоя помощь.")

            show Fl_fogging with Fl_dissolve1
            $ Fl.say(Fl_kvl, "Очевидно она либо врёт, либо не помнит что произошло этим утром. Что на самом деле ещё хуже! Если она не может дать отчёт своим действиям, она становится ещё опаснее для тебя.")
            $ Fl.say(Fl_th, "Врёт или не помнит...")
            $ Fl.say(Fl_th, "И то и то хреново! {w}Но в любом случае я ничего у неё узнать не смогу, нет смысла продолжать это. Только тупее буду выглядить, ещё за шизоида примет.")
            hide Fl_fogging with Fl_dissolve1

            show mi sad pioneer2 with Fl_fast

            $ Fl.say(Fl_mi, "Единственный кто себя странно вёл сегодня утром это ты, Ян...")
            $ Fl.say(Fl_mi, "Смотрел на меня испуганным взглядом, будто приведение увидел. {w}А потом убежал куда-то. Я пыталась тебя остановить, кричала, а ты даже слушать не стал...")

            show Fl_fogging with Fl_dissolve1
            $ Fl.say(Fl_kvl, "Вот как для неё всё было на самом деле, интересно...")
            $ Fl.say(Fl_th, "Если она не врёт, конечно!")
            $ Fl.say(Fl_kvl, "Ну да, если она просто не выдумала. Чтобы ты считал, что всё это было не больше чем глюк.")
            hide Fl_fogging with Fl_dissolve1

            $ Fl.Status("+15")
            $ Fl.say(Fl_gg, "Прости... Походу акклиматизация, вот и почудилось что-то странное. Наверное я глупо сейчас выглядел?")

            show mi pity smile2 pioneer2 with Fl_fast

            $ Fl.say(Fl_mi, "Всё нормально, но больше не пугай меня так, ладно?")
            $ Fl.say(Fl_r, "В ответ я кивнул. {w}Мне повезло, что Мику необидчивая личность и может слёгкостью закрыть глаза даже на такие громкие обвинения. {w}Но всё же не стоит так играть на чувствах девушки...")
            $ Fl.say(Fl_th, "Голос?")

            show Fl_fogging with Fl_dissolve1
            $ Fl.say(Fl_kvl, "Позже это обсудим. Сейчас мне нужно всё обдумать.")
            $ Fl.say(Fl_th, "Ладно.")
            $ Fl.StopMusic(3)
            hide Fl_fogging with Fl_dissolve1

            $ Fl.Status("+25")
            $ Fl.Pause(4.0)


            $ add_mi += 1
            $ Obs_mi += 2




        "Рассказать ей про домик":
            $ Fl.ShowScreens(_with=Fl_dissolve1)
            $ Fl.PlayMusic("Fl_dorama_kt1", 1, 4)
            $ Fl.say(Fl_r, "Пока я размышлял стоит ли поднимать тему про утренний инцедент, как случайно мои руки полезли в карманы.")
            $ Fl.say(Fl_r, "Мои пальцы нащупали ключ от домика... {w}и ещё один...")
            
            $ Fl.Status("+30")
            $ Fl.say(Fl_th, "Точно! Я ведь утром ключи Мику забрал, когда одевался. {w}Интересно если бы я не вспомнил тогда о них, то чтобы со мной сделала Мику?")
            $ Fl.say(Fl_gg, "Кстати, Мику, представляешь меня поселили в твоём домике. Теперь мы с тобой соседи.")

            show mi grin pioneer2

            $ Fl.say(Fl_mi, "Правда-правда?!", _with=hpunch)

            $ Fl.PlaySound("Fl_mi_laugh", 1, 0, False)
            show mi laugh pioneer1 with Fl_fast

            $ Fl.say(Fl_mi, "УРА! Янечка, теперь живёт со мной! Я так рада!!! Мы теперь сможем столько всего вместе делать! Петь, играть, веселиться, болтать до утра! Ура!")
            $ Fl.say(Fl_gg, "{mn}")
            
            $ Fl.Pause(1.5)

            $ Fl.say(Fl_th, "Не думал, что после такой информации, Мику вот так бурно отреагирует. Неужели она правда счастлива, что я теперь живу с ней в одном домике?")

            hide mi laugh pioneer1 with Fl_fast

            $ Fl.say(Fl_r, "Но ждать ответа долго не пришлось. Мику начала носиться туда сюда и подпрыгивать. Она радовалась как маленький ребёнок, которому купили игрушку.")
            $ Fl.say(Fl_r, "Мику прям светилась от счастья.")
            $ Fl.say(Fl_r, "Она начала перечислять все возможные виды занятий, которые она хотела бы со мной разделить. И переодически повторяя «Ура»!")
            $ Fl.say(Fl_gg, "Мику?")

            $ Fl.Pause(1.0)
            $ Fl.say(Fl_gg, "Слушай, Мику...")
            $ Fl.say(Fl_r, "Я пытался достучаться до пионерки, но казалось что мои слова пролетали мимо ушей девушки, которая светилась от радости, подобно самой яркой звезде.")
            
            $ Fl.AttackScreens()
            $ Fl.say(Fl_r, "Но мне удалось её поймать и взять за плечи, тем самым остановить поток богатой фантазии Мику.")
            $ Fl.say(Fl_gg, "Мику, остановись!")

            show mi confusion pioneer3 with Fl_fast

            $ Fl.say(Fl_mi, "А? Что такое?")
            $ Fl.say(Fl_gg, "Мику, я тоже очень рад, что теперь живу с тобой в одном домике, но зачем же так бурно реагировать?")

            show mi joy2 pioneer3 with Fl_fast

            $ Fl.say(Fl_mi, "Прости... Просто я так обрадовалась, что не смогла себя сдержать.")

            show mi tender2 pioneer3 with Fl_fast

            $ Fl.say(Fl_mi, "Но я правда очень рада, что теперь мы будем жить в одном домике.")
            $ Fl.say(Fl_gg, "И я.")
            $ Fl.say(Fl_r, "На моём лице появилась улыбка и почему-то теперь я тоже светился от счастья. Возможно лучики счастья Мику попали и на моё вечно угрюмое лицо.")
            $ Fl.say(Fl_r, "Да безусловно, глубоко внутри я осознавал, что возможно наше сожительство может послужить мне серьёзной угрозой, если Мику и правда одержима, она может в любой момент на меня напасть.")
            $ Fl.say(Fl_r, "Но в данный момент меня это мало волновало. Глядя на Мику и её обворожительную улыбку, все самые страшные опасения пропали вовсе.")
            $ Fl.say(Fl_gg, "А точно чуть не забыл.")
            $ Fl.say(Fl_r, "Я вытащил из карманов джинс ключ и протянул его Мику.")

            show mi pity pioneer1 with Fl_fast

            $ Fl.say(Fl_mi, "Ой! Я как раз его потеряла, всё в домике осмотрела, а так и не нашла.")
            $ Fl.say(Fl_mi, "Ян, где ты его нашёл?")
            $ Fl.say(Fl_th, "Ну как сказать... {w}Я просто по чистой случайности прихватил его пока одевался, а потом благодаря ему смог сбежать от Яндерки-Мику.")
            $ Fl.say(Fl_r, "Но я решил упустить этот момент и просто соврал.")
            $ Fl.say(Fl_gg, "Он на ступеньках валялся, вот подумал, что наверное ты его потеряла.")

            show mi happy pioneer2 with Fl_fast

            $ Fl.say(Fl_mi, "Спасибо тебе большое, что нашёл его.")

            show mi grin pioneer2 with Fl_fast

            $ Fl.say(Fl_mi, "Ян - ты мой герой!")

            $ Fl.say(Fl_r, "Я покраснел. {w}Я не ожидал услышать чего-то подобного, а ещё то каким тоном и с выражением лица она это произнесла, такой милоте я не смог противостоять.")

            $ Fl.PlaySound("Fl_mi_laugh", 1, 0, False)
            show mi laugh pioneer1 with Fl_fast

            $ Fl.say(Fl_mi, "Хахахах. Ян, засмущался!")
            $ Fl.say(Fl_gg, "Тебе просто показалась.")
            $ Fl.say(Fl_r, "Я постарался сделать более каменное лицо, но вышло у меня это так себе.")

            $ Fl.PlaySound("Fl_mi_laugh", 1, 0, False)
            $ Fl.say(Fl_mi, "Хахах. Засмущался, засмущался!")
            $ Fl.say(Fl_r, "Продолжала повторять Мику с детской улыбкой на лице.")

            $ Fl.Status("+20")
            $ Fl.say(Fl_r, "Данная картина заставила меня тоже засмеяться. И теперь к хохоту Мику присоединился и мой.")

            $ Fl.Pause(3.0)



            $ Ist_mi += 1




        "Промолчать":
            $ Fl.ShowScreens(_with=Fl_dissolve1)
            $ Fl.Status("+20")
            $ Fl.say(Fl_r, "Я решил, что лучше не стоит начинать расспрос. Хотя бы до той поры, пока не убежусь, что мне ничего не привиделось и странное поведение Мику не иллюзия.")
            $ Fl.say(Fl_th, "В данный момент не было ни одного намёка на то, что у Мику есть какие-то склонности к одержимости...")
            $ Fl.say(Fl_r, "Отложив данный разговор на другой раз, я вернулся к Мику.")


            $ Obs_mi += 1






    show mi smile pioneer2 with Fl_fast
    if Ist_mi == 1:
        $ Fl.Pause(0.1)
    else:
        $ Fl.PlayMusic("Fl_dorama_kt1", 1, 4)

    $ Fl.say(Fl_mi, "Кстати, Ян, я ведь хотела кое-что тебе показать!")

    scene bg Fl_int_musclub_mattresses_day:
        subpixel True
        zoom 1.0 xalign 0.5 yalign 0.5
        ease 1 zoom 1.3 xalign 0.8 yalign 0.75
    $ Fl.Pause(1.0)
    with vpunch


    $ Fl.say(Fl_r, "Сказала Мику после чего усадила меня на матрас, а сама побежала в сторону музыкальных инструментов.")
    $ Fl.say(Fl_r, "Её целью оказалась обычная гитара. Взяв её в руки, она быстро подсела ко мне с прехитрой улыбкой.")
    $ Fl.say(Fl_r, "После чего посмотрела ещё раз на гитару, потом на меня своими голубыми глаза, которые напоминали цвет морской волны.")

    $ Fl.StopMusic(5)
    $ Fl.say(Fl_r, "Мику прикинула и лёгкими движениями кончиков пальцев начала перебирать струны. И вновь задумалась, будто пыталась что-то вспомнить.")
    $ Fl.say(Fl_r, "На миг всё затихло, казалось что не одна Мику погрузилась в размышления, а вместе с собой она забрала и меня. {w}Но это был всего лишь миг... Пионерка улыбнулась и снова посмотрела на меня. На сей раз в её глазах появился огонёк.")
    $ Fl.say(Fl_mi, "Ян, слушай!")
    $ Fl.say(Fl_r, "Мику уверенно поставила пальцы, зажимая нужные акорды, и начала играть.")
    $ Fl.StopAmbience(3)
    $ Fl.HideScreens(_with=Fl_fast)

    $ Fl.PlayMusic("Fl_Sredi_nikh_ty_cover", 1, 3)

    $ Fl.Pause(6.0)
    show Fl_belizna_eff with Fl_dissolve1

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_th, "Это ведь{mn}")
    $ Fl.say(Fl_r, "Звонкий девичий вокал разнёся по всему музклубу. {w}Мику исполняла мою песню, которую я ей продемонстрировал вчера на бас-гитаре.")
    
    $ Fl.Status("+15")
    $ Fl.say(Fl_r, "Непроизвольно моё лицо нарисовалась улыбка. Улыбка, полная радости и счастья.")
    $ Fl.say(Fl_r, "Прослушивание своей композиции с женским вокалом, заставил меня погрузиться в нирвану. Казалось, что сейчас для меня существует только матрас и пионерка, а весь мир это сплошная пустота, состоящая из белого цвета.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Pause(1.0)
    call screen skip with Fl_dissolve1
    screen skip:
        tag menu
        modal True
        textbutton ["{font=[Fl_Script]}Пропустить{/font}"]:
            text_style "Fl_text_big_save_load"
            style "Fl_button_None"
            text_size 40
            ypos 990
            xalign 0.97
            action Hide("skip", Dissolve(1.0)), Return()
    hide Fl_belizna_eff with Fl_dissolve1



    $ Fl.StopMusic(3)
    $ Fl.Pause(3.5)
    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 3)
    $ Fl.PlayMusic("Fl_dorama_kt1", 1, 8)
    $ Fl.Status("-15")
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_mi, "Ян, ну что скажешь?! Правда здорово? Я только сегодня утром её выучила!")

    $ Fl.Pause(1.0)
    $ Fl.say(Fl_gg, "Мику{mn}", cps="28")
    $ Fl.say(Fl_gg, "Ты просто нечто!")
    $ Fl.say(Fl_r, "На моём лице давно не было такой широкой и настоящей, ненаигранной, улыбки. {w}Я аккуратно положил свою руку на голову Мику и медленно начал поглаживать.")

    $ Fl.Pause(2.5)
    $ Fl.say(Fl_mi, "Ян, ты меня смущаешь...")
    $ Fl.say(Fl_gg, "Прости.")
    $ Fl.say(Fl_r, "Рассмеялся я, после чего оставил макушку девушки в покое.")
    $ Fl.say(Fl_mi, "Но я рада, что тебе понравилось! Было сложно подобрать акорды по памяти, но у меня получилось.")
    $ Fl.say(Fl_gg, "Ты правда только утром её выучила?")
    $ Fl.say(Fl_mi, "Да!")

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_th, "Она и впрямь девушка аркест{mn} {w}Так ещё и с феноменальной памятью, потому что иначе я не могу объяснить, как за такой короткий срок можно запомнить мелодию и текст.")
    $ Fl.say(Fl_th, "Хотя, на создание этой песни у меня ушло всего две бессонные ночи, так что я тоже своего рода {u}необычный{/u}.")
    $ Fl.say(Fl_mi, "Янечка, а ты можешь ещё раз сыграть её на бас-гитаре. Просто на ней у меня не получается сыграть, а мне так нравится, как эта песня звучит именно на ней.")
    $ Fl.say(Fl_gg, "Без проблем, моя юная ученица.")

    $ Fl.PlaySound("Fl_mi_laugh", 1, 0, False)
    $ Fl.Pause(1.0)
    $ Fl.say(Fl_r, "Мику подала мне басуху и уселась рядом со мной.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(5)
    scene bg Fl_black with Fl_dissolve2
    $ Fl.Pause(5.5)


    $ Fl.Save("День2: Кушать в компании всегда приятно!")
    $ Fl.PlaySound("Fl_dinner_horn_processed", 1, 0, False)
    $ Fl.Pause(3.5)
    scene bg Fl_int_musclub_mattresses_day with Fl_dissolve2
    
    $ Fl.Pause(2.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.AutoSave()
    $ Fl.say(Fl_r, "Трудно сказать, сколько времени прошло с того момента, как в моих руках появилась бас-гитара. Но звук, означавший о том что пора принимать пищу, вернул нас в реальность.")

    show mi normal pioneer3 with Fl_fast

    $ Fl.say(Fl_gg, "Ну что, идём кушать?")

    show mi happy pioneer2 with Fl_fast

    $ Fl.say(Fl_mi, "Угу. Я так проголодалась!")
    $ Fl.say(Fl_r, "Придя к единогласному решению, мы отправились в столовую, не забыв закрыть здание музкружка на замок.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopAmbience(4)
    scene bg Fl_black with Fl_dissolve2
    $ Fl.Pause(4.0)

    $ Fl.PlayAmbience("Fl_dining_hall_full", 1, 4)
    scene bg Fl_int_dining_hall_people_day with Fl_dissolve2

    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Подойдя к раздаче, нас повстречала уже знакомая картина - полностью забитая столовая и отсуствие свободных мест.")
    $ Fl.say(Fl_r, "Получив свою заветную порцию мы с Мику пытались глазами найти хоть один свободный столик. Хотя бы возле кого-то сесть бы...")
    $ Fl.say(Fl_r, "И удача оказалась на нашей стороне, как раз пионеры из младших отрядов закончили свою трапезу и оставив поднос пулей выбежали наружу.")
    $ Fl.say(Fl_th, "Повезло-повезло!")
    $ Fl.HideScreens(_with=Fl_fast)


    show Fl_chair3
    show mi normal pioneer3:
        xalign 0.5
        Fl_pris2
    with Fl_dissolve1

    $ Fl.PlayMusic("Fl_bridge_over_stars", 1, 4)
    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_r, "На обед оказалась картошка пюре и рыбная котлета. Я бы не назвал себя фанатом рыбы, но почему-то взглянув на сегодняшний рацион меня накрыла ностальгия по школьным денькам.")
    $ Fl.say(Fl_r, "Ведь кроме как в школе, я нигде не мог отведать рыбной котлеты. {w}И вроде бы мне она нравилась...")

    $ Fl.Pause(3.0)
    $ Fl.say(Fl_th, "Вкусно! {w}Интересно в СССР всегда так вкусно готовили?", _with=hpunch)
    $ Fl.say(Fl_r, "Я посмотрел на Мику.")

    show mi sad pioneer2 with Fl_fast

    $ Fl.say(Fl_r, "Пионерка без какого-либо энтузиазма ковыряла котлету вилкой.")
    $ Fl.say(Fl_gg, "Не любишь рыбу?")

    show mi sad smile pioneer2 with Fl_fast

    $ Fl.say(Fl_mi, "Ага. Просто...")
    $ Fl.say(Fl_gg, "Тогда.{break}")

    show mi shocked pioneer1 with vpunch

    $ Fl.say(Fl_r, "Я ловким движением руки насадил котлету на вилко и отправил прямиком к себе в тарелку.")

    show mi dontlike pioneer1 with Fl_fast

    $ Fl.say(Fl_mi, "Ян, ты зачем мою котлету забрал?!")
    $ Fl.say(Fl_gg, "Ты же сама сказала, что она тебе не нравится...")
    $ Fl.say(Fl_mi, "Да! Но это не повод забирать её себе, может я собиралась её съесть!")

    show mi angry d pioneer1 with Fl_fast

    $ Fl.say(Fl_r, "Мику мило надула щёчки, отводя свои глазки вдругую сторону. {w}Глядя на неё, я не сдержался и рассмеялся. Комичность и схожесть с типичной аниме сценкой сильно подняло мне настроение.")
    $ Fl.say(Fl_r, "Признаться честно мне ещё не доводилось видеть, чтобы Мику на меня злилась. Мне даже казалось, что став её другом, она просто не могла заставить себя показывать недовольство в мой адрес.")
    $ Fl.say(Fl_r, "А сейчас вон сидит и дуется на меня.")
    $ Fl.say(Fl_gg, "Ладно, держи.")
    $ Fl.say(Fl_r, "Я перекинул яблоко раздора обратно Мику, после чего та сразу переменилась в лице.")

    show mi smile pioneer2 with Fl_fast

    $ Fl.say(Fl_r, "Не став зацикливаться над случившимся, я откусил рыбное блюдо. {w}Мику с интересом посмотрела на меня, после чего аккуратно поднесла вилку ко рту.")

    $ Fl.Pause(2.0)

    show mi happy pioneer2 with Fl_fast

    $ Fl.say(Fl_mi, "Мммм. Фкусно!")
    $ Fl.say(Fl_gg, "Хахаха. Мику, не говори с забитым ртом.")
    
    show mi smile pioneer2 with Fl_fast

    $ Fl.say(Fl_mi, "Я говорю вкусно!")
    $ Fl.say(Fl_gg, "Я же говорил!")

    show mi dontlike pioneer1 with Fl_fast

    $ Fl.say(Fl_mi, "Ничего ты мне не говорил. Забрал мою котлету и хотел её слопать!")
    $ Fl.say(Fl_th, "Действительно{mn}")

    show mi normal pioneer3 with Fl_fast

    $ Fl.say(Fl_r, "Мы вернулись к трапезе.")

    $ Fl.Pause(4.0)
    $ Fl.say(Fl_mi, "Ян, а какое твоё самоё любимое блюдо?")
    $ Fl.say(Fl_gg, "Хм{mn} {w}Дай, подумать.")
    $ Fl.say(Fl_th, "Пицца? {w}Паста? {w}Ход-дог? {w}Или шашлык?")

    show Fl_fogging with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Доширак. На другое же тебе денег не хватало, Сударь.")
    $ Fl.say(Fl_th, "Доширак это пища богов, не трогай святое!")
    $ Fl.say(Fl_kvl, "Ну-ну. Как скажешь.")
    hide Fl_fogging with Fl_dissolve1

    $ Fl.Pause(2.0)
    $ Fl.say(Fl_gg, "Наверное пелемени... {w}А твоё?")

    show mi rapture pioneer3 with Fl_fast
    
    $ Fl.say(Fl_mi, "Омурайсу!")
    $ Fl.say(Fl_mi, "Я просто его обожаю. Особенно люблю писать сверху кетчупом разные надписи. Это так весело. Ты обязательно должен попробовать! А точно... Омурайсу это...")
    $ Fl.say(Fl_r, "Мику начала детально рассписывать что из себя представляет это блюдо с необычным названием. {w}Но я и так прекарсно знал, что это популярное японское блюдо, состоящее из жареного риса, покрытого или завернутого в омлет, и украшенное кетчупом.")
    $ Fl.say(Fl_th, "Помню даже пробовал сам его приготовить. Но в итоге омлет порвался, рис вывалился, а надпись слилась. {w}Так что получился чисто русский омлет на завтрак...")

    show mi happy2 pioneer2 with Fl_fast

    $ Fl.say(Fl_mi, "...Ну и воть!")
    $ Fl.say(Fl_r, "Пока я витал в облаках, пионерка закончила свой разказ и выжидала от меня какого-то ответа.")
    $ Fl.say(Fl_th, "Что ещё за «воть»? {w}О чём она говорила, что закончила такой милой формой слова?")
    if Ist_mi == 1:
        $ Fl.HideScreens(_with=Fl_dissolve1)
        menu:
            "Предложить что-нибудь приготовить вместе":
                $ Fl.ShowScreens(_with=Fl_dissolve1)
                $ Fl.say(Fl_gg, "А почему бы нам не приготовить Омурайсу здесь?")

                show mi shocked pioneer1

                $ Fl.say(Fl_mi, "Здесь?!", _with=hpunch)
                $ Fl.say(Fl_gg, "Ну да. Попросим у поваров ингридиенты и приготовим японский омлет.")

                show mi sad pioneer2 with Fl_fast

                $ Fl.say(Fl_mi, "Думаешь, нам разрешат?")
                $ Fl.say(Fl_gg, "Не знаю, но попробовать стоит!")

                show mi smile pioneer2 with Fl_fast

                $ Fl.say(Fl_r, "На лице Мику появилась улыбка. Она, как и я, поверила в то что всё пройдёт гладко и мы сможем насладиться готовкой.")
                $ Fl.say(Fl_r, "Нестав терять времени, мы поспешили опустошить наши тарелки от уже остывшей еды.")
                $ Fl.StopMusic(3)
                $ Fl.StopAmbience(3)
                $ Fl.HideScreens(_with=Fl_dissolve1)


                $ Fl.PlaySound("Fl_pause_time", 1.0, 2, False)
                scene Fl_pause
                with Fl_effect_time_pause

                $ Fl.Pause (3.5)
                scene bg Fl_black with Fl_dissolve2
                $ Fl.Pause (1.5)

                $ Fl.Save("День2: Готовим еду из Джапании")
                $ Fl.DayTime("sunset", "sunset")

                $ Fl.PlayAmbience("Fl_dining_hall_empty", 1, 4)
                scene bg Fl_int_kitchen_day with Fl_dissolve2
                $ Fl.ShowScreens(_with=Fl_dissolve1)
                $ Fl.say(Fl_r, "Кое-как с горем по полам нам всё же удалось уговорить поваров освободить нам помещение на час. И теперь кухня была в нашем расспоряжении.")

                $ Fl.PlayMusic("Fl_doramami2", 1, 6)
                show mi normal pioneer3 with Fl_fast

                $ Fl.say(Fl_gg, "Дамы и господа, мы вас привествуем на японской кухни, сегодня мы будем готовить... {w}Как его там... {w}Омурайсу и нет это не что-то связаное с харакири у самураев, это омлет!")
        
                $ Fl.PlaySound("Fl_mi_laugh", 1, 0, False)
                show mi laugh pioneer1 with Fl_fast

                $ Fl.say(Fl_mi, "Ян, хватит глупостями заниматься!")

                show mi normal pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "Лучше помоги мне нужные ингредиенты отыскать.")
                $ Fl.HideScreens(_with=Fl_fast)
                scene bg Fl_black with blinds


                $ Fl.Pause (2.5)

                scene bg Fl_int_kitchen_day 
                show mi normal pioneer3
                with blinds
                $ Fl.ShowScreens(_with=Fl_dissolve1)
                $ Fl.say(Fl_r, "Перерыв все шкафчики на кухне и даже заглянув в кастрюлю, наши ингридиенты наконец-то лежали на столе, на котором и будет происходить наша готовка.")
                $ Fl.say(Fl_gg, "Ну с чего начнём?")
                $ Fl.say(Fl_mi, "Так для начало разбей яйца и добавь молока.")
                $ Fl.say(Fl_gg, "Куриные?")
                $ Fl.say(Fl_th, "{mn}")

                $ Fl.Pause (1.5)
                $ Fl.say(Fl_th, "М-да{mn} {w}Только я мог задать такой тупой вопрос, <п*здец>...")

                show Fl_fogging with Fl_dissolve1
                $ Fl.say(Fl_kvl, "Да я сам удивляюсь твоей глупости. Какте по-твоему она предложила разбить яйца? Ты ещё спроси молоко чьё?")
                $ Fl.say(Fl_th, "Да понял я уже! {w}Ну ляпнул не подумав, с кем не бывает?")
                $ Fl.say(Fl_kvl, "Ну ладно тебе можно.")
                $ Fl.say(Fl_th, "А вот щас не понял!")
                $ Fl.say(Fl_th, "Это на что ты сейчас намекаешь?")
                $ Fl.say(Fl_r, "Но голос, не собирался отвечать на поставленный вопрос.")
                $ Fl.say(Fl_th, "Ну и правильно, молчи. И так сейчас неловко ещё ты со своим сарказмом.")
                hide Fl_fogging with Fl_dissolve1

                show mi tender5 pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "Ян, конечно куриные! Что за глупые вопросы?")
                $ Fl.say(Fl_gg, "Прости, ляпнул неподумав...")

                show mi normal pioneer3 with Fl_fast

                $ Fl.say(Fl_r, "Взяв в руки, яйца я аккуратно их разбил, после чего выкинул скорлупу в рядом стоящее мусорное ведро.")
                $ Fl.say(Fl_r, "Подлив молока и посолив, я начал взбивать субстанцию до той поры, пока она не превратиться в тесто для нашего омлета.")
                $ Fl.say(Fl_r, "Мику делала тоже самое. {w}Мы решили сделать каждому по порции. {w}Я ей, она мне.")

                show mi joy pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "А у тебя неплохо получается!")
                $ Fl.say(Fl_gg, "Спасибо.")
                $ Fl.say(Fl_r, "Краешки губ приподнялись, слышать похвалу было очень приятно.")

                show mi normal pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "Так теперь подлей масла и вылей яйцо на сковородку. И поджарь его, пока оно не правратиться в румяный блинчик. Вот так!")
                $ Fl.say(Fl_r, "Я повторил всё что мне показала Мику и решил, пока блинчик будет жариться, немного поговорить с пионеркой.")
                $ Fl.say(Fl_gg, "А ты давно готовишь?")

                show mi smile pioneer2 with Fl_fast

                $ Fl.say(Fl_mi, "С самого детства.")

                show mi happy pioneer2 with Fl_fast

                $ Fl.say(Fl_mi, "Я маме всегда помогала готовить.")

                show mi pity grin2 pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "Правда в начале я очень много продуктов переводила и приходилось мои кулинарные творения выкидывать в мусорку.")

                show mi tender pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "Но после нескольких неудач, я смогла научиться готовить! И мы с мамой почти всегда вместе готовим. А иногда даже нам папу удаётся вытащить с дивана к нам на кухню помогать!")
                $ Fl.say(Fl_th, "У неё очень дружная семья... {w}Интересно какая семья была у меня? {w}Наверное у меня были очень добрые и чуткие родители, потому что вряд ли другие позволили бы мне замкнуться в себе и сидеть на шее, погружаясь в творчество.")
                $ Fl.say(Fl_mi, "А однаж{break2}")

                show mi scared pioneer1

                $ Fl.say(Fl_mi, "Ян!", _with=hpunch)
                $ Fl.say(Fl_gg, "Что?")

                $ Fl.Status("-40")
                $ Fl.say(Fl_r, "Мику указала пальцем на сковородку, из которой поднялся столб огня.")

                $ Fl.Status("-5")
                $ Fl.Status("panic", False)
                $ Fl.say(Fl_gg, "ЧЁРТ!", _with=hpunch)
                $ Fl.say(Fl_r, "Взяв сковородку в руки, я закинул её в раковину и поднял кран до самого вверха.")

                show mi pity2 pioneer1 with Fl_fast

                $ Fl.Status("+25")
                $ Fl.Status("normal", False)
                $ Fl.say(Fl_mi, "Ян, будь внимательнее! Мы могли кухню сжечь! А потом бы нам так досталось...")
                $ Fl.say(Fl_gg, "Прости, отвлёкся...")

                show mi normal pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "Ничего, давай я тебе помогу!")
                $ Fl.HideScreens(_with=Fl_dissolve1)


                $ Fl.PlaySound("Fl_pause_time", 1.0, 2, False)
                scene Fl_pause
                with Fl_effect_time_pause

                $ Fl.Pause (3.5)
                scene bg Fl_black with Fl_dissolve2
                $ Fl.Pause (1.5)

                scene bg Fl_int_kitchen_day with Fl_dissolve2
                $ Fl.ShowScreens(_with=Fl_dissolve1)
                $ Fl.Status("+20")
                $ Fl.say(Fl_r, "Пока Мику взбивала яйцо, я отмыл сковородку и теперь под надзором девушки, мне удалось сделать блинчик для нашего омлета.")
                $ Fl.say(Fl_r, "Нашей следующей целью была начинка, состоящая из белого риса и колбасы. {w}Курицу нам конечно повара не собирались отдавать, так что мы быстро нашли замену.")

                show mi normal pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "Ян, я пока сделаю начинку, а ты поищи пожалуйста кетчуп.")
                $ Fl.say(Fl_gg, "Ага.")

                hide mi normal pioneer3 with Fl_fast

                $ Fl.say(Fl_r, "Я начал рыться по ящикам, в надежде отыскать кетчуп времён СССР. Воображение нарисовала его в обычной пласмасовой бутылке с красной крышкой.")

                $ Fl.Pause (3.0)
                $ Fl.say(Fl_r, "Поиски к счастью не затянулись, уже на просмотре второго ящика я нашёл заветный соус. {w}В моих руках находилась бутылка Болгарского кетчупа. Он выглядил так, как я предполагал.")

                show mi normal pioneer3 with Fl_fast

                $ Fl.say(Fl_r, "Я вернулся к пионерки и продемонстрировал свою находку.")
                $ Fl.say(Fl_mi, "Поставь его вон туда. И помоги мне с начинкой. Нужно колбасу нарезать квадратиками.")
                $ Fl.say(Fl_r, "Я кивнул в знак понимания. И взяв нож, принялся за колбасу.")
                $ Fl.HideScreens(_with=Fl_fast)
                scene bg Fl_black with blinds


                $ Fl.Pause (3.5)

                scene bg Fl_int_kitchen_day with blinds
                $ Fl.ShowScreens(_with=Fl_dissolve1)
                $ Fl.say(Fl_r, "С готовкой было покончено. Остался последний штрих сего блюда. {w}Надпись кетчупом!")
                $ Fl.say(Fl_r, "Каждый по очереди написал сверху что-то своё.")
                $ Fl.say(Fl_r, "Мику аккуратно начала выводить какой-то японский иероглиф и тихо хихикала.")
                $ Fl.say(Fl_th, "Сто пудов написала что-то странное...")
                $ Fl.say(Fl_r, "Когда очередь дошла до меня, то я постарался вспомнить хоть что-то на японском. {w}И после долгих размышлений, я написал...")

                $ Fl.Pause (2.5)

                show mi normal pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "Ян, пойдём за столик сядем, а то тут неудобно будет есть.")
                $ Fl.say(Fl_r, "Мику была права, тут не то чтоб поесть негде было, тут развернуться толком негде! {w}Поэтому кивнув я отправился хвостиком за ней.")
                $ Fl.HideScreens(_with=Fl_dissolve1)
                $ Fl.StopMusic(3)
                $ Fl.StopAmbience(3)
                scene bg Fl_black with Fl_effect_5


                $ Fl.Pause (2.5)

                scene bg Fl_int_dining_hall_sunset
                show Fl_chair3
                show mi normal pioneer3:
                    xalign 0.5
                    Fl_pris2
                with Fl_effect_5

                $ Fl.PlayMusic("Fl_bridge_over_stars", 1, 4)
                $ Fl.ShowScreens(_with=Fl_dissolve1)
                $ Fl.say(Fl_mi, "Так! Я буду первой! Ты ведь не против, Ян?")
                $ Fl.say(Fl_gg, "Давай, я не против.")
                $ Fl.say(Fl_r, "Пионерка протянула мне тарелку с омлетом, приготовленного и подписанного лично ей... {w}для меня...")
                $ Fl.say(Fl_r, "Данное блюдо украшала ровная красивая надпись...")

                $ Fl.Pause (2.0)
                if persistent.Fl_dictionary_6 == False:
                    $ Fl.PodskDict()
                $ persistent.Fl_dictionary_6 = True
                $ Fl.say(Fl_th, "{i}Hentai{/i}{mn}", cps="29")

                $ Fl.Pause (1.5)
                $ Fl.say(Fl_gg, "Мику...")
                $ Fl.say(Fl_mi, "Да?")
                $ Fl.say(Fl_gg, "Почему ты сверху написала иероглифами Извращенец?")

                show mi look away pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "Хе-хе.")

                $ Fl.AttackScreens()
                $ Fl.say(Fl_gg, "Эй! Что это ещё за «Хе-хе»?!")
                $ Fl.say(Fl_r, "Мику старалась изобразить, будто ничего не понимает. Но её сдавленные смешки выдавали, игру эмоций пионерки.")

                show mi normal pioneer3 with Fl_fast

                $ Fl.say(Fl_r, "Я не стал на этом зацикливаться. {w}Думаю Мику удалось вызвать у меня нужную реакцию на её выходку.")
                $ Fl.say(Fl_r, "Отломив небольшой кусочек омурайсу, я закинул его рот.")

                $ Fl.Pause (1.5)
                $ Fl.say(Fl_gg, "Чёрт! Мику, это очень вкусно. Ты просто умница!")
                $ Fl.say(Fl_r, "Распробовав данное блюдо, я набросился на него, попутно рассхваливая Мику. {w}А иероглифы, написанные кетчупом, вовсе вылетеле из головы.")

                show mi shy pioneer1 with Fl_fast

                $ Fl.say(Fl_mi, "Тебе правда понравилось?")
                $ Fl.say(Fl_gg, "Мгх. Уху.")
                $ Fl.say(Fl_r, "С набитым ртом ответил я.")
                $ Fl.say(Fl_th, "А ведь кто-то сегодня отчитывал Мику, а сам вон сижу как хомяк с полным ртом.")

                show mi grin pioneer2 with Fl_fast

                $ Fl.say(Fl_mi, "А мне мама всегда говорила, что путь к сердцу мужчины лежит через желудок.")

                show mi shy pioneer1 with Fl_fast

                $ Fl.say(Fl_mi, "Ой, прости. Ты не подумай! Просто...")
                $ Fl.say(Fl_gg, "Всё нормально. Но ты и правда вкусно готовишь!")

                show mi happy pioneer2 with Fl_fast

                $ Fl.say(Fl_mi, "Спасибо, мне очень приятно это слышать. Эти слова очень много для меня значат!")

                $ Fl.Pause (2.0)
                $ Fl.say(Fl_th, "Много значат{mn}")
                $ Fl.HideScreens()
                $ Fl.StopMusic()


                $ Fl.PlaySound("Fl_flashback", 1.0, 0, False)
                scene bg Fl_int_house_of_un_ceiling_rain
                show Fl_prolog_dream
                with Fl_flash_fast

                $ Fl.ShowScreens(_with=Fl_fast)
                $ Fl.say(Fl_gg, "Эти слова так много для тебя значат?")
                $ Fl.say(Fl_r, "Осторожно поинтересовался я.")
                $ Fl.say(Fl_mi, "Конечно, ведь ты ответил взаимно на мои чувства!")
                $ Fl.HideScreens()


                $ Fl.PlaySound("Fl_flashback", 1.0, 0, False)
                scene bg Fl_int_dining_hall_sunset
                show mi happy pioneer2:
                    xalign 0.5
                    Fl_pris2
                with Fl_flash_fast

                $ Fl.PlayMusic("Fl_bridge_over_stars", 1, 6)
                $ Fl.Pause (1.5)
                $ Fl.Status("-20")
                $ Fl.ShowScreens(_with=Fl_dissolve1)
                $ Fl.say(Fl_r, "Перед глаза всплыли флешбеки прошлой ночи. Когда Мику признавалась мне в любви.")
                $ Fl.say(Fl_th, "Интересно Мику помнит о вчерашнем? {w}Или старается мастерски скрыть чтобы не показаться слабой. {w}А может и вовсе ждёт от меня каких-то действий.")
                $ Fl.say(Fl_r, "Внутри всё сжалось. Чувство вины взяло вверх. Я не мог перестать думать о случившемся прошлой ночью. Казалось что я вновь играю на чувствах пионерки. {w}От чего моментально становится тошно.")

                show mi sad pioneer2 with Fl_fast

                $ Fl.say(Fl_mi, "Ян, что-то не так?")

                $ Fl.Status("+10")
                $ Fl.say(Fl_gg, "А? {w}Нет, всё в порядке. Просто задумался.")
                $ Fl.say(Fl_gg, "Кстати, теперь моя очередь презентовать свой омурайсу.")

                show mi smile pioneer2 with Fl_fast

                $ Fl.say(Fl_r, "От былой печали Мику простыл след, теперь она смотрела на меня с широкой улыбкой, в ожидании посмотреть на мои плоды кулинарии. Мне удалось сменить тему и свести беспокойство девушки на нет.")
                $ Fl.say(Fl_gg, "Вуаля. Кушать подано, моя принцесса!")
                $ Fl.say(Fl_r, "Сказал я, войдя в роль какого-то дворецкого. {w}В голове нарисовалась забавная сцена. Где я в костюме протягиваю блюдо, скрытое в баранчике, для Мику, которая одета в пышном платьице и с короной на голове.")
                $ Fl.say(Fl_th, "Хотя если приглядеться, то Мику и правда похожа на принцессу...")

                show mi pity pioneer1 with Fl_fast

                $ Fl.say(Fl_mi, "Ян, ты чего? Неужели я и правда похожа на принцессу?")
                $ Fl.say(Fl_gg, "Эм{mn} {w}Ну да...")
                $ Fl.say(Fl_th, "Молодец! Сам же ляпнул что-то, а теперь еле два слова могу связать! {w}Да я прям альфач, ничего не скажешь!")

                show mi pity grin pioneer2 with Fl_fast

                $ Fl.say(Fl_mi, "Ян, да что на тебя нашло? Сегодня весь день то и дело, что меня хвалишь...")
                $ Fl.say(Fl_gg, "Потому что есть за что! Ты и правда нечто, не перестаю удивляться тебе!")

                show Fl_fogging with Fl_dissolve1
                $ Fl.say(Fl_kvl, "{b}Нечто{/b} - это ещё слабо сказано.")
                $ Fl.say(Fl_th, "Тут ты прав. Особенно после вчерашнего...")
                $ Fl.say(Fl_kvl, "И про утрений инцедент не забывай, Сударь.")
                hide Fl_fogging with Fl_dissolve1

                show mi grin pioneer2 with Fl_fast

                $ Fl.say(Fl_mi, "Ян, да ты просто льстец!")
                $ Fl.say(Fl_r, "Сказала Мику и перевела взгляд на рядом стоящую тарелку. После чего сразу же рассмеялась.")

                $ Fl.PlaySound("Fl_mi_laugh", 1, 0, False)
                show mi laugh pioneer1

                $ Fl.Pause (1.5)
                $ Fl.say(Fl_mi, "Ян, что это?")
                $ Fl.say(Fl_r, "Пионерка тыкнула пальцем на омлет, сверху которого кетчупом был нарисован смайлик виде неко.")
                $ Fl.say(Fl_th, "Да я ничего лучше не придумал, чем нарисовать милый смайлик. Всё же мой японский не выходил за рамки аниме и хентая, поэтому ничего нормально мне в голову не пришло написать.")
                $ Fl.say(Fl_gg, "Хватит уже смеяться. Я в отличие от некоторых не писал обзывательства на еде!")

                $ Fl.PlaySound("Fl_mi_laugh", 1, 0, False)
                $ Fl.say(Fl_mi, "Прости. Но это правда забавно...")

                show mi normal pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "И очень мило.")

                $ persistent.Fl_dostn_11 = True
                show Fl_dost_11_in_kod:
                    xalign -1.0 yalign 0.7
                show Fl_dost_11_in_kod:
                    ease 1.0 xalign 0.01
                $ Fl.Pause(0.5)
                $ Fl.PlaySound("Fl_achievement", 1, 0, False)
                $ Fl.Pause(1.5)
                hide Fl_dost_11_in_kod with Fl_dissolve1

                $ Fl.say(Fl_r, "Мику откусила небольшой кусочек, после чего сразу высказа свою критику.")
                $ Fl.say(Fl_mi, "Вкусно!")
                $ Fl.say(Fl_r, "На что я лишь улыбнулся. И продолжил уже ковырять свой омлет.")
                $ Fl.HideScreens(_with=Fl_fast)
                scene bg Fl_black with Fl_dissolve1



                $ Ist_mi += 1


                $ Fl.Pause (4.5)
                $ Fl.Save("День2: Мику не хочет меня отпускать")

                scene bg Fl_int_dining_hall_sunset with Fl_dissolve1
                $ Fl.Pause (1.0)
                $ Fl.ShowScreens(_with=Fl_dissolve1)
                $ Fl.say(Fl_r, "Трудно сказать, сколько времени прошло за нашим совместным обедом. Но после долгой продолжительной беседы, наши тарелки наконец-то опустели.")
                $ Fl.say(Fl_r, "Мы решили не задерживаться. Помыв за собой посуду, мы отправились на выход.")
                $ Fl.HideScreens(_with=Fl_fast)
                $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
                $ Fl.StopMusic(3)
                scene bg Fl_black with Fl_effect_1


                $ Fl.Pause (2.0)

                scene bg Fl_ext_dining_hall_near_sunset
                show Fl_light_c 
                with Fl_effect_1
                $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 2)
                $ Fl.Pause (1.0)
                $ Fl.ShowScreens(_with=Fl_dissolve1)
                $ Fl.say(Fl_gg, "Ладно, Мику, я пойду. Мне ещё к вожатой нужно зайти за формой.")

                show mi shy pioneer1 with Fl_fast
                $ Fl.say(Fl_mi, "Ян, подожди...", cps="28")

                $ Fl.PlayMusic("Fl_niles_blues", 1, 2)
                $ Fl.say(Fl_r, "Мику взяла меня за руку и мило улыбнулась, нескрывая свои красные щёки.")
                $ Fl.say(Fl_r, "Как и вчера её руки оказались очень тёплыми. {w}Кажется, что я вот вот могу обжечься в любой момент только от одного её касания.")
                $ Fl.say(Fl_mi, "Ты не мог бы сходить со мной в музклуб. Это ненадолго обещаю!", cps="35")
                $ Fl.say(Fl_gg, "Мику, меня и правда ждёт вожатая, прости.")

                show mi pity grin2 pioneer3 with Fl_fast
                $ Fl.say(Fl_mi, "Ну пожалуйста!", cps="31")

                show mi sad3 pioneer3 with Fl_fast
                $ Fl.say(Fl_mi, "Это ненадолго! Мне просто... нужно кое-что... Прости, не могу сейчас сказать.", cps="31")

                show mi pity grin2 pioneer3 with Fl_fast
                $ Fl.say(Fl_mi, "Ян, вожатая может подождать, правда?", cps="31")
                $ Fl.say(Fl_r, "Мику состроила щенячьи глазки.")
                $ Fl.say(Fl_th, "Неплохая провокация, Мику.")
                $ Fl.say(Fl_gg, "Ладно пошли в музклуб, если ты так настаиваешь.")

                show Fl_fogging with Fl_dissolve1
                $ Fl.say(Fl_kvl, "Провакация, на которую ты купился. Поздравляю, Сударь!")
                $ Fl.say(Fl_th, "Ну не могу я ей отказать, когда она так просит!")
                $ Fl.say(Fl_kvl, "А ты хоть головой подумал для чего она так настаивает, чтобы ты пошёл к ней в клуб?")
                $ Fl.say(Fl_th, "Да знаю я к чему ты клонишь. Но за весь день она никак не проявила свою яндерную сторону, тебе это не кажется странным?")
                $ Fl.say(Fl_kvl, "Мне то кажется, а вот тебе походу нет!")
                $ Fl.say(Fl_kvl, "Я ведь не шутил, что она опасна и всё что было утром это не простой глюк! {w}Но ты конечно никого не станешь слушать, будешь дальше вертеться вокруг Мику и игнорировать меня!")
                $ Fl.say(Fl_th, "Не парься, я всегда на готове. Если она вдруг и {u}правда{/u} станет одержимой, то быстро решу как мне быть.")
                $ Fl.say(Fl_kvl, "Да-да. Ну как скажешь...")
                hide Fl_fogging with Fl_dissolve1

                show mi smile pioneer2 with Fl_fast

                $ Fl.say(Fl_r, "Своими словами я смог заставить пионерку вновь одарить меня искренней улыбкой. {w}Эта улыбка согрела моё замёрзшее сердце, из-за чего то приятно кольнуло внутри. {w}Эта улыбка - единственное что хотелось видеть в данный момент.")
                
                $ Fl.Pause (1.5)
                $ Fl.say(Fl_th, "Я хочу чтобы она почаще улыбалась...")
                $ Fl.HideScreens(_with=Fl_dissolve1)
                $ Fl.StopMusic(2)
                scene bg Fl_black with Fl_dissolve2


                $ Fl.Pause (3.0)

                scene bg Fl_ext_musclub_sunset
                show Fl_light_c 
                with Fl_dissolve2
                $ Fl.Pause (1.0)
                $ Fl.ShowScreens(_with=Fl_dissolve1)
                $ Fl.say(Fl_r, "Мы всё ближе подходили к музклубу. {w}И я только сейчас понял, что ни разу не видел это здание в лучах солнца. Вчера мы сильно засиделись и возможности полюбоваться пейзажом под красно-оранжевым фильтром у меня не было.")
                $ Fl.HideScreens(_with=Fl_fast)

                $ Fl.PlaySound("Fl_walk2", 1, 0, False)
                scene bg Fl_ext_musclub_sunset:
                    ease 2.5 zoom 1.7 xalign 0.6 yalign 0.43
                $ Fl.Pause (2.5)
                scene bg Fl_ext_musclub_verandah_sunset with Fl_fast
                $ Fl.Pause (1.0)
                $ Fl.PlaySound("Fl_open_door_2", 1, 0, False)
                scene bg Fl_black with Fl_fast

                $ Fl.Pause (1.0)
                scene bg Fl_int_musclub_mattresses_sunset with Fl_dissolve1

                $ Fl.Pause (1.0)
                $ Fl.PlayMusic("Fl_Rokudenashi_Majutsu_Koushi_to_Akashic_Records_OST", 1, 6)
                show mi happy pioneer2 with Fl_dissolve1

                $ Fl.ShowScreens(_with=Fl_fast)
                $ Fl.say(Fl_mi, "Ян, жди здесь и никуда не уходи!")
                $ Fl.say(Fl_gg, "Да я нику...{break}")

                $ Fl.PlaySound("Fl_walk2", 1, 0, False)
                hide mi happy pioneer2 with easeoutleft

                $ Fl.say(Fl_r, "Не успел я договорить, как аквамариновая пионерка убежала в клодовую.")
                $ Fl.say(Fl_th, "Интересно, какие тайны хранит эта кладовая. Сколько бы Мику туда не бегала вечно что-то интересное притаскивала.")

                show Fl_fogging with Fl_dissolve1
                $ Fl.say(Fl_kvl, "Коллекцию ножей.")
                $ Fl.say(Fl_th, "Ага. По акции ухватила. Набор для юных Яндер, блин!")
                $ Fl.HideScreens(_with=Fl_fast)
                hide Fl_fogging with Fl_dissolve1


                $ Fl.Pause (2.5)
                show mi joy pioneer3 with easeinleft

                $ Fl.ShowScreens(_with=Fl_fast)
                $ Fl.say(Fl_mi, "А вот и я!")
                $ Fl.say(Fl_r, "Торжественно произнеся, пыталась что-то спрятать за спиной Мику. {w}Это «что-то» имелло прямоугольную форму и отдалённо напоминало тоненькую книженцию или тетрадь.")
                $ Fl.say(Fl_gg, "Мику, что ты там прячешь за спиной?")

                show mi pity grin2 pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "Ничего.")
                $ Fl.say(Fl_th, "Неужели это додзинси с юри?")
                $ Fl.say(Fl_r, "Попытался глупо отшутиться я у себя в голове.")
                $ Fl.say(Fl_mi, "Ян{mn}")
                $ Fl.say(Fl_mi, "Возможно, тебе это будет не интересно или даже не нужно...")
                $ Fl.say(Fl_mi, "Но возьми её пожалуйста!")
                $ Fl.say(Fl_r, "Мику протянула мне тетрадь, на обложке которой были изображены принты с котиками.")
                $ Fl.say(Fl_th, "Да, всё же мои догадки были верны. Это и правда оказалась тетрадка.")
                $ Fl.say(Fl_gg, "Что это?")

                show mi shy4 pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "А ты открой.")
                $ Fl.say(Fl_r, "Я послушно перевернул обложку. На первой странице меня встретила следующая надпись: «Мои собственные композиции» и чуть ниже «Хатсунэ Мику».")
                $ Fl.say(Fl_th, "Не может быть это...")
                $ Fl.say(Fl_r, "Я перевернул следующую страницу. {w}И ещё одну. {w}И ещё. {w}Все станицы представляли собой ноты для разных инструментов. И даже были табы для гитары!")
                $ Fl.say(Fl_gg, "Мику, у меня слов нет. {w}Спасибо, но почему ты раньше не говорила, что у тебя есть целая тетрадь с авторскими композициями?")
                $ Fl.say(Fl_mi, "Ну я думала, вдруг тебе не понравится или не интересно будет. Там гитары немного, но тоже есть. А ты у нас на гитаре играешь.")
                $ Fl.say(Fl_gg, "Ты шутишь? Это ведь здорово!")
                $ Fl.say(Fl_r, "Творчество это моё хобби и моя слабость. Как только что-то касается его, то я начинаю вести себя словно маленький ребёнок, как сейчас.")

                show mi joy pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "Правда? {w}Я рада!")
                $ Fl.say(Fl_gg, "Как прочитаю обязательно верну!")

                show mi normal pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "Не надо. Я ведь её тебе подарить хотела, просто засмушалась.")
                $ Fl.say(Fl_gg, "Подарить?..")
                $ Fl.say(Fl_mi, "Угу.")
                $ Fl.say(Fl_gg, "Но разве тебе эта вещь не дорога? Всё же как никак там все твои песни.")
                $ Fl.say(Fl_mi, "Не волнуйся, они старые. Я их все наизусть знаю.")
                $ Fl.say(Fl_th, "Не могу поверить, что Мику отдала мне столь ценный предмет. {w}У неё явно не один год ушёл на заполнение тетрадки 48 листов.")
                $ Fl.say(Fl_mi, "Точно, Ян ты же к вожатой собирался, а я тебя тут задерживаю.")
                $ Fl.say(Fl_gg, "Да ничего. Я не тороплюсь.")
                $ Fl.say(Fl_th, "Сказал тот, кто у столовой очень спешил и не собирался идти с Мику.")

                show mi look away pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "Я была бы, конечно, рада чтобы ты остался.")

                show mi smile pioneer2 with Fl_fast

                $ Fl.say(Fl_mi, "Но ты так до конца смены настоящим пионером не станешь.")
                $ Fl.say(Fl_r, "Намекнула Мику, бросив взгляд на мою футболку с джинсами.")
                $ Fl.say(Fl_gg, "Твоя правда.")
                $ Fl.say(Fl_gg, "Ну тогда до встречи?")

                show mi happy pioneer2 with Fl_fast

                $ Fl.say(Fl_mi, "Конечно!")

                show mi normal pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "И обязательно загляни в раздел с гитарой, я там много интересных песен написала.")
                $ Fl.say(Fl_r, "Я удовлетворительно кивнул головой и отправился становиться настоящим пионером.")
                $ Fl.StopMusic(4)
                $ Fl.HideScreens(_with=Fl_dissolve1)
                scene bg Fl_black with Fl_dissolve2
                
                
                $ Fl.Pause(5.0)

                $ add_mi += 1





            "Сменить тему":
                $ Fl.ShowScreens(_with=Fl_dissolve1)
                $ Fl.DayTime("day", "day")
                $ Fl.say(Fl_gg, "А точно! Хотел спросить. Мику, а ты хоть раз готовила сама?")

                show mi confusion pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "А?")

                show mi normal pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "Конечно! Мы с мамой почти всегда вместе готовим. Я ещё с детства помогала маме в готовке.")

                show mi joy2 pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "Правда, один раз чуть пожар не устроила...")

                show mi normal pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "Ну это неважно! Я очень долго училась готовить. По началу у меня ничего не получалось и много продуктов приходилось выкидывать, но мама всё понимала и не злилась...")
                $ Fl.HideScreens(_with=Fl_fast)
                scene bg Fl_black with Fl_dissolve1


                $ Fl.Pause (4.5)
                $ Fl.Save("День2: Мику не хочет меня отпускать")

                scene bg Fl_int_dining_hall_sunset with Fl_dissolve1
                $ Fl.DayTime("sunset", "sunset")
                $ Fl.Pause (1.0)
                $ Fl.ShowScreens(_with=Fl_dissolve1)
                $ Fl.say(Fl_r, "Трудно сказать, сколько времени прошло за нашим совместным обедом. Но после долгой продолжительной беседы, наши тарелки наконец-то опустели.")
                $ Fl.say(Fl_r, "Мы решили не задерживаться. Помыв за собой посуду, мы отправились на выход.")
                $ Fl.HideScreens(_with=Fl_fast)
                $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
                $ Fl.StopMusic(3)
                scene bg Fl_black with Fl_effect_1


                $ Fl.Pause (2.0)

                scene bg Fl_ext_dining_hall_near_sunset
                show Fl_light_c 
                with Fl_effect_1
                $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 2)
                $ Fl.Pause (1.0)
                $ Fl.ShowScreens(_with=Fl_dissolve1)
                $ Fl.say(Fl_gg, "Ладно, Мику, я пойду. Мне ещё к вожатой нужно зайти за формой.")

                show mi shy pioneer1 with Fl_fast
                $ Fl.say(Fl_mi, "Ян, подожди...", cps="28")

                $ Fl.PlayMusic("Fl_niles_blues", 1, 2)
                $ Fl.say(Fl_r, "Мику взяла меня за руку и мило улыбнулась, нескрывая свои красные щёки.")
                $ Fl.say(Fl_r, "Как и вчера её руки оказались очень тёплыми. {w}Кажется, что я вот вот могу обжечься в любой момент только от её касания.")
                $ Fl.say(Fl_mi, "Ты не мог бы сходить со мной в музклуб. Это ненадолго обещаю!", cps="31")
                $ Fl.say(Fl_gg, "Мику, меня и правда ждёт вожатая, прости.")

                show mi pity grin2 pioneer3 with Fl_fast
                $ Fl.say(Fl_mi, "Ну пожалуйста!", cps="31")

                show mi sad3 pioneer3 with Fl_fast
                $ Fl.say(Fl_mi, "Это правда ненадолго! Мне просто... нужно кое-что... Прости, не могу сейчас сказать.", cps="31")

                show mi pity grin2 pioneer3 with Fl_fast

                $ Fl.say(Fl_mi, "Ян, вожатая может подождать, правда?", cps="31")
                $ Fl.say(Fl_gg, "Прости, но если я сегодня не надену форму, то вожатая такое со мной сделает, что даже страшно представить.")
                $ Fl.say(Fl_r, "Частично это была правда.")

                show mi pity grin pioneer2 with Fl_fast

                $ Fl.say(Fl_mi, "Ладно...")

                show mi sad smile pioneer2 with Fl_fast

                $ Fl.say(Fl_mi, "Тогда ты сможешь зайти, как освободишься?")
                $ Fl.say(Fl_gg, "Конечно, без проблем.")

                hide mi sad smile pioneer2 with Fl_dissolve1
                $ Fl.StopMusic(5)

                $ Fl.say(Fl_r, "Мику улыбнулась на прощание и пошла в сторону музклуба. {w}Стоило пионерке пройти пару шагов, как от её улыбки не осталось и следа.")
                $ Fl.say(Fl_r, "Я хотел было её окликнуть, но та уже быстро скрылась за поворотом.")
                $ Fl.say(Fl_th, "Может всё же стоило пойти за ней...")
                $ Fl.say(Fl_r, "Подумал я. {w}Накручивать себя у меня не было ни малейшего желания. {w}Поэтому я решил не стоять без дела, а наконец-то покончить с этой долбаной формой, которую уже какой день не могу забрать.")
                $ Fl.HideScreens(_with=Fl_dissolve1)
                scene bg Fl_black with Fl_dissolve2
                
                
                $ Fl.Pause(5.0)
                

                $ add_mi += 1






    else:
        $ Fl.DayTime("day", "day")
        $ Fl.say(Fl_gg, "А точно, чуть не забыл!")

        show mi confusion pioneer3 with Fl_fast

        $ Fl.say(Fl_gg, "Мику ты знала что мы теперь с тобой в одном домике живём?")

        show mi normal pioneer3 with Fl_fast

        $ Fl.say(Fl_mi, "Знаю, мне вожатая после линейки рассказала.")
        $ Fl.say(Fl_th, "Интересная логика у вожатой. В начале рассказать Мику о новом соседе, а потом уже этому соседу ключи выдать.")
        $ Fl.say(Fl_mi, "Мы теперь живём вместе, правда здорово?")
        $ Fl.say(Fl_gg, "Ага, наверное...")
        $ Fl.say(Fl_r, "Неожиданно в столовой раздался крик, и я машинально повернул голову к источнику.")
        $ Fl.StopMusic()
        $ Fl.HideScreens(_with=Fl_fast)

        $ Fl.PlaySound("Fl_swipe", 1.0, 0, False)
        $ persistent.Fl_photo_pallery_7 = True
        scene cg Fl_msk_canteen_rage with pushright

        $ Fl.PlayMusic("Fl_demilitarized_zone", 1, 0)
        $ Fl.ShowScreens(_with=Fl_fast)
        $ Fl.Master(Fl_screen_attack_hard)
        $ Fl.say(Fl_msk, "ТАК <БЛ*ТЬ>!", master=Fl_screen_attack, _with=vpunch)
        $ Fl.Master(Fl_screen_attack_hard)
        $ Fl.say(Fl_msk, "ТОЛЯН, КАКОГО ХРЕНА «ЭТО» У МЕНЯ В ТАРЕЛКЕ?!", master=Fl_screen_attack, _with=vpunch)
        $ Fl.say(Fl_th, "Интересно что на этот раз Толян выкинул, что Миха на всю столовку орёт?")
        $ Fl.HideScreens(_with=Fl_fast)

        scene bg Fl_int_dining_hall_people_day with blinds
        show msk sad shirt with Fl_fast:
            fleft
        show to cry pioneer with Fl_fast:
            yalign 0.5 xalign 0.25

        $ Fl.ShowScreens(_with=Fl_fast)
        $ Fl.say(Fl_r, "Позади нас стоял разъярённый Михалыч и Толян. На его лице были слёзы. То ли из-за вины содеянного, то ли из-за того что на него накричали.")

        hide to cry pioneer with moveoutright
        $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)

        $ Fl.say(Fl_r, "Толян тут же рванул прочь из столовой.")

        hide msk sad shirt with moveoutright
        $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)

        $ Fl.say(Fl_r, "А Миха, всё ещё не сбавляя гнева, следом за ним.")
        $ Fl.StopMusic(3)
        $ Fl.say(Fl_th, "Да уж. Весело.")

        show mi confusion pioneer3:
            xalign 0.5
            Fl_pris2
        with Fl_dissolve1
        $ Fl.PlayMusic("Fl_bridge_over_stars", 1, 3)

        $ Fl.say(Fl_r, "Я повернулся обратно к Мику. Которая безразлично ковырялась в своей тарелке. Казалось что всё происходящее её нисколечки не интересовало.")
        $ Fl.say(Fl_gg, "Так на чём мы остановились?")

        show mi normal pioneer3 with Fl_fast
        $ Fl.say(Fl_r, "Задав литорический вопрос, я сразу же привлёк внимание пионерки.")
        $ Fl.say(Fl_gg, "На домике...")
        $ Fl.say(Fl_r, "Я поправил карман джинс. {w}И рукой нашупал ключ?")
        $ Fl.say(Fl_th, "Стоп. Это ведь ключ Мику. Я ведь так и не вернул его.")
        $ Fl.say(Fl_gg, "Мику, это случайно не твой ключ?")

        show mi smile pioneer2 with Fl_fast
        $ Fl.say(Fl_mi, "Мой! А где ты его нашёл?")
        $ Fl.say(Fl_gg, "Ну...")
        $ Fl.say(Fl_th, "Ну как сказать... {w}Я просто по чистой случайности прихватил его пока одевался, а потом благодаря ему смог сбежать от Яндерки-Мику.")
        $ Fl.say(Fl_r, "Но я решил упустить этот момент и просто соврал.")
        $ Fl.say(Fl_gg, "Он на ступеньках валялся, вот подумал, что наверное ты его потеряла.")

        show mi happy pioneer2 with Fl_fast

        $ Fl.say(Fl_mi, "Спасибо тебе большое, что нашёл его.")

        show mi sad2 pioneer2 with Fl_fast

        $ Fl.say(Fl_mi, "Иначе мне бы Марина Владимировна такой выговор сделала бы...")
        $ Fl.say(Fl_gg, "Ну хорошо, что всё обошлось.")
        $ Fl.say(Fl_r, "Попытался я подбодрить Мику.")

        show mi smile pioneer2 with Fl_fast

        $ Fl.say(Fl_mi, "Угу.")
        $ Fl.HideScreens(_with=Fl_dissolve1)
        $ Fl.StopMusic(3)


        $ Fl.PlaySound("Fl_pause_time", 1.0, 2, False)
        scene Fl_pause
        with Fl_effect_time_pause

        $ Fl.Pause (3.5)
        scene bg Fl_black with Fl_dissolve2
        $ Fl.Pause (1.5)

        scene bg Fl_int_dining_hall_people_day with Fl_dissolve2
        $ Fl.ShowScreens(_with=Fl_dissolve1)
        $ Fl.say(Fl_r, "Быстро покончив с едой, я вспомнил об одном очень важном деле.")
        $ Fl.say(Fl_gg, "Мику, ну я пойду. Меня Марина Владимировна просила зайти после обеда к ней за формой.")

        show mi sad3 pioneer3 with Fl_fast

        $ Fl.say(Fl_mi, "Ладно...")
        $ Fl.say(Fl_r, "Мику опустила взгляд на тарелку и молча продолжила водить вилкой по тарелке.")
        $ Fl.say(Fl_r, "А я быстрым шагом направился к выходу.")
        $ Fl.StopAmbience(3)
        $ Fl.HideScreens(_with=Fl_dissolve1)
        scene bg Fl_black with Fl_dissolve2
                
                
        $ Fl.Pause(5.0)


    if add_mi == 1:
        $ Fl.Pause(0.1)
    else:
        $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 2)
    scene bg Fl_house_of_mt_sunset
    show Fl_light_c 
    with Fl_effect_mosaic
    $ Fl.Pause (1.5)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.AutoSave()
    $ Fl.say(Fl_r, "Путь до домика вожатой не занял много времени. {w}За два дня я уже более менее освоился в лагере. И приблизительно знал где что находится.")
    $ Fl.say(Fl_r, "И наудивление этому поспособствовал обходной лист с Михалычем.")

    $ Fl.Pause (2.0)
    $ Fl.say(Fl_r, "Нестав терять ни минуты, я подошёл к двери и постучался.")
    $ Fl.HideScreens(_with=Fl_fast)


    $ Fl.PlaySound("Fl_walk2", 1, 0, False)
    $ Fl.Pause (1.5)
    $ Fl.PlaySound ("Fl_door_knock", 1, 0, False)

    $ Fl.Pause (1.5)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_th, "А в ответ тишина...")
    $ Fl.say(Fl_r, "Идти куда-то не было никакого желания, поэтому я решил зайти внутрь и подождать, когда вожатая нагуляется.")
    $ Fl.HideScreens(_with=Fl_fast)
    $ Fl.Pause (1.0)
    call screen Fl_house_of_mt_sunset_clicked with Fl_fast
    screen Fl_house_of_mt_sunset_clicked:
        tag menu
        modal True
        add "images/bg/Fl_house_of_mt_sunset.jpg"
        text ["{font=[Fl_Script]}Наведите на объект{/font}"]:
            size 50
            ypos 30
            xalign 0.967
        imagebutton:
            xalign 0.384 ypos 426
            auto "images/objects/Fl_house_of_mt_sunset_clicked_%s.png"
            hover_sound "gui/main_menu/Fl_click_menu.mp3"
            action Hide("Fl_house_of_mt_sunset_clicked"), Return()
                    
    $ Fl.PlaySound("Fl_open_door_2", 1, 0, False)
    scene bg Fl_int_house_of_mv_sunset with Fl_flash:
        subpixel True
        zoom 1.4 xalign 0.5 yalign 0.5 alpha 1.0
        ease 5 zoom 1.0 xalign 0.5 yalign 0.5 alpha 1.0
            

    $ Fl.Save("День2: Тихий час")
    $ Fl.Pause (2.5)

    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_gg, "И где она вечно шляется?")

    scene bg Fl_int_house_of_mv_sunset:
        Fl_bg_zoom_th(1.0, 1.5, 1.5, 0.5, 0.2, 0.5, 0.55)
    $ Fl.Pause (1.5)
    $ Fl.PlaySound("Fl_bed_squeak", 1, 0, False)
    $ Fl.AttackMaster(False)
    $ Fl.say(Fl_r, "Я присел на середину левой кровати. Потому что если я не ошибаюсь, то кровать напротив принадлежит вожатой. На мои выводы рассуждения намекает ещё белый лифчик, одиноко свысавший на перилах.")
    
    $ Fl.ShowBlinking()
    $ Fl.Status("-35")
    $ Fl.Status("dream", False)
    $ Fl.say(Fl_r, "Неожиданно всё моё тело обмякло. {w}Только сейчас я смог осознать, что полностью вымотался. Сил совсем не было. Каждая частичка моего дряхлого тела молила об отдыхе. И как назло кровать стала неестесвенно мягкой, словно пух.")
    
    $ Fl.PlaySound("Fl_bed_squeak", 1, 0, False)
    $ Fl.say(Fl_r, "Подняв белый флаг перед сонливостью, я улёгся на кровать.")
    $ Fl.HideScreens(_with=Fl_fast)


    $ Fl.HideBlinking()
    $ Fl.Pause (0.3)
    $ Fl.ShowBlink()
    $ Fl.Pause (3.0)

    $ Fl.ShowScreens(_with=Fl_fast)
    $ Fl.say(Fl_kvl, "Сударь, ты решил прямо здесь лечь спать? А как же вожатая?")
    $ Fl.say(Fl_th, "А что вожатая?")
    $ Fl.say(Fl_kvl, "Как ты думаешь, что она подумает, когда застукает тебя, спящего у неё в домике?")
    $ Fl.say(Fl_kvl, "Сто процентов примет тебя за извращенца. {w}Хотя{mn} {w}Она ещё в первый день приняла тебя за него.")
    $ Fl.say(Fl_th, "Закончил?")
    $ Fl.say(Fl_kvl, "Да.")
    $ Fl.say(Fl_th, "Вот и отлично. Спокойной ночи.")
    $ Fl.say(Fl_r, "Голос ещё что-то пытался мне сказать, но мой мозг не смог осмыслить ни единого слова.")
    $ Fl.say(Fl_r, "Пытаясь переварить кашу в голове, мой разум оконательно сдался и погрузился в объятия морфея.")
    $ Fl.StopAmbience(4)
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    if Ist_mi >= 2:
        $ Fl.Status("")
        $ Fl.Save("День2: Неко-Мику, фулла не будет")            
        $ Fl.Pause(9.0)
        $ Fl.HideBlink()
        $ Fl.DayTime("rain", "rain")


        $ persistent.Fl_photo_pallery_8 = True
        scene cg Fl_catmiku:
            subpixel True
            truecenter
            yalign 0.85
            zoom 1.3
            ease 10.0 yalign 0.1 zoom 1.0
        show Fl_prolog_dream:
            alpha 0.45
        with Fl_dissolve2

        $ Fl.Pause (3.0)
        $ Fl.ShowScreens(_with=Fl_dissolve1)
        $ Fl.PlayMusic("Fl_fogive_me", 1, 15)
        $ Fl.say(Fl_r, "Мику сидит на мне верхом, без капли стеснения, не смотря на то, что на ней нет одежды. А на голове у неё красуется пара кошачьих ушек.")
        $ Fl.say(Fl_r, "Она смотрит мне прямо в глаза со смесью смущения и веселья. Её длинные волосы, спускаются мне на живот, скрывая всё интересное. Но даже так это зрелище сводит меня с ума.")
        $ Fl.say(Fl_gg, "Мику...")
        $ Fl.say(Fl_mi, "Янечка... Ой, то есть хозяин. Вы проснулись, ня?")
        $ Fl.say(Fl_gg, "Хозяин...")
        $ Fl.say(Fl_r, "Но не успел я договорить, как почувствовал тяжесть ниже живота.")

        $ Fl.AttackScreens()
        $ Fl.say(Fl_mi, "НЯ!!!")
        $ Fl.say(Fl_r, "Мику опустила взгляд вниз, после чего её щеки воспылали, а на лице появилась хитрая ухмылка.")
        $ Fl.say(Fl_mi, "Хозяин, вы такой извращенец. Неужели вас завело моё тело?")
        $ Fl.say(Fl_r, "Сказала Мику с ехидным взглядом, демонстрируя свою фигуру проводя ладонями по своей груди.")
        $ Fl.say(Fl_r, "Руки неко(Мику) плавно опустились на мой торс.")
        $ Fl.say(Fl_r, "Медленными движениями, она гладила меня. И с каждым движением её дыхание учащалось. {w}Как и моё.")
        $ Fl.say(Fl_th, "Мику такая тёплая… {w}такая маленькая... {w}и такая лёгкая...")
        $ Fl.say(Fl_r, "Неожиданно руки Мику оказались на моей гениталии.")
        $ Fl.say(Fl_mi, "Хозяин, он весь дрожит. Можно я согрею его своим теплом?")
        $ Fl.say(Fl_r, "Больше не в силах терпеть, я резким движение обхватил левой рукой талию девушки, а свободной пропустил сквозь волосы, аккуратно дотронувшись до её шеи.")
        $ Fl.say(Fl_r, "Наши губы соприкоснулись.")
        $ Fl.say(Fl_r, "Всё замерло на миг. Только стук сердца едва нарушал эту тишину.")
        $ Fl.say(Fl_r, "Широко открытие глаза Мику закрылись. И теперь она дала свободу рукам. А если быть точнее руке. {w}Левая рука оставалась лежать на моём члене, а правую она положила мне на грудь.")
        $ Fl.say(Fl_mi, "Хозяин, я...")
        $ Fl.say(Fl_mi, "Я очень сильно хочу от вас котят, ня!")
        $ Fl.say(Fl_mi, "Вы же сделаете одолжение для Мику, ня?")
        $ Fl.say(Fl_r, "После этих слов, я полностью потерял контроль над телом. Руки сами ухватились за грудь неко. {w}Я начал ласкать её, нежно сжимая руками. Мой язык так же не оставил без внимания соски неко.")
        $ Fl.say(Fl_r, "В тот же миг всё заполнилось женскими стонами и милым «Ня».")
        $ Fl.say(Fl_r, "Мику решила не сидеть в сторонке и, обхвотив мой член, начала водить рукой туда сюда.")
        $ Fl.say(Fl_r, "С каждой секундой моя ласка заставляла Мику сильнее намокать в нужном месте.")
        $ Fl.say(Fl_r, "Округлив свои голубые глаза, Мику резко остановилась и своими ладонями постаралась уложить меня на кровать.")
        $ Fl.say(Fl_mi, "Хозяин, можешь немного поиграть вот тут?")
        $ Fl.say(Fl_r, "Мику медленно опустила руку меж своих ног. И прикусив нижнюю губу сделала парочку движений в районе клитора.")
        $ Fl.say(Fl_r, "Я же сразу поняв её намёк, дотронулся до её «киски» и аккуратно провёл по ней двумя пальцами.")
        $ Fl.say(Fl_mi, "Ня! Такое странное чувство, хозяин! Будто внутри всё горит, мне... {w}Мне так хорошо, ня!")
        $ Fl.say(Fl_gg, "Прости, я больше не могу!")
        $ Fl.say(Fl_mi, "О чём вы, хозя...{break}")

        
        $ Fl.AttackScreens(True)
        $ Fl.say(Fl_mi, "НЯЯЯЯ!!!")
        $ Fl.say(Fl_r, "Я быстро вошёл в Мику. {w}Внутри неё было тепло и узко, из-за чего я отчётливо чувствовал, как она всё сильнее обхватывает меня.")
        $ Fl.say(Fl_r, "Я вновь приподнялся и начал медленно двигаться, но Мику уложила меня обратно и перехватила инциативу на себя. Её движения были плавными и изящными. Я чувствовал, как её бёдра бьются об мои ноги. А грудь с каждым движением подпрыгивала.")
        $ Fl.say(Fl_mi, "Ян, вставай.")
        $ Fl.say(Fl_gg, "А?")
        $ Fl.say(Fl_mi, "Ян, хватит спать кому говорю!")
        $ Fl.StopMusic()


        $ Fl.Save("День2: А ведь такой сон был...") 

        scene bg Fl_int_house_of_mv_sunset with hpunch
        $ Fl.Status("60")
        $ Fl.Status("tension", False)
        $ Fl.DayTime("sunset", "sunset")
        $ Fl.Master(Fl_screen_attack_hard)
        $ Fl.say(Fl_r, "Я резко вскочил.", master=Fl_screen_attack, _with=vpunch)
        $ Fl.say(Fl_r, "Было очень трудно собраться с мыслями. Ориентир в пространстве был сильно искажён, отчего я пытался глазами найти источник шума, но в глаза бросались лишь размытые очертания комнаты.")
        $ Fl.HideScreens(_with=Fl_fast)

        show mv normal pioner1 with Fl_dissolve1

        $ Fl.PlayMusic("Fl_goodbye_home_shores", 1, 5)
        $ Fl.ShowScreens(_with=Fl_fast)
        $ Fl.say(Fl_r, "И вот наконец-то фиолетовое пятно приобрело более чёткую картину. {w}Как оказалось, этим пятном была Марина Владимировна.")

        show mv laugh pioner1 with Fl_fast

        $ Fl.say(Fl_mv, "Доброе утро, соня.")
        $ Fl.say(Fl_gg, "Ага...")
        $ Fl.say(Fl_r, "Вяло ответил я. После чего поник.")
        
        show Fl_vignette with Fl_dissolve1
        $ Fl.Pause(1.0)
        $ Fl.say(Fl_th, "Почему{mn} {w}Вот почему нужно было меня будить на самом интересном моменте!!!")
        $ Fl.say(Fl_r, "Перед глазами всё ещё стояла та картина с Мику, где она с кошачьими ушками сидит на мне верхом. {w}Где она чуть ли не самое миловидное, что я смог повстречать за свою жизнь.")
        $ Fl.say(Fl_th, "Ненавижу мир грёз!")
        $ Fl.say(Fl_kvl, "Трудно с тобой не согласиться, Сударь. Даже я немного разочарован...")
        $ Fl.say(Fl_th, "Неужели ты наконец-то начал меня понимать?")
        $ Fl.say(Fl_kvl, "Сон и правда был уж оооочень интересным. Так что да, на этот раз я на твоей стороне.")
        $ Fl.say(Fl_r, "Как бы комична не была данная сцена, но со стороны это определённо выглядит убого и мерзко, как девственник вогнал себя в пучину депрессии из-за пошлого сна.")

        show mv angry pioner1 with Fl_fast

        $ Fl.say(Fl_mv, "Ян, приём!")
        $ Fl.say(Fl_th, "Опять ей что-то надо... Ей не хватило того, что она мой шикарный сон запорола?")
        $ Fl.say(Fl_gg, "Да, вы что-то хотели, Марина Владимировна?")

        show mv laugh pioner2 with Fl_fast

        $ Fl.say(Fl_mv, "Ну чего ты? Не выспался?")

        show mv smile pioner2 with Fl_fast

        $ Fl.say(Fl_mv, "После обеда прошло уже больше трёх часов.")
        hide Fl_vignette with Fl_dissolve1

        $ Fl.Status("+10")
        $ Fl.say(Fl_r, "Я попытался немного расслабить лицо. Вышло так себе. {w}Но мне всё же удалось избавиться от монотонной речи.")
        $ Fl.say(Fl_gg, "Есть такое, ночью плохо спал.")
        $ Fl.say(Fl_gg, "Марина Владимировна, вы лучше скажите, когда я уже получу форму? А то так и к концу смены не стать мне пионером.")

        show mv laugh pioner1 with Fl_fast

        $ Fl.say(Fl_mv, "Какой умничка, не забыл всё таки!")

        hide mv laugh pioner1 with Fl_fast

        $ Fl.say(Fl_r, "Я не стал как-то коментировать стёб вожатой. На самом деле, он мне уже порядком наскучил и не вызывал уже былой реакции. Теперь мне казалось, что этот стёб выделял какой-то приятный элемент в нашем общении, словно мы уже давно знакомы.")
        $ Fl.say(Fl_r, "А тем временем, вожатая подошла к шкафчику. {w}Приоткрыв дверцу шкафа, она протянула руку и оттуда вытащила новый и чистенький комплект пионерской формы.")
        
        show mv smile pioner1 with Fl_fast

        $ Fl.say(Fl_mv, "Держи! И носи на здоровье пионер.")

        show mv normal pioner1 with Fl_fast

        $ Fl.say(Fl_mv, "Одна просьба. Постарайся её не запачкать, ладно?")
        $ Fl.say(Fl_gg, "Хорошо, как скажите.")
        $ Fl.say(Fl_r, "Я взял пионерскую форму в руки. {w}И казалось на этом всё, но вожатая дала мне ещё пакет, внутри которого оказались мыльные принадлежости: полотенце, мыло, зубной порошок(понятие не имею, как им пользоваться).")
        $ Fl.say(Fl_r, "Но кое-чего не было...")
        $ Fl.say(Fl_gg, "А, где станок?")

        show mv smile pioner1 with Fl_fast

        $ Fl.say(Fl_mv, "Станок тебе придётся самому взять.")
        $ Fl.say(Fl_mv, "Он находится на складе.")
        $ Fl.say(Fl_mv, "Ян, ты успел познакомиться с Катей?")
        $ Fl.say(Fl_gg, "Если вы про девушку с голубыми волосами, то да.")
        $ Fl.say(Fl_mv, "Славно, ключи от склада возьмёшь у неё!")
        $ Fl.say(Fl_gg, "Хорошо, я могу идти?")
        $ Fl.say(Fl_mv, "Да, конечно.")

        hide mv smile pioner1 with Fl_fast

        $ Fl.say(Fl_r, "Задерживаться не было смысла. Мне престоялая очередная авантюра.")
        $ Fl.say(Fl_r, "Получив квест от вожатой, я направился на выход.")
        $ Fl.say(Fl_mv, "Ян, стой!")
        $ Fl.say(Fl_th, "Блин, да что опять то?")

        show mv smile pioner1 with Fl_fast

        $ Fl.say(Fl_gg, "Да?")
        $ Fl.say(Fl_mv, "Можешь сдать мне свой обходной пожалуйста?")
        $ Fl.say(Fl_th, "Обходной{mn} {w}Точно бумажка, ради которой мне пришлось бегать по лагерю целый день.")

        show mv smile pioner1 with Fl_fast

        $ Fl.say(Fl_r, "Я вяло протянул бегунок вожатой.")
        $ Fl.say(Fl_r, "Вожатая даже не удосужилась посмотреть на лицевую сторону, где находились все подписи, а просто положила бумажку в карман юбки.")
        $ Fl.say(Fl_th, "Да вы издеваетесь? Зачем я вообще тогда бегал за этими подписями!")

        hide mv smile pioner1 with Fl_fast

        $ Fl.say(Fl_r, "Отчитавшись перед вожатой, я направился в то место, где была большая вероятность встретить Катю.")
        $ Fl.StopAmbience(2)
        $ Fl.HideScreens(_with=Fl_dissolve1)
        $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
        scene bg Fl_black with Fl_dissolve1
        $ Fl.StopMusic(3)

        
        $ Fl.Pause(5.0)




    else:
        $ Fl.Status("")
        $ Fl.Save("День2: Наконец-то я получу форму...")            
        $ Fl.Pause(9.0)
        $ Fl.HideBlink()
        $ Fl.DayTime("sunset", "sunset")

        $ Fl.ShowScreens(_with=Fl_dissolve1)
        $ Fl.Status("30")
        $ Fl.Status("dream", False)

        $ Fl.say(Fl_r, "Не знаю сколько времени я проспал, как услышал мягкий женский голос. Сквозь сон было очень трудно разобрать что от меня хотели.")
        $ Fl.say(Fl_r, "Я медленно открыл глаза.")
        $ Fl.HideScreens(_with=Fl_fast)

        scene bg Fl_int_house_of_mv_sunset with Fl_flash
        $ Fl.Pause(2.0)
        with Fl_flash

        $ Fl.say(Fl_r, "Было очень трудно собраться с мыслями. Ориентир в пространстве был сильно искажён, отчего я пытался глазами найти источник шума, но в глаза бросались лишь размытые очертания комнаты.")
        $ Fl.HideScreens(_with=Fl_fast)

        show mv normal pioner1 with Fl_dissolve1

        $ Fl.PlayMusic("Fl_goodbye_home_shores", 1, 5)
        $ Fl.ShowScreens(_with=Fl_fast)
        $ Fl.say(Fl_r, "И вот наконец-то фиолетовое пятно приобрело более чёткую картину. {w}Как оказалось, этим пятном была Марина Владимировна.")

        show mv laugh pioner1 with Fl_fast

        $ Fl.say(Fl_mv, "Доброе утро, соня.")
        $ Fl.say(Fl_gg, "Ага...")
        $ Fl.say(Fl_r, "Вяло ответил я.")

        show mv laugh pioner2 with Fl_fast

        $ Fl.say(Fl_mv, "Ну чего ты? Не выспался?")

        show mv smile pioner2 with Fl_fast

        $ Fl.say(Fl_mv, "После обеда прошло уже больше трёх часов.")
        hide Fl_vignette with Fl_dissolve1

        $ Fl.Status("+10")
        $ Fl.say(Fl_r, "Я попытался немного расслабить лицо. Вышло так себе. {w}Но мне всё же удалось избавиться от монотонной речи.")

        $ Fl.Status("+30")
        $ Fl.Status("normal", False)
        $ Fl.say(Fl_gg, "Есть такое, ночью плохо спал.")
        $ Fl.say(Fl_gg, "Марина Владимировна, вы лучше скажите, когда я уже получу форму? А то так и к концу смены не стать мне пионером.")

        show mv laugh pioner1 with Fl_fast

        $ Fl.say(Fl_mv, "Какой умничка, не забыл всё таки!")

        hide mv laugh pioner1 with Fl_fast

        $ Fl.say(Fl_r, "Я не стал как-то коментировать стёб вожатой. На самом деле, он мне уже порядком наскучил и не вызывал уже былой реакции. Теперь мне казалось, что этот стёб выделял какой-то приятный элемент в нашем общении, словно мы уже давно знакомы.")
        $ Fl.say(Fl_r, "А тем временем, вожатая подошла к шкафчику. {w}Приоткрыв дверцу шкафа, она протянула руку и оттуда вытащила новый и чистенький комплект пионерской формы.")
        
        show mv smile pioner1 with Fl_fast

        $ Fl.say(Fl_mv, "Держи! И носи на здоровье пионер.")

        show mv normal pioner1 with Fl_fast

        $ Fl.say(Fl_mv, "Одна просьба. Постарайся её не запачкать, ладно?")
        $ Fl.say(Fl_gg, "Хорошо, как скажите.")
        $ Fl.say(Fl_r, "Я взял пионерскую форму в руки. {w}И казалось на этом всё, но вожатая дала мне ещё пакет, внутри которого оказались мыльные принадлежости: полотенце, мыло, зубной порошок(понятие не имею, как им пользоваться).")
        $ Fl.say(Fl_r, "Но кое-чего не было...")
        $ Fl.say(Fl_gg, "А, где станок?")

        show mv smile pioner1 with Fl_fast

        $ Fl.say(Fl_mv, "Станок тебе придётся самому взять.")
        $ Fl.say(Fl_mv, "Он находится на складе.")
        $ Fl.say(Fl_mv, "Ян, ты успел познакомиться с Катей?")
        $ Fl.say(Fl_gg, "Если вы про девушку с голубыми волосами, то да.")
        $ Fl.say(Fl_mv, "Славно, ключи от склада возьмёшь у неё!")
        $ Fl.say(Fl_gg, "Хорошо, я могу идти?")
        $ Fl.say(Fl_mv, "Да, конечно.")

        hide mv smile pioner1 with Fl_fast

        $ Fl.say(Fl_r, "Задерживаться не было смысла. Мне престоялая очередная авантюра.")
        $ Fl.say(Fl_r, "Получив квест от вожатой, я направился на выход.")
        $ Fl.say(Fl_mv, "Ян, стой!")
        $ Fl.say(Fl_th, "Блин, да что опять то?")

        show mv smile pioner1 with Fl_fast

        $ Fl.say(Fl_gg, "Да?")
        $ Fl.say(Fl_mv, "Можешь сдать мне свой обходной пожалуйста?")
        $ Fl.say(Fl_th, "Обходной{mn} {w}Точно бумажка, ради которой мне пришлось бегать по лагерю целый день.")

        show mv smile pioner1 with Fl_fast

        $ Fl.say(Fl_r, "Я вяло протянул бегунок вожатой.")
        $ Fl.say(Fl_r, "Вожатая даже не удосужилась посмотреть на лицевую сторону, где находились все подписи, а просто положила бумажку в карман юбки.")
        $ Fl.say(Fl_th, "Да вы издеваетесь? Зачем я вообще тогда бегал за этими подписями!")

        hide mv smile pioner1 with Fl_fast

        $ Fl.say(Fl_r, "Отчитавшись перед вожатой, я направился в то место, где была большая вероятность встретить Катю.")
        $ Fl.StopMusic(3)
        $ Fl.HideScreens(_with=Fl_dissolve1)
        $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
        scene bg Fl_black with Fl_dissolve1

        
        $ Fl.Pause(5.0)






    $ Fl.Save("День2: На площади")


    $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 4)
    scene bg Fl_ext_square_sunset:
        zoom 1.3 xalign 0.3 yalign 0.6
    show Fl_light_c 
    with Fl_effect_3

    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.AutoSave()
    $ Fl.say(Fl_r, "Я сидел на лавочке и пристально смотрел на Генду. Я заметитл одну деталь, которую не заметил впервый день. {w}Под памятником, находилась решётка, по всей видимости она являлась водоотводом.")

    show Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Ты так и будешь здесь просто сидеть?")
    $ Fl.say(Fl_th, "Это куда лучше чем бегать по всему лагерю за Катей. А так рано или поздно она сама здесь появится.")
    $ Fl.say(Fl_kvl, "Как знаешь.")
    $ Fl.say(Fl_r, "По интонации голоса можно было понять, что продолжать дискусию со мной он не собирался. Но было то что я хотел спросить у него.")
    $ Fl.say(Fl_th, "Слушай, а ты помнишь что-то из моей реальности?")
    $ Fl.say(Fl_r, "Мне не давало покоя тот факт, что я не помню тех кто был связан со мной.")
    $ Fl.say(Fl_kvl, "Помню конечно. Я же могу копаться во всех твоих воспоминаниях, забыл?")
    $ Fl.say(Fl_th, "Значит ты помнишь как зовут моих родителей или подругу детства?")
    $ Fl.say(Fl_kvl, "{mn}")
    $ Fl.say(Fl_r, "Но голос не ответил. Такая же тишина, как попытка вспомнить кого-то...")
    $ Fl.say(Fl_th, "Ты тоже не можешь вспомнить{mn}")
    $ Fl.say(Fl_kvl, "Ты прав. Я не могу вспомнить, то чего ты сам не помнишь. Извини.")
    $ Fl.say(Fl_th, "Да ничего, всё нормально.")
    hide Fl_vignette with Fl_dissolve1

    $ Fl.say(Fl_r, "Я продолжил свои посиделки в тишине. Почему то появилась какая-то апатия. {w}Гляделки с жизнерадостными пионерами, что резвились на площади. {w}Пение птиц и яркое солнце.")
    $ Fl.say(Fl_r, "Моё ожиданние Кати была попытка уйти от реальности.")
    $ Fl.say(Fl_r, "Сколько бы я не смотрел за поведением попаданцев меня всегда удивляло, как они с первых же минут менялись, как будучи затворником они резко становились экстравертами?")
    $ Fl.say(Fl_r, "Я же так резко измениться не мог. Признаться честно, я очень рад что здесь столько классных людей и всегда можно повеселиться. Но порой так хочется побыть в одиночестве и о чём нибудь поразмышлять. Что собственно сейчас я и делаю...")
    $ Fl.say(Fl_ka, "Если столько сидеть, то может голову напечь.")
    $ Fl.say(Fl_th, "А вот и Катя появилась.")

    show kt smile pioner1 with Fl_dissolve1

    $ Fl.say(Fl_gg, "Привет, Кать. Какими судьбами здесь?")
    $ Fl.say(Fl_ka, "Да вот Марина Владимировна попросила одного пионера до склада проводить.")
    $ Fl.say(Fl_th, "Забавно вышло. Думал, что я ищу Катю, а в итоге она меня.")
    $ Fl.say(Fl_gg, "А этот пионер случайно не станок хочет со склада взять?")
    $ Fl.say(Fl_r, "Подыграл я пионерке.")

    show kt laugh pioner2 with Fl_fast

    $ Fl.say(Fl_ka, "А ты откуда знаешь, подслушивал?")
    $ Fl.say(Fl_r, "Я улыбнулся в ответ. И решил наконец-то встать с лавочки.")

    hide kt laugh pioner2 with Fl_fast
    scene bg Fl_ext_square_sunset:
        Fl_bg_zoom_otd(1.3, 1.0, 1.5, 0.3, 0.5, 0.6, 0.5)
    show Fl_light_c 

    $ Fl.Pause(1.5)
    $ Fl.say(Fl_gg, "Ладно, на складе я ещё не был. Интересно что там.")
    $ Fl.say(Fl_r, "Катя же не стала терять время и направилась в нужную сторону.")
    $ Fl.say(Fl_ka, "Не отставай!")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(4.0)
    scene bg Fl_ext_warehouse_day
    show Fl_light_c 
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_ka, "Пришли.")

    show kt smile pioner1 at right with Fl_dissolve1

    $ Fl.say(Fl_r, "Мы оказались почти у самого выхода из лагеря. За густыми кустами виднелся кирпичный забор с воротами.")
    $ Fl.say(Fl_gg, "А куда ведут эти ворота?")
    $ Fl.say(Fl_r, "Пионерка довольно быстро нашла то что зацепило моё внимание.")
    $ Fl.say(Fl_ka, "Эти? В сторону леса. Там есть тропа, если по ней долго идти, можно выйти к небольшому пруду.")

    show kt laugh pioner1 at right with Fl_dissolve1

    $ Fl.say(Fl_ka, "Или ты уже строишь план побега?")

    show Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Строит конечно! Вот уже ищет пути отхода если Микуська решит снова его покусать.")
    $ Fl.say(Fl_th, "Вот как ты находишь моменты когда надо свои шуточки вставить?")
    $ Fl.say(Fl_kvl, "А у меня есть тревожный сигнал, он мне и говорит когда надо пошутить.")
    $ Fl.say(Fl_th, "Задолбал ты уже своими шутками, меня если захотят убить, то же будешь шутить?")
    $ Fl.say(Fl_kvl, "А почему бы и нет, сударь. Смех продливает жизнь!")
    $ Fl.say(Fl_th, "Понял, значит с твоими шутками мне недолго осталось.")
    hide Fl_vignette
    show kt normal pioner1 at right
    with Fl_dissolve1

    $ Fl.say(Fl_r, "Пока я спорил со своей шизой, Катя почему то нахмурилась.")
    $ Fl.say(Fl_gg, "А? Нет конечно, куда мне сбегать. Мне здесь нравится.")
    $ Fl.say(Fl_r, "Как можно быстрее среагировал я на вопрос девушки.")

    show kt smile pioner1 at right with Fl_dissolve1

    $ Fl.say(Fl_r, "Такой ответ очень обрадовал пионерку и былого серьёзного выражения лица след простыл.")
    $ Fl.say(Fl_ka, "Рада что тебе здесь понравилось.")

    show kt smile pioner2 at right with Fl_dissolve1

    $ Fl.say(Fl_ka, "Но не переживай, может мы ещё раз сходим в поход. Мы обычно отрядом каждую смену выбираемся куда-то или до пруда или на опушку леса.")
    $ Fl.say(Fl_ka, "Ты раньше бывал в походах?")

    show kt smile pioner1 at right with Fl_dissolve1

    $ Fl.say(Fl_th, "На природе я раньше бывал часто. Мне всегда нравилось пожарить мясо в лесу или у речки. В начале с родителями, потом мы с друзьями сами выбирались частенько. Атмосфера от таких посиделок непередаваемая!")
    $ Fl.say(Fl_th, "Но в походах - нет, не бывал. Да и желания как такового не было ночевать в лесу.")
    $ Fl.say(Fl_gg, "Нет.")
    $ Fl.say(Fl_ka, "Значит ты обязан сходить с нашим отрядом! Тебе обязательно понравится.")
    $ Fl.say(Fl_r, "Я почему то сразу представил, как Миха и парни из клуба придут с рюкзаками, которые будут звенеть от алкашки. А если ещё Толян пойдёт, то туса будет не забываемая!")
    $ Fl.say(Fl_th, "Одни нажрутся. Второй сто пудов потушит костёр по-пионерски.")
    $ Fl.say(Fl_gg, "Хорошо, обязательно схожу если выпадет возможность.")
    $ Fl.say(Fl_ka, "Ладно, пошли. Будем одного пионера в порядок приводить.")

    $ Fl.PlaySound("Fl_open_door_1", 1.0, 0, False)
    hide kt smile pioner1 at right with Fl_dissolve1

    $ Fl.say(Fl_r, "Пионерка радостно открыла склад и упорхнула. Мне же оставалось молча проследовать за ней.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    if Ist_mi >=2:
        $ Fl.StopAmbience(0.5)
        $ Fl.PlaySound("Fl_glith", 1, 0, False)
        $ Fl.DayTime("rain", "rain")
        scene bg Fl_int_sklad_night_blood
        show Fl_interference_anim
        with Fl_flash
        $ Fl.ShowScreens(_with=Fl_fast)
        $ Fl.say(Fl_mi, "ЯН!", _with=hpunch)
        $ Fl.say(Fl_mi, "Прош... ..та..!", _with=hpunch)
        $ Fl.say(Fl_ka, "Ян?")

        $ Fl.PlayAmbience("Fl_camp_entrance_day", 1, 1)
        $ Fl.DayTime("sunset", "sunset")
        scene bg Fl_int_sklad_day
        show kt tender pioner1
        with Fl_fast
        $ Fl.Status("-20")
        $ Fl.Status("tension", False)
        $ Fl.say(Fl_r, "На меня уставилась девушка. На её глазах читался испуг и недопонимание. Она пыталась вытянуть руку, но стоило мне обратить внимание на неё, тут же убрала.")
        $ Fl.say(Fl_ka, "Ян, ты в порядке?")
        $ Fl.say(Fl_gg, "А? А да, всё нормально, просто что-то задумался.")
        $ Fl.Status("-20")
        $ Fl.Status("stress", False)
        $ Fl.say(Fl_th, "Что это мать его было{mn}")
        $ Fl.say(Fl_th, "Голос, ты тут?")

        show Fl_vignette with Fl_dissolve1
        $ Fl.say(Fl_kvl, "Что случилось?")
        $ Fl.say(Fl_th, "Ты и сам блин видел!")
        $ Fl.say(Fl_kvl, "Ты о чём, сударь?")
        $ Fl.say(Fl_th, "Я зашёл на склад, но он выглядел иначе. Была ночь, а повсюду была кровь и со мной говорила Мику!")
        $ Fl.say(Fl_kvl, "Так-так, сударь. Ты случайно не перегрелся на солнце?")
        $ Fl.say(Fl_th, "Какое нафиг солнце?!", _with=hpunch)
        $ Fl.say(Fl_kvl, "Да не кричи ты. Я не знаю что ты видел, но я бы тоже это увидел. Так что это странно...")
        $ Fl.say(Fl_th, "Это всё что ты можешь сказать?")
        $ Fl.say(Fl_kvl, "К сожалению да. Но глюки это действительно странно... {w}Я подумаю что это могло быть.")
        hide Fl_vignette with Fl_dissolve1

        $ Fl.say(Fl_r, "Кое-как, пытаясь справиться с шоком от увиденного, я решил вернуться к всё ещё обеспокоенной пионерке.")
        $ Fl.Status("+40")
        $ Fl.Status("normal", False)
        $ Fl.say(Fl_gg, "Правда всё в порядке.")

        show kt sad1 pioner1 with Fl_dissolve1

        $ Fl.say(Fl_ka, "Ладно, но если что я могу с тобой сходить в медпункт.")
        $ Fl.say(Fl_gg, "Кать, правда, всё хорошо.")

        hide kt sad1 pioner1 with Fl_dissolve1
        $ Fl.say(Fl_r, "Катя ещё раз одарила меня встревоженным взглядом, но не стала спорить.")
        $ Fl.say(Fl_r, "Я же принялся осматривать само помещение.")
        $ Fl.HideScreens(_with=Fl_dissolve1)

        $ Fl.Pause(2.5)
        $ Fl.PlayMusic("Fl_chill", 1, 3)

    else: 
        scene bg Fl_int_sklad_day with Fl_effect_2
        $ Fl.Pause(2.0)
        $ Fl.PlayMusic("Fl_chill", 1, 3)

    $ Fl.Save("День2: Время складных историй.")
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Склад оказался ещё больше, чем с наружи. Он был чуть ли не на половину забит строй материалами и прочих мешков. Но по-мимо них затесались ещё запасы провизии - мешки с сахаром.")
    $ Fl.say(Fl_th, "Так вот как выглядит наказание вожатой.")
    $ Fl.say(Fl_r, "Мешки были разного размера. Начиная от 5кг, заканчивая 15кг. На любой вкус для пионера взависимости от тяжести наказания.")
    $ Fl.say(Fl_gg, "Как среди строй материала может находиться станок для бритья?")

    show kt laugh pioner2 with Fl_dissolve1

    $ Fl.say(Fl_ka, "Я так и думала, что ты об этом спросишь.")
    if Ist_mi >=2:
        $ Fl.say(Fl_r, "Катя вновь вошла в привычный жизнерадостный образ. Наверное она не зацикливается на каких-то странностях нежели я.")
    else:
        $ Fl.say(Fl_r, "Катя с хитрой улыбкой смотрела прямо на меня. Наверное не я один кто спрашивал подобное у неё.")

        show Fl_vignette with Fl_dissolve1
        $ Fl.say(Fl_kvl, "Думаешь, ещё есть пионер с небритой щетиной, как у бомжа?")
        $ Fl.say(Fl_th, "Да что ты всё прикопался к моей щетине? {w}Да неухоженная, но не настолько же всё плохо!")
        $ Fl.say(Fl_kvl, "Ничего, скоро мы это исправим. Вот увидишь как помолодеешь на лет 10.")
        hide Fl_vignette with Fl_dissolve1

        $ Fl.say(Fl_r, "Я уже начинал сильно жалеть наличию голоса в моей голове. Хотя кто бы вообще хотел иметь подобный бубнёж в голове...")

    show kt laugh pioner1 with Fl_dissolve1

    $ Fl.say(Fl_ka, "Сейчас найду. Где-то он был тут...")

    hide kt laugh pioner1 with Fl_dissolve1

    $ Fl.say(Fl_r, "После чего пионерка принялась искать заветный артефакт, что приведёт моё лицо в порядок.")
    $ Fl.say(Fl_gg, "А много таких заданий тебе подкидывает вожатая?")
    $ Fl.say(Fl_r, "Про Катю я знаю мало, да и мы толком даже не поговорили после той встречи у ворот.")
    $ Fl.say(Fl_th, "Хотя если так подумать, то я мало с кем успел общаться в лагере. Мику наверное единственная с кем я больше всего времени провожу и почему то игнорирую остальных.")
    $ Fl.say(Fl_ka, "В каком смысле?")
    $ Fl.say(Fl_gg, "Ну вот таких заданий как сейчас. Ищешь бритву для новичка.")
    $ Fl.say(Fl_ka, "Ааа, ты об этом.")
    $ Fl.say(Fl_ka, "Ну довольно много, то кому-то что-то открыть надо, то принести что-то со склада. Иногда бывает что надо всех обежать и предупредить.")
    $ Fl.say(Fl_r, "Катя продолжала перебирать коробки, попутно ведя диалог со мной.")
    $ Fl.say(Fl_gg, "Почему ты вообще решила вызваться помощницей вожатой? Как по мне пионерлагерь создан для отдыха, а не выполнять тонну поручений.")

    show kt normal pioner2 with Fl_dissolve1

    $ Fl.say(Fl_ka, "Вот тут, Ян, ты не прав!")
    $ Fl.say(Fl_ka, "Лагерь не только для отдыха. Здесь учат быть более ответственным, помогать старшим и уметь общаться со сверстниками и находить общие интересы.")

    hide kt normal pioner2 with Fl_dissolve1

    $ Fl.say(Fl_r, "Исправив помарку в моих словах, пионерка вернулась к поискам.")
    $ Fl.say(Fl_ka, "А решила я стать помощницей, потому что сама хочу в будущем пойти учиться на педагогический. Мне нравится общаться с детьми, да и я люблю людей. Такой уж я человек.")
    $ Fl.say(Fl_ka, "Помощница вожатой неплохая возможность попробовать себя в этом деле.")

    $ Fl.Pause(2.5)
    $ Fl.say(Fl_th, "Понятно. {w}Действительно, что-то я об этом и не подумал. У каждого свои цели и свои предпочтения. По первому впечатлению о Кате можно было и догадаться, что такому человеку как она подходит роль помощницы вожатой.")
    $ Fl.say(Fl_th, "Как же здесь люди отличаются от моей реальности{mn}")
    $ Fl.say(Fl_gg, "Понял.")

    show kt smile pioner1 with Fl_dissolve1

    $ Fl.say(Fl_ka, "Вожатой куда сложнее. Я занимаюсь обычными поручениями, а на ней ответственность за всех пионеров в её отряде.")
    $ Fl.say(Fl_ka, "Следить за порядком, заполнение тонны бумаг. Это не так просто как кажется, Ян.")
    $ Fl.say(Fl_gg, "Тут ты права. Пока пионеры подростки им это тяжело понять.")

    show Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Тоже мне старый дед нашёлся.")
    $ Fl.say(Fl_th, "Ну знаешь, когда я начал жить один, то сам ощутил на себе весь тяжкий груз взрослого человека.")
    $ Fl.say(Fl_kvl, "Поэтому планировал жить на улице после того как тебя из квартиры выперли?")
    $ Fl.say(Fl_th, "Ты прав, я не справился. Может мне и пришлось резко повзрослеть, но ребячество и наивная гордость у меня действительно присутствовала.")
    $ Fl.say(Fl_kvl, "Ну ты действительно крутился в своей жизни как мог.")
    hide Fl_vignette with Fl_dissolve1

    $ Fl.say(Fl_ka, "А ты куда интереснее, Ян, чем я думала.")
    $ Fl.say(Fl_th, "Интересно можно ли считать это похвалой?")

    hide kt smile pioner1 with Fl_fast

    $ Fl.say(Fl_ka, "Нашла!", _with=vpunch)
    $ Fl.say(Fl_r, "Наконец-то нужная коробка лежала у ног пионерки. Она была доверху забита старыми дедовскими станками.")
    
    show kt smile pioner1 with Fl_dissolve1

    $ Fl.say(Fl_ka, "Держи.")
    $ Fl.say(Fl_gg, "Спасибо.")

    hide kt smile pioner1 with Fl_dissolve1

    $ Fl.say(Fl_r, "Выполнить поручение вожатой оказалось не таким простым делом, теперь Кате предстояло вернуть все коробки на свои места.")
    $ Fl.say(Fl_gg, "Давай помогу.")
    $ Fl.say(Fl_r, "Девушка была только рада такому жесту.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(4)

    $ Fl.PlaySound("Fl_pause_time", 1.0, 2, False)
    scene Fl_pause
    with Fl_effect_time_pause


    $ Fl.Pause (3.0)
    scene bg Fl_black with Fl_dissolve2
    $ Fl.Pause (1.0)


    scene bg Fl_ext_warehouse_sunset
    show Fl_light_c 
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Когда с уборкой было покончено, снаружи всё заполнилось в тёплый оттенок. Солнце заходило за гаризонт, тем самым создавая сказочную атмосферу. Было трудно поверить, что такая красота меня окружала всё это время, а я её попросту не замечал.")

    show Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Молодец, Сударь, поступил как истинный пионер!")
    $ Fl.say(Fl_th, "Сам в шоке. Наверное форма на меня так повлияла.")
    $ Fl.say(Fl_r, "Было странное ощущение, но я действительно в глубине души радовался своему маленькому доброму поступку.")
    hide Fl_vignette with Fl_dissolve1

    show kt smile pioner1 at right with Fl_dissolve1

    $ Fl.say(Fl_ka, "Ян, а ты сам куда планируешь поступать как закончишь школу?")
    $ Fl.say(Fl_r, "Почему то на моём лице произвольно появилась кривоватая ухмылка.")
    $ Fl.say(Fl_th, "Если бы ты только знала, что я уже закончил школу и всё что меня ждало в будущем тонну долгов и нищая жизнь.")
    $ Fl.say(Fl_gg, "Не знаю, пока ещё не задумывался. Ищу себя.")

    show kt laugh pioner2 at right with Fl_dissolve1

    $ Fl.say(Fl_ka, "Будешь музыкой заниматься в будущем?")
    $ Fl.say(Fl_r, "Я сделал вопросительное выражение лица.")

    show kt smile pioner1 at right with Fl_fast

    $ Fl.say(Fl_ka, "Мику и правда может хорошо тебя подтянуть в музыке!")
    $ Fl.say(Fl_gg, "Кстати, раз мы эту тему подняли. Не знаешь почему с Мику никто не хочет общаться?")

    show kt normal pioner1 at right with Fl_dissolve1

    $ Fl.say(Fl_ka, "Ты о чём?")
    $ Fl.say(Fl_gg, "Мику говорила, что никто не хочет вступать в её кружок и все стараются её избегать, лишь бы не пересечься лишний раз.")
    $ Fl.say(Fl_gg, "Это из-за её быстрой речи?")

    show kt sad1 pioner1 at right with Fl_dissolve1

    $ Fl.say(Fl_ka, "Есть такое, я тоже замечала, что с ней никто не разговаривает. Но последние смены она сама перестала с другими общаться.")

    if Ist_mi >=2:
        $ Fl.say(Fl_ka, "Она не обращает ни на кого внимание. Смотрит на всех словно сквозь стену.")
        $ Fl.say(Fl_th, "Сама сторонится других? {w}Неужели она просто такая же одиночка, как я?")
        $ Fl.say(Fl_th, "Хотя странно всё это, почему со мной она так счастлива? Из-за увлечения или то что я не такой как все?")
    else:
        $ Fl.say(Fl_ka, "Наверное она уже привыкла и сама перестала заводить с кем-то разговор.")

    show kt normal pioner2 at right with Fl_dissolve1

    $ Fl.say(Fl_ka, "Ты же с Мику в одном домике живёшь?")
    $ Fl.say(Fl_gg, "Ага.")

    show kt normal pioner1 at right with Fl_fast

    $ Fl.say(Fl_ka, "Про 13 домик ходят разные слухи, но ты в них не верь.")
    $ Fl.Status("-10")
    $ Fl.Status("tension", False)
    $ Fl.say(Fl_gg, "Какие слухи?")

    show Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Сударь, может это нам поможет понять что произошло вчера ночью.")
    $ Fl.say(Fl_th, "Возможно, надо распросить у Кати подробнее про байки о домике Мику.")
    hide Fl_vignette with Fl_dissolve1

    hide kt normal pioner1 at right with Fl_dissolve1

    $ Fl.say(Fl_ka, "Пошли, по дороге расскажу. Чего нам тут стоять у склада.")
    $ Fl.say(Fl_r, "Девушка направилась в сторону откуда мы пришли, я же увлечённым её речью принял предложение.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2

    $ Fl.Pause (4.0)
    scene bg Fl_ext_houses2_sunset
    show Fl_light_c 
    with Fl_dissolve2
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Катя шла молча. Она явно себя отчитывала за то что проговорилась про домик Мику.")
    $ Fl.say(Fl_gg, "Так что за слухи?")
    $ Fl.say(Fl_r, "Решил я разрушить тишину между нами.")

    $ Fl.PlayMusic("Fl_razg_zn", 1, 4)
    $ Fl.say(Fl_ka, "Не знаю даже как тебе объяснить. Началось это со слухов младших отрядов.")
    $ Fl.say(Fl_ka, "Они рассказывали что-то про призраков и что ночью в домике что-то происходит.")
    $ Fl.say(Fl_ka, "В начале я не верила этим слухам. Думала, что это дети, они любят что-то придумать и друг друга пугать.")
    $ Fl.say(Fl_ka, "Но потом действительно стало странно{mn} {w}Все кого заселяли в этот дом, просили их переселить. Каждый рассказывал своё, у кого вещи терялись или появлялись тех что раньше не было. Кто-то слышал какой-то шум ночью или в самом доме было ужасно холодно. Но всех беспокоили кошмары.")
    $ Fl.say(Fl_ka, "Не знаю почему, но никто не мог объяснить все эти странности. Да и массово никто бы не стал так шутить и подыгрывать детям.")
    $ Fl.say(Fl_gg, "А вожатая что насчёт этого думает?")
    $ Fl.say(Fl_ka, "Говорит что это просто байка и возможно сами же дети подшучивают над жильцами.")
    $ Fl.say(Fl_th, "Ну да, ни один взрослый не поверит в паранольманщину.")
    $ Fl.say(Fl_th, "Я бы тоже наверное нашёл логическое объяснение, но я тут переродился как бы...")
    $ Fl.say(Fl_ka, "Ян, ты же вчера ночевал в 13 доме, ты сам заметил что-то странное?")
    $ Fl.say(Fl_th, "Заметил ли я что-то странное?")
    $ Fl.say(Fl_th, "А стуки в дверь по среди ночи можно принять за странность?")
    $ Fl.say(Fl_th, "Хотя опять же, может представители пионеров младших могли постучать и убежать.")

    show Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Хочешь сказать, что этой ночью тебя дети вырубили и затащили в дом обратно?")
    $ Fl.say(Fl_th, "Точно. Об этом я почему то не подумал{mn}")
    $ Fl.say(Fl_th, "А ты что считаешь о призраках в доме Мику?")
    $ Fl.say(Fl_kvl, "Не знаю, муть какая-то. Но если с этим домом действительно что-то не так, то следует об этом распросить вожатую.")
    $ Fl.say(Fl_th, "Ты прав.")
    hide Fl_vignette with Fl_dissolve1

    $ Fl.say(Fl_ka, "Ян, приём!")
    $ Fl.say(Fl_gg, "Что? А нет, ничего странного не заметил.")
    $ Fl.say(Fl_r, "Не успев среагировать, я соврал Кате.")
    $ Fl.say(Fl_ka, "Ян, ты порой странный. Резко начинаешь витать в облаках...")
    $ Fl.say(Fl_gg, "Я просто пытался вспомнить было ли что-то такое из того что ты перечислила.")
    $ Fl.say(Fl_th, "Да уж, с голосом действительно трудно переговариваться когда кто-то рядом. {w}Так и за сумащедщего могут принять...")
    $ Fl.say(Fl_gg, "А Мику хоть раз жаловалась на странности?")
    $ Fl.say(Fl_ka, "Нет, ни разу. Мику наверное единственная кому удалось ужиться в этом доме.")
    $ Fl.say(Fl_gg, "Поэтому с Мику никто не живёт?")
    $ Fl.say(Fl_ka, "Ага.")
    $ Fl.say(Fl_th, "А вожатая молодец, сбагрила меня в домик с призраками!")

    $ Fl.StopMusic(4)
    $ Fl.say(Fl_ka, "Извини, что запугала. Надеюсь из-за меня ты не захочешь переселиться.")
    $ Fl.say(Fl_r, "Девушка поникла и опустила голову.")
    $ Fl.say(Fl_gg, "Не переживай, это всего лишь байки.")
    $ Fl.say(Fl_r, "Катя подняла голову и улыбнулась.")
    $ Fl.say(Fl_ka, "Ну и отлично!")
    $ Fl.say(Fl_ka, "Кстати, а вы очень хорошо сдружились с Мику!")
    $ Fl.say(Fl_r, "Почему то ухмылка пионерки вогнала меня в краску. Этот хитрый взгляд явно намекал не на просто дружбу между нами с Мику.")
    $ Fl.say(Fl_gg, "Ревнуешь?")

    $ Fl.PlaySound("Fl_smeh_sn", 1, 0, False)
    $ Fl.say(Fl_ka, "Завидую. {w}Не каждому выпадает возможность подружиться с Мику, а особенно переночевать в её доме в первый же день.")
    $ Fl.say(Fl_th, "Я что-то не понял, теперь каждый пионер в лагере знает что я ночевал у Мику?")

    show Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Да вы уже в лагере парочка официально.")
    $ Fl.say(Fl_th, "Детский сад какой-то.")
    $ Fl.say(Fl_kvl, "Ну а что ты хотел, сударь, это же дети. У них всё просто и очевидно.")
    hide Fl_vignette with Fl_dissolve1

    $ Fl.say(Fl_gg, "Весь лагерь уже об этом знает?")
    $ Fl.say(Fl_ka, "Что именно? То что ты с Мику быстро сдружился или то что ты неё ночевал?")
    $ Fl.say(Fl_th, "Вот лиса, играется со мной!")
    $ Fl.say(Fl_gg, "Второе.")
    $ Fl.say(Fl_ka, "Да не парься, Ян. Об этом знает только вожатая и я.")
    $ Fl.say(Fl_ka, "Забыл, я же помощница вожатой!")
    $ Fl.say(Fl_gg, "Ну да{mn}")
    $ Fl.say(Fl_r, "На моём лице читалось недовольство, никогда не любил сплетни и то что люди додумывают себе. Катя это заметила и сбавила обороты.")
    $ Fl.say(Fl_ka, "Эх, хотела бы я тоже подружиться с Мику так просто.")
    $ Fl.say(Fl_gg, "А ты хорошо знаешь Мику?")

    if Ist_mi >=2:
        $ Fl.say(Fl_ka, "А что?")
        $ Fl.say(Fl_r, "Пионерка вновь сделала хитрый взгляд. Прям читался намёк.")

        show Fl_vignette with Fl_dissolve1
        $ Fl.say(Fl_kvl, "А ты не хочешь распросить Катю о странном поведении Мику?")
        $ Fl.say(Fl_th, "Думаешь она может что-то знать об этом?")
        $ Fl.say(Fl_kvl, "Ну она с ней куда больше времени здесь живёт, может что-то странное да заметила.")
        $ Fl.say(Fl_th, "А ты прав...")
        hide Fl_vignette with Fl_dissolve1

    elif Obs_mi >= 2 or Ist_mi == 1:
        $ Fl.say(Fl_ka, "Ну Мику довольно замкнутая.")
        $ Fl.say(Fl_th, "Может стоит её распросить о странностях Мику, хоть так проясню ситуацию что произошла утром.")

        show Fl_vignette with Fl_dissolve1
        $ Fl.say(Fl_kvl, "Неплохая мысль, сударь. Катя должна лучше знать Мику.")
        $ Fl.say(Fl_th, "С ней мало кто общается, так что навряд ли.")
        $ Fl.say(Fl_kvl, "Но попробовать всё же стоит.")
        hide Fl_vignette with Fl_dissolve1

    else:
        $ Fl.say(Fl_ka, "Я о многих знаю что-то в этом лагере.")
    $ Fl.say(Fl_th, "Стоит ли у Кати спрашивать об яндерных наклонностях Мику{mn} Или же нет{mn}")
    $ Fl.HideScreens(_with=Fl_dissolve1)

    menu:
        "Спросить у Кати про Мику":
            $ Obs_mi += 1
            $ Fl.ShowScreens(_with=Fl_dissolve1)
            $ Fl.say(Fl_gg, "Кать, а ты замечала в Мику что-то странное?")
            $ Fl.say(Fl_ka, "Странное{mn} В каком плане «странное»?")
            $ Fl.say(Fl_r, "Девушка с искренним непониманием смотрела на меня.")

            $ Fl.Pause(2.0)
            $ Fl.Status("-10")
            $ Fl.say(Fl_th, "Пофиг расскажу как есть.")
            $ Fl.say(Fl_gg, "Ну бывало такое что она смотрит пристально на людей и при этом её взгляд координально меняется?")
            $ Fl.say(Fl_ka, "В каком смысле?")
            $ Fl.say(Fl_r, "Катя одарила меня серьёзным выражением лица, какзалось её больше волнует что я хочу наплести про Мику, чем сам мой вопрос.")
            $ Fl.say(Fl_gg, "Ну она сегодня утром смотрела, как я спал. Пустым взглядом{mn}")
            $ Fl.say(Fl_r, "Пионерка тут же улыбнулась.")
            $ Fl.say(Fl_ka, "Эх, дурачок ты, Ян!")
            $ Fl.say(Fl_ka, "Как же до вас парней туго доходит. Понравился ты ей, вот и засматривается она на тебя!")
            $ Fl.say(Fl_th, "Ну <них*ра> себе засматривается, блин!")
            $ Fl.say(Fl_th, "Я знаю как засматриваются девушки, когда им кто-то нравится. И взгляд с узкими зрачками даже и близко не то!")
            $ Fl.say(Fl_gg, "Нет нет, это не то. У неё потом зрачки сузились и она будто на своей волне говорила одно и тоже.")
            $ Fl.say(Fl_ka, "Ян, это называется волнение. Просто видно из-за одиночества у неё это выражается иначе.")
            $ Fl.say(Fl_th, "Ясно. Зря я поднял эту тему, Катя ничего подобного не замечала.")

            show Fl_vignette with Fl_dissolve1
            $ Fl.say(Fl_kvl, "Или Мику просто никогда не показывала такую сторону другим.")
            $ Fl.say(Fl_th, "Тоже об этом подумал. Яндерские наклоности проявляются только в сторону того кто тебе нравится.")
            $ Fl.say(Fl_kvl, "Сударь, ты постоянно упоминаешь яндере. Ты ведь понимаешь, что если Мику действительно Яндере, то тебе нельзя сближаться с другими девушками?")
            $ Fl.say(Fl_th, "Я не об этом, мне просто так легче охаректизовать поведение Мику с утра.")
            $ Fl.say(Fl_th, "Лучше скажи, ты хоть примерно смог разобраться что с ней было не так?")
            $ Fl.say(Fl_kvl, "Нет, мало данных, поэтому и предлагаю тебе узнать о ней по больше, но держаться от неё самой подальше.")
            $ Fl.say(Fl_th, "Хех, а задачка не такая уж и простая.")
            $ Fl.Status("+10")
            hide Fl_vignette with Fl_dissolve1
            $ add_mi += 1


        "Лучшее не стоит":
            $ Fl.ShowScreens(_with=Fl_dissolve1)
            $ Fl.say(Fl_th, "Нет. Ещё подумают что я сумашедший. Или куда хуже распустят слухи про Мику, ей и так досталось.")
            $ Fl.say(Fl_th, "Если я и хочу разобраться что с Мику не так, то сделаю это лично. Распрашивать у других плохая идея, лучше у самой Мику узнать путём времяпровождения.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(5.0)
    scene bg Fl_ext_house_of_mi_sunset
    show Fl_light_c 
    with Fl_dissolve2
    $ Fl.AutoSave()
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Оставшийся путь мы провели молча. Возможно из-за того что наш диалог в конце завернул не в то русло, а может причина была в ином. Но никто и не возражал тишине, каждый смог обдумать своё и такая компания тоже неплоха.")

    show kt smile pioner1 with Fl_dissolve1
    
    $ Fl.say(Fl_ka, "А вот и твой дом, Ян.")
    $ Fl.say(Fl_r, "Перед глазами стоял обычный дом, его дизайну не удивлял, да и наверное я так за время блужданий привык, что смог бы отличить каждый дом в лагере.")
    $ Fl.say(Fl_ka, "Ладно у меня ещё дела есть, прости что вот так ухожу. Если что я ты знаешь где меня искать.")
    $ Fl.say(Fl_gg, "На площади?")

    $ Fl.PlaySound("Fl_smeh_sn", 1, 0, False)
    show kt laugh pioner1 with Fl_dissolve1

    $ Fl.say(Fl_ka, "У меня в домике! Я же не целый день бегаю по поручениям вожатой и работаю.")
    $ Fl.say(Fl_gg, "Точно.")
    $ Fl.say(Fl_gg, "Тогда до встречи, а я пока пойду навещу призраков из баек.")

    show kt smile pioner1 with Fl_dissolve1

    $ Fl.say(Fl_r, "Юмор был среднечок, но Кате он понравился. Мой настрой её радовал, всё же она немного винила себя за то что наговорила мне про дом в котором я живу.")

    hide kt smile pioner1 with Fl_dissolve1

    $ Fl.say(Fl_r, "Катя ушла, а я ещё какое-то время попилил взглядом дверь и наконец-то решил зайти.")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    $ Fl.Save("День2: Настоящий пионер.")
    $ Fl.PlaySound("Fl_open_door_2", 1, 0, False)
    scene bg Fl_int_house_of_mi_sunset with Fl_flash:
        subpixel True
        zoom 1.4 xalign 0.5 yalign 0.5 alpha 1.0
        ease 5 zoom 1.0 xalign 0.5 yalign 0.5 alpha 1.0
            
    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Мыслей не было. Поэтому ничего мне не помешало сделать то что я так долго планировал.")
    $ Fl.say(Fl_gg, "Ну что ж, пора уже сбрить с себя эту шевелюру.")
    $ Fl.say(Fl_r, "Станок в руке не внушал доверия.")
    $ Fl.say(Fl_th, "У меня таким дед лицо себе постоянно резал. Газетка тут хоть навсякий найдётся?")
    $ Fl.say(Fl_r, "Сделав мыльный раствор в стакане, я начал намыливать лицо.")
    $ Fl.say(Fl_gg, "Ну погнали!")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(4)

    $ Fl.PlaySound("Fl_pause_time", 1.0, 2, False)
    scene Fl_pause
    with Fl_effect_time_pause


    $ Fl.Pause(3.0)
    scene bg Fl_black with Fl_dissolve2
    $ Fl.Pause(1.0)

    scene bg Fl_int_house_of_mi_sunset with Fl_dissolve2
    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Как и ожидалось пораниться мне всё же удалось. Я не придумал ничего лучше чем вытирать кровь просто рукой.")

    show Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Я погляжу газетки не нашлось?")
    hide Fl_vignette with Fl_fast

    scene bg Fl_int_house_of_mi_sunset:
        Fl_bg_zoom_th(1.0, 1.5, 1.5, 0.5, 0.2, 0.5, 0.55)
    $ Fl.Pause(1.5)
    $ Fl.PlaySound("Fl_bed_squeak", 1, 0, False)
    $ Fl.AttackMaster(False)
    $ Fl.say(Fl_r, "Я проигнорировал вопрос голоса и молча прилёг на кровать.")

    $ Fl.PlayMusic("Fl_seven", 1, 8)
    show Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Сударь, это не дело. Снова решил лечь спать?")
    $ Fl.say(Fl_th, "Какое-то не простое перерождение получается. Ещё с первого дня столько странностей, не понимаю что делать и как правильно поступить.")
    $ Fl.say(Fl_r, "Продолжая игнорировать речь голоса, проговорил я.")
    $ Fl.say(Fl_kvl, "Слушай, тебе бы развеяться. Веди обычную жизнь пионера, когда ты последнее время вот так отдыхал?")
    $ Fl.say(Fl_kvl, "Я разберусь с вопросами что тебя тревожат.")
    $ Fl.say(Fl_th, "Ты?")
    $ Fl.Status("-10")
    $ Fl.say(Fl_th, "Я кроме твоих шуток и стёбов ничего не слышал! {w}Это я не знаю, это я сказать не могу, тут тебе знать не положено. Чем ты мне можешь помочь?")
    $ Fl.say(Fl_th, "Ты больше шило в жопе, чем шиза. Шиза порой бывает хотя бы полезная!")
    $ Fl.say(Fl_r, "Эмоции переполняли меня, я был очень зол всей ситуацией в которой мне приходилось разбираться {b}одному{/b}.")
    $ Fl.say(Fl_kvl, "{mn2}")
    $ Fl.Pause (2.5)
    $ Fl.Status("+10")
    $ Fl.say(Fl_th, "Обиделся?")
    $ Fl.say(Fl_kvl, "{mn}Нет.")
    $ Fl.say(Fl_kvl, "На самом деле ты прав, но у меня есть причины почему я не могу тебе всё рассказывать. {w}Но до того как ты начал на меня вымешать свою злость я хотел тебе кое-что рассказать.")
    $ Fl.say(Fl_th, "Ладно извини, я погорячился.")
    $ Fl.say(Fl_th, "Что ты хотел мне рассказать?")
    $ Fl.say(Fl_kvl, "Слова Кати про 13 дом. Я действительно чувствую странную ауру здесь. И{mn2} такая же аура исходит от Мику.")
    $ Fl.say(Fl_th, "Это ещё как понимать?")
    $ Fl.say(Fl_kvl, "Не знаю как бы тебе правильно объяснить, но тут будто моё сознание с твоим сильно проседает. Мне трудно находится у тебя в голове пока ты рядом с Мику или в этом доме.")
    $ Fl.say(Fl_th, "Знаешь из-за чего это может быть?")
    $ Fl.say(Fl_kvl, "Есть догадки, но я не уверен в них. Может нам удаться что-то об этом узнать.")
    $ Fl.say(Fl_th, "Понятно.")
    $ Fl.Pause(3.0)
    if Ist_mi >=2:
        $ Fl.say(Fl_th, "Знаешь всё{mn} так странно. И мне не даёт покоя то что я увидел когда вошёл внутрь сарая. {w}Тот глюк или видение{mn} я будто испытал дежавю.")
        $ Fl.say(Fl_kvl, "Может это как-то связано с аурой этого дома?")
        $ Fl.say(Fl_th, "Не знаю, честно не знаю.")
    $ Fl.say(Fl_th, "Ещё поведение Мику с утра{mn}")
    if Ist_mi >=2:
        $ Fl.say(Fl_th, "Да она странная, но мне достаточно хватило времени чтобы понять, что именно это меня в ней и притягивает. Быть не такой как все, наверное это и есть свежий глоток воздуха для меня.")
        $ Fl.say(Fl_th, "Наверное это странно слышать от меня, который до сих пор зациклен на инциденте утром. Но может пора бы закрыть глаза на то что произошло и наслаждаться жизнью пионера?")
        $ Fl.say(Fl_kvl, "Сударь...")
    else:
        $ Fl.say(Fl_th, "Может я себя просто накручиваю, голос?")
        $ Fl.say(Fl_kvl, "Определённо. И как я и сказал мы разберёмся с этим. А пока...")
    $ Fl.say(Fl_kvl, "Ты слишком себя нагружаешь. Тебе стоит развеется и спокойно прожить эту смену.")
    $ Fl.say(Fl_th, "А дальше что? Куда я попаду после того как смена закончится?")
    $ Fl.say(Fl_kvl, "{mn2}")
    $ Fl.say(Fl_r, "Но как и ожидалось даже голос не знает ответ на эту загадку. Я погряз в своих мыслях и мне это очень не нравилось.")
    hide Fl_vignette with Fl_dissolve1
    $ Fl.StopMusic(5)

    $ Fl.Master(Fl_bg_zoom_otd(1.5, 1.0, 1.5, 0.2, 0.5, 0.55, 0.5))
    $ Fl.Pause(1.5)
    $ Fl.PlaySound("Fl_bed_squeak", 1, 0, False)
    $ Fl.Status("+20")
    $ Fl.Status("normal", False)
    $ Fl.say(Fl_gg, "Ладно, пофиг что будет. Надо наслаждаться моментом. Своей жизни что ли не хватило на размышляния о «важном».")

    $ Fl.PlaySound("Fl_making", 1, 0, False)
    $ Fl.AttackMaster(False)
    $ Fl.say(Fl_r, "Я наспех переоделся в пионерскую форму. {w}С галстуком вышли проблемы, так что я его просто завязал на руке.")
    $ Fl.say(Fl_r, "Ещё раз полюбовавшись собой в зеркале, я выполз наружу.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    scene bg Fl_black with Fl_effect_3


    $ Fl.PlaySound("Fl_open_door_2", 1, 0, False)
    $ Fl.Save("День2: Новая операция - забить желудок.")
    $ Fl.Pause(3.5)
    scene bg Fl_ext_house_of_mi_sunset
    show Fl_light_c 
    with Fl_effect_3
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Снаружи во всю светило солнце. Чем больше оно заходило за горизонт, тем сильнее мир приобретал яркую вспышку оттенков.")
    $ Fl.say(Fl_th, "Сходить покурить что ли.")
    $ Fl.AttackMaster(False)
    $ Fl.say(Fl_r, "Но крепкая мужская рука, что упала мне на плечо прервала мои планы.")

    show msk evilsmile pioneer with Fl_dissolve1

    $ Fl.say(Fl_msk, "Янчик, даров!")

    show msk surprise pioneer with Fl_fast

    $ Fl.say(Fl_msk, "Ух тыж, <бл*> нифига ты побрился!", _with=hpunch)
    $ Fl.say(Fl_th, "Да неужели я так плохо выглядел с бородой?")

    show msk evilsmile pioneer with Fl_fast

    show Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Неееее.")
    $ Fl.say(Fl_th, "Ладно признаю, ты был прав. Может наконец-то я стал похож на человека.")
    $ Fl.say(Fl_kvl, "Так так, мне не послышалось? Можешь повторить?")
    $ Fl.say(Fl_th, "Ага, обязательно!")
    hide Fl_vignette with Fl_dissolve1

    $ Fl.say(Fl_r, "Нарушителем моего одиночества оказался никто иной, как Михалыч. Император юморной категории {w}в пионерской форме.")
    $ Fl.PlayMusic("Fl_dogonyalki", 1, 4)
    $ Fl.say(Fl_gg, "Какие люди. Вижу тебя вожатая всё же заставила переодеться.")

    show msk sad pioneer with Fl_dissolve1

    $ Fl.say(Fl_msk, "Ага, достала уже со своими нравоучениями. Эта форма <п*здец> какая неудобная.")
    $ Fl.say(Fl_r, "Тут было тяжело не согласиться. Я привык носить свободную одежду, но тут был другой случай. Правда судя по всему я ещё и форму неправильно надел. Миха заправил рубашку и галстук криво, но завязал. Я же это всё успешно проигнорировал...")
    $ Fl.say(Fl_gg, "И не говори.")

    show msk smile2 pioneer with Fl_dissolve1

    $ Fl.say(Fl_msk, "Ты главное нормально её натяни, а то вожатая докопается.")
    $ Fl.say(Fl_r, "После чего, я наспех заправил рубашку и по примеру Михана накинул галстук.")

    show msk evilsmile pioneer with Fl_fast

    $ Fl.PlaySound("Fl_msk_laugh", 1, 0, False)
    $ Fl.say(Fl_msk, "Ну вылитый пионер ё-маё!")
    $ Fl.say(Fl_th, "<Бл*> мне вот так ходить до конца смены? Капец как неудобно.")
    $ Fl.say(Fl_gg, "Ладно, Мих, что хотел?")

    show msk smile pioneer with Fl_fast

    $ Fl.say(Fl_msk, "Да тебя искал везде. Только у Кати узнал, что ты оказывается с Мику живёшь.")

    show msk happy2 pioneer with Fl_dissolve1

    $ Fl.say(Fl_r, "Миха сделал глупую ухмылку. Даже трудно представить, что он сейчас выкинет. Обычно такое выражение лица не предвещало ничего хорошего. {w}В голове пронеслись события в библиотеке.")
    $ Fl.say(Fl_msk, "И чё как? Успел «насмотреться» на Мику?")
    $ Fl.say(Fl_th, "Приехали, ещё один.")

    show Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Тили тили тесто жених и невеста.")
    $ Fl.say(Fl_th, "{mn}")
    hide Fl_vignette with Fl_dissolve1

    $ Fl.say(Fl_gg, "Да ничего такого. Просто живём вместе.")

    show msk happy pioneer with Fl_fast

    $ Fl.say(Fl_msk, "Ничё ещё успеешь, целая смена впереди для флирта!")
    $ Fl.say(Fl_th, "А я погляжу ты у нас время зря не теряешь в лагере.")

    show msk smile pioneer with Fl_dissolve1

    $ Fl.say(Fl_msk, "Лан я чё пришёл то... Скоро ужин, погнали хавать!")
    $ Fl.say(Fl_r, "Компания мне бы не помешала, да и с Миханом не соскучишься, так что я сразу дал добро.")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.StopMusic(5)
    $ Fl.StopAmbience(5)
    scene bg Fl_black with Fl_dissolve2


    $ Fl.Pause(6.0)
    $ Fl.PlayAmbience("Fl_dining_hall_full", 1, 4)
    scene bg Fl_int_dining_hall_people_sunset with Fl_dissolve2
    $ Fl.Pause(1.5)
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_r, "Столовая была как обычно забита, хотя горн прозвучал минуту назад и нам с Михой пришлось перейти на бег.")
    $ Fl.say(Fl_gg, "Мда уж, хоть свободный столик найдём?")

    show msk evilsmile pioneer with Fl_dissolve1

    $ Fl.say(Fl_msk, "Не очкуй, Янчик, щас куда-то пришвартуемся!")
    $ Fl.say(Fl_r, "По довольной мине Михи можно было быть уверенным что он всё порешает, а вот каким способом уже никому неизвестно...")

    show msk happy2 pioneer with Fl_dissolve1

    $ Fl.say(Fl_msk, "Я же сказал решим этот вопрос!")
    $ Fl.say(Fl_r, "Бросив свой взгляд куда уставился Михалыч, я скривился.")
    $ Fl.Status("-20")
    $ Fl.Status("tension", False)
    $ Fl.say(Fl_th, "Не не только не с ней!")
    $ Fl.say(Fl_r, "За столиком, на который положил свой взгляд Миха, сидела Аня с ещё одной рыжей подружкой. {w}Вторую рыжую я уже успел заметить на линейке, а Аня своим взлобным взглядом уже тогда дала чёткий намёк не подходить к ней.")

    show Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Ну а что ты хотел, Ромэо? Ты же ей не принёс тогда цветы.")
    $ Fl.say(Fl_th, "Ага и теперь она может создать мне море проблем с вожаткой.")
    $ Fl.say(Fl_kvl, "То есть одержимую Мику ты не боишься, так и рвёшься к ней. А какую-то красноволосую девушку, что пригрозила тебе ты готов за киллометр избегать?")
    $ Fl.say(Fl_kvl, "Забей ты на вчерашний инцидент. К тому же с тобой Петросян вон, он вчера с ней вроде неплохо ладил.")
    $ Fl.say(Fl_th, "Кстати да...")
    hide Fl_vignette with Fl_dissolve1

    $ Fl.Status("+20")
    $ Fl.Status("normal", False)

    show msk serious pioneer with Fl_dissolve1

    $ Fl.say(Fl_msk, "Ян, ты чего завис? Погнали еда остынет же.")
    $ Fl.say(Fl_gg, "Да так неважно. Пошли уже составим компанию дамам.")
    $ Fl.say(Fl_th, "Чувствую когда-то общение с голосом в компании других ой как аукнется{mn}")
    $ Fl.HideScreens(_with=Fl_dissolve1)


    show msk smile pioneer with Fl_fast
    $ Fl.Pause(1.0)
    hide msk smile pioneer with Fl_dissolve1
    $ Fl.Pause(1.0)
    scene bg Fl_black with Fl_dissolve1


    $ Fl.Pause(2.0)
    scene bg Fl_int_dining_hall_people_sunset with Fl_effect_left1
    $ Fl.PlayMusic("Fl_divine_life_society", 1, 5)
    show Fl_chair3:
        xalign 0.52
    show al smile pioner1:
        ypos 0.07 zoom 1.0 xalign 0.52

    show Fl_chair3:
        xalign 0.1
    show an smile pioner1:
        ypos 0.07 zoom 1.0 xalign 0.1
    with Fl_dissolve1

    $ Fl.Pause(1.0)
    show Fl_chair3:
        xalign 0.95
    show msk smile pioneer:
        xalign 0.95
        Fl_pris2
    with Fl_dissolve1

    $ Fl.Pause(1.0)
    $ Fl.say(Fl_r, "И вот мы оказались в царстве рыжей компашки.")

    show an serious pioner1 with Fl_fast

    $ Fl.say(Fl_r, "Стоило Ане заприметить меня, как она тут же нахмурилась.")
    $ Fl.say(Fl_msk, "Ну чё, рыжики, такие хмурые?")

    show an smile pioner1 with Fl_dissolve1

    $ Fl.say(Fl_r, "Аня ещё раз посмотрела на меня, после чего сделала хитрую ухмылку. В голове красноволосой особы уже промелькнул какой-то план.")
    $ Fl.say(Fl_an, "Так так, кто тут у нас. Ян, у тебя должок забыл? Или я...")
    $ Fl.say(Fl_gg, "Да пофиг, могу хоть щас привести вожатую. Зачем пионерке ещё тратить своё свободное время чтобы сдать товарища.")
    $ Fl.say(Fl_r, "Я решил пойти в атаку первый. Лучший способ бороться с задирами, не дать им ту реакцию которую они ожидают.")

    show an serious angry pioner2 with Fl_fast

    $ Fl.say(Fl_an, "Думаешь, я шучу? Тебе же потом достанется от вожатой!")
    $ Fl.say(Fl_gg, "Ага. И что?")
    $ Fl.say(Fl_r, "На моём лице промелькнула ухмылка.")

    show msk shocked pioneer with Fl_fast

    $ Fl.say(Fl_msk, "Вы знакомы?")

    show an angry pioner1 with Fl_fast

    $ Fl.say(Fl_an, "Миша, это ты его научил своим приёмчиков?!", _with=hpunch)

    show msk serious pioneer with Fl_fast

    $ Fl.say(Fl_msk, "Ты чё орёшь на меня? Ничё я никого не учил!")

    show an serious pioner2 with Fl_dissolve1

    $ Fl.say(Fl_an, "Пф, ещё один смельчак...")
    $ Fl.say(Fl_r, "В этом коротком поединке я одержал вверх.")
    $ Fl.say(Fl_r, "Пионерка надулась и обиженно смотрела на меня.")

    show Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Сударь, я тебя не узнаю. В начале боялся подойти, а теперь спокойно поставил девушку на место.")
    $ Fl.say(Fl_th, "Ты же можешь заглянуть ко мне в голову. Так что чему ты удивляешься?")
    $ Fl.say(Fl_r, "В прошлой жизни после смерти подруги я стал очень холодным и грубым, в этом мире я почему-то об этом позабыл и так паршиво себя не вёл. Наверное потеря воспоминаний на это повлияло.")
    $ Fl.say(Fl_kvl, "А если она всё же расскажет вожатой, что ты некультурно выражаешься?")
    $ Fl.say(Fl_th, "Ну где мешки с сахаром мы уже знаем.")
    $ Fl.say(Fl_r, "От меня прозвучал сарказм, но почему-то это подняло нам двоим настроение.")
    hide Fl_vignette with Fl_dissolve1

    show al laugh pioner1 with Fl_dissolve1

    $ Fl.say(Fl_alp, "А ты забавный. {w}Так ты и есть тот самый новенький - Ян?")
    $ Fl.say(Fl_gg, "Он самый. А ты...")

    show al smile pioner1 with Fl_fast

    $ Fl.say(Fl_al, "Алиса - подруга вот этот надутой пионерки.")
    $ Fl.say(Fl_th, "Всё таки дуэт рыжих. Интересно, что из себя представляет Алиса{mn}")

    show an sad pioner2 with Fl_dissolve1

    $ Fl.say(Fl_an, "И ты туда же{mn}")
    $ Fl.say(Fl_al, "Ну не обижайся. Это ведь хорошо, что у нас ещё один серьёзный парень в отряде!")

    show an laugh pioner1 with Fl_fast

    $ Fl.say(Fl_an, "А ты права!")

    show an smile pioner1 with Fl_fast

    $ Fl.say(Fl_an, "Ян, я знаю как ты можешь исполнить свой долг.")
    $ Fl.say(Fl_th, "Ну что опять{mn}")
    $ Fl.say(Fl_r, "Я зациклился на пионерке.")
    $ Fl.say(Fl_an, "Мы сегодня планируем собраться после отбоя у нас в домике. Миша уже знает. Сейчас тебя в курс дела введём.")

    show msk upset pioneer with Fl_fast

    $ Fl.say(Fl_msk, "Так, я чё то вообще не догоняю. Что Миша уже знает?")

    show an angry pioner2 
    show al laugh pioner1
    with Fl_fast

    $ Fl.say(Fl_an, "Миша, не тупи блин!", _with=hpunch)
    $ Fl.say(Fl_an, "Мы сегодня планировали духов вызвать, ты забыл?")

    show msk smile pioneer with Fl_fast

    $ Fl.say(Fl_msk, "А это помню. Через доску хреныджи или как там её.")
    $ Fl.say(Fl_gg, "Доска Уиджи, откуда она у вас?")

    show an smile pioner1
    show al smile pioner1
    with Fl_fast

    $ Fl.say(Fl_al, "Да нашли её, когда гуляли в заброшенном корпусе.")
    $ Fl.say(Fl_al, "Вот решили почему бы не вызвать кого-то. Весело же будет.")
    $ Fl.say(Fl_th, "Обычно после вот такого веселья, герои ужастиков умирали...")
    $ Fl.say(Fl_msk, "Янчик, ты с нами?")
    $ Fl.say(Fl_gg, "Вызвать какую-то потусторонюю хрень? Ты как думаешь?")
    $ Fl.say(Fl_an, "Да ладно тебе, ты правда в веришь в приведений?")
    $ Fl.say(Fl_th, "Ещё одна фраза после которой...")

    show Fl_vignette with Fl_dissolve1
    $ Fl.say(Fl_kvl, "Да ладно сходи с ними. Ты же не будешь всю смену думать только о Мику!")
    $ Fl.say(Fl_th, "Да ну его. {w}Ну посидим мы, кто-то специально подёргает указатель и все начнут визжать. Знаю я как эти посиделки проходят.")
    $ Fl.say(Fl_kvl, "Сударь, ты упускаешь главную суть всего этого. {w}Хорошо провести время и возможность завести новые знакомства.")
    $ Fl.Pause(2.5)
    $ Fl.say(Fl_th, "Ладно ты прав. Это куда лучше, чем сидеть и забивать голову разными мыслями.")
    hide Fl_vignette with Fl_dissolve1

    $ Fl.say(Fl_r, "Меня прервала пионерка с голубыми волосами.")
    $ Fl.say(Fl_r, "Относя свой поднос, Мику пересеклась со мной зрительным контактом. На лице девушки читалась грусть. {w}Наверное она ожидала, что мы вместе поужинаем, а я оставил её в одиночестве и сижу веселюсь с другими.")
    $ Fl.StopMusic(4)

    scene bg Fl_int_dining_hall_people_sunset with Fl_effect_left1
    $ Fl.say(Fl_r, "Не в силах больше смотреть на грустную мордашку японки, я резко вскочил и собирался уже пойти за ней, как меня остановили.")
    $ Fl.say(Fl_an, "Ян, ты куда?!")
    $ Fl.say(Fl_gg, "Да я вспомнил, что у меня ещё дела есть.")
    $ Fl.say(Fl_an, "А вызов духов?")
    $ Fl.say(Fl_gg, "Да-да, я приду. После отбоя верно?")
    $ Fl.say(Fl_r, "Я рванул к выходу, по следам двух длинных хвостиков.")
    $ Fl.say(Fl_al, "Да подожди! Номер дома хоть знаешь?")
    $ Fl.say(Fl_r, "Но я не ответил, словно под гипнозом или чарами я сокращал растояние до двери.")
    $ Fl.say(Fl_al, "23 домик, в 10 вечера!")
    $ Fl.HideScreens(_with=Fl_dissolve1)
    $ Fl.PlaySound("Fl_open_door_2", 1, 0, False)
    scene bg Fl_black with Fl_effect_1
    $ Fl.StopAmbience(3)


    $ Fl.Save("День2: Прогулка с Микуськой")
    $ Fl.Pause(3.0)
    $ Fl.PlayAmbience("Fl_camp_center_evening", 1, 4)
    $ Fl.AutoSave()
    scene bg Fl_ext_dining_hall_near_sunset
    show Fl_light_c
    with Fl_effect_1
    $ Fl.ShowScreens(_with=Fl_dissolve1)
    $ Fl.say(Fl_gg, "Мику, подожди!", _with=hpunch)
    $ Fl.say(Fl_r, "Девушка и не планировала останавливаться, казалось она пропустила мимо ушей мои слова. Но я решил не сдаваться.")

    scene bg Fl_ext_dining_hall_away_sunset
    show Fl_light_c
    with Fl_fast
    $ Fl.say(Fl_gg, "Мику, подожди.")
    $ Fl.say(Fl_r, "Уже более сдерженно сказал я.")

    show mi upset pioneer3 with Fl_dissolve1

    $ Fl.say(Fl_r, "Наконец-то Мику обратила на меня внимание.")
    $ Fl.say(Fl_th, "Походу она действительно на меня обиделась, за то что проигнорил её на ужине.")
    $ Fl.say(Fl_mi, "Привет, Ян...")
    $ Fl.say(Fl_th, "Так формально{mn} Надо это исправлять.")
    $ Fl.say(Fl_gg, "Прости, что не смог с тобой поужинать. {w}Просто пока за формой забежал, потом на склад за станком, а там уже Миха меня перехватил в столовую.")

    show mi normal pioneer3 with Fl_fast

    $ Fl.say(Fl_mi, "Это заметно. Ты теперь как настоящий пионер!")
    $ Fl.say(Fl_gg, "Служу советскому союзу!")
    $ Fl.say(Fl_th, "Если я конечно в совок попал.")

    $ Fl.PlaySound("Fl_mi_laugh", 1, 0, False)
    show mi laugh pioneer1 with Fl_fast

    $ Fl.say(Fl_mi, "Верим верим, товарищ Ленин!")

    show mi pity smile pioneer2 with Fl_dissolve1

    $ Fl.say(Fl_mi, "Так непривычно смотреть на тебя без щетины.")
    $ Fl.say(Fl_gg, "Это да, сам себя странно чувствую без неё.")

    show mi normal pioneer3 with Fl_dissolve1

    $ Fl.say(Fl_mi, "Но тебе очень идёт! Правда правда!")
    $ Fl.say(Fl_r, "Мне было очень приятно слышать подобный комплимент, что мысленно отчитал себя за то что забил на свой внешний вид.")
    $ Fl.say(Fl_mi, "Янечка, постой на месте.")

    hide mi normal pioneer3 with Fl_dissolve1

    $ Fl.say(Fl_r, "Мику приблизилась ко мне. И поднесла руки к моей шее.")
    $ Fl.Status("-20")
    $ Fl.Status("tension", False)
    $ Fl.Pause(3.0)
    $ Fl.say(Fl_r, "Но ничего странного не произошло. Она просто перевязала мне галстук, наверное так как он и должен был изначально завязан - правильно.")

    show mi shy3 pioneer3 with Fl_dissolve1

    $ Fl.say(Fl_mi, "Теперь ты настоящий пионер.")
    $ Fl.Status("+30")
    $ Fl.Status("good", False)
    $ Fl.say(Fl_r, "Японка мило засмушалась, а я лишь мягко улыбнулся ей в ответ.")
    $ Fl.say(Fl_gg, "Спасибо.")

    show mi smile pioneer2 with Fl_fast

    $ Fl.say(Fl_mi, "Пионеры должны помогать товарищам. А ты ещё и мой член кружка!")
    $ Fl.say(Fl_gg, "Ты кстати в музклуб шла?")

    show mi normal pioneer3 with Fl_fast

    $ Fl.say(Fl_mi, "Ага.")
    $ Fl.say(Fl_gg, "Ну тогда пошли. Есть идеи чем можно заняться?")

    show mi joy pioneer3 with Fl_fast

    $ Fl.say(Fl_mi, "Я думаю, музклуб может подождать. У меня есть идея получше.")
    $ Fl.say(Fl_r, "Почему то в мою голову пришла не та мысль, которая должна была прийти нормальному человеку.")
    $ Fl.say(Fl_gg, "И что у тебя за идея?")
    $ Fl.say(Fl_mi, "Ян{mn}")
    if Ist_mi>=2:
        $ Fl.say(Fl_mi, "Не хочешь сходить со мной на пляж? Вчера был пляжный день и было очень много людей, а сегодня там должно быть меньше и вот я...")
        $ Fl.say(Fl_r, "По какой-то причине Мику снова занервничала и начала тараторить.")
        $ Fl.say(Fl_th, "Странно, я уже начинаю привыкать к этому. Есть в этой болтливости своя фишка.")
        $ Fl.say(Fl_gg, "Почему бы и нет.")

        show Fl_vignette with Fl_dissolve1
        $ Fl.say(Fl_kvl, "Сударь, у тебя то плавки есть? Или ты планируешь вновь перед Мику в труселях щеголять.")
        $ Fl.say(Fl_th, "Чёрт, точно! У меня же никаких своих вещей нет.")
        $ Fl.say(Fl_kvl, "А у тебя они разве были до переезда в Совёнок?")
        $ Fl.say(Fl_r, "С явной издёвкой задал мне вопрос голос.")
        $ Fl.say(Fl_th, "Да ты задолбал уже! Будешь вечно ссылаться на мою бедность в прошлой жизни?", _with=hpunch)
        $ Fl.say(Fl_kvl, "Ну иногда.")
        $ Fl.say(Fl_kvl, "И не стой столбом, а то действительно начнут тебя считать сумашедшим с вот этими выпадами из реальности во время разговора.")
        hide Fl_vignette with Fl_dissolve1

        $ Fl.say(Fl_gg, "Но есть одна проблема{mn}")

        show mi smile pioneer2 with Fl_fast

        $ Fl.say(Fl_mi, "Плавки с собой не взял?")
        $ Fl.say(Fl_th, "Неужели это так легко прочесть? Или такая проблема тут у многих пионеров?")
        $ Fl.say(Fl_r, "Интуиция девушки меня поразила.")

        show mi happy pioneer2 with Fl_fast

        $ Fl.say(Fl_mi, "Не переживай, у меня есть.")

        $ Fl.Status("-20")
        $ Fl.Status("normal", False)
        $ Fl.Pause(1.5)
        $ Fl.say(Fl_gg, "Мику{mn} а что делают у тебя мужские плавки?")

        show mi look away pioneer3 with Fl_dissolve1

        $ Fl.say(Fl_mi, "А это секрет.")
        $ Fl.say(Fl_gg, "{mn2}")
        $ Fl.Pause(2.0)

        $ Fl.PlaySound("Fl_mi_laugh", 1, 0, False)
        show mi laugh pioneer1 with Fl_dissolve1

        $ Fl.say(Fl_mi, "Ты о чём там подумал, глупенький?")

        show mi normal pioneer3 with Fl_fast

        $ Fl.say(Fl_mi, "Я просто когда собирала багаж то случайно прихватила папины плавки...")
        $ Fl.say(Fl_gg, "А-а-а-а-а...")

        $ Fl.PlaySound("Fl_mi_laugh", 1, 0, False)
        show mi laugh pioneer1 with Fl_fast

        $ Fl.say(Fl_mi, "Ян, ты такой забавный!")
        $ Fl.say(Fl_th, "Что-то я отупел за этот день{mn}")
        $ Fl.say(Fl_gg, "Сама виновата, что ставить меня в такое положение.")

        show mi normal pioneer3 with Fl_fast

        $ Fl.say(Fl_mi, "Ну извини. {w}Так мы пойдём на пляж?")
        $ Fl.say(Fl_gg, "Ну если проблема с плавками решена, то пошли.")
        $ Fl.HideScreens(_with=Fl_dissolve1)
        scene bg Fl_black with Fl_dissolve2


        $ Fl.Pause(5.0)
        $ Fl.AutoSave()
        scene bg Fl_ext_house_of_mi_sunset
        show Fl_light_c
        with Fl_dissolve2
        $ Fl.Status("+30")
        $ Fl.Status("good", False)
        $ Fl.ShowScreens(_with=Fl_dissolve1)
        $ Fl.say(Fl_r, "Я стоял у двери своего дома, точнее нашего. {w}Мику предложила переодеться сразу в домике, а я лишь поддержал эту мысль.")
        $ Fl.say(Fl_th, "Вот собственно и настал мой пляжный сезон.")

        show Fl_vignette with Fl_dissolve1
        $ Fl.say(Fl_kvl, "Ты уверен, что идти куда-то с Мику хорошая идея?")
        $ Fl.say(Fl_th, "А что не так?")
        $ Fl.say(Fl_kvl, "Ну если она решит тебя утопить, то потом не проси меня о помощи!")
        $ Fl.say(Fl_th, "Слушай, ты сильно накручиваешь. Да мы не знаем что именно произошло утром, но смотри! С Мику всё нормально, обычная милая девушка!")
        $ Fl.say(Fl_kvl, "Ну-ну.")
        $ Fl.say(Fl_kvl, "Сударь, насколько я помню. {w}Ты же плавать не умеешь?")
        $ Fl.say(Fl_th, "{mn}")
        $ Fl.say(Fl_r, "Я действительно не умел плавать. В детстве отец пару раз пытался научить, я но постоянно тонул... {w}Двоюродный брат тоже попытался научить, но закончилось моим наблюдением - как вода всё сильнее скрывала от меня ясные лучи солнца...")
        $ Fl.say(Fl_r, "Не знаю чему стала причина моему неумению плавать, то ли никто не хотел тратить на это время, то ли мои проблемы с лёгкими из-за чего я не мог контролировать дыхание, находясь в воде.")
        $ Fl.say(Fl_kvl, "Что планируешь делать?")
        $ Fl.say(Fl_th, "Что-что, Мику попрошу научить.")
        $ Fl.say(Fl_kvl, "Ладно, Ромэо, иди к своей Джульэте.")
        $ Fl.say(Fl_th, "И как я с Сударя превратился в Ромэо?")
        $ Fl.say(Fl_kvl, "Ну он же в конце помер, вот и тебя твоя яндере на тот свет унесёт.")
        $ Fl.say(Fl_th, "Я {w}повторяю {w}с Мику {w}всё хорошо!")
        $ Fl.say(Fl_kvl, "Как скажешь.")
        $ Fl.HideScreens(_with=Fl_dissolve1)
        hide Fl_vignette with Fl_dissolve1


        $ Fl.Pause(2.0)
        $ Fl.PlaySound("Fl_open_door_2", 1, 0, False)
        show mi normal pioneer3 with Fl_effect_down1


        $ Fl.ShowScreens(_with=Fl_dissolve1)
        $ Fl.say(Fl_r, "Из двери вышла голубоволосая девушка с милой улыбкой на лице. В руках она держала сумку, её содержимое было предельно понятно - полотенца, крем от загара и прочие атрибуты для похода на пляж.")
        $ Fl.say(Fl_th, "Какая же она милашка, я не могу.")
        $ Fl.say(Fl_r, "С каждым разом мои чувства к Мику менялись. Я словно метался между двух огней. Голос и я от части считаем её опасной, но всё неизвестное манит человека. Может поэтому я хожу по тонкому льду с целью узнать болтливую пионерку получше.")
        $ Fl.say(Fl_mi, "Я готова!")
        $ Fl.say(Fl_mi, "Теперь твоя очередь переодеваться, я тебя за дверью подожду.")
        $ Fl.say(Fl_gg, "Хорошо, я мигом!")

        hide mi normal pioneer3 with Fl_effect_down1

        $ Fl.say(Fl_r, "Мику ещё раз мне улыбнулась и освободила проход.")
        $ Fl.HideScreens(_with=Fl_dissolve1)
        $ Fl.PlaySound("Fl_open_door_2", 1, 0, False)
        scene bg Fl_black with Fl_dissolve1


        $ Fl.Pause(3.0)
        scene bg Fl_int_house_of_mi_sunset with Fl_dissolve1
        $ Fl.ShowScreens(_with=Fl_dissolve1)
        $ Fl.say(Fl_r, "Я пулей влетел внутрь и оглянулся.")
        $ Fl.say(Fl_r, "Мику уже подготовила мне плавки с узором в набросок цветов, отдалёно напоминащие стиль гавайки.")
        $ Fl.say(Fl_th, "Неплохо!")
        $ Fl.HideScreens(_with=Fl_dissolve1)


        $ Fl.PlaySound("Fl_pause_time", 1.0, 2, False)
        scene Fl_pause
        with Fl_effect_time_pause

        $ Fl.Pause (3.5)
        scene bg Fl_black with Fl_dissolve2
        $ Fl.Pause (1.5)

        scene bg Fl_int_house_of_mi_sunset with Fl_dissolve2
        $ Fl.ShowScreens(_with=Fl_dissolve1)
        $ Fl.say(Fl_r, "Покончив с таким пустяковым делом, я был полностью готов к пляжному отдыху.")
        $ Fl.say(Fl_gg, "Ну пора.")

        show Fl_vignette with Fl_dissolve1
        $ Fl.say(Fl_kvl, "Подожди.")
        $ Fl.say(Fl_th, "Ну что опять?")
        $ Fl.say(Fl_r, "С ноткой раздражения задал я вопрос голосу.")
        $ Fl.say(Fl_kvl, "Помнишь мы обсуждали про странную ауру в доме?")
        $ Fl.say(Fl_th, "Проклятие 13 дома{mn}")
        $ Fl.say(Fl_r, "Вспоминания о рассказе Кати тяжело вбились мне в виски.")
        $ Fl.say(Fl_kvl, "Возможно это не просто байки и что-то в этом доме действительно есть. Меня словно выталкивает из твоей головы. Нигде подобного не ощущал кроме присуствия Мику, но тут{mn}")
        $ Fl.say(Fl_th, "Всё же от странностей нам не убежать...")
        $ Fl.say(Fl_kvl, "Если хочешь то можешь что-то разузнать об этом подробнее, а можешь и забить на это. Но будь готов к тому, что если что-то произойдёт с тобой внутри этого дома, меня может не быть рядом и я ни чем помочь не смогу.")
        $ Fl.Status("-20")
        $ Fl.Status("normal", False)
        $ Fl.say(Fl_r, "Как бы меня голос не бесил, но вот резкая его потеря куда страшнее его вечных подколов.")
        $ Fl.say(Fl_th, "Хорошо я займусь этим, а ты информируй меня как ты под воздействием ауры.")
        $ Fl.say(Fl_kvl, "Договорились.")
        $ Fl.say(Fl_kvl, "Ладно иди уже к своей Микуське.")
        hide Fl_vignette with Fl_dissolve1
        $ Fl.HideScreens(_with=Fl_dissolve1)
        $ Fl.StopAmbience(4)
        scene bg Fl_black with Fl_dissolve2


        $ Fl.Pause (5.5)
        $ Fl.PlayAmbience("Fl_lake_shore_evening", 1, 4)
        scene bg Fl_ext_beach_sunset
        show Fl_light_c
        with Fl_dissolve2
        $ Fl.Pause (1.5)
        $ Fl.Status("+20")
        $ Fl.Status("good", False)
        $ Fl.ShowScreens(_with=Fl_dissolve1)
        $ Fl.say(Fl_r, "Медленно, но верно солнце стремительно уходило за горизонт. Время отбоя приближалось, но едва ли нас с Мику это волновало.")

        show mi normal swim3 with Fl_dissolve2

        $ Fl.PlayMusic("Fl_dorama_kt1", 1, 4)
        $ Fl.say(Fl_mi, "Я тут!")
        $ Fl.say(Fl_th, "{mn}")
        $ Fl.Status("+10")
        $ Fl.Status("euphoria", False)
        $ Fl.say(Fl_r, "Признаться честно у меня челюсть отвисла от увиденного.")
        $ Fl.say(Fl_r, "Мику явилась передо мной в очень красивом купальнике, идеально сочетающий с её цветом волос. Трудно передать оценку пляжного наряда девушки, слишком он уж идёт ей.")
        $ Fl.Status("-10")
        $ Fl.Status("good", False)
        $ Fl.say(Fl_r, "Но я быстро взял себя в руки.")
        $ Fl.say(Fl_th, "Да уж, меня так удивил купальник, а нижнее бельё что продемонстрировала пионерка вчера ночью - ни капельки...")

        show mi pity grin swim2 with Fl_dissolve1

        $ Fl.say(Fl_mi, "Как тебе?")
        $ Fl.say(Fl_r, "Спросила Мику, покрутившись передо мной чтобы я мог оценить её купальник.")
        $ Fl.say(Fl_gg, "Тебе очень идёт.")

        show mi happy2 swim2 with Fl_dissolve1

        $ Fl.say(Fl_mi, "Я рада что он тебе понравился!")

        show mi grin swim2 with Fl_fast

        $ Fl.say(Fl_mi, "Ты кстати тоже классно смотришься!")
        $ Fl.say(Fl_r, "Я перевёл взгляд вниз, где вовсю красовались батины плавки.")
        $ Fl.say(Fl_th, "Ну в принципе сойдёт, лучше чем в трусах.")

        show mi grin swim2 at Fl_bg_zoom_e(1.5, 1.5, 0.7, 0.5, -5.0, 0.35, 0.35)

        $ Fl.AttackMaster()
        $ Fl.say(Fl_mi, "Ян, догоняй!")
        $ Fl.say(Fl_r, "Стоило на мгновение отвести взгляд от аквамариновой пионерки, как она уже упархнула в воду.")
        $ Fl.say(Fl_th, "Ну ладно. {w}Главное ощущать дно, а то сам пойду потом на дно...")
        $ Fl.HideScreens(_with=Fl_dissolve1)
        $ Fl.Master(Fl_bg_zoom_to_e(1.38, 3.0, 0.62, 0.47))


        $ Fl.Pause (4.0)
        $ Fl.ShowScreens(_with=Fl_dissolve1)
        $ Fl.say(Fl_r, "Когда моё тело погрузилось на половину я замер. Идти дальше не хотелось, опора под ногами резко исчезала, тем самым отделя меня от одного мига бесконечности и марева небытия.")
        $ Fl.say(Fl_r, "В отличие от меня, Мику спокойно себе ощущала в воде. Она улыбалась, зазывала к себе. Всего лишь один шаг и всё может измениться, всего лишь один шаг разделял меня от дна или цели. Всего лишь шаг...")
        $ Fl.say(Fl_mi, "Ну чего ты встал как в копанный?")
        $ Fl.say(Fl_r, "И этот самый шаг произошёл.")

        scene bg Fl_ext_beach_water_sunset
        show Fl_light_c
        with vpunch

        $ Fl.Status("-40")
        $ Fl.Status("tension", False)
        $ Fl.say(Fl_r, "Мику потянула меня к себе. Я же понял, что потерял опору под ногами.")
        $ Fl.say(Fl_mi, "Я держу, всё хорошо. Не переживай ты не утонешь.")
        $ Fl.say(Fl_r, "Но приобрёл новую опору.")
        $ Fl.say(Fl_gg, "Мику, ты что творишь?!", _with=hpunch)

        $ Fl.PlaySound("Fl_mi_laugh", 1, 0, False)
        $ Fl.say(Fl_mi, "Дурачок ты всё таки. {w}Ты почему мне не сказал, что плавать не умеешь?")
        $ Fl.Status("+20")
        $ Fl.Status("normal", False)
        $ Fl.say(Fl_gg, "Догадалась...")
        $ Fl.say(Fl_mi, "Как тут не догадаешься, когда ты стоишь и смотришь на воду, думаешь идти или нет.")
        $ Fl.say(Fl_th, "Хотел бы я читать тебя как открытую книгу.")
        $ Fl.say(Fl_r, "Я вновь ощутил жар. Руки Мику были неестественно горячие, как и тогда. Тепло разносилось по всему телу, становилось дурно.")
        $ Fl.say(Fl_th, "Это ненормально. Не может быть у человека настолько горячая рука.")

        $ Fl.Pause (2.0)
        $ Fl.say(Fl_th, "Может она чем-то болеет? {w}Нет не в плохом плане, а что-то связанное с повышенной температурой тела или типо того.")
        $ Fl.say(Fl_r, "Я посмотрел на Мику. {w}Жизнерадостная пионерка не давала ни намёка на какой-то недуг.")
        $ Fl.say(Fl_gg, "Мику, а у тебя всегда такие горячие руки?")
        $ Fl.say(Fl_mi, "Ты о чём? Руки как руки...")
        $ Fl.say(Fl_th, "Значит сама Мику ничего странного в этом не замечает. {w}Снова себя лишний раз накручиваю и ищу какой-то подвох.")
        $ Fl.say(Fl_gg, "Забудь. Сейчас есть дела куда важнее.")
        $ Fl.say(Fl_mi, "И какие же?")
        $ Fl.say(Fl_r, "Ехидная улыбка девушки говорила сама за себя, что она и так знает ответ на свой же вопрос.")
        $ Fl.say(Fl_gg, "Научить меня плавать конечно же!")

        $ Fl.PlaySound("Fl_mi_laugh", 1, 0, False)
        $ Fl.say(Fl_mi, "Я уже думала не попросишь.")
        $ Fl.HideScreens(_with=Fl_dissolve1)


        $ Fl.PlaySound("Fl_pause_time", 1.0, 2, False)
        scene bg Fl_black
        with Fl_effect_time_pause

        $ Fl.Pause (4.5)
        scene bg Fl_ext_beach_water_sunset
        show Fl_light_c
        with Fl_dissolve2
        $ Fl.Pause (1.5)
        $ Fl.Status("+20")
        $ Fl.Status("good", False)
        $ Fl.ShowScreens(_with=Fl_dissolve1)
        $ Fl.say(Fl_r, "За короткий промежуток времени мне наконец-то получилось освоить всю прелесть от нахождения в воде.")
        $ Fl.say(Fl_r, "Рассекая волны, я без какого либа труда плавал в том же темпе что и Мику. {w}Не знаю как ей удалось научить меня плавать так быстро, но Мику определённо хороший учитель!")
        $ Fl.say(Fl_mi, "Ян, догоняй!")
        $ Fl.say(Fl_r, "Мику резко рванула вперёд, а я следом за ней.")
        $ Fl.say(Fl_gg, "Ну держись!")
        $ Fl.HideScreens(_with=Fl_dissolve1)

        $ Fl.Pause (2.5)
        $ Fl.ShowScreens(_with=Fl_dissolve1)
        $ Fl.say(Fl_r, "Стоило мне догнать пионерку, как её след тут же простыл.")
        $ Fl.say(Fl_th, "Да где же о{break}")
        $ Fl.AttackScreens(True)
        with Fl_flash
        $ Fl.say(Fl_mi, "Попался!", _with=hpunch)
        $ Fl.say(Fl_r, "Она застала меня в расплох. От чего последовал шквал воды мне прямо в лицо.")
        $ Fl.say(Fl_gg, "Хана тебе!")
        $ Fl.AttackScreens(True)
        $ Fl.Pause (1.5)
        $ Fl.AttackScreens(True)
        $ Fl.say(Fl_r, "Я начал создавать множество брызгов, Мику же оставалось отбиваться в слепую и принять поражение.")
        $ Fl.say(Fl_mi, "Всё всё, ты победил.")
        $ Fl.AttackScreens(True)
        $ Fl.say(Fl_mi, "Ахахах, ну хватит, Ян. Я проиграла.")
        $ Fl.say(Fl_gg, "Ты признаешь поражение?")
        $ Fl.say(Fl_mi, "Да, ты победил.")
        $ Fl.say(Fl_r, "Я остановился. {w}Но это была лишь уловка{break2}")
        $ Fl.AttackScreens(True)
        $ Fl.say(Fl_mi, "Получай!", _with=vpunch)
        $ Fl.say(Fl_th, "Ах ты хитрюга!")
        $ Fl.say(Fl_r, "Сократив дистанцию, я схватил Мику и начал тереть ей макушку.")
        $ Fl.say(Fl_mi, "Ай, прости прости. Я больше так не буду!")
        $ Fl.say(Fl_th, "Я больше на это не поведусь!")
        $ Fl.say(Fl_gg, "Точно не будешь?")
        $ Fl.say(Fl_mi, "Не буду, я признаю поражение.")
        $ Fl.StopMusic(4)
        $ Fl.say(Fl_r, "Неожиданно нарисовалась следующая картина. {w}Мы стояли очень близко друг другу. Наши взгляды были направлены друг на друга.")
        $ Fl.say(Fl_r, "Между нами появилась неловкая тишина. Мы не знали чего хотели, но явно ожидали чего.")

        $ Fl.Pause (4.5)
        $ Fl.say(Fl_mi, "Что-то становится прохладно. Может поплывём к берегу?")
        $ Fl.say(Fl_gg, "Да, конечно.")
        $ Fl.say(Fl_r, "Мику отплыла от меня.")
        $ Fl.Status("-40")
        $ Fl.Status("tension", False)
        $ Fl.say(Fl_r, "Почему то стало паршиво на душе.")
        $ Fl.say(Fl_th, "Что со мной вообще твориться? {w}Чего я добиваюсь от неё?")

        $ Fl.Pause (2.0)
        $ Fl.say(Fl_th, "Я запутался{mn}")
        $ Fl.say(Fl_r, "Мику уже стояла на берегу и одевалась. Я решил не заставлять её ждать, пока соберусь с мыслями.")
        $ Fl.HideScreens(_with=Fl_dissolve1)
        scene bg Fl_black with Fl_dissolve2


        $ Fl.Pause (5.5)
        scene bg Fl_ext_un_hideout_sunset
        show Fl_light_c
        with Fl_dissolve2
        $ Fl.ShowScreens(_with=Fl_dissolve1)
        $ Fl.Status("+40")
        $ Fl.Status("good", False)
        $ Fl.say(Fl_r, "Расходиться мы не хотели, поэтому после купания решили обсохнуть в части пляже где обычно никого нет.")
        $ Fl.say(Fl_r, "Закат завораживал. Я как маленький ребёнок любовался красками вечера изредка поглядывая на Мику.")
        $ Fl.say(Fl_r, "Пионерка молча любовалась закатом, улыбалась. Казалось что для неё ничего другого и не существует кроме огненного гиганта.")
        $ Fl.say(Fl_th, "Не понимаю, что в моей жизни происходит и чего на самом деле хочу. {w}Кажется всё что надо у меня есть, но в тоже время я пуст.")
        $ Fl.say(Fl_th, "Может эта музыканка и есть моё перерождение?")
        $ Fl.say(Fl_th, "Нет, это не любовь. Просто{mn}")
        $ Fl.say(Fl_th, "Я словно ожил. {w}Перерождение - это шанс начать всё с чистого листа. Вот только какой смысл от чистого листа если чернила закончились? Напечатать слишком просто, а взять готовый текст ещё проще.")

        $ Fl.Pause (2.0)
        $ Fl.say(Fl_th, "Наверное я в ней вижу отражение себя.")
        $ Fl.say(Fl_th, "Хотя тут можно с этим поспорить. Она лучшая версия меня.")
        $ Fl.say(Fl_th, "Каждый день люди за что-то борются, каждый день происходит маленькая битва с самими собой, каждый день мы находим результат этой борьбы.")
        $ Fl.say(Fl_th, "Мику с одиночеством. {w}Я с утратой.")
        $ Fl.HideScreens(_with=Fl_dissolve1)

        $ Fl.Pause (2.5)
        $ Fl.ShowScreens(_with=Fl_dissolve1)
        $ Fl.say(Fl_mi, "Ян.")
        $ Fl.say(Fl_gg, "Да?")
        $ Fl.say(Fl_mi, "Можно тебя кое о чём спросить?")
        $ Fl.say(Fl_r, "Девушка нервничала и это было слишком заметно.")
        $ Fl.say(Fl_gg, "Можешь спрашивать о чём угодно.")
        $ Fl.say(Fl_mi, "{mn}")
        $ Fl.say(Fl_mi, "Что скрывается под повязкой на твоей руке? Ты её не снял даже когда в воду зашёл.")
        $ Fl.say(Fl_gg, "{mn}")
        $ Fl.say(Fl_gg, "Прости, я не могу ответить на этот вопрос.")
        $ Fl.Status("-20")
        $ Fl.Status("normal", False)
        $ Fl.say(Fl_r, "Мой шрам, который я оставил на своём теле в тот раковой день, был для меня больной темой.")
        $ Fl.say(Fl_mi, "А говорил, что на любой ответишь.")
        $ Fl.say(Fl_r, "С грустной улыбкой на лице прозвучали слова пионерки.")
        $ Fl.say(Fl_th, "На любой кроме этого. Я не могу об этом говорить с каждым.")

        $ Fl.Pause (2.5)
        $ Fl.say(Fl_mi, "Ты под ней скрываешь шрам, так ведь?")
        $ Fl.Status("-20")
        $ Fl.Status("tension", False)
        $ Fl.say(Fl_r, "Я резко повернулся. Внутри всё напряглось.")
        $ Fl.say(Fl_gg, "Откуда ты{break}")
        $ Fl.say(Fl_mi, "Ты сам вчера рассказал, что потерял дорогого человека. Не трудно было догадаться.")
        $ Fl.say(Fl_gg, "{mn}")
        $ Fl.say(Fl_gg, "Давай закроем эту тему?")
        $ Fl.say(Fl_r, "В моём голосе было раздражение. Обсуждать попытку суицида меня выводила из себя. Эта ошибка была показателем моей слабости, от которой я так упорно пытался убежать...")
        $ Fl.say(Fl_mi, "Мне тоже когда-то было грустно. Да и сейчас мне очень тоскливо. Но это не выход...")
        $ Fl.say(Fl_th, "Я и без других знаю, что это не выход{mn} Но что оставалось делать, когда боль пожирала тебя изнутри, она сводила меня с ума{mn}")
        $ Fl.say(Fl_gg, "{mn}")
        $ Fl.say(Fl_gg, "А со мной тебе тоже тоскливо?")
        $ Fl.say(Fl_mi, "Нет.")
        $ Fl.say(Fl_mi, "Я наконец-то нашла человека, которого так долго искала.")
        $ Fl.say(Fl_r, "Мику откинулась на песок с улыбкой на лице. Её слова были искренними, что даже слегка пугало.")
        $ Fl.say(Fl_gg, "Вот как.")
        $ Fl.say(Fl_mi, "А тебе?")
        $ Fl.say(Fl_gg, "Тоскливо ли мне?")
        $ Fl.say(Fl_mi, "Ага.")
        $ Fl.say(Fl_r, "Не став терять время на размышления, я уже знал для себя ответ на поставленный вопрос.")
        $ Fl.HideScreens(_with=Fl_dissolve1)
        

        scene bg Fl_ext_sky_sunset with Fl_effect_3
        $ Fl.ShowScreens(_with=Fl_dissolve1)
        $ Fl.Status("+40")
        $ Fl.Status("good", False)
        $ Fl.say(Fl_r, "Составив компанию девушке на песке, я ответил.")
        $ Fl.say(Fl_gg, "Неа. Я тоже нашёл человека, которого так долго искал.")
        $ Fl.say(Fl_r, "Мику поняла о ком шла речь и засмушалась.")
        $ Fl.say(Fl_gg, "Извини, не хотел смушать.")
        $ Fl.say(Fl_mi, "Да ничего подобного!", _with=hpunch)
        $ Fl.say(Fl_th, "Ещё и дуется, ты погляди!")
        $ Fl.HideScreens(_with=Fl_dissolve1)
        scene bg Fl_black with Fl_dissolve2


        $ Fl.Pause (6.5)
        $ Fl.DayTime("night", "night")
        $ Fl.Save("День2: Ночь. Мику.")
        $ Fl.PlayAmbience("Fl_lake_shore_night", 1, 4)
        scene bg Fl_ext_un_hideout_night
        show Fl_dust_full
        with Fl_dissolve2
        $ Fl.AutoSave()
        $ Fl.ShowScreens(_with=Fl_dissolve1)
        $ Fl.say(Fl_r, "Время пролетело незаметно. Ранее горячий песок стал враждебным, разрушая наш момент идилии.")
        $ Fl.say(Fl_gg, "Уже темно, может пойдём?")
        $ Fl.say(Fl_mi, "По домам?")
        $ Fl.say(Fl_gg, "Мы в одном домике живём глупышка.")
        $ Fl.say(Fl_mi, "Ой, точно!")
        $ Fl.say(Fl_r, "Мы обменялись улыбками.")
        $ Fl.say(Fl_mi, "Может перед сном сходим в баню? В такое время там никого нет, а мне так нравится баня ночью!")





    else:
        pass
    #Здесь развилка на одержим и истину



    ##Истинная##
    #Про форму и бороду.
    #Душ с Мику
    #Легенда про 13 дом.
    #Про шрам



    ##Промолчать##
    #Гг обещал зайти к Мику за тетрадью



    ##Очки##
    #Одержимость - (3-4)
    #Истинные - (2)
    #Доп - (2-3)

