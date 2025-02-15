#Write a program to implement abstraction on animal class (base class). The abstract method will be move that is for displaying what subclasses can do.

from abc import ABC

class Animal:
    def move(self):
        pass
class human(Animal):
    def move(self):
        print("I can walk and run.")   
class snake(Animal):
    def move(self):
        print("I can crawl on the floor.")  
class rabbit(Animal):
    def move(self):
        print("I can hop around.")  

h1=human()
h1.move()

s1=snake()
s1.move()

r1=rabbit()
r1.move()
