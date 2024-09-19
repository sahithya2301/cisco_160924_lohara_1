class Dog:
    # Class attribute
    species = "Canis lupus familiaris"
    
    # Constructor (initializer) method
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old."
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}."

# Creating an object (instance of the class)
dog1 = Dog("Buddy", 3)
print(dog1.description())  # Output: Buddy is 3 years old.
print(dog1.speak("Woof!"))  # Output: Buddy says Woof!

fork = Dog("Fork", 5)
print(fork.description())  # Output: Buddy is 3 years old.
print(fork.speak("Woof!"))  # Output: Buddy says Woof!

dogs = [dog1, fork]
from functools import reduce
#reduce syntax
#reduce(<func>, iterable,init_value)
ages_sum = reduce((lambda s, dog: s + dog.age), dogs, 0)
print(ages_sum)

nums = [10,20,30,41]
nums_sum = reduce(lambda s,num: s+num, nums,0) #101
nums_prod = reduce(lambda p,num: p*num, nums,1) #246000
print(nums_sum, nums_prod)
