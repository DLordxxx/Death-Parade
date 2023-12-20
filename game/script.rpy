# Определение персонажей игры

define gg = Character('???', color="#5a11ad") #фиол


define ch = Character('Чревоугодие', color="#FF6600") #оранж
define gul = Character('Гулу', color="#FF6600")

define le = Character('Лень', color="#00bfff") #голуб
define asid = Character('Диас', color="#00bfff")

define jad = Character('Жадность', color="#ccff00") #шартрез
define ava = Character('Аварит', color="#ccff00")

define lux = Character('Похоть', color="#c4149b") #роза
define lux = Character('Люкси', color="#c4149b")

define gn = Character('Гнев', color="#bf0d0d") #крас
define ai = Character('Айра', color="#bf0d0d")

define gor = Character('Гордыня', color="#FEb7F0") #цвет испуганой нимфы+b
define bia = Character('Бия', color="#FEb7F0")

define zav = Character('Зависть', color="#5353ec") #лазурь
define dvor = Character('Дворецкий', color="#5353ec")

#Запоминающие действия
define beryshi = False
define snova = False
define vajno1 = False
define vajno2 = False
define was = False

# Музыка и звуки
define audio.glazaout = "music/glazaout.ogg"
define audio.sbil = "sound/sbil.ogg"
define audio.fon = "music/fon.mp3"
define audio.doroga = "music/doroga.mp3"
define audio.pecepcia = "music/pecepcia.mp3"
define audio.rest = "music/rest.mp3"
define audio.lenb = "music/lenb.mp3"
define audio.jad = "music/jad.mp3"
define audio.polomka = "sound/polomka.mp3"
define audio.pohot = "music/pohot.mp3"
define audio.romantic = "music/romantic.mp3"
define audio.gnev = "music/gnev.mp3"
define audio.mogilamusic = "music/mogilamusic.mp3"
define audio.vstrecha = "music/vstrecha.mp3"
define audio.ypal = "sound/ypal.mp3"
define audio.koroleva = "music/koroleva.mp3"
define audio.taina = "music/taina.mp3"
define audio.alarm = "music/alarm.mp3"
define audio.zavistb = "music/zavistb.mp3"
define audio.happyend = "music/happyend.mp3"
define audio.dver = "sound/dver.mp3"
define audio.open = "sound/open.mp3"

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

# ЗНАКОМСТВО
    stop music fadeout 1
    scene bg lift
    with fade
    play music fon

    dvor '''
    Приветствую вас в нашем отеле «Mortiferum Hotel»!

    Мы рады каждому гостю, ведь именно он подарит незабываемые эмоции, которые вы запомните навсегда!

    Какой этаж желаете?
    '''
#здесь нужен силует гг
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg '''
    Что простите?

    Куда я попал?
    '''
#пропадает гг - говорит двор
    hide gg
    with dissolve
    dvor '''
    Ох, так вы один из новых постояльцев?

    Позвольте мне немного вас просветить. Этот отель по своей сути необычный – люди, прибывшие сюда могут очиститься как физически, так и духовно.
    '''
    stop music fadeout 1
#(гудок от фуры) (флешка)
    play music glazaout
    scene black with off
    pause 1.0
    scene bg machine with onn
    stop music fadeout 3

    play music doroga

    '''
    Всплывают резкие воспоминания…

    Яркий свет фар и громкий шум от гудка надвигающейся фуры, которую уже ничто не остановит.
    '''
    stop music fadeout 1
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
    play music fon
    dvor '''
    Советую посетить первый этаж, там можно отведать вкуснейшие блюда.

    Думаю, и вы найдёте что-нибудь себе по вкусу, заранее желаю приятного аппетита!
    '''
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Спасибо… *в недоумении*"
    hide gg
    with dissolve
    '''Лифт поднимается с цокольного на первый'''

# РЕЦЕПЦИЯ
    stop music fadeout 1
    scene bg recpcia
    with fade
    play music pecepcia
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg '''
    Здесь кто-нибудь есть?

    Хм, а что это?
    '''
    "*Найден листочек*"
    show gg norm:
        zoom .3
        xalign 0.1
        yalign 0.7
    with move
    menu:
        gg "Занятно…"

        "Взять":
            #Сцена с листочек-чек (порядок блюд)
            hide gg
            with dissolve
            scene bg chek
            with fade
            pause
            gg "Интересно, к чему бы это?"
            scene black
            with fade
            "Взяв листочек, он направился в ресторан."

        "Оставить":
            hide gg
            with dissolve
            scene black
            with fade
            "Оставив листочек, он направился в ресторан."

#первый этаж, ЧРЕВОУГОДИЕ
    stop music fadeout 1
    scene bg restaurant
    with fade
    play music rest
    show chrev norm:
        zoom 1.2
        xalign 0.4
        yalign 0.99
    with dissolve
    gul'''
    Не желаете ли что-нибудь отведать?
    '''

