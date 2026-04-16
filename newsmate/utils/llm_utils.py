from google import genai
from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path
from newsmate.utils.logger import get_logger

load_dotenv()
client = genai.Client()
logger = get_logger(__name__)

def load_prompt(prompt_name, article):
    logger.info(f"Loading prompt: {prompt_name}")
    prompt_path = Path(__file__).resolve().parents[1] / "prompts" / f"{prompt_name}.txt"
    with open(prompt_path, 'r', encoding='utf-8') as f:
        prompt = f.read()
    logger.info(f"{prompt_name} Prompt loaded successfully")
    return prompt.format(article=article)


def generate_content(prompt_name, article):
    prompt = load_prompt(prompt_name, article)
    logger.info("Initiating LLM call")
    start_time = datetime.now()
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    end_time = datetime.now()
    logger.info(f"LLM call completed in {end_time - start_time} seconds")
    return response