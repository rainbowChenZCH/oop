# interface is a class that has only abstract methods, it help to the reusability of the code.
# it cannot be instantiated but can be implemented by the subclass.
# The subclass must implement all the abstract methods of the interface.


from abc import ABC, abstractmethod
import pytest

class Interface(ABC):
    
    @abstractmethod
    def method(self):
        pass
    
    @abstractmethod
    def method2(self):
        pass
    
class BadImplementation(Interface):
    
    def method(self):
        return 'BadImplementation method'
        
class Implementation(Interface):
    
    def method(self):
        return 'Implementation method'
        
    def method2(self):
        return 'Implementation method2'
        
def test_interface():
    with pytest.raises(TypeError):
        interface = Interface()
    
def test_not_all_implemented():
    with pytest.raises(TypeError):
        bad_implementation = BadImplementation()

def test_implemented():
    assert Implementation().method() == 'Implementation method'
    assert Implementation().method2() == 'Implementation method2'

if __name__ == '__main__':
    # implementation can be instantiated and method can be called
    Implementation().method()
    # the interface cannot be instantiated 
    try:
        interface = Interface()
    except TypeError as e:
        print(e)
        # Can't instantiate abstract class Interface with abstract methods method, method2
    
    try:
        bad_implementation = BadImplementation()
    except TypeError as e:
        print(e)
        # Can't instantiate abstract class BadImplementation with abstract method method2
    
    