# A soft drink company recently surveyed 12,467 of its customers and found that approximately 14% of those surveyed purchase one or more energy drinks per week.
# Of those customers who purchase energy drinks, approximately 64% of them prefer citrus-flavored energy drinks.
# Write a program that displays the following:
# - The approximate number of customers in the survey who purchase one or more energy drinks per week
# - The approximate number of customers in the survey who prefer citrus-flavored energy drinks

# variables
customers_surveyed = 12467
percent_who_purchase_one_or_more = 0.14
percent_who_prefer_citrus_flavored = 0.64

# calculate how many customers purchase 1 or more energy drinks per week
number_of_customers_who_purchase_one_or_more = int(customers_surveyed * percent_who_purchase_one_or_more)

# display the result
print(f"Number of customers surveyed who purchase one or more energy drinks per week: {number_of_customers_who_purchase_one_or_more}")

# calculate how many customers prefer citrus-flavored energy drinks
number_of_customers_who_prefer_citrus_flavored = int(customers_surveyed * percent_who_prefer_citrus_flavored)

# display the result
print(f"Number of customers surveyed who prefer citrus-flavored energy drinks: {number_of_customers_who_prefer_citrus_flavored}")