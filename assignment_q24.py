from collections import deque

available_restaurants = ["Umucyo Resto", "Solution Resto", "Obina Resto"]
request = deque()
returned = []

def show_restaurants():
   
    print("Available Restaurants:")
    for restaurant in available_restaurants:
        print(f"- {restaurant}")

def place_order(restaurant, order_details):
    if restaurant not in available_restaurants:
        print(f"Restaurant {restaurant} is not available.")
        return
    
    order = (restaurant, order_details)
    request.append(order)
    returned.append(order)
    print(f"Order placed: {order}")

def returne():
    
    if returned:
        last_order = returned.pop()
        request.remove(last_order)
        print(f"Order returned: {last_order}")
    else:
        print("No orders to undo.")

def deliver_order():
    
    if request:
        order = request.popleft()
        print(f"Delivering order: {order}")
    else:
        print("No orders to deliver.")

def show_orders():
    
    print("Current Orders :")
    for order in request:
        print(order)

def main():
   
    while True:
        print("\nMenu:")
        print("1. Show Available Restaurants")
        print("2. Place Order")
        print("3. return our Order")
        print("4. Deliver Order")
        print("5. Show Current Orders")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            show_restaurants()
        elif choice == '2':
            restaurant = input("Enter restaurant name: ")
            order_details = input("Enter things you want to order: ")
            place_order(restaurant, order_details)
        elif choice == '3':
            returne()
        elif choice == '4':
            deliver_order()
        elif choice == '5':
            show_orders()
        elif choice == '6':
            print("Exiting the service.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
