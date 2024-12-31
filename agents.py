from crewai import Agent
from tools import yt_tool
import os
from dotenv import load_dotenv
from crewai import Agent,Task, Crew
from langchain_groq import ChatGroq


load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
os.enviorn["GROQ_MODEL_NAME"] = "llama3-70b-8192"


llm = ChatGroq(
    temperature=0,
    model_name='llama3-70b-8192',groq_api_key=GROQ_API_KEY
   )
print(llm.invoke("hi"))

##senior blog contect reserchers
blog_researchers = Agent(
    role='Blog Reserachers from youtube vedios',
    goal = 'get the relevant video content for the topic{topic} from yt channel',
    name='blog_researchers',
    description='get the relevant video content for the topic{topic} from yt channel',
    verbose=True,
    memory = True,
    backstory = (
            "Expert in understanding videos in AI Data Scinece, machine learning and gen ai and providing suggestions"
    ),
    tools=[yt_tool],
    allow_delegation=True,
    llm=llm
)

## creating a senior blog writer agent with yt tool

blog_writer = Agent(
    role = 'blog writer',
    goal = 'Narrate compelling tech stories about the vedio {topic} from YT channel',
    verbose=True,
    memory = True,
    backstory = (
            "Expert in simplifying complex topics, you craft engaging narratives that educate and bring new discoveries to \
                light in an accessible manner"
    ),
    tools=[yt_tool],
    allow_delegation=False,
    llm=llm
)