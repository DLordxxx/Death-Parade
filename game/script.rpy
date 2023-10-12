# Определение персонажей игры.

# Задаётся изначальная позиция персонажей
init:
    $ left = Position(xalign=0.2)
    $ right = Position(xalign=0.75)
init-1:
    $ menu_timer_onoff=False

# Заставка
label splashscreen:
    screen black
    scene zastavka with fade
    pause(2)
    scene black with fade
    return

# Игра начинается здесь:
label start:

# Первая сцена
    stop music fadeout 1
    scene bg test
    with fade

# Объявляется таймер
    $ timez = 100
    $ time_range = 100
    $ marker = "no_choice"
    $ menu_timer_onoff=True

    menu:
        "Выбор?"

        "1":
            "Вы выбрали первый вариант"

            jump final1
        "2":
            "Вы выбрали второй вариант"

            jump final2

label final1:
    "Поздравляю, вы открыли первую концовку!"

    return

label final2:
    "Поздравляю, вы открыли вторую концовку!"

    return

label no_choice:
    "Неудача"

    return
