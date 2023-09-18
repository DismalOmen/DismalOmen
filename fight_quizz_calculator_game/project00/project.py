import sys
import random

def main():
    language_menu()

#SELECCIONAR IDIOMA//CHOOSE LANGUAGE
def language_menu():
    print("""
         ______________________________
        / \                             \.
        |   |                            |.
        \_ |      //ELEGIR UN IDIOMA//   |.
            |     //CHOOSE A LANGUAGE//  |.
            |                            |.
            |                            |.
            |      [1] - ESPAÑOL         |.
            |                            |.
            |                            |.
            |      [2] - ENGLISH         |.
            |                            |.
            |                            |.
            |      [3] - QUIT            |.
            |                            |.
            |   _________________________|___
            |  /                            /.
            \_/____________________________/.

          """)
    ("/     [1]     /     [2]     /     [3]     /")

    option = input("/     [1]     /     [2]     /     [3]     /")

    if option == "1":
        print()
        print()
        print()
        print("El texto se encontrará en español, espero que disfrutes!")
        menu_español()

    elif option == "2":
        print()
        print()
        print()
        print("Text will be in english, have fun!")
        menu_ingles()

    elif option == "3":
        sys.exit("See you next time! -------- Nos vemos la próxima!")

def menu_ingles():
    print("""

                   _.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._
                .-'---      - ---     --     ---   -----   - --       ----  ----   -     ---`-.
                |                     -WELCOME, SELECT FROM THE OPTIONS BELOW-                |
                |                                                                             |
                |                             [1]  Game list.                                 |
                |                                                                             |
                |                             [2]  Help/Intructions.                          |
                |                                                                             |
                |                             [3]  Back to main menu.                         |
                |                                                                             |
                |                             [4]  Exit.                                      |
                (___       _       _       _       _       _       _       _       _       ___)
                    `-._.-' (___ _) (__ _ ) (_   _) (__  _) ( __ _) (__  _) (__ _ ) `-._.-'
                            `-._.-' (  ___) ( _  _) ( _ __) (_  __) (__ __) `-._.-'
                                    `-._.-' (__  _) (__  _) (_ _ _) `-._.-'
                                            `-._.-' (_ ___) `-._.-'
                                                    `-._.-'

         """)
    option = input("/     [1]     /     [2]     /     [3]     /     [4]     /       ")
    if option == "1":
        print()
        print()
        print("Press [3] if you want to go back.")
        print()
        print()
        print("""
                _.--.__.-'""`-.__.--.__.-'""`-.__.--.__.-'""`-.__.--.__.-'""`-._
               # "`--'""`-.__.-'""`--'""`-.__.-'""`--'""`-.__.-'""`--'""`-.__.-'"  #
                #                          PATH          A                        #
                 #                         PATH          B                       #
                #                          PATH          C                        #
               #                           PATH          D                         #
             #  _.--.__.-'""`-.__.--.__.-'""`-.__.--.__.-'""`-.__.--.__.-'""`-._    #
                "`--'""`-.__.-'""`--'""`-.__.-'""`--'""`-.__.-'""`--'""`-.__.-'"

              """)
        path = input("/     [A]     /     [B]     /     [C]     /     [D]     /    [3]     /").lower()
        if path not in ["a","b","c","3","d"]:
             print()
             print("Please, select one of the options.")
             print()
             while True:
                try:
                    path = input("/     [A]     /     [B]     /     [C]     /     [D]     /     [3]     /").lower()
                    if path in ["a","b","c","3","d"]:
                        break
                except:
                    pass
        if path == "a":
            print()
            print("Welcome to path A, enjoy!")
            print()
            path_a_english()
        elif path == "b":
            print()
            print("Welcome to path B, enjoy!")
            print()
            path_b_english()
        elif path == "c":
            print()
            print("Welcome to path C, enjoy!")
            print()
            path_c_english()
        elif path == "3":
            print()
            language_menu()
            print()
        elif path == "d":
            print()
            easy_calculus()

    elif option == "2":
        print()
        print("These are the instructions, read carefully.")
        print("""

            _.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._
            .-'---      - ---     --     ---   -----   - --       ----  ----   -     ---`-.

                [PATH A: only your decisions will take you to victory, win only using
                your words, pay atention to what you really NEED to say.]

                [PATH B: win 5 BATTLES where your life is on the line.
                           CONTROLES: 1 - ATACK for 25 dmg. (win 25 mana)
                                      2 - HEAL yourself for 25 HP,
                                          you dont lose turns healing. (lose 25 mana)
                                      3 - SPECIAL HIT for 50 dmg.
                                          (lose 50 mana)]

                [PATH C: two "mini-games", one is a simple question and answer gam,e while
                the other, is a gamble game much like 4-5-6 or Cee-lo, but simpler.]

                [PATH C: simple calculator that given two numbers it will return simple
                operations like: + / - / *]

            (___       _       _       _       _       _       _       _       _       ___)
                (__  _) ( __ _) (__  _) (__ _ ) `-._.-' ( _ __) (_  __) (_ __ ) (_  __)
                ( _ __) (_  __) (__ __) `-._.-'         `-._.-' (__ __) (__  _) (__ _ )
                (__  _) (_ _ _) `-._.-'                         `-._.-' (_ _ _) (_  __)
                (_ ___) `-._.-'                                         `-._.-' (___ _)
                `-._.-'                                                         `-._.-'


              """)
        print()
        volver = input("Press any key then enter when you feel like going back to main menu.")
        if volver:
            menu_ingles()
    elif option == "3":
        language_menu()
    elif option == "4":
        sys.exit("See you soon!")
def menu_español():
    print("""

                   _.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._
                .-'---      - ---     --     ---   -----   - --       ----  ----   -     ---`-.
                |                    -BIENVENIDO, ELIGE ENTRE LAS OPCIONES-                   |
                |                                                                             |
                |                             [1]  Lista de juegos.                           |
                |                                                                             |
                |                             [2]  Ayuda/Instrucciones.                       |
                |                                                                             |
                |                             [3]  Volver atrás.                              |
                |                                                                             |
                |                             [4]  Salir.                                     |
                (___       _       _       _       _       _       _       _       _       ___)
                    `-._.-' (___ _) (__ _ ) (_   _) (__  _) ( __ _) (__  _) (__ _ ) `-._.-'
                            `-._.-' (  ___) ( _  _) ( _ __) (_  __) (__ __) `-._.-'
                                    `-._.-' (__  _) (__  _) (_ _ _) `-._.-'
                                            `-._.-' (_ ___) `-._.-'
                                                    `-._.-'

         """)
    option = input("/     [1]     /     [2]     /     [3]     /     [4]     /       ")
    if option == "1":
        print()
        print()
        print("Recordá que con [3] volves para atrás.")
        print()
        print()
        print("""
                _.--.__.-'""`-.__.--.__.-'""`-.__.--.__.-'""`-.__.--.__.-'""`-._
               # "`--'""`-.__.-'""`--'""`-.__.-'""`--'""`-.__.-'""`--'""`-.__.-'"  #
                #                          CAMINO        A                        #
                 #                         CAMINO        B                       #
                #                          CAMINO        C                       #
               #                           CAMINO        D                         #
              #   _.--.__.-'""`-.__.--.__.-'""`-.__.--.__.-'""`-.__.--.__.-'""`-._  #
                "`--'""`-.__.-'""`--'""`-.__.-'""`--'""`-.__.-'""`--'""`-.__.-'"

              """)
        path = input("/     [A]     /     [B]     /     [C]     /     [D]     /     [3]     /").lower()
        if path not in ["a","b","c","3","d"]:
             print()
             print("Por favor, seleccione una de las opciones indicadas.")
             print()
             while True:
                try:
                    path = input("/     [A]     /     [B]     /     [C]     /     [D]     /     [3]     /").lower()
                    if path in ["a","b","c","3","d"]:
                        break
                except:
                    pass
        if path == "a":
            print()
            print("Bienvenido al cámino A, disfrutá")
            print()
            path_a()
        elif path == "b":
            print()
            print("Bienvenido al cámino B, disfrutá")
            print()
            path_b()
        elif path == "c":
            print()
            print("Bienvenido al cámino C, disfrutá")
            print()
            path_c_spanish()
        elif path == "3":
            print()
            menu_español()
            print()
        elif path == "D":
            print()
            print("Bienvenido al cámino D, disfrutá")
            easy_calculus_spanish()




    elif option == "2":
        print()
        print("Estas son las instrucciones de los juegos, leé atentamente.")
        print("""

            _.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._
            .-'---      - ---     --     ---   -----   - --       ----  ----   -     ---`-.

                [CAMINO A: solo tus decisiones te llevaran a la victoria, debilita al rival
                con nada mas que la coherencia, presta atención a que NECESITAS decir y que
                no, ahi esta la clave de tu victoria.]

                [CAMINO B: supera 5 BATALLAS donde tu vida se pondrán en juego.
                           CONTROLES: 1 - ATACAS por 25 de daño. (ganás 25 maná)
                                      2 - Te CURÁS por 25 de vida,
                                          no pierdes tu turno. (pierdes 25 maná)
                                      3 - ATAQUE ESPECIAL por 50 de daño.
                                          (pierdes 50 maná)]

                [CAMINO C: consiste en dos "mini-juegos", el primero es una trivia donde se
                pone en juego tu vida, mientras que el segundo es una apuesta de dados con
                otro jugador, en donde se tiran hasta 3 veces el dado para conseguir el nú-
                -mero mas alto posible.]

                [CAMINO D: una simple calculadora donde ingresas dos números y devuelve las
                siguientes operaciones: + / - / *.]

            (___       _       _       _       _       _       _       _       _       ___)
                (__  _) ( __ _) (__  _) (__ _ ) `-._.-' ( _ __) (_  __) (_ __ ) (_  __)
                ( _ __) (_  __) (__ __) `-._.-'         `-._.-' (__ __) (__  _) (__ _ )
                (__  _) (_ _ _) `-._.-'                         `-._.-' (_ _ _) (_  __)
                (_ ___) `-._.-'                                         `-._.-' (___ _)
                `-._.-'                                                         `-._.-'


              """)
        print()
        volver = input("Presione cualquier tecla luego enter cuando quiera regresar al menu.")
        if volver:
            menu_español()
    elif option == "3":
        language_menu()
    elif option == "4":
        sys.exit("Hasta la próximaaaa")

