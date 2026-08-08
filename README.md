Developed By: Mustafa Mehmood Javed

## 📌 Overview

CryptoTraceX is a cybersecurity application developed to demonstrate the detection, analysis, and investigation of cryptocurrency-related malware in a safe and controlled environment.

Cryptocurrency malware can target digital wallets, browser information, clipboard data, credentials, private keys, and other sensitive information associated with cryptocurrency transactions. Such threats can result in financial loss and unauthorized access to digital assets.

CryptoTraceX provides an educational platform that demonstrates the workflow used during a cryptocurrency malware investigation. The system combines static analysis, simulated dynamic analysis, Indicators of Compromise (IOC) extraction, cryptocurrency wallet investigation, threat intelligence visualization, database storage, and automated PDF reporting.

The project uses simulated malware behavior for educational purposes and does **not execute real malicious software**.

---

## 🎯 Project Objectives

The main objectives of CryptoTraceX are:

- Perform static malware analysis.
- Extract Indicators of Compromise (IOCs).
- Identify suspicious URLs, IP addresses, email addresses, and cryptocurrency wallet addresses.
- Calculate and display file hashes such as SHA256.
- Simulate suspicious cryptocurrency malware behavior.
- Investigate suspicious cryptocurrency wallets.
- Present threat intelligence through an interactive dashboard.
- Store investigation results using SQLite.
- Maintain a history of previous investigations.
- Generate automated PDF threat reports.
- Display live cryptocurrency market information.
- Provide a centralized environment for educational malware investigation.

---

## 🚀 Key Features

### 🔑 1. Authentication System
CryptoTraceX starts with a login interface that provides controlled access to the application.
- Username authentication
- Password authentication
- Project identification
- Developer information
- Live cryptocurrency market information

### 🔍 2. Static Malware Analysis
Examines suspicious files without execution to gather baseline intel:
- File name & size
- SHA256 cryptographic hash
- Extracted URLs, IP addresses, and email addresses
- Extracted cryptocurrency wallet addresses
- Suspicious indicator highlights & risk metrics

### 🧩 3. Indicators of Compromise (IOC) Extraction
Extracts and categorizes actionable artifacts:
- Network IOCs (IPs, URLs)
- Communication channels (Emails)
- Financial targets (Crypto Wallet Addresses)
- File Fingerprints (SHA256 Hashes)

### 🦠 4. Dynamic Malware Analysis
A **safe sandbox simulation** of malicious runtime behavior:
- Clipboard hijacking monitoring
- Browser credential harvesting attempts
- Registry modification for persistence
- DNS query telemetry
- Command-and-Control (C2) communication patterns

### ₿ 5. Blockchain Intelligence
Investigates targeted cryptocurrency wallets and blockchain-linked metrics, demonstrating how on-chain intelligence supports cybercrime investigations.

### 📊 6. Threat Intelligence Dashboard
Consolidates raw data into interactive visualizations:
- Consolidated analysis metrics
- Aggregated IOC categorizations
- Risk scoring and wallet intelligence summary
- Overall investigation telemetry

### 💰 7. Live Cryptocurrency Market Rates
Provides real-time financial context directly on the login panel via the **CoinGecko API**:

| Cryptocurrency | Symbol |
|---|---|
| Bitcoin | BTC |
| Ethereum | ETH |
| Solana | SOL |

Retrieves real-time USD price data and 24-hour price variations with resilient error handling.

### 🗄️ 8. Database & Analysis History
Powered by **SQLite**, allowing users to persist analysis outputs, store full session histories, and review past case files without re-running scans.

### 📄 9. Automated PDF Threat Reports
Uses **ReportLab** to generate exportable, structured PDF executive summaries including file hashes, risk profiles, IOC lists, wallet findings, and forensic timelines.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Core application logic |
| **Streamlit** | Web interface & interactive frontend |
| **SQLite** | Local relational database storage |
| **Pandas** | Data structuring & tabular processing |
| **Plotly** | Interactive visualization widgets |
| **ReportLab** | Document generation & PDF layout engine |
| **Requests** | HTTP client for external API calls |
| **CoinGecko API** | Live market data telemetry |
| **Git & GitHub** | Source code management & repository host |
| **VS Code** | Primary Integrated Development Environment |

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │        Login        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Dashboard      │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
      ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
      │   Static     │ │   Dynamic    │ │  Blockchain  │
      │  Analysis    │ │  Analysis    │ │ Intelligence │
      └──────┬───────┘ └──────┬───────┘ └──────┬───────┘
             │                │                │
             └────────────────┼────────────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │ Threat Intelligence  │
                   │      Dashboard       │
                   └──────────┬───────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
             ┌──────────────┐    ┌──────────────┐
             │   Database   │    │ PDF Reports  │
             │  & History   │    │ Generation   │
             └──────────────┘    └──────────────┘


