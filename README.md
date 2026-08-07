# CryptoTraceX — Cryptocurrency Malware Tracking System


### Developed By

**Mustafa Mehmood Javed**

### Project Title

**CryptoTraceX — Cryptocurrency Malware Tracking System**

---

## 1. Introduction

CryptoTraceX is a cybersecurity-based application developed for the analysis and investigation of cryptocurrency-related malware. Cryptocurrency malware can target digital wallets, browser information, clipboard data, private keys, and other sensitive information used in cryptocurrency transactions.

The purpose of CryptoTraceX is to demonstrate how cybersecurity professionals can analyze suspicious malware samples, extract Indicators of Compromise (IOCs), simulate malicious activities, investigate cryptocurrency wallets, and generate threat intelligence reports.

The project uses a safe and educational simulation approach instead of executing real malicious software.

---

## 2. Project Objectives

The main objectives of CryptoTraceX are:

- To perform static malware analysis
- To extract Indicators of Compromise (IOCs)
- To identify suspicious URLs, IP addresses, emails, and wallet addresses
- To simulate dynamic malware behavior
- To perform cryptocurrency wallet tracking
- To visualize threat intelligence information
- To store investigation results in a database
- To generate automated PDF threat reports
- To provide an interactive cybersecurity dashboard

---

## 3. System Overview

CryptoTraceX is a Python-based cybersecurity application developed using Streamlit. The application provides an interactive dashboard through which users can perform different malware investigation and cryptocurrency intelligence tasks.

The system contains multiple modules including authentication, static analysis, dynamic analysis, blockchain intelligence, threat intelligence visualization, analysis history, and PDF report generation.

The project is designed as an educational tool for understanding the workflow of cryptocurrency malware investigation.

---

## 4. Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main Programming Language |
| Streamlit | Web Dashboard |
| SQLite | Database Storage |
| Pandas | Data Processing |
| Plotly | Data Visualization |
| ReportLab | PDF Report Generation |
| Requests | Live Cryptocurrency Data |
| CoinGecko API | Cryptocurrency Market Data |
| Git | Version Control |
| GitHub | Source Code Repository |
| VS Code | Development Environment |

---

## 5. System Requirements

### Hardware

- Intel Core i3 processor or above
- Minimum 4 GB RAM
- Minimum 1 GB free storage
- Internet connection for live cryptocurrency prices

### Software

- Windows 10/11
- Python 3.13
- Visual Studio Code
- Git
- Streamlit
- Required Python libraries

---

## 6. Project Methodology

The system follows a structured malware investigation workflow:

1. User opens the CryptoTraceX application.
2. User logs into the system.
3. The dashboard provides access to investigation modules.
4. A malware sample can be submitted for static analysis.
5. Static analysis extracts important Indicators of Compromise.
6. Dynamic analysis simulates suspicious malware activities.
7. Cryptocurrency wallet information is investigated.
8. Threat intelligence information is visualized.
9. Analysis results are stored in the database.
10. A PDF threat report can be generated.
11. Previous investigations can be reviewed through the history section.

---

## 7. Login Module

The application starts with a login interface that provides access to the CryptoTraceX system.

The login page contains the project title, developer information, username and password fields, and login functionality.

The login interface also displays a live cryptocurrency market section showing current prices of major cryptocurrencies including:

- Bitcoin (BTC)
- Ethereum (ETH)
- Solana (SOL)

The cryptocurrency information is retrieved through the CoinGecko API.

---

## 8. Dashboard Module

After successful authentication, the user is provided with the main CryptoTraceX dashboard.

The dashboard provides access to the major modules of the system, including:

- Static Analysis
- Dynamic Analysis
- Blockchain Intelligence
- Threat Intelligence Dashboard
- Analysis History
- PDF Report Generation

The dashboard acts as the central navigation point for the complete malware investigation workflow.

---

## 9. Static Malware Analysis

The Static Analysis module examines a malware sample without executing it.

The system analyzes the submitted sample and extracts useful information such as:

- File name
- File size
- SHA256 hash
- URLs
- IP addresses
- Email addresses
- Cryptocurrency wallet addresses
- Suspicious indicators
- Risk information

Static analysis helps investigators identify potentially malicious characteristics while keeping the sample inactive.

---

## 10. Indicators of Compromise (IOC) Extraction

Indicators of Compromise are important pieces of information that can be used to identify suspicious or malicious activity.

CryptoTraceX extracts different IOC types including:

- IP addresses
- URLs
- Email addresses
- Cryptocurrency wallet addresses
- File hashes

