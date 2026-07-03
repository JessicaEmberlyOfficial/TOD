import os
import time
import pygame

class start():
  pygame.mixer.init()
  pygame.mixer.music.set_volume(1)
  pygame.mixer.music.load(os.getcwd() + "/assets/MUSIC/mainmenu.mp3")
  pygame.mixer.music.play(loops=-1)
  os.system("clear")
  question = input("""
////////////////////////////////////////////////////////////////////////
//:::::::::::: ::   .:   :::. ::::::::::::                            //
//;;;;;;;;'''',;;   ;;,  ;;`;;;;;;;;;;''''                            //
//     [[    ,[[[,,,[[[ ,[[ '[[,   [[                                 //
//     $$    "$$$nnn$$$c$$$cc$$$c  $$                                 //
//     88,    888   mM8o888   888, 88,                                //
//     MMM    MMM    YMMYMM   ""`  MMM                                //
//    ...   :::.    :::..,::::::      :::::::-.    :::.  .-:.     ::-.//
// .;;;;;;;.`;;;;,  `;;;;;;;''''       ;;,   `';,  ;;`;;  ';;.   ;;;;'//
//,[[     \[[,[[[[[. '[[ [[cccc        `[[     [[ ,[[ '[[,  '[[,[[['  //
//$$$,     $$$$$$ "Y$c$$ $$´´´´         $$,    $$c$$$cc$$$c   c$$$    //
//"888,_ _,88P888    Y88 888oo,__       888_,o8P' 888   888,,8P"`     //
//  "YMMMMMP" MMM     YM `""YUMMM      MMMMP"`   YMM   ""`mM´         //
////////////////////////////////////////////////////////////////////////
(st)art game, (s)ettings, (h)elp, or (e)xit?: """)
  if question == "st":
    pygame.mixer.music.stop()
    chapter1()
  if question == "s":
    intro()
  if question == "h":
    help()
  if question == "e":
    os.system("clear")
    pygame.quit()
    os._exit(os.EX_OK)
  else:
    error1()

def settings():
  os.system("clear")
  question = input("""
////////////////////////////////////////////////////////////////////////
//:::::::::::: ::   .:   :::. ::::::::::::                            //
//;;;;;;;;'''',;;   ;;,  ;;`;;;;;;;;;;''''                            //
//     [[    ,[[[,,,[[[ ,[[ '[[,   [[                                 //
//     $$    "$$$nnn$$$c$$$cc$$$c  $$                                 //
//     88,    888   mM8o888   888, 88,                                //
//     MMM    MMM    YMMYMM   ""`  MMM                                //
//    ...   :::.    :::..,::::::      :::::::-.    :::.  .-:.     ::-.//
// .;;;;;;;.`;;;;,  `;;;;;;;''''       ;;,   `';,  ;;`;;  ';;.   ;;;;'//
//,[[     \[[,[[[[[. '[[ [[cccc        `[[     [[ ,[[ '[[,  '[[,[[['  //
//$$$,     $$$$$$ "Y$c$$ $$´´´´         $$,    $$c$$$cc$$$c   c$$$    //
//"888,_ _,88P888    Y88 888oo,__       888_,o8P' 888   888,,8P"`     //
//  "YMMMMMP" MMM     YM `""YUMMM      MMMMP"`   YMM   ""`mM´         //
////////////////////////////////////////////////////////////////////////
(r)esize, (g)o back, or (e)xit?: """)
  if question == "r":
    os.system("clear")
    print("Please make sure that you resize your terminal. [3]")
    time.sleep(1)
    os.system("clear")
    print("Please make sure that you resize your terminal. [2]")
    time.sleep(1)
    os.system("clear")
    print("Please make sure that you resize your terminal. [1]")
    time.sleep(1)
    os.system("clear")
    print("When the extended title card fits, please wait. [5]")
    time.sleep(1)
    os.system("clear")
    print("When the extended title card fits, please wait. [4]")
    time.sleep(1)
    os.system("clear")
    print("When the extended title card fits, please wait. [3]")
    time.sleep(1)
    os.system("clear")
    print("When the extended title card fits, please wait. [2]")
    time.sleep(1)
    os.system("clear")
    print("When the extended title card fits, please wait. [1]")
    time.sleep(1)
    os.system("clear")
    count = 1
    while count < 5:
      os.system("clear")
      print("""
**********////////////////////////////////////////////////////////////////////////**********
**********//:::::::::::: ::   .:   :::. ::::::::::::                            //**********
**********//;;;;;;;;'''',;;   ;;,  ;;`;;;;;;;;;;''''                            //**********
**********//     [[    ,[[[,,,[[[ ,[[ '[[,   [[                                 //**********
**********//     $$    "$$$""'$$$c$$$cc$$$c  $$                                 //**********
**********//     88,    888   "88o888   888, 88,                                //**********
**********//     MMM    MMM    YMMYMM   ""`  MMM                                //**********
**********//    ...   :::.    :::..,::::::      :::::::-.    :::.  .-:.     ::-.//**********
**********// .;;;;;;;.`;;;;,  `;;;;;;;''''       ;;,   `';,  ;;`;;  ';;.   ;;;;'//**********
**********//,[[     \[[,[[[[[. '[[ [[cccc        `[[     [[ ,[[ '[[,  '[[,[[['  //**********
**********//$$$,     $$$$$$ "Y$c$$ $$""''         $$,    $$c$$$cc$$$c   c$$"    //**********
**********//"888,_ _,88P888    Y88 888oo,__       888_,o8P' 888   888,,8P"`     //**********
**********//  "YMMMMMP" MMM     YM ""''YUMMM      MMMMP"`   YMM   '"`mM'        //**********
**********////////////////////////////////////////////////////////////////////////**********
""")
      count = count + 1
      time.sleep(3)
      os.system("clear")
      if count == 5:
        start()
  if question == "g":
    start()
  if question == "e":
    pygame.quit()
    os.system("clear")
    os._exit(os.EX_OK)

