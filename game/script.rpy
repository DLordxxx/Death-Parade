# Определение персонажей игры.

# Задаётся изначальная позиция персонажей
init:
    $ left = Position(xalign=0.2)
    $ right = Position(xalign=0.75)
init-1:
    $ menu_timer_onoff=False

# Игра начинается здесь:
label start:

# Первая сцена в аудитории
    scene bg test
    with fade
    '''
    ТЕСТОВОЕ СООБЩЕНИЕ
    '''

    return
