import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(page_title="Coding Bootcamp Builder", layout="centered")

st.title("🚀 Coding Bootcamp Builder (FREE MODE)")
st.caption("Build your personal bootcamp without API errors")

# ---------------- FORM ---------------- #
with st.form("bootcamp_form"):
    languages = st.text_input("What languages or frameworks do you know?")
    experience = st.text_input("How long have you been coding?")
    projects = st.text_area("What have you built before? List any projects.")
    goal = st.text_input("What is your goal?", placeholder="e.g. get a backend job, go freelance")

    col1, col2 = st.columns(2)

    with col1:
        hours = st.number_input("Hours available per week", min_value=1, max_value=40, value=10)

    with col2:
        timeline = st.selectbox("Timeline", ["4 weeks", "8 weeks", "12 weeks", "16 weeks"])

    submitted = st.form_submit_button("Build My Bootcamp")

# ---------------- FREE LOGIC (NO AGENTS) ---------------- #
if submitted:
    if not languages or not experience or not projects or not goal:
        st.error("Please fill all fields before continuing.")
    else:
        st.success("✅ Bootcamp Generated Successfully (FREE MODE)")

        st.subheader("📊 Your Profile Summary")
        st.write(f"**Languages:** {languages}")
        st.write(f"**Experience:** {experience}")
        st.write(f"**Projects:** {projects}")
        st.write(f"**Goal:** {goal}")
        st.write(f"**Hours/Week:** {hours}")
        st.write(f"**Timeline:** {timeline}")

        st.subheader("📚 Your Week-by-Week Plan")

        weeks = int(timeline.split()[0])

        for i in range(1, weeks + 1):
            with st.expander(f"Week {i}"):

                st.write("**Focus:** Skill building + practice")

                st.write("**Project:**")
                st.write("Small hands-on coding project")

                st.write("**Goals:**")
                st.write("• Practice coding daily")
                st.write("• Build consistency")
                st.write("• Improve problem solving")

                st.write("**Resources:**")
                st.write("• YouTube tutorials")
                st.write("• Practice exercises")
                st.write("• Documentation reading")

                st.warning("Checkpoint: Complete weekly practice")

        st.subheader("🎯 Final Capstone Project")
        st.write("Build a complete real-world project based on your chosen goal.")

        if st.button("Start Over"):
            st.session_state.clear()
            st.rerun()