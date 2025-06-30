
class Pet:

    all = []

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self, name, pet_type, owner = ''):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.name = name
        self.owner = owner
        self.pet_type = pet_type
        Pet.all.append(self)




class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise TypeError("Pet must be an instance of Pet class")

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)


