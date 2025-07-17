import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials

sheet_id = "Example sheet ID, replace with your actual ID"  

# === STEP 1: Set up Google Sheets credentials ===
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("SERVICE ACCOUNT KEY HERE", scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open_by_key(sheet_id).sheet1

# === STEP 2: Scrape data ===
url = "http://books.toscrape.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# Extract book data
books = soup.select('.product_pod')

# Prepare header row
header = ["Title", "Price", "Rating"]
sheet.clear()  # clear old content before writing
sheet.append_row(header)  # Add column headers

# Go through each book
for book in books:
    title = book.h3.a['title']
    price = book.select_one('.price_color').text.strip()
    rating = book.select_one('p.star-rating')['class'][1]  # e.g. 'One', 'Two', etc.

    # Append the row to the sheet
    row = [title, price, rating]
    sheet.append_row(row)
