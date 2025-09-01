from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from tools import search_tool,wiki_tool,save_to_txt,sanitize_filename
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent,AgentExecutor
load_dotenv()

class ResearchResponse(BaseModel):
    topic : str
    summary : str
    sources : list[str]
    tools_used: list[str] 


llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a reasearch assistant that will help generate a research paper.
            Answer the user query and use necessary tools.
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder","{chat_history}"),
        ("human","{query}"),
        ("placeholder","{agent_scratchpad}"),
    ]
).partial(format_instructions = parser.get_format_instructions())
tools = [search_tool,wiki_tool]
agent = create_tool_calling_agent(
    llm = llm,
    prompt = prompt,
    tools = tools
)

agent_executor = AgentExecutor(agent = agent , tools=tools,verbose=True)
query = input("What can I help you research?\n")
raw_response = agent_executor.invoke({"query":query})

try:
    structured_response = parser.parse(raw_response.get("output"))
    print("\nFinal Parsed Response")
    print(structured_response)

    unique_filename = sanitize_filename(structured_response.topic)
    print(f"\nUnique filename: {unique_filename}")
    data_to_save = (
        f"Topic: {structured_response.topic}\n\n"
        f"Summary: {structured_response.summary}\n\n"
        f"Sources: {', '.join(structured_response.sources)}"
    )
    save_message = save_to_txt(data_to_save, filename=unique_filename)
    print(save_message)

except Exception as e:
    print("\nError parsing final response")
    print("Error:", e)
    print("Raw Response:", raw_response)