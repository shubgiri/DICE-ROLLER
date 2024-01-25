import tkinter as tk
import random


class DiceRoller:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Rolling Simulator")

        self.result_label = tk.Label(root, text="", font=("Helvetica", 20))
        self.result_label.pack(pady=20)

        self.roll_button = tk.Button(root, text="Roll Dice", command=self.roll_dice, font=("Helvetica", 14))
        self.roll_button.pack()

    def roll_dice(self):
        dice_result = random.randint(1, 6)
        self.result_label.config(text=f"Result: {dice_result}")


if __name__ == "__main__":
    root = tk.Tk()
    dice_roller = DiceRoller(root)
    root.mainloop()
