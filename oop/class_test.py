import pytest

class classA:
    publicProperty= 111
    _protectedProperty = 222
    __privateProperty = 333
    
    def __privateMethod(self):
        return "private method"
    
    def publicMethod(classA):
        return "public method"
    
def outer_method(classA):
    return "outer method"

class TestClass:
    class classA:
        publicProperty= 111
        _protectedProperty = 222
        __privateProperty = 333
        
    A= classA()
    
    def test_class_public_property(self):
        
        # class public property can be accessed and modified from outside the class.
        
        assert classA.publicProperty == 111
        classA.publicProperty = "111"
        assert classA.publicProperty == "111"
        classA.publicProperty = 111
        
    def test_one_instance_public_property(self):
        
        # instance public property can be accessed and modified from outside the class, but it is only for the instance, the modification will not affect the class property.
        
        # Note: the priority of the instance property is higher than the class property. 
        
        assert self.A.publicProperty == 111
        self.A.publicProperty = "111"
        assert self.A.publicProperty == "111"
        assert classA.publicProperty == 111
        
        del self.A.publicProperty
        assert self.A.publicProperty == 111
        
    def test_multi_instance_public_property(self):
        
        # each instance has its own public property, the modification of the property of one instance will not affect the property of the other instance.
        
        # each () will create a new instance.
        
        assert classA().publicProperty == 111
        classA().publicProperty = "111"

        assert classA().publicProperty == 111
        

    def test_protected_property(self):
        
        # one underlined property can be accessed from outside the class, you should consider it as a protected property to distinguish it from the public properties.
        
        assert classA._protectedProperty == 222
        classA._protectedProperty = "222"
        assert classA._protectedProperty == "222"
        
    def test_private_property(self):
        
        # two underlined properties can not be accessed from outside the class, it is used as a private property.
        # python make the property private by rename the two underlined propertyies.you can access it by using the class name and the property name like this: classA()._classA__privateProperty
        
        with pytest.raises(AttributeError):
            assert classA.__privateProperty == 333
            
        assert classA._classA__privateProperty == 333
        
        classA._classA__privateProperty = "333"
        assert classA._classA__privateProperty == "333"
    

    def test_private_method(self):
        
        # private method can not be accessed from outside the class.
        # assert classA.__privateMethod() == "private method"
        
        with pytest.raises(AttributeError):
            assert classA.__privateMethod() == "private method"
        # AttributeError: type object 'classA' has no attribute '_TestClass__privateMethod'
        

        # you can access it by using the class name and the method name like this: classA._classA__privateMethod(classA), which seems to be a little bit strange.
        print(classA.__dict__)
        
        assert classA._classA__privateMethod(classA) == "private method"
        
        # something interesting is that you can change the private method to a public method by using the class name and the method name like this: classA._classA__privateMethod = outer_method, the param of the outer_method is the instance of the class.
             
        classA._classA__privateMethod = outer_method
        print(classA.__dict__)
        # print(1/0)
        
        assert classA._classA__privateMethod(classA) == "outer method"
        
    def test_public_method(self):
        
        # public method can be accessed from outside the class. and also can be changed to a outer method.
        
        assert classA.publicMethod(classA) == "public method"
        classA.publicMethod = outer_method
        assert classA.publicMethod(classA) == "outer method"
        
            