# 💰 Budget Tracker (Python)

A simple command-line Budget Tracker built in **Python**, designed to help you log expenses, track your spending, and view your remaining budget in real-time. This project uses basic Python data structures and JSON for persistence (optional), making it beginner-friendly and highly extendable.

---

## 🚀 About the Project

This CLI-based budget tracker allows users to:

- Set an initial budget
- Add multiple expenses with descriptions
- See a breakdown of all expenses
- Track total spending and remaining balance

It's a lightweight project focused on **practical learning**, with clean code, modular functions, and easy-to-understand logic.

---

## 🧰 Tech Stack

- **Python 3.x**
- **JSON** for (optional) data persistence

---

## ✅ Features

- Add expenses with description and amount
- View:
  - Total budget
  - List of all expenses
  - Total spent
  - Remaining balance
- Input handling with a simple menu loop
- JSON-based load/save logic included (commented for optional use)

---

## 📝 Code Structure

- `add_expense()` – Adds an expense entry  
- `get_total_expenses()` – Calculates total amount spent  
- `get_balance()` – Computes remaining budget  
- `show_budget_details()` – Prints budget summary  
- `load_budget_data()` – (Optional) Loads data from a JSON file  
- `save_budget_data()` – (Optional) Saves data to a JSON file  
- `main()` – Runs the program interactively via terminal

---

## 📦 How to Run

### 🔧 Requirements

- Python 3.x installed

### ▶️ Steps

1. Clone the repository or copy the script into a `.py` file
2. Open your terminal and navigate to the file directory
3. Run the program:

```bash
python budget_tracker.py
```

4. Follow the on-screen instructions to add expenses and view your budget

---

## 💡 Future Improvements

- Enable saving and loading data using JSON (already included, just uncomment)
- Add category-based expense tracking (e.g. Food, Travel, Shopping)
- Add monthly reports or bar chart summaries
- Build a GUI using Tkinter or a web version using Flask

---

## 📄 License

This is a personal project built for hands-on practice. Feel free to use or modify it for learning purposes.

---

Let me know if you'd like to upload this to GitHub with a preview GIF or CLI screenshot!
