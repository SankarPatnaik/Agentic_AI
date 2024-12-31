# Crewai Multi-Agent Blog Content Creator

This project uses Crewai to build multiple AI agents that communicate among each other to create blog content from YouTube videos. It leverages OpenAI's ChatGPT as the language model (LLM) to perform various tasks such as caption extraction, research, and content creation.

## About Crewai

Crewai is a platform designed for building and deploying collaborative AI agents. These agents can perform complex tasks by communicating and coordinating with each other, making it easier to build sophisticated AI-driven applications.

## Project Overview

The Crewai Multi-Agent Blog Content Creator is designed to automate the process of generating blog content from YouTube videos. The project comprises three main AI agents:

1. **Caption Extractor**: This agent extracts captions from YouTube videos, providing a text transcript of the video's audio content.
2. **Blog Researcher**: This agent uses the extracted captions to gather detailed information about the video's topic, performing extensive research to enrich the content.
3. **Blog Writer**: This agent takes the researched information and creates coherent, engaging blog content that summarizes and expands on the video's topic.

### Detailed Workflow

1. **Caption Extraction**: 
    - The Caption Extractor agent fetches the YouTube video captions, which serve as the primary data source.
    
2. **Research Task**: 
    - The Blog Researcher agent analyzes the extracted captions to identify key topics and concepts.
    - It performs additional research to gather comprehensive information on these topics, leveraging various online resources.
    
3. **Write Task**: 
    - The Blog Writer agent takes the detailed information from the Blog Researcher.
    - It summarizes the information and crafts it into well-structured blog content.

### Potential Use Cases

- **Content Creation**: Automates the creation of high-quality blog posts from video content, saving time for content creators.
- **Educational Summaries**: Generates detailed summaries and explanations of educational YouTube videos for use in study guides or educational blogs.
- **Marketing**: Creates blog content that can be used to promote products, services, or ideas presented in YouTube videos.
- **SEO**: Enhances SEO by generating relevant, keyword-rich blog content derived from popular YouTube videos.

## Project Structure

- `main.py`: The main script that orchestrates the interaction between different agents.
- `note_engine.py`: Contains the logic for processing and managing notes and tasks.
- `prompts.py`: Contains prompt templates used by the agents.
- `requirements.txt`: Lists the required Python packages.

## Installation

To run this project, you need to have Python installed on your machine. Follow the steps below to set up the environment:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/hargurjeet/crewai/tree/main
    cd crewai-multi-agent-blog
    ```

2. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the main script**:
    ```sh
    python main.py
    ```

2. **Follow the prompts**: The script will guide you through the process of extracting captions, researching, and writing the blog content.

## Files

- **main.py**: Coordinates the tasks of extracting captions, researching, and writing.
- **note_engine.py**: Handles the management of research notes and task execution.
- **prompts.py**: Stores the prompts used by the AI agents for various tasks.
- **requirements.txt**: Lists dependencies like `llama-index`, `pypdf`, `python-dotenv`, and `pandas`.

## Requirements

- Python 3.7 or higher
- Required Python packages (listed in `requirements.txt`)

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improving the project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- **Crewai**: For providing the platform to build and deploy collaborative AI agents.
- **OpenAI**: For developing the ChatGPT model, which powers the language understanding and generation tasks in this project.
