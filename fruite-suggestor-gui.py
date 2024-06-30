import tkinter as tk
from tkinter import messagebox


disease_food_dict = {
    "diabetes": ["Leafy greens", "Whole grains", "Nuts", "Berries", "Fish"],
    "hypertension": ["Leafy greens", "Berries", "Red beets", "Oatmeal", "Bananas"],
    "anemia": ["Red meat", "Poultry", "Seafood", "Beans", "Dark leafy greens"],
    "osteoporosis": ["Dairy products", "Leafy greens", "Fish", "Nuts", "Tofu"],
    "constipation": ["Whole grains", "Fruits", "Vegetables", "Nuts", "Seeds"],
    "acid reflux": ["Bananas", "Melons", "Oatmeal", "Green vegetables", "Lean poultry"],
}


def get_recommendations():
    user_disease = disease_entry.get().strip().lower()
    if user_disease in disease_food_dict:
        recommended_foods = disease_food_dict[user_disease]
        recommendations = f"For {user_disease.capitalize()}, you should consider eating:\n"
        recommendations += "\n".join(f"- {food}" for food in recommended_foods)
    else:
        recommendations = "Sorry, we don't have food recommendations for that disease at the moment."

    messagebox.showinfo("Food Recommendations", recommendations)


root = tk.Tk()
root.title("Food Recommendation System")


title_label = tk.Label(root, text="Welcome to the Food Recommendation System!", font=("Helvetica", 16))
title_label.pack(pady=10)

instruction_label = tk.Label(root, text="Enter a disease to get food recommendations.", font=("Helvetica", 12))
instruction_label.pack(pady=5)

disease_entry = tk.Entry(root, font=("Helvetica", 14), width=30)
disease_entry.pack(pady=10)

recommend_button = tk.Button(root, text="Get Recommendations", font=("Helvetica", 14), command=get_recommendations)
recommend_button.pack(pady=20)


root.mainloop()