def path_a_english():
    print()
    print("""
             A warrior path is not easy, make sure to not make ANY mistakes.
             Your own life is at stake, give everything fro victort.

          """)
    continuar = input("/     [1] CONTINUE     /     [2] QUIT    /")
    if continuar not in ["1", "2"]:
        while True:
            try:
                continuar = input("/     [1] CONTINUE     /     [2] QUIT    /")
                if continuar in ["1","2"]:
                    break
            except:
                pass
    if continuar == "1":
        print()
        print("""
                Your first enemy, well, maybe you don't have to think of him like that but anyways.
                Remember that your words are your most efficient weapon here

              """)
        print()
        print("""
                 Morning, welcome to hell.
                 ¿Why are you here?
                 I feel the moral obligation to remind you, your answers may or may not affect your mortal life.
                      /
                     /
            )            (
           /(   (\___/)  )
          ( #)  \ ('')| ( #
           ||___c\  > '__||
           ||**** ),_/ **'|
     .__   |'* ___| |___*'|
      \_\  |' (    ~   ,)'|
       ((  |' /(.  '  .)\ |
        \\_|_/ <_ _____> \______________
         /   '-, \   / ,-'      ______
        /      (//   \\)     __/     /
                            './_____/

              """)
        opcion0 = input("/     [1] Know more about the place.     /     [2] ¡RUTHLESS ATACK!    /     [3] Honestly, no idea.     /     [4] Mercy, i ask for mercy.    /")
        if opcion0 not in ["1", "2", "3", "4"]:
            while True:
                try:
                    opcion0 = input("/     [1] Know more about the place.     /     [2] ¡RUTHLESS ATACK!    /     [3] Honestly, no idea.     /     [4] Mercy, i ask for mercy.    /")
                    if opcion0 in ["1", "2", "3", "4"]:
                        break
                except:
                    pass
        if opcion0 =="2" or opcion0 == "4":
                path_a_mistaken()

        if opcion0 == "1" or opcion0 == "3":
            print()
            print("""
                 Oh, so nobody explain your situation to you. I apologize again but this is a really busy place so bear with me for a second.
                 Currently you are in hell, i must say that human vision of hell is a bit... well... fuzzy...
                 Your option are clear, preserv your human life or live here, free of ANY NEEDS.
                      /
                     /
            )            (
           /(   (\___/)  )
          ( #)  \ ('')| ( #
           ||___c\  > '__||
           ||**** ),_/ **'|
     .__   |'* ___| |___*'|
      \_\  |' (    ~   ,)'|
       ((  |' /(.  '  .)\ |
        \\_|_/ <_ _____> \______________
         /   '-, \   / ,-'      ______
        /      (//   \\)     __/     /
                            './_____/

                  """)
            opcion1 = input("/     [1] I NEED to know how to get out here.     /     [2] As if we could free ourselfs from desire just like that...    /     [3] Fuzzy?     /     [4] Sneaky atack.    /")
            if opcion1 not in ["1", "2", "3", "4"]:
                while True:
                    try:
                        opcion1 = input("/     [1] I NEED to know how to get out here.     /     [2] As if we could free ourselfs from desire just like that...    /     [3] Fuzzy?     /     [4] Sneaky atack.    /")
                        if opcion1 in ["1", "2", "3", "4"]:
                            break
                    except:
                        pass
            if opcion1 == "2" or opcion1 == "3":
                print()
                print("""

                 At some point in time, humans decided that hell was a living nightmare,
                 when in reality is the only place where you can live free of any kind of prison.
                 So before you leave, tell me ¿How much time do you NEED to understand what happened here?
                      /
                     /
            )            (
           /(   (\___/)  )
          ( #)  \ ('')| ( #
           ||___c\  > '__||
           ||**** ),_/ **'|
     .__   |'* ___| |___*'|
      \_\  |' (    ~   ,)'|
       ((  |' /(.  '  .)\ |
        \\_|_/ <_ _____> \______________
         /   '-, \   / ,-'      ______
        /      (//   \\)     __/     /
                            './_____/


                      """)
            elif opcion1 == "1" or opcion1 == "4":
                path_a_mistaken0()
            opcion2 = input("/     [1] I'll like to stay and think about it, i NEED time.     /     [2] Im good, don't NEED anything.    /     [3] KILL!     /     [4] Honestly, i NEED a few minutes.    /")
            if opcion2 not in ["1", "2", "3", "4"]:
                while True:
                    try:
                        opcion2 = input("/     [1] I'll like to stay and think about it, i NEED time.     /     [2] Im good, don't NEED anything.    /     [3] KILL!     /     [4] Honestly, i NEED a few minutes.    /")
                        if opcion2 in ["1", "2", "3", "4"]:
                            break
                    except:
                        pass
            if opcion2 == "2" or opcion2 == "3":
                print()
                print("CONGRATS! PATH A IS DONE!")
                print()
                print("""

                                                                        ___
                                             ___..--'  .`.
                                    ___...--'     -  .` `.`.
                           ___...--' _      -  _   .` -   `.`.
                  ___...--'  -       _   -       .`  `. - _ `.`.
           __..--'_______________ -         _  .`  _   `.   - `.`.
        .`    _ /\    -        .`      _     .`__________`. _  -`.`.
      .` -   _ /  \_     -   .`  _         .` |HELL's EXIT|`.   - `.`.
    .`-    _  /   /\   -   .`        _   .`   |___________|  `. _   `.`.
  .`________ /__ /_ \____.`____________.`     ___       ___  - `._____`|
    |   -  __  -|    | - |  ____  |   | | _  |   |  _  |   |  _ |
    | _   |  |  | -  |   | |.--.| |___| |    |___|     |___|    |
    |     |--|  |    | _ | |'--'| |---| |   _|---|     |---|_   |
    |   - |__| _|  - |   | |.--.| |   | |    |   |_  _ |   |    |
 ---``--._      |    |   |=|'--'|=|___|=|====|___|=====|___|====|
 -- . ''  ``--._| _  |  -|_|.--.|_______|_______________________|
`--._           '--- |_  |:|'--'|:::::::|:::::::::::::::::::::::|
_____`--._ ''      . '---'``--._|:::::::|:::::::::::::::::::::::|
----------`--._          ''      ``--.._|:::::::::::::::::::::::|
`--._ _________`--._'        --     .   ''-----.................|'
     `--._----------`--._.  _           -- . :''           -    ''
          `--._ _________`--._ :'              -- . :''      -- . ''
 -- . ''       `--._ ---------`--._   -- . :''
          :'        `--._ _________`--._:'  -- . ''      -- . ''
  -- . ''     -- . ''    `--._----------`--._      -- . ''     -- . ''
                              `--._ _________`--._
 -- . ''           :'              `--._ ---------`--._-- . ''    -- . ''
          -- . ''       -- . ''         `--._ _________`--._   -- . ''
:'                 -- . ''          -- . ''  `--._----------`--._

                      """)
                menu_ingles()


            elif opcion2 == "1" or opcion2 == "4":
                path_a_mistaken0()()

    elif continuar == "2":
        menu_ingles()

def path_a_mistaken():
    print()
    print("""

                     *
                     *
          (\___/)     (
          \ (- -)     )\ *      Warning shot, next time you are done.
          c\   >'    ( #       /
            )-_/      '       /
     _______| |__    ,|//
    # ___ `  ~   )  ( /
    \,|  | . ' .) \ /#
   _( /  )   , / \ / |
    //  ;;,,;,;   \,/
     _,#;,;;,;,
    /,i;;;,,;#,;
   ((  %;;,;,;;,;
    ))  ;#;,;%;;,,
  _//    ;,;; ,#;,
 /_)     #,;  //
        //    \|_
        \|_    |#
         |#\    -"
   -"


                  """)
    path_a_english()

def path_a_mistaken0():
    print()
    print("""

                                     .""--..__
                     _                     []       ``-.._
                  .'` `'.                  ||__           `-._
                 /    ,-.\                 ||_ ```---..__     `-.
                /    /:::\\               /|//}          ``--._  `.
                |    |:::||              |////}                `-.
                |    |:::||             //'///                    `.
                |    |:::||            //  ||'                      `|
                /    |:::|/        _,-//\  ||
               /`    |:::|`-,__,-'`  |/  \ ||
             /`  |   |'' ||           \   |||
           /`    \   |   ||            |  /||
         |`       |  |   |)            \ | ||
        |          \ |   /      ,.__    \| ||         ------------- Your own decisions ended with your life.
        /           `         /`    `\   | ||
       |                     /        \  / ||
       |                     |        | /  ||
       /         /           |        `(   ||
      /          .           /          )  ||
     |            \          |     ________||
    /             |          /     `-------.|
   |\            /          |              ||
   \/`-._       |           /              ||
    //   `.    /`           |              ||
   //`.    `. |             \              ||
  ///\ `-._  )/             |              ||
 //// )   .(/               |              ||
 ||||   ,'` )               /              //
 ||||  /                    /             ||
 `\\` /`                    |             //
     |`                     \            ||
    /                        |           //
  /`                          \         //
/`                            |        ||
`-.___,-.      .-.        ___,'        (/
         `---'`   `'----'`

              """)
    menu_ingles()