def help():
  os.system("clear")
  question = input("""
////////////////////////////////////////////////////////////////////////
//:::::::::::: ::   .:   :::. ::::::::::::                            //
//;;;;;;;;'''',;;   ;;,  ;;`;;;;;;;;;;''''                            //
//     [[    ,[[[,,,[[[ ,[[ '[[,   [[                                 //
//     $$    "$$$nnn$$$c$$$cc$$$c  $$                                 //
//     88,    888   mM8o888   888, 88,                                //
//     MMM    MMM    YMMYMM   ""`  MMM                                //
//    ...   :::.    :::..,::::::      :::::::-.    :::.  .-:.     ::-.//
// .;;;;;;;.`;;;;,  `;;;;;;;''''       ;;,   `';,  ;;`;;  ';;.   ;;;;'//
//,[[     \[[,[[[[[. '[[ [[cccc        `[[     [[ ,[[ '[[,  '[[,[[['  //
//$$$,     $$$$$$ "Y$c$$ $$´´´´         $$,    $$c$$$cc$$$c   c$$$    //
//"888,_ _,88P888    Y88 888oo,__       888_,o8P' 888   888,,8P"`     //
//  "YMMMMMP" MMM     YM `""YUMMM      MMMMP"`   YMM   ""`mM´         //
////////////////////////////////////////////////////////////////////////
(a)bout, (c)redits, (g)o back, or (e)xit?
""")
  if question == "a":
    about()
  if question == "c":
    credits()
  if question == "g":
    start()
  if question == "e":
    os.system("clear")
    os._exit(os.EX_OK)

def about():
  os.system("clear")
  count = 10
  while count > 1:
    print("""
////////////////////////////////////////////////////////////////////////
//:::::::::::: ::   .:   :::. ::::::::::::                            //
//;;;;;;;;'''',;;   ;;,  ;;`;;;;;;;;;;''''                            //
//     [[    ,[[[,,,[[[ ,[[ '[[,   [[                                 //
//     $$    "$$$nnn$$$c$$$cc$$$c  $$                                 //
//     88,    888   mM8o888   888, 88,                                //
//     MMM    MMM    YMMYMM   ""`  MMM                                //
//    ...   :::.    :::..,::::::      :::::::-.    :::.  .-:.     ::-.//
// .;;;;;;;.`;;;;,  `;;;;;;;''''       ;;,   `';,  ;;`;;  ';;.   ;;;;'//
//,[[     \[[,[[[[[. '[[ [[cccc        `[[     [[ ,[[ '[[,  '[[,[[['  //
//$$$,     $$$$$$ "Y$c$$ $$´´´´         $$,    $$c$$$cc$$$c   c$$$    //
//"888,_ _,88P888    Y88 888oo,__       888_,o8P' 888   888,,8P"`     //
//  "YMMMMMP" MMM     YM `""YUMMM      MMMMP"`   YMM   ""`mM´         //
////////////////////////////////////////////////////////////////////////
About:
    - Created by:
        - APITA Games:

    - Notes:
        - Please enjoy our game. ~ Jessica Emberly.
        
[This page will close in """ + str(count) + """]
""")
    time.sleep(1)
    count = count - 1
    os.system("clear")
    if count == 1:
      help()

def credits():
  os.system("clear")
  count = 10
  while count > 1:
    print("""
////////////////////////////////////////////////////////////////////////
//:::::::::::: ::   .:   :::. ::::::::::::                            //
//;;;;;;;;'''',;;   ;;,  ;;`;;;;;;;;;;''''                            //
//     [[    ,[[[,,,[[[ ,[[ '[[,   [[                                 //
//     $$    "$$$nnn$$$c$$$cc$$$c  $$                                 //
//     88,    888   mM8o888   888, 88,                                //
//     MMM    MMM    YMMYMM   ""`  MMM                                //
//    ...   :::.    :::..,::::::      :::::::-.    :::.  .-:.     ::-.//
// .;;;;;;;.`;;;;,  `;;;;;;;''''       ;;,   `';,  ;;`;;  ';;.   ;;;;'//
//,[[     \[[,[[[[[. '[[ [[cccc        `[[     [[ ,[[ '[[,  '[[,[[['  //
//$$$,     $$$$$$ "Y$c$$ $$´´´´         $$,    $$c$$$cc$$$c   c$$$    //
//"888,_ _,88P888    Y88 888oo,__       888_,o8P' 888   888,,8P"`     //
//  "YMMMMMP" MMM     YM `""YUMMM      MMMMP"`   YMM   ""`mM´         //
////////////////////////////////////////////////////////////////////////
Credits:
    - Development team:
        - Lead Developer:
            - Jessica Emberly""" +
        #- Assistant Developer
            #- Siouxsie Gonzales
    """- Main Menu:
        - Music:
            - MM-01 by TeddyBearSuicide
    - In-Game:
        - Sound Effects:
            - 8-bit Game Start by u_xmiiqyhi46 on Pixabay
            
        - Characters (In order of appearance):
            - Sebastian (Frog): Sebastian Sins
            - Wendolyn (Frog): Wendolyn Dallas
            - Caleb (Spider): Caleb Jimarez
            
[This page will close in """ + str(count) + """]
""")
    time.sleep(1)
    count = count - 1
    os.system("clear")
    if count == 1:
      help()

