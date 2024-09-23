# This is my string practice

# Here are the items in the customer's basket. Each item is a tuple
# of (item name, weight, price per kilograms).
basket = [
    ("Oranges", 2.0, 22000),
    ("Watermelon", 0.5, 12000),
    ("Snakefruit", 2.5, 10000)
]


# Calculate the total price for each item (weight times price per kilogram)
# and add them up to get a subtotal.
#
subtotal = 0
for item in basket:
    fruit, weight, unit_price = item
    subtotal += (weight * unit_price)


# Now calculate the sales tax and total bill.
#
tax_rate = 0.11  # 11% PPN
tax_amt = subtotal * tax_rate
total = subtotal + tax_amt


# Print the receipt for the customer.
#
print("Subtotal:    Rp{:>10}".format(subtotal))
print("Sales Tax:   Rp{:>10}".format(tax_amt))
print("Total:       Rp{:>10}".format(total))


#################################################

def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")

print(get_word("My name is Shofiyya Kheista Humairo", 3))