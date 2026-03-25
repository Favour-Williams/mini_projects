from service import PersonalFinanceTracker
from colorama import init, Fore, Style
init(autoreset=True)  

def main():
    tracker = PersonalFinanceTracker()
    try:
        tracker.load_file()
        while True:
            print(Style.BRIGHT + Fore.YELLOW + "Welcome to your Personal Finance Tracker")
            user_input = input(Fore.MAGENTA + "Enter service/command(add, delete, view, filter, budget, summary, quit): ")

            match user_input.lower():
                case "add":
                    print(Style.BRIGHT + Fore.CYAN + "============ ADD TRANSACTION ============")
                    typ = input("Enter type (income/expense): ")
                    category = input("Enter category (Food/Transport/Entertainment/Bills/Other):  ")
                    amount = input("Enter amount: ")
                    note = input("Enter a short note (or press Enter to skip): ")

                    try:
                        amount = float(amount)
                    except ValueError:
                        print(Fore.RED + "Amount must be a number.")
                        continue

                    tracker.add_transaction(typ, category, amount, note)
                    continue


                case "view":
                    print(Style.BRIGHT + Fore.CYAN + "================== VIEWING TRANSACTIONS ==================")
                    tracker.view_transactions()
                    print(Style.BRIGHT + Fore.CYAN + "================== DONE VIEWING TRANSACTIONS ==================")
                    continue


                case "budget":
                    category = input("Enter category (Food/Transport/Entertainment/Bills/Other):  ")
                    max_amt = input("Enter amount: ")
                    try:
                        max_amt = float(max_amt)
                    except ValueError:
                        print(Fore.RED + "Amount must be a number.")
                        continue
                    tracker.set_budget(category, max_amt)
                    continue


                case "summary":
                    print(Style.BRIGHT + Fore.CYAN + "================== VIEWING SUMMARY ==================")
                    tracker.view_summary()
                    continue


                case "delete":
                    print(Style.BRIGHT + Fore.CYAN + "===== DELETE A TRANSACTION =====")
                    tracker.delete_transaction()
                    continue

                case "filter":
                    moncat = input("Filter by (month/category): ")
                    typ = input(f"Enter {moncat}: ")

                    tracker.filter_transactions(moncat, typ)
                    continue
                    
                case "quit":
                    print("Goodbye!")
                    break
           
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting...")


if __name__ == "__main__":
    main()