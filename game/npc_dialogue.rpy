# ============================================================
# СИСТЕМА ДИАЛОГОВ С NPC
# ============================================================

default npc_question = ""
default npc_answer = ""
default current_npc = ""

# ------------------------------------------------------------
# Данные NPC
# ------------------------------------------------------------

define npc_village_head = {
    "name": "Староста Ривена",
    "personality": "Пожилой, мудрый и осторожный староста. Говорит спокойно и уважительно. Хорошо знает деревню и ближайшие окрестности.",
    "knowledge": "Знает жителей Ривена, лес вокруг деревни, местные дороги, волков, гоблинов и старые слухи о чудовищах."
}

define npc_merchant = {
    "name": "Торговец",
    "personality": "Хитрый, разговорчивый и немного жадный торговец. Любит шутить и торговаться.",
    "knowledge": "Знает торговые маршруты, цены, слухи, путешественников и большую часть событий, происходящих в деревне."
}

define npc_blacksmith = {
    "name": "Кузнец",
    "personality": "Молчаливый, суровый и прямолинейный кузнец. Не любит пустых разговоров.",
    "knowledge": "Хорошо разбирается в оружии, броне, металлах и знает многих жителей деревни."
}


# ------------------------------------------------------------
# Начало разговора
# ------------------------------------------------------------

label talk_to_npc(npc):

    $ current_npc = npc

    $ npc_question = ""
    $ npc_answer = ""

    scene black
    with dissolve

    show screen npc_dialogue_screen

    $ renpy.pause()

    hide screen npc_dialogue_screen

    return


# ------------------------------------------------------------
# Ответ NPC
# ------------------------------------------------------------

label npc_answer_local:

    if npc_question.strip() == "":
        $ npc_answer = "Старик смотрит на тебя с недоумением. Похоже, ты ничего не спросил."

    elif current_npc == "village_head":

        if "гоблин" in npc_question.lower():
            $ npc_answer = "Гоблины стали появляться в лесу всё чаще. Раньше они почти никогда не подходили к деревне."

        elif "лес" in npc_question.lower():
            $ npc_answer = "Тёмный лес начинается сразу за северной дорогой. Советую не заходить туда без оружия."

        elif "деревн" in npc_question.lower():
            $ npc_answer = "Ривен существует уже несколько поколений. Здесь живут простые люди, которые хотят лишь спокойно растить детей и работать."

        elif "волк" in npc_question.lower():
            $ npc_answer = "Последние недели волки стали вести себя необычно. Они подходят слишком близко к домам."

        else:
            $ npc_answer = "Староста задумчиво хмурится. «Интересный вопрос... Но боюсь, я не знаю на него ответа»."

    elif current_npc == "merchant":

        if "товар" in npc_question.lower() or "куп" in npc_question.lower():
            $ npc_answer = "Ха! Конечно, у меня есть товары. Но сначала покажи золото."

        elif "лес" in npc_question.lower():
            $ npc_answer = "В лес сейчас лучше не ходить. Я видел нескольких охотников, которые вернулись оттуда далеко не в лучшем состоянии."

        elif "гоблин" in npc_question.lower():
            $ npc_answer = "Гоблины? Я бы держался от них подальше. Но если хочешь заработать, иногда их шкуры неплохо покупают."

        else:
            $ npc_answer = "Торговец пожимает плечами. «Возможно. А теперь, может, что-нибудь купишь?»"

    elif current_npc == "blacksmith":

        if "меч" in npc_question.lower() or "оруж" in npc_question.lower():
            $ npc_answer = "Оружие должно быть крепким. Хороший меч может спасти тебе жизнь там, где разговоры уже не помогут."

        elif "брон" in npc_question.lower():
            $ npc_answer = "Нормальная броня стоит денег. Но если собираешься идти в лес, лучше потрать золото на защиту."

        elif "гоблин" in npc_question.lower():
            $ npc_answer = "Гоблины мелкие, но их много. Не позволяй им окружить себя."

        else:
            $ npc_answer = "Кузнец продолжает работать и коротко отвечает: «Не знаю»."


    return


# ------------------------------------------------------------
# ЭКРАН ДИАЛОГА
# ------------------------------------------------------------

screen npc_dialogue_screen():

    modal True

    add Solid("#111111")

    frame:
        xalign 0.5
        yalign 0.5

        xsize 1000
        ysize 650

        padding (40, 40)

        vbox:

            spacing 25

            text "Разговор" size 45 xalign 0.5

            null height 10

            if current_npc == "village_head":
                text "Староста Ривена" size 32

            elif current_npc == "merchant":
                text "Торговец" size 32

            elif current_npc == "blacksmith":
                text "Кузнец" size 32

            null height 10

            if npc_answer != "":
                frame:
                    xfill True
                    ysize 180

                    text npc_answer size 28

            else:
                frame:
                    xfill True
                    ysize 180

                    text "Персонаж ждёт твоего вопроса..." size 28

            null height 10

            input:

                value VariableInputValue("npc_question")

                length 300

                xfill True

                size 28

                allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789 .,!?-"

            null height 10

            hbox:

                spacing 30

                xalign 0.5

                textbutton "Спросить":
                    action [
                        Hide("npc_dialogue_screen"),
                        Jump("npc_answer_local")
                    ]

                textbutton "Закончить разговор":
                    action Return()