label restaurant:
    #ВЫБРАТЬ ПРАВИЛЬНЫЙ ПОРЯДОК (2413)=(ГРЕХ)
    show chrev norm:
        zoom 1.2
        xalign 0.99
        yalign 0.99
    with move
    menu:
        gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете."

        #ПОРЯДОК "Е"
        "Ежевичный чизкейк":
            menu:
                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                #ПОРЯДОК "ЕГ"
                "Гребешки в сливочном соусе":
                    menu:
                        gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "ЕГХ"
                        "Хинкали с шампиньонами":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ЕГХР"
                                "Ризотто с песто":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant

                        #ПОРЯДОК "ЕГР"
                        "Ризотто с песто":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ЕГРХ"
                                "Хинкали с шампиньонами":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant
                #ПОРЯДОК "ЕХ"
                "Хинкали с шампиньонами":
                    menu:
                        gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "ЕХГ"
                        "Гребешки в сливочном соусе":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ЕХГР"
                                "Ризотто с песто":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant
                        #ПОРЯДОК "ЕХР"
                        "Ризотто с песто":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ЕХРГ"
                                "Гребешки в сливочном соусе":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant
                #ПОРЯДОК "ЕР"
                "Ризотто с песто":
                    menu:
                        gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "ЕРГ"
                        "Гребешки в сливочном соусе":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ЕРГX"
                                "Хинкали с шампиньонами":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant

                        #ПОРЯДОК "ЕРХ"
                        "Хинкали с шампиньонами":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ЕРХГ"
                                "Гребешки в сливочном соусе":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant

        #ПОРЯДОК "Г"
        "Гребешки в сливочном соусе":
            menu:
                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                #ПОРЯДОК "ГЕ"
                "Ежевичный чизкейк":
                    menu:
                        gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "ГЕХ"
                        "Хинкали с шампиньонами":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ГЕХР"
                                "Ризотто с песто":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant

                        #ПОРЯДОК "ГЕР"
                        "Ризотто с песто":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ГЕРХ"
                                "Хинкали с шампиньонами":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant

                #ПОРЯДОК "ГХ"
                "Хинкали с шампиньонами":
                    menu:
                        gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "ГХЕ"
                        "Ежевичный чизкейк":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                "Ризотто с песто":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant

                        #ПОРЯДОК "ГХР"
                        "Ризотто с песто":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ГХРЕ"
                                "Ежевичный чизкейк":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant

                #ПОРЯДОК "ГР"
                "Ризотто с песто":
                    menu:
                        gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "ГРЕ"
                        "Ежевичный чизкейк":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ГРЕХ"
                                "Хинкали с шампиньонами":
                                    gul"Надеюсь вам понравились наши блюда и вы вернетесь к нам еще раз!"
                                    hide chrev
                                    with dissolve
                                    jump skip1

                        #ПОРЯДОК "ГРХ"
                        "Хинкали с шампиньонами":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ГРХЕ"
                                "Ежевичный чизкейк":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant

        #ПОРЯДОК "Х"
        "Хинкали с шампиньонами":
            menu:
                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                #ПОРЯДОК "ХЕ"
                "Ежевичный чизкейк":
                    menu:
                        gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "ХЕГ"
                        "Гребешки в сливочном соусе":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ХЕГР"
                                "Ризотто с песто":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant

                        #ПОРЯДОК "ХЕР"
                        "Ризотто с песто":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ХЕРГ"
                                "Гребешки в сливочном соусе":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant

                #ПОРЯДОК "ХГ"
                "Гребешки в сливочном соусе":
                    menu:
                        gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "ХГЕ"
                        "Ежевичный чизкейк":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                "Ризотто с песто":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant

                        #ПОРЯДОК "ХГР"
                        "Ризотто с песто":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ХГРЕ"
                                "Ежевичный чизкейк":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant

                #ПОРЯДОК "ХР"
                "Ризотто с песто":
                    menu:
                        gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "ХРЕ"
                        "Ежевичный чизкейк":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ХРЕГ"
                                "Гребешки в сливочном соусе":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant

                        #ПОРЯДОК "ХРГ"
                        "Гребешки в сливочном соусе":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ХРГЕ"
                                "Ежевичный чизкейк":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant

        #ПОРЯДОК "Р"
        "Ризотто с песто":
            menu:
                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                #ПОРЯДОК "РЕ"
                "Ежевичный чизкейк":
                    menu:
                        gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "РЕГ"
                        "Гребешки в сливочном соусе":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "РЕГХ"
                                "Хинкали с шампиньонами":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant

                        #ПОРЯДОК "РЕХ"
                        "Хинкали с шампиньонами":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "РЕХГ"
                                "Гребешки в сливочном соусе":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant

                #ПОРЯДОК "РГ"
                "Гребешки в сливочном соусе":
                    menu:
                        gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "РГЕ"
                        "Ежевичный чизкейк":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "РГЕХ"
                                "Хинкали с шампиньонами":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant

                        #ПОРЯДОК "РГХ"
                        "Хинкали с шампиньонами":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "РГХЕ"
                                "Ежевичный чизкейк":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant

                #ПОРЯДОК "РХ"
                "Хинкали с шампиньонами":
                    menu:
                        gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "РХЕ"
                        "Ежевичный чизкейк":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "РХЕГ"
                                "Гребешки в сливочном соусе":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant

                        #ПОРЯДОК "РХГ"
                        "Гребешки в сливочном соусе":
                            menu:
                                gul"Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "РХГЕ"
                                "Ежевичный чизкейк":
                                    gul"Вы уверены, что съедите все?"
                                    jump restaurant

