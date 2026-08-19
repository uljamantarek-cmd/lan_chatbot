import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableBranch, RunnableParallel

from prompts import programming_prompt, math_prompt, general_prompt, summary_prompt
from schemas import ChatResponse, SummaryResponse

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b", api_key=os.getenv("GROQ_API_KEY"))

structured_model = model.with_structured_output(ChatResponse)
summary_model = model.with_structured_output(SummaryResponse)

PROGRAMMING_KEYWORDS = [
    "code", "python", "function", "program", "bug", "error", "javascript",
    "java", "algorithm", "loop", "array", "variable", "class", "compile", "debug",
]

MATH_KEYWORDS = [
    "math", "calculate", "equation", "solve", "algebra", "geometry",
    "derivative", "integral", "sum", "multiply", "divide", "square", "triangle",
]


def is_programming(input_data: dict) -> bool:
    question = input_data["question"].lower()
    return any(word in question for word in PROGRAMMING_KEYWORDS)


def is_math(input_data: dict) -> bool:
    question = input_data["question"].lower()
    return any(word in question for word in MATH_KEYWORDS)


programming_chain = programming_prompt | structured_model
math_chain = math_prompt | structured_model
general_chain = general_prompt | structured_model
summary_chain = summary_prompt | summary_model

branch_chain = RunnableBranch(
    (is_programming, programming_chain),
    (is_math, math_chain),
    general_chain,
)

parallel_chain = RunnableParallel(
    main=branch_chain,
    summary=summary_chain,
)


def get_response(question: str) -> dict:
    result = parallel_chain.invoke({"question": question})
    main: ChatResponse = result["main"]
    summary: SummaryResponse = result["summary"]

    return {
        "answer": main.answer,
        "category": main.category,
        "confidence": main.confidence,
        "keywords": main.keywords,
        "summary": summary.summary,
    }
