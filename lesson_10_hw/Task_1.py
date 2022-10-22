class Godzilla:
    def __init__(self, stomach_volume, current_volume):
        self.stomach_volume = stomach_volume
        self.current_volume = current_volume

    def method_eat(self, person_volume):
        counter = self.current_volume + person_volume
        if counter > self.stomach_volume * 0.9:
            print("Годзила сыт")
        else:
            print("Годзила скушал человека с весом", person_volume)
            print("Осталось места в желудке:", (self.stomach_volume - person_volume))
            self.current_volume += person_volume


object = Godzilla(100, 10)
object.method_eat(10)
