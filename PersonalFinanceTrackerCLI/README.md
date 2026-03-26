# Personal Finance Tracker CLI

A simple CSV-based personal finance tracker built in Python.

## Project Structure

- `main.py` - interactive CLI loop, user commands and prompts.
- `service.py` - core `PersonalFinanceTracker` class with CSV persistence and business logic:
  - `transactions.csv` for income/expense entries
  - `budget.csv` for category budget limits

## Features

1. Add transaction (income or expense)
2. View all transactions
3. Set category budget and track limits
4. View summary (total income, total expenses, balance)
5. View spending by category with a simple bar chart text display
6. Show budget status (OK/Nearly over/OVER BUDGET)
7. Delete transaction by row index
8. Filter transactions by month or category
9. Export monthly summary to `summary_MM_YYYY.txt`


## Installation

1. Clone or download this repository
2. Install dependencies:
```bash
pip install colorama
```

## Usage

Run:
```bash
python main.py
```

Then enter one of the commands:
- `add` (prompts for type, category, amount, note)
- `view` (shows all transactions)
- `filter` (prompt month/category and value)
- `budget` (set category budget)
- `summary` (show totals, category stats, budget status)
- `export` (write text summary file)
- `delete` (remove a transaction by list index)
- `quit` (exit app)

## Data storage

- Transactions saved to `transactions.csv` with headers `Date,Type,Category,Amount,Note`.
- Budgets saved to `budget.csv` with headers `Category,Amount(P),Month`.

## Notes & improvements

- `delete` currently uses the displayed index, not transaction id.
- No unique transaction ID in file; index-based record deletion is used.
- Category and type input is case-insensitive but standardized to lower-case when validating.
- The app uses `colorama` for terminal color output.
- Add tests, input validation, and argument-based CLI parsing for non-interactive use as future enhancements.
