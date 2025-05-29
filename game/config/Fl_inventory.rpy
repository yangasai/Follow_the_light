# -*- coding: ひきこもり -*-
screen Fl_items(number, name, items, check, stats):
    tag menu
    zorder 100
    modal True
    if check != True:
        $ check = Fl.InventoryIf(check, stats)
    fixed at Fl_menu_move:
        frame background "gui/inventory/background2.png"
        imagebutton offset (1423, 184):
            if check:
                hover_sound "gui/main_menu/Fl_click_menu.mp3"
                auto "gui/inventory/exit2_%s.png"
                action [Fl_QuitItemsMenu(), Return()]
            else:
                idle Fl.Brightness("gui/inventory/exit2_idle.png", -0.2)
        text name style "Fl_text_item_label" offset (793, 172)

        vbox pos (0.309, 0.242) spacing 6:
            use Fl_items_slots(number, items, stats)
        vbox pos (0.526, 0.242) spacing 6:
            use Fl_inventory_slots



screen Fl_inventory_message:
    text Fl_inventory_message style "Fl_text_label" size 40 at Fl_message_move
    timer 3.4 action [SetVariable("Fl_inventory_message", ""), Hide("Fl_inventory_message")]


screen Fl_items_slots(number, items, stats):
    grid 4 2 spacing 7:
        for slot in range(0, 8):
            imagebutton:
                idle "gui/inventory/slots/" + items[slot]["name"] + "_idle.png"
                if items[slot]["name"] != "empty":
                    hover_sound "gui/main_menu/Fl_click_menu.mp3"
                    hover Fl.Brightness("gui/inventory/slots/" + items[slot]["name"] + "_hover.png", 0.1)
                    action Fl_ShowItem(number, items, stats, slot)

screen Fl_inventory_slots:
    grid 4 Fl.InventorySlotsLen()/4 spacing 7:
        for slot in range(0, Fl.InventorySlotsLen()):
            imagebutton:
                idle "gui/inventory/slots/" + Fl_inventory[slot]["name"] + "_idle.png"
                if Fl_inventory[slot]["name"] not in ["empty", "lock"] and not Fl_show_items_window:
                    hover_sound "gui/main_menu/Fl_click_menu.mp3"
                    hover "gui/inventory/slots/" + Fl_inventory[slot]["name"] + "_hover.png"
                    insensitive Fl.Brightness("gui/inventory/slots/" + Fl_inventory[slot]["name"] + "_idle.png", 0.5)
                    action Fl_SelectedSlot(slot)

