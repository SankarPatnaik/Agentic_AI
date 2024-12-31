from crewai import Crew, Process,Agent,Task
from agents import blog_researchers, blog_writer
from tasks import research_task, write_task
from langchain_groq import ChatGroq
from crewai import LLM
import os
#Load Your LLM API Key . I have used GROQ API
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
os.enviorn["GROQ_MODEL_NAME"] = "llama3-70b-8192"


llm = LLM(
    model="groq/llama3-70b-8192",
    temperature=0.7
)

#Test My LLL
print(llm.invoke("hi"))
crew = Crew(
    agents = [blog_researchers, blog_writer],
    tasks = [research_task, write_task],
    process = Process.sequential,
    memory = True,
    cache = True,
    max_rpm = 100,
    share_crew=True,
    llm=llm
)

##start the task execution process with enhanced feedback
result = crew.kickoff(input={'topic': 'AI vs ML vs DL vs Data science'})
print(result)