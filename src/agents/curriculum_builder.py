import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def build_curriculum(assessment: dict, projects: list, timeline_weeks: int) -> dict:
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY missing from .env")

        client = OpenAI(api_key=api_key)

        system_prompt = """
You are a coding bootcamp curriculum designer.
Using the assessment and project list provided, build a structured week-by-week curriculum.
Return ONLY a raw JSON object with no markdown and no explanation.
Return EXACTLY these keys:
- total_weeks: integer
- weekly_hours: integer
- stack_focus: string
- weeks: list of week objects, each containing:
    - week_number: integer
    - theme: short title for the week
    - project: project title assigned
    - goals: list of 3 specific learning goals
    - deliverable: what user builds by end of week
    - resources: list of 2-3 learning resources
"""

        user_message = f"""
ASSESSMENT:
{json.dumps(assessment, indent=2)}

PROJECTS:
{json.dumps(projects, indent=2)}

TIMELINE_WEEKS:
{timeline_weeks}
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
        
        result = json.loads(content)

        if len(result.get("weeks", [])) != timeline_weeks:
            raise ValueError("Weeks count does not match timeline_weeks")

        return result

    except Exception as e:
        raise Exception(f"Curriculum build failed: {str(e)}")