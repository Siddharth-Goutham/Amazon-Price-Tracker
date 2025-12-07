📦 Amazon Price Tracker (Python)

A Python-based Amazon Price Tracker that monitors product prices and sends an email notification when the price drops below a desired value.


🚀 Features
- Tracks Amazon product price automatically  
- Sends email alerts when price drops  
- Uses environment variables for secure credentials  
- Lightweight and easy to run  


🛠️ Technologies Used
- Python 3  
- requests  
- beautifulsoup4  
- python-dotenv  


📂 Project Setup

1. Download the Project
- Download the project as a ZIP from GitHub  
- Extract the folder  
- Open the folder in your code editor  


2. Install Required Libraries

Run the following command in the terminal:

pip install requests beautifulsoup4 python-dotenv


3. Create a .env File (Important)

Create a file named `.env` in the project root and add:

SMTP_ADDRESS=smtp.gmail.com  
EMAIL=your_email@gmail.com  
EMAIL_PASSWORD=your_app_password  


🔑 How to Generate a Gmail App Password

Since Google does not allow regular Gmail passwords for apps anymore, you must generate an App Password.

Steps:

1. Go to:
https://myaccount.google.com/security  

2. Enable **2-Step Verification** (if it is not already enabled)

3. After enabling 2-Step Verification:
- Search for **App Passwords**
- Enter your Gmail password for verification
- Type the app name as: Amazon Price Tracker
- Click **Generate**

4. Google will generate a 16-character password

5. Copy that password and paste it into your `.env` file like this:

EMAIL_PASSWORD=your_app_password

⚠️ Do NOT use your real Gmail password. Always use a Gmail App Password.


4. Run the Program!!


🔐 Security Notice
- The `.env` file is not uploaded to GitHub for security reasons  
- Each user must create their own `.env` file with personal credentials  
- This is standard industry practice for handling secrets safely  


📌 Use Case
This project is useful for:
- Tracking product price drops  
- Learning web scraping  
- Learning email automation in Python  
- Understanding secure environment variable usage  


👨‍💻 Author

Siddharth Goutham  
Python Project – Amazon Price Tracker
