import streamlit as st
import google.generativeai as genai
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Configure the Gemini API with your API key
genai.configure(api_key="AIzaSyCCnNwevZD1Nn3Te3E3LU_Iqo_H44cxex4")

model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize session state for storing chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = ""

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
        color: #00e68a;
        font-size: 60px;
        margin-top: 20px;
        margin-bottom: 30px;
    }
    .title1 {
        text-align: center;
        color: #00e68a;
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
st.markdown("<h1 class='title'>Welcome To AI Companion!</h1>", unsafe_allow_html=True)
st.markdown("<h1 class='title1'>How does AI benefit me?</h1>", unsafe_allow_html=True)

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

# Chatbot input for user queries
user_input = st.text_input("Ask how AI benefits your profession and field:")

if user_input:
    if user_input.lower() == "delete chat history":
        # Clear chat history if user types the delete command
        st.session_state["chat_history"] = ""
        st.success("Chat history has been deleted.")
    else:
        # Create the prompt dynamically with profession, field, and user input
        ai_benefit_prompt = (
            f"As an AI assistant called 'AI Tutor', provide specific benefits of AI for a {profession} working in the {field} field. "
            f"Respond directly to this query: '{user_input}'."
        )

        try:
            # Generate AI Benefit response
            benefit_response = model.generate_content(ai_benefit_prompt)
            ai_benefit_text = benefit_response.text if benefit_response and benefit_response.text else "AI Buddy provides insights and tools for your field."

            # Append response to chat history in session state
            st.session_state["chat_history"] += f"\nUser Query: {user_input}\nAI Response: {ai_benefit_text}\n"

        except Exception as e:
            # Display an error message if there is an issue with the API call
            ai_benefit_text = f"An error occurred while fetching the AI Benefit: {str(e)}"

        # Display the AI-generated response
        st.markdown(f"<div class='description'><strong>AI Benefit:</strong><br>{ai_benefit_text}</div>", unsafe_allow_html=True)

        # PDF generation and download button
        if ai_benefit_text:
            buffer = BytesIO()
            c = canvas.Canvas(buffer, pagesize=letter)
            c.drawString(72, 750, "AI Companion Chat Summary")
            c.drawString(72, 730, f"Profession: {profession}")
            c.drawString(72, 710, f"Field: {field}")
            c.drawString(72, 690, f"User Query: {user_input}")
            text = c.beginText(72, 670)
            text.setFont("Helvetica", 10)
            text.textLines(f"AI Benefit Response:\n{ai_benefit_text}")
            c.drawText(text)
            c.save()
            buffer.seek(0)

            # Add the download button
            st.download_button(
                label="Download as PDF",
                data=buffer,
                file_name="AI_Companion_Chat_Summary.pdf",
                mime="application/pdf"
            )
 

# Sidebar introduction and delete chat history button
st.sidebar.title("Meet AI Tutor")
st.sidebar.markdown("AI Tutor is here to help you explore and understand AI in your profession and field. Get customized insights and guidance tailored to your area of expertise!")



st.sidebar.markdown("""
### Getting Started:
1. *Select Profession and Field:* Use the dropdown menus under the main title to choose your profession (e.g., Teacher, Engineer) and field (e.g., Technology, Healthcare).
2. *Type Your Question:* Enter your question in the input box above to learn how AI benefits your selected profession and field.
""", unsafe_allow_html=True)