#ЛИФТ-РАЗГОВОРЫ
label skip1:
    scene black
    with fade
    "Возвращается к лифту."
    stop music fadeout 1
    if snova:
        scene bg lenb
        with fade
        play music lenb
        show lenb norm:
            zoom .6
            xalign 0.5
            yalign 0.7
        with dissolve

        asid"Снова вы? Ну как, выспались?"
        jump yshel

    play music fon
    scene bg lift
    with fade

    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Тот молодой господин, в ресторане, был несколько странным. Вы знакомы с ним?"
    hide gg
    with dissolve
    dvor '''
    Вряд ли. *небольшая улыбка на лице*

    Желаете продолжить обзор нашего отеля?
    '''
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg '''
    Чертовщина какая-то.

    Мне надо поскорее отсюда выбраться... *шепотом*
    '''
    hide lenb
    with dissolve
    scene black
    with fade
    "Лифт поднимается на второй этаж."

#второй этаж, ЛЕНЬ
label lenb:
    stop music fadeout 1
    scene bg lenb
    with fade
    play music lenb
    '''
    Фойе представляет собой небольшое пространство с тусклым светом, который едва ли освещает дюжину картин на стене.

    Чуть ниже красовались оливковые диванчики и, судя по их виду, простояли они здесь больше века.

    На одном из них расположился джентльмен, не отводящий взгляда от вычурных произведений искусства.
    '''
    show lenb norm:
        zoom .6
        xalign 0.5
        yalign 0.7
    with dissolve
    asid"Неужели вам хочется бегать, словно тушканчик, по этажам?"
    hide lenb
    with dissolve
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Что вы имеете в виду?"
    hide gg
    with dissolve
    show lenb norm:
        zoom .6
        xalign 0.5
        yalign 0.7
    with dissolve
    asid'''
    Чуточку отдыха никому не помешает.

    Я сижу здесь порядка двух сотен лет, избегая всякую суету.

    Вы в самом деле думаете, что я несчастен?
    '''
    hide lenb
    with dissolve
    '''Мужчина откидывается назад, отчего пролежни дивана под ним становятся гораздо заметнее.'''
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Прошу прощения, но мне пора идти, я хочу осмотреть все этажи отеля."
    hide gg
    with dissolve
    show lenb norm:
        zoom .6
        xalign 0.5
        yalign 0.7
    with dissolve
    asid"Бросьте, милостивый. Разве вам здесь не нравится?"
    show lenb norm:
        zoom .6
        xalign 0.5
        yalign 0.8
    with move
    menu:
        asid"Вечное спокойствие, тишина, не надо никуда лишний раз бегать…"

        "Попытаться уйти":
            jump skip2

        "Остаться":
            jump skip2

#ИЛЛЮЗИЯ ВЫБОРА
label skip2:
    asid"Вы не понимаете, что теряете!"
    hide lenb
    with dissolve
    '''Лицо мужчины вмиг стало мрачным.

    Его слабые и дрожащие руки едва ли могли меня удержать, но я все равно не способен был сделать и шага в сторону лифта.
    '''
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Пустите!"
    hide gg
    with dissolve
    show lenb norm:
        zoom .6
        xalign 0.5
        yalign 0.8
    with dissolve
    asid"Таких удобств вам более нигде не отыскать, поверьте на слово!"
    hide lenb
    with dissolve
    show gg norm:
        zoom .3
        xalign 0.1
        yalign 0.7
    with dissolve
    menu:
        gg "Не смейте меня задерживать! Я не собираюсь здесь больше оставаться!"

        "Попытаться уйти":
            jump yshel

        "Не сопротивляться":
            jump ostalsa

#НЕ ПОДДАЛСЯ РЕЧАМ ЛЕНИ
label yshel:
    hide gg
    with dissolve
    show lenb norm:
        zoom .6
        xalign 0.5
        yalign 0.7
    with dissolve
    asid"*вздох* Смею предположить, что вам претит моя компания."
    hide lenb
    with dissolve
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "..."
    hide gg
    with dissolve
    show lenb norm:
        zoom .6
        xalign 0.5
        yalign 0.7
    with dissolve
    asid'''
    В любом случае мне было приятно с вами повстречаться.

    Примите небольшой презент в знак признательности за наше мимолетное знакомство.
    '''
    hide lenb
    with dissolve
    "Мужчина протянул небольшую коробочку."
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Что там?"
    hide gg
    with dissolve
    show lenb norm:
        zoom .6
        xalign 0.5
        yalign 0.7
    with dissolve
    asid"В отеле всегда царит шум, но на моем этаже целыми сутками тишина, потому возьми с собой эти беруши. Уверен, позже они тебе понадобятся."
    $ renpy.notify ("Получены беруши")
    hide lenb
    with dissolve
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Вы крайне добры."
    hide gg
    with dissolve

    stop music fadeout 1
    #ЗАПОМИНАЮЩЕЕ ДЕЙСТВИЕ
    $ beryshi = True
    jump skip3

