# Shopping Cart Program
# Created for internship Task

class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, name, price, quantity=1):
        if name in self.cart:
            self.cart[name]['quantity'] += quantity
        else:
            self.cart[name] = {'price': price, 'quantity': quantity}
        print(f"{quantity} x {name} added to cart.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
            return
        print("\n--- Cart Contents ---")
        for item, details in self.cart.items():
            subtotal = details['price'] * details['quantity']
            print(f"{item}: ₹{details['price']} x {details['quantity']} = ₹{subtotal}")
        print("---------------------")

    def update_quantity(self, name, quantity):
        if name in self.cart:
            self.cart[name]['quantity'] = quantity
            print(f"Updated {name} quantity to {quantity}.")
        else:
            print(f"{name} not found in cart.")

    def remove_item(self, name):
        if name in self.cart:
            del self.cart[name]
            print(f"{name} removed from cart.")
        else:
            print(f"{name} not found in cart.")

    def calculate_total(self):
        total = sum(details['price'] * details['quantity'] for details in self.cart.values())
        print(f"Total cost: ₹{total}")
        return total


# Menu-driven interface
def main():
    cart = ShoppingCart()

    while True:
        print("\n--- Shopping Cart Menu ---")
        print("1. Add Item")
        print("2. View Cart")
        print("3. Update Quantity")
        print("4. Remove Item")
        print("5. Calculate Total")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter quantity: "))
            cart.add_item(name, price, quantity)

        elif choice == "2":
            cart.view_cart()

        elif choice == "3":
            name = input("Enter item name to update: ")
            quantity = int(input("Enter new quantity: "))
            cart.update_quantity(name, quantity)

        elif choice == "4":
            name = input("Enter item name to remove: ")
            cart.remove_item(name)

        elif choice == "5":
            cart.calculate_total()

        elif choice == "6":
            print("Exiting... Thank you for shopping!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

