# -*- coding: ひきこもり -*-

init -100 python:

    store.selected_slot = "_"
    persistent._file_page = 1


init python in Fl:

    serial_number = 0

    def serial():

        global serial_number
        serial_number += 1
        return serial_number




init -150 python in Fl:

    from sys import prefix
    import store, random, inspect, datetime, re, os

    Settings, Show, Hide, Play, Stop, Set, Call, Jump, Scene, With, Action, Statement, Dysplayable = range(0, 13)
    


    sunset_sprite_color = (0.94, 0.82, 1.0)
    night_sprite_color = (0.63, 0.78, 0.82)


    def SpritesReg(character, attribs, size = "normal"):
        global sunset_sprite_color, night_sprite_color
        
        vals = {"normal":(900,1080),"far":(675,1080)}
        comp = str(vals[size])
        for attrib in attribs:
            comp=comp+',(0,0), "sprites/'+size+'/'+character+'/'+attrib+'.png"'
        return(renpy.display.layout.ConditionSwitch("persistent.sprite_time=='sunset'",renpy.display.im.MatrixColor( eval("renpy.display.im.Composite("+comp+")"), renpy.display.im.matrix.tint(sunset_sprite_color[0],sunset_sprite_color[1],sunset_sprite_color[2]) ),"persistent.sprite_time=='night'",renpy.display.im.MatrixColor( eval("renpy.display.im.Composite("+comp+")"), renpy.display.im.matrix.tint(night_sprite_color[0],night_sprite_color[1],night_sprite_color[2]) ),True,eval("renpy.display.im.Composite("+comp+")") ))
    



    def say(who, what="", voice=None, sound=None, start_voice=False, start_sound=False,
            end_voice=False, end_sound=False, at=[], behind=[], zorder=0, master=None, screens=None,
            interact=True, cps=None, bold=False, font=None, timer=None, veiled=False, extend=None,
            dis=False, trans="", show_effect=None, hide_effect=None, _with=None):
        """
        IN:
            who - <character> / <text>
            image - <emotion> <extra> <distance> / <text>
            what - <text>
            voice - string
            sound - string
            start_voice - int
            start_sound - int
            end_voice - int
            end_sound - int
            at - expression
            behind - string
            zorder - int
            master - expression
            screens - expression
            interact - True/False
            cps - int
            bold - int
            font - expression
            timer - int
            extend - "save"/True
            dis - True/False
            trans - expression
            show_effect - string
            hide_effect - string
            _with - expression
        TYPE:
            Statement
        """
        
        if _with:
            renpy.game.interface.set_transition(_with)
        if master:
            if master in [store.Fl_screen_attack, store.Fl_screen_attack_hard]:
                store.Fl.Master()
            store.Fl.Master(master, False)
        what = "{cps=" + str(cps) + "}" + what + "{/cps}" if cps else what
        what = TextTags(TextSwear(what, veiled))
        renpy.say(who, what, interact)
        if timer:
            store.Fl.Timer(timer)


    def Timer(time, label=None):
        ui.timer(time, ui.jumps(label) if label else store.Return())


    def Return():
        renpy.return_statement()


    def DefaultVariables():
            store.Fl_inventory = []
            for slot in range(0, 4):
                store.Fl_inventory.append({"slot":slot, "name":"empty", "stats":None})
            for slot in range(4, 8):
                store.Fl_inventory.append({"slot":slot, "name":"lock", "stats":None})
            store.Fl_status_action = False
            store.Fl_complete = {"status":False, "inventory":False}
            store.Fl_status_points = [15, "depression"]
            store.Fl_status_name = ""
            store.Fl_status = ""
            store.Fl_status_color = "#FF0000"
            store.Fl_time = 0
            store.Fl_save_text = ""
            store.Fl_after_load = False
            store.save_name = ""
            store.Fl_block_keys = False
            store.Fl_screens = False
            store.Fl_sprite_time = "night"
            store.Fl_timeofday = "day"
            store.Fl_hover_slot = {"slot":None, "name":"empty", "stats":None}
            store.Fl_backpack = {"slot":"BPK", "name":"empty", "stats":None}
            store.Fl_weapon = {"slot":"WPG", "name":"lock", "stats":None}
            store.Fl_show_items_window = False
            store.persistent._file_page = "FilePage_1"


    def ScreensActivate(loop=False):
            if store.Fl_config_interface:
                store.config.window_title = store.Fl_config_mod_name

    def TransformsCheckList(at):
        list = []
        if "," not in str(at).replace("rpy\',", ""):
            list.append(at)
        elif len(at) >= 1:
            for item in range(0, len(at)):
                list.append(at[item])
        return list


    def Mapoverlay(at=None, reset=True):
        at = store.Fl_screen_normal(0) if not at else TransformsCheckList(at)
        renpy.show_layer_at(at, "mapoverlay", reset)


    def ModIdentify(name, author, label, font=None, color=None):
            """
            NOTE:
                Совместимость с фильтром «Табличный (альбомный) список модов»
            IN:
                name - string
                label - string
                folder - string
                font - string
                color - string
            TYPE:
                Settings
            """
            store.Fl_config_mod_name = name

    def IsModActive():
        return store.save_name.find(store.Fl_config_mod_name) != -1


    def Save(name="", text=True):
        if text:
            store.save_name = name



    def CallbackOnLoad(slot):
            try:
                if store.persistent.Fl_on_save_timeofday[slot]:
                    store.persistent.timeofday = store.persistent.Fl_on_save_timeofday[slot][0]
                    store.persistent.sprite_time = store.persistent.Fl_on_save_timeofday[slot][1]
                    store.persistent.font_size = store.persistent.Fl_on_save_timeofday[slot][2]
                    store.persistent.hentai = store.persistent.Fl_on_save_timeofday[slot][3]
                    store._preferences.volumes["music"] = store.persistent.Fl_on_save_timeofday[slot][4]
                    store._preferences.volumes["sfx"] = store.persistent.Fl_on_save_timeofday[slot][5]
                    store._preferences.volumes["voice"] = store.persistent.Fl_on_save_timeofday[slot][6]
        
            except:
                pass


    def CallbackOnSave(slot):
            if not store.persistent.Fl_on_save_timeofday:
                store.persistent.Fl_on_save_timeofday = {}
            store.persistent.Fl_on_save_timeofday[slot] = (store.persistent.timeofday, store.persistent.sprite_time, store.persistent.font_size, store.persistent.hentai, store._preferences.volumes["music"], store._preferences.volumes["sfx"], store._preferences.volumes["voice"])






    def DayTime(typein, typesp, day=True, sprites=True):
            if day:
                store.Fl_timeofday = typein
            if typein == "prologue":
                typein == "day"
            if sprites:
                store.Fl_sprite_time = typesp
            store.persistent.sprite_time = store.Fl_sprite_time


    #Теги текста
    def TextSwear(name, veiled):
        if "<" in name:
            if store.persistent.Fl_swear_filter:
                for item in range(0, len(re.findall("<", name))):
                    item = name[name.find("<")+1:name.find(">")].lower()
                    if item in store.Fl_swear_dict:
                        if not veiled:
                            if name[name.find("<")+1:name.find(">")].replace(" ", "").istitle():
                                name = name[:name.find("<")] + store.Fl_swear_dict[item].title() + name[name.find(">")+1:]
                            elif name[name.find("<")+1:name.find(">")].isupper():
                                name = name[:name.find("<")] + store.Fl_swear_dict[item].upper() + name[name.find(">")+1:]
                            else:
                                name = name[:name.find("<")] + store.Fl_swear_dict[item] + name[name.find(">")+1:]
                        else:
                            word = name[name.find("<")+1:name.find(">")]
                            name = name[:name.find("<")+3].replace("<", "") + "*" * (len(word)-2) + name[name.find(">")+1:]
            else:
                name = Replace(name, ["<", "", ">", ""])
        return name


    def Replace(name, args=[]):
        for item in range(0, len(args), 2):
            name = name.replace(args[item], args[item+1])
        return name


    def TextTags(name):
        return Replace(name, ["{mn}", "{w=0.3}.{w=0.3}.{w=0.3}.",
                              "{mn2}", "{w=0.6}.{w=0.6}.{w=0.6}.",
                              "{break}", "...{w=0.5}{nw}",
                              "{break2}", "...{w=1.0}{nw}",])



    #layout.MAIN_MENU = 'Вы действительно хотите выйти в главное меню?\nНесохраненные данные будут потеряны.'
    #layout.ARE_YOU_SURE = "Вы уверены?"
    #layout.DELETE_SAVE = "Вы уверены, что хотите удалить это сохранение?"
    #layout.OVERWRITE_SAVE = "Вы уверены, что хотите переписать это сохранение?"
    #layout.LOADING = "Загрузка приведёт к потере несохранённых данных.\nВы уверены, что хотите сделать это?"
    #layout.QUIT = "Вы уверены, что хотите выйти?"
    #layout.SLOW_SKIP = "Вы уверены, что хотите начать пропуск?"
    #layout.FAST_SKIP_UNSEEN = "Вы уверены, что хотите пропустить всё до следующего выбора?"
    #layout.FAST_SKIP_SEEN = "Вы уверены, что хотите пропустить всё до следующего нового диалога или выбора?"

    

    #Воспроизведение и стоп(name-название, volume-громкость, t-fadein, l-loop)
    def PlayMusic(name, volume, t):
            renpy.music.set_volume(volume, delay=0, channel="music")
            renpy.music.play("audio/music/" + str(name) + ".ogg", channel="music", loop=True, fadeout=None, synchro_start=False, fadein=t, tight=None, if_changed=True)

    def PlayMusic2(name, volume, s, t):
            renpy.music.set_volume(volume, delay=0, channel="music")
            renpy.music.play("audio/music/" + str(name) + ".ogg", channel="music", loop=True, fadeout=None, synchro_start=s, fadein=t, tight=None, if_changed=True)

    def PlayMusicFrom(fr, name, volume, t):
            renpy.music.set_volume(volume, delay=0, channel="music")
            renpy.music.play("" + str(fr) +  "audio/music/" + str(name) + ".ogg", channel="music", loop=True, fadeout=None, synchro_start=False, fadein=t, tight=None, if_changed=True)

    def PlaySound(name, volume, t, l): 
            renpy.music.set_volume(volume, delay=0, channel="sound")
            renpy.music.play("audio/sound/" + str(name) + ".ogg", channel="sound", loop=l, fadeout=None, synchro_start=False, fadein=t, tight=None, if_changed=True)

    def PlaySound2(name, volume, t, l): 
            renpy.music.set_volume(volume, delay=0, channel="sound")
            renpy.music.play("audio/vocal/" + str(name) + ".ogg", channel="sound", loop=l, fadeout=None, synchro_start=False, fadein=t, tight=None, if_changed=True)

    def PlaySound3(name, volume, t, l): 
            renpy.music.set_volume(volume, delay=0, channel="sound")
            renpy.music.play("audio/sound/" + str(name) + ".ogg", channel="sound", loop=l, fadeout=None, synchro_start=False, fadein=t, tight=None, if_changed=True)

    def PlaySound4(name, volume, t, l): 
            renpy.music.set_volume(volume, delay=0, channel="sound")
            renpy.music.play("audio/sound/" + str(name) + ".ogg", channel="sound", loop=l, fadeout=None, synchro_start=False, fadein=t, tight=None, if_changed=True)

    def PlayAmbience(name, volume, t): 
            renpy.music.set_volume(volume, delay=0, channel="voice")
            renpy.music.play("audio/ambiences/" + str(name) + ".ogg", channel="ambience", loop=True, fadeout=None, synchro_start=False, fadein=t, tight=None, if_changed=True)






    def StopSound(fadeout=False):
            renpy.music.stop("sound", fadeout)

    def StopSound3(fadeout=False):
            renpy.music.stop("sound", fadeout)

    def StopSound4(fadeout=False):
            renpy.music.stop("sound", fadeout)


    def StopMusic(fadeout=False):
            renpy.music.stop("music", fadeout)


    def StopMusic2(fadeout=False):
            renpy.music.stop("music", fadeout)


    def StopAmbience(fadeout=False):
            renpy.music.stop("ambience", fadeout)


    def StopAudio(type = "sound",fadeout = False):
            renpy.music.stop(type, fadeout)

    #######################################################

    #ЭКРАНЫ
    def ShowScreens(window_show=True, _with=None):
        if window_show: store._window_show(_with)

    def HideScreens(window_hide=True, full=False, _with=None):
            if full:
                store._window_show(None)
                renpy.pause(0.1)
            if window_hide: store._window_hide(_with)

    
    def AttackScreens(hard=False):
        renpy.show_layer_at(getattr(store, "Fl_screen_attack" + ("_hard" if hard else "")), layer="screens") #экран встряски


    def AttackMaster(hard=False):
            renpy.show_layer_at(getattr(store, "Fl_screen_attack" + ("_hard" if hard else "")), layer="master") #экран зума


    def ShowScreen(at=None, reset=True):
        at = store.Fl_screen_normal(0) if not at else TransformsCheckList(at)
        renpy.show_layer_at(at, "screens", reset)


    def HideScreen(_with=None, fast=False, check=True, pause=True):
        if check: store.Fl_screens = False
        time = 0.25 if fast else 0.5
        renpy.show_layer_at(store.Fl_hidescreens(time), layer="screens")
        if pause: renpy.pause(time, hard=True)
        renpy.show_layer_at(store.Fl_screen_normal(0), layer="screens")
        store._window_hide(_with)



    def Master(at=None, reset=True, voice=None, sound=None, start_voice=False,  start_sound=False, end_voice=False, end_sound=False, _with=None):
        at = store.Fl_screen_normal(0) if not at else TransformsCheckList(at)
        renpy.show_layer_at(at, "master", reset)
        if voice:
            store.Fl.PlaySound2(voice, start=start_voice, end=end_voice)
        if sound:
            store.Fl.PlaySound(sound, start=start_sound, end=end_sound)
        if _with:
            renpy.game.interface.set_transition(_with)


    def NormalScreens(window_show=True, _with=None):
            """
            IN:
                window_show - True/False
                _with - expression
            TYPE:
                Show
            """
            renpy.show_layer_at(store.Fl_screen_normal(0), layer="screens")
            if window_show: store._window_show(_with)


        
    
    #######################################################



    def Pause(delay=None, music=None, with_none=None, hard=True, checkpoint=None):
        if not delay:
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse="pause", type="pause", roll_forward=None)
            return
        if delay <= 0:
            return
        renpy.pause(delay, music, with_none, hard, checkpoint)



    #АвтоСейв
    def AutoSave(auto=True, text=True, force=False):
        #if text:
            #store.save_name = name
        if (auto and store.persistent.Fl_autosaves and not store.Fl_after_load) or force:
            renpy.loadsave.cycle_saves("Fl_FilePage_auto-", 12)
            if not force:
                renpy.take_screenshot()
                renpy.hide_screen("Fl_autosave")
                renpy.show_screen("Fl_autosave")
            renpy.save("Fl_FilePage_auto-1", store.save_name)
            if not force:
                renpy.pause(0.1, hard=True)


    def PodskSave():
        renpy.take_screenshot()
        renpy.hide_screen("Fl_podsk_save")
        renpy.show_screen("Fl_podsk_save")


    def PodskDict():
        renpy.take_screenshot()
        renpy.hide_screen("Fl_podsk_dict")
        renpy.show_screen("Fl_podsk_dict")



    #Эффект моргания
    def ShowBlink():
            renpy.hide("Fl_unblink", layer="mapoverlay")
            renpy.show("Fl_blink", layer="mapoverlay")

    
    def ShowUnblink():
            renpy.hide("Fl_blink", layer="mapoverlay")
            renpy.show("Fl_unblink", layer="mapoverlay")

    
    def ShowBlinking():
            renpy.show("Fl_blinking", layer="mapoverlay")


    def HideBlink():
            renpy.hide("Fl_blink", layer="mapoverlay")


    def HideUnblink():
            renpy.hide("Fl_unblink", layer="mapoverlay")


    def HideBlinking():
            renpy.hide("Fl_blinking", layer="mapoverlay")
            



    #Статус персонажа
    def Status(value, sound=True, hard=False):
            if value == False:
                store.Fl_status_action = False
                return
            elif not store.Fl_status_action:
                store.Fl_status_action = True
            if "+" in value:
                value_int = value[1:]
                store.Fl_status_points[0] += int(value_int)
            elif "-" in value:
                value_int = value[1:]
                store.Fl_status_points[0] -= int(value_int)
            elif IsOnlyAlpha(value, "eng"):
                store.Fl_status_points[1] = value
            elif value != "":
                store.Fl_status_points[0] = int(value)
            if store.Fl_status_points[0] > 120:
                store.Fl_status_points[0] = 120
            elif store.Fl_status_points[0] < 0:
                store.Fl_status_points[0] = 0
            if value == "":
                store.Fl_status_points[0] = 0
                store.Fl_status_points[1] = ""
                store.Fl_status_name = ""
            elif store.Fl_status_points[0] == 0:
                store.Fl_status_name = "Состояние: Смерть"
                store.Fl_status_color = store.Fl_red_dark_color
            elif store.Fl_status_points[1] == "depression":
                store.Fl_status_name = "Состояние: Депрессия"
                store.Fl_status_color = store.Fl_gray_color
            elif store.Fl_status_points[1] == "panic":
                store.Fl_status_name = "Состояние: Паника"
                store.Fl_status_color = store.Fl_red_color
            elif store.Fl_status_points[1] == "anger":
                store.Fl_status_name = "Состояние: Злость"
                store.Fl_status_color = store.Fl_red_color
            elif store.Fl_status_points[1] == "rage":
                store.Fl_status_name = "Состояние: Ярость"
                store.Fl_status_color = store.Fl_red_color
            elif store.Fl_status_points[1] == "dream":
                store.Fl_status_name = "Состояние: Сонливость"
                store.Fl_status_color = store.Fl_blue_dark_color2
            elif store.Fl_status_points[0] == 5:
                store.Fl_status_name = "Состояние: Критическое"
                store.Fl_status_color = store.Fl_red_color
            elif store.Fl_status_points[0] <= 20:
                store.Fl_status_name = "Состояние: Апатия"
                store.Fl_status_color = store.Fl_brown_color
            elif store.Fl_status_points[0] <= 40:
                store.Fl_status_name = "Состояние: Стресс"
                store.Fl_status_color = store.Fl_orange_color
            elif store.Fl_status_points[0] <= 60:
                store.Fl_status_name = "Состояние: Напряжение"
                store.Fl_status_color = store.Fl_yellow_color
            elif store.Fl_status_points[0] <= 80:
                store.Fl_status_name = "Состояние: Нормальное"
                store.Fl_status_color = store.Fl_blue_dark_color2
            elif store.Fl_status_points[0] <= 100:
                store.Fl_status_name = "Состояние: Хорошее"
                store.Fl_status_color = store.Fl_green_light_color
            else:
                store.Fl_status_name = "Состояние: Эйфория"
                store.Fl_status_color = store.Fl_purple_color
            if store.persistent.Fl_status_sound and sound:
                renpy.sound.play("audio/sound/Fl_status" + ("2" if value == "" or store.Fl_status_points[0] == 0 or hard else "") + ".ogg", "sound")
            dict = {"":"", "Смерть":"death", "Критическое":"critical", "Апатия":"apathy", "Стресс":"stress", "Напряжение":"tension", "Нормальное":"normal", "Хорошее":"good", "Эйфория":"euphoria"}
            if store.Fl_status_points[1] != "normal":
                store.Fl_status = store.Fl_status_points[1]
            else:
                store.Fl_status = dict[store.Fl_status_name.replace("Состояние: ", "")]
           


    def IsOnlyAlpha(name, type):
        dict = {"rus":"eng", "eng":"rus"}
        symbols = bool(re.compile("[{}\"..]").findall(name))
        return IsPresentAlpha(name, type) and not IsPresentAlpha(name, dict[type]) and not symbols


    def IsPresentAlpha(name, type):
        letters = "[а-яА-Я]+" if type == "rus" else "[a-zA-Z]+"
        return bool(re.compile(letters).findall(name))

    def Brightness(img, b):
        return store.im.MatrixColor(img, store.im.matrix.brightness(b))



    

    #Инвентарь
    def InventoryIf(name, stats=None):
        for item in range(0, len(store.Fl_inventory)):
            if store.Fl_inventory[item]["name"] == name and stats == store.Fl_inventory[item]["stats"]:
                return True
        return False


    def SelectedSlot(name):
        dict = {"BPK":store.Fl_backpack, "WPG":store.Fl_weapon}
        name = {"slot":name, "name":dict[name]["name"], "stats":dict[name]["stats"]} if name in dict else store.Fl_inventory[name]
        return name

    def Item(id, stats=None, type="add", message="Получен предмет:"):
            if id not in store.Fl_backpacks_list:
                for slot in range(0, len(store.Fl_inventory)):
                    if store.Fl_inventory[slot] == {"slot":slot, "name":"empty" if type == "add" else id, "stats":None if type == "add" else stats}:
                        store.Fl_inventory[slot] = {"slot":slot, "name":id if type == "add" else "empty", "stats":stats if type == "add" else None}
                        break
            elif type == "add":
                dict = {"easy":[4, 8, "1/5"], "average":[8, 14, "2/5"], "big":[14, 20, "3/5"], "very_big":[20, 26, "4/5"], "enormous":[26, 32, "5/5"]}
                store.Fl_backpack = {"slot":"BPK", "name":id, "stats":{"q":dict[id][2], "c":dict[id][1]-4}}
                if message:
                    store.Fl.PlaySound("Fl_curtains")
                store.Fl.InventorySlots("empty", dict[id][0], dict[id][1])
                if id == "easy":
                    store.Fl.Item(store.Fl_inventory[0]["name"], message=None)
                    store.Fl.Item(store.Fl_inventory[1]["name"], message=None)
                    store.Fl.Item(store.Fl_inventory[2]["name"], message=None)
                    store.Fl.Item(store.Fl_inventory[3]["name"], store.Fl_inventory[3]["stats"], message=None)
                    store.Fl.InventorySlots("empty", 0, 4)
            elif id == "easy":
                store.Fl_backpack = {"slot":"BPK", "name":"empty", "stats":None}
                store.Fl.PlaySound("Fl_curtains")
                store.Fl.InventorySlots("lock", 4, 8)
            if message:
                renpy.music.play("gui/main_menu/Fl_" + ("new_item" if type == "add" else "lock") + ".ogg", "sound")
                renpy.hide_screen("Fl_new_item")
                renpy.show_screen("Fl_new_item", id, message)


    def InventorySlots(name, is_from, is_to):
        for slot in range(is_from, is_to):
            store.Fl_inventory[slot] = {"slot":slot, "name":name, "stats":None}



    def ItemDescription(name):
        dict = {"phone": "",
                "matches":"",
                "flashlight":"",
                "knife":"",
                "easy":"",
                "key13":"",
                "brush":"",
                "dentifrice":"",
                "keydoor":"",
                "keypr":"",
                "bottle":""}
        return dict[name]


    def ItemEmpty(number, item):
            name = getattr(store, "Fl_items_reserve" + str(number))
            name[item] = {"slot":name[item]["slot"], "name":"empty"}


    def InventorySlotsLen():
        count = 0
        for item in store.Fl_inventory:
            if item["name"] != "lock":
                count += 1
        return count


    def Inventory(item, type="apply"):
            store.Fl.NormalScreens(False)
            store.Fl_hover_slot = {"slot":None, "name":"empty", "stats":None}
            renpy.call_screen("Fl_inventory", type, item)


    def ItemsMenu(number, name="", check=True, stats=None):
            store.Fl.NormalScreens(False)
            store.Fl_show_items_window = True
            items = getattr(store, "Fl_items_reserve" + str(number))
            renpy.call_screen("Fl_items", number, name, items, check, stats)


    def ItemsList(*args):
            store.Fl_items_seen = {}
            for key in range(1, 17):
                store.Fl_items_seen.setdefault(str(key), False)
            for num in range(0, len(args)+1):
                setattr(store, "Fl_items_reserve" + str(num+1), [])
                for n in range(0, 9):
                    getattr(store, "Fl_items_reserve" + str(num+1)).append({"slot":n, "name":"empty"})
            for item in range(0, len(args)):
                getattr(store, "Fl_items_reserve" + str(item+1))[args[item][0]] = {"slot":args[item][0], "name":args[item][1], "stats":args[item][2] if len(args[item]) == 3 else None}

    def GlobalDict(name, key, value):
        getattr(store, name)[key] = value


    def Message(name):
            dict = {
                "inventory":[
                    "Теперь вам доступен инвентарь!",
                    "Инвентарь вы сможете пополнять по ходу игры различными вещами, которые могут понадобиться вам по сюжету.", ""],
                "backpack":[
                    "Вы получили рюкзак!",
                    "Рюкзак позволяют вам носить гораздо больше вещей с собой, открывая большее количество ячеек в инвентаре.", ""],
                "status":[
                    "{size=-4}Теперь вам доступно влияние на состояние!{/size}",
                    "Все поступки и реплики героя зависят исключительно от его состояния. Само же состояние в основном меняется в зависимости от происходящих вокруг ситуаций, но и также от принятых вами выборов."]}
            store.Fl.NormalScreens(False)
            store.Fl.PlaySound("Fl_lock")
            renpy.call_screen("Fl_message", name, dict[name][0], dict[name][1])