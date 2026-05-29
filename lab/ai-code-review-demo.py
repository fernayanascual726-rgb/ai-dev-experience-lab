"""Minimal AI Code Review Workflow demo.

This demo does not call an AI model. Instead, it simulates the shape of an
AI-assisted code review so the workflow is easy to inspect and run locally.

The focus is Developer Experience:
- a developer provides code
- AI suggests review points
- a human reviewer validates the suggestions
"""

from dataclasses import dataclass


PROBLEMATIC_CODE = """
def calc(x,y):
    r=[]
    for i in x:
        try:
            r.append(i/y)
        except:
            pass
    return r
""".strip()


@dataclass
class ReviewSuggestion:
    category: str
    observation: str
    developer_check: str


def simulate_ai_review(code: str) -> list[ReviewSuggestion]:
    """Return simulated AI review suggestions for a small Python snippet."""
    suggestions: list[ReviewSuggestion] = []

    # Readability: compact formatting makes review harder.
    if "def calc(x,y):" in code or "r=[]" in code:
        suggestions.append(
            ReviewSuggestion(
                category="Readability",
                observation="The function is compact but hard to scan. Spacing and clearer structure would make review easier.",
                developer_check="Confirm whether formatting follows the team's Python style guide.",
            )
        )

    # Naming: short names hide intent from future maintainers.
    if "calc" in code or "r" in code:
        suggestions.append(
            ReviewSuggestion(
                category="Naming",
                observation="Names such as 'calc', 'x', 'y', and 'r' do not explain the domain intent.",
                developer_check="Rename variables based on the actual business meaning before merging.",
            )
        )

    # Error handling: a bare except can hide production issues.
    if "except:" in code:
        suggestions.append(
            ReviewSuggestion(
                category="Error Handling",
                observation="A bare except silently ignores all errors, including unexpected runtime failures.",
                developer_check="Decide which exception should be handled and whether skipped items should be logged or returned.",
            )
        )

    # Optimization: validate inputs before looping when possible.
    if "/y" in code:
        suggestions.append(
            ReviewSuggestion(
                category="Optimization",
                observation="The divisor is used repeatedly without validation. A zero value will fail for every item.",
                developer_check="Validate the divisor once before the loop and define the expected behavior for invalid input.",
            )
        )

    return suggestions


def print_workflow_header() -> None:
    """Show the workflow this demo is trying to model."""
    print("AI Code Review Workflow")
    print("1. Developer writes code")
    print("2. AI proposes review suggestions")
    print("3. Developer validates each suggestion")
    print("4. Human reviewer decides what should change")
    print()


def print_review(code: str, suggestions: list[ReviewSuggestion]) -> None:
    """Print code and simulated AI review suggestions."""
    print("Input code:")
    print("-" * 40)
    print(code)
    print("-" * 40)
    print()

    print("Simulated AI Review Suggestions:")
    for index, suggestion in enumerate(suggestions, start=1):
        print(f"\n{index}. {suggestion.category}")
        print(f"   Observation: {suggestion.observation}")
        print(f"   Human check: {suggestion.developer_check}")


def main() -> None:
    print_workflow_header()
    suggestions = simulate_ai_review(PROBLEMATIC_CODE)
    print_review(PROBLEMATIC_CODE, suggestions)


if __name__ == "__main__":
    main()