#CAMINO A ENTERO
def path_a():
    print()
    print("""
             El camino de un guerrero no es fácil, asegurate de no cometer errores.
             Tus propias decisiones te van a llevar por este recorrido, se fuerte.
             La buena noticia es que la victoria está en tus manos, la mala, quizas
             no vuelvas con vida.

          """)
    continuar = input("/     [1] PARA CONTINUAR     /     [2] PARA SALIR DEL JUEGO    /")
    if continuar not in ["1", "2"]:
        while True:
            try:
                continuar = input("/     [1] PARA CONTINUAR     /     [2] PARA SALIR DEL JUEGO    /")
                if continuar in ["1","2"]:
                    break
            except:
                pass
    if continuar == "1":
        print()
        print("""
                Tu primer enemigo, o quizas no tenes porque verlos de esa forma, bueno, sin vueltas.
                Recorda que tus decisiones son tus armas, suerte y segui luchando.

              """)
        print()
        print("""
                 Buenos días, bienvenido al infierno.
                 ¿Cuales son sus intenciones?
                 Siento la necesidad de recordarte que tus decisiones van a afectar directamente tu vida mortal, pido disculpas si es un inconveniente.
                      /
                     /
            )            (
           /(   (\___/)  )
          ( #)  \ ('')| ( #
           ||___c\  > '__||
           ||**** ),_/ **'|
     .__   |'* ___| |___*'|
      \_\  |' (    ~   ,)'|
       ((  |' /(.  '  .)\ |
        \\_|_/ <_ _____> \______________
         /   '-, \   / ,-'      ______
        /      (//   \\)     __/     /
                            './_____/

              """)
        opcion0 = input("/     [1] Conocer mas sobre este lugar.     /     [2] ¡ATACAR SIN PIEDAD!    /     [3] Honestamente, no se que hago acá.     /     [4] Piedad, pido piedad.    /")
        if opcion0 not in ["1", "2", "3", "4"]:
            while True:
                try:
                    opcion0 = input("/     [1] Conocer mas sobre este lugar.     /     [2] ¡ATACAR SIN PIEDAD!    /     [3] Honestamente, no se que hago acá.     /     [4] Piedad, pido piedad.    /")
                    if opcion0 in ["1", "2", "3", "4"]:
                        break
                except:
                    pass
        if opcion0 =="2" or opcion0 == "4":
                path_a_equivocado()

        if opcion0 == "1" or opcion0 == "3":
            print()
            print("""
                 Parece que nadie le explico su situacion, suele pasar. Me disculpo nuevamente pero entienda que este es un lugar muy concurrido.
                 Actualmente se encuentra en lo que ustedes conocen como el infierno, no está demás aclarar que su visión del lugar está bastante... ofuscada...
                 Sus opciones son claras, conservar su vida mortal o existir solamente en un mundo libre de NECESIDADES.
                      /
                     /
            )            (
           /(   (\___/)  )
          ( #)  \ ('')| ( #
           ||___c\  > '__||
           ||**** ),_/ **'|
     .__   |'* ___| |___*'|
      \_\  |' (    ~   ,)'|
       ((  |' /(.  '  .)\ |
        \\_|_/ <_ _____> \______________
         /   '-, \   / ,-'      ______
        /      (//   \\)     __/     /
                            './_____/

                  """)
            opcion1 = input("/     [1] Entiendo, necesito saber como salir de acá.     /     [2] Los mortales no nos libramos de las necesidades así como así    /     [3] ¿Ofuscada?     /     [4] Ataque sigiloso.    /")
            if opcion1 not in ["1", "2", "3", "4"]:
                while True:
                    try:
                        opcion1 = input("[1] Entiendo, necesito saber como salir de acá.     /     [2] Los mortales no nos libramos de las necesidades así como así    /     [3] ¿Ofuscada?     /     [4] Ataque sigiloso.    /")
                        if opcion1 in ["1", "2", "3", "4"]:
                            break
                    except:
                        pass
            if opcion1 == "2" or opcion1 == "3":
                print()
                print("""

                 No creas que es así, el problema con los mortales es que ustedes mismos son sus propios inhibidores, de otra forma no conocerían límites.
                 En algun punto de su corta historia, decidieron que el infierno era un lugar de castigos cuando la realidad es que, simplemente, es un mundo libre de sus carceles morales.
                 Antes que terminemos, digame algo ¿Cuanto tiempo necesitaría para entender lo que pasó acá?
                      /
                     /
            )            (
           /(   (\___/)  )
          ( #)  \ ('')| ( #
           ||___c\  > '__||
           ||**** ),_/ **'|
     .__   |'* ___| |___*'|
      \_\  |' (    ~   ,)'|
       ((  |' /(.  '  .)\ |
        \\_|_/ <_ _____> \______________
         /   '-, \   / ,-'      ______
        /      (//   \\)     __/     /
                            './_____/


                      """)
            elif opcion1 == "1" or opcion1 == "4":
                path_a_equivocado0()
            opcion2 = input("/     [1] Me gustaría quedarme necesito procesarlo bien.     /     [2] No necesito ningun tiempo.    /     [3] ¡REMATAR!     /     [4] Honestamente, necesito algunos minutos.    /")
            if opcion2 not in ["1", "2", "3", "4"]:
                while True:
                    try:
                        opcion2 = input("/     [1] Me gustaría quedarme hasta procesarlo bien.     /     [2] No necesito ningun tiempo.    /     [3] ¡REMATAR!     /     [4] Honestamente, necesito algunos minutos.    /")
                        if opcion2 in ["1", "2", "3", "4"]:
                            break
                    except:
                        pass
            if opcion2 == "2" or opcion2 == "3":
                print()
                print("FELICIDADES, LOGRASTE SUPERAR EL PRIMER CAMINO")
                print()
                print("""

                                                                        ___
                                             ___..--'  .`.
                                    ___...--'     -  .` `.`.
                           ___...--' _      -  _   .` -   `.`.
                  ___...--'  -       _   -       .`  `. - _ `.`.
           __..--'_______________ -         _  .`  _   `.   - `.`.
        .`    _ /\    -        .`      _     .`__________`. _  -`.`.
      .` -   _ /  \_     -   .`  _         .` |HELL's EXIT|`.   - `.`.
    .`-    _  /   /\   -   .`        _   .`   |___________|  `. _   `.`.
  .`________ /__ /_ \____.`____________.`     ___       ___  - `._____`|
    |   -  __  -|    | - |  ____  |   | | _  |   |  _  |   |  _ |
    | _   |  |  | -  |   | |.--.| |___| |    |___|     |___|    |
    |     |--|  |    | _ | |'--'| |---| |   _|---|     |---|_   |
    |   - |__| _|  - |   | |.--.| |   | |    |   |_  _ |   |    |
 ---``--._      |    |   |=|'--'|=|___|=|====|___|=====|___|====|
 -- . ''  ``--._| _  |  -|_|.--.|_______|_______________________|
`--._           '--- |_  |:|'--'|:::::::|:::::::::::::::::::::::|
_____`--._ ''      . '---'``--._|:::::::|:::::::::::::::::::::::|
----------`--._          ''      ``--.._|:::::::::::::::::::::::|
`--._ _________`--._'        --     .   ''-----.................|'
     `--._----------`--._.  _           -- . :''           -    ''
          `--._ _________`--._ :'              -- . :''      -- . ''
 -- . ''       `--._ ---------`--._   -- . :''
          :'        `--._ _________`--._:'  -- . ''      -- . ''
  -- . ''     -- . ''    `--._----------`--._      -- . ''     -- . ''
                              `--._ _________`--._
 -- . ''           :'              `--._ ---------`--._-- . ''    -- . ''
          -- . ''       -- . ''         `--._ _________`--._   -- . ''
:'                 -- . ''          -- . ''  `--._----------`--._

                      """)


            elif opcion2 == "1" or opcion2 == "4":
                path_a_equivocado0()

    elif continuar == "2":
        menu_español()

def path_a_equivocado():
    print()
    print("""

                     *
                     *
          (\___/)     (
          \ (- -)     )\ *      Esta vez es una advertencia, la próxima no lo será.
          c\   >'    ( #       /
            )-_/      '       /
     _______| |__    ,|//
    # ___ `  ~   )  ( /
    \,|  | . ' .) \ /#
   _( /  )   , / \ / |
    //  ;;,,;,;   \,/
     _,#;,;;,;,
    /,i;;;,,;#,;
   ((  %;;,;,;;,;
    ))  ;#;,;%;;,,
  _//    ;,;; ,#;,
 /_)     #,;  //
        //    \|_
        \|_    |#
         |#\    -"
   -"


                  """)
    path_a()

def path_a_equivocado0():
    print()
    print("""

                                     .""--..__
                     _                     []       ``-.._
                  .'` `'.                  ||__           `-._
                 /    ,-.\                 ||_ ```---..__     `-.
                /    /:::\\               /|//}          ``--._  `.
                |    |:::||              |////}                `-.
                |    |:::||             //'///                    `.
                |    |:::||            //  ||'                      `|
                /    |:::|/        _,-//\  ||
               /`    |:::|`-,__,-'`  |/  \ ||
             /`  |   |'' ||           \   |||
           /`    \   |   ||            |  /||
         |`       |  |   |)            \ | ||
        |          \ |   /      ,.__    \| ||         ------------- Parece que tus propias decisiones terminaron con tu vida, quiza en la próxima.
        /           `         /`    `\   | ||
       |                     /        \  / ||
       |                     |        | /  ||
       /         /           |        `(   ||
      /          .           /          )  ||
     |            \          |     ________||
    /             |          /     `-------.|
   |\            /          |              ||
   \/`-._       |           /              ||
    //   `.    /`           |              ||
   //`.    `. |             \              ||
  ///\ `-._  )/             |              ||
 //// )   .(/               |              ||
 ||||   ,'` )               /              //
 ||||  /                    /             ||
 `\\` /`                    |             //
     |`                     \            ||
    /                        |           //
  /`                          \         //
/`                            |        ||
`-.___,-.      .-.        ___,'        (/
         `---'`   `'----'`

              """)
    menu_español()

