# NewsMate

NewsMate generates a daily AI news digest by collecting articles from The Guardian, summarizing each story with Gemini, and exporting a polished PDF report.

## Description

This project automates an end-to-end reporting workflow:

- Fetches AI-related technology articles for a target date.
- Extracts and parses article content.
- Summarizes each article using Gemini (`gemini-2.5-flash`).
- Produces a styled PDF digest saved by date.

## Features

- Date-based article extraction from The Guardian API.
- LLM-powered article summarization.
- PDF generation with cover page and article sections.
- Structured logs and date-organized output artifacts.

## Tech Stack

- Python 3.13+
- requests + BeautifulSoup4 for scraping/parsing
- Google GenAI SDK for summaries
- reportlab for PDF generation
- pandas for data handling

## Project Structure

```text
newsmate/
	components/
		get_news.py         # Article collection and summarization pipeline
		generate_pdf.py     # PDF generation and formatting
	pipelines/
		supervisor.py       # Orchestrates the full workflow
	prompts/
		summary_prompt.txt  # Prompt template for LLM summaries
	utils/
		llm_utils.py        # Prompt loading and model calls
		logger.py           # Logging setup
main.py                # Pipeline entry point
data/                  # Generated PDF outputs (grouped by date)
logs/                  # Runtime logs
```

## Prerequisites

- Python 3.13 or newer
- A Gemini API key
- A Guardian Open Platform API key

## Setup

1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies.
4. Create a `.env` file from `.env.example`.

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .
copy .env.example .env
```

Add your keys to `.env`:

```env
GEMINI_API_KEY=your_gemini_api_key
GUARDIAN_API_KEY=your_guardian_api_key
```

## Usage

Run the pipeline using:

```bash
python main.py
```

By default, `main.py` runs for a fixed date (`2026-01-03`).

To run for a different date, update the value passed to `run_pipeline(...)` in `main.py`.

## Output

- PDF digest file is generated under `data/DD-MM-YYYY/`.
- Logs are written to `logs/`.

## License

This project is licensed under the terms in the `LICENSE` file.
