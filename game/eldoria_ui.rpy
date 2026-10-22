# ==========================================
# ЭЛЬДОРИЯ — ИГРОВОЙ ИНТЕРФЕЙС
# ==========================================

init python:
    if "eldoria_hud" not in config.overlay_screens:
        config.overlay_screens.append("eldoria_hud")


# Цвета интерфейса

define eldoria_gold = "#f4d58d"
define eldoria_text = "#f5f0df"
define eldoria_dark = "#18202b"


# Панель характеристик

style eldoria_panel:
    background Solid("#18202be8")
    padding (16, 12)

style eldoria_text_style:
    color "#f5f0df"
    size 18
    outlines [(1, "#000000", 1, 1)]


screen eldoria_hud():

    zorder 100

    # Не показывать HUD в главном меню
    if renpy.get_screen("main_menu") is None:

        frame:
            style "eldoria_panel"
            xalign 0.02
            yalign 0.02
            xmaximum 360

            vbox:
                spacing 5

                text "⚔ ЭЛЬДОРИЯ" color eldoria_gold size 22

                text "Уровень: [level]" style "eldoria_text_style"

                text "Опыт: [xp]/[level * 50]" style "eldoria_text_style"

                text "Здоровье: [hp]/[max_hp]" style "eldoria_text_style"

                bar:
                    value hp
                    range max_hp
                    xmaximum 300
                    ymaximum 12

                text "Золото: [gold]" style "eldoria_text_style"

                text "Зелья: [potions]" style "eldoria_text_style"


# ==========================================
# КАРТОЧКА ПЕРСОНАЖА ДЛЯ ДИАЛОГОВ
# ==========================================

screen eldoria_character_card(character_name, description=""):

    zorder 90

    frame:
        background Solid("#18202bf0")
        padding (20, 14)
        xalign 0.03
        yalign 0.98
        xmaximum 500

        vbox:
            spacing 6

            text "[character_name]" color eldoria_gold size 28

            if description:
                text "[description]" color eldoria_text size 18