def intro():
  print("""
////////////////////////////////////////////////////////////////////////
//:::::::::::: ::   .:   :::. ::::::::::::                            //
//;;;;;;;;'''',;;   ;;,  ;;`;;;;;;;;;;''''                            //
//     [[    ,[[[,,,[[[ ,[[ '[[,   [[                                 //
//     $$    "$$$nnn$$$c$$$cc$$$c  $$                                 //
//     88,    888   mM8o888   888, 88,                                //
//     MMM    MMM    YMMYMM   ""`  MMM                                //
//    ...   :::.    :::..,::::::      :::::::-.    :::.  .-:.     ::-.//
// .;;;;;;;.`;;;;,  `;;;;;;;''''       ;;,   `';,  ;;`;;  ';;.   ;;;;'//
//,[[     \[[,[[[[[. '[[ [[cccc        `[[     [[ ,[[ '[[,  '[[,[[['  //
//$$$,     $$$$$$ "Y$c$$ $$´´´´         $$,    $$c$$$cc$$$c   c$$$    //
//"888,_ _,88P888    Y88 888oo,__       888_,o8P' 888   888,,8P"`     //
//  "YMMMMMP" MMM     YM `""YUMMM      MMMMP"`   YMM   ""`mM´         //
////////////////////////////////////////////////////////////////////////
Wendolyn: It
""")
  time.sleep(1)
  os.system("clear")
  print("""
////////////////////////////////////////////////////////////////////////
//:::::::::::: ::   .:   :::. ::::::::::::                            //
//;;;;;;;;'''',;;   ;;,  ;;`;;;;;;;;;;''''                            //
//     [[    ,[[[,,,[[[ ,[[ '[[,   [[                                 //
//     $$    "$$$nnn$$$c$$$cc$$$c  $$                                 //
//     88,    888   mM8o888   888, 88,                                //
//     MMM    MMM    YMMYMM   ""`  MMM                                //
//    ...   :::.    :::..,::::::      :::::::-.    :::.  .-:.     ::-.//
// .;;;;;;;.`;;;;,  `;;;;;;;''''       ;;,   `';,  ;;`;;  ';;.   ;;;;'//
//,[[     \[[,[[[[[. '[[ [[cccc        `[[     [[ ,[[ '[[,  '[[,[[['  //
//$$$,     $$$$$$ "Y$c$$ $$´´´´         $$,    $$c$$$cc$$$c   c$$$    //
//"888,_ _,88P888    Y88 888oo,__       888_,o8P' 888   888,,8P"`     //
//  "YMMMMMP" MMM     YM `""YUMMM      MMMMP"`   YMM   ""`mM´         //
////////////////////////////////////////////////////////////////////////
Wendolyn: It was
""")
  time.sleep(1)
  os.system("clear")
  print("""
////////////////////////////////////////////////////////////////////////
//:::::::::::: ::   .:   :::. ::::::::::::                            //
//;;;;;;;;'''',;;   ;;,  ;;`;;;;;;;;;;''''                            //
//     [[    ,[[[,,,[[[ ,[[ '[[,   [[                                 //
//     $$    "$$$nnn$$$c$$$cc$$$c  $$                                 //
//     88,    888   mM8o888   888, 88,                                //
//     MMM    MMM    YMMYMM   ""`  MMM                                //
//    ...   :::.    :::..,::::::      :::::::-.    :::.  .-:.     ::-.//
// .;;;;;;;.`;;;;,  `;;;;;;;''''       ;;,   `';,  ;;`;;  ';;.   ;;;;'//
//,[[     \[[,[[[[[. '[[ [[cccc        `[[     [[ ,[[ '[[,  '[[,[[['  //
//$$$,     $$$$$$ "Y$c$$ $$´´´´         $$,    $$c$$$cc$$$c   c$$$    //
//"888,_ _,88P888    Y88 888oo,__       888_,o8P' 888   888,,8P"`     //
//  "YMMMMMP" MMM     YM `""YUMMM      MMMMP"`   YMM   ""`mM´         //
////////////////////////////////////////////////////////////////////////
Wendolyn: It was that
""")
  time.sleep(1)
  os.system("clear")
  

