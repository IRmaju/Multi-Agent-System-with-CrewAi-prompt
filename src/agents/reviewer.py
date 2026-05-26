import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def review_curriculum(curriculum: dict, assessment: dict) -> dict:
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY missing from .env")

        client = OpenAI(api_key=api_key)

        system_prompt = """
You are a senior bootcamp mentor and curriculum reviewer.
Review the curriculum and add mentorship checkpoints.
Return ONLY a raw JSON object with no markdown and no explanation.
Return EXACTLY these keys:
- overall_feedback: 2-3 sentences on the curriculum's strengths
- difficulty_rating: one of "too easy", "well balanced", "too hard"
- weeks: same weeks list but each week must include:
    - checkpoint: a specific, concrete and testable task/question
- final_project: a capstone project object with:
    - title: name of the final project
    - description: 3-4 sentences
    - requirements: list of 5 technical requirements
    - estimated_hours: integer
"""

        user_message = f"""
CURRICULUM:
{json.dumps(curriculum, indent=2)}

ASSESSMENT:
{json.dumps(assessment, indent=2)}
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        content = response.choices[0].message.content
        
        # Is line ko humne bilkul sahi aur ek hi line mein seedha kar diya hai
        content = content.replace("```json", "").replace("```", "").strip()
        
        return json.loads(content)

    except Exception as e:
        raise Exception(f"Curriculum review failed: {str(e)}")