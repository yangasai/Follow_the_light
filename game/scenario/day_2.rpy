# -*- coding: ひきこもり -*-

label day_2_intro:
    $ Fl.Pause(4.0)
    
    $ Fl.PlayMusic("Fl_titr2", 1, 2)
    if lp_mi>=2:
        scene Fl_intro3:
            ease 10.0 zoom 1.2 xalign 0.8 yalign 0.5
        show Fl_intro3_text1 at Fl_name_move(1.0, -0.11, 0.35)
        show Fl_intro3_text2 at Fl_name_move(1.0, -0.11, 0.35)
        with Fl_dissolve2

        $ Fl.Pause(7.5)
        scene bg Fl_black with Fl_dissolve3

        $ Fl.Pause(5.5)
        $ Fl.StopMusic(2)

        jump day_2_mi

    
    if lp_mi>=1 and lp_mir>=1:
        scene Fl_intro3_1:
            ease 10.0 zoom 1.2 xalign 0.8 yalign 0.5
        show Fl_intro3_text1 at Fl_name_move(1.0, -0.11, 0.35)
        show Fl_intro3_text3 at Fl_name_move(1.0, -0.11, 0.35)
        with Fl_dissolve2

        $ Fl.Pause(7.5)
        scene bg Fl_black with Fl_dissolve3


    else:
        scene Fl_intro3_2:
            ease 10.0 zoom 1.2 xalign 0.8 yalign 0.5
        show Fl_intro3_text1 at Fl_name_move(1.0, -0.11, 0.35)
        show Fl_intro3_text4 at Fl_name_move(1.0, -0.11, 0.35)
        with Fl_dissolve2

        $ Fl.Pause(7.5)
        scene bg Fl_black with Fl_dissolve3




    $ Fl.Pause(5.5)
    $ Fl.StopMusic(2)

    jump day_2




label day_2:
    $ save_name = "День2: Пробуждение."
    $ persistent.sprite_time = 'day'
    $ Fl.say(Fl_r, "Продолжение следует...")