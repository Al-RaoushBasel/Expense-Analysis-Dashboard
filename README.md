# 💸 Expense Analysis Dashboard

**Expense Analysis Dashboard** is a Python-based tool with an interactive GUI that helps you analyze expenses, track spending habits across categories, and visualize trends through dynamic charts.

## 🌟 Features

- **📄 CSV File Input:** Analyze expenses from a provided CSV file.
- **💵 Total Spending Calculation:** Get insights into your overall expenditure.
- **📂 Category-Based Analysis:** Organize and analyze spending by categories (e.g., Groceries, Bills, Entertainment).
- **📊 Visual Trends:** Generate bar charts (spending by category) and line charts (daily spending trends).
- **📅 Monthly and Yearly Summaries:** View summarized expenses for any month or year.
- **📋 Interactive GUI:** Modern, user-friendly interface with pop-ups for results.
- **💾 Export Feature:** Save detailed reports and summaries to a CSV file.
- **🧹 Error Handling:** Provides meaningful error messages for missing or invalid files.

## 📥 Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Al-RaoushBasel/Expense-Analysis-Dashboard.git
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd Expense-Analysis-Dashboard
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *Ensure you have Python 3 installed.*
4. **Run the Project:**
   ```bash
   python main.py
   ```

## 📱 Usage

1. **Upload File:** Use the default `expenses.csv` file located in the `data` directory, or provide your own CSV file. The CSV should contain the following columns:
   - `Date` (e.g., 2025-01-01)
   - `Category` (e.g., Groceries, Entertainment)
   - `Description` (e.g., Supermarket, Movie Tickets)
   - `Amount` (e.g., 45.00)

2. **Analyze Expenses:** Use the interactive GUI to:
   - View **Total Spending**: Displays a pop-up showing the total expenditure.
   - View **Spending by Category**: Generates a bar chart to visualize category-based spending.
   - View **Daily Spending Trends**: Generates a line chart to show how your spending evolves over time.
   - View **Monthly Summary**: Summarizes your spending for a selected month.
   - View **Yearly Summary**: Summarizes your spending for a selected year.

3. **Export Report:** Save detailed summaries and analyses to a CSV file.

4. **Error Handling:** The tool provides feedback for invalid or missing files, ensuring a smooth user experience.

## 🛠️ Technologies Used

- **Python:** Main programming language.
- **Pandas:** Data manipulation and analysis.
- **Matplotlib:** Visualizations.
- **Tkinter:** For creating a professional, interactive GUI.
- **CSV:** File format for data input.

## 📸 Screenshots

Here are some snapshots of the Expense Analysis Dashboard in action:

### 1. **Dashboard Overview**
![image](https://github.com/user-attachments/assets/9db61d8d-d713-4347-96e0-504a4082ee47)
*Description: The main interface of the application, showing various options for analyzing expenses.*

---

### 2. **Spending by Category**
![image](https://github.com/user-attachments/assets/b8547c75-751d-4e02-af86-411912c53190)
*Description: A bar chart visualization displaying expenses categorized by type.*

---

### 3. **Monthly Summary**
![image](https://github.com/user-attachments/assets/a7342c73-4099-41d6-9efa-0ca5bfa9ccd3)
*Description: A detailed monthly spending summary for easy tracking and budgeting.*
