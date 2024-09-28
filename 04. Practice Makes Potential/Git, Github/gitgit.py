class animals:
    def __init__(self, name, species, num_legs, edibility, age):  # 동물의 특성
        self.name = name
        self.species = species
        self.num_legs = num_legs
        self.edibility = edibility
        self.age = age
        self.velocity = 0

    def __str__(self):
        return self.name

    def birth(self):
        return f"{self}가 태어났습니다. 종은 {self.species}, 다리의 개수는 {self.num_legs}개, 식용가능 여부는{self.edibility}입니다."


horse = animals("twinky", "Zibra", "4", "Yes")
print(horse.birth())
