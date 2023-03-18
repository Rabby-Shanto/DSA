

class AnimalShelter:
    def __init__(self):
        self.catsQueue = []
        self.dogsQueue = []

    def enqueue(self,animal,type):

        if type == "Cat":
            return self.catsQueue.append(animal)
        
        else:
            return self.dogsQueue.append(animal)
        
    def dequeueCat(self):
        if len(self.catsQueue) == 0:
            return None
        else:
            return self.catsQueue.pop(0)
        
    def dequeDog(self):
        if len(self.dogsQueue) == 0:
            return None
        else:
            return self.dogsQueue.pop(0)
        
    def dequeueAny(self):
        if len(self.dogsQueue) == 0:
            res = self.catsQueue.pop(0)
        else:
            res = self.dogsQueue.pop(0)
        
        return res
    


Instance = AnimalShelter()


Instance.enqueue(1,'Cat')
Instance.enqueue(2,'Dog')
Instance.enqueue(5,'Dog')
Instance.enqueue(6,'Cat')
print(Instance.catsQueue)
print(Instance.dogsQueue)
print(Instance.dequeueAny())
print(Instance.dogsQueue)