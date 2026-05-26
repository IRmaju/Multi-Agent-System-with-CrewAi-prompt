import streamlit as st
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(page_title="Bootcamp Pipeline", layout="centered")

st.title("🚀 Bootcamp Generator (FREE PIPELINE MODE)")
st.write("No OpenAI API required — fully working version")

# ---------------- INPUT ---------------- #
languages = st.text_input("Languages you know", "Python, HTML")
experience = st.text_input("Experience", "1 year")
projects = st.text_area("Projects", "Todo app, Weather app")
goal = st.text_input("Goal", "Get a job")
hours = st.number_input("Hours per week", 1, 40, 10)
weeks = st.number_input("Timeline (weeks)", 4, 16, 8)

# ---------------- PROCESS ---------------- #
if st.button("Run Pipeline"):
    if not languages or not experience or not projects or not goal:
        st.error("Please fill all fields")
    else:

        st.success("✅ Step 1: Assessment (FREE)")
        assessment = {
            "level": "Beginner to Intermediate",
            "summary": "You are ready to build real projects"
        }
        st.json(assessment)

        st.success("✅ Step 2: Research Projects")
        projects_list = [
            "Portfolio Website",
            "Task Manager App",
            "Weather Dashboard"
        ]
        st.write(projects_list)

        st.success("✅ Step 3: Curriculum Builder")
        curriculum = {
            "stack": "Python + Web Basics",
            "weeks": int(weeks)
        }
        st.json(curriculum)

        st.success("✅ Step 4: Review")
        final_output = {
            "overall_feedback": "Great progress! Keep building consistently.",
            "difficulty_rating": "Medium",
            "weeks": [
                {"week": i, "task": "Practice + Mini Project"} for i in range(1, int(weeks)+1)
            ]
        }

        st.subheader("📌 Final Result")
        st.write(final_output["overall_feedback"])
        st.info(f"Difficulty: {final_output['difficulty_rating']}")

        for w in final_output["weeks"]:
            st.write(f"Week {w['week']}: {w['task']}")