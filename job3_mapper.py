# mapper.py - Job 3: Count reviews per product
import sys
import json

for line in sys.stdin:
    try:
        review = json.loads(line)
        
        # Extract product ID
        product_id = review.get('asin', 'unknown')
        
        # Output: product_id \t 1
        print(f"{product_id}\t1")
    except:
        continue