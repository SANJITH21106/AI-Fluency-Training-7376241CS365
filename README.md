# Day 1 Assessment: Three Ways to Answer a Private-Data Question

## Objective

This assessment compares three approaches to answering a question that requires access to private data:

1. Plain Chatbot
2. Rule-Based Workflow
3. AI Agent

## Scenario

A fictional student has five March expenses:

| Category | Amount |
|---|---:|
| Food | ₹4,500 |
| Travel | ₹2,000 |
| Shopping | ₹3,200 |
| Education | ₹1,500 |
| Entertainment | ₹1,800 |

Question:

> How much did I spend on food in March, what was my largest expense, and what should I review?

## Systems

### 1. Plain Chatbot

The chatbot receives only the question and has no access to the private expense data or tools.

Run:

```powershell
python chatbot.py