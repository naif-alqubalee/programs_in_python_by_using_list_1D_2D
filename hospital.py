# Program for hospital by using two dimension list 

# some empty lists
All_lists = []
lisname  = [] # name of patients
lisroom = [] # type_of_room
lisdays = [] # days
lisuntil_p = [] # price

# Notice
print("please, enter only two or three patients to try\n the program works on any number given to it but I mean to try it")

patients = int(input("Enter how many patients: "))
for k in range(patients):
    name = input("enter name: ")
    lisname.append(name)

    days = int(input("Enter how long does he need to stay here (days): "))
    lisdays.append(days)

    type_of_room = input("enter type of room A or B or C: ")
    lisroom.append(type_of_room)

    unitl_pr = float(input("Enter the price: "))
    lisuntil_p.append(unitl_pr)

# Add all lists in one list it name is All_lists
All_lists.append(lisname)
All_lists.append(lisroom)
All_lists.append(lisdays)
All_lists.append(lisuntil_p)

# amount
a = 0
amount = []
for l in All_lists[2] and All_lists[3]:
    amo = All_lists[2][a] * All_lists[3][a]
    amount.append(amo)
    a += 1

# # discount 
discount = []
z = 0
for v in All_lists[1]:
    if v == "A" or v == "a":
        discount1 = amount[z] * 0.1 # discount for room A
        discount.append(discount1)
    elif v == "B" or v == "b":
        discount2 = amount[z] * 0.1 # discount for room B
        discount.append(discount2)
    else:
        discount3 = amount[z] * 0.1 # discount for room C
        discount.append(discount3)
    z += 1

# Addresses for the table
print(f"name\ttype_room\tdays\tuntil_price\t   amount\tdiscount")
print("-"*70)

# to print the operetion
w,s,q = 0,0,0
for t in All_lists[0] and All_lists[1] and All_lists[2] and All_lists[3]:
    print(f"{All_lists[0][w]}\t   {All_lists[1][w]}\t\t{All_lists[2][w]}\t  {All_lists[3][w]}\t  {amount[s]}\t  {discount[q]}")
    w += 1
    s += 1
    q += 1

print("-"*70)

