from dotenv import load_dotenv
load_dotenv()

from decouple import config
api_key=config("OPENROUTER_API_KEY")

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
  base_url="https://openrouter.ai/api/v1",
  model = "openrouter/owl-alpha",
  api_key=api_key
)

from prompts.answer_prompt import ANSWER_PROMPT
from langfuse import observe

@observe
def generate_answer(state):
    prompt = ANSWER_PROMPT.format(
        context=state["context"],
        query=state["query"]
    )

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }