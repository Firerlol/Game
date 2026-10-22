from pathlib import Path

content = '''# Интерфейс «Эльдории»
# Основа HUD для открытого мира и карточек персонажей для диалогов.
# Файл не требует внешних изображений и совместим с Ren'Py.

style eldoria_panel:
    background Solid("#111827dd")
    padding (18, 12)

style eldoria_label:
    color "#f4e7c2"
    size 22
    outlines [(2, "#17120d", 0, 0)]

screen eldoria_hud():
    zorder 100

    frame:
        style "eldoria_panel"
        xalign 0.02
        yalign 0.02

        vbox:
            spacing 4
            text "ЭЛЬДОРИЯ" style "eldoria_label" size 18
            text "Уровень [level]  •  Опыт [xp]/[level * 50]" style "eldoria_label" size 16
            text "Здоровье [hp]/[max_hp]" style "eldoria_label" size 16
            text "Золото [gold]  •  Зелья [potions]" style "eldoria_label" size 16

# Вспомогательная карточка для визуально-новелльных диалогов.
# Позже рядом можно разместить полноценный аниме-спрайт персонажа.
screen eldoria_character_card(character_name, mood="neutral"):
    zorder 90
    frame:
        style "eldoria_panel"
        xalign 0.03
        yalign 0.98
        xmaximum 420

        vbox:
            spacing 5
            text character_name color "#f7dca2" size 26
            if mood == "angry":
                text "Выражение: гнев" color "#f5b5a9" size 16
            elif mood == "happy":
                text "Выражение: радость" color "#b9f0c3" size 16
            else:
                text "Выражение: спокойствие" color "#d7e2f0" size 16

# Направление художественного оформления:
# - открытый мир: пиксельная 2D-графика;
# - диалоги: аниме-портреты персонажей;
# - деревня: тёплая палитра и уютные детали;
# - лес: тёмная, холодная палитра и туман;
# - руины/подземелья: каменные оттенки, контрастный свет;
# - редкие безопасные места могут быть яркими и красочными,
#   а опасные зоны — более мрачными и реалистичными.
'''
path = Path("/mnt/data/eldoria_ui.rpy")
path.write_text(content, encoding="utf-8")
print(f"Создан файл: {path}")
