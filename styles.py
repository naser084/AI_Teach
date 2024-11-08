import streamlit as st
import google.generativeai as genai

# Configure the Gemini API with your API key
genai.configure(api_key="AIzaSyCCnNwevZD1Nn3Te3E3LU_Iqo_H44cxex4")

model = genai.GenerativeModel("gemini-1.5-flash")


# Inject CSS into the app
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #d1e7ff;
    }
    .title {
        text-align: center;
        color: #007bff;
        font-size: 60px;
        margin-top: 20px;
        margin-bottom: 30px;
    }
    .title1 {
        text-align: center;
        color: #007bff;
        font-size: 40px;
        margin-bottom: 10px;
    }
    .description {
        font-size: 20px;
        margin: 20px;
        background-color: #f0f4f8;
        padding: 15px;
        border-radius: 8px;
    }
    .css-1aumxhk {
        background-color: #f0f4f8 !important;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .stButton > button {
        background-color: #007bff;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #0056b3;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Apply the CSS class to the Title
st.markdown("<h1 class='title'>Welcome To AI Buddy!</h1>", unsafe_allow_html=True)
st.markdown("<h1 class='title1'>How does AI benefit me?</h1>", unsafe_allow_html=True)
st.markdown("<h1 class='title1'>What can AI Buddy do for me?</h1>", unsafe_allow_html=True)

# Profession and Field selection below title
col1, col2 = st.columns(2)

# Dropdown to select a profession
with col1:
    profession = st.selectbox("Profession", ["Student", "Teacher", "Doctor", "Lawyer", "Engineer", "Entrepreneur", "Other"])
    if profession == "Other":
        profession = st.text_input("Enter your profession")

# Dropdown to select a field
with col2:
    field = st.selectbox("Field", ["Technology", "Finance", "Education", "Business", "Science", "Healthcare", "Law", "Other"])
    if field == "Other":
        field = st.text_input("Enter your field")

# Button to submit profession and field
if st.button("Submit"):
    # Create the system prompt based on selected profession and field
    ai_benefit_prompt = f"As an AI assistant called 'AI Buddy', explain the specific benefits of AI for a {profession} working in the {field} field. Describe in short precise detail how AI enhances their work, learning, or decision-making."
    ai_buddy_role_prompt = f"Explain the role of AI Buddy in assisting a {profession} within the {field} field. Describe in short precise detail how AI Buddy acts as a personalized assistant to support their professional growth and learning."

    try:
        # Generate AI Benefit response
        benefit_response = model.generate_content(ai_benefit_prompt)
        ai_benefit_text = benefit_response.text if benefit_response and benefit_response.text else "AI Buddy provides insights and tools for your field."

        # Generate AI Buddy Role response
        role_response = model.generate_content(ai_buddy_role_prompt)
        ai_buddy_role_text = role_response.text if role_response and role_response.text else "AI Buddy acts as your assistant, supporting your journey in this field."

    except Exception as e:
        # Display an error message if there is an issue with the API call
        ai_benefit_text = f"An error occurred while fetching the AI Benefit: {str(e)}"
        ai_buddy_role_text = f"An error occurred while fetching the Role of AI Buddy: {str(e)}"

    # Display the AI-generated responses
    st.markdown(f"<div class='description'><strong>AI Benefit:</strong><br>{ai_benefit_text}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='description'><strong>Role of AI Buddy:</strong><br>{ai_buddy_role_text}</div>", unsafe_allow_html=True)

# Sidebar introduction
st.sidebar.title("Meet AI Tutor")
st.sidebar.markdown("AI Tutor is here to help you explore and understand AI in your profession and field. Get customized insights and guidance tailored to your area of expertise!")

st.sidebar.markdown("""
### Getting Started:
1. *Select Profession and Field:* Use the dropdown menus under the main title to choose your profession (e.g., Teacher, Engineer) and field (e.g., Technology, Healthcare).
2. *Click "Submit":* Press the "Submit" button to confirm your choices. it tells you how AI benefits your field and its role in your professional journey.
""", unsafe_allow_html=True)