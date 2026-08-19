# LangChain Chatbot using RunnableBranch & RunnableParallel

## Project Overview
A Streamlit-based AI chatbot built with LangChain (LCEL) that routes a user's
question to a specialized prompt using `RunnableBranch`, generates the main
answer and a summary simultaneously using `RunnableParallel`, and returns the
result as a validated Pydantic object.

## Features
- Streamlit chat interface with chat history and a Clear Chat button
- Dynamic prompts built with `PromptTemplate`
- Topic-based routing with `RunnableBranch` (Programming / Mathematics / General)
- Simultaneous answer + summary generation with `RunnableParallel`
- Structured, schema-validated responses with Pydantic (`with_structured_output`)

## RunnableBranch Implementation
`chatbot.py` defines keyword-based condition functions (`is_programming`,
`is_math`) that inspect the user's question. `RunnableBranch` uses these
conditions to route the question to one of three prompt pipelines:
`programming_chain`, `math_chain`, or `general_chain` (the default branch).

## RunnableParallel Implementation
Once a branch is selected, the chatbot runs two chains simultaneously with
`RunnableParallel`:
- `main`: the routed answer chain (`ChatResponse`)
- `summary`: a summary chain (`SummaryResponse`)

Both results are merged in `get_response()` before being sent to the UI.

## Pydantic Structured Output Implementation
`schemas.py` defines two Pydantic models, `ChatResponse` (answer, category,
confidence, keywords) and `SummaryResponse` (summary). The chat model is bound
to these schemas with `model.with_structured_output(...)`, so responses are
returned as validated Python objects instead of raw strings.

## Installation
1. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your Groq API key:
   ```
   copy .env.example .env
   ```
4. Run the app:
   ```
   streamlit run app.py
   ```
