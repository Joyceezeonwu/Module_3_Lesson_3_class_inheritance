#Creating a parent class called Students
class Students:
    def __init__(self, first_name, last_name, student = []):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + '@stutern.com'
    # print("check")  

#Creating instance of the parent class
stud_1 = Students("Bukola", "Dare")
stud_2 = Students("Temitope", "Balogun") 
# print(stud_1.first_name)

#Creating the child class Group_leader
class Group_leader(Students):
    def __init__(self, first_name, last_name, student=[]):
        super().__init__(first_name, last_name)
        self.student = student 
        
    #check    
    # print("child class created") 

#Defining a method that adds students to the list of student under the group leader
    def add_students(self, student):
        self.student.append(student)
        print(self.student, student)
    # print("method created successfully")

#Defining a method that removes students from the list of students under the group leader
    def remove(self, student):
        self.student.remove(student)
        print(self.student, student)
    #check
    # print("item removed successfully")

#Defining a method that prints out the full names of students in the list of students under group leader
    def fullname(self):
        '{} {}'.format(self.first_name, self.last_name)
        return '{} {}'.format(self.first_name, self.last_name)

    #check
    # print ("successful")

#Creating 3 more instances of the parent class.
stud_3 = Students("Lindsay", "Fair") 
stud_4 = Students("Faith", "Stone") 
stud_2 = Students("Ryan", "Star")
# print(stud_3.last_name)

#Creating 2 instances of the sub class you.
G_lead_1 = Group_leader("Dan", "Ryan")
G_lead_2 = Group_leader("Stella", "Glory")
# print(G_lead_1.first_name)

#Adding 2 students each to the list of students under the instances of my subclass.
# G_lead_1.add_students("Christy")
# G_lead_1.add_students("Thompson")
# G_lead_2.add_students("Sandra")
# G_lead_2.add_students("Humphrey")

#Remove 1 student each from the list of students under the instances of your subclass
# G_lead_1.remove("Christy")
# G_lead_2.remove("Humphrey")

#Print the full name of the students in the list of students under the instances of your subclass.
print(G_lead_1.fullname())
print(G_lead_2.fullname())

#Print the email of the instances of your subclass.
def email(self, first_name, last_name):
    self.email = first_name + '.' + last_name + '@stutern.com'
print(G_lead_1.email)
print(G_lead_2.email)