def path_b_english():

    def image_phx():
        print("""

            -----------Nabis-----------

           _..--""---.
          /           ".
          `            l
          |'._  ,._ l/".
          |  _J<__/.v._/
           \( ,~._,,,,-)
            `-\' \`,,j|
               \_,____J
          .--.__)--(__.--.
         /  `-----..--'. j
         '.- '`--` `--' \\
        //  '`---'`  `-' \\
       //   '`----'`.-.-' \\
     _//     `--- -'   \' | \________
    |  |         ) (      `.__.---- -'.
     \7          \`-(               74\\.
     ||       _  /`-(               l|//7__
     |l    ('  `-)-/_.--.          f''` -.-"|
     |\     l\_  `-'    .'         |     |  |
     llJ   _ _)J--._.-('           |     |  l
     |||( ( '_)_  .l   ". _    ..__I     |  L
     ^\\\||`'   "   '"-. " )''`'---'     L.-'`-.._
          \ |           ) /.              ``'`-.._``-.
          l l          / / |                      |''|
           " \        / /   "-..__                |  |
           | |       / /          1       ,- t-...J_.'
           | |      / /           |       |  |
           J  \  /"  (            l       |  |
           | ().'`-()/            |       |  |
          _.-"_.____/             l       l.-l
      _.-"_.+"|                  /        \.  .
/"\.-"_.-"  | |                 /          \   .
\_   "      | |                1            | `'|
  |ll       | |                |            i   |
  \\\       |-\               \j ..          L,,'. `/
 __\\\     ( .-\           .--'    ``--../..'      '-..
   `'''`----`\\\\ .....--'''
              \\\\

            """)
    def image_devil0():
        print("""

                  ----------Dante----------

                               ,-.
       ___,---.__          /'|`\          __,---,___
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
  ,'        |           ~'\     /`~           |        `.
 /      ___//              `. ,'          ,  , \___      .
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |
|   /          /\_  `   .    |    ,      _/\          \   |
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /
 \  \           | `._   `\\  |  //'   _,' |           /  /
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
     ``       /     \    ,='/ \`=.    /     \       ''
             |__   /|\_,--.,-.--,--._/|\   __|
             /  `./  \\`\ |  |  | /,//' \,'  .
            /   /     ||--+--|--+-/-|     \   .
           |   |     /'\_\_\ | /_/_/`\     |   |
            \   \__, \_     `~'     _/ .__/   /
             `-._,-'   `-._______,-'   `-._,-'

            """)


    def image_egypt():
        print("""

                  ---------NEFERTITT PHENOMENON----------


     .--._       ||                      .----.    ||
           /     `.     ||                    .'      \   ||
          |       |     ||                    )o>   )  |  ||
          / (   o/      ||                   /_.      /   ||
        .' \    _\      ||                     \-'   |    ||
      .'    `._'        ||                      `.    \   ||
    .'        -.        ||                      .'     '. ||
   /     |     |        ||                     /   /  | | ||
  /    .'      /       .''.                   .    |  | |.''.
 |  |  |      |    .-==:==:======:============|    |  | |:==:=
 |  |  |  .--.-.  /_/  '..'     _|_           |   /   ) |'..'
 |  |  `.'   | |        ||     /.-.\          |  /  .'  | ||
 |  \    `.  / |`-._    ||     \   /          |.'  /    | ||
 |   `-._   `-.|._  `-. ||      |-|`.       .-'  .'     | ||
 |       /`-.  `::.____`...____(.-') `..---' _.-'       \ ||
 |      |    `-.._.--._''''----`| |  '-._-.'. (_________.|||
 |      |   |  |        ||      | |`. _.' .' .'----------|||
 |      |  / \ |        ||      \ /  -_.-` .' .'         |||
 |      | |  | |        ||       |       .' .'          / ||
 \      | './  '._     .--.______'_____ : .'    _......_  ||..
  `.__.(    `-._--`.-_(_________________ :    -'         `-'  `.
        `'-''---` /_/                    `:.______...------- `..>

            """)

    def image_skeleton0():
        print("""
                    ----------NABIS 2.0----------

                              _.--""-._
  .                         ."         ".
 / \    ,^.         /(     Y             |      ).
/   `---. |--'\    (  \__..'--   -   -- -'""-.-'  )
|        :|    `>   '.     l_..-------.._l      .'
|      __l;__ .'      "-.__.||_.-'v'-._||`"----"
 \  .-' | |  `              l._       _.'
  \/    | |                   l`^^'^^'j
        | |                _   \_____/     _
        j |               l `--__)-'(__.--' |
        | |               | /`---``-----'"1 |  ,-----.
        | |               )/  `--' '---'   \'-'  ___  `-.
        | |              //  `-'  '`----'  /  ,-'   I`.  .
      _ L |_            //  `-.-.'`-----' /  /  |   |  `. .
     '._' / \         _/(   `/   )- ---' ;  /__.J   L.__.\ :
      `._;/7(-.......'  /        ) (     |  |            | |
      `._;l _'--------_/        )-'/     :  |___.    _._./ ;
        | |                 .__ )-'\  __  \  \  I   1   / /
        `-'                /   `-\-(-'   \ \  `.|   | ,' /
                           \__  `-'    __/  `-. `---'',-'
                              )-._.-- (        `-----'
                             )(  l\ o ('..-.
                       _..--' _'-' '--'.-. |
                __,,-'' _,,-''            \ .
               f'. _,,-'                   \ .
              ()--  |                       \ .
                \.  |                       /  .
                  \ \                      |._  |
                   \ \                     |  ()|
                    \ \                     \  /
                     ) `-.                   | |
                    // .__)                  | |
                 _.//7'                      | |
               '---'                         j_| `
                                            (| |
                                             |  .
                                             |lllj
                                             |||||



            """)

    def double_enemy():
        print("""

                          ----------LION TWINS----------

                             /|
                                     |\|
                                     |||
                                     |||
                                     |||
                                     |||
                                     |||
                                     |||
                                  ~-[ o ]-~
                                     |/|
                                     |/|
             ///~`     |\\_          `0'         =\\\\         . .
            ,  |='  ,))\_| ~-_                    _)  \      _/_/|
           / ,' ,;((((((    ~ \                  `~~~\-~-_ /~ (_/-
         /' -~/~)))))))'\_   _/'                      \_  /'  D   |
        (       (((((( ~-/ ~-/                          ~-;  /    \--_
         ~~--|   ))''    ')  `                            `~~\_    \   )
             :        (_  ~\           ,                    /~~-     ./
              \        \_   )--__  /(_/)                   |    )    )|
    ___       |_     \__/~-__    ~~   ,'      /,_;,   __--(   _/      |
  //~~\`\    /' ~~~----|     ~~~~~~~~'        \-  ((~~    __-~        |
((()   `\`\_(_     _-~~-\                      ``~~ ~~~~~~   \_      /
 )))     ~----'   /      \                                   )       )
  (         ;`~--'        :                                _-    ,;;(
            |    `\       |                             _-~    ,;;;;)
            |    /'`\     ;                          _-~          _/
           /~   /    |    )                         /;;;''  ,;;:-~
          |    /     / | /                         |;;'   ,''
          /   /     |  \\|                         |   ,;(    -Tua Xiong
        _/  /'       \  \_)                   .---__\_    \,--._______
       ( )|'         (~-_|                   (;;'  ;;;~~~/' `;;|  `;;;|
        ) `\_         |-_;;--__               ~~~----__/'    /'_______|
        `----'       (   `~--_ ~~~;;------------~~~~~ ;;;'_/'
            """)

    def death_image():
        print()
        print("""

                                        .""--..__
                     _                     []       ``-.._
                  .'` `'.                  ||__           `-._
                 /    ,-.\                 ||_ ```---..__     `-.
                /    /:::\\               /|//}          ``--._  `.
                |    |:::||              |////}                `-. .
                |    |:::||             //'///                    `..
                |    |:::||            //  ||'                      `|
                /    |:::|/        _,-//\  ||
               /`    |:::|`-,__,-'`  |/  \ ||
             /`  |   |'' ||           \   |||
           /`    \   |   ||            |  /||
         |`       |  |   |)            \ | ||
        |          \ |   /      ,.__    \| ||
        /           `         /`    `\   | ||
       |                     /        \  / ||                  YOU DIED
                                                               YOU DIED
       |                     |        | /  ||                  YOU DIED
       /         /           |        `(   ||                  YOU DIED

      /          .           /          )  ||
     |            \          |     ________||
    /             |          /     `-------.|
   |\            /          |              ||
   \/`-._       |           /              ||
    //   `.    /`           |              ||
   //`.    `. |             \              ||
  ///\ `-._  )/             |              ||
 //// )   .(/               |              ||
 ||||   ,'` )               /              //
 ||||  /                    /             ||
 `\\` /`                    |             //
     |`                     \            ||
    /                        |           //
  /`                          \         //
/`                            |        ||
`-.___,-.      .-.        ___,'        (/
         `---'`   `'----'`


            """)
        menu_ingles()
    def claim_head(hp_foe, win_condition):
        if hp_foe == 0:
            return win_condition + 1
    def special_hit(hp_foe):
        return hp_foe - 50
    def heal(hp_player, mana):
        if mana >= 25:
            return hp_player + 25, mana - 25
    def hit(hp_foe, mana):
        return hp_foe - 25, mana +  25
    def foe_hit(hp_player):
        return hp_player - 25
    def fight_simulation(hp_player,hp_foe,mana,win_condition):
        while True:
            try:
                hit_test = input("/     [1] HIT  (DMG=25)  /     [2] HEAL (HP +25 MANA -25)   /     [3]  SPECIAL HIT (50 MANA)   /")
                if hit_test == "1":
                    hp_player = foe_hit(hp_player)
                    hp_foe, mana = hit(hp_foe, mana)
                    print()
                    print()
                    print (f"ENEMY HP:{hp_foe}----MANA:{mana}----YOUR HP:{hp_player}")
                    print()
                    print()
                elif hit_test == "2":
                    if mana >= 25:
                        hp_player, mana = heal(hp_player, mana)
                        print()
                        print()
                        print(f"YOUR HP:{hp_player}----MANA:{mana}")
                        print()
                        print()
                    else:
                        print()
                        print()
                        print("Not enough mana!")
                        print()
                        print()
                elif hit_test == "3":
                    if mana > 49:
                        hp_foe = special_hit(hp_foe)
                        mana = mana - 50
                        print()
                        print()
                        print(f"ENEMY HP:{hp_foe}----MANA:{mana}")
                        print()
                        print()
                    else:
                        print()
                        print()
                        print("NOT ENOUGH MANA!")
                        print()
                        print()
                if hp_foe <= 0 and hp_player > 0:
                    foe_death_choice = input("/     [1] CLAIM HEAD")
                    if foe_death_choice == "1":
                        win_condition = claim_head(hp_foe, win_condition)
                        print()
                        print()
                        print("CONGRATULATIONS, KEEP FIGHTING!")
                        print()
                        print()
                        if win_condition and hp_player > 0:
                            return win_condition, hp_player
                if hp_player <= 0 or hp_foe <= 0:
                    break
            except:
                pass

    def stage0():
        hp_player = 100
        hp_foe = 100
        mana = 0
        win_condition = 0
        double_enemy()
        try:
            win_condition, hp_player = fight_simulation(hp_player,hp_foe,mana,win_condition)
            if win_condition and hp_player > 0:
                return (win_condition, hp_player)
        except:
            sys.exit(death_image())

    def stage1():
        hp_player = 100
        hp_foe = 200
        mana = 15
        win_condition = 0
        image_skeleton0()
        try:
            win_condition, hp_player = fight_simulation(hp_player,hp_foe,mana,win_condition)
            if win_condition and hp_player > 0:
                return (win_condition, hp_player)
        except:
            sys.exit(death_image())

    def stage2():
        hp_player = 100
        hp_foe = 350
        mana = 25
        win_condition = 0
        image_egypt()
        try:
            win_condition, hp_player = fight_simulation(hp_player,hp_foe,mana,win_condition)
            if win_condition and hp_player > 0:
                return (win_condition, hp_player)
        except:
            sys.exit(death_image())

    def stage3():
        hp_player = 115
        hp_foe = 500
        mana = 50
        win_condition = 0
        image_devil0()
        try:
            win_condition, hp_player = fight_simulation(hp_player,hp_foe,mana,win_condition)
            if win_condition and hp_player > 0:
                return (win_condition, hp_player)
        except:
            sys.exit(death_image())

    def stage4():
        hp_player = 130
        hp_foe = 700
        mana = 75
        win_condition = 0
        image_phx()
        try:
            win_condition, hp_player = fight_simulation(hp_player,hp_foe,mana,win_condition)
            if win_condition and hp_player > 0:
                return (win_condition, hp_player)
        except:
            sys.exit(death_image())
    stage0()
    stage1()
    stage2()
    stage3()
    stage4()


