from service import PersonalFinanceTracker

def main():
    tracker = PersonalFinanceTracker()
    try:
        tracker.load_file()
        while True:
            print("Welcome to your Personal Finance Tracker")
            user_input = input("Enter service/command(add, view, budget, summary, quit): ")

            match user_input.lower():
                case "add":
                    print("============ ADD TRANSACTION ============")
                    typ = input("Enter type (income/expense): ")
                    category = input("Enter category (Food/Transport/Entertainment/Bills/Other):  ")
                    amount = input("Enter amount: ")
                    note = input("Enter a short note (or press Enter to skip): ")

                    try:
                        amount = float(amount)
                    except ValueError:
                        print("Amount must be a number.")
                        continue

                    tracker.add_transaction(typ, category, amount, note)
                    continue


                case "view":
                    print("================== VIEWING TRANSACTIONS ==================")
                    tracker.view_transactions()
                    print("================== DONE VIEWING TRANSACTIONS ==================")
                    continue


                case "budget":
                    category = input("Enter category (Food/Transport/Entertainment/Bills/Other):  ")
                    max_amt = input("Enter amount: ")
                    try:
                        max_amt = float(max_amt)
                    except ValueError:
                        print("Amount must be a number.")
                        continue
                    tracker.set_budget(category, max_amt)
                    continue


                case "summary":
                    print("================== VIEWING SUMMARY ==================")
                    tracker.view_summary()
                    continue

                    
                case "quit":
                    print("Goodbye!")
                    break
           
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting...")


if __name__ == "__main__":
    main()