import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

# Function to create a PDF file
def create_pdf(content, filename="page_content.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    text = c.beginText(40, 750)
    text.setFont("Helvetica", 12)
    text.textLines(content)
    c.drawText(text)
    c.save()
    return filename

# Function to send the PDF via email
def send_email(to_email, pdf_filename):
    # Set up the email content
    msg = MIMEMultipart()
    msg['Subject'] = "Your Requested PDF"
    msg['From'] = "youremail@example.com"  # Your email here
    msg['To'] = to_email

    # Body of the email
    body = "Please find attached the PDF of your requested page content."
    msg.attach(MIMEText(body, "plain"))

    # Attach the PDF file
    with open(pdf_filename, "rb") as f:
        pdf_attachment = MIMEApplication(f.read(), _subtype="pdf")
        pdf_attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(pdf_filename))
        msg.attach(pdf_attachment)

    # Send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:  # Using Gmail SMTP
        server.starttls()
        server.login("youremail@example.com", "your_password")  # Your email credentials here
        server.send_message(msg)

# Streamlit page setup
st.title("Generate PDF and Send via Email")
st.write("Enter the content you want to save as a PDF and email.")

# User input for content
content = st.text_area("Enter Content", "Type your content here...")
email = st.text_input("Enter Email Address")

# Button to generate PDF and send email
if st.button("Generate PDF and Send Email"):
    if content and email:
        # Create PDF
        pdf_filename = create_pdf(content)
        
        # Send email
        try:
            send_email(email, pdf_filename)
            st.success(f"PDF has been sent to {email}.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
        
        # Remove the PDF file after sending
        if os.path.exists(pdf_filename):
            os.remove(pdf_filename)
    else:
        st.warning("Please provide both content and an email address.")
