from langchain_core.prompts import PromptTemplate

programming_prompt = PromptTemplate(
    input_variables=["question"],
    template=(
        "You are a Programming Assistant. Answer the following programming "
        "question clearly, with code examples where useful.\n\n"
        "Question: {question}"
    ),
)

math_prompt = PromptTemplate(
    input_variables=["question"],
    template=(
        "You are a Math Tutor. Solve the following math problem step by step. "
        "Write all math in plain text only (for example: x^2, sqrt(x), 2x + 5 = 15). "
        "Do not use LaTeX or markdown math formatting.\n\n"
        "Question: {question}"
    ),
)

general_prompt = PromptTemplate(
    input_variables=["question"],
    template=(
        "You are a General Assistant. Answer the following question helpfully "
        "and accurately.\n\n"
        "Question: {question}"
    ),
)

summary_prompt = PromptTemplate(
    input_variables=["question"],
    template="Summarize the following question in one short sentence.\n\nQuestion: {question}",
)