#Решил полежать
label ostalsa:
    gg "И вправду, думаю, отдых мне не помешает."
    hide gg
    with dissolve
    stop music fadeout 1
    scene black
    with fade
    play music rest
    gg "Кажется, где-то это я уже слышал."

    #ЗАПОМИНАЮЩЕЕ ДЕЙСТВИЕ
    $ snova = True
    scene bg restaurant
    with fade
    jump restaurant



#ЛИФТ-РАЗГОВОРЫ
label skip3:
    scene bg lift
    with fade
    play music fon
    dvor "Ох, вы уже здесь… Не захотелось составить компанию нашему замечательному постояльцу со второго этажа?"
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Нет, он несколько странный."
    hide gg
    with dissolve
    dvor "Вероятно, вы правы. *хмурится*"
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Будьте любезны, на третий."
    hide gg
    with dissolve
    dvor "Как вам будет угодно."

#третий этаж, ЖАДНОСТЬ

label avanostb:
    stop music fadeout 1
    scene bg jadnostb
    with fade
    play music jad
    '''Громкая музыка из дальнего проигрывателя сильно бьет по ушам.

    Над ним склонился мужчина, отчаянно пытаясь починить его, но, кажется, все безнадежно.
    '''
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Здравс…"
    hide gg
    with dissolve
    show jad norm:
        zoom .5
        xalign 0.7
        yalign 0.99
    with dissolve
    ava "Черт побери, заткнись! Я не спал уже восемь ночей!"
    hide jad
    with dissolve
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Я подумал вам нужна помощь..."
    hide gg
    with dissolve
    show jad norm:
        zoom .5
        xalign 0.7
        yalign 0.99
    with dissolve
    ava "Себе помоги, мальчонка!"
    hide jad
    with dissolve
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Почему вы мне грубите? Я ведь к вам с добрыми намерениями."
    hide gg
    with dissolve
    show jad norm:
        zoom .5
        xalign 0.7
        yalign 0.99
    with dissolve
    ava "Ну и с чем ты мне поможешь?"
    hide jad
    with dissolve
    # Развилка
    menu:
        "*достает беруши*"

        "Отдать":
            jump otdal

        "Оставить себе":
            jump sebe

label otdal:
    $ renpy.notify ("Отданы беруши")
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Кажется, они вам нужнее."
    hide gg
    with dissolve
    show jad norm:
        zoom .5
        xalign 0.7
        yalign 0.99
    with dissolve
    ava "Почему делишься со мной столь “дорогой” вещью?"
    hide jad
    with dissolve
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Мне по нраву шумные места."
    hide gg
    with dissolve
    $ vajno1 = True

    jump skip4

label sebe:
    "*замечает молоток*"
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Кажется, у меня есть решение."
    hide gg
    with dissolve
    "*начинает замахиваться*"
    # звук поломки
    stop music fadeout 1
    play sound polomka
    "*хрусь*"
    show jad norm:
        zoom .5
        xalign 0.7
        yalign 0.99
    with dissolve
    ava "Хм, интересно, почему я раньше до этого не догадался."
    jump skip4

label skip4:
    show jad norm:
        zoom .5
        xalign 0.7
        yalign 0.99
    with dissolve
    ava "Спасибо тебе, теперь я наконец-то смогу проводить свое время в тишине и спокойствии у себя в логове."
    hide jad
    with dissolve
    stop music fadeout 1

    scene bg lift
    with fade
    play music fon
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Так приятно вновь оказаться в тишине."
    hide gg
    with dissolve
    dvor "Безусловно, мы ведь стараемся обеспечить комфорт каждому гостю."
    "*свет становится явно тусклее*"
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.6
    with dissolve
    gg "Вам еще есть над чем поработать."
    hide gg
    with dissolve
    "*нажимает на кнопку четвертого этажа*"

#четвертый этаж, ПОХОТЬ

label pohotb:
    stop music fadeout 1
    scene bg pohot
    with fade
    play music pohot
    "*комната усыпана свечами и лепестками роз на полу*"
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg '''Романтично…

    Интересно, для кого такая атмосфера сделана?
    '''
    hide gg
    with dissolve
    show pohotb norm:
        zoom .16
        xalign 0.8
        yalign 0.99
    with dissolve
    lux '''Давненько я не встречала настолько обворожительных джентльменов в отеле.

    Вы здесь недавно?
    '''
    hide pohotb
    with dissolve
    "*на лице девушки кроткая улыбка*"
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Приятно слышать. *смущенно*"
    hide gg
    with dissolve
    show pohotb zovet:
        zoom .26
        xalign 0.7
        yalign 0.99
    with dissolve
    lux "Присаживайся ко мне на диванчик, красавчик."
    "*присел на край дивана*"
    show pohotb zovet:
        zoom .26
        xalign 0.9
        yalign 0.99
    with move
#БЕЗ РАЗЛИВОК
    menu:
        lux "Вам понравился мой прием?"

        "Сказать правду":
            jump true

        "Солгать":
            jump false

