"""
Day 1 - System 1: Plain Chatbot

A plain chatbot has access only to the question.
It does not have access to the user's private expense data.
"""

from config import QUESTION


def chatbot_answer(question: str) -> str:
    """
    Simulate a plain chatbot without private-data access.

    The chatbot cannot calculate the user's actual expenses because
    the private expense data is not provided to it.
    """

    return (
        "Plain Chatbot Response:\n"
        "I can explain how to analyze a monthly budget, but I cannot "
        "determine your actual food spending or largest expense because "
        "I do not have access to your private March expense data.\n\n"
        f"Question received: {question}"
    )


if __name__ == "__main__":
    print("=" * 60)
    print("SYSTEM 1: PLAIN CHATBOT")
    print("=" * 60)
    print()
    print(chatbot_answer(QUESTION))