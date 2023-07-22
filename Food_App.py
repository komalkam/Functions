class FoodItem:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class FoodOrderingApp:
    def __init__(self):
        self.food_items = []
        self.users = {}
        self.orders = []

    def add_food_item(self, name, quantity, price, discount, stock):
        food_id = len(self.food_items) + 1
        new_food_item = FoodItem(food_id, name, quantity, price, discount, stock)
        self.food_items.append(new_food_item)

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                break

    def view_food_items(self):
        for food_item in self.food_items:
            print(f"FoodID: {food_item.food_id}, Name: {food_item.name}, Quantity: {food_item.quantity}, "
                  f"Price: {food_item.price}, Discount: {food_item.discount}, Stock: {food_item.stock}")

    def remove_food_item(self, food_id):
        self.food_items = [food_item for food_item in self.food_items if food_item.food_id != food_id]

    def register_user(self, full_name, phone_number, email, address, password):
        self.users[email] = {
            'full_name': full_name,
            'phone_number': phone_number,
            'address': address,
            'password': password
        }

    def login_user(self, email, password):
        if email in self.users and self.users[email]['password'] == password:
            return True
        return False

    def place_order(self, user_email, selected_items):
        order_details = {
            'user_email': user_email,
            'selected_items': selected_items
        }
        self.orders.append(order_details)

    def view_order_history(self, user_email):
        print(f"Order History for {user_email}:")
        for order in self.orders:
            if order['user_email'] == user_email:
                selected_items = ", ".join([self.food_items[item - 1].name for item in order['selected_items']])
                print(f"Items: {selected_items}")

    def update_user_profile(self, email, full_name, phone_number, address, password):
        if email in self.users:
            self.users[email]['full_name'] = full_name
            self.users[email]['phone_number'] = phone_number
            self.users[email]['address'] = address
            self.users[email]['password'] = password


def main():
    app = FoodOrderingApp()

 
    app.add_food_item("Tandoori Chicken", "4 pieces", 240, 10, 50)
    app.add_food_item("Vegan Burger", "1 Piece", 320, 5, 20)
    app.add_food_item("Truffle Cake", "500gm", 900, 15, 30)

    app.view_food_items()
    app.edit_food_item(2, "Veggie Burger", "1 Piece", 350, 8, 25)
    app.view_food_items()

    app.remove_food_item(3)
    app.view_food_items()

   
    app.register_user("Komal Kamble", "1234567890", "Komal@example.com", "123 Main St", "password123")
    
    if app.login_user("Komal@example.com", "password123"):
        print("Login Successful!")
    else:
        print("Invalid Credentials!")

    app.place_order("Komal@example.com", [2, 3])
    app.view_order_history("Komal@example.com")

    app.update_user_profile("Komal@example.com", "Komal Kamble", "9876543210", "456 Park Ave", "newpassword123")

if __name__ == "__main__":
    main()
