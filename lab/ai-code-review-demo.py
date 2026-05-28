"""A lightweight demo for AI Code Review Workflow.

The code intentionally keeps the business logic simple. It can be used as
sample input when asking an AI assistant to review readability, edge cases,
and validation boundaries.
"""


def calculate_review_score(changed_files, test_count, has_description):
    """Calculate a simple review readiness score for a pull request."""
    score = 0

    # Smaller changes are easier to review and usually carry less coordination cost.
    if changed_files <= 3:
        score += 40
    elif changed_files <= 8:
        score += 25
    else:
        score += 10

    # Tests are not a complete quality signal, but they help reviewers trust changes.
    if test_count >= 5:
        score += 35
    elif test_count > 0:
        score += 20

    # A clear description helps reviewers understand intent and risk.
    if has_description:
        score += 25

    return min(score, 100)


def review_recommendation(score):
    """Return a human-readable review recommendation."""
    if score >= 80:
        return "Ready for review"
    if score >= 50:
        return "Needs a focused reviewer check"
    return "Needs more context before review"


def main():
    pull_request = {
        "changed_files": 5,
        "test_count": 3,
        "has_description": True,
    }

    score = calculate_review_score(
        pull_request["changed_files"],
        pull_request["test_count"],
        pull_request["has_description"],
    )

    print(f"Review readiness score: {score}")
    print(f"Recommendation: {review_recommendation(score)}")


if __name__ == "__main__":
    main()