#СКАЗАЛ ПРАВДУ
label true:
    hide pohotb
    with dissolve
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg '''Да…

    Но к чему такое большое внимание ко мне?
    '''
    hide gg
    with dissolve
    show pohotb zovet:
        zoom .26
        xalign 0.9
        yalign 0.99
    with dissolve
    show pohotb zovet:
        zoom .26
        xalign 0.7
        yalign 0.99
    with move
    lux "Что вы, не льстите себе."
    jump dialog1

#СКАЗАЛ ЛОЖЬ
label false:
    hide pohotb
    with dissolve
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Нет, мне не нравится ваша навязчивость."
    hide gg
    with dissolve
    show pohotb zovet:
        zoom .26
        xalign 0.9
        yalign 0.99
    with dissolve
    show pohotb zovet:
        zoom .26
        xalign 0.7
        yalign 0.99
    with move
    lux "Значит мне нужно узнать тебя поближе…"
    jump dialog1

#ПРОДОЛЖЕНИЕ ДИАЛОГА
label dialog1:
    show pohotb zovet:
        zoom .26
        xalign 0.5
        yalign 0.99
    with move
    "*девушка подсела ближе и нежно опустила руку на колено*"
    show pohotb zovet:
        zoom .26
        xalign 0.1
        yalign 0.99
    with move
    menu:
        lux "У такого мужчины как вы, должно быть, есть девушка?"

        "Да":
            hide pohotb
            with dissolve
            show gg norm:
                zoom .3
                xalign 0.25
                yalign 0.7
            with dissolve
            gg "Поэтому мне не нужно долго задерживаться, иначе она будет переживать за меня."
            hide gg
            with dissolve
            show pohotb zovet:
                zoom .26
                xalign 0.1
                yalign 0.99
            with dissolve
            show pohotb zovet:
                zoom .26
                xalign 0.5
                yalign 0.99
            with move
            lux "Если ты “задержишься”, то у нас будет больше времени, чтобы раскрыть наши отношения."
            hide pohotb
            with dissolve
            show gg norm:
                zoom .3
                xalign 0.25
                yalign 0.7
            with dissolve
            gg "Наши?"
            hide gg
            with dissolve
            "*проскользнула ухмылка на ее лице*"
            show pohotb zovet:
                zoom .26
                xalign 0.5
                yalign 0.99
            with dissolve
            show pohotb zovet:
                zoom .26
                xalign 0.1
                yalign 0.99
            with move
            lux '''Разве тебе не хочется жить в большом доме с личным дворецким.

            Будешь наслаждаться жизнью припеваючи: в достатке, тепле, уюте и окутанный любовью.
            '''
            hide pohotb
            with dissolve
            jump dialog2

        "Нет":
            hide pohotb
            with dissolve
            jump dialog2

#ПРОДОЛЖЕНИЕ ДИАЛОГА
label dialog2:
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Я не совсем понимаю, к чему вы клоните."
    hide gg
    with dissolve
    show pohotb zovet:
        zoom .26
        xalign 0.1
        yalign 0.99
    with dissolve
    show pohotb zovet:
        zoom .26
        xalign 0.5
        yalign 0.99
    with move
    lux "Как вы смотрите на то, чтобы провести незабываемый вечер в компании юной дамы."
    hide pohotb
    with dissolve
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "..."
    hide gg
    with dissolve
    hide gg
    with dissolve
    show pohotb zovet:
        zoom .26
        xalign 0.5
        yalign 0.99
    with dissolve
    show pohotb zovet:
        zoom .26
        xalign 0.1
        yalign 0.99
    with move
    menu:

        lux "Неужели вы хотите, чтобы такая девушка как я осталась в одиночестве?"

        "Составить компанию":
            hide pohotb
            with dissolve
            show gg norm:
                zoom .3
                xalign 0.25
                yalign 0.7
            with dissolve
            gg "Вы настолько очаровательная девушка, что вам невозможно отказать."
            hide gg
            with dissolve
            show pohotb zovet:
                zoom .26
                xalign 0.1
                yalign 0.99
            with dissolve
            show pohotb zovet:
                zoom .26
                xalign 0.5
                yalign 0.99
            with move
            lux '''Наконец-то нашелся достойный мужчина мне в мужья.

            Теперь мы сможем жить в свое удовольствие и ни в чем себе не отказывать.
            '''
            hide pohotb
            with dissolve
            jump romantic

        "Покинуть комнату":
            hide pohotb
            with dissolve
            show gg norm:
                zoom .3
                xalign 0.25
                yalign 0.7
            with dissolve
            gg "Ни в коем случае, я бы с радостью остался, но у меня совсем нет времени."
            hide gg
            with dissolve
            show pohotb zovet:
                zoom .26
                xalign 0.1
                yalign 0.99
            with dissolve
            show pohotb zovet:
                zoom .26
                xalign 0.5
                yalign 0.99
            with move
            lux "Очень жаль, а мне хотелось всего лишь быть любимой и счастливой со своим близким человеком."
            hide pohotb
            with dissolve
            jump dialog3

### РОМАНТИЧЕСКАЯ КОНЦОВКА (ОСТАЛСЯ В ЗАТОЧЕНИИ У ЖЕНЩИНЫ)
label romantic:
    stop music fadeout 1
    window hide
    scene poster wedding
    with fade
    play music romantic
    pause
    "Девушка добился своего и теперь у нее есть достойный мужчина."
    stop music fadeout 1
    $ persistent.ending1 = True
    return

