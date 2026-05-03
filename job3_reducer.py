# reducer.py - Job 3: Find top 10 most reviewed products
import sys

product_counts = {}

# Collect all counts
for line in sys.stdin:
    line = line.strip()
    product, count = line.split('\t')
    
    try:
        count = int(count)
    except:
        continue
    
    if product in product_counts:
        product_counts[product] += count
    else:
        product_counts[product] = count

# Sort by count (highest first) and take top 10
sorted_products = sorted(product_counts.items(), key=lambda x: x[1], reverse=True)

print("TOP 10 MOST REVIEWED PRODUCTS")
print("=" * 40)
print("Product ID\t\tReview Count")
print("-" * 40)

for i, (product, count) in enumerate(sorted_products[:10], 1):
    print(f"{i}. {product}\t{count}")