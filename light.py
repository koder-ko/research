# light는 True => on  False => off

import random
import copy

class person:
    def __init__(self, typeof: str):
        self.light_count = 0
        self.person_type = typeof
        self.people_count = -1

    def light_control(self, light_type: bool):
        # B
        if self.person_type == "B":
            if light_type == True:
                self.people_count += 1
                return False
            else:
                return light_type
        else:
            if self.light_count < 3 and light_type == False:
                return True
            else:
                return light_type


people_list = [person("B")]

lightfirst = bool(random.randint(0, 1))
light = lightfirst
minit = 0
average = 0
time = 0
a = True
inptime = int(input("몇번 시행할지 입력:"))

for i in range(1, 100):
    people_list.append(person("A"))

cur_list = copy.deepcopy(people_list)

while True:
    while a:
        cur = random.randint(0, 99)
        target = cur_list[cur]
        light = target.light_control(light)
        minit += 1
        if cur_list[0].people_count == 197:
            a = False
    print(minit)
    average += minit
    time += 1
    minit = 0
    a = True
    cur_list = copy.deepcopy(people_list)
    if time == inptime:
        break


print(f"초기 전등: {lightfirst} 시행 횟수: {time} 평균 시행:{average/time}")