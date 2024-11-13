class Room:
    room_number = 108  

    def __init__(self, item, installed_year, company_name, condition):
        self.item = item
        self.installed_year = installed_year
        self.company_name = company_name
        self.condition = condition

    def display_info(self):
        return f"Item: {self.item}, Installed Year: {self.installed_year}, Company Name: {self.company_name}, Condition: {self.condition}, Room Number: {Room.room_number}"

item1 = Room("Projector", 2020, "ABC Tech", "Good")
item2 = Room("Whiteboard", 2019, "XYZ Supplies", "Excellent")
item3 = Room("Laptop", 2021, "Tech Corp", "Fair")


print(item1.display_info())
print(item2.display_info())
print(item3.display_info())