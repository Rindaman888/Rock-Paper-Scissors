import random

Rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

Paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

Scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
''' 
Win = '''
██╗    ██╗██╗███╗   ██╗
██║    ██║██║████╗  ██║
██║ █╗ ██║██║██╔██╗ ██║
██║███╗██║██║██║╚██╗██║
╚███╔███╔╝██║██║ ╚████║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝
'''
Loss = '''
██╗      ██████╗ ███████╗███████╗
██║     ██╔═══██╗██╔════╝██╔════╝
██║     ██║   ██║███████╗███████╗
██║     ██║   ██║╚════██║╚════██║
███████╗╚██████╔╝███████║███████║
╚══════╝ ╚═════╝ ╚══════╝╚══════╝
'''

Draw = '''
██████╗ ██████╗  █████╗ ██╗    ██╗
██╔══██╗██╔══██╗██╔══██╗██║    ██║
██║  ██║██████╔╝███████║██║ █╗ ██║
██║  ██║██╔══██╗██╔══██║██║███╗██║
██████╔╝██║  ██║██║  ██║╚███╔███╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ 
'''
valid_vulue = '''
.--------------------------------------------------.
|██████╗ ██╗     ███████╗ █████╗ ███████╗███████╗  |
|██╔══██╗██║     ██╔════╝██╔══██╗██╔════╝██╔════╝  |
|██████╔╝██║     █████╗  ███████║███████╗█████╗    |
|██╔═══╝ ██║     ██╔══╝  ██╔══██║╚════██║██╔══╝    |
|██║     ███████╗███████╗██║  ██║███████║███████╗  |
|╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝  |
|                                                  |
|███████╗███╗   ██╗████████╗███████╗██████╗        |
|██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔══██╗       |
|█████╗  ██╔██╗ ██║   ██║   █████╗  ██████╔╝       |
|██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗       |
|███████╗██║ ╚████║   ██║   ███████╗██║  ██║       |
|╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝       |
|                                                  |
|                     █████╗                       |
|                    ██╔══██╗                      |
|                    ███████║                      |
|                    ██╔══██║                      |
|                    ██║  ██║                      |
|                    ╚═╝  ╚═╝                      |
|                                                  |
|██╗   ██╗ █████╗ ██╗     ██╗██████╗               |
|██║   ██║██╔══██╗██║     ██║██╔══██╗              |
|██║   ██║███████║██║     ██║██║  ██║              |
|╚██╗ ██╔╝██╔══██║██║     ██║██║  ██║              |
| ╚████╔╝ ██║  ██║███████╗██║██████╔╝              |
|  ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝╚═════╝               |
|                                                  |
|██╗   ██╗ █████╗ ██╗     ██╗   ██╗███████╗        |
|██║   ██║██╔══██╗██║     ██║   ██║██╔════╝        |
|██║   ██║███████║██║     ██║   ██║█████╗          |
|╚██╗ ██╔╝██╔══██║██║     ██║   ██║██╔══╝          |
| ╚████╔╝ ██║  ██║███████╗╚██████╔╝███████╗        |
|  ╚═══╝  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝        |
'--------------------------------------------------'
'''

rock_paper_scissors = [Rock,Paper,Scissors]

playedchoose = int(input("What do you choose? Type 0 for Rock | Type 1 for Paper | Type 2 for Scissors \n: "))
if playedchoose >= 3 or playedchoose < 0:
    print(f"{valid_vulue}")
else:
    print("You Choose",rock_paper_scissors[playedchoose])
    
    computerchoose = random.randint(0,2)
    print("Computer Choose",rock_paper_scissors[computerchoose])

    if playedchoose == computerchoose:
        print(f"{Draw}")
    elif playedchoose == 0 and computerchoose == 2:
        print(f"{Win}")
    elif computerchoose == 0 and playedchoose == 2:
        print(f"{Loss}")
    elif computerchoose > playedchoose:
        print(f"{Loss}")
    elif playedchoose > computerchoose:
        print(f"{Win}")


