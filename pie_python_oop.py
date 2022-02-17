class User:     # For Inheritance Purposes
    def log(self):
        print("Users")

class Teacher(User):        # Inheriting the User class
    def log(self):      # For Polymorphism
        print("I'm a Teacher!")

class Customer(User):       # Inheriting the User class
    def log(self):
        print("I'm a Customer!")
    
    # Initializer/Constructor function
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    # Creating a property
    # Property Definition for Name Parameter Start
    @property
    def name(self):
        #print("Getting Name Value")
        return self._name

    @name.setter
    def name(self, name):
        #print("Setting Name Value")
        self._name = name
    # Property Definition for Name Parameter Stops

    # To change the name of the customer
    def change_name(self, new_name):
        self.name = new_name

    # To change the membership type of the customer
    def update_membership(self, new_membership):
        self.membership_type = new_membership

    # Converting customer to str type object
    def __str__(self):
        return self.name + " " + self.membership_type

    # To display all the customers and their membership type
    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    # To check if you have repeated customer info.
    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False

    # To output the customers in a list,
    # Override the __repr__ attribute
    __repr__ = __str__


users = [Customer("Caleb", "Gold"),
         Customer("Blessing", "Gold"),
         Customer("Favour", "Silver"),
         Customer("Joshua", "Bronze"),
         Teacher()]

for i in range(len(users) - 1):
    print(users[i].name)
print("-" * 45)

for user in users:
    user.log()
print("-" * 45)

User.log(users)
