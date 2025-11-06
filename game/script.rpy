# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Staff
define char_quinn = Character("Quinn Harbin")
define char_cleon = Character("Cleo Gangleri")
define char_theo = Character("Theo Brimings")
define char_dalia = Character("Dalia Summers")

#Customers
define char_marg = Character("Margaret Winters")
define char_mirc = Character("Breaden Mircof")
define char_jane = Character("Jane Motley")
define char_chad = Character("Chaddicus Bargingtonner")
define char_sol = Character("Helene Sol")
define char_celeste = Character("Celestia Druidess")
define char_conner = Character("Connor Daines")
define char_henry = Character("Henry Daines")
define char_kaffi = Character("Kaffi Cleid")
define char_gerald = Character("Gerald Foscher")
define char_alex = Character("Alex Reeler")

init:
    $ import random
$ marg_reject = False
$ mirc_reject = False
$ jane_reject = False
$ chad_reject = False
$ sol_reject = False
$ celeste_reject = False
$ conner_reject = False
$ henry_reject = False
$ kaffi_reject = False
$ gerald_reject = False
$ alex_reject = False

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory
    $ day1_scene_list = ["marg_scene"]
    $ original_scene_list = ["mirc_scene", "jane_scene", "chad_scene", "sol_scene", "celeste_scene", "conner_scene", "henry_scene", "kaffi_scene", "gerald_scene", "alex_scene"]
    $ day1_scene_list.extend(random.sample(original_scene_list, 2))
    $ i = 1
    call marg_scene
    while i < len(day1_scene_list):
        $ original_scene_list.remove(day1_scene_list[i])
        call expression day1_scene_list[i]
        $ i += 1


    #$ day1_scene_list = ["marg_scene"]
    #$ event_2 = random.choice(original_scene_list)
    #$ original_scene_list.remove(event_2)
    #$ day1_scene_list.append(event_2)
    #$ event_3 = random.choice(original_scene_list)
    #$ original_scene_list.remove(event_3)
    #$ day1_scene_list.append(event_3)

    #$ day2_scene_list = []
    #$ day2_scene_list.extend(day1_scene_list)
    #$ event_4 = random.choice(original_scene_list)
    #$ original_scene_list.remove(event_4)
    #$ day2_scene_list.append(event_4)
    #$ event_5 = random.choice(original_scene_list)
    #$ original_scene_list.remove(event_5)
    #$ day2_scene_list.append(event_5)
    #$ event_6 = random.choice(original_scene_list)
    #$ original_scene_list.remove(event_6)
    #$ day2_scene_list.append(event_6)

    $ day3_scene_list = []

    $ day4_scene_list = []

    $ day5_scene_list = []

    # These display lines of dialogue.



    # This ends the game.

    return

label marg_scene:
    char_marg "test1"
    return

label mirc_scene:
    char_marg "test2"
    return


label jane_scene:
    char_marg "test3"
    return


label chad_scene:
    char_marg "test4"
    return


label sol_scene:
    char_marg "test5"
    return


label celeste_scene:
    char_marg "test6"
    return
    

label conner_scene:
    char_marg "test7"
    return


label henry_scene:
    char_marg "test8"
    return


label kaffi_scene:
    char_marg "test9"
    return


label gerald_scene:
    char_marg "test10"
    return


label alex_scene:
    char_marg "test11"
    return
