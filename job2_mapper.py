# mapper.py - Job 2: Extract reviewer ID for review counting

import sys
import json
from typing import Optional


DEFAULT_REVIEWER_ID = "unknown"


def process_review(review_line: str) -> Optional[str]:
    """
    Process a review record and return mapper output.

    Parameters:
        review_line (str): JSON review input line

    Returns:
        Optional[str]:
            reviewerID with count value in mapper format
            Example: A123XYZ\t1
    """

    try:
        review_data = json.loads(review_line.strip())

        reviewer_id = review_data.get(
            "reviewerID",
            DEFAULT_REVIEWER_ID
        )

        return f"{reviewer_id}\t1"

    except json.JSONDecodeError:
        return None


def main() -> None:
    """
    Read input stream and process review records.
    """

    for line in sys.stdin:

        output = process_review(line)

        if output is not None:
            print(output)


if __name__ == "__main__":
    main()
