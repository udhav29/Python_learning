print(" Billing Program ")
bill_items = []

while True:
    print("\nOptions:")
    print("1. Create Bill (Add Item)")
    print("2. Display Item Price and Total Bill Amount")
    print("3. Display Grand Total")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item_name = input("Enter item name: ")
        while True:
            try:
                item_price = float(input(f"Enter price for {item_name}: "))
                if item_price < 0:
                    print("Price cannot be negative. Please enter a valid price.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number for the price.")
        
        while True:
            try:
                item_quantity = int(input(f"Enter quantity for {item_name}: "))
                if item_quantity < 1:
                    print("Quantity must be at least 1. Please enter a valid quantity.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter an integer for the quantity.")
        
        bill_items.append({'name': item_name, 'price': item_price, 'quantity': item_quantity})
        print(f"'{item_name}' added to the bill.")

    elif choice == '2':
        if not bill_items:
            print("No items in the bill yet. Please add items first.")
            continue

        print("\n--- Current Bill ---")
        sub_total = 0
        print(f"{'Item':<20} {'Price':<10} {'Quantity':<10} {'Subtotal':<10}")
        print("-" * 50)
        for item in bill_items:
            item_subtotal = item['price'] * item['quantity']
            print(f"{item['name']:<20} {item['price']:<10.2f} {item['quantity']:<10} {item_subtotal:<10.2f}")
            sub_total += item_subtotal
        print("-" * 50)
        print(f"{'Total Amount:':<40} {sub_total:<10.2f}")

    elif choice == '3':
        if not bill_items:
            print("No items in the bill yet.")
            grand_total = 0
        else:
            grand_total = sum(item['price'] * item['quantity'] for item in bill_items)
        
        print(f"\nGrand Total of the bill: {grand_total:.2f}")

    elif choice == '4':
        print("Exiting billing program. Thank you!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
