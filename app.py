import streamlit as st
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import datetime

# Custom CSS for styling
def apply_custom_css():
    st.markdown("""
    <style>
        /* Main theme colors */
        :root {
            --primary-color: #2E86C1;
            --secondary-color: #3498DB;
            --accent-color: #1ABC9C;
            --background-color: #F8F9F9;
            --text-color: #2C3E50;
        }
        
        /* Page background */
        .stApp {
            background-color: var(--background-color);
        }
        
        /* Headers */
        h1, h2, h3 {
            color: var(--primary-color);
            font-weight: 700;
        }
        
        h1 {
            font-size: 2.5rem !important;
            border-bottom: 3px solid var(--accent-color);
            padding-bottom: 0.5rem;
        }
        
        h2 {
            font-size: 1.8rem !important;
            margin-top: 1.5rem !important;
        }
        
        /* Form styling */
        .stButton button {
            background-color: var(--primary-color) !important;
            color: white !important;
            font-weight: 600 !important;
            padding: 0.5rem 1.5rem !important;
            border-radius: 30px !important;
            border: none !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton button:hover {
            background-color: var(--accent-color) !important;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        /* Form input fields */
        .stTextInput input, .stTextArea textarea, .stSelectbox, .stNumberInput {
            border-radius: 5px !important;
            border: 1px solid #E0E0E0 !important;
            transition: all 0.3s ease !important;
        }
        
        .stTextInput input:focus, .stTextArea textarea:focus {
            border-color: var(--accent-color) !important;
            box-shadow: 0 0 5px rgba(26, 188, 156, 0.3) !important;
        }
        
        /* Custom card-like sections */
        .card {
            background-color: white;
            border-radius: 10px;
            padding: 1.5rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-bottom: 1.5rem;
        }
        
        .section-header {
            color: var(--primary-color);
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        /* Success message styling */
        .success-message {
            background-color: #D4EFDF;
            color: #196F3D;
            padding: 1rem;
            border-radius: 5px;
            border-left: 5px solid #27AE60;
            margin: 1rem 0;
        }
        
        /* Warning banner */
        .test-banner {
            background-color: #FDEDEC;
            border-left: 5px solid #E74C3C;
            padding: 1rem;
            margin-bottom: 1.5rem;
            border-radius: 5px;
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.8rem;
            color: #34495E;
            margin-top: 2rem;
        }
        
        /* Icons */
        .icon {
            margin-right: 0.5rem;
            color: var(--primary-color);
        }

        /* Improve text visibility */
        p, li, label, .stMarkdown, .stSelectbox, .stNumberInput {
            color: #2C3E50 !important;
        }
        
        /* Label and help text */
        .css-1p1nr97, div[data-testid="stMarkdownContainer"] p {
            color: #34495E !important;
        }

        /* Streamlit default text */
        .css-183lzff {
            color: #2C3E50 !important;
        }
    </style>
    """, unsafe_allow_html=True)