def chapter1():
  os.system("clear")
  sound = pygame.mixer.Sound(os.getcwd() + "/assets/SFX/gamestart.mp3")
  pygame.mixer.Sound.play(sound)
  os.system("clear")
  time.sleep(3)
  os.system("clear")
  print("""
      .::.    .::. `:         
    ,;'  ';,,;'  ';,`;`         
    n[  - [nn[  - [n '[n        
    Y$    $YY$    $Y  "$c       
     8o,,o8  8o,,o8    "8o      
      "MM"    "MM"        "Mm     
       mm                    mm 
  .:`:\        (.)            /:`:. <[*nervous whistling*]>
,;'  `;\                     /;`  ';,
n[    '[n                   n['    [n
Y$     "$c cccc  cccc cccc  $"     $Y
 8o,    "8o                o8"    ,o8 
  "M      "Mm             mM"     M"  
""")
  time.sleep(1)
  os.system("clear")
  print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[  -   [nn[  -   [n[[          
      88888o,  ,o8  8o,  ,o8 88         
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm         (.)         mm <[*nervous whistling*]>
  .:`:\                       /:`:.
,;'  `;\                     /;`  ';,
n[    '[n                   n['    [n
Y$     "$c cccc  cccc cccc  $"     $Y
 8o,    "8o                o8"    ,o8 
  "M      "Mm             mM"     M"  
""")
  time.sleep(1)
  os.system("clear")
  print("""
         `:  .::::.    .::::.       
         ,;,;' ,' ';,,;' ,' ';,   
         [[n[      [nn[      [n    
         $$Y$  -   $YY$  -   $Y     
         88 8o,  ,o8  8o,  ,o88      
         MMM  "MmmM"    "MmM"mmm      
        MMMM                   MM 
        MMMM         ).)       mm <[*nervous whistling*]>
  .:`:\                       /:`´:.
,;'  `;\                     /;`   ';,
n[    '[n                   n['     [n
Y$     "$c cccc  cccc cccc  $"      $Y
 8o,    "8o                o8"     ,o8 
  "M      "Mm             mM"      M"  
""")
  time.sleep(1)
  os.system("clear")
  print("""
                 .::::.    .::::.     
            /;`,;' ,' ';,,;' ,' ';,   
           n[' n[      [nn[      [n   
          c$"  Y$  -   $YY$  -   $Y   
         o8"    8o,  ,o8  8o,  ,o8    
        mM"      "MmmM"    "MmmM"   
        MM                     MM
  .:`:  MM          ).)         /:`:. <[*nervous whistling*]>
,;'  `;                        /;`  ';,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc  cccc c$"     $Y
 8o,    "8o                o8"     ,o8 
  "M      "Mm             mM"      M"
""")
  time.sleep(1)
  os.system("clear")
  print("""
         `:  .::::.    .::::.       
         ,;,;' ,' ';,,;' ,' ';,   
         [[n[      [nn[      [n    
         $$Y$  -   $YY$  -   $Y     
         88 8o,  ,o8  8o,  ,o88      
         MMM  "MmmM"    "MmmM"mm      
        MMMM                   MM 
    .:`:MMMM         ).)      :`:. <[*nervous whistling*]>
  .:`:\ MMM                  /:`:.
,;'  `;\MM                  /;`  ';,
n[    '[n                   n['    [n
Y$     "$c cccc  cccc cccc  $"     $Y
 8o,    "8o                o8"    ,o8 
  "M      "Mm             mM"     M"  
""")
  time.sleep(1)
  os.system("clear")
  print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  (.) $YY$  (.) $Y$$          
      88888o,  ,o8  8o,  ,o8 88          
      MM  "MmmM"    "MmmmM"  MM     
      MM                     MM
      mm         (--)        mm
  .:`:                        /:`:.
,;'  `;                      /;`  ';,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc  cccc c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"     M"  
""")
  time.sleep(1)
  os.system("clear")
  print("""
  .: .:   :.    .:   :. :.  
,;',;'     ';,,;'     ';,';,
n[ n[  (.)  [nn[  (.)  [n [n
Y$ Y$       $YY$       $Y $Y
 8o,8o,d8b,o8  8o,d8b,o8,o8 
  "M "MYMPM"    "MYMPM" M"  
  .:                    :.  
,;'                      ';,
n[        ————            [n
Y$                        $Y
 8o,                    ,o8 
  "M                    M"
  mmmmmmmmmmmmmmmmmmmmmmmm
  mmmmmmmmmmmmmmmmmmmmmmmm
.´                        `.
""")
  time.sleep(1)
  os.system("clear")
  print("""
  .: .:   :.    .:   :. :.  
,;',;'     ';,,;'     ';,';,
n[ n[  -    [nn[   -   [n [n
Y$ Y$       $YY$       $Y $Y
 8o,8o,d8b,o8  8o,d8b,o8,o8 
  "M "MYMPM"    "MYMPM" M"  
  .:                    :.  
,;'                      ';,
n[          ()            [n <[Wendolyn: Yo.]>   
Y$                        $Y
 8o,                    ,o8 
  "M                    M"
  mmmmmmmmmmmmmmmmmmmmmmmm
  mmmmmmmmmmmmmmmmmmmmmmmm
.´                        `.
""")
  time.sleep(3)
  os.system("clear")
  print("""
  .: .:   :.    .:   :. :.  
,;',;'     ';,,;'     ';,';,
n[ n[  (.)  [nn[  (.)  [n [n
Y$ Y$       $YY$       $Y $Y
 8o,8o,d8b,o8  8o,d8b,o8,o8 
  "M "MYMPM"    "MYMPM" M"  
  .:                    :.  
,;'                      ';,
n[        ————            [n
Y$                        $Y
 8o,                    ,o8 
  "M                    M"
  mmmmmmmmmmmmmmmmmmmmmmmm
  mmmmmmmmmmmmmmmmmmmmmmmm
.´                        `.
""")
  time.sleep(1)
  os.system("clear")
  print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  -   $YY$  -   $Y$$          
      88888o,  ,o8  8o,  ,o8 88          
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm         (.)         mm
 ,;'`;q                      /;`'';,
,;'  `'                     /;`    ':,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc cccc  c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"     M" 
""")
  time.sleep(1)
  os.system("clear")
  print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  (.) $YY$ (.)  $Y$$          
      88888o,  ,o8  8o,  ,o8 88          
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm         ( )         mm <[Sebastian: What's up?]>
 ,;'`;q                      /;`'';,
,;'  `'                     /;'    ':,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc cccc  c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"     M" 
""")
  time.sleep(3)
  os.system("clear")
  print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  (.) $YY$ (.)  $Y$$          
      88888o,  ,o8  8o,  ,o8 88          
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm         ¿_          mm
 ,;'`;q                      /;`'';,
,;'  `'                     /;'    ':,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc cccc  c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"     M" 
""")
  time.sleep(1)
  os.system("clear")
  choice = input("""
  .: .:   :.    .:   :. :.
,;',;'     ';,,;'     ';,';,
n[ n[  (.)  [nn[  (.)  [n [n
Y$ Y$       $YY$       $Y $Y
 8o,8o,d8b,o8  8o,d8b,o8,o8 
  "M "MYMPM"    "MYMPM" M"  
  .:                    :. (a): <[Sooo, why are you so nervous?]>
,;'                      ';, (b): <[Are you going to be like this the whole day?]>
n[        ————            [n (c): <[You're thinking about your ex aren't you?]>
Y$                        $Y (d): <[Sebastian, hey look, breathe, alright? You got this.]>
 8o,                    ,o8 (e): <[Ummm, sooo why exactly are you... are you in trouble?]>
  "M                    M"
  mmmmmmmmmmmmmmmmmmmmmmmm
  mmmmmmmmmmmmmmmmmmmmmmmm
.´                        `.
Please choose a letter: """)
  if choice == "a":
    os.system("clear")
    print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  (.) $YY$ (.)  $Y$$          
      88888o,  ,o8  8o,  ,o8 88          
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm        (--)         mm
 ,;'`;q                      /;`'';,
,;'  `'                     /;'    ':,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc cccc  c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"     M" 
""")
    time.sleep(1)
    os.system("clear")
    print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  -   $YY$  -   $Y$$          
      88888o,  ,o8  8o,  ,o8 88          
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm         ()          mm <[*deep breath*]>
 ,;'`;q                      /;`'';,
,;'  `'                     /;'    ':,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc cccc  c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"     M" 
""")
    time.sleep(1)
    os.system("clear")
    print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  (.) $YY$ (.)  $Y$$          
      88888o,  ,o8  8o,  ,o8 88          
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm         ()          mm <[Honestly I'm lost.]>
 ,;'`;q                      /;`'';,
,;   `'                     /;'    ':,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc cccc  c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"     M" 
""")
    time.sleep(3)
    os.system("clear")
    print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  (.) $YY$ (.)  $Y$$          
      88888o, `,o8  8o,` ,o8 88          
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm         ()          mm <[I miss Caleb.]>
 ,;'`;q                      /;`'';,
,;   `'                     /;'    ':,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc cccc  c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"     M" 
""")
    time.sleep(3)
    os.system("clear")
    print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  -   $YY$  -   $Y$$          
      88888o, `,o8  8o,` ,o8 88          
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm         ¿_          mm <[*crying*]>
 ,;'`;q                      /;`'';,
,;   `'                     /;'    ':,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc cccc  c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"     M" 
""")
    time.sleep(1)
    os.system("clear")
    print("""
  .: .:   :.    .:   :. :.  
,;',;'     ';,,;'     ';,';,
n[ n[  (.)  [nn[  (.)  [n [n
Y$ Y$       $YY$       $Y $Y
 8o,8o,d8b,o8  8o,d8b,o8,o8 
  "M "MYMPM"    "MYMPM" M"  
  .:                    :.  
,;'                      ';,
n[        ————            [n
Y$                        $Y
 8o,                    ,o8 
  "M                    M"
  mmmmmmmmmmmmmmmmmmmmmmmm
  mmmmmmmmmmmmmmmmmmmmmmmm
.´                        `.
""")
    time.sleep(1)
    os.system("clear")
    print("""
  .: .:   :.    .:   :. :.  
,;',;'     ';,,;'     ';,';,
n[ n[  (.)  [nn[  (.)  [n [n
Y$ Y$       $YY$       $Y $Y
 8o,8o,d8b,o8  8o,d8b,o8,o8 
  "M "MYMPM"    "MYMPM" M"  
  .:                    :.  
,;'                      ';,
n[         ————           [n
Y$                        $Y
 8o,                    ,o8 
  "M                    M"
  mmmmmmmmmmmmmmmmmmmmmmmm
  mmmmmmmmmmmmmmmmmmmmmmmm
.´                        `.
""")
    time.sleep(1)
    os.system("clear")
    print("""
  .: .:   :.    .:   :. :.  
,;',;'     ';,,;'     ';,';,
n[ n[  (.)  [nn[  (.)  [n [n
Y$ Y$       $YY$       $Y $Y
 8o,8o,d8b,o8  8o,d8b,o8,o8 
  "M "MYMPM"    "MYMPM" M"  
  .:                    :.  
,;'                      ';,
n[          ()            [n <[Well, I am always here for you hun, just let it out.]>
Y$                        $Y
 8o,                    ,o8 
  "M                    M"
  mmmmmmmmmmmmmmmmmmmmmmmm
  mmmmmmmmmmmmmmmmmmmmmmmm
.´                        `.
""")
    time.sleep(5)
    os.system("clear")
    print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  -   $YY$  -   $Y$$          
      88888o, `,o8  8o,` ,o8 88          
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm         ¿_          mm <[Thanks.]>
 ,;'`;q                      /;`'';,
,;   `'                     /;'    ':,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc cccc  c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"    mM" 
""")
    time.sleep(5)
    os.system("clear")
    print("""
//////////////////////////////////////////////////////////////////////////////////////
//  .,-:::::   ::   .:   :::.  ::::::::::. ::::::::::::.,:::::: :::::::..       :.  //
//,;;;'````'  ,;;   ;;,  ;;`;;  `;;;```.;;;;;;;;;;;'''';;;;'''' ;;;;``;;;;      ;;  //
//[[[        ,[[[,,,[[[ ,[[ '[[, `]]nnn]]'      [[      [[cccc   [[[,/[[['      [[  //
//$$$        "$$$```$$$c$$$cc$$$c $$$""         $$      $$````   $$$$$$c        $$  //
//`88bo,__,o, 888   `88o888   888,888o          88,     888oo,__ 888b `88bo,    88  //
//  `YUMMMMMP`MMM    YMMYMM   ``` YMMMb         MMM     8888YUMMMMMMM   `W`     MM  //
//  .,-:::::     ...     .        :::::::::::. :::    .,::::::::::::::::::.,::::::  //
//,;;;'````'  .;;;;;;;.  ;;,.    ;;;`;;;```.;;;;;;    ;;;;'''';;;;;;;;'''';;;;''''  //
//[[[        ,[[     ``[,[[[[, ,[[[[,`]]nnn]]' [[[     [[cccc      [[      [[cccc   //
//$$$        $$$,     $$$$$$$$$$$"$$$ $$$``    $$'     $$````      $$      $$`````  //
//`88bo,__,o,"888,_ _,88P888 Y88" 888o888o    o88oo,.__888oo,__    88,     888oo,__ //
//  `YUMMMMMP` `YMMMMMP` MMM  M'  `MMMYMMMb   ````YUMMM````YUMMM   MMM     88888UMMM//
//////////////////////////////////////////////////////////////////////////////////////
""")
    time.sleep(5)
    os.system("clear")
    save = input("""
////////////////////////////////////////////////////////////////////////
//:::::::::::: ::   .:   :::. ::::::::::::                            //
//;;;;;;;;'''',;;   ;;,  ;;`;;;;;;;;;;''''                            //
//     [[    ,[[[,,,[[[ ,[[ '[[,   [[                                 //
//     $$    "$$$nnn$$$c$$$cc$$$c  $$                                 //
//     88,    888   mM8o888   888, 88,                                //
//     MMM    MMM    YMMYMM   ""`  MMM                                //
//    ...   :::.    :::..,::::::      :::::::-.    :::.  .-:.     ::-.//
// .;;;;;;;.`;;;;,  `;;;;;;;''''       ;;,   `';,  ;;`;;  ';;.   ;;;;'//
//,[[     \[[,[[[[[. '[[ [[cccc        `[[     [[ ,[[ '[[,  '[[,[[['  //
//$$$,     $$$$$$ "Y$c$$ $$´´´´         $$,    $$c$$$cc$$$c   c$$$    //
//"888,_ _,88P888    Y88 888oo,__       888_,o8P' 888   888,,8P"`     //
//  "YMMMMMP" MMM     YM `""YUMMM      MMMMP"`   YMM   ""`mM´         //
////////////////////////////////////////////////////////////////////////
(s)ave game, (c)ontinue, or (e)xit: """)
    if save == "s":
      os.system("clear")
      os.system("touch savefile.txt")
      with open("savefile.txt", "w") as f:
        f.write("a1")
      chapter2()
    if save == "c":
      os.system("clear")
      chapter2()
    if save == "e":
      pygame.quit()
      os.system("clear")
      os._exit(os.EX_OK)
  if choice == "b":
    time.sleep(1)
    os.system("clear")
    print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  (.)  $YY$ (.) $Y$$          
      88888o,  ,o8  8o,  ,o8 88          
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm         ¿_          mm 
 ,;'`;q                      /;`'';,
,;'  `'                     /;'    ':,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc cccc  c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"     M" 
""")
    time.sleep(3)
    os.system("clear")
    print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  -   $YY$  -   $Y$$          
      88888o,  ,o8  8o,  ,o8 88          
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm         ¿_          mm 
 ,;'`;q                      /;`'';,
,;'  `'                     /;'    ':,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc cccc  c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"     M" 
""")
    time.sleep(1)
    os.system("clear")
    print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  -   $YY$  -   $Y$$          
      88888o,  ,o8  8o,  ,o8 88          
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm         ()          mm <[*deep breath*]> 
 ,;'`;q                      /;`'';,
,;'  `'                     /;'    ':,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc cccc  c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"     M" 
""")
    time.sleep(1)
    os.system("clear")
    print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  -   $YY$  -   $Y$$          
      88888o,  ,o8  8o,  ,o8 88          
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm         ¿_          mm <[I need to go.]>
 ,;'`;q                      /;`'';,
,;'  `'                     /;'    ':,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc cccc  c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"     M" 
""")
    time.sleep(3)
    os.system("clear")
    print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  -   $YY$  -   $Y$$          
      88888o,  ,o8  8o,  ,o8 88          
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm         ¿_          mm <[*sniffles*]>
 ,;'`;q           `          /;`'';,
,;'  `'                     /;'    ':,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc cccc  c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"     M" 
""")
    time.sleep(3)
    os.system("clear")
    print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  (.) $YY$  (.) $Y$$          
      88888o,  ,o8  8o,  ,o8 88          
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm         ¿_          mm
 ,;'`;q                      /;`'';,
,;'  `'                     /;'    ':,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc cccc  c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"     M" 
""")
    time.sleep(1)
    os.system("clear")
    print("""
  .: .:   :.    .:   :. :.  
,;',;'     ';,,;'     ';,';,
n[ n[  (.)  [nn[  (.)  [n [n
Y$ Y$       $YY$       $Y $Y
 8o,8o,d8b,o8  8o,d8b,o8,o8 
  "M "MYMPM"    "MYMPM" M"  
  .:                    :.  
,;'                      ';,
n[         ————           [n
Y$                        $Y
 8o,                    ,o8 
  "M                    M"
  mmmmmmmmmmmmmmmmmmmmmmmm
  mmmmmmmmmmmmmmmmmmmmmmmm
.´                        `.
""")
    time.sleep(1)
    os.system("clear")
    print("""
  .: .:   :.    .:   :. :.  
,;',;'     ';,,;'     ';,';,
n[ n[  (´)  [nn[  (`)  [n [n
Y$ Y$       $YY$       $Y $Y
 8o,8o,d8b,o8  8o,d8b,o8,o8 
  "M "MYMPM"    "MYMPM" M"  
  .:                    :.  
,;'                      ';,
n[      ______            [n
Y$                        $Y
 8o,                    ,o8 
  "M                    M"
  mmmmmmmmmmmmmmmmmmmmmmmm
  mmmmmmmmmmmmmmmmmmmmmmmm
.´                        `.
""")
    time.sleep(1)
    os.system("clear")
    print("""
  .: .:   :.    .:   :. :.  
,;',;'     ';,,;'     ';,';,
n[ n[  (.)  [nn[  (.)  [n [n
Y$ Y$       $YY$       $Y $Y
 8o,8o,d8b,o8  8o,d8b,o8,o8 
  "M "MYMPM"    "MYMPM" M"  
  .:                    :.  
,;'                      ';,
n[         ()             [n <[Ok.]>
Y$                        $Y
 8o,                    ,o8 
  "M                    M"
  mmmmmmmmmmmmmmmmmmmmmmmm
  mmmmmmmmmmmmmmmmmmmmmmmm
.´                        `.
""")
    time.sleep(5)
    os.system("clear")
    print("""
//////////////////////////////////////////////////////////////////////////////////////
//  .,-:::::   ::   .:   :::.  ::::::::::. ::::::::::::.,:::::: :::::::..       :.  //
//,;;;'````'  ,;;   ;;,  ;;`;;  `;;;```.;;;;;;;;;;;'''';;;;'''' ;;;;``;;;;      ;;  //
//[[[        ,[[[,,,[[[ ,[[ '[[, `]]nnn]]'      [[      [[cccc   [[[,/[[['      [[  //
//$$$        "$$$```$$$c$$$cc$$$c $$$""         $$      $$````   $$$$$$c        $$  //
//`88bo,__,o, 888   `88o888   888,888o          88,     888oo,__ 888b `88bo,    88  //
//  `YUMMMMMP`MMM    YMMYMM   ``` YMMMb         MMM     8888YUMMMMMMM   `W`     MM  //
//  .,-:::::     ...     .        :::::::::::. :::    .,::::::::::::::::::.,::::::  //
//,;;;'````'  .;;;;;;;.  ;;,.    ;;;`;;;```.;;;;;;    ;;;;'''';;;;;;;;'''';;;;''''  //
//[[[        ,[[     ``[,[[[[, ,[[[[,`]]nnn]]' [[[     [[cccc      [[      [[cccc   //
//$$$        $$$,     $$$$$$$$$$$"$$$ $$$``    $$'     $$````      $$      $$`````  //
//`88bo,__,o,"888,_ _,88P888 Y88" 888o888o    o88oo,.__888oo,__    88,     888oo,__ //
//  `YUMMMMMP` `YMMMMMP` MMM  M'  `MMMYMMMb   ````YUMMM````YUMMM   MMM     88888UMMM//
//////////////////////////////////////////////////////////////////////////////////////
""")
    time.sleep(5)
    os.system("clear")
    save = input("""
////////////////////////////////////////////////////////////////////////
//:::::::::::: ::   .:   :::. ::::::::::::                            //
//;;;;;;;;'''',;;   ;;,  ;;`;;;;;;;;;;''''                            //
//     [[    ,[[[,,,[[[ ,[[ '[[,   [[                                 //
//     $$    "$$$nnn$$$c$$$cc$$$c  $$                                 //
//     88,    888   mM8o888   888, 88,                                //
//     MMM    MMM    YMMYMM   ""`  MMM                                //
//    ...   :::.    :::..,::::::      :::::::-.    :::.  .-:.     ::-.//
// .;;;;;;;.`;;;;,  `;;;;;;;''''       ;;,   `';,  ;;`;;  ';;.   ;;;;'//
//,[[     \[[,[[[[[. '[[ [[cccc        `[[     [[ ,[[ '[[,  '[[,[[['  //
//$$$,     $$$$$$ "Y$c$$ $$´´´´         $$,    $$c$$$cc$$$c   c$$$    //
//"888,_ _,88P888    Y88 888oo,__       888_,o8P' 888   888,,8P"`     //
//  "YMMMMMP" MMM     YM `""YUMMM      MMMMP"`   YMM   ""`mM´         //
////////////////////////////////////////////////////////////////////////
(s)ave game, (c)ontinue, or (e)xit: """)
    if save == "s":
      os.system("clear")
      os.system("touch savefile.txt")
      with open("savefile.txt", "w") as f:
        f.write("b1")
      chapter2()
    if save == "c":
      os.system("clear")
      chapter2()
    if save == "e":
      os.system("clear")
      os._exit(os.EX_OK)
  if choice == "c":
    os.system("clear")
    print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  (.) $YY$ (.)  $Y$$          
      88888o,  ,o8  8o,  ,o8 88          
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm         ¿_          mm
 ,;'`;q                      /;`'';,
,;'  `'                     /;'    ':,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc cccc  c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"     M" 
""")
    time.sleep(1)
    os.system("clear")
    print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  ___ $YY$ ___  $Y$$          
      88888o,  ,o8  8o,  ,o8 88          
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm         ¿_          mm <[Yeah, I am honestly.]>
 ,;'`;q                      /;`'';,
,;'  `'                     /;'    ':,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc cccc  c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"     M" 
""")
    time.sleep(3)
    os.system("clear")
    print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  ___ $YY$ ___  $Y$$          
      88888o,`` ,o8  8o,`,o8 88          
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm          ()         mm <[*deep breaths*]>
 ,;'`;q                      /;`'';,
,;'  `'                     /;'    ':,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc cccc  c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"     M" 
""")
    time.sleep(1)
    os.system("clear")
    print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  ___ $YY$ ___  $Y$$          
      88888o,`` ,o8  8o,`,o8 88          
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm          ¿_         mm <[*sniffles*]>
 ,;'`;q            `         /;`'';,
,;'  `'                     /;'    ':,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc cccc  c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"     M" 
""")
    time.sleep(1)
    os.system("clear")
    print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  (.) $YY$ (.)  $Y$$          
      88888o,  ,o8  8o,  ,o8 88          
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm         ¿_          mm
 ,;'`;q                      /;`'';,
,;'  `'                     /;'    ':,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc cccc  c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"     M" 
""")
    time.sleep(1)
    os.system("clear")
    print("""
  .: .:   :.    .:   :. :.  
,;',;'     ';,,;'     ';,';,
n[ n[  (.)  [nn[  (.)  [n [n
Y$ Y$       $YY$       $Y $Y
 8o,8o,d8b,o8  8o,d8b,o8,o8 
  "M "MYMPM"    "MYMPM" M"  
  .:                    :.  
,;'                      ';,
n[         ()             [n <[I understand, well just know I am here.]>
Y$                        $Y
 8o,                    ,o8 
  "M                    M"
  mmmmmmmmmmmmmmmmmmmmmmmm
  mmmmmmmmmmmmmmmmmmmmmmmm
.´                        `.
""")
    time.sleep(3)
    os.system("clear")
    print("""
       `:  .::::.    .::::.  `:          
       ,;,;' ,' ';,,;' ,' ';,,;          
       [[n[      [nn[      [n[[          
       $$Y$  (.) $YY$ (.)  $Y$$          
      88888o,  ,o8  8o,  ,o8 88          
      MM  "MmmM"    "MmmM"   MM     
      MM                     MM
      mm         ()          mm <[Thanks.]>
 ,;'`;q                      /;`'';,
,;'  `'                     /;'    ':,
n[    '[n                    n['    [n
Y$     "$c cccc  cccc cccc  c$"     $Y
 8o,    "8o                o8"    ,o8 
  "M     "Mm              mM"     M" 
""")
    time.sleep(3)
    os.system("clear")
    print("""
//////////////////////////////////////////////////////////////////////////////////////
//  .,-:::::   ::   .:   :::.  ::::::::::. ::::::::::::.,:::::: :::::::..       :.  //
//,;;;'````'  ,;;   ;;,  ;;`;;  `;;;```.;;;;;;;;;;;'''';;;;'''' ;;;;``;;;;      ;;  //
//[[[        ,[[[,,,[[[ ,[[ '[[, `]]nnn]]'      [[      [[cccc   [[[,/[[['      [[  //
//$$$        "$$$```$$$c$$$cc$$$c $$$""         $$      $$````   $$$$$$c        $$  //
//`88bo,__,o, 888   `88o888   888,888o          88,     888oo,__ 888b `88bo,    88  //
//  `YUMMMMMP`MMM    YMMYMM   ``` YMMMb         MMM     8888YUMMMMMMM   `W`     MM  //
//  .,-:::::     ...     .        :::::::::::. :::    .,::::::::::::::::::.,::::::  //
//,;;;'````'  .;;;;;;;.  ;;,.    ;;;`;;;```.;;;;;;    ;;;;'''';;;;;;;;'''';;;;''''  //
//[[[        ,[[     ``[,[[[[, ,[[[[,`]]nnn]]' [[[     [[cccc      [[      [[cccc   //
//$$$        $$$,     $$$$$$$$$$$"$$$ $$$``    $$'     $$````      $$      $$`````  //
//`88bo,__,o,"888,_ _,88P888 Y88" 888o888o    o88oo,.__888oo,__    88,     888oo,__ //
//  `YUMMMMMP` `YMMMMMP` MMM  M'  `MMMYMMMb   ````YUMMM````YUMMM   MMM     88888UMMM//
//////////////////////////////////////////////////////////////////////////////////////
""")
    time.sleep(5)
    os.system("clear")
    save = input("""
////////////////////////////////////////////////////////////////////////
//:::::::::::: ::   .:   :::. ::::::::::::                            //
//;;;;;;;;'''',;;   ;;,  ;;`;;;;;;;;;;''''                            //
//     [[    ,[[[,,,[[[ ,[[ '[[,   [[                                 //
//     $$    "$$$nnn$$$c$$$cc$$$c  $$                                 //
//     88,    888   mM8o888   888, 88,                                //
//     MMM    MMM    YMMYMM   ""`  MMM                                //
//    ...   :::.    :::..,::::::      :::::::-.    :::.  .-:.     ::-.//
// .;;;;;;;.`;;;;,  `;;;;;;;''''       ;;,   `';,  ;;`;;  ';;.   ;;;;'//
//,[[     \[[,[[[[[. '[[ [[cccc        `[[     [[ ,[[ '[[,  '[[,[[['  //
//$$$,     $$$$$$ "Y$c$$ $$´´´´         $$,    $$c$$$cc$$$c   c$$$    //
//"888,_ _,88P888    Y88 888oo,__       888_,o8P' 888   888,,8P"`     //
//  "YMMMMMP" MMM     YM `""YUMMM      MMMMP"`   YMM   ""`mM´         //
////////////////////////////////////////////////////////////////////////
(s)ave game, (c)ontinue, or (e)xit: """)
    if save == "s":
      os.system("clear")
      os.system("touch savefile.txt")
      with open("savefile.txt", "w") as f:
        f.write("c1")
      chapter2()
    if save == "c":
      os.system("clear")
      chapter2()
    if save == "e":
      os.system("clear")
      os._exit(os.EX_OK)
  #if save == "d":
  #if save == "e":

def chapter2():
  os.system("clear")
  print("Therapist: So, you..., you miss him? Caleb?")
  time.sleep(5)
  os.system("clear")
  print("""
     /:``:\          /:` .::.    .::. `:\          /:``:\     
    /;`  `;\        /;`,;'  ';,,;'  ';,`;\        /;`  `;\    
   n['    '[n      n[' n[    [nn[    [n '[n      n['    '[n   
  c$"      "$c    c$"  Y$ (.) YY (.) $Y  "$c    c$"      "$c  
 o8"        "8o  o8"    8o `  o8  `  8o   o8"  "8o        "''
mM"          "MmmM"      "MM" () "MM"      "MmmM"          "Mm <[I just...]>
""")
  time.sleep(3)
  os.system("clear")
  print("""
     /:``:\          /:` .::.    .::. `:\          /:``:\     
    /;`  `;\        /;`,;'  ';,,;'  ';,`;\        /;`  `;\    
   n['    '[n      n[' n[    [nn[    [n '[n      n['    '[n   
  c$"      "$c    c$"  Y$ ___ YY ___ $Y  "$c    c$"      "$c  
 o8"        "8o  o8"    8o `  o8  `  8o   o8"  "8o        "''
mM"          "MmmM"      "MM" () "MM"      "MmmM"          "Mm <[Yes, I miss him.]>
""")
  time.sleep(3)
def error1():
  os.system("clear")
  print("Invalid entry, please try again. [5]")
  time.sleep(1)
  os.system("clear")
  print("Invalid entry, please try again. [4]")
  time.sleep(1)
  os.system("clear")
  print("Invalid entry, please try again. [3]")
  time.sleep(1)
  os.system("clear")
  print("Invalid entry, please try again. [2]")
  time.sleep(1)
  os.system("clear")
  print("Invalid entry, please try again. [1]")
  os.system("clear")
  start()