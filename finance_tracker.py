''' import necessary libraries '''
import csv
import os


def main():
    ''' prompt user for income/expense and print report '''
    print('Welcome to your Personal Finance Tracker 🏦')
    while True:
        transaction = input('What would you like to add? (Income/Expense): ').lower()
        if transaction in ['income', 'expense']:
            amount = input('Enter the amount: $')
            description = input('Enter the description: ')
            save_transaction(transaction, amount, description)
        elif transaction == 'report':
            print(f'The net balance is {generate_report()}')
            break
        else:
            print('Invalid input. Please try again!')

def save_transaction(type, amount, description):
    ''' Write to CSV '''
    headers = ['type', 'amount', 'description']
    with open('transactions.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        if os.stat('transactions.csv').st_size == 0:
            writer.writerow(headers)
        writer.writerow([type, amount, description])
        
def get_incomes():
    ''' Read from CSV and filter incomes '''
    with open('transactions.csv', encoding='utf-8') as file:
        reader = csv.reader(file)

        incomes = [row[1] for row in reader if row[0] == 'income']

        return incomes

def get_expenses():
    ''' Read from CSV and filter expenses '''
    with open('transactions.csv', encoding='utf-8') as file:
        reader = csv.reader(file)

        expenses = [row[1] for row in reader if row[0] == 'expense']

        return expenses

def generate_report():
    ''' Summarize incomes and expenses '''
    incomes = [float(amount) for amount in get_incomes()]
    expenses = [float(amount) for amount in get_expenses()]

    return sum(incomes) - sum(expenses)

if __name__ == "__main__":
    main()
