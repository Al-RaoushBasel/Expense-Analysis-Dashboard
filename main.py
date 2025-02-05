import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px  # For interactive visualizations

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


def calculate_monthly_totals(data):
    """Calculate and display monthly total spending."""
    monthly_totals = data.groupby(data['Date'].dt.to_period('M'))['Amount'].sum()
    print("\nMonthly Total Spending:")
    print(monthly_totals)
    monthly_totals.plot(kind='line', marker='o', title='Monthly Spending Trends')
    plt.xlabel('Month')
    plt.ylabel('Total Amount ($)')
    plt.grid()
    plt.tight_layout()
    plt.show()


def calculate_yearly_totals(data):
    """Calculate and display yearly total spending."""
    yearly_totals = data.groupby(data['Date'].dt.year)['Amount'].sum()
    print("\nYearly Total Spending:")
    print(yearly_totals)
    yearly_totals.plot(kind='bar', color='orange', title='Yearly Spending Trends')
    plt.xlabel('Year')
    plt.ylabel('Total Amount ($)')
    plt.tight_layout()
    plt.show()


def top_categories(data, period, value):
    """
    Display top 3 spending categories for a specific period (month/year).
    :param data: DataFrame containing expense data.
    :param period: 'month' or 'year' to specify the period type.
    :param value: Specific month (YYYY-MM) or year (YYYY) to filter data.
    """
    if period == 'month':
        filtered_data = data[data['Date'].dt.to_period('M') == value]
    elif period == 'year':
        filtered_data = data[data['Date'].dt.year == int(value)]
    else:
        print("Invalid period. Use 'month' or 'year'.")
        return

    if filtered_data.empty:
        print(f"No data found for the specified {period}: {value}")
        return

    category_totals = filtered_data.groupby('Category')['Amount'].sum()
    top_categories = category_totals.nlargest(3)
    print(f"\nTop 3 Categories for {period} {value}:")
    print(top_categories)
    top_categories.plot(kind='bar', title=f'Top Categories for {period.capitalize()} {value}', color='purple')
    plt.xlabel('Category')
    plt.ylabel('Total Amount ($)')
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
    print("4. View Monthly Spending Summary")
    print("5. View Yearly Spending Summary")
    print("6. View Top Categories for a Specific Month or Year")
    print("7. Export Category Spending to CSV")
    print("8. Exit")
    return input("Enter your choice (1-8): ")

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
            calculate_monthly_totals(data)
        elif choice == '5':
            calculate_yearly_totals(data)
        elif choice == '6':
            period = input("Enter period ('month' or 'year'): ").strip().lower()
            value = input(f"Enter the specific {period} (e.g., '2025-01' for month or '2025' for year): ").strip()
            top_categories(data, period, value)
        elif choice == '7':
            export_category_summary(data)
        elif choice == '8':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    print("This file is meant to contain logic and should be run only for testing.")