#ПРОДОЛЖЕНИЕ ДИАЛОГА
label dialog3:
    stop music fadeout 1
    scene black
    with fade
    "*заходит в лифт*"
    scene bg lift
    with fade
    play music fon
    dvor "Значит все-таки отказались…"
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Печально оставлять такую даму в одиночестве, но ничего не поделаешь…"
    hide gg
    with dissolve
    dvor "Возможно, ей нужен более достойный мужчина."
    scene black
    with fade
    "*нажимает на кнопку пятого этажа*"

#пятый этаж, ГНЕВ
label gnev:
    stop music fadeout 1
    scene bg gnev
    with fade
    play music vstrecha
    '''Стены пятого этажа были настолько близки друг к другу, что казалось будто они вот-вот сомкнутся, придавив всё вокруг, словно они сжимают каждого проходящего в лепёшку.

    Двери очень манили своими внушительными размерами и привлекали внимание.'''
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Интересно, они куда ведут?"
    hide gg
    with dissolve
    show gnev norm:
        zoom .58
        xalign 0.65
        yalign 0.99
    with dissolve
    ai '''Эй, мужик!

    Смотри куда прешь!'''
    hide gnev
    with dissolve
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Комната слишком мала, а я хотел пройти…"
    hide gg
    with dissolve
    show gnev norm:
        zoom .58
        xalign 0.65
        yalign 0.99
    with dissolve
    ai "Меня это не волнует, умей отвечать за свои поступки, щенок."
    hide gnev
    with dissolve
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Как вы меня назвали? Мне послышалось?"
    hide gg
    with dissolve
    show gnev podozrenie:
        zoom .7
        xalign 0.68
        yalign 0.99
    with dissolve
    ai "Cопляк, почисти свои грязные уши."
    hide gnev
    with dissolve
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Прошу разговаривать более спокойно с незнакомым для вас человеком, грубиян!"
    hide gg
    with dissolve
    show gnev podozrenie:
        zoom .7
        xalign 0.68
        yalign 0.99
    with dissolve
    ai '''Думаешь, если ты такой добрый и хороший, то тебе все дозволено.

    Я тебе сейчас покажу что значит «быть спокойным»
    '''
    hide gnev
    with dissolve
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "И что же вы мне сделаете?"

    '''*гнев достает нож*

    *начинает ускорять шаг*
    '''
    stop music fadeout 1

#ПЕРВЫЙ ВЫБОР (ЛАБИРИНТ)
label labirint1:
    play music gnev
    # Объявляется таймер
    $ timez = 100
    $ time_range = 100
    $ marker = "no_choice"
    $ menu_timer_onoff=True
    show gg norm:
        zoom .3
        xalign 0.1
        yalign 0.7
    with move
label dver1:
    menu:
        gg "Нельзя ошибаться…"

        "Налево":
            play sound dver
            "*заперто*"
            jump dver1
        "Прямо":
            play sound open
            gg "Одна есть"
            jump labirint2
        "Направо":
            play sound dver
            "*заперто*"
            jump dver1

#ВТОРОЙ ВЫБОР (ЛАБИРИНТ)
label labirint2:
    $ timez = 100
    $ time_range = 100
    $ marker = "no_choice"
    $ menu_timer_onoff=True

label dver2:
    menu:
        gg "Нельзя ошибаться…"

        "Налево":
            play sound dver
            "*заперто*"
            jump dver2
        "Прямо":
            play sound dver
            "*заперто*"
            jump dver2
        "Направо":
            play sound open
            "Еще немного"
            jump labirint3


#ТРЕТИЙ ВЫБОР (ЛАБИРИНТ)
label labirint3:
    $ timez = 100
    $ time_range = 100
    $ marker = "no_choice"
    $ menu_timer_onoff=True

label dver3:
    menu:
        gg "Нельзя ошибаться…"

        "Налево":
            play sound dver
            "*заперто*"
            jump dver3
        "Прямо":
            play sound dver
            "*заперто*"
            jump dver3
        "Направо":
            play sound open
            "Последняя..."
            hide gg
            with dissolve
            $ menu_timer_onoff=False
            jump exit

label no_choice:
    stop music fadeout 1
    scene black
    with fade

    gg "Кажется, у меня потемнело в глазах..."
    #УПАЛ
    play sound ypal
    "*теряет сознание*"

    ### КОНЦОВКА-СМЕРТЬ
    play music mogilamusic

    window hide
    scene poster death
    with fade
    pause
    "Всех ждет один конец..."
    stop music fadeout 1
    $ persistent.ending2 = True
    return

#ВЫШЕЛ ИЗ ЛАБИРИНТА (EXIT)
label exit:
    stop music fadeout 1
    scene black
    with fade
    gg "Фух, оторвался…"
    "*идет к лифту*"

    scene bg lift
    with fade
    play music fon
    dvor '''Все в порядке?

    Выглядите неважно.
    '''
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg '''Меня преследовал психопат.

    Почему вы с этим ничего не делаете.
    '''
    hide gg
    with dissolve
    dvor '''Странно, такого не наблюдалось.

    Впрочем, я не могу ничего с этим поделать.
    '''

