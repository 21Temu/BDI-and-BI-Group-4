# mapper.py - Job 2: Extract reviewer ID 
import sys
import json


def process_review(review_line):
    """
    Process a single review record and extract reviewer ID.

    Args:
        review_line (str): JSON review record

    Returns:
        str: reviewer_id with count value
    """

    try:
        review_data = json.loads(review_line)

        # Extract reviewer ID
        reviewer_id = review_data.get("reviewerID", "unknown")

        # Return mapper output format
        return f"{reviewer_id}\t1"

    except json.JSONDecodeError:
        return None


# Read input from Hadoop streaming
for line in sys.stdin:

    output = process_review(line)

    if output:
        print(output)
