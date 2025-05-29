# -*- coding: ひきこもり -*-
label splashscreen:
    $ Fl.DefaultVariables()
    $ Fl.Pause(0.1)

    $ Fl.PlaySound("Fl_rotation", 1, 0, False)
    show Fl_preview
    $ Fl.Pause(3.0)
    scene bg Fl_black with Fl_dissolve2

    $ Fl.Pause(2.0)
    scene layer:
        subpixel True
        truecenter
        yalign 0.85
        zoom 1.26
        ease 8.5 yalign 0.1 zoom 1.0
    with Fl_dissolve2
    show text_1 at zoom_repeat(1.4, 1.0, 1.05, 1.35, 1.15, 0.25, 3.7)
    $ Fl.Pause(5.4)
    scene bg Fl_black with Fl_flash_fast

    $ Fl.Pause(2.0)

    python:
        from time import localtime, strftime
        t = strftime("%H:%M:%S", localtime())
        hour, min, sec = t.split(":")
        hour = int(hour)

    if hour in [22,23,24,0,1,2,3,4,5,6]:
        call screen Fl_disclaimer_night with Fl_dissolve1
        screen Fl_disclaimer_night:
            modal True
            tag menu
            add "disclaimer_night"
            imagebutton:
                idle "images/preview/disclaimer_night.jpg" 
                hover "images/preview/disclaimer_night.jpg" 
                action Hide("Fl_disclaimer_night", Dissolve(1.0)), Return()

    elif hour in [20,21] or hour in [7,8]:
        call screen Fl_disclaimer_sunset with Fl_dissolve1
        screen Fl_disclaimer_sunset:
            modal True
            tag menu
            add "disclaimer_sunset"
            imagebutton:
                idle "images/preview/disclaimer_sunset.jpg" 
                hover "images/preview/disclaimer_sunset.jpg" 
                action Hide("Fl_disclaimer_sunset", Dissolve(1.0)), Return()

    else:
        call screen Fl_disclaimer_day with Fl_dissolve1
        screen Fl_disclaimer_day:
            modal True
            tag menu
            add "disclaimer_day"
            imagebutton:
                idle "images/preview/disclaimer_day.jpg" 
                hover "images/preview/disclaimer_day.jpg" 
                action Hide("Fl_disclaimer_day", Dissolve(1.0)), Return()

    $ Fl.Pause(3.0)


    $ Fl.PlayMusic("Fl_detroit", 1, 3)
    $ Fl.Pause(1.5)
    scene bg Fl_black
    $ Fl.Pause(1.5)
    #$ config.allow_skipping = False
    call screen Fl_loading(0.25) with Fl_fast
    $ Fl.StopMusic(2)
    $ Fl.Pause (2.5)
    #$ config.allow_skipping = True

    return