def path_b():
    def image_phx():
        print("""

            -----------Nabis-----------

           _..--""---.
          /           ".
          `            l
          |'._  ,._ l/".
          |  _J<__/.v._/
           \( ,~._,,,,-)
            `-\' \`,,j|
               \_,____J
          .--.__)--(__.--.
         /  `-----..--'. j
         '.- '`--` `--' \\
        //  '`---'`  `-' \\
       //   '`----'`.-.-' \\
     _//     `--- -'   \' | \________
    |  |         ) (      `.__.---- -'.
     \7          \`-(               74\\.
     ||       _  /`-(               l|//7__
     |l    ('  `-)-/_.--.          f''` -.-"|
     |\     l\_  `-'    .'         |     |  |
     llJ   _ _)J--._.-('           |     |  l
     |||( ( '_)_  .l   ". _    ..__I     |  L
     ^\\\||`'   "   '"-. " )''`'---'     L.-'`-.._
          \ |           ) /.              ``'`-.._``-.
          l l          / / |                      |''|
           " \        / /   "-..__                |  |
           | |       / /          1       ,- t-...J_.'
           | |      / /           |       |  |
           J  \  /"  (            l       |  |
           | ().'`-()/            |       |  |
          _.-"_.____/             l       l.-l
      _.-"_.+"|                  /        \.  .
/"\.-"_.-"  | |                 /          \   .
\_   "      | |                1            | `'|
  |ll       | |                |            i   |
  \\\       |-\               \j ..          L,,'. `/
 __\\\     ( .-\           .--'    ``--../..'      '-..
   `'''`----`\\\\ .....--'''
              \\\\

            """)
    def image_devil0():
        print("""

                  ----------Dante----------

                               ,-.
       ___,---.__          /'|`\          __,---,___
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
  ,'        |           ~'\     /`~           |        `.
 /      ___//              `. ,'          ,  , \___      .
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |
|   /          /\_  `   .    |    ,      _/\          \   |
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /
 \  \           | `._   `\\  |  //'   _,' |           /  /
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
     ``       /     \    ,='/ \`=.    /     \       ''
             |__   /|\_,--.,-.--,--._/|\   __|
             /  `./  \\`\ |  |  | /,//' \,'  .
            /   /     ||--+--|--+-/-|     \   .
           |   |     /'\_\_\ | /_/_/`\     |   |
            \   \__, \_     `~'     _/ .__/   /
             `-._,-'   `-._______,-'   `-._,-'

            """)


    def image_egypt():
        print("""

                  ---------NEFERTITT PHENOMENON----------


     .--._       ||                      .----.    ||
           /     `.     ||                    .'      \   ||
          |       |     ||                    )o>   )  |  ||
          / (   o/      ||                   /_.      /   ||
        .' \    _\      ||                     \-'   |    ||
      .'    `._'        ||                      `.    \   ||
    .'        -.        ||                      .'     '. ||
   /     |     |        ||                     /   /  | | ||
  /    .'      /       .''.                   .    |  | |.''.
 |  |  |      |    .-==:==:======:============|    |  | |:==:=
 |  |  |  .--.-.  /_/  '..'     _|_           |   /   ) |'..'
 |  |  `.'   | |        ||     /.-.\          |  /  .'  | ||
 |  \    `.  / |`-._    ||     \   /          |.'  /    | ||
 |   `-._   `-.|._  `-. ||      |-|`.       .-'  .'     | ||
 |       /`-.  `::.____`...____(.-') `..---' _.-'       \ ||
 |      |    `-.._.--._''''----`| |  '-._-.'. (_________.|||
 |      |   |  |        ||      | |`. _.' .' .'----------|||
 |      |  / \ |        ||      \ /  -_.-` .' .'         |||
 |      | |  | |        ||       |       .' .'          / ||
 \      | './  '._     .--.______'_____ : .'    _......_  ||..
  `.__.(    `-._--`.-_(_________________ :    -'         `-'  `.
        `'-''---` /_/                    `:.______...------- `..>

            """)

    def image_skeleton0():
        print("""
                    ----------NABIS 2.0----------

                              _.--""-._
  .                         ."         ".
 / \    ,^.         /(     Y             |      ).
/   `---. |--'\    (  \__..'--   -   -- -'""-.-'  )
|        :|    `>   '.     l_..-------.._l      .'
|      __l;__ .'      "-.__.||_.-'v'-._||`"----"
 \  .-' | |  `              l._       _.'
  \/    | |                   l`^^'^^'j
        | |                _   \_____/     _
        j |               l `--__)-'(__.--' |
        | |               | /`---``-----'"1 |  ,-----.
        | |               )/  `--' '---'   \'-'  ___  `-.
        | |              //  `-'  '`----'  /  ,-'   I`.  .
      _ L |_            //  `-.-.'`-----' /  /  |   |  `. .
     '._' / \         _/(   `/   )- ---' ;  /__.J   L.__.\ :
      `._;/7(-.......'  /        ) (     |  |            | |
      `._;l _'--------_/        )-'/     :  |___.    _._./ ;
        | |                 .__ )-'\  __  \  \  I   1   / /
        `-'                /   `-\-(-'   \ \  `.|   | ,' /
                           \__  `-'    __/  `-. `---'',-'
                              )-._.-- (        `-----'
                             )(  l\ o ('..-.
                       _..--' _'-' '--'.-. |
                __,,-'' _,,-''            \ .
               f'. _,,-'                   \ .
              ()--  |                       \ .
                \.  |                       /  .
                  \ \                      |._  |
                   \ \                     |  ()|
                    \ \                     \  /
                     ) `-.                   | |
                    // .__)                  | |
                 _.//7'                      | |
               '---'                         j_| `
                                            (| |
                                             |  .
                                             |lllj
                                             |||||



            """)

    def double_enemy():
        print(f"""

                          ----------LION TWINS----------

                             /|
                                     |\|
                                     |||
                                     |||
                                     |||
                                     |||
                                     |||
                                     |||
                                  ~-[ o ]-~
                                     |/|
                                     |/|
             ///~`     |\\_          `0'         =\\\\         . .
            ,  |='  ,))\_| ~-_                    _)  \      _/_/|
           / ,' ,;((((((    ~ \                  `~~~\-~-_ /~ (_/-
         /' -~/~)))))))'\_   _/'                      \_  /'  D   |
        (       (((((( ~-/ ~-/                          ~-;  /    \--_
         ~~--|   ))''    ')  `                            `~~\_    \   )
             :        (_  ~\           ,                    /~~-     ./
              \        \_   )--__  /(_/)                   |    )    )|
    ___       |_     \__/~-__    ~~   ,'      /,_;,   __--(   _/      |
  //~~\`\    /' ~~~----|     ~~~~~~~~'        \-  ((~~    __-~        |
((()   `\`\_(_     _-~~-\                      ``~~ ~~~~~~   \_      /
 )))     ~----'   /      \                                   )       )
  (         ;`~--'        :                                _-    ,;;(
            |    `\       |                             _-~    ,;;;;)
            |    /'`\     ;                          _-~          _/
           /~   /    |    )                         /;;;''  ,;;:-~
          |    /     / | /                         |;;'   ,''
          /   /     |  \\|                         |   ,;(    -Tua Xiong
        _/  /'       \  \_)                   .---__\_    \,--._______
       ( )|'         (~-_|                   (;;'  ;;;~~~/' `;;|  `;;;|
        ) `\_         |-_;;--__               ~~~----__/'    /'_______|
        `----'       (   `~--_ ~~~;;------------~~~~~ ;;;'_/'
            """)

    def death_image():
        print()
        print("""

                                        .""--..__
                     _                     []       ``-.._
                  .'` `'.                  ||__           `-._
                 /    ,-.\                 ||_ ```---..__     `-.
                /    /:::\\               /|//}          ``--._  `.
                |    |:::||              |////}                `-. .
                |    |:::||             //'///                    `..
                |    |:::||            //  ||'                      `|
                /    |:::|/        _,-//\  ||
               /`    |:::|`-,__,-'`  |/  \ ||
             /`  |   |'' ||           \   |||
           /`    \   |   ||            |  /||
         |`       |  |   |)            \ | ||
        |          \ |   /      ,.__    \| ||
        /           `         /`    `\   | ||
       |                     /        \  / ||                  YOU DIED
                                                               YOU DIED
       |                     |        | /  ||                  YOU DIED
       /         /           |        `(   ||                  YOU DIED

      /          .           /          )  ||
     |            \          |     ________||
    /             |          /     `-------.|
   |\            /          |              ||
   \/`-._       |           /              ||
    //   `.    /`           |              ||
   //`.    `. |             \              ||
  ///\ `-._  )/             |              ||
 //// )   .(/               |              ||
 ||||   ,'` )               /              //
 ||||  /                    /             ||
 `\\` /`                    |             //
     |`                     \            ||
    /                        |           //
  /`                          \         //
/`                            |        ||
`-.___,-.      .-.        ___,'        (/
         `---'`   `'----'`


            """)
    def claim_head(hp_foe, win_condition):
        if hp_foe == 0:
            return win_condition + 1
    def special_hit(hp_foe):
        return hp_foe - 50
    def heal(hp_player, mana):
        if mana >= 25:
            return hp_player + 25, mana - 25
    def hit(hp_foe, mana):
        return hp_foe - 25, mana +  25
    def foe_hit(hp_player):
        return hp_player - 25
    def fight_simulation(hp_player,hp_foe,mana,win_condition):
        while True:
            try:
                hit_test = input("/     [1] PEGAR  (DMG=25)  /     [2] CURAR (HP +25 MANA -25)   /     [3] GOLPE ESPECIAL (50 MANA)   /")
                if hit_test == "1":
                    hp_player = foe_hit(hp_player)
                    hp_foe, mana = hit(hp_foe, mana)
                    print()
                    print()
                    print (f"VIDA ENEMIGO:{hp_foe}----TU MANA:{mana}----TU VIDA:{hp_player}")
                    print()
                    print()
                elif hit_test == "2":
                    if mana >= 25:
                        hp_player, mana = heal(hp_player, mana)
                        print()
                        print()
                        print(f"TU VIDA:{hp_player}----TU MANA:{mana}")
                        print()
                        print()
                    else:
                        print()
                        print()
                        print("SIN MANA!")
                        print()
                        print()
                elif hit_test == "3":
                    if mana > 49:
                        hp_foe = special_hit(hp_foe)
                        mana = mana - 50
                        print()
                        print()
                        print(f"VIDA ENEMIGO:{hp_foe}----TU MANA:{mana}")
                        print()
                        print()
                    else:
                        print()
                        print()
                        print("SIN MANA!")
                        print()
                        print()
                if hp_foe <= 0 and hp_player > 0:
                    foe_death_choice = input("/     [1] RECLAMAR CABEZA")
                    if foe_death_choice == "1":
                        win_condition = claim_head(hp_foe, win_condition)
                        print()
                        print()
                        print("FELICITACIONES, SIGUE LUCHANDO!")
                        print()
                        print()
                        if win_condition and hp_player > 0:
                            return win_condition, hp_player
                if hp_player <= 0 or hp_foe <= 0:
                    break
            except:
                pass

    def stage0():
        hp_player = 100
        hp_foe = 100
        mana = 0
        win_condition = 0
        print(double_enemy())
        try:
            win_condition, hp_player = fight_simulation(hp_player,hp_foe,mana,win_condition)
            if win_condition and hp_player > 0:
                return (win_condition, hp_player)
        except:
            sys.exit(death_image())

    def stage1():
        hp_player = 100
        hp_foe = 200
        mana = 15
        win_condition = 0
        print(image_skeleton0())
        try:
            win_condition, hp_player = fight_simulation(hp_player,hp_foe,mana,win_condition)
            if win_condition and hp_player > 0:
                return (win_condition, hp_player)
        except:
            sys.exit(death_image())

    def stage2():
        hp_player = 100
        hp_foe = 350
        mana = 25
        win_condition = 0
        print(image_egypt())
        try:
            win_condition, hp_player = fight_simulation(hp_player,hp_foe,mana,win_condition)
            if win_condition and hp_player > 0:
                return (win_condition, hp_player)
        except:
            sys.exit(death_image())

    def stage3():
        hp_player = 115
        hp_foe = 500
        mana = 50
        win_condition = 0
        print(image_devil0())
        try:
            win_condition, hp_player = fight_simulation(hp_player,hp_foe,mana,win_condition)
            if win_condition and hp_player > 0:
                return (win_condition, hp_player)
        except:
            sys.exit(death_image())

    def stage4():
        hp_player = 130
        hp_foe = 700
        mana = 75
        win_condition = 0
        print(image_phx())
        try:
            win_condition, hp_player = fight_simulation(hp_player,hp_foe,mana,win_condition)
            if win_condition and hp_player > 0:
                return (win_condition, hp_player)
        except:
            sys.exit(death_image())
    stage0()
    stage1()
    stage2()
    stage3()
    stage4()


