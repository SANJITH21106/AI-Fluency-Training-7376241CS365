"""
Day 1 - System 3: AI Agent

The agent uses a simple reasoning-and-tool loop.

Goal -> Decide -> Act -> Observe -> Decide -> Finish
"""

from config import QUESTION
from tools import (
    get_expenses,
    calculate_food_spending,
    find_largest_expense,
)


def run_agent(question: str) -> str:
    print("AGENT TRACE")
    print("-" * 60)

    # Goal
    print("Goal: Answer the user's private-data budgeting question.")

    # Decision 1
    print("Decision: I need access to the private expense data.")

    # Act
    print("Action: Calling tool -> get_expenses()")
    expenses = get_expenses()

    # Observe
    print(f"Observation: Received {len(expenses)} expense records.")

    # Decision 2
    print("Decision: Calculate the food spending.")
    food_total = calculate_food_spending(expenses)

    print(f"Observation: Food spending = ₹{food_total}")

    # Decision 3
    print("Decision: Find the largest expense.")
    largest = find_largest_expense(expenses)

    print(
        f"Observation: Largest expense = "
        f"{largest['category']} - ₹{largest['amount']}"
    )

    # Final decision
    print("Decision: Enough information is available. Finish.")

    if largest["amount"] >= 4000:
        review = (
            f"Review your {largest['category'].lower()} spending "
            f"because it is your largest expense."
        )
    else:
        review = "Review the categories with the highest spending."

    return (
        "\nAI Agent Response:\n"
        f"Food spending: ₹{food_total}\n"
        f"Largest expense: {largest['category']} "
        f"({largest['item']}) - ₹{largest['amount']}\n"
        f"What to review: {review}\n"
    )


if __name__ == "__main__":
    print("=" * 60)
    print("SYSTEM 3: AI AGENT")
    print("=" * 60)
    print()

    answer = run_agent(QUESTION)

    print(answer)
    print(f"Question: {QUESTION}")