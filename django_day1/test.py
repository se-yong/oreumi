class Character:
    def __init__(self, name, job, level):
        self.name = name
        self.job = job
        self.level = level

    def skill(self, skill_number):
        raise NotImplementedError("Subclasses must implement this method")

    def level_up(self):
        self.level += 1
        print(f"{self.name}, now level = {self.level}")
        if self.job == "magician":
            print("magician level up!!!")
        elif self.job == "worrior":
            print("worrior level up!!!")
        self.skill(self.level)

class Magician(Character):
    def skill(self, skill_number):
        print(f"{self.job} skill {skill_number} activate!")

class Warrior(Character):
    def skill(self, skill_number):
        print(f"{self.job} skill {skill_number} activate!")

name_1 = input("첫 번째 유저의 이름을 입력하세요: ")
job_1 = "magician"
level_1 = 1
oreumi_1 = Magician(name_1, job_1, level_1)

name_2 = input("두 번째 유저의 이름을 입력하세요: ")
job_2 = "worrior"
level_2 = 1
oreumi_2 = Warrior(name_2, job_2, level_2)

oreumi_1.level_up()

oreumi_2.level_up()
