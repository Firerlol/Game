
define e = Character("Элиан")

default level = 1
default xp = 0
default gold = 25
default hp = 100

label start:
    scene black
    with fade

    "Королевство Эльдория. Год 742."
    "Чудовища вновь угрожают человеческим землям."
    "Ты — молодой странник, которому предстоит стать героем."

    menu:
        "Куда отправиться?"
        "В деревню Ривен":
            jump village
        "В тёмный лес":
            jump forest

label village:
    "Ты прибыл в деревню Ривен."
    "Староста просит прогнать волков."

    menu:
        "Принять задание":
            $ xp += 30
            $ gold += 20
            "Задание выполнено! +30 опыта, +20 золота."
            jump level_check
        "Пойти в лес":
            jump forest

label forest:
    "Из тёмных кустов появляется гоблин!"

    menu:
        "Сразиться":
            $ xp += 40
            $ gold += 15
            $ hp -= 15
            "Гоблин побеждён! +40 опыта, +15 золота."
            jump level_check
        "Отступить":
            jump village

label level_check:
    if xp >= 50 and level == 1:
        $ level = 2
        $ hp = 120
        "Новый уровень! Максимальное здоровье увеличено."

    "Уровень: [level]"
    "Опыт: [xp]"
    "Золото: [gold]"
    "Здоровье: [hp]"

    menu:
        "Продолжить":
            jump village
        "Закончить игру":
            return
