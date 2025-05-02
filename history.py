import json
import os

class HistoryManager:
    def __init__(self):
        self.filename = "calc_history.json"

    def add_to_history(self, expression, result):
        history = self.load_history()
        history.append({"expression": expression, "result": result})
        with open(self.filename, "w") as f:
            json.dump(history, f, indent=4)

    def show_history(self):
        history = self.load_history()
        if not history:
            print("No history found.")
            return
        print("\n--- Calculation History ---")
        for item in history:
            print(f"{item['expression']} = {item['result']}")

    def clear_history(self):
        with open(self.filename, "w") as f:
            json.dump([], f)

    def load_history(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            return json.load(f)
