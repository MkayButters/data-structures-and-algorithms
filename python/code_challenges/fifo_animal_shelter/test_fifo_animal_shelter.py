import pytest
from fifo_animal_shelter import Queue, AnimalShelter, InvalidOperationError


def test_if_dog_enqueue():
    animal = AnimalShelter()
    animal.enqueue("dog")
    assert animal.dog_queue.front



def test_if_cat_enqueue():
    animal = AnimalShelter()
    animal.enqueue("cat")
    assert animal.cat_queue.front



def test_if_different_enqueue():
    animal = AnimalShelter()
    with pytest.raises(InvalidOperationError):
        animal.enqueue("alligator")


def test_if_cat_dequeue():
    animal = AnimalShelter()
    animal.enqueue("cat")
    animal.enqueue("dog")
    animal.enqueue("cat")
    actual = animal.dequeue("cat")
    expected = "cat"
    assert actual == expected

def test_if_dog_dequeue():
    animal = AnimalShelter()
    animal.enqueue("cat")
    animal.enqueue("dog")
    animal.enqueue("cat")
    actual = animal.dequeue("dog")
    expected = "dog"
    assert actual == expected

def test_if_nopref_dequeue():
    animal = AnimalShelter()
    with pytest.raises(InvalidOperationError):
        animal.dequeue("alligator")

