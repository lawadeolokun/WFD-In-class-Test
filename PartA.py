class Staff:
    def __init__(self, name, DoB, sex, staffID, address):
        self.name = name
        self.DoB = DoB
        self.sex = sex
        self.staffID = staffID
        self.address = address

    def print_init_attributes(self):
            print(f"Name: {self.name}")
            print(f"DoB: {self.DoB}")
            print(f"Sex: {self.sex}")
            print(f"Staff ID: {self.staffID}")
            print(f"Address: {self.address}")

    def update_name(self,new_name):
            if isinstance(new_name, str):
                self.name = new_name
            else:
                print("Name entered is invalid")
            
    def update_DoB(self,new_DoB):
            if isinstance(new_DoB, str):
                self.DoB = new_DoB
            else:
                print("DOB entered is invalid")

    def update_sex(self,new_sex):
            if isinstance(new_sex, str):
                self.sex = new_sex
            else:
                print("Sex entered is invalid")

    def update_staffID(self,new_staffID):
            if isinstance(new_staffID, str):
                self.staffID = new_staffID
            else:
                print("Staff ID entered is invalid")

    def update_address(self, new_address):
            if isinstance(new_address, str):
                self.address = new_address
            else:
                print("Address entered is invalid")

class Doctor(Staff):
    def __init__(self, name, DoB, sex, staffID, address, specialisation, salary, years_experience):
        super().__init__(name, DoB, sex, staffID, address)
        self.specialisation = specialisation
        self.salary = salary
        self.years_experience = years_experience

    def print_attributes(self):
        super().print_init_attributes()
        print(f"Specialisation: {self.specialisation}")
        print(f"Salary: {self.salary}")
        print(f"Years of Experience: {self.years_experience}")

    def update_specialisation(self, new_specialisation):
        if isinstance(new_specialisation, str):
            self.specialisation = new_specialisation
        else:
            print("Specialisation entered is invalid")
    
    def update_salary(self, new_salary):
        if isinstance(new_salary, (int, float)):
            self.salary = new_salary
        else:
            print("Salary entered is invalid")

    def update_years_experience(self, new_years_experience):
        if isinstance(new_years_experience, (int, float)):
            self.years_experience = new_years_experience
        else:
            print("Years of Experience entered is invalid")

staff1 = Staff("Steven Smith", "04/12/1988", "Male", "12345", "53 Waterville Terrace")
doctor1 = Doctor("Sandra Johnson", "17/05/1993", "Female", "90152", "4 Ballentree Lodge", "Cardiology", "€123,000", "21")

print("\nStaff:")
staff1.print_init_attributes()

print("\nDoctor:")
doctor1.print_attributes()

print("\nUpdate Staff")
staff1.update_staffID("B15003847")
staff1.update_address("101 Oldtown Road")
staff1.print_init_attributes()

print("\nUpdate Doctor")
doctor1.update_specialisation("Neurology")
doctor1.update_name("Richie Tinpot")
doctor1.print_attributes()