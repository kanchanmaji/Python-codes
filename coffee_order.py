# =========================
# ANSI COLOR CODES
# =========================
RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"


# =========================
# Coffee Class
# =========================
class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# =========================
# Order Class
# =========================
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"{GREEN}✔ Added {coffee.name} to your cart{RESET}")

    def total(self):
        return sum(item.price for item in self.items)

    def show_order(self):
        if not self.items:
            print(f"{RED}✖ No item in cart{RESET}")
            return

        print(f"\n{CYAN}{BOLD}➤ Your Order{RESET}")
        print(f"{CYAN}{'-' * 30}{RESET}")

        for i, item in enumerate(self.items, 1):
            print(f"{YELLOW}→ {i}. {item.name:<12} ₹{item.price}{RESET}")

        print(f"{CYAN}{'-' * 30}{RESET}")
        print(f"{BOLD}Total: ₹{self.total()}{RESET}")

    def checkout(self):
        if not self.items:
            print(f"{RED}✖ No item in cart{RESET}")
            return

        self.show_order()
        confirm = input(f"{BLUE}Confirm order? (yes/no): {RESET}").strip().lower()

        if confirm == "yes":
            print(f"{GREEN}{BOLD}✔ Order placed successfully ☕{RESET}")
            self.items.clear()
        else:
            print(f"{YELLOW}⚠ Checkout cancelled{RESET}")


# =========================
# Main Program
# =========================
def main():
    menu = [
        Coffee("Chai", 20),
        Coffee("Matcha", 40),
        Coffee("Espresso", 80),
        Coffee("Coffee", 30)
    ]

    order = Order()

    while True:
        print(f"\n{CYAN}{'=' * 35}{RESET}")
        print(f"{CYAN}{BOLD}      ☕ COFFEE MENU ☕{RESET}")
        print(f"{CYAN}{'=' * 35}{RESET}")

        for i, coffee in enumerate(menu, 1):
            print(f"{YELLOW}➤ {i}. {coffee.name:<10} ₹{coffee.price}{RESET}")

        print(f"\n{BLUE}➤ 5. View Order{RESET}")
        print(f"{BLUE}➤ 6. Checkout{RESET}")
        print(f"{BLUE}➤ 7. Exit{RESET}")

        choice = input(f"\n{BOLD}Select option (1–7): {RESET}").strip()

        if choice in ['1', '2', '3', '4']:
            order.add_item(menu[int(choice) - 1])

        elif choice == '5':
            order.show_order()

        elif choice == '6':
            order.checkout()

        elif choice == '7':
            print(f"{GREEN}Thank you for visiting ☕{RESET}")
            break

        else:
            print(f"{RED}✖ Invalid choice. Try again!{RESET}")


# =========================
# Entry Point
# =========================
if __name__ == "__main__":
    main()