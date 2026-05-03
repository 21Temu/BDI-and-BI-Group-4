# mapper.py - Job 1: Extract product ID and rating
import sys
import json

# Read each line from input
for line in sys.stdin:
    try:
        # Parse JSON line
        review = json.loads(line)
        
        # Extract product ID (asin) and rating (overall)
        product_id = review.get('asin', 'unknown')
        rating = review.get('overall', 0)
        
        # Output: product_id \t rating
        # The tab separates key (product) from value (rating)
        print(f"{product_id}\t{rating}")
    except:
        # Skip lines that can't be parsed
        continue