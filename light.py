# light는 True => on  False => off

import random

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

light = bool(random.randint(0, 1))
years = 0
days = 0

for i in range(1, 100):
    people_list.append(person("A"))

print(len(people_list))

while True:
    if people_list[0].people_count == 197:
        break
    cur = random.randint(0, 99)
    target = people_list[cur]
    light = target.light_control(light)
    days += 1
    if days == 365:
        years += 1
        days = 0

print(f"초기 전등: {light} 걸린 시간) {years}년 {days}일")