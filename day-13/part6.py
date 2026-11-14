from dataclasses import dataclass

@dataclass
class Course:
    title: str
    instructor: str
    students: int = 0

    def __post_init__(self)-> None:
        if self.students < 0:
            raise ValueError("Students cannot be negative")

    def enroll(self, amount: int) -> int:
        if amount <= 0:
            raise ValueError("Enrollment must be positive")
       
        self.students += amount
        return self.students

    def is_popular(self) -> bool:
        return self.students >= 30

course = Course("Python Fundamentals", "Alex")

print(course.enroll(35))
print(course.is_popular())
print(course)    
