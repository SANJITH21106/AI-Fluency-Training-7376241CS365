"""
Tools available to the AI agent.
"""

from config import PRIVATE_EXPENSES


def get_expenses() -> list:
    """Return the private expense data."""
    return PRIVATE_EXPENSES


def calculate_food_spending(expenses: list) -> int:
    """Calculate total food spending."""
    return sum(
        expense["amount"]
        for expense in expenses
        if expense["category"].lower() == "food"
    )


def find_largest_expense(expenses: list) -> dict:
    """Find the largest expense."""
    return max(expenses, key=lambda expense: expense["amount"])