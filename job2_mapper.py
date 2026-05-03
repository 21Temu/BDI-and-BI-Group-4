# mapper.py - Job 2: Extract reviewer ID (count 1 per review)
import sys
import json

for line in sys.stdin:
    try:
        review = json.loads(line)
        
        # Extract reviewer ID
        reviewer_id = review.get('reviewerID', 'unknown')
        
        # Output: reviewer_id \t 1
        # Each review counts as 1 for that reviewer
        print(f"{reviewer_id}\t1")
    except:
        continue