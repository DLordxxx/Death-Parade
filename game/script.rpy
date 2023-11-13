# Определение персонажей игры

define gg = Character('???', color="#5a11ad") #фиол
define ch = Character('Чревоугодие', color="#FF6600") #оранж
define le = Character('Лень', color="#00bfff") #голуб
define jad = Character('Жадность', color="#ccff00") #шартрез
define pox = Character('Похоть', color="#c4149b") #роза
define gn = Character('Гнев', color="#bf0d0d") #крас
define gor = Character('Гордыня', color="#FEb7F0") #цвет испуганой нимфы+b
define zav = Character('Зависть', color="#5353ec") #лазурь

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
        ch "Выбор?"

        "1":
            "Вы выбрали первый вариант"

            jump final1
        "2":
            "Вы выбрали второй вариант"

            jump final2

label final1:
    gg "Поздравляю, вы открыли первую концовку!"

    jump start

label final2:
    gg "Поздравляю, вы открыли вторую концовку!"

    return

label no_choice:
    "Неудача"

    return