📂 Project StructurePlaintextCryptoTraceX/
│
├── app.py
├── static_analysis/
│   └── Static analysis modules
├── dynamic_analysis/
│   └── Dynamic analysis modules
├── blockchain/
│   └── Blockchain intelligence modules
├── dashboard/
│   └── Dashboard components
├── database/
│   └── cryptotracex.db
├── reports/
│   └── PDF report generation modules
├── uploads/
│   └── Uploaded analysis files
├── requirements.txt
└── README.md

⚙️ InstallationStep 1 — Clone the RepositoryBashgit clone [https://github.com/mustafajaved304/CryptoTraceX.git](https://github.com/mustafajaved304/CryptoTraceX.git)
Step 2 — Open the Project DirectoryBashcd CryptoTraceX
Step 3 — Create a Virtual EnvironmentBashpython -m venv venv
Step 4 — Activate the Virtual EnvironmentWindows:Bashvenv\Scripts\activate
Linux/macOS:Bashsource venv/bin/activate
Step 5 — Install Required DependenciesBashpip install -r requirements.txt
(If requests is missing from your requirements file, run pip install requests)▶️ Running the ApplicationAfter activating your virtual environment, launch the Streamlit server:Bashstreamlit run app.py
Open the provided local URL (typically http://localhost:8501) in your browser to access CryptoTraceX.🔐 Application WorkflowPlaintextLogin ──► Dashboard ──► Select Module (Static / Dynamic) ──► IOC Extraction
                              │
                              ▼
                     Blockchain Intelligence
                              │
                              ▼
                Threat Intelligence Visualization
                              │
                              ▼
                     Save to DB & History ──► Export PDF Report
🔬 Static Analysis WorkflowPlaintextFile Upload ──► File Identification ──► SHA256 Hash Generation ──► IOC Extraction ──► Classification ──► Risk Score
🦠 Dynamic Analysis WorkflowPlaintextStart Simulation ──► Simulated Behavior ──► Event Capture ──► Threat Classification ──► Results Summary
₿ Cryptocurrency Investigation WorkflowPlaintextTarget Wallet Address ──► On-Chain Query ──► Historical Telemetry ──► Risk Exposure ──► Threat Intel Summary
📊 Threat Intelligence WorkflowPlaintextStatic Intel  ──┐
Dynamic Intel ──┼──► Threat Intel Dashboard ──► [IOCs | Risk Metrics | Wallet Data | Statistics]
Chain Intel   ──┘
💰 Cryptocurrency APIIntegrated via CoinGecko REST API supporting real-time lookups for Bitcoin (BTC), Ethereum (ETH), and Solana (SOL). Includes automated fallbacks in the event of rate limits or connection dropouts.🗃️ DatabaseBuilt on SQLite (cryptotracex.db) to enable:Persistent analysis session logsDirect access to historical scan filesRapid re-evaluation without repeating computational tasks📄 Report GenerationUses ReportLab to convert raw JSON/SQLite findings into clean, multi-page security documentation:PlaintextRaw Analysis Data ──► Data Formatter ──► ReportLab Engine ──► PDF Threat Report
🧪 Testing SummaryComponentStatusLogin System✅ PassedDashboard✅ PassedStatic Analysis✅ PassedIOC Extraction✅ PassedDynamic Analysis✅ PassedBlockchain Intelligence✅ PassedThreat Intelligence Dashboard✅ PassedLive Cryptocurrency Rates✅ PassedDatabase Storage✅ PassedAnalysis History✅ PassedPDF Report Generation✅ Passed📈 ResultsCryptoTraceX provides a fully functional, self-contained educational tool that successfully demonstrates end-to-end malware triage, IOC extraction, blockchain correlation, and executive reporting within a clean Streamlit interface.⚠️ LimitationsDynamic behavior is entirely simulated for execution safety; no hypervisor/kernel sandbox drivers are included.On-chain wallet analytics are scoped for demonstration purposes.Market data is subject to CoinGecko public API availability and rate limits.Designed purely as an educational tool rather than an enterprise-grade CTI solution.🔮 Future EnhancementsReal-time blockchain transaction stream trackingSupport for additional UTXO and EVM chainsML-driven PE header malware classification modelsLive VirusTotal / AlienVault OTX API integrationInteractive graph generation for wallet cluster analysis🔒 Security & SafetyCryptoTraceX is designed strictly for educational and defensive cybersecurity analysis. All dynamic analysis runs in a simulated state; no live malware binary execution takes place.📚 Educational FocusThis project demonstrates practical concepts in:Malware Static & Dynamic TriageIndicators of Compromise (IOC) ManagementThreat Intelligence CorrelationBlockchain Cybercrime TrackingDefensive Security Reporting👨‍💻 DeveloperMustafa Mehmood JavedProject: CryptoTraceX — Cryptocurrency Malware Tracking SystemProject Type: OEL-1Stack: Python / Streamlit / SQLite / Plotly / ReportLab🔗 GitHub Repository: CryptoTraceX Repository📜 LicenseThis project is created for educational and academic research purposes.⭐ AcknowledgementCryptoTraceX was developed as an academic cybersecurity project to demonstrate practical concepts of cryptocurrency malware tracking, threat intelligence, and security reporting.© 2026 Mustafa Mehmood Javed — CryptoTraceX
