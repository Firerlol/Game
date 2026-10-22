# ==========================================
# ЭЛЬДОРИЯ — ДЕРЕВНЯ РИВЕН
# ==========================================

default hero_x = 0.50
default hero_y = 0.72
default village_message = "Деревня Ривен"

init python:

    def move_hero_to_mouse():
        x, y = renpy.get_mouse_pos()

        x = max(0.06, min(0.94, x / config.screen_width))
        y = max(0.25, min(0.92, y / config.screen_height))

        renpy.store.hero_x = x
        renpy.store.hero_y = y

        if abs(x - 0.50) < 0.12 and abs(y - 0.42) < 0.12:
            renpy.store.village_message = "Главная площадь Ривена"
        elif abs(x - 0.20) < 0.12 and abs(y - 0.55) < 0.12:
            renpy.store.village_message = "Жилые дома"
        elif abs(x - 0.80) < 0.12 and abs(y - 0.55) < 0.12:
            renpy.store.village_message = "Дорога к лесу"
        else:
            renpy.store.village_message = "Деревня Ривен"


screen pixel_house(x, y, house_color="#9b6242"):

    fixed:
        xpos x
        ypos y
        xsize 150
        ysize 125

        add Solid(house_color) xpos 20 ypos 38 xsize 110 ysize 78
        add Solid("#59352e") xpos 5 ypos 20 xsize 140 ysize 25
        add Solid("#704034") xpos 15 ypos 10 xsize 120 ysize 15
        add Solid("#422a25") xpos 62 ypos 75 xsize 28 ysize 41
        add Solid("#9dd7dc") xpos 32 ypos 52 xsize 22 ysize 20
        add Solid("#422a25") xpos 41 ypos 52 xsize 4 ysize 20
        add Solid("#422a25") xpos 32 ypos 60 xsize 22 ysize 4


screen riven_village():

    modal True
    zorder 50

    # Трава
    add Solid("#477b45")

    # Дороги
    add Solid("#b99b68") xpos 0 ypos 0.38 xsize 1.0 ysize 0.17
    add Solid("#b99b68") xpos 0.43 ypos 0.25 xsize 0.14 ysize 0.55

    # Деревья
    for tree_x, tree_y in [
        (0.05, 0.12),
        (0.25, 0.20),
        (0.70, 0.12),
        (0.91, 0.22),
        (0.08, 0.72),
        (0.88, 0.78),
    ]:

        fixed:
            xpos tree_x
            ypos tree_y
            xsize 70
            ysize 90

            add Solid("#65452d") xpos 27 ypos 42 xsize 16 ysize 38
            add Solid("#285b35") xpos 8 ypos 15 xsize 54 ysize 42
            add Solid("#347443") xpos 17 ypos 0 xsize 36 ysize 35
            add Solid("#42894b") xpos 23 ypos 7 xsize 18 ysize 17

    # Дома
    use pixel_house(0.06, 0.25, "#ad7650")
    use pixel_house(0.68, 0.25, "#92704e")
    use pixel_house(0.12, 0.62, "#9c5945")
    use pixel_house(0.69, 0.64, "#b18454")

    # Название локации
    frame:
        xpos 0.02
        ypos 0.02
        background Solid("#18202be8")
        padding (12, 8)

        text "РИВЕН" color "#f4d58d" size 26

    # Текущее место
    frame:
        xalign 0.5
        ypos 0.02
        background Solid("#18202be8")
        padding (10, 7)

        text "[village_message]" color "#ffffff" size 18

    # Обработка нажатия
    button:
        xpos 0
        ypos 0.15
        xsize 1.0
        ysize 0.85
        background None
        action Function(move_hero_to_mouse)

    # Герой
    fixed:
        xpos hero_x
        ypos hero_y
        xanchor 0.5
        yanchor 0.5
        xsize 44
        ysize 64

        add Solid("#263a2a") xpos 5 ypos 51 xsize 34 ysize 8
        add Solid("#35364a") xpos 9 ypos 38 xsize 10 ysize 18
        add Solid("#35364a") xpos 25 ypos 38 xsize 10 ysize 18
        add Solid("#3f6594") xpos 7 ypos 22 xsize 30 ysize 22
        add Solid("#e4b58c") xpos 12 ypos 5 xsize 20 ysize 19
        add Solid("#49352e") xpos 10 ypos 2 xsize 24 ysize 8
        add Solid("#d0a45b") xpos 7 ypos 35 xsize 30 ysize 4

    # Выход
    textbutton "Выйти":
        xalign 0.97
        yalign 0.96
        text_size 22
        action Return()


label test_village_map:

    call screen riven_village

    "Ты покинул деревню Ривен."

    return
