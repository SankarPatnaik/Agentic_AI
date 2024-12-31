from crewai import Task
from tools import yt_tool
from agents import blog_reseracher, blog_writer

##Reserache task
research_task = Task(
    name="Research",
    description="Identify the video {topic}. Get the detailed information about the video from the channel.",
    expected_output = "A comprehensive 3 paragraphs long report based on the {topic} of video "
    tools=[yt_tool],
    agents=[blog_reseracher],
)

## Writing task with language model configuration
write_task = Task(
    description=(
        "Get the info from the you tube channel on the topic{topic}."
    ),
    expected_output="Summarize the info from the youtube channel video on the topic{topic} and create the content for the blog",
    tools=[yt_tool],
    agents=[blog_writer],
    async_execution = False,
    output_file="new-blog-post.md"
)