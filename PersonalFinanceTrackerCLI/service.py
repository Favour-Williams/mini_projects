import csv
import os
from datetime import date  


class PersonalFinanceTracker:
    def __init__(self, file1="transactions.csv", file2="budget.csv")->None:
        self.file1 = file1
        self.file2 = file2


    def load_file(self)->None:
        transactions_headers = ['Date', 'Type', 'Category', 'Amount', 'Note']
        budget_headers = ['Category', 'Amount(P)', 'Month']

        if not os.path.exists(self.file1) :
            with open(self.file1, 'w', newline='') as csvfile1:
                writer1 = csv.DictWriter(csvfile1, fieldnames=transactions_headers)
                writer1.writeheader()

        if not os.path.exists(self.file2) :
            with open(self.file2, 'w', newline='') as csvfile2:

                writer2 = csv.DictWriter(csvfile2, fieldnames=budget_headers)
                writer2.writeheader()

    def add_transaction(self, typ, category, amount, note=None):
        types = ["income", "expense"]
        categories = ["food", "transport", "entertainment", "bills", "other"]

        if typ.lower() not in types:
            print("Types has to be income or expense thank you.")
            return 
        if category.lower() not in categories:
            print("Category has to be Food/Transport/Entertainment/Bills/Other thank you.")
            return
        today = date.today()
        transaction_data = [today, typ, category, amount, note]

        with open(self.file1, 'a', newline='') as csvfile1:
            csvwriter1 = csv.writer(csvfile1)
            csvwriter1.writerow(transaction_data)
        print('Transaction saved!')

    def view_transactions(self):
        with open(self.file1, 'r', newline='') as csvfile1:
            csvFile1 = csv.reader(csvfile1)
            next(csvFile1)
            print(f'{"Date":<12} {"Type":<10} {"Category":<15} {"Amount":<10} {"Note":<20}')
            print("-" * 67)
            for line in csvFile1:
                print(f'{line[0]:<12} {line[1]:<10} {line[2]:<15} {line[3]:<10} {line[4]:<20}')
        
    def set_budget(self, category, max_amt):
        categories = ["food", "transport", "entertainment", "bills", "other"]

        if category.lower() not in categories:
            print("Category has to be Food/Transport/Entertainment/Bills/Other thank you.")
            return
        

        today = date.today()
        month =  today.month

        budget_data = [category, max_amt, month]

        with open(self.file2, 'a', newline='') as csvfile2:
            csvwriter2 = csv.writer(csvfile2)
            csvwriter2.writerow(budget_data)
        print('Budget saved!')

    def view_summary(self):
        total_income = 0.0
        total_expenses = 0.0
        category_totals = {}
        budget_limits = {}

        with open(self.file1, 'r', newline='') as csvfile1, open(self.file2, 'r', newline='') as csvfile2:

            csvFile1 = csv.reader(csvfile1)
            next(csvFile1)  

            csvFile2 = csv.reader(csvfile2)
            next(csvFile2)  

            for line in csvFile1:
                amount = float(line[3])
                
                if line[1].lower() == "income":
                    total_income += amount
                elif line[1].lower() == "expense":
                    total_expenses += amount
                    cat = line[2].lower()
                    category_totals[cat] = category_totals.get(cat, 0.0) + amount
            
            print(f'Total Income:      P {total_income:.2f}')
            print(f'Total Expenses:    P {total_expenses:.2f}')
            print(f'Balance:           P {total_income - total_expenses:.2f}')

            print(f'\n')

            print('--- Spending by Category ---')
            for key, value in category_totals.items():
                print(f'{key}      P{value:.2f}')


            for line in csvFile2:
                cat = line[0].lower()    
                limit = float(line[1])   
                budget_limits[cat] = limit

            
            print('--- Budget Status ---')
            for cat, spent in category_totals.items():
                if cat in budget_limits:      
                    limit = budget_limits[cat]
                    percentage = (spent / limit) * 100
                    if spent > limit:
                        status = "⚠️  OVER BUDGET"
                    elif percentage >= 80:
                        status = "⚠️  Nearly over"
                    else:
                        status = "✅"
                    print(f'{cat}: spent P{spent:.2f} of P{limit:.2f}  {status}')
                    
        



