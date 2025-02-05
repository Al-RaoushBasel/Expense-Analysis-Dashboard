import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk  # For modern widgets like dropdowns
import main  # Importing functions from main.py


class ExpenseDashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Analysis Dashboard")
        self.root.geometry("800x600")
        self.root.configure(bg="#f8f9fa")

        # Initialize variables
        self.file_path = tk.StringVar()

        # Header
        header = tk.Label(
            root,
            text="💸 Expense Analysis Dashboard",
            font=("Arial", 20, "bold"),
            bg="#343a40",
            fg="#ffffff",
            padx=10,
            pady=10,
        )
        header.pack(fill=tk.X)

        # Main Content Frame
        main_frame = tk.Frame(root, bg="#f8f9fa", padx=10, pady=10)
        main_frame.pack(expand=True)

        # File Selection
        file_frame = tk.Frame(main_frame, bg="#f8f9fa")
        file_frame.pack(pady=10)
        tk.Label(file_frame, text="CSV File:", bg="#f8f9fa", font=("Arial", 12)).pack(
            side=tk.LEFT, padx=5
        )
        tk.Entry(
            file_frame, textvariable=self.file_path, font=("Arial", 12), width=50
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(
            file_frame,
            text="Browse",
            command=self.load_file,
            bg="#007bff",
            fg="#ffffff",
            font=("Arial", 12),
        ).pack(side=tk.LEFT, padx=5)

        # Buttons Frame
        button_frame = tk.Frame(main_frame, bg="#f8f9fa")
        button_frame.pack(expand=True)

        tk.Button(
            button_frame,
            text="View Total Spending",
            command=self.view_total_spending,
            bg="#28a745",
            fg="#ffffff",
            font=("Arial", 12),
            width=20,
        ).grid(row=0, column=0, padx=10, pady=10)

        tk.Button(
            button_frame,
            text="View Charts",
            command=self.view_charts,
            bg="#17a2b8",
            fg="#ffffff",
            font=("Arial", 12),
            width=20,
        ).grid(row=0, column=1, padx=10, pady=10)

        tk.Button(
            button_frame,
            text="Monthly Summary",
            command=self.view_monthly_summary,
            bg="#ffc107",
            fg="#343a40",
            font=("Arial", 12),
            width=20,
        ).grid(row=1, column=0, padx=10, pady=10)

        tk.Button(
            button_frame,
            text="Yearly Summary",
            command=self.view_yearly_summary,
            bg="#fd7e14",
            fg="#ffffff",
            font=("Arial", 12),
            width=20,
        ).grid(row=1, column=1, padx=10, pady=10)

        tk.Button(
            button_frame,
            text="Export Report",
            command=self.export_report,
            bg="#dc3545",
            fg="#ffffff",
            font=("Arial", 12),
            width=20,
        ).grid(row=2, column=0, columnspan=2, pady=10)

        # Status Area
        self.status = tk.Label(
            root,
            text="Welcome to the Expense Dashboard!",
            bg="#343a40",
            fg="#ffffff",
            font=("Arial", 10),
        )
        self.status.pack(fill=tk.X)

    def set_status(self, message):
        """Update the status area."""
        self.status.config(text=message)

    def load_file(self):
        """Load a CSV file."""
        file = filedialog.askopenfilename(
            filetypes=[("CSV Files", "*.csv")], title="Select Expense File"
        )
        if file:
            self.file_path.set(file)
            self.set_status(f"Loaded file: {file}")

    def view_total_spending(self):
        """View total spending in a pop-up."""
        if self.file_path.get():
            data = main.load_data(self.file_path.get())
            total_spending = data['Amount'].sum()
            messagebox.showinfo(
                "Total Spending", f"Your total spending is: ${total_spending:.2f}"
            )
            self.set_status("Displayed total spending.")
        else:
            messagebox.showerror("Error", "Please load a file first!")

    def view_charts(self):
        """View bar and pie charts."""
        if self.file_path.get():
            data = main.load_data(self.file_path.get())
            main.spending_by_category(data)
            main.interactive_pie_chart(data)
            self.set_status("Displayed charts.")
        else:
            messagebox.showerror("Error", "Please load a file first!")

    def view_monthly_summary(self):
        """View monthly summary."""
        if self.file_path.get():
            data = main.load_data(self.file_path.get())
            main.calculate_monthly_totals(data)
            self.set_status("Displayed monthly summary.")
        else:
            messagebox.showerror("Error", "Please load a file first!")

    def view_yearly_summary(self):
        """View yearly summary."""
        if self.file_path.get():
            data = main.load_data(self.file_path.get())
            main.calculate_yearly_totals(data)
            self.set_status("Displayed yearly summary.")
        else:
            messagebox.showerror("Error", "Please load a file first!")

    def export_report(self):
        """Export the summary report."""
        if self.file_path.get():
            data = main.load_data(self.file_path.get())
            main.export_category_summary(data)
            self.set_status("Exported report.")
        else:
            messagebox.showerror("Error", "Please load a file first!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseDashboardApp(root)
    root.mainloop()