#шестой этаж, ГОРДЫНЯ
label gorbyz:
    stop music fadeout 1
    scene bg gord
    with fade
    play music koroleva
    show gord norm:
        xalign 0.85
        yalign 0.99
    with dissolve
    bia "Опять эти невежды."
    hide gord
    with dissolve
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Что простите?"
    hide gg
    with dissolve
    show gord norm:
        xalign 0.85
        yalign 0.99
    with dissolve
    bia "Почему меня всегда окружают существа похожие на людей..."
    hide gord
    with dissolve
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Вам не кажется, что начинать диалог с оскорбления, считается плохим тоном."
    hide gg
    with dissolve
    show gord dymaet:
        zoom .6
        xalign 0.85
        yalign 0.99
    with dissolve
    bia '''Возможно, вы неправильно меня поняли...

    Для меня уважение к собеседнику является неотъемлемой частью диалога, но вы не похожи на джентльмена.
    '''
    hide gord
    with dissolve
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Давайте не будем ссориться."
    hide gg
    with dissolve
    show gord dymaet:
        zoom .6
        xalign 0.85
        yalign 0.99
    with dissolve
    bia '''«Ссоры» раскрывают мой потенциал находиться в высшем обществе.

    Такому плебею как вы этого не понять.
    '''
    show gord dymaet:
        zoom .6
        xalign 0.99
        yalign 0.99
    with move
    menu:
        bia "Меня огорчает разделять с вами один воздух."

        "Спокойно":
            hide gord
            with dissolve
            show gg norm:
                zoom .3
                xalign 0.25
                yalign 0.7
            with dissolve
            gg "Вы слишком молоды и многого не знаете, так что не стоит задирать свой нос, настолько высоко."
            hide gg
            with dissolve
            show gord interes:
                zoom .6
                xalign 0.85
                yalign 0.99
            with dissolve
            bia "Да что вы обо мне знаете!"
            hide gord
            with dissolve
            show gg norm:
                zoom .3
                xalign 0.25
                yalign 0.7
            with dissolve
            gg "Просто не могу поверить, что ваш удел-это оскорбления и больше вы ни на что не способны."
            hide gg
            with dissolve
            show gord interes:
                zoom .6
                xalign 0.85
                yalign 0.99
            with dissolve
            bia "Я способен уничтожать эго, одним только словом, вы считаете этого мало?"
            hide gord
            with dissolve
            show gg norm:
                zoom .3
                xalign 0.25
                yalign 0.7
            with dissolve
            gg '''Думаю, вам нужно взглянуть на жизнь под другим углом, где нет оскорблений, высокомерия и все счастливы.

            Вы же должны понимать, что перед смертью все равны и всё что вы натворите, будучи живым, припомнится вам в будущем.'''
            hide gg
            with dissolve
            show gord interes:
                zoom .6
                xalign 0.85
                yalign 0.99
            with dissolve
            bia "Вы единственный человек, который так снисходительно относится к моему высокомерию, меня это поразило."
            hide gord
            with dissolve
            "*кроткая улыбка*"
            show gord interes:
                zoom .6
                xalign 0.85
                yalign 0.99
            with dissolve
            bia '''Возможно, вы правы и мне нужно пересмотреть свое отношение к людям.

            В качестве извинений могу сказать информацию, которая пригодится тебе в будущем.

            Запомни этот шифр, он тебе скоро понадобятся…'''
            $ renpy.notify ("Получен шифр")
            bia "12562"
            hide gord
            with dissolve
            ### ВАЖНО
            stop music fadeout 1
            $ vajno2 = True
            jump skip5

        "Грубо":
            hide gord
            with dissolve
            show gg norm:
                zoom .3
                xalign 0.25
                yalign 0.7
            with dissolve
            gg "Я не потерплю оскорбления в свой адрес, ты слишком ничтожен, чтобы разговаривать со мной так!"
            hide gg
            with dissolve
            show gord interes:
                zoom .6
                xalign 0.85
                yalign 0.99
            with dissolve
            bia "Как же легко вывести из себя таких толстолобых как ты."
            hide gord
            with dissolve
            show gg norm:
                zoom .3
                xalign 0.25
                yalign 0.7
            with dissolve
            gg "Может вы уже закончите меня оскорблять!"
            hide gg
            with dissolve
            show gord interes:
                zoom .6
                xalign 0.85
                yalign 0.99
            with dissolve
            bia "Я сделаю это, когда сам посчитаю нужным."
            hide gord
            with dissolve
            show gg norm:
                zoom .3
                xalign 0.25
                yalign 0.7
            with dissolve
            gg '''С вами просто невозможно разговаривать!

            Вы невыносимы!'''
            hide gg
            with dissolve
            show gord interes:
                zoom .6
                xalign 0.85
                yalign 0.99
            with dissolve
            bia "Думал вы продержитесь подольше…"
            hide gord
            with dissolve
            scene black
            with fade
            "*идет к лифту*"
            stop music fadeout 1
            jump skip5

# СЦЕНА ПЕРЕД ЛИФТОМ
label skip5:
    scene bg pered
    with fade
    play music fon
