"""
Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in Linked list data structure.
"""
from time import time

import pytest
from queue import Queue


class Animal:
    
    def __init__(self, name):
        self.name = name
        self.timestamp = time()


class Dog(Animal):
    def __repr__(self):
        return f'Dog: {self.name}'


class Cat(Animal):
    def __repr__(self):
        return f'Cat: {self.name}'


class AnimalShelter:
    
    def __init__(self):
        self.dog_queue = Queue(10)
        self.cat_queue = Queue(10)
        
    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self.dog_queue.enqueue(animal)
        elif isinstance(animal, Cat):
            self.cat_queue.enqueue(animal)
    
    def dequeue_dog(self):
        if self.dog_queue.is_empty():
            raise Exception('No Dogs Left')
        return self.dog_queue.dequeue()
    
    def dequeue_cat(self):
        if self.cat_queue.is_empty():
            raise Exception('No Cats Left')
        return self.cat_queue.dequeue()
    
    def dequeue_any(self):
        dog = self.dog_queue.peek()
        cat = self.cat_queue.peek()
        
        if not dog and not cat:
            raise Exception('No Animals Left')
        elif dog and not cat:
            return self.dog_queue.dequeue()
        elif cat and not dog:
            return self.cat_queue.dequeue()
        
        if dog.timestamp < cat.timestamp:
            return self.dog_queue.dequeue()
        else:
            return self.cat_queue.dequeue()


def test_animal_shelter():
    animal_shelter = AnimalShelter()
    
    dog_1 = Dog('1')
    animal_shelter.enqueue(dog_1)
    
    dog_2 = Dog('2')
    animal_shelter.enqueue(dog_2)
    
    cat_1 = Cat('1')
    animal_shelter.enqueue(cat_1)
    
    dog_3 = Dog('3')
    animal_shelter.enqueue(dog_3)
    
    cat_2 = Cat('2')
    animal_shelter.enqueue(cat_2)
    
    assert animal_shelter.dequeue_any() == dog_1
    assert animal_shelter.dequeue_cat() == cat_1
    assert animal_shelter.dequeue_dog() == dog_2
    assert animal_shelter.dequeue_cat() == cat_2
    assert animal_shelter.dequeue_any() == dog_3
    
    with pytest.raises(Exception) as e:
        animal_shelter.dequeue_any()
    assert str(e.value) == 'No Animals Left'
    
    with pytest.raises(Exception) as e:
        animal_shelter.dequeue_dog()
    assert str(e.value) == 'No Dogs Left'
    
    with pytest.raises(Exception) as e:
        animal_shelter.dequeue_cat()
    assert str(e.value) == 'No Cats Left'
