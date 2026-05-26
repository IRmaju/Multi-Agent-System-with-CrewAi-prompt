import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def assess_user(user_input: dict) -> dict:
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY missing from .env")

        client = OpenAI(api_key=api_key)

        system_prompt = """
You are a senior coding mentor.
Assess the user's current level and return ONLY a raw JSON object with no markdown and no explanation.
Return EXACTLY these keys:
- level: one of "beginner", "intermediate", "advanced"
- strong_languages: list of languages they know well
- weak_areas: list of specific gaps or weaknesses
- recommended_stack: list of technologies they should focus on given their goal
- assessment_summary: 2-3 sentences summarizing their profile
"""

        user_message = f"""
languages: {user_input.get('languages')}
experience_years: {user_input.get('experience_years')}
projects_built: {user_input.get('projects_built')}
goal: {user_input.get('goal')}
hours_per_week: {user_input.get('hours_per_week')}
timeline_weeks: {user_input.get('timeline_weeks')}
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
        raise Exception(f"Assessment failed: {str(e)}")