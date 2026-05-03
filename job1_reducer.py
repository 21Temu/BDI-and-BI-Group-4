# reducer.py - Job 1: Calculate average rating per product
import sys

current_product = None
total_rating = 0
count = 0

# Read each line from mapper output
for line in sys.stdin:
    # Remove extra spaces
    line = line.strip()
    
    # Split the line into product and rating
    product, rating = line.split('\t')
    
    # Convert rating to float
    try:
        rating = float(rating)
    except:
        continue
    
    # If we're still on the same product
    if current_product == product:
        total_rating += rating
        count += 1
    else:
        # If this is a new product, output the previous product's average
        if current_product is not None:
            average = total_rating / count
            print(f"{current_product}\t{average:.2f}\t{count}")
        
        # Start new product
        current_product = product
        total_rating = rating
        count = 1

# Output the last product
if current_product is not None:
    average = total_rating / count
    print(f"{current_product}\t{average:.2f}\t{count}")