from evaluator import ExpressionEvaluator
from history import HistoryManager
from utils import clear_screen, print_banner

class CalculatorUI:
    def __init__(self):
        self.evaluator = ExpressionEvaluator()
        self.history = HistoryManager()

    def run(self):
        while True:
            clear_screen()
            print_banner()
            print("1. Perform Calculation")
            print("2. View History")
            print("3. Clear History")
            print("4. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                expr = input("Enter expression (e.g. 2 + 3 * 4): ")
                result = self.evaluator.evaluate(expr)
                print(f"Result: {result}")
                self.history.add_to_history(expr, result)
                input("Press Enter to continue...")
            elif choice == '2':
                self.history.show_history()
                input("Press Enter to continue...")
            elif choice == '3':
                self.history.clear_history()
                print("History cleared.")
                input("Press Enter to continue...")
            elif choice == '4':
                print("Thank you for using the calculator!")
                break
            else:
                print("Invalid choice.")
                input("Press Enter to continue...")