def path_c_english():
    menu0()
def path_c_spanish():
    menu0_spanish()

def welcome():
    name = input("Please enter your name/Por Favor, introduzca su nombre: ")
    while True:
        try:
            if not name:
                name = input("Please enter your name/Por Favor, introduzca su nombre: ")
            if name:
                break
        except:
            pass
    return name
def menu0():
    name = welcome()
    print(f"""
    .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.
    :::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::..
    '      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `

                Welcome {name}, is up to you how you wanna do this,
                so don't waste my time and just pick one.

                [1]- Talk it out
                [2]- Gamble

    .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.
    :::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::..
    '      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `

            """)
    menu_123 = input("/     [1]      /     [2]     /")
    if menu_123 not in ["1", "2"]:
        while True:
            try:
                menu_123 = input("/     [1]      /     [2]     /")
                if menu_123 in ["1", "2"]:
                    break
            except:
                pass
    if menu_123 == "1":
        print()
        print()
        print("Wish you luck, choose wisely or die.")
        talk_it_out()
    elif menu_123 == "2":
        print()
        print()
        print("Hope luck is with you.")
        ceelo()


def talk_it_out():
    mistake = 0
    print()
    print()
    print(f"""

        Satan Jr.
                              ..
                        .\   / _\   ..
                       /_ \   ||   / _.
                        ||    ||    ||
                 ; ,     \`.__||__.'/             Satan Jr:
         |\     /( ;\_.;  `./|  __.'              Let me guess, you don't have any idea why you are here.
         ' `.  _|_\/_;-'_ .' '||                  This is so boring, all the humans are the same, just
          \ _/`       `.-\_ / ||                  crying babys...
      , _ _`; ,--.   ,--. ;'_ _|,
      '`''\| /  ,-\ | _,-\ |/''`'                 Well, i got to do this anyways so let's be quick,
       \ .-- \__\_/ /` )_/ --. /                  Do you wish to continue?
       /    .         -'  .    \ -
      |     /             \     |                 ANSWERS:
   .   .  -' `-..____...-' `-  .                  [1] - For calling people out about their looks, you
.'`'.__ `._      `-..-''    _.'|                  really look like a baby.
 \ .--.`.  `-..__    _,..-'   L|
  '    \ \      _,| |,_      /_7)                 [2] - We do cry a lot, it's so annoying.
        \ \    /       \ _.-'/||
         \ \  /.'|   |`.__.'` ||                  [3] - WAIT IM I DEAD?! AND WHY ARE YOU SO CUTE??!!
          \ `//_/     \       ||                        PLEASE LET ME HUG YOU
           `/ \|       |      ||
            `"`'.  _  .'      ||                  [4] - I almost fall asleep while you were talking,
                 \ | /        ||                        please let me go back and choose another
                  |'|                                   option.
               .-.|||.-.                                (THIS IS YOUR ONLY CHANCE OF GOING BACK
              '----"----'                                BEFORE GAME STARTS)

           """)
    while True:
            try:
                choice0 = input("/     [1]      /     [2]     /     [3]      /     [4]      /")
                if choice0 in ["1", "2", "3", "4"]:
                    break
            except:
                pass
    if choice0 == "1" or choice0 == "2" or choice0 == "3":
        print()
        print()
        print(f"""

        Satan Jr.
                              ..
                        .\   / _\   ..
                       /_ \   ||   / _.
                        ||    ||    ||
                 ; ,     \`.__||__.'/             Satan Jr:
         |\     /( ;\_.;  `./|  __.'              LOL, so you are a funny one, i like those ones.
         ' `.  _|_\/_;-'_ .' '||                  That's cause i am a baby, im currently 2023 years.
          \ _/`       `.-\_ / ||                  But enough about me, let me explain something.
      , _ _`; ,--.   ,--. ;'_ _|,
      '`''\| /  ,-\ | _,-\ |/''`'                 Im something like a filter, if you don't get trough
       \ .-- \__\_/ /` )_/ --. /                  this interrogation, well...
       /    .         -'  .    \ -                So, first question. "Age" of the universe please?
      |     /             \     |                 ANSWERS:
   .   .  -' `-..____...-' `-  .                  [1] - around 8 BILLION years.
.'`'.__ `._      `-..-''    _.'|
  '    \ \      _,| |,_      /_7)                 [2] - around 14 BILLION years.
        \ \    /       \ _.-'/||
         \ \  /.'|   |`.__.'` ||                  [3] - around 54 MILLION years.
          \ `//_/     \       ||
           `/ \|       |      ||
            `"`'.  _  .'      ||
                 \ | /        ||
                  |'|
               .-.|||.-.
              '----"----'
           """)
        while True:
            try:
                choice1 = input("/     [1]      /     [2]     /     [3]      /")
                if choice1 == "2":
                    break
                elif choice1 == "3" or choice1 == "1":
                    mistake += 1
                    if mistake == 2:
                        print()
                        print("Well, that was quick. Next you'll get it right.")
                        talk_it_out()
            except:
                pass
        print()
        print()
        print(f"""


                              ..
                        .\   / _.   ..          Satan Jr.
                       /_ \   ||   / _.
                        ||    ||    ||          I mean you get used to it, at this point i might be seeing thousands
                 ; ,     \`.__||__.'/           of your kind lurking around here, but in a couple of centuries im out,
         |\     /( ;\_.;  `./|  __.'            so it's not that bad.
         ' `.  _|_\/_;-'_ .' '||
          \ _/`       `.-\_ / ||                Since we are talking about numbers, how many people lives in earth?
      , _ _`; ,--.   ,--. ;'_ _|,
      '`''\| /  ,-\ | _,-\ |/''`'               [1] - around 350 million
       \ .-- \__\_/ /` )_/ --. /
       /    .         -'  .    .                [2] - around 2 billion
      |     /             \     |
   .   .  -' `-..____...-' `-  .                [3] - around 8 billion
.'`'.__ `._      `-..-''    _.'|
 \ .--.`.  `-..__    _,..-'   L|
  '    \ \      _,| |,_      /_7)
        \ \    /       \ _.-'/||
         \ \  /.'|   |`.__.'` ||
          \ `//_/     \       ||
           `/ \|       |      ||
            `"`'.  _  .'      ||
                 \ | /        ||
                  |'|
               .-.|||.-.
              '----"----'



               """)

        while True:
            try:
                choice2 = input("/     [1]      /     [2]     /     [3]      /")
                if choice2 == "3":
                    break
                elif choice2 == "2" or choice2 == "1":
                    mistake += 1
                    if mistake == 2:
                        print()
                        print("Well, that was quick. Next you'll get it right.")
                        talk_it_out()
            except:
                pass
        print()
        print()
        print("""

                              ..
                        .\   / _.   ..          Satan Jr.
                       /_ \   ||   / _.
                        ||    ||    ||          Good job so far, now, if you get this one right the next question
                 ; ,     \`.__||__.'/           will be asked by Satan himself.
         |\     /( ;\_.;  `./|  __.'            Let's get right to it, should we?
         ' `.  _|_\/_;-'_ .' '||
          \ _/`       `.-\_ / ||                How many circles of hell did Dante described?
      , _ _`; ,--.   ,--. ;'_ _|,
      '`''\| /  ,-\ | _,-\ |/''`'               [1] - 7
       \ .-- \__\_/ /` )_/ --. /
       /    .         -'  .    .                [2] - 5
      |     /             \     |
   .   .  -' `-..____...-' `-  .                [3] - 1
.'`'.__ `._      `-..-''    _.'|
 \ .--.`.  `-..__    _,..-'   L|                [4] - 9
  '    \ \      _,| |,_      /_7)
        \ \    /       \ _.-'/||                [5] - 12
         \ \  /.'|   |`.__.'` ||
          \ `//_/     \       ||                [6] - 3
           `/ \|       |      ||
            `"`'.  _  .'      ||
                 \ | /        ||
                  |'|
               .-.|||.-.
              '----"----'



              """)
        while True:
            try:
                choice2 = input("/     [1]      /     [2]     /     [3]      /     [4]      /     [5]     /     [6]      /")
                if choice2 == "4":
                    break
                elif choice2 in ["1","2","3","5","6"] :
                    mistake += 1
                    if mistake == 2:
                        print()
                        print("Well, that was quick. Next you'll get it right.")
                        talk_it_out()
            except:
                pass
        print()
        print()
        print(f"""


                             /  (.-./  (
                            /           \      .^.          Hell clerk:
                           |  -=- -=-    |    (_|_)
                            \   /       /      //           Satan Jr, your father is looking for you.
                             \  .=.    /       \            He told you multiple times to leave the work to us, hell clerks.
                        ___.__`..;._.-'---...  //           Now, you either go to do your homework or i'll have to call him,
                  __.--"        `;'     __   `-.            right here and right at this very moment!
        -===-.--""      __.,              ""-.  ".
          '=_    __.---"   | `__    __'   / .'  .'
          `'-""             \             .'  .'            Oh sorry, didn't see you there, well i guess he did the job right,
                             |  __ __    /   |              He's quite good with the questions to be honest.
		                     |  __ __   //'''               I don't want to keep you waiting here so let's jump right to it.
		                     |         ' | //               Good luck in your last question and Satan is pretty chill so don't
                             |    .      |//                be afraid.
                            .'`., , ,,,.`'.
                           .'`',.',`.` ,.'.`
                            ',',,,,.'...',,'
                            '..,',`'.`,`,.',
                           ,''.,'.,;',.'.`.'
                           '.`.',`,;',',;,.;
                            ',`'.`';',',`',.
                             |     |     |
                             |     |     |
                            (     )(     )

              """)
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print(f"""


   ,    ,    /\   /.            Sorry about my son, he's a troublemaker, i'll tell you that...
  /( /\ )\  _\ \_/ /_           Anyways, let's end this quick.
  |\_||_/| < \_   _/ >          El barrio Huele a ----------- is a song from Ayax y Prok.
  \______/  \|0   0|/           Full song name?
    _\/_   _(_  ^  _)_
   ( () ) /`\|V" "V|/`.         [1] - El barrio huele a polvo
     ||   \  \_____/  /         [2] - El barrio huele a widow
     ()   /\   )=(   / |        [3] - El barrio huele a delito
    |  | /  \_/\=/\_/  |


              """)
        while True:
            try:
                choice2 = input("/     [1]      /     [2]     /     [3]      /")
                if choice2 == "2":
                    print("CONGRATS! YOU WON!")
                    menu0()
                    break
                elif choice2 in ["1","3"] :
                    mistake += 1
                    if mistake == 2:
                        print()
                        print("Well, that was quick. Next you'll get it right.")
                        talk_it_out()
            except:
                pass


    elif choice0 == "4":
        print()
        print()
        menu0()


