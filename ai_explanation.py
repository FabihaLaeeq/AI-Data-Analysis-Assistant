import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)


# -------------------------------------------------
# EXISTING AI EXPLANATION
# -------------------------------------------------

def generate_explanation(answer):

    if not api_key:
        return "AI explanation is unavailable because the Gemini API key is missing."

    model = genai.GenerativeModel("gemini-3.6-flash")

    prompt = f"""
    Explain this data analysis result in simple language for a beginner.

    Result:
    {answer}

    Give a short explanation in 2-3 sentences.
    Do not invent any additional facts.
    """

    response = model.generate_content(prompt)

    return response.text


# -------------------------------------------------
# AI DATASET INSIGHTS
# -------------------------------------------------

def generate_dataset_insights(df):

    if not api_key:
        return "AI insights are unavailable because the Gemini API key is missing."

    model = genai.GenerativeModel("gemini-3.6-flash")

    # Create a compact summary instead of sending the entire dataset
    dataset_summary = f"""
    Dataset shape:
    {df.shape}

    Column names:
    {list(df.columns)}

    Data types:
    {df.dtypes.to_string()}

    Missing values:
    {df.isnull().sum().to_string()}

    Duplicate rows:
    {df.duplicated().sum()}

    Numerical summary:
    {df.describe(include="number").to_string()}

    Categorical summary:
    {df.describe(include="object").to_string()}
    """

    prompt = f"""
    You are an AI data analyst.

    Analyze the following dataset summary and provide useful,
    factual insights for a beginner.

    DATASET SUMMARY:
    {dataset_summary}

    Give 5-7 important insights.

    Focus on:
    1. Important patterns
    2. Highest or lowest values when supported by the data
    3. Missing values
    4. Duplicate data
    5. Possible outliers
    6. Relationships between numerical variables
    7. Useful recommendations

    IMPORTANT RULES:
    - Only use information supported by the provided dataset summary.
    - Do not invent facts.
    - Clearly say when something cannot be determined.
    - Keep the language simple.
    - Use bullet points.
    """

    response = model.generate_content(prompt)

    return response.text