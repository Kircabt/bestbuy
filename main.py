# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)


def start(store: Store):
    while True:
        print("\n--- Store Menu ---")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please enter your choice (1-4): ").strip()

        if choice == "1":
            print("\n--- Current Inventory ---")
            active_products = store.get_all_products()
            if not active_products:
                print("No active products available.")
            else:
                for idx, product in enumerate(active_products, start=1):
                    print(f"{idx}. {product.name} | Price: ${product.price:.2f} | Stock: {product.quantity}")

        elif choice == "2":
            total_qty = store.get_total_quantity()
            print(f"\nTotal items in store: {total_qty}")

        elif choice == "3":
            print("\n--- Place an Order ---")
            active_products = store.get_all_products()
            if not active_products:
                print("No products available to order.")
                continue

            shopping_list = []
            while True:
                # Show available products each time to pick from
                print("\nAvailable items:")
                for idx, product in enumerate(active_products, start=1):
                    print(f"{idx}. {product.name} (Stock: {product.quantity})")
                print("Press Enter without a number to finish adding items to your order.")

                prod_choice = input("Select product number to buy: ").strip()
                if not prod_choice:
                    break

                try:
                    prod_idx = int(prod_choice) - 1
                    if prod_idx < 0 or prod_idx >= len(active_products):
                        print("Invalid selection. Please choose a number from the list.")
                        continue

                    selected_product = active_products[prod_idx]

                    qty_choice = input(f"How many '{selected_product.name}' would you like? ").strip()
                    qty = int(qty_choice)

                    # Store tracking tuple
                    shopping_list.append((selected_product, qty))
                    print(f"Added {qty}x {selected_product.name} to your cart.")

                except ValueError:
                    print("Invalid input. Please enter numbers only.")

            if shopping_list:
                try:
                    total_price = store.order(shopping_list)
                    print(f"\nOrder complete! The total cost is: ${total_price:.2f}")
                except ValueError as error:
                    print(f"\nOrder Failed: {error}")
            else:
                print("Order canceled or empty cart.")

        elif choice == "4":
            print("Thank you for visiting! Goodbye.")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250.0, quantity=500)
    mac = Product("MacBook Air M2", price=1450.0, quantity=100)
    pixel = Product("Google Pixel 7", price=500.0, quantity=250)

    # Initialize store
    best_buy = Store([bose, mac, pixel])

    # Kick off interactive menu
    start(best_buy)