# Logo and company branding
def display_company_header():
    # Using columns for logo and title
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 10px;">
            <div style="background-color: #3498DB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto;">
                <span style="color: white; font-size: 2.5rem; font-weight: bold;">C</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <h1>CADIA 3D Printing Service</h1>
        <br/>
        <p style="color: #34495E; margin-top: -1.8rem; font-size: 1.1rem;">Professional 3D printing solutions for all your needs</p>
        """, unsafe_allow_html=True)

# Main function
def main():
    # Page configuration
    st.set_page_config(
        page_title="CADIA 3D Printing Service Orders",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Apply custom CSS
    apply_custom_css()
    
    # Display company header with logo
    display_company_header()
    
    # Test version banner
    st.markdown("""
    <div class="test-banner">
        <strong>⚠️ Test Version:</strong> Please note this is a test version of the order form and you are not yet placing real orders. 
        Real orders will be accepted soon.
    </div>
    """, unsafe_allow_html=True)
    
    # Introduction section
    st.markdown("""
    <div class="card">
        <div class="section-header">📋 How It Works</div>
        <ol>
            <li>Upload your CAD file in .step format</li>
            <li>Fill in your contact and shipping information</li>
            <li>Specify your printing details (color, quantity, etc.)</li>
            <li>Submit your order</li>
            <li>We'll contact you with a quote and timeline</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # Create a form with styling
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">🔍 Upload Your Design</div>', unsafe_allow_html=True)
    
    with st.form("order_form"):
        # File uploader - only accepts .step files
        uploaded_file = st.file_uploader("Upload your CAD file", type=["step"], 
                                        help="Please upload your CAD file in .step format")
        
        # Personal Information Section
        st.markdown("""
        <div class="section-header" style="margin-top:20px;">
            👤 Personal Information
        </div>
        """, unsafe_allow_html=True)
        
        # Two columns for personal information
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name*", help="Enter your full name")
            email = st.text_input("Email Address*", help="Enter your email address")
            phone = st.text_input("Phone Number*", help="Enter your phone number")
        
        with col2:
            address_line1 = st.text_input("Street Address*", help="Enter your street address")
            address_line2 = st.text_input("Apt/Suite/Other", help="Optional additional address information")
            city = st.text_input("City*", help="Enter your city")
            state = st.text_input("State/Province*", help="Enter your state or province")
            zip_code = st.text_input("ZIP/Postal Code*", help="Enter your ZIP or postal code")
            country = st.text_input("Country*", help="Enter your country")
        
        # Order details section
        st.markdown("""
        <div class="section-header" style="margin-top:20px;">
            🎨 Printing Specifications
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            color = st.selectbox("Material Color", 
                                options=["Black", "White", "Gray", "Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Custom"])
        
        with col2:
            if color == "Custom":
                custom_color = st.text_input("Specify Custom Color")
            
            quantity = st.number_input("Quantity", min_value=1, value=1, step=1)
        
        special_instructions = st.text_area("Special Instructions", 
                                          help="Any special requirements for your order")
        
        # Terms and submit
        st.markdown("<hr style='margin: 1.5rem 0'>", unsafe_allow_html=True)
        terms_agreement = st.checkbox("I agree to the terms and conditions*")
        submit_button = st.form_submit_button("Submit Order")
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close the card
    
    # Handle form submission (this is outside the form)
    if submit_button:
        # Validate required fields
        required_fields = [
            (name, "Full Name"), 
            (email, "Email Address"), 
            (phone, "Phone Number"),
            (address_line1, "Street Address"),
            (city, "City"),
            (state, "State/Province"),
            (zip_code, "ZIP/Postal Code"),
            (country, "Country")
        ]
        
        missing_fields = [field_name for value, field_name in required_fields if not value]
        
        # Check file upload
        if uploaded_file is None:
            st.error("Please upload a .step file.")
        # Check terms agreement
        elif not terms_agreement:
            st.error("You must agree to the terms and conditions.")
        # Check required fields
        elif missing_fields:
            st.error(f"Please fill in the following required fields: {', '.join(missing_fields)}")
        # Process the order
        else:
            # Show processing message with spinner
            with st.spinner("Processing your order..."):
                # Save the uploaded file
                if uploaded_file is not None:
                    # Create orders directory if it doesn't exist
                    if not os.path.exists("orders"):
                        os.makedirs("orders")
                    
                    # Create a timestamped order ID
                    order_id = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{name.replace(' ', '_')}"
                    
                    # Create order directory
                    order_dir = os.path.join("orders", order_id)
                    os.makedirs(order_dir, exist_ok=True)
                    
                    # Save the file
                    file_path = os.path.join(order_dir, uploaded_file.name)
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    
                    # Save order details to a text file
                    order_details_path = os.path.join(order_dir, "order_details.txt")
                    with open(order_details_path, "w") as f:
                        f.write(f"Order ID: {order_id}\n")
                        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                        f.write(f"Name: {name}\n")
                        f.write(f"Email: {email}\n")
                        f.write(f"Phone: {phone}\n\n")
                        f.write(f"Shipping Address:\n")
                        f.write(f"{address_line1}\n")
                        if address_line2:
                            f.write(f"{address_line2}\n")
                        f.write(f"{city}, {state} {zip_code}\n")
                        f.write(f"{country}\n\n")
                        f.write(f"Order Details:\n")
                        selected_color = custom_color if color == "Custom" else color
                        f.write(f"Color: {selected_color}\n")
                        f.write(f"Quantity: {quantity}\n")
                        f.write(f"Special Instructions: {special_instructions}\n")
                    
                    # Send email notification
                    try:
                        # Create email content
                        email_subject = f"New 3D Printing Order - {order_id}"
                        email_body = f"""
                        New 3D Printing Order Received
                        
                        Order ID: {order_id}
                        Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                        
                        Customer Information:
                        Name: {name}
                        Email: {email}
                        Phone: {phone}
                        
                        Shipping Address:
                        {address_line1}
                        {address_line2 if address_line2 else ""}
                        {city}, {state} {zip_code}
                        {country}
                        
                        Order Details:
                        Material Color: {selected_color}
                        Quantity: {quantity}
                        Special Instructions: {special_instructions}
                        
                        File: {uploaded_file.name}
                        """
                        
                        # Get email configuration from secrets
                        sender_email = st.secrets["email"]["sender_email"]
                        receiver_email = st.secrets["email"]["receiver_email"]
                        smtp_server = st.secrets["email"]["smtp_server"]
                        smtp_port = st.secrets["email"]["smtp_port"]
                        email_password = st.secrets["email"]["password"]
                        
                        # Create message
                        message = MIMEMultipart()
                        message["From"] = sender_email
                        message["To"] = receiver_email
                        message["Subject"] = email_subject
                        
                        # Add body to email
                        message.attach(MIMEText(email_body, "plain"))
                        
                        # Attach the uploaded .step file
                        with open(file_path, "rb") as file:
                            attachment = MIMEApplication(file.read(), Name=uploaded_file.name)
                        attachment["Content-Disposition"] = f'attachment; filename="{uploaded_file.name}"'
                        message.attach(attachment)
                        
                        # Send email
                        with smtplib.SMTP(smtp_server, smtp_port) as server:
                            server.starttls()  # Secure the connection
                            server.login(sender_email, email_password)
                            server.send_message(message)
                            
                        st.markdown("""
                        <div style="background-color: #D4EDDA; color: #155724; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
                            <strong>✅ Email notification sent successfully</strong> to sbussiso321@gmail.com
                        </div>
                        """, unsafe_allow_html=True)
                        
                    except Exception as e:
                        st.warning(f"Could not send email notification: {str(e)}")
                    
                    # Success card with order details
                    st.markdown(f"""
                    <div class="card success-message" style="background-color: #D1F2EB; border-left: 5px solid #1ABC9C;">
                        <h2 style="color: #117A65; margin-top: 0;">Order Submitted Successfully! 🎉</h2>
                        <p><strong>Order ID:</strong> {order_id}</p>
                        <p>Thank you for your order! We've received your design and details.</p>
                        <p>We'll review your order and contact you shortly with pricing and timeline information.</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Show order summary
                    with st.expander("View Order Summary", expanded=True):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown("### 👤 Customer Details")
                            st.markdown(f"**Name:** {name}")
                            st.markdown(f"**Email:** {email}")
                            st.markdown(f"**Phone:** {phone}")
                        
                        with col2:
                            st.markdown("### 📦 Shipping Details")
                            st.markdown(f"**Address:** {address_line1}")
                            if address_line2:
                                st.markdown(f"{address_line2}")
                            st.markdown(f"{city}, {state} {zip_code}")
                            st.markdown(f"{country}")
                        
                        st.markdown("### 🖨️ Print Details")
                        st.markdown(f"**File:** {uploaded_file.name}")
                        st.markdown(f"**Color:** {selected_color}")
                        st.markdown(f"**Quantity:** {quantity}")
                        
                        if special_instructions:
                            st.markdown("### 📝 Special Instructions")
                            st.markdown(special_instructions)
            
            # Display confetti animation
            st.balloons()
    
    # Footer
    company_name = st.secrets["settings"]["company_name"]
    support_email = st.secrets["settings"]["support_email"]
    current_year = datetime.now().year
    
    st.markdown(f"""
    <div class="footer">
        <p style="color: #34495E;">© {current_year} {company_name}. All rights reserved.</p>
        <p style="color: #34495E;">Questions? Contact us at {support_email}</p>
    </div>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()