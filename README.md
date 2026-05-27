🚀 Coding Bootcamp Builder (Multi-Agent AI System)

🧠 Project Overview
Ye ek AI-based multi-agent system hai jo user ka coding profile analyze karke us ke liye complete personalized bootcamp roadmap generate karta hai.

System 4 AI agents use karta hai:
📊 User Assessment Agent
🔎 Project Research Agent
📚 Curriculum Builder Agent
🧑‍🏫 Curriculum Reviewer Agent
⚙️ Tech Stack
🐍 Python
🤖 OpenAI (gpt-4o-mini)
🌿 python-dotenv
🎨 Streamlit
🧠 Multi-Agent Prompt System

coding-bootcamp-builder/
├── src/
│   ├── agents/
│   ├── main.py
│   └── app.py
├── .env
├── .env.example
├── requirements.txt
└── README.md

🔑 Setup Instructions
1️⃣ Install Dependencies
pip install -r requirements.txt
2️⃣ Add API Key
OPENAI_API_KEY=your-key-here
📦 requirements.txt
crewai
openai
python-dotenv
streamlit


🔄 System Flow
1️⃣ Assessment
User ka skill level analyze hota hai 📊
2️⃣ Project Research
AI 8 best projects suggest karta hai 🔎
3️⃣ Curriculum Builder
Week-by-week bootcamp plan banta hai 📚

▶️ Run Project
CLI Pipeline
python src/main.py
Streamlit App
streamlit run src/app.py

🎯 Features
✨ AI-based learning roadmap
✨ 8 real-world coding projects
✨ Personalized weekly plan
✨ Mentorship checkpoints
✨ Final capstone project
✨ Interactive Streamlit UI

🚀 Output Flow
Assessment → Projects → Curriculum → Review → Final Plan

4️⃣ Reviewer Agent

Final mentorship checkpoints + capstone add hota hai 🧑‍🏫
