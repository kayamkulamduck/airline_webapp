    # ✈️ Airline Booking Market Demand Web App

This is a Flask-based web app that fetches and displays airline market demand trends. It was built as part of a skill assessment for a Python Developer internship.

---

## 🔍 Features

- ✅ Scrapes real airline route data (via OpenFlights public dataset)
- 📊 Displays demand insights with simulated prices and popularity
- 🎨 Simple, responsive UI with charts and tables
- 🧰 Clean, modular code (scraping, processing, UI)
- 🧪 Easily swappable data sources (can connect to real airline APIs)

---

## 🛠️ Tech Stack

- Python 3.12
- Flask
- Pandas
- Plotly.js (for charts)
- HTML + Bootstrap

---

## 📦 Folder Structure

airline_webapp/
├── app.py # Flask app entrypoint
├── scraper.py # Route data scraper (from OpenFlights)
├── templates/
│ └── index.html # Frontend HTML template
├── venv/ # Virtual environment
├── requirements.txt # Python dependencies
└── README.md # You're reading it :)
