import pandas as pd
import matplotlib.pyplot as plt

# ===== Helper Functions =====

def load_data(file_path='data/expenses.csv'):
    """Load the expenses data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        data['Date'] = pd.to_datetime(data['Date'])  # Convert 'Date' column to datetime
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        exit()
    except KeyError:
        print("Error: The required columns ('Date', 'Category', 'Amount') are missing.")
        exit()


def display_total_spending(data):
    """Calculate and display the total spending."""
    total_spent = data['Amount'].sum()
    print(f"\nTotal Spending: ${total_spent:.2f}")


def spending_by_category(data):
    """Display a bar chart for spending by category."""
    category_spending = data.groupby('Category')['Amount'].sum()
    category_spending.plot(kind='bar', title='Spending by Category', color='skyblue')
    plt.xlabel('Category')
    plt.ylabel('Total Amount ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def daily_spending_trend(data):
    """Display a line chart for daily spending trends."""
    daily_spending = data.groupby('Date')['Amount'].sum()
    daily_spending.plot(kind='line', title='Daily Spending Over Time', marker='o', color='green')
    plt.xlabel('Date')
    plt.ylabel('Amount ($)')
    plt.grid()
    plt.tight_layout()
    plt.show()


def export_category_summary(data):
    """Export spending by category to a CSV file."""
    category_spending = data.groupby('Category')['Amount'].sum()
    category_spending.to_csv('data/category_spending_summary.csv')
    print("Category spending summary exported to 'data/category_spending_summary.csv'.")


def display_menu():
    """Display the main menu and return the user's choice."""
    print("\n======= Expense Analysis Dashboard =======")
    print("1. View Total Spending")
    print("2. View Spending by Category (Bar Chart)")
    print("3. View Daily Spending Trends (Line Chart)")
    print("4. Export Category Spending to CSV")
    print("5. Exit")
    return input("Enter your choice (1-5): ")

# ===== Main Program =====

def main():
    # Load data
    file_path = input("Enter the path to your expenses file (default: 'data/expenses.csv'): ")
    if not file_path.strip():
        file_path = 'data/expenses.csv'
    data = load_data(file_path)

    # Menu-driven interface
    while True:
        choice = display_menu()
        if choice == '1':
            display_total_spending(data)
        elif choice == '2':
            spending_by_category(data)
        elif choice == '3':
            daily_spending_trend(data)
        elif choice == '4':
            export_category_summary(data)
        elif choice == '5':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
