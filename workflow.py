"""
Day 1 - System 2: Rule-Based Workflow

A rule-based workflow follows predefined steps.
There is no LLM and no autonomous decision-making.
"""

from config import PRIVATE_EXPENSES, QUESTION


def run_workflow(question: str) -> str:
    # Step 1: Find food spending.
    food_expense = next(
        expense for expense in PRIVATE_EXPENSES
        if expense["category"].lower() == "food"
    )

    # Step 2: Find the largest expense.
    largest_expense = max(
        PRIVATE_EXPENSES,
        key=lambda expense: expense["amount"]
    )

    # Step 3: Apply a predefined review rule.
    if largest_expense["amount"] >= 4000:
        review = (
            f"Review your {largest_expense['category'].lower()} spending "
            "because it is your largest expense."
        )
    else:
        review = "Review the categories with the highest spending."

    # Step 4: Produce the final answer.
    return (
        "Rule-Based Workflow Response:\n"
        f"Food spending: ₹{food_expense['amount']}\n"
        f"Largest expense: {largest_expense['category']} "
        f"({largest_expense['item']}) - ₹{largest_expense['amount']}\n"
        f"What to review: {review}\n\n"
        f"Question processed: {question}"
    )


if __name__ == "__main__":
    print("=" * 60)
    print("SYSTEM 2: RULE-BASED WORKFLOW")
    print("=" * 60)
    print()
    print(run_workflow(QUESTION))