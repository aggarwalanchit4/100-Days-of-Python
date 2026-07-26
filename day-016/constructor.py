# -----------------------------------------
# Challenge 1 — Constructor and self
# -----------------------------------------

class student : 
    def __init__(self , name , course , year , college_name):
        self.name = name
        self.course = course 
        self.year = year 
        self.college_name = college_name
        pass

student1 = student("Anchit" , "Btech CSE AI" , "2nd" , "NIET")
print(f"Name of student is {student1.name}")
print(f"course of student is {student1.course}")
print(f"year of studying: {student1.year}")
print(f"Name of college is {student1.college_name}")