# fixed some attributes or methood into parent class for chalid class 
# and even itself if you make any object of parent class
from abc import ABC ,abstractmethod
class student(ABC):

    def complete_GED_course(self,GED_Course_Name):
        self.GED_Course_Name = GED_Course_Name
        return f"{self.GED_Course_Name} course finished"
    
    @abstractmethod
    def attendence(self,percentage):
        self.percentage = percentage
        return self.percentage
    
    def attendence(self,percentage):
        self.percentage = percentage
        return self.percentage

class cse_Student(student):
    
    def attendence(self, percentage):
        return super().attendence(percentage)
    
student1 = student()

print(student1.attendence(70))
student2 = cse_Student()

print(student2.complete_GED_course("English"))