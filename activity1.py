#Write a program to create a parent class Person (attributes - name, idnumber) with a method display to display the attributes. Create a child class Employee (attributes - name, idnumber, salary, post). Access the attributes of parent class in child class. Then, create an object for child class and call the display method to display the name and idnumber.

#parent class
class person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber

    def display(self):
        return("The employee's name is {} and the idnumber is {}".format(self.name,self.idnumber))  

class employee(person):
    def __init__(self,name,idnumber,salary,post):
        person.__init__(self,name,idnumber)
        self.salary=salary
        self.post=post

emp1=employee("Ali",231,3000,"intern")     
print(emp1.display())         