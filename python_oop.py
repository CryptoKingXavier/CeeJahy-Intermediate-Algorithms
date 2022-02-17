class Customer:
    # Initializer/Constructor function
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

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

customers = [Customer("Caleb", "Gold"), Customer("Blessing", "Gold"), Customer("Favour", "Silver"), Customer("Joshua", "Bronze")]
for i in range(len(customers)):
    print(f"Name: {customers[i].name}, Membership Type: {customers[i].membership_type}")

customers[0].update_membership("Diamond")
customers[1].update_membership("Diamond")
customers[2].update_membership("Gold")
customers[3].update_membership("Silver")

print("-" * 45)

for i in range(len(customers)):
    print(f"Name: {customers[i].name}, Membership Type: {customers[i].membership_type}")

print("-" * 45)
for i in range(len(customers)):
    print(customers[i])

print("-" * 45)
print(Customer.print_all_customers(customers))
#customers[0].change_name("CeeJahy")
#print(customers[0])


#customers[1].change_name("Caleb")
print(customers[0] == customers[1])

print("-" * 45)
print(customers)
