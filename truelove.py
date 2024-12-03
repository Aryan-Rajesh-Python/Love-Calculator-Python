import pyfiglet
import random
import tkinter as tk
from tkinter import messagebox

# Fun Love Quotes
love_quotes = [
    "Love is not about how many days you’ve been together, it’s about how much you love each other.",
    "A true relationship is two imperfect people refusing to give up on each other.",
    "In all the world, there is no heart for me like yours. In all the world, there is no love for you like mine.",
    "Love is the only reality, and it is not a mere sentiment. It is the ultimate truth at the heart of creation."
]

# Zodiac Compatibility Function
def zodiac_compatibility(birthday1, birthday2):
    # Zodiac signs based on date ranges (simplified)
    zodiac_signs = {
        "Aries": (3, 21, 4, 19),
        "Taurus": (4, 20, 5, 20),
        "Gemini": (5, 21, 6, 20),
        "Cancer": (6, 21, 7, 22),
        "Leo": (7, 23, 8, 22),
        "Virgo": (8, 23, 9, 22),
        "Libra": (9, 23, 10, 22),
        "Scorpio": (10, 23, 11, 21),
        "Sagittarius": (11, 22, 12, 21),
        "Capricorn": (12, 22, 1, 19),
        "Aquarius": (1, 20, 2, 18),
        "Pisces": (2, 19, 3, 20)
    }

    def get_zodiac(month, day):
        for sign, (start_month, start_day, end_month, end_day) in zodiac_signs.items():
            if ((month == start_month and day >= start_day) or (month == end_month and day <= end_day)):
                return sign
        return None

    month1, day1 = map(int, birthday1.split("-"))
    month2, day2 = map(int, birthday2.split("-"))

    zodiac1 = get_zodiac(month1, day1)
    zodiac2 = get_zodiac(month2, day2)

    compatibility = {
        ("Aries", "Leo"): 90,
        ("Taurus", "Virgo"): 85,
        ("Gemini", "Aquarius"): 80,
        ("Cancer", "Pisces"): 75,
        ("Libra", "Sagittarius"): 70,
        # Add more combinations
    }

    score = compatibility.get((zodiac1, zodiac2), 50)
    return score

# Fun Name Compatibility (Counts letters in the names)
def name_compatibility(name1, name2):
    name3 = name1 + name2
    count1 = 0
    count2 = 0
    for i in name3:
        if i.lower() in "true":
            count1 += 1
        if i.lower() in "love":
            count2 += 1
    count3 = str(count1) + str(count2)
    return int(count3)

# Main Love Calculator Function
def love_calculator():
    name1 = entry_name1.get()
    name2 = entry_name2.get()

    if not name1 or not name2:
        messagebox.showerror("Error", "Please enter both names.")
        return

    # Get Zodiac Compatibility Score
    birthday1 = entry_birthday1.get()
    birthday2 = entry_birthday2.get()
    zodiac_score = zodiac_compatibility(birthday1, birthday2)

    # Get Name Compatibility Score
    name_score = name_compatibility(name1, name2)

    # Combine both scores
    final_score = (name_score + zodiac_score) // 2  # Averaging both scores

    # Generate Final Message
    if final_score < 10 or final_score > 90:
        result = f"Your score is {final_score}, you go together like coke and mentos!"
    elif 40 < final_score < 50:
        result = f"Your score is {final_score}, you are alright together!"
    else:
        result = f"Your score is {final_score}."

    # Show a Love Quote
    quote = random.choice(love_quotes)

    # Display Results in the GUI
    result_label.config(text=result)
    quote_label.config(text=quote)

# Set up the GUI with tkinter
window = tk.Tk()
window.title("Love Calculator")
window.geometry("400x400")

# Create a banner with pyfiglet
banner = pyfiglet.figlet_format("Love Calculator")
banner_label = tk.Label(window, text=banner, font=("Courier", 10))
banner_label.pack()

# Name Inputs
tk.Label(window, text="Enter your name:").pack()
entry_name1 = tk.Entry(window)
entry_name1.pack()

tk.Label(window, text="Enter your partner's name:").pack()
entry_name2 = tk.Entry(window)
entry_name2.pack()

# Birthdate Inputs
tk.Label(window, text="Enter your birthdate (MM-DD):").pack()
entry_birthday1 = tk.Entry(window)
entry_birthday1.pack()

tk.Label(window, text="Enter your partner's birthdate (MM-DD):").pack()
entry_birthday2 = tk.Entry(window)
entry_birthday2.pack()

# Calculate Button
calculate_button = tk.Button(window, text="Calculate Compatibility", command=love_calculator)
calculate_button.pack()

# Result and Quote Labels
result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack()

quote_label = tk.Label(window, text="", font=("Arial", 12, "italic"))
quote_label.pack()

# Run the GUI loop
window.mainloop()
