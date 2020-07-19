from inherit import Contact

class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send "
              "'{}' order to '{}'".format(order, self.name))

c = Contact("Some Body", "somebody@example.net")
print(c.name, c.email)