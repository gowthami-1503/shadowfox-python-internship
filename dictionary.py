my_expenses={
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}
my_partner={
    "Hotel": 1000,
    "Food": 900,
    "Transportation":600,
    "Attractions":400,
    "Miscellaneous":150
}
my_total=sum(my_expenses.values())
my_partner_total=sum(my_partner.values())
print("my_total_expenses:",my_total);
print("my_partner_expenses:",my_partner_total);
if my_total>my_partner_total:
    print("I spent more money");
elif my_partner_total>my_total:
    print("My partner spent more");
else: 
    print("both spent the same amount.");
max_difference = 0
max_category = ""

for category in my_expenses:
    difference = abs(my_expenses[category] - my_partner[category])

    if difference > max_difference:
        max_difference = difference
        max_category = category

print("Highest spending difference is in:", max_category)
print("Difference amount:", max_difference)    
         