# 🛡️ CryptoTraceX

## Cryptocurrency Malware Tracking System

CryptoTraceX is a cybersecurity project developed as part of **Open Ended Lab (OEL-1)**. The project simulates the analysis of cryptocurrency wallet-stealing malware by performing static analysis, dynamic behavior simulation, blockchain wallet tracking, and threat intelligence reporting through an interactive dashboard.

---

## 📖 Project Overview

Cryptocurrency theft is one of the fastest-growing cybercrime threats. Malware such as clipboard hijackers, keyloggers, and browser injectors target cryptocurrency users by stealing or replacing wallet addresses.

CryptoTraceX provides a safe simulation environment to analyze such threats by extracting Indicators of Compromise (IOCs), monitoring simulated malware behavior, tracking cryptocurrency wallets, and generating threat intelligence reports.

---

## ✨ Features

- 🔍 Static Malware Analysis
- ⚡ Dynamic Malware Analysis Simulation
- 🪙 Cryptocurrency Wallet Tracking
- 📊 Interactive Threat Intelligence Dashboard
- 📄 Automated PDF Report Generation
- 🗃️ SQLite Database Integration
- 📈 IOC Visualization using Charts
- 🔐 Secure Login System

---

## 🛠️ Technologies Used

- Python
- Streamlit
- SQLite
- Plotly
- ReportLab
- Pandas

---

## 📁 Project Structure

```
CryptoTraceX/
│
├── app.py
├── blockchain/
│   └── tracker.py
│
├── dashboard/
│   └── charts.py
│
├── database/
│   └── db.py
│
├── dynamic_analysis/
│   └── simulator.py
│
├── static_analysis/
│   ├── analyzer.py
│   └── ioc_extractor.py
│
├── reports/
│   └── pdf_report.py
│
├── malware_samples/
├── uploads/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CryptoTraceX.git
```

Go into the project directory

```bash
cd CryptoTraceX
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🔑 Login Credentials

Username

```
admin
```

Password

```
admin123
```

---

## 🔄 Workflow

1. Login to the application.
2. Upload a malware sample.
3. Perform Static Malware Analysis.
4. Extract Indicators of Compromise (IOCs).
5. Execute Dynamic Malware Analysis Simulation.
6. Track Cryptocurrency Wallets.
7. Visualize Threat Intelligence.
8. Generate a PDF Threat Report.
9. Review Analysis History.

---

## 📊 Modules

### Static Analysis

- SHA256 Hash Generation
- Wallet Extraction
- URL Detection
- IP Address Detection
- Email Extraction

### Dynamic Analysis

- Clipboard Hijacking Simulation
- Browser Credential Access
- Registry Persistence
- DNS Requests
- Command & Control Communication
- Dropped Files
- Process Injection

### Blockchain Intelligence

- Bitcoin Wallet Tracking
- Ethereum Wallet Tracking
- Transaction History
- Wallet Risk Assessment

### Reporting

- PDF Report Generation
- SQLite Database Storage
- Threat Intelligence Dashboard

---

## 📚 Academic Purpose

This project was developed for educational purposes to demonstrate concepts related to:

- Malware Analysis
- Reverse Engineering
- Threat Intelligence
- Blockchain Forensics
- Digital Investigation

---

## 👨‍💻 Developer

**Mustafa Mehmood Javed**


## 📄 License

This project is intended for educational and research purposes only.