def menu0_spanish():
    name = welcome()
    print(f"""
    .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.
    :::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::..
    '      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `

                Bienvenido {name}, vos decidís como hacer esto,
                entonces, no gastes mi tiempo y contestá que vas a hacer.

                [1]- Resolverlo hablando
                [2]- Apostar

    .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.
    :::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::..
    '      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `

            """)
    menu_123 = input("/     [1]      /     [2]     /")
    if menu_123 not in ["1", "2"]:
        while True:
            try:
                menu_123 = input("/     [1]      /     [2]     /")
                if menu_123 in ["1", "2"]:
                    break
            except:
                pass
    if menu_123 == "1":
        print()
        print()
        print("Buena suerte, elige sabiamente o muere.")
        talk_it_out_spanish()
    elif menu_123 == "2":
        print()
        print()
        print("Espero que la suerte te acompañe.")
        ceelo_spanish()


def talk_it_out_spanish():
    mistake = 0
    print()
    print()
    print(f"""

        Satan Jr.
                              ..
                        .\   / _\   ..
                       /_ \   ||   / _.
                        ||    ||    ||
                 ; ,     \`.__||__.'/             Satan Jr:
         |\     /( ;\_.;  `./|  __.'              Dejame adivinar, no tenes idea de porque estas acá.
         ' `.  _|_\/_;-'_ .' '||                  Esto es tan aburrido, todos los humanos son iguales, solo
          \ _/`       `.-\_ / ||                  son unos bebés llorones...
      , _ _`; ,--.   ,--. ;'_ _|,
      '`''\| /  ,-\ | _,-\ |/''`'                 Bueno, tengo que hacer esto de todas formas así que...
       \ .-- \__\_/ /` )_/ --. /                  ¿Deseas continuar?
       /    .         -'  .    \ -
      |     /             \     |                 RESPUESTAS:
   .   .  -' `-..____...-' `-  .                  [1] - Para hablar de como se ven los demás, vos realmente
.'`'.__ `._      `-..-''    _.'|                  te pareces a un bebé.
 \ .--.`.  `-..__    _,..-'   L|
  '    \ \      _,| |,_      /_7)                 [2] - Si, lloramos mucho, es bastante molesto a veces.
        \ \    /       \ _.-'/||
         \ \  /.'|   |`.__.'` ||                  [3] - ESPERÁ, ME MORÍ??? SOS MUY HERMOSO
          \ `//_/     \       ||                        POR FAVOR DEJAME ABRAZARTE
           `/ \|       |      ||
            `"`'.  _  .'      ||                  [4] - Casi me duermo mientras hablabamos,
                 \ | /        ||                        dejame volver y elegir otra opción.
                  |'|
               .-.|||.-.                                (ÚLTIMA CHANCE DE VOLVER ATRÁS)
              '----"----'

           """)
    while True:
            try:
                choice0 = input("/     [1]      /     [2]     /     [3]      /     [4]      /")
                if choice0 in ["1", "2", "3", "4"]:
                    break
            except:
                pass
    if choice0 == "1" or choice0 == "2" or choice0 == "3":
        print()
        print()
        print(f"""

        Satan Jr.
                              ..
                        .\   / _\   ..
                       /_ \   ||   / _.
                        ||    ||    ||
                 ; ,     \`.__||__.'/             Satan Jr:
         |\     /( ;\_.;  `./|  __.'              LOL, entonces sos uno de los graciosos, me gustan esos.
         ' `.  _|_\/_;-'_ .' '||                  Bueno, me veo como un bebé porque lo soy, tengo 2023 años.
          \ _/`       `.-\_ / ||                  Pero suficiente de mi, dejame explicarte la situación.
      , _ _`; ,--.   ,--. ;'_ _|,
      '`''\| /  ,-\ | _,-\ |/''`'                 Soy algo así como un filtro, sino pasas este interrogatorio
       \ .-- \__\_/ /` )_/ --. /                  emm bueno...
       /    .         -'  .    \ -                Primera pregunta, ¿Edád del universo aproxímada?
      |     /             \     |                 ANSWERS:
   .   .  -' `-..____...-' `-  .                  [1] - cerca de 8 BILLONES de años.
.'`'.__ `._      `-..-''    _.'|
  '    \ \      _,| |,_      /_7)                 [2] - cerca de 14 BILLONES de años.
        \ \    /       \ _.-'/||
         \ \  /.'|   |`.__.'` ||                  [3] - cerca de 700 MILLONES de años.
          \ `//_/     \       ||
           `/ \|       |      ||
            `"`'.  _  .'      ||
                 \ | /        ||
                  |'|
               .-.|||.-.
              '----"----'
           """)
        while True:
            try:
                choice1 = input("/     [1]      /     [2]     /     [3]      /")
                if choice1 == "2":
                    break
                elif choice1 == "3" or choice1 == "1":
                    mistake += 1
                    if mistake == 2:
                        print()
                        print("Bueno, eso fue rápido, la próxima lo vas a hacer mejor.")
                        talk_it_out_spanish()
            except:
                pass
        print()
        print()
        print(f"""


                              ..
                        .\   / _.   ..          Satan Jr.
                       /_ \   ||   / _.
                        ||    ||    ||          A esta altura ya estoy acostumbrado de estar acá, quizas veo miles de
                 ; ,     \`.__||__.'/           tu especie por acá, pero por suerte en unos siglos salgo asi que no
         |\     /( ;\_.;  `./|  __.'            está tan mal después de todo.
         ' `.  _|_\/_;-'_ .' '||
          \ _/`       `.-\_ / ||                Ya que estamos hablando de números, ¿Cuanta gente vive en la tierra?
      , _ _`; ,--.   ,--. ;'_ _|,
      '`''\| /  ,-\ | _,-\ |/''`'               [1] - cerca de 350 millones
       \ .-- \__\_/ /` )_/ --. /
       /    .         -'  .    .                [2] - cerca de 2 billones
      |     /             \     |
   .   .  -' `-..____...-' `-  .                [3] - cerca de 8 billones
.'`'.__ `._      `-..-''    _.'|
 \ .--.`.  `-..__    _,..-'   L|
  '    \ \      _,| |,_      /_7)
        \ \    /       \ _.-'/||
         \ \  /.'|   |`.__.'` ||
          \ `//_/     \       ||
           `/ \|       |      ||
            `"`'.  _  .'      ||
                 \ | /        ||
                  |'|
               .-.|||.-.
              '----"----'



               """)

        while True:
            try:
                choice2 = input("/     [1]      /     [2]     /     [3]      /")
                if choice2 == "3":
                    break
                elif choice2 == "2" or choice2 == "1":
                    mistake += 1
                    if mistake == 2:
                        print()
                        print("Bueno, eso fue rápido, la próxima lo vas a hacer mejor.")
                        talk_it_out_spanish()
            except:
                pass
        print()
        print()
        print("""

                              ..
                        .\   / _.   ..          Satan Jr.
                       /_ \   ||   / _.
                        ||    ||    ||          Buen trabajo hasta ahora, si contestas bien está
                 ; ,     \`.__||__.'/           la próxima la pregunta Satan.
         |\     /( ;\_.;  `./|  __.'            Vamos al hueso, ¿te parece?
         ' `.  _|_\/_;-'_ .' '||
          \ _/`       `.-\_ / ||                Cuantos "círculos" del infierno describió Dante?
      , _ _`; ,--.   ,--. ;'_ _|,
      '`''\| /  ,-\ | _,-\ |/''`'               [1] - 7
       \ .-- \__\_/ /` )_/ --. /
       /    .         -'  .    .                [2] - 5
      |     /             \     |
   .   .  -' `-..____...-' `-  .                [3] - 1
.'`'.__ `._      `-..-''    _.'|
 \ .--.`.  `-..__    _,..-'   L|                [4] - 9
  '    \ \      _,| |,_      /_7)
        \ \    /       \ _.-'/||                [5] - 12
         \ \  /.'|   |`.__.'` ||
          \ `//_/     \       ||                [6] - 3
           `/ \|       |      ||
            `"`'.  _  .'      ||
                 \ | /        ||
                  |'|
               .-.|||.-.
              '----"----'



              """)
        while True:
            try:
                choice2 = input("/     [1]      /     [2]     /     [3]      /     [4]      /     [5]     /     [6]      /")
                if choice2 == "4":
                    break
                elif choice2 in ["1","2","3","5","6"] :
                    mistake += 1
                    if mistake == 2:
                        print()
                        print("Bueno, eso fue rápido, la próxima lo vas a hacer mejor.")
                        talk_it_out_spanish()
            except:
                pass
        print()
        print()
        print(f"""


                             /  (.-./  (
                            /           \      .^.          Empleado del infierno:
                           |  -=- -=-    |    (_|_)
                            \   /       /      //           Satan Jr, tu padre te está buscando.
                             \  .=.    /       \            Te dijo multiples veces que dejes este trabajo a nosotros, los empleados del infierno.
                        ___.__`..;._.-'---...  //           Ahora te vas a hacer tu tarea o lo voy a tener que llamar,
                  __.--"        `;'     __   `-.            justo acá y justo en este momento!
        -===-.--""      __.,              ""-.  ".
          '=_    __.---"   | `__    __'   / .'  .'
          `'-""             \             .'  .'            Uh disculpá no te ví, bueno supongo que hizo su trabajo bien.
                             |  __ __    /   |              Es bastante bueno con las preguntas para ser honesto.
		                     |  __ __   //'''               No te quiero mantener esperando asi que pasemos al asunto.
		                     |         ' | //               Suerte en tu última pregunta y Satan es alguien tranquilo asi que
                             |    .      |//                no tengas miedo.
                            .'`., , ,,,.`'.
                           .'`',.',`.` ,.'.`
                            ',',,,,.'...',,'
                            '..,',`'.`,`,.',
                           ,''.,'.,;',.'.`.'
                           '.`.',`,;',',;,.;
                            ',`'.`';',',`',.
                             |     |     |
                             |     |     |
                            (     )(     )

              """)
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print(f"""


   ,    ,    /\   /.            Perdón por eso, mi hijo es problemático, por decir algo...
  /( /\ )\  _\ \_/ /_           De todas formas, terminos esto rápido.
  |\_||_/| < \_   _/ >          El barrio Huele a ----------- es una canción de Ayax y Prok.
  \______/  \|0   0|/           ¿Nombre completo?
    _\/_   _(_  ^  _)_
   ( () ) /`\|V" "V|/`.         [1] - El barrio huele a polvo
     ||   \  \_____/  /         [2] - El barrio huele a widow
     ()   /\   )=(   / |        [3] - El barrio huele a delito
    |  | /  \_/\=/\_/  |


              """)
        while True:
            try:
                choice2 = input("/     [1]      /     [2]     /     [3]      /")
                if choice2 == "2":
                    print("FELICIDADES!! GANASTE!!")
                    menu0_spanish()
                    break
                elif choice2 in ["1","3"] :
                    mistake += 1
                    if mistake == 2:
                        print()
                        print("Bueno, eso fue rápido, la próxima lo vas a hacer mejor.")
                        talk_it_out_spanish()
            except:
                pass


    elif choice0 == "4":
        print()
        print()
        menu0_spanish()

