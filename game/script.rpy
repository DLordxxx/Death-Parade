# Определение персонажей игры

# define gg = Character('???', color="#5a11ad")
# define ch = Character('Чревоугодие', color="#1ab85e")
# define len = Character('Лень', color="#c4149b")
# define jad = Character('Жадность', color="#f7b707")
# define pox = Character('Похоть', color="#144fd9")
# define gnev = Character('Гнев', color="#1cc7b6")
# define gor = Character('Гордыня', color="#bf0d0d")
# define zav = Character('Зависть', color="#25a8cc")

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

    jump start

label final2:
    "Поздравляю, вы открыли вторую концовку!"

    return

label no_choice:
    "Неудача"

    return
