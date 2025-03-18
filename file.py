#BASIC CURRENCY CONERTER
import requests
import tkinter as tk
from tkinter import messagebox, ttk

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    
    if "rates" in data and target_currency in data["rates"]:
        return data["rates"][target_currency]
    else:
        return None

def convert_currency():
    base_currency = base_currency_var.get().upper()
    target_currency = target_currency_var.get().upper()
    try:
        amount = float(amount_var.get())
        rate = get_exchange_rate(base_currency, target_currency)
        
        if rate:
            converted_amount = amount * rate
            result_var.set(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        else:
            messagebox.showerror("Error", "Invalid currency or data unavailable.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")

# UI Setup
root = tk.Tk()
root.title("Currency Converter")
root.attributes('-fullscreen', True)
root.configure(bg="#1C2833")

# Styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 14), padding=10)
style.configure("TEntry", font=("Arial", 14), padding=5)
style.configure("TLabel", font=("Arial", 16), background="#1C2833", foreground="white")

# Main frame
frame = tk.Frame(root, bg="#2C3E50", padx=40, pady=40)
frame.pack(expand=True)

title_label = tk.Label(frame, text="Currency Converter", font=("Arial", 30, "bold"), bg="#2C3E50", fg="#F4D03F")
title_label.pack(pady=20)

tk.Label(frame, text="Base Currency:", font=("Arial", 16), bg="#2C3E50", fg="white").pack(pady=5)
base_currency_var = tk.StringVar()
base_currency_entry = ttk.Entry(frame, textvariable=base_currency_var, font=("Arial", 14))
base_currency_entry.pack(pady=5)

tk.Label(frame, text="Target Currency:", font=("Arial", 16), bg="#2C3E50", fg="white").pack(pady=5)
target_currency_var = tk.StringVar()
target_currency_entry = ttk.Entry(frame, textvariable=target_currency_var, font=("Arial", 14))
target_currency_entry.pack(pady=5)

tk.Label(frame, text="Amount:", font=("Arial", 16), bg="#2C3E50", fg="white").pack(pady=5)
amount_var = tk.StringVar()
amount_entry = ttk.Entry(frame, textvariable=amount_var, font=("Arial", 14))
amount_entry.pack(pady=5)

convert_button = ttk.Button(frame, text="Convert", command=convert_currency)
convert_button.pack(pady=20)

result_var = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_var, font=("Arial", 18, "bold"), fg="#58D68D", bg="#2C3E50")
result_label.pack(pady=10)

exit_button = ttk.Button(frame, text="Exit", command=root.quit)
exit_button.pack(pady=10)

root.mainloop()
