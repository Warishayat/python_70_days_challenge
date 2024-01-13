#super keyword
class person:
    def __init__(self):
        self.name="waris"
        self.section="4A-Afternoon"
    def display_info(self):
        print(F"MY name is {self.name} and section is {self.section}")

class student(person):
    def __init__(self):
        super().__init__()
        self.roll="21368"
        self.dept="Software-Enginnering"

    def display(self):
        super().display_info()
        print(f"Name is {self.name} his section is{self.section} , where roll num is {self.roll} and department is {self.dept}")


a=student()
a.display_info()
a.display()