def gamble():
   turns = 0
   dice = 0
   while True:
      try:
         msg = input("/[1] ROLL - [2] STAY/  ----> ")
         if msg == "1":
             dice_roll()
             turns += 1
             dice0 = random.randint(1,6)
             dice = dice + dice0
             print(dice)
         elif msg == "2":
             print(dice)
         if turns == 3:
               return dice
      except:
            pass
def ceelo():
    player_name = input("Name----->  ")
    player = gamble()
    player0_name =input("Name----->  ")
    player0 = gamble()
    if player > player0:
        print(f"{player_name} WON!")
        menu0()
    if player < player0:
        print(f"{player0_name} WON!")
        menu0()
    if player == player0:
        print("TIE!")
        menu0()
def gamble_spanish():
   turns = 0
   dice = 0
   while True:
      try:
         msg = input("/[1] TIRAR - [2] QUEDARSE/  ----> ")
         if msg == "1":
             dice_roll()
             turns += 1
             dice0 = random.randint(1,6)
             dice = dice + dice0
             print(dice)
         elif msg == "2":
             print(dice)
         if turns == 3:
               return dice
      except:
            pass
def ceelo_spanish():
    player_name = input("Nombre----->  ")
    player = gamble()
    player0_name =input("Nombre----->  ")
    player0 = gamble()
    if player > player0:
        print(f"{player_name} GANÓ!")
        menu0_spanish()
    if player < player0:
        print(f"{player0_name} GANÓ!")
        menu0_spanish()
    if player == player0:
        print("EMPATE!")
        menu0_spanish()




def dice_roll():
    print("""


     _______     /\O    O.
    /O     /\   /  \      .
   /   O  /O \ / O  \O____O\ ))
((/_____O/    ..    /O     /
  \O    O\    / \  /   O  /
   \O    O\ O/   \/_____O/
    \O____O\/ ))         ))
  ((

         """)
def easy_calculus():
    print("Put two numbers in (first one, hit enter, repeat with the other), different calculations will be done, +, -, *.")
    x = int(input(""))
    y = int(input(""))
    plus = easy_calculator(x,y)
    minus = easy_calculator0(x,y)
    mult = easy_calculator1(x,y)
    print(f"""

            Plus operation = {plus}
            Minus operation = {minus}
            Multiplication operation = {mult}

             +------+.      +------+      +------+       +------+      .+------+
            |`.    | `.    |\     |\      |      |      /|     /|    .' |    .'|
            |  `+--+---+   | +----+-+     +------+     +-+----+ |   +---+--+'  |
            |   |  |   |   | |    | |     |      |     | |    | |   |   |  |   |
            +---+--+.  |   +-+----+ |     +------+     | +----+-+   |  .+--+---+
             `. |    `.|    \|     \|     |      |     |/     |/    |.'    | .'
               `+------+     +------+     +------+     +------+     +------+


          """)
    menu_ingles()
def easy_calculus_spanish():
    print("Inserte dos números (primero uno, presione enter, luego otro y repita) y las siguintes operaciones se van a realizar, +, -, *.")
    x = int(input(""))
    y = int(input(""))
    plus = easy_calculator(x,y)
    minus = easy_calculator0(x,y)
    mult = easy_calculator1(x,y)
    print(f"""

            Suma = {plus}
            Resta = {minus}
            Multiplicación = {mult}

            +------+.      +------+       +------+       +------+      .+------+
            |`.    | `.    |\     |\      |      |      /|     /|    .' |    .'|
            |  `+--+---+   | +----+-+     +------+     +-+----+ |   +---+--+'  |
            |   |  |   |   | |    | |     |      |     | |    | |   |   |  |   |
            +---+--+.  |   +-+----+ |     +------+     | +----+-+   |  .+--+---+
             `. |    `.|    \|     \|     |      |     |/     |/    |.'    | .'
               `+------+     +------+     +------+     +------+     +------+


          """)
    menu_español()

def easy_calculator(x, y):
    return x + y
def easy_calculator0(x,y):
    return x - y
def easy_calculator1(x,y):
    return x * y

if __name__ == "__main__":
    main()