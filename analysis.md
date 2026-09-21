# Day 1 Assessment: Three Ways to Answer a Private-Data Question

## 1. Scenario

This assessment uses a small fictional student budgeting example.

The private data contains five March expenses:

- Food: ₹4,500
- Travel: ₹2,000
- Shopping: ₹3,200
- Education: ₹1,500
- Entertainment: ₹1,800

The question is:

> How much did I spend on food in March, what was my largest expense, and what should I review?

---

## 2. Plain Chatbot

The plain chatbot receives only the user's question.

It does not have access to the private expense data and does not have any tools.

Therefore, it cannot determine the actual food spending or largest expense.

### Flow

Question → Chatbot → Response

### Result

The chatbot explains that it cannot answer the private-data portion because the required data is unavailable.

---

## 3. Rule-Based Workflow

The rule-based workflow uses predefined Python instructions.

It directly accesses the private expense data and follows fixed steps:

1. Find the Food expense.
2. Find the largest expense.
3. Apply a predefined review rule.
4. Generate the answer.

### Flow

Question → Fixed Rules → Private Data → Calculation → Response

### Result

- Food spending: ₹4,500
- Largest expense: Food — ₹4,500
- Review: Food spending

The workflow is predictable because the steps are predefined.

---

## 4. AI Agent

The AI agent uses a goal, tools, and a decision loop.

The agent first determines that it needs the private expense data. It then calls the `get_expenses()` tool and observes the returned data.

After that, it decides to calculate food spending and find the largest expense.

### Agent Loop

Goal → Decide → Act → Observe → Decide → Finish

### Tool Calls

The agent uses:

- `get_expenses()`
- `calculate_food_spending()`
- `find_largest_expense()`

### Result

- Food spending: ₹4,500
- Largest expense: Food — ₹4,500
- Review: Food spending

The agent also produces a trace showing its decisions, actions, and observations.

---

# 5. Comparison

| Aspect | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Flexibility | Low | Low to Medium | High |
| Decision-making | No autonomous tool decision | Fixed programmer-defined rules | Dynamic tool/action selection |
| Tool usage | No | No separate tool loop | Yes |
| Private-data access | No | Yes | Yes through tools |
| Multi-step handling | Limited | Predefined steps | Can perform multiple steps |
| Automation | Basic response | High for predefined tasks | High for variable tasks |
| Reliability | Cannot answer without required data | Predictable for defined cases | Flexible but more complex |
| Suitability for this task | Limited | Suitable | Suitable |

---

# 6. Key Differences

## Plain Chatbot

A plain chatbot is useful when the required information is already available in the conversation.

It cannot directly access private data or perform external actions unless those capabilities are added.

## Rule-Based Workflow

A rule-based workflow is useful when the task has clear and predictable steps.

It is easier to test because the same input follows the same predefined logic.

## AI Agent

An AI agent is useful when the task requires multiple steps and tool usage.

Instead of following only one fixed sequence, the agent can decide what information or tool it needs, observe the result, and continue until the goal is completed.

---

# 7. Suitability Analysis

For this particular budgeting question:

- The plain chatbot cannot access the private expense data.
- The rule-based workflow can solve the problem using predefined calculations.
- The AI agent can solve the problem while demonstrating tool usage and an agent loop.

The agent provides more flexibility, while the rule-based workflow provides more predictable execution.

Higher autonomy is not automatically better. The appropriate approach depends on the task requirements.

---

# 8. General Conclusion

The three implementations demonstrate increasing levels of capability:

**Plain Chatbot**
→ Generates a response without private-data access.

**Rule-Based Workflow**
→ Uses fixed program logic to access and process private data.

**AI Agent**
→ Uses a goal-oriented loop with tools, observations, and decisions.

The main difference is not simply the use of an LLM. An agent combines an LLM-based decision process with tools and an execution loop to handle multi-step tasks.