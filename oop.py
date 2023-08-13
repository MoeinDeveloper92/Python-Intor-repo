class Customer:
    def __init__(self, name, memberShipType):
        self.name = name
        self.memberShipType = memberShipType

    def __str__(self):
        # any time that we want to convert a customer to a string
        return self.name + " " + self.memberShipType

    def printAllCustomers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.memberShipType == other.memberShipType:
            return True
        else:
            return False


customers = [Customer("Cleb", "Gold"), Customer("Brad", "Bronze")]

# method that are not attached to any specofu object are static
# static method
# if we did not define the __str methodm, it would print the physical address of the object

print(customers[0] == customers[1])
