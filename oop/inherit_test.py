
# inheritance test

# class includes porperty(s) and method(s), inherited by the child class. 
# Polymorphism is also tested by the method(s) of the parent and mutatedChild class.

class parent:
    name="parent"
    def __init__(self):
        print("Parent class constructor")
        
    def method(self):
        return "parent method return"
    
class child(parent):
    pass

class mutatedChild(parent):
    def __init__(self):
        self.name = "mutatedChild"
        print("Mutated Child class constructor")
    
    def method(self):
        return "mutatedChild method return"
        
def test_property():
    assert parent().name == "parent"
    assert child().name == "parent"
    assert mutatedChild().name == "mutatedChild"
    
    # passed
    # parent class has a property name and child class has inherited it, mutatedChild has changed the property name.
    
    
def test_method():
    assert parent().method() == "parent method return"
    assert child().method() == "parent method return"
    assert mutatedChild().method() == "mutatedChild method return"
    
    # passed
    # parent class has a method and child class has inherited it, mutatedChild has changed the method.
    