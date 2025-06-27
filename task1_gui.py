import tkinter as tk
from tkinter import ttk


def convert():
    try:
        value = float(entry_temp.get())
        unit = combo_unit.get()

        if unit == "Celsius":
            f = (value * 9/5) + 32
            k = value + 273.15
        elif unit == "Fahrenheit":
            f = value
            k = (value - 32) * 5/9 + 273.15
            value = (value - 32) * 5/9
        elif unit == "Kelvin":
            k = value
            value = value - 273.15
            f = (value * 9/5) + 32

        label_result.config(text=f"Celsius: {value:.2f} °C\n\nFahrenheit: {f:.2f} °F\n\nKelvin: {k:.2f} K")
    except ValueError:
        label_result.config(text="Invalid input!")

# GUI setup
root = tk.Tk()
root.geometry("600x600")
root.configure(bg="#F1F0A4")
root.title("Temperature Converter")

tk.Label(root, text="Enter Temperature:",font=('GEORGIA',20)).pack(anchor=tk.W,padx=100, pady=10)
entry_temp = tk.Entry(root, font=('Georgia', 16), width=30)
entry_temp.pack(padx=30)

tk.Label(root, text="Select Unit:",font=('GEORGIA',20)).pack(anchor=tk.W,padx=100, pady=10)
combo_unit = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"] ,font=('Georgia', 16), width=29)
combo_unit.set("Celsius")
combo_unit.pack()

tk.Button(root, text="Convert", command=convert ,font=('GEORGIA',20)).pack(pady=10)
label_result = tk.Label(root, text="", font=("Arial", 18))
label_result.pack()

root.mainloop()
