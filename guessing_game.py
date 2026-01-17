import tkinter as tk
from tkinter import messagebox
import random

# Game setup
number = random.randint(1, 100)
attempts = 0
max_attempts = 7

def check_guess():
    global attempts

    try:
        guess = int(entry.get())
    except:
        messagebox.showerror("Error", "Please enter a valid number!")
        return

    attempts += 1

    if guess == number:
        messagebox.showinfo("Congratulations ", f"You guessed the number in {attempts} attempts!")
        reset_game()
    elif attempts >= max_attempts:
        messagebox.showerror("Game Over ", f"You lost! The number was {number}")
        reset_game()
    elif guess < number:
        result_label.config(text="Too low! ")
    else:
        result_label.config(text="Too high! ")

def reset_game():
    global number, attempts
    number = random.randint(1, 100)
    attempts = 0
    entry.delete(0, tk.END)
    result_label.config(text="New game started!")

# GUI window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("350x300")
root.resizable(False, False)

tk.Label(root, text="Guess the number (1 to 100)", font=("Arial", 14)).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

tk.Button(root, text="Check Guess", font=("Arial", 12), command=check_guess).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

attempts_label = tk.Label(root, text="Max Attempts: 7", font=("Arial", 10))
attempts_label.pack()

tk.Button(root, text="Restart Game", font=("Arial", 10), command=reset_game).pack(pady=10)

root.mainloop()
