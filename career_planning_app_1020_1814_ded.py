# 代码生成时间: 2025-10-20 18:14:25
import streamlit as st

# Career Planning App
# This app helps users to plan their career paths

# Function to get user input for career planning
def get_user_input():
    st.title("Career Planning System")
    user_name = st.text_input("What's your name?", "Enter your name")
    current_job = st.text_input("What is your current job?", "Enter your current job")
    years_experience = st.number_input("How many years of experience do you have?", min_value=0, value=0)
    return user_name, current_job, years_experience

# Function to suggest career paths based on user input
def suggest_career_paths(user_name, current_job, years_experience):
    # Placeholder for career path suggestion logic
    # This can be expanded to include more sophisticated algorithms
    if years_experience > 5:
        return f"Hi {user_name}, with {years_experience} years of experience in {current_job}, you could consider the following career paths: Senior Developer, Team Lead."
    else:
        return f"Hi {user_name}, with {years_experience} years of experience in {current_job}, you could consider the following career paths: Junior Developer, Mid-Level Developer."

# Main function to run the app
def main():
    try:
        user_name, current_job, years_experience = get_user_input()
        career_suggestions = suggest_career_paths(user_name, current_job, years_experience)
        st.write(career_suggestions)
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Run the app
if __name__ == "__main__":
    main()