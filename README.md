# CADIA 3D Printing Order Form

A Streamlit application for collecting 3D printing orders, including file uploads and customer information.

## Features

- File upload for .step CAD files
- Customer information collection
- Order details and preferences
- Email notifications with file attachments
- Clean, modern UI

## Setup Instructions

### Local Development

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your secrets:
   - Create a `.streamlit/secrets.toml` file with your email configuration:
   ```toml
   [email]
   sender_email = "your-email@gmail.com"
   receiver_email = "your-email@gmail.com"
   smtp_server = "smtp.gmail.com"
   smtp_port = 587
   password = "your-app-password"  # For Gmail, use an App Password

   [settings]
   company_name = "CADIA 3D Printing Service"
   support_email = "support@cadia3dprinting.com"
   ```

4. Run the app:
   ```
   streamlit run app.py
   ```

### Deployment to Streamlit Cloud

1. Push your code to GitHub (make sure to include the requirements.txt file)
2. Sign up for [Streamlit Cloud](https://streamlit.io/cloud)
3. Create a new app by connecting to your GitHub repository
4. Add your secrets in the Streamlit Cloud dashboard:
   - Go to your app > Advanced settings > Secrets
   - Add the same secrets configuration as in the local development setup

## Gmail App Password Setup

To send emails using Gmail:

1. Enable 2-Step Verification on your Google account
2. Generate an App Password:
   - Go to your Google Account > Security
   - Under "Signing in to Google," select "App passwords"
   - Select "Mail" and "Other" (Custom name: "CADIA 3D Printing App")
   - Use the generated password in your secrets.toml file

## File Structure

- `app.py`: Main application code
- `.streamlit/secrets.toml`: Configuration secrets (not included in repository)
- `orders/`: Directory where uploaded files and order details are saved
- `requirements.txt`: Python dependencies
- `README.md`: This file

## Support

For questions or issues, please contact support@cadia3dprinting.com 