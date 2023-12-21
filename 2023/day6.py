import sys
from pathlib import Path
from functools import reduce
import operator

# current_file_path = Path(__file__).resolve()
# parent_dir = current_file_path.parent.parent
# sys.path.append(str(parent_dir))

# from utils import parseinput

# lines = parseinput('inputs/2023-6.txt')

# times = [int(x.strip()) for x in lines[0].split(' ') if x.strip() not in ("","Time:")]
# distances = [int(x.strip()) for x in lines[1].split(' ') if x.strip() not in ("","Distance:")]

# winncombos = []
# for time, distance in zip(times, distances):
#     racechances = 0
#     for i in range(0,time):
#         speed = i
#         timeleft = time - speed
#         mydisctance = speed * timeleft
#         if mydisctance > distance:
#             racechances += 1
#     winncombos.append(racechances)
    
# print(reduce(operator.mul, winncombos, 1))
            
    
# PART 2
# wincombo = 0
# bigtime = 53717880
# bigdistance = 275118112151524
# startpoint = bigtime // 2
# print(startpoint)
# print(bigdistance)

# distance1, distance2 = (bigdistance+1,bigdistance+1)
# bigspeed = startpoint
# smallspeed = startpoint - 1
# while distance1 > bigdistance and distance2 > bigdistance:
#     bigtimeleft = bigtime - bigspeed
#     smalltimeleft = bigtime - smallspeed
#     distance1 = bigspeed*bigtimeleft
#     distance2 = smallspeed*smalltimeleft
#     if distance2 > bigdistance:
#         wincombo += 1
#     if distance1 > bigdistance:
#         wincombo += 1
#     bigspeed += 1
#     smallspeed -= 1
        
# print(wincombo, bigspeed, smallspeed)

import math

def calculate_winning_combinations_part_two(bigtime, bigdistance):
    # Solve the quadratic inequality i * (bigtime - i) > bigdistance
    a = -1
    b = bigtime
    c = -bigdistance

    # Calculate the discriminant
    d = b**2 - 4*a*c

    # Calculate the roots of the quadratic equation
    root1 = (-b - math.sqrt(d)) / (2*a)
    root2 = (-b + math.sqrt(d)) / (2*a)

    # The winning combinations are the integer values between the roots
    wincombo = math.floor(root2) - math.ceil(root1) + 1

    return wincombo

print(calculate_winning_combinations_part_two(53717880, 275118112151524))