The extracted information can be used by security analysts during further investigation and threat intelligence analysis.

---

## 11. Dynamic Analysis

The Dynamic Analysis module provides a safe simulation of suspicious malware behavior.

Instead of executing real malware, the system demonstrates possible malicious activities such as:

- Clipboard monitoring
- Browser credential access
- Registry persistence
- DNS communication
- Command-and-control communication

The simulated approach allows students to understand malware behavior without creating unnecessary security risks.

---

## 12. Blockchain Intelligence

The Blockchain Intelligence module focuses on cryptocurrency wallet investigation.

The system allows suspicious cryptocurrency wallet addresses to be investigated and provides information related to wallet activity and risk assessment.

This module demonstrates how blockchain information can be used as part of a cryptocurrency-related cybercrime investigation.

---

## 13. Threat Intelligence Dashboard

The Threat Intelligence Dashboard provides a graphical representation of collected security information.

Charts and visual elements help investigators understand:

- Threat indicators
- Malware analysis results
- Wallet intelligence
- Risk information
- Investigation statistics

The dashboard makes complex security information easier to understand and interpret.

---

## 14. Live Cryptocurrency Market Rates

CryptoTraceX also provides a live cryptocurrency market section.

The login interface displays current market information for:

- Bitcoin
- Ethereum
- Solana

The system retrieves the current USD price and 24-hour price change through the CoinGecko API.

This feature provides additional cryptocurrency context within the investigation environment.

---

## 15. Database and Analysis History

The application uses SQLite for storing investigation information.

Completed analysis results can be stored and reviewed later through the History module.

Database storage allows the system to maintain previous investigation records and provides a simple way to review historical analysis results.

---

## 16. PDF Threat Report Generation

CryptoTraceX includes an automated PDF report generation feature.

After completing an investigation, the system can generate a structured threat report containing important analysis information.

The generated report can include:

- Malware information
- Hash information
- Extracted IOCs
- Risk assessment
- Wallet information
- Investigation results

This feature demonstrates how security analysts can document their findings in a professional format.

---

## 17. Testing

The major modules of CryptoTraceX were tested during development.

| Module | Status |
|--------|--------|
| Login System | Passed |
| Dashboard | Passed |
| Static Analysis | Passed |
| IOC Extraction | Passed |
| Dynamic Analysis | Passed |
| Blockchain Intelligence | Passed |
| Threat Intelligence Dashboard | Passed |
| Live Crypto Rates | Passed |
| Database Storage | Passed |
| Analysis History | Passed |
| PDF Report Generation | Passed |

---

## 18. Results

The completed CryptoTraceX system successfully demonstrates the basic workflow of cryptocurrency malware investigation.

The system can analyze simulated malware samples, extract Indicators of Compromise, simulate suspicious activities, investigate cryptocurrency wallets, visualize threat intelligence information, store investigation results, and generate PDF reports.

The addition of live cryptocurrency market information also provides current Bitcoin, Ethereum, and Solana market data within the application.

---

## 19. Limitations

The project has some limitations:

- Dynamic malware analysis is simulated rather than real malware execution.
- Blockchain investigation is designed for educational purposes.
- Some threat intelligence information is simulated.
- Live cryptocurrency prices depend on external API availability.
- The system is intended for educational and demonstration purposes rather than production-level malware investigation.

---

## 20. Future Enhancements

Possible future improvements include:

- Integration with real malware sandbox environments
- Integration with additional threat intelligence APIs
- Real-time blockchain transaction tracking
- Multiple cryptocurrency network support
- Advanced malware behavior analysis
- Machine learning-based malware classification
- Automated IOC reputation checking
- Real-time security alerts
- Advanced user authentication
- Expanded threat intelligence visualization

---

## 21. Conclusion

CryptoTraceX is an educational Cryptocurrency Malware Tracking System developed to demonstrate important cybersecurity concepts related to malware analysis, Indicators of Compromise, cryptocurrency investigations, blockchain intelligence, and threat reporting.

The project combines static analysis, simulated dynamic analysis, wallet investigation, database storage, visualization, live cryptocurrency information, and automated PDF reporting into a single Streamlit-based application.

The project provides practical experience in developing a cybersecurity investigation platform while demonstrating how cryptocurrency-related threats can be analyzed in a controlled and safe environment.

---

## 22. Repository

**GitHub Repository:**

`https://github.com/mustafajaved304/CryptoTraceX`


## 23. Developer

**Mustafa Mehmood Javed**

**Project:** CryptoTraceX — Cryptocurrency Malware Tracking System

