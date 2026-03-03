my_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}
my_total = sum(my_expenses.values());
partner_total = sum(partner_expenses.values());

print("Your my expense:", my_total)
print("Partner total expense:", partner_total)
if my_total > partner_total:
    print("You spent more money.");
elif partner_total > my_total:
    print("Your partner spent more money.");
else:
    print("Both spent the same amount.");
    # ... (your dictionary definitions and initial prints)

# Define these BEFORE the loop starts
max_difference = 0
max_category = ""

for category in my_expenses:
    # Everything inside the loop MUST be indented
    difference = abs(my_expenses[category] - partner_expenses[category])
    
    if difference > max_difference:
        max_difference = difference
        max_category = category

print("Highest spending difference is in:", max_category)
print("Difference amount:", max_difference)

