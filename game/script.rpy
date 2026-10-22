define e = Character("Элиан")

default level = 1
default xp = 0
default gold = 25
default weapon_bonus = 0
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

    call screen riven_village

    scene black
    with dissolve

    "Ты находишься в деревне Ривен."

    if wolf_quest_done:
        "Староста благодарит тебя за помощь."
        "Староста" "Ты доказал, что достоин доверия. Береги себя."
    else:
        "Староста" "Путник, в лесу появились волки. Нам нужна твоя помощь."

        menu:
            "Принять задание и отправиться в лес":
                jump forest

            "Пока остаться в деревне":
                jump world_map

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
                $ damage = renpy.random.randint(12, 20) + (level - 1) * 3 + weapon_bonus
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

# ==========================================
# ЖИТЕЛИ ДЕРЕВНИ РИВЕН
# ==========================================

label village_elder:

    "Староста" "Рад видеть тебя, странник!"
    
    if wolf_quest_done:
        "Староста" "Спасибо за помощь с волками. Ты настоящий герой!"
    else:
        "Староста" "В лесу развелись волки. Помоги нам избавиться от них."

        menu:
            "Принять задание":
                "Староста" "Отлично! Возвращайся после победы над волком."
                jump forest

            "Отказаться":
                "Староста" "Что ж, буду ждать, когда ты будешь готов."

    return


label village_merchant:

    "Торговец" "Добро пожаловать! У меня есть зелья здоровья."

    menu:
        "Купить зелье здоровья — 15 золота" if gold >= 15:
            $ gold -= 15
            $ potions += 1
            "Ты купил зелье. Зелий теперь: [potions]."
        "Посмотреть товары":
            "Торговец" "Пока у меня есть только зелья здоровья."
        "Уйти":
            "Торговец" "Заглядывай ещё!"

    return


label village_blacksmith:

    "Кузнец" "Моё оружие поможет тебе в путешествии."

    menu:
        "Улучшить оружие — 30 золота" if gold >= 30:
            $ gold -= 30
            $ renpy.store.weapon_bonus = getattr(renpy.store, "weapon_bonus", 0) + 3
            "Кузнец" "Готово! Твои атаки теперь сильнее."
        "Уйти":
            "Кузнец" "Возвращайся, когда накопишь золото."

    return
