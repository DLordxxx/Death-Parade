# Определение персонажей игры

define gg = Character('???', color="#5a11ad") #фиол
define ch = Character('Чревоугодие', color="#FF6600") #оранж
define le = Character('Лень', color="#00bfff") #голуб
define jad = Character('Жадность', color="#ccff00") #шартрез
define pox = Character('Похоть', color="#c4149b") #роза
define gn = Character('Гнев', color="#bf0d0d") #крас
define gor = Character('Гордыня', color="#FEb7F0") #цвет испуганой нимфы+b
define zav = Character('Зависть', color="#5353ec") #лазурь
define dvor = Character('Дворецкий', color="#5353ec") #лазурь

# Музыка и звуки
define audio.glazaout = "music/glazaout.ogg"
define audio.sbil = "sound/sbil.ogg"
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
    pause(0.5)
    scene zastavka2 with fade
    pause(2)
    scene black with fade
    return

# Игра начинается здесь:
label start:

# Первая сцена
    stop music fadeout 1
    scene bg lift
    with fade

    dvor '''
    Приветствую вас в нашем отеле «Peccatum Mortale»!

    Мы рады каждому гостю, ведь именно он подарит незабываемые эмоции, которые вы запомните навсегда!

    Какой этаж желаете?
    '''
#здесь нужен силует гг

    gg '''
    Что простите?

    Куда я попал?
    '''
#пропадает гг - говорит двор

    dvor '''
    Ох, так вы один из новых постояльцев?

    Позвольте мне немного вас просветить. Этот отель по своей сути необычный – люди, прибывшие сюда могут очиститься как физически, так и духовно
    '''
#(гудок от фуры) (флешка)
    play music glazaout
    scene black with off
    pause 1.0
    scene bg q with onn
    stop music fadeout 3

    '''
    Всплывают резкие воспоминания…

    Яркий свет фар и громкий шум от гудка надвигающейся фуры, которую уже ничто не остановит.
    '''
    play sound sbil
    '''
    Удар.

    Слышно лишь тёплую кровь, капающую на белоснежную дорогу.
    '''
#затемнение-кружок
    play music glazaout
    scene black with off
    pause 1.0
    scene bg lift with onn
    stop music fadeout 3

    dvor '''
    Советую посетить первый этаж, там можно отведать вкуснейшие блюда.

    Думаю, и вы найдёте что-нибудь себе по вкусу, заранее желаю приятного аппетита!
    '''
    gg "Спасибо… *в недоумении*"

    '''Лифт поднимается с цокольного на первый'''

# Объявляется таймер
#     $ timez = 100
#     $ time_range = 100
#     $ marker = "no_choice"
#     $ menu_timer_onoff=True
#
#     menu:
#         ch "Выбор?"
#
#         "1":
#             "Вы выбрали первый вариант"
#
#             jump final1
#         "2":
#             "Вы выбрали второй вариант"
#
#             jump final2
#
# label final1:
#     gg "Поздравляю, вы открыли первую концовку!"
#
#     jump start
#
# label final2:
#     gg "Поздравляю, вы открыли вторую концовку!"
#
#     return
#
# label no_choice:
#     "Неудача"

    return
