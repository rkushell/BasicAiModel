from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime
from datetime import datetime
import re

def save_to_txt(data: str, filename: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"Research Output\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"

def sanitize_filename(topic: str) -> str:
    s = topic.strip().replace(" ", "_")
    s = re.sub(r'(?u)[^-\w.]', '', s)
    return f"{s}.txt"

save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="saves structured research data to a text file.",
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name = 'search', 
    func = search.run,
    description="searches web for information",
)

api_wrapper = WikipediaAPIWrapper(top_k_results = 1,doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

