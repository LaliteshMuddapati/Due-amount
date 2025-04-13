def due_amount(bill,paid):
    return paid-bill

bill=float(input("Enter the bill: "))
paid=float(input("Enter the paid amount: ")) 

print(due_amount(bill,paid))