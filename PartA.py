class Staff:
    def __init__(self, name, DoB, sex, staffID, address):
        self.name = name
        self.DoB = DoB
        self.sex = sex
        self.staffID = staffID
        self.address = address

        def printInitAttributes(self):
            print(f"Name: {self.name}")
            print(f"DoB: {self.DoB}")
            print(f"Sex: {self.sex}")
            print(f"Staff ID: {self.staffID}")
            print(f"Address: {self.address}")
