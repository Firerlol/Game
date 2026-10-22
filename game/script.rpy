define e = Character("Элиан")

default level = 1
default xp = 0
default gold = 25
default hp = 100
default max_hp = 100
default potions = 2
default wolf_quest_done = False
default forest_visits = 0

default enemy_name = "Гоблин"
default enemy_hp = 30
default enemy_attack = 8
default enemy_xp = 20
default enemy_gold = 10

label start:
    scene black
    with fade

    "Королевство Эльдория. Год 742."
    "Чудовища вновь угрожают человеческим землям."
    "Ты — молодой странник, которому предстоит стать героем."
    e "Пора выяснить, что скрывается за границами королевства."

    jump world_map

label world_map:
    scene black
    with dissolve

    "Куда отправиться?"
    "Уровень: [level]  |  Здоровье: [hp]/[max_hp]  |  Золото: [gold]"

    menu:
        "Деревня Ривен":
            jump village
        "Тёмный лес":
            jump forest
        "Заброшенные руины" if level >= 2:
            jump ruins
        "Выпить зелье здоровья" if potions > 0 and hp < max_hp:
            $ hp = min(max_hp, hp + 40)
            $ potions -= 1
            "Ты выпил зелье и восстановил здоровье. Осталось зелий: [potions]."
            jump world_map
        "Отдохнуть в деревне" if hp < max_hp:
            $ hp = max_hp
            "Ты отдохнул в безопасном месте и полностью восстановил здоровье."
            jump world_map
        "Посмотреть характеристики":
            jump status_screen

label village:
    scene black
    with dissolve

    "Ты прибыл в деревню Ривен."
    "За деревянным частоколом жители пытаются вести обычную жизнь, несмотря на угрозу чудовищ."

    menu:
        "Поговорить со старостой" if not wolf_quest_done:
            "Староста: «В лесу завелись волки. Помоги нам, и я награжу тебя»."
            menu:
                "Принять задание":
                    jump forest
                "Пока отказаться":
                    jump village
        "Получить награду за помощь" if wolf_quest_done:
            "Староста благодарит тебя. Это задание уже выполнено."
            jump village
        "Отправиться на площадь":
            "Торговец предлагает зелье здоровья за 15 золотых."
            menu:
                "Купить зелье здоровья (15 золота)" if gold >= 15:
                    $ gold -= 15
                    $ potions += 1
                    "Ты купил зелье. Всего зелий: [potions]."
                    jump village
                "Уйти от торговца":
                    jump village
        "Отдохнуть и восстановить здоровье":
            $ hp = max_hp
            "Ты провёл время в деревне и полностью восстановил здоровье."
            jump village
        "Вернуться к карте":
            jump world_map

label forest:
    scene black
    with dissolve

    $ forest_visits += 1
    "Ты входишь в тёмный лес. Между деревьями слышится рычание."

    if renpy.random.randint(1, 100) <= 65:
        $ enemy_name = "Волк"
        $ enemy_hp = 28 + (level - 1) * 5
        $ enemy_attack = 7 + (level - 1) * 2
        $ enemy_xp = 25
        $ enemy_gold = renpy.random.randint(5, 12)
    else:
        $ enemy_name = "Гоблин"
        $ enemy_hp = 35 + (level - 1) * 6
        $ enemy_attack = 9 + (level - 1) * 2
        $ enemy_xp = 30
        $ enemy_gold = renpy.random.randint(8, 16)

    "На тропе появляется: [enemy_name]!"
    jump combat

label ruins:
    scene black
    with dissolve

    "Ты входишь в заброшенные руины. На камнях видны древние руны."
    "Из тени поднимается скелет-страж!"

    $ enemy_name = "Скелет-страж"
    $ enemy_hp = 55 + (level - 2) * 8
    $ enemy_attack = 12 + (level - 2) * 2
    $ enemy_xp = 45
    $ enemy_gold = renpy.random.randint(15, 25)

    jump combat

label combat:
    while enemy_hp > 0 and hp > 0:
        "Противник: [enemy_name] — здоровье [enemy_hp]."
        "Твоё здоровье: [hp]/[max_hp]."

        menu:
            "Атаковать":
                $ damage = renpy.random.randint(12, 20) + (level - 1) * 3
                $ enemy_hp = max(0, enemy_hp - damage)
                "Ты наносишь [damage] урона!"

                if enemy_hp > 0:
                    $ damage_taken = renpy.random.randint(max(1, enemy_attack - 3), enemy_attack + 3)
                    $ hp = max(0, hp - damage_taken)
                    "[enemy_name] атакует и наносит тебе [damage_taken] урона."

            "Выпить зелье здоровья ([potions])" if potions > 0 and hp < max_hp:
                $ hp = min(max_hp, hp + 40)
                $ potions -= 1
                "Ты восстановил здоровье. Теперь: [hp]/[max_hp]."
                $ damage_taken = renpy.random.randint(max(1, enemy_attack - 3), enemy_attack + 3)
                $ hp = max(0, hp - damage_taken)
                "[enemy_name] пользуется моментом и наносит [damage_taken] урона."

            "Попытаться убежать":
                if renpy.random.randint(1, 100) <= 60:
                    "Тебе удалось скрыться!"
                    jump world_map
                else:
                    "Противник преграждает путь!"
                    $ damage_taken = renpy.random.randint(max(1, enemy_attack - 3), enemy_attack + 3)
                    $ hp = max(0, hp - damage_taken)
                    "[enemy_name] наносит тебе [damage_taken] урона."

    if hp <= 0:
        jump defeat

    "Победа! Ты одолел противника: [enemy_name]."
    $ xp += enemy_xp
    $ gold += enemy_gold
    "Получено: [enemy_xp] опыта и [enemy_gold] золота."

    if enemy_name == "Волк" and not wolf_quest_done:
        $ wolf_quest_done = True
        $ xp += 20
        $ gold += 15
        "Ты выполнил просьбу старосты! Дополнительно: +20 опыта и +15 золота."

    jump level_check

label level_check:
    while xp >= level * 50:
        $ xp -= level * 50
        $ level += 1
        $ max_hp += 20
        $ hp = max_hp
        "Новый уровень: [level]! Максимальное здоровье увеличено до [max_hp]. Здоровье полностью восстановлено."

    jump status_screen

label status_screen:
    scene black
    with dissolve

    "—— Характеристики Элиана ——"
    "Уровень: [level]"
    "Опыт: [xp]/[level * 50]"
    "Здоровье: [hp]/[max_hp]"
    "Золото: [gold]"
    "Зелья здоровья: [potions]"

    menu:
        "Продолжить приключение":
            jump world_map
        "Закончить игру":
            return

label defeat:
    scene black
    with fade

    "Ты пал в бою, но твоё приключение ещё может продолжиться."
    "В деревне тебя нашли и выходили. Ты потерял 10 золотых."

    $ gold = max(0, gold - 10)
    $ hp = max_hp

    "Ты снова в строю. Здоровье восстановлено, золото: [gold]."
    jump village
