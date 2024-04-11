# prac5.py

class Zoo:
    def __init__(self, zoo_dict):
        self.zoo_dict = {}

    def add_animal(self, animal):
        if animal.name in list(self.zoo_dict.keys()) and animal.species in list(self.zoo_dict.values()):
            print(f"{animal.name} The {animal.species}는 이미 동물원에 있습니다. 다른 이름을 사용하거나, 다른 종으로 추가해주세요.")
        else:
            self.zoo_dict[animal.name] = animal.species


    def show_animals(self):
        print("현재 동물원에는 다음 동물들이 있습니다.")
        print()
        for i in list(self.zoo_dict.keys()):
            print(f" - {i} The {self.zoo_dict[i]}")

    def show_animals_by_species(self, species):
        for a, b in self.zoo_dict.items():
            if b == species:
               return print(f" - {a} The {b}")
            if b not in self.zoo_dict.values():
                return print("동물원에 말씀하신 종의 동물이 없습니다.")
            else:
                return print("동물원에 말씀하신 종의 동물이 없습니다.")
        pass
    
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

def main():
    print(Animal("Leo","Lion").name)
    # 동물원을 선언하고 10마리의 동물들을 추가합니다.
    zoo = Zoo({})
    zoo.add_animal(Animal("Leo", "Lion"))
    zoo.add_animal(Animal("Harry", "Hippo"))
    zoo.add_animal(Animal("Ella", "Elephant"))
    zoo.add_animal(Animal("Gerry", "Giraffe"))
    zoo.add_animal(Animal("Gira", "Giraffe"))
    zoo.add_animal(Animal("Terry", "Lion"))
    zoo.add_animal(Animal("Barry", "Bear"))
    zoo.add_animal(Animal("Larry", "Leopard"))
    zoo.add_animal(Animal("Cary", "Crocodile"))
    zoo.add_animal(Animal("Mary", "Monkey"))

    # 동물원에 있는 모든 동물을 출력합니다.
    zoo.show_animals()
    ## 출력 결과 : 
    '''
    현재 동물원에는 다음 동물들이 있습니다 :
    - Leo the Lion
    - Harry the Hippo
    - Ella the Elephant
    - Gerry the Giraffe
    - Gira the Giraffe
    - Terry the Lion
    - Barry the Bear
    - Larry the Leopard
    - Cary the Crocodile
    - Mary the Monkey
    '''

    # 특정 종에 해당하는 동물들의 이름만 출력합니다.
    # zoo.show_animals_by_species("Lion")
    # 출력 결과 : 
    '''
    - Leo the Lion
    - Terry the Lion
    '''
    zoo.show_animals_by_species("Parrot")
    # 출력 결과 : 
    '''
    - Ella the Elephant
    '''

    # 이미 존재하는 동물을 추가한 경우, 해당 동물이 이미 있음을 출력합니다.
    zoo.add_animal(Animal("Leo", "Lion"))
    # 출력 결과 : 
    '''
    "Leo the Lion"은 이미 동물원에 있습니다. 다른 이름을 사용하거나, 다른 종으로 추가해주세요.
    '''

if __name__ == "__main__":
    main()