import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def research_projects(assessment: dict) -> list:
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY missing from .env")

        client = OpenAI(api_key=api_key)

        system_prompt = """
You are a technical research agent.
Based on the user's assessment, brainstorm a list of highly relevant practical coding projects that match their recommended stack and target level.
Return ONLY a raw JSON object with a single key 'projects' which contains a list of objects. No markdown, no explanation.
Each project object inside the list MUST have:
- title: Name of the project
- description: 1-2 sentences explaining what it is
- difficulty: 'beginner', 'intermediate', or 'advanced'
"""

        user_message = f"""
USER ASSESSMENT:
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
        
        data = json.loads(content)
        return data.get("projects", [])

    except Exception as e:
        raise Exception(f"Project research failed: {str(e)}")