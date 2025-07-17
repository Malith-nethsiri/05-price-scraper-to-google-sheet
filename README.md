# 🛒 Price Scraper to Google Sheets Automation

This Python project scrapes product prices from a target website and automatically logs the data into a Google Sheet using the Google Sheets API.

## 🚀 Features
- Web scraping using `requests` and `BeautifulSoup`
- Google Sheets integration via `gspread` and service accounts
- Automates price tracking and logging
- Clean, tabular output in Sheets

## 🧠 Tech Stack
- Python
- BeautifulSoup
- gspread
- Google Sheets API

## ⚙️ Setup Instructions

### 1. Clone the repo

git clone https://github.com/your-username/05-price-scraper-to-google-sheet.git
cd 05-price-scraper-to-google-sheet

### 2. Install dependencies
    pip install -r requirements.txt

###3. Google Sheets API setup

      Create a Google Cloud Project      
      Enable Sheets API and Drive API      
      Create a service account and download the JSON key      
      Share your Google Sheet with the service account email

📂 Folder Structure

/05-price-scraper-to-google-sheet

│

├── main.py                 # Main script

├── united-kiln-*.json      # Service account key

├── requirements.txt

└── README.md

