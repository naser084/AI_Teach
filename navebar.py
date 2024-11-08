import streamlit as st

# Inject custom CSS to style the sidebar
st.markdown(
    """
    <style>
    /* Custom styling for the sidebar */
    .sidebar .sidebar-content {
        background-color: #f0f4f8;
        padding: 20px;
    }
    
    /* Custom styling for the title */
    h1 {
        color: #4CAF50;
        text-align: center;
    }
    
    /* Custom button styling */
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.title("My Streamlit App")

# Create a main navigation using selectbox
page = st.selectbox("Select a page", ["Home", "About", "Contact"])

# Content for each page
if page == "Home":
    st.header("Home")
    st.write("Welcome to the home page!")
elif page == "About":
    st.header("About")
    st.write("This is the about page.")
elif page == "Contact":
    st.header("Contact")
    st.write("This is the contact page.")
