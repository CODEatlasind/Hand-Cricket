import random
oe=int(input("Lets Play; u bat 1st:"))
while oe<=1 and oe>=6:
    oe=int(input("Enter a number b/w 1-6:"))

UR_totalrun=0
#Ur batting
z=random.randint(1,6)
while oe!=z:
    print(f'U drew {oe}')
    print(f'CPU drew {z}')
    UR_totalrun+=oe
    oe=int(input("Ur turn, Enter a number b/w 1-6:"))
    z=random.randint(1,6)

print(f'''1st inning is over. 
          You Scored {UR_totalrun}.
        
          2nd Inning Starts: ''')
#CPU's turn
z=random.randint(1,6)
oe=int(input("ur turn:"))
CPU_totalrun=0
while oe!=z:
    print(f'CPU drew {z}')
    print(f'U drew {oe}')
    CPU_totalrun+=oe
    oe=int(input("CPU turn, Enter a number b/w 1-6:"))
    z=random.randint(1,6)   
if(UR_totalrun>CPU_totalrun): 
   print(f'U won. U scored {UR_totalrun}. CPU scored {CPU_totalrun}') 
elif(CPU_totalrun>UR_totalrun): 
   print(f'CPU won. CPU scored {CPU_totalrun}. U Scored {UR_totalrun}') 
elif(CPU_totalrun==UR_totalrun): 
   print(f'Matchs a tie. U scored {UR_totalrun}. CPU scored {CPU_totalrun}') 