x = int(input())
y = int(input())
g = int(input())
# the line contains the ship is list
ship_place_list = []
for i in range(x):
    ship_place_list.append(" ")
if x%2==0:
    ship_index = x//2-1
    ship_place_list[ship_index] = '@'
else:
    ship_index = x//2
    ship_place_list[ship_index] = '@'
# cluster
cluster_list = []
for i in range(x*y):
    cluster_list.append("*")
for i in range(len(cluster_list)):
    if i%x==0 and i!=0:
        print()
    print(cluster_list[i],end="")
else:
    print()
# space between ship and cluster
g_list = []
for i in range(x*g):
    g_list.append(" ")
for i in range(len(g_list)):
    if i%x==0 and i!=0:
        print()
    print(g_list[i], end="")
else:
    print()
# ship and -- lines
for i in range(len(ship_place_list)):
    print(ship_place_list[i],end="")
print()
print("-"*72)
# big while loop that contains tours
time = 0
score = 0
exit_code = True
before_cluster_list = []
before_cluster = 0
if score<x*y:
    while(exit_code):
        score = cluster_list.count(" ")
        action = input("Choose your action!")
        action = action.lower()
        if time%5 == 0 and time != 0:
            g -=1
            for i in range(before_cluster*x):
                before_cluster_list.append(" ")
        if action == 'exit':
            break
        if action == 'left' and ship_index != 0:
            ship_index -=1
            time +=1
        elif action == 'left' and ship_index == 0:
            time +=1
        if action == 'right' and ship_index != len(ship_place_list)-1:
            ship_index +=1
            time +=1
        elif action == 'right' and ship_index == len(ship_place_list)-1:
            time +=1
        if action == 'fire':
            hollow_check_list = []
            for i in range(ship_index,ship_index+(x*(y-1))+1,x):
                hollow_check_list.append(i)
            number_of_pop = 0
            for i in hollow_check_list[::-1]:
                if cluster_list[i] == " ":
                    pass
                elif cluster_list[i] == "*":
                    number_of_pop += 1
            for i in range(0, number_of_pop):
                hollow_check_list.pop(number_of_pop - 1 - i)
            # Laser animation in g
            laser_in_g_list = []
            for i in range(ship_index,ship_index+(x*(g-1))+1,x):
                laser_in_g_list.append(i)
            laser_animation_flag_for_g = True
            while laser_animation_flag_for_g:
                for i in laser_in_g_list[::-1]:
                    if before_cluster !=0:
                        for j in range(len(before_cluster_list)):
                            if j % x == 0 and j != 0:
                                print()
                            print(before_cluster_list[j], end="")
                        else:
                            print()
                    for j in range(len(cluster_list)):
                        if j % x == 0 and j != 0:
                            print()
                        print(cluster_list[j], end="")
                    else:
                        print()
                    g_list[i] = "|"
                    for j in range(len(g_list)):
                        if j % x == 0 and j != 0:
                            print()
                        print(g_list[j], end="")
                    else:
                        print()
                    for k in range(len(ship_place_list)):
                        print(ship_place_list[k], end="")
                    else:
                        print()
                    print("-"*72)
                    g_list[i] = " "
                else:
                    laser_animation_flag_for_g = False
                    laser_in_g_list = []
            # Laser animation in cluster
            laser_animation_flag_for_cluster = True
            while laser_animation_flag_for_cluster:
                if hollow_check_list != []:
                    for j in hollow_check_list[::-1]:
                        if cluster_list[j] == "*":
                            cluster_list[j] = " "
                            if before_cluster != 0:
                                for i in range(len(before_cluster_list)):
                                    if i % x == 0 and i != 0:
                                        print()
                                    print(before_cluster_list[i], end="")
                                else:
                                    print()
                            for i in range(len(cluster_list)):
                                if i % x == 0 and i != 0:
                                    print()
                                print(cluster_list[i], end="")
                            for i in range(len(g_list)):
                                if i % x == 0 and i != 0:
                                    print()
                                print(g_list[i], end="")
                            else:
                                print()
                            for k in range(len(ship_place_list)):
                                print(ship_place_list[k], end="")
                            else:
                                print()
                            print("-" * 72)
                            laser_animation_flag_for_cluster = False
                        if cluster_list[j] == " ":
                            cluster_list[j]="|"
                            if before_cluster !=0:
                                for i in range(len(before_cluster_list)):
                                    if i % x == 0 and i != 0:
                                        print()
                                    print(before_cluster_list[i], end="")
                                else:
                                    print()
                            for i in range(len(cluster_list)):
                                if i % x == 0 and i != 0:
                                    print()
                                print(cluster_list[i], end="")
                            for i in range(len(g_list)):
                                if i % x == 0 and i != 0:
                                    print()
                                print(g_list[i], end="")
                            else:
                                print()
                            for k in range(len(ship_place_list)):
                                print(ship_place_list[k], end="")
                            else:
                                print()
                            print("-" * 72)
                            cluster_list[j]= " "
                if hollow_check_list == []:
                    cluster_list[ship_index+((y-1)*x)] = " "
                    if before_cluster != 0:
                        for i in range(len(before_cluster_list)):
                            if i % x == 0 and i != 0:
                                print()
                            print(before_cluster_list[i], end="")
                        else:
                            print()
                    for i in range(len(cluster_list)):
                        if i % x == 0 and i != 0:
                            print()
                        print(cluster_list[i], end="")
                    for i in range(len(g_list)):
                        if i % x == 0 and i != 0:
                            print()
                        print(g_list[i], end="")
                    else:
                        print()
                    for k in range(len(ship_place_list)):
                        print(ship_place_list[k], end="")
                    else:
                        print()
                    print("-" * 72)
                    laser_animation_flag_for_cluster = False























