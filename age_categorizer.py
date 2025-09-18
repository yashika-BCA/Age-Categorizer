import tkinter as tk

# Function to determine age category and display result in a new window
def categorize_age():
    try:
        age = int(age_entry.get())  # Get age input

        # Define category and prefix based on age
        if age < 11:
            category, prefix = ("Children", "Aww, you are") if age >= 5 else ("Toddler", "Look at you, growing up fast!") if age >= 2 else ("Newborn", "Aww, welcome to the world, little one!")
        elif age < 20:
            category, prefix = ("Adult Teen", "Hey, you're officially a teenager adult!") if age >= 18 else ("Young Teenager", "You're stepping into the exciting teen phase!") if age >= 15 else ("Child Teen", "Enjoy your childhood, the teenage years are coming!")
        elif age >= 20:
            category, prefix = ("Young Adult", "You're thriving in your prime, chase your dreams!") if age < 30 else ("Adult", "Adulting at its finest! Balancing life with wisdom!") if age < 40 else ("Mid Aged", "You're in your peak years of experience!") if age < 50 else ("Old", "A lifetime of experiences, wisdom, and memories!") if age < 75 else ("Senior Citizen", "Bless us with your wisdom, you've seen the world!")
        else:
            category, prefix = ("Old", "Wow, you are")

        # Open new results window
        result_window = tk.Toplevel(root)
        result_window.title("Your Age Category")
        result_window.geometry("1000x800")
        result_window.configure(bg="#34495E")  # Dark theme for results

        # Display result with a styled label
        result_text = f"{prefix} {category}!"
        tk.Label(result_window, text=result_text, font=("Arial", 26, "bold"), fg="white", bg="#34495E").pack(expand=True)

        # Back Button to return to the main screen
        tk.Button(result_window, text="Back", font=("Arial", 16), bg="#E74C3C", fg="white", command=result_window.destroy).pack(pady=20)

    except ValueError:
        error_label.config(text="⚠️ Please enter a valid number!", fg="red")

# Create main window
root = tk.Tk()
root.title("Age Categorization")
root.geometry("600x400")
root.configure(bg="#2C3E50")  # Dark theme background

# Styling
font_large = ("Arial", 24, "bold")
font_medium = ("Arial", 18)
btn_style = {"font": font_medium, "bg": "#1ABC9C", "fg": "white", "activebackground": "#16A085", "padx": 20, "pady": 10}

# Centered Layout
frame = tk.Frame(root, bg="#2C3E50")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Label
tk.Label(frame, text="Enter your age:", font=font_large, fg="white", bg="#2C3E50").pack(pady=15)

# Entry field
age_entry = tk.Entry(frame, font=font_medium, width=15, justify="center", relief="solid", bd=3)
age_entry.pack(pady=10)

# Error Label for input validation
error_label = tk.Label(frame, text="", font=("Arial", 14), bg="#2C3E50")
error_label.pack(pady=5)

# Button to check category
tk.Button(frame, text="Check Category", command=categorize_age, **btn_style).pack(pady=20)

# Run the Tkinter loop
root.mainloop()
