import time

class Food:
    def __init__(self, name, nutrients, volume):
        self.name = name
        self.nutrients = nutrients
        self.volume = volume
        self.digested = 0

    def digest(self, organ):
        if organ is None:
            return 0
        nutrient_absorbed = min(organ.absorb_nutrient(self.nutrients), self.nutrients)
        self.nutrients -= nutrient_absorbed
        self.digested += nutrient_absorbed
        self.volume -= 1
        return nutrient_absorbed

class Stomach:
    def __init__(self, capacity):
        self.capacity = capacity
        self.content = None

    def is_full(self):
        return self.content is not None and self.content.volume + 1 > self.capacity

    def digest(self, organ):
        if self.content is None:
            raise Exception("No food in the stomach")
        nutrient_absorbed = self.content.digest(organ)
        if self.content.volume == 0:
            self.content = None
        return nutrient_absorbed

    def feed_food(self, food):
        self.content = food

class Intestine:
    absorb_nutrient_rate = 1

    def __init__(self, length):
        self.length = length

    def absorb_nutrient(self, nutrients):
        absorbed = 0
        while nutrients > 0 and self.length > 0:
            nutrients -= 1
            absorbed += 1
            self.length -= self.absorb_nutrient_rate
        return absorbed if absorbed > 0 else None

def simulate_digestion(food, stomach, intestine):
    while food.digested < food.nutrients:
        if stomach.is_full():
            nutrient_absorbed = stomach.digest(intestine)
            print(f"Stomach Content: {stomach.content.name} - {stomach.content.nutrients} nutrients left")
        else:
            nutrient_absorbed = stomach.digest(intestine)
            print(f"Stomach Content: {stomach.content.name} - {stomach.content.nutrients} nutrients left")

        time.sleep(1)  # Add a sleep of 1 second for better visualization

    print(f"The food {food.name} has been fully digested.")

if __name__ == "__main__":
    apple = Food("apple", 10, 5)
    stomach = Stomach(5)
    intestine = Intestine(10)

    # Feed the food to the stomach
    stomach.feed_food(apple)

    simulate_digestion(apple, stomach, intestine)