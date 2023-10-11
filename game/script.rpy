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
    '''
    ТЕСТОВОЕ СООБЩЕНИЕ
    '''

    return
