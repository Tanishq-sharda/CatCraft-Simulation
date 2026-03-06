from Cat import Cat

def print_signature():
    print("Tanishq Sharda")

def get_int(prompt: str) -> int:
    """Safe integer input helper (view-side)."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def choose_cat(cats) -> int:
    """Return a valid cat index (0-based)."""
    while True:
        idx = get_int("Which cat? (1-3): ")
        if 1 <= idx <= len(cats):
            return idx - 1
        print("Invalid choice. Please pick from the numbered cats.")

def main():
    """
    View (UI) for CatCraft.
    - Talks to the user
    - Calls Cat methods
    - Catches exceptions
    - Does NOT access Cat instance variables directly :contentReference[oaicite:18]{index=18}
    """
    cats = [Cat("Anuska"), Cat("Lilly"), Cat("Siya")]

    print("Welcome to the World of CatCraft!")

    while True:
        print("\nCats in the world:")
        for i, cat in enumerate(cats, 1):
            print(f"{i}. {cat}")

        print("\n1. Feed\t2. Hit\t3. Night\t4. Quit")
        choice = get_int("Choice: ")

        if choice == 4:
            print("Goodbye! Exiting CatCraft...")
            break

        if choice == 1:
            cat_idx = choose_cat(cats)
            fish = get_int("How many fish? ")
            if fish < 0:
                print("Invalid number of fish. Enter a non-negative number.")
                continue

            try:
                cats[cat_idx].feed(fish)
                print("Purr!")  # view prints reactions; model stays silent :contentReference[oaicite:19]{index=19}
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 2:
            cat_idx = choose_cat(cats)
            try:
                cats[cat_idx].hit()
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 3:
            for cat in cats:
                if cat.night():
                    print(f"{cat.get_name()} left you a gift!")

        else:
            print("Invalid menu choice. Pick 1, 2, 3, or 4.")

if __name__ == "__main__":
    print_signature()
    main()
    