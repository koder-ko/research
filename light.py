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
lightfirst = bool(random.randint(0, 1))
light = lightfirst
hour = 0
minit = 0

for i in range(1, 100):
    people_list.append(person("A"))
while True:
    if people_list[0].people_count == 197:
        break
    cur = random.randint(0, 99)
    target = people_list[cur]
    light = target.light_control(light)
    minit += 1
    if minit == 60:
        hour += 1
        minit = 0

print(f"초기 전등: {lightfirst} 걸린 시간) {hour}시간 {minit}분 => {hour/24}일")