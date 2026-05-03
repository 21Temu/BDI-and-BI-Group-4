# reducer.py - Job 2: Count total reviews per user
import sys

current_user = None
total_reviews = 0

for line in sys.stdin:
    line = line.strip()
    user, count = line.split('\t')
    
    try:
        count = int(count)
    except:
        continue
    
    if current_user == user:
        total_reviews += count
    else:
        if current_user is not None:
            print(f"{current_user}\t{total_reviews}")
        
        current_user = user
        total_reviews = count

# Output last user
if current_user is not None:
    print(f"{current_user}\t{total_reviews}")