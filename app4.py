expenses = []
running = True

while running:
    print("1. Add expenses")
    print("2. View expenses")
    print("3. View total")
    print("4. Exit")

    choice = int(input("Choose an option "))

    if choice == 1:
        newExpense = input("Enter a new expense: ")
        expenseAmount = float(input("Enter the amount: "))

        expenses.append({"desc": newExpense, "amount": expenseAmount})

    elif choice == 2:
        if not expenses:
            print("No expenses yet.")
        else:
            print("\nYour expenses:")
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. {expense['desc']} — ${expense['amount']:.2f}")
    elif choice == 3:
        total = 0
        for expense in expenses:
            total += expense["amount"]
        print(f"\nTotal is: ${total:.2f}")
    elif choice == 4:
        running = False
    else :
        print("Not an option!")