# ВЫБОР (ЦОКОЛЬНЫЙ ЭТАЖ)
    menu:
        gg "Интересно, куда исчез Дворецкий?"

        "Цокольный этаж":
            stop music fadeout 1
            jump cokol

        "Седьмой этаж":
            stop music fadeout 1
            jump zavistb


# ЦОКОЛЬНЫЙ ЭТАЖ
label cokol:
    scene bg cokol
    with fade
    play music taina
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg '''Просторная комнатка.

    Может быть я здесь найду что-нибудь интересное.'''
    hide gg
    with dissolve
    # СЦЕНА ШКАТУЛКИ
    scene bg skatylka
    with fade
    "*находит шкатулку*"

    if vajno1 and vajno2:
        menu:
            gg "Необходим шифр..."

            "12461":
                #ALARM
                stop music fadeout 1
                play music alarm
                "*сработала сигнализация*"
                jump skip6

            "12562 *что-то знакомое*":
                "В шкатулке лежал старый листок."
                jump pravda

            "12451":
                #ALARM
                stop music fadeout 1
                play music alarm
                "*сработала сигнализация*"
                jump skip6

            "12361":
                #ALARM
                stop music fadeout 1
                play music alarm
                "*сработала сигнализация*"
                jump skip6
    else:
        menu:
            gg "Необходим шифр..."

            "12461":
                #ALARM
                stop music fadeout 1
                play music alarm
                "*сработала сигнализация*"
                jump skip6

            "12562":
                "В шкатулке лежал старый листок."
                jump pravda

            "12451":
                #ALARM
                stop music fadeout 1
                play music alarm
                "*сработала сигнализация*"
                jump skip6

            "12361":
                #ALARM
                stop music fadeout 1
                play music alarm
                "*сработала сигнализация*"
                jump skip6

# ОТЕЛЬ-ЛИМБ (ПРАВДА)
label pravda:
    scene black
    with fade
    '''
    Вы умерли и находитесь в отеле-лимбе, суть которого проверить вашу стойкость.

    Перед заключительным испытанием вы должны узнать правду.

    Дворецкий – это ваш брат, он и является судьей душ, попавших в этот отель.

    У вас есть два пути:

    Забвение.

    Или...

    Перерождение.

    Выбор за вами, будьте осторожны!

    '''
    gg "..."
    $ was = True
    jump skip6

# ПРОДОЛЖАЕМ
label skip6:
    stop music fadeout 1
    scene bg pered
    with fade
    play music fon
    if was:
        "После прочитанного перебивало дыхание..."
    menu:
        "Седьмой этаж":
            jump zavistb

#седьмой этаж, ЗАВИСТЬ
label zavistb:
    stop music fadeout 1
    scene bg zavis
    with fade
    play music zavistb
    '''Последняя комната представляла собой роскошные диваны, обшитые самой дорогой кожей, камин, из которого доносился треск тлеющей древесины.

    И сам дворецкий, стоящей спиной и устремляющий свой взгляд в огромное окно из которого открывались потрясающие виды.'''
    show zavis norm:
        zoom .61
        xalign 0.8
        yalign 0.8
    with dissolve
    zav "Ну вот мы и встретились брат мой!"
    hide zavis
    with dissolve
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Почему именно здесь? Я думал ты пропал без вести…"
    hide gg
    with dissolve
    show zavis sidit:
        zoom .4
        xalign 0.85
        yalign 0.99
    with dissolve
    zav '''Так и есть, мне надоело быть твоей тенью, которая всегда обделена!

    Поэтому я решил покинуть дом и теперь вершу судьбы таких же «особенных»!'''
    hide zavis
    with dissolve
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Но как я сюда попал?"
    hide gg
    with dissolve
    show zavis sidit:
        zoom .4
        xalign 0.85
        yalign 0.99
    with dissolve
    zav "Ты умер и теперь я буду вершить твою судьбу! Ты предашься забвению или переродишься…"
    hide zavis
    with dissolve
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg '''«Предаться забвению»?

    То есть потерять всё что у меня было…'''
    hide gg
    with dissolve
    show zavis sidit:
        zoom .4
        xalign 0.85
        yalign 0.99
    with dissolve
    zav '''Даже в этом чертовом отеле у тебя есть шанс на перерождение, а я тут навечно…

    Ты словно родился с золотой ложкой во рту!'''
    hide zavis
    with dissolve
    show gg norm:
        zoom .3
        xalign 0.25
        yalign 0.7
    with dissolve
    gg "Но как я мог на это повлиять?"
    hide gg
    with dissolve
    show zavis sidit:
        zoom .4
        xalign 0.85
        yalign 0.99
    with dissolve
    menu:
        zav "Хватит уже, выбирай!"

        #СМЕРТЬ
        "Переродиться":
            hide zavis
            with dissolve
            stop music fadeout 1
            jump no_choice

        #Реинкарнация
        "Придаться забвению":
            hide zavis
            with dissolve
            stop music fadeout 1
            scene poster happy end
            with fade
            play music happyend
            pause
            "У меня получилось..."
            ### КОНЦОВКА HAPPY END
            stop music fadeout 1
            $ persistent.ending3 = True

            return

    return
