"""
Day 1 Assessment Runner

Runs:
1. Plain Chatbot
2. Rule-Based Workflow
3. AI Agent
"""

from config import QUESTION
from chatbot import chatbot_answer
from workflow import run_workflow
from agent import run_agent


def main():
    print("\n" + "=" * 70)
    print("DAY 1 ASSESSMENT: THREE WAYS TO ANSWER A PRIVATE-DATA QUESTION")
    print("=" * 70)

    print("\nQUESTION:")
    print(QUESTION)

    print("\n" + "=" * 70)
    print("1. PLAIN CHATBOT")
    print("=" * 70)
    print(chatbot_answer(QUESTION))

    print("\n" + "=" * 70)
    print("2. RULE-BASED WORKFLOW")
    print("=" * 70)
    print(run_workflow(QUESTION))

    print("\n" + "=" * 70)
    print("3. AI AGENT")
    print("=" * 70)
    print(run_agent(QUESTION))

    print("\n" + "=" * 70)
    print("ASSESSMENT COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()