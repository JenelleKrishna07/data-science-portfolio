# inventory.py — Module 23 Final Submission (with feedback improvements)

shoe_list = []

class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (f"{self.product} ({self.code}) — {self.quantity} units @ R{self.cost:.2f} "
                f"from {self.country}")

def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # skip header
            for line in file:
                if line.strip() == "":
                    continue
                parts = line.strip().split(",")
                if len(parts) == 5:
                    country, code, product, cost, quantity = parts
                    try:
                        shoe = Shoe(country, code, product, float(cost), int(quantity))
                        shoe_list.append(shoe)
                    except ValueError:
                        print(f"⚠️ Invalid data on line: {line.strip()}")
                else:
                    print(f"⚠️ Malformed line skipped: {line.strip()}")
    except FileNotFoundError:
        print("❌ Error: 'inventory.txt' file not found.")

def capture_shoes():
    try:
        country = input("Enter country: ").strip()
        code = input("Enter shoe code: ").strip()
        product = input("Enter product name: ").strip()
        cost = float(input("Enter cost: "))
        quantity = int(input("Enter quantity: "))

        new_shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(new_shoe)
        print("✅ Shoe added.")
    except ValueError:
        print("❌ Please enter valid numbers for cost and quantity.")
        capture_shoes()

def view_all():
    if not shoe_list:
        print("📭 No shoes in inventory.")
    for shoe in shoe_list:
        print(shoe)

def re_stock():
    if not shoe_list:
        print("❌ No shoes to restock.")
        return
    lowest = min(shoe_list, key=lambda x: x.quantity)
    print(f"📉 Lowest stock item: {lowest}")
    confirm = input("Would you like to restock this item? (yes/no): ").strip().lower()
    if confirm == "yes":
        try:
            add = int(input(f"Enter quantity to add to {lowest.product}: "))
            lowest.quantity += add
            update_inventory_file()
            print("✅ Stock updated.")
        except ValueError:
            print("❌ Invalid number.")
    else:
        print("❌ Restock cancelled.")

def search_shoe():
    code = input("Enter shoe code to search: ").strip().lower()
    found = False
    for shoe in shoe_list:
        if shoe.code.strip().lower() == code:
            print("🔍 Found:", shoe)
            found = True
            break
    if not found:
        print("❌ Shoe not found.")

def value_per_item():
    for shoe in shoe_list:
        total = shoe.cost * shoe.quantity
        print(f"{shoe.product} ({shoe.code}) — Total Value: R{total:.2f}")

def highest_qty():
    if not shoe_list:
        print("❌ No shoes in stock.")
        return
    highest = max(shoe_list, key=lambda x: x.quantity)
    print(f"🛒 ON SALE: {highest.product} — {highest.quantity} units available!")

def update_inventory_file():
    try:
        with open("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                line = f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
                file.write(line)
    except Exception as e:
        print("❌ Error writing to inventory.txt:", e)

def main():
    read_shoes_data()
    while True:
        print("\n📦 Nike Inventory Menu")
        print("1 - View all shoes")
        print("2 - Add new shoe")
        print("3 - Restock lowest quantity")
        print("4 - Search shoe by code")
        print("5 - Show value per item")
        print("6 - Show highest stock item")
        print("7 - Exit")

        choice = input("Select an option (1–7): ").strip()
        if choice == "1":
            view_all()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            search_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            update_inventory_file()
            print("✅ Inventory saved. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please enter 1–7.")

if __name__ == "__main__":
    main()
