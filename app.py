import os
import requests
import streamlit as st

from static_analysis.ioc_extractor import IOCExtractor
from dynamic_analysis.simulator import DynamicAnalyzer
from blockchain.tracker import BlockchainTracker
from dashboard.charts import DashboardCharts
from reports.pdf_report import PDFReport
from database.db import db

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="CryptoTraceX",
    page_icon="🛡️",
    layout="wide"
)

# =====================================================
# SESSION
# =====================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "report" not in st.session_state:
    st.session_state.report = None

if "wallet" not in st.session_state:
    st.session_state.wallet = None


# =====================================================
# LIVE CRYPTO PRICES
# =====================================================

def get_crypto_prices():
    try:
        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={
                "ids": "bitcoin,ethereum,solana",
                "vs_currencies": "usd",
                "include_24hr_change": "true"
            },
            timeout=5
        )

        if response.status_code == 200:
            return response.json()

    except Exception:
        return None

    return None

# =====================================================
# LOGIN PAGE
# =====================================================

if not st.session_state.logged_in:

    st.markdown("""
    <style>

    .main{
        background-color:#0E1117;
    }

    .login-box{
        background:#1E1E1E;
        padding:35px;
        border-radius:15px;
        box-shadow:0px 0px 20px rgba(0,255,170,.2);
    }

    h1,h2,h3,p{
        text-align:center;
    }

    </style>
    """, unsafe_allow_html=True)

    col1,col2,col3 = st.columns([1,2,1])

    with col2:

        # =================================================
        # LIVE CRYPTO MARKET RATES
        # =================================================

        crypto = get_crypto_prices()

        st.error("🔴 LIVE CRYPTO MARKET RATES")

        if crypto:
            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                    "₿ Bitcoin",
                    f"${crypto['bitcoin']['usd']:,.2f}",
                    f"{crypto['bitcoin'].get('usd_24h_change', 0):+.2f}%"
                )

            with c2:
                st.metric(
                    "Ξ Ethereum",
                    f"${crypto['ethereum']['usd']:,.2f}",
                    f"{crypto['ethereum'].get('usd_24h_change', 0):+.2f}%"
                )

            with c3:
                st.metric(
                    "◎ Solana",
                    f"${crypto['solana']['usd']:,.2f}",
                    f"{crypto['solana'].get('usd_24h_change', 0):+.2f}%"
                )
        else:
            st.warning("Live crypto prices are temporarily unavailable.")

        st.caption("● Live market data")
        st.divider()

        # Existing login interface

        st.markdown("""
        <div class="login-box">

        <h1>🛡️ CryptoTraceX</h1>

        <h3>Cryptocurrency Malware Tracking System</h3>

        <br>

    

        <p style="font-size:18px;">
        <b>Developed By</b>
        </p>

        <h2 style="color:#00FF99;">
        Mustafa Mehmood Javed
        </h2>

        <hr>

        </div>

        """, unsafe_allow_html=True)

        username = st.text_input(
            "Username"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button(
            "🔐 Login",
            use_container_width=True
        ):

            if username=="admin" and password=="admin123":

                st.session_state.logged_in=True
                st.rerun()

            else:

                st.error("Invalid Username or Password")

    st.stop()

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.image(
    "https://img.icons8.com/fluency/96/security-checked.png",
    width=80
)

st.sidebar.title("CryptoTraceX")

page = st.sidebar.radio(

    "Navigation",

    [

        "Dashboard",

        "Static Analysis",

        "Dynamic Analysis",

        "Blockchain",

        "History"

    ]

)

st.sidebar.markdown("---")

st.sidebar.success("Logged In")

if st.sidebar.button("Logout"):

    st.session_state.logged_in=False

    st.rerun()

# =====================================================
# DASHBOARD
# =====================================================

if page=="Dashboard":

    st.title("🛡 Threat Intelligence Dashboard")

    st.info("""
Welcome to **CryptoTraceX**.

This platform analyzes cryptocurrency wallet-stealing malware,
extracts Indicators of Compromise (IOCs),
tracks suspicious wallets,
and generates threat intelligence reports.
""")

    data = db.get_analysis()

    total = len(data)

    high = 0
    medium = 0
    low = 0

    for row in data:

        if row[8]=="HIGH":

            high+=1

        elif row[8]=="MEDIUM":

            medium+=1

        else:

            low+=1

    a,b,c,d = st.columns(4)

    a.metric(
        "Samples Analysed",
        total
    )

    b.metric(
        "High Risk",
        high
    )

    c.metric(
        "Medium Risk",
        medium
    )

    d.metric(
        "Low Risk",
        low
    )

    st.divider()

    st.subheader("System Overview")

    st.write("""
✔ Static Malware Analysis

✔ Dynamic Malware Analysis

✔ IOC Extraction

✔ Blockchain Wallet Tracking

✔ Threat Intelligence Dashboard

✔ Automated PDF Reports
""")
    # =====================================================
# STATIC ANALYSIS
# =====================================================

elif page == "Static Analysis":

    st.title("🔍 Static Malware Analysis")

    st.write(
        "Upload a malware sample to extract Indicators of Compromise (IOCs)."
    )

    uploaded = st.file_uploader(
        "Choose a malware sample",
        type=["txt", "exe", "bin"]
    )

    if uploaded:

        os.makedirs("uploads", exist_ok=True)

        filepath = os.path.join("uploads", uploaded.name)

        with open(filepath, "wb") as f:
            f.write(uploaded.read())

        if st.button("Start Static Analysis"):

            extractor = IOCExtractor(filepath)

            report = extractor.extract()

            report["filename"] = uploaded.name

            st.session_state.report = report

            try:
                db.save_analysis(report)
            except:
                pass

            st.success("Static Analysis Completed Successfully")

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("File Information")

                st.code(report["sha256"])

                st.write("### Bitcoin Wallets")
                st.write(report["bitcoin"])

                st.write("### Ethereum Wallets")
                st.write(report["ethereum"])

            with col2:

                st.write("### URLs")
                st.write(report["urls"])

                st.write("### IP Addresses")
                st.write(report["ips"])

                st.write("### Emails")
                st.write(report["emails"])

                st.write("### Risk Level")

                if report["risk"] == "HIGH":
                    st.error(report["risk"])

                elif report["risk"] == "MEDIUM":
                    st.warning(report["risk"])

                else:
                    st.success(report["risk"])

            st.divider()

            st.subheader("IOC Statistics")

            st.plotly_chart(
                DashboardCharts.ioc_chart(report),
                use_container_width=True
            )

# =====================================================
# DYNAMIC ANALYSIS
# =====================================================

elif page == "Dynamic Analysis":

    st.title("⚡ Dynamic Malware Analysis")

    st.write("""
Run the malware inside a simulated sandbox environment.

The simulator observes:

• Clipboard Hijacking

• Browser Credential Access

• Registry Persistence

• DNS Requests

• Command & Control Communication

• Dropped Files

• Process Injection
""")

    if st.button("Run Dynamic Analysis"):

        analyzer = DynamicAnalyzer()

        logs = analyzer.execute()

        st.success("Dynamic Analysis Completed")

        st.divider()

        for log in logs:

            st.write(
                f"🟢 **[{log['time']}]**  {log['event']}  ➜  `{log['status']}`"
            )

# =====================================================
# BLOCKCHAIN TRACKER
# =====================================================

elif page == "Blockchain":

    st.title("₿ Blockchain Wallet Tracker")

    wallet = st.text_input(
        "Enter Bitcoin / Ethereum Wallet Address"
    )

    if st.button("Track Wallet"):

        if wallet.strip() == "":

            st.warning("Please enter a wallet address.")

        else:

            tracker = BlockchainTracker()

            result = tracker.lookup(wallet)

            st.session_state.wallet = result

            try:
                db.save_wallet(
                    result["wallet"],
                    result["blockchain"],
                    str(result["balance"]),
                    result["transactions"],
                    result["risk"]
                )
            except:
                pass

            st.success("Wallet Intelligence Generated")

            c1, c2 = st.columns(2)

            with c1:

                st.metric(
                    "Blockchain",
                    result["blockchain"]
                )

                st.metric(
                    "Balance",
                    result["balance"]
                )

            with c2:

                st.metric(
                    "Transactions",
                    result["transactions"]
                )

                st.metric(
                    "Threat Level",
                    result["risk"]
                )

            st.divider()

            st.subheader("Wallet Transaction History")

            st.plotly_chart(
                DashboardCharts.wallet_transactions(result),
                use_container_width=True
            )

            st.subheader("Wallet Summary")

            st.plotly_chart(
                DashboardCharts.wallet_summary(result),
                use_container_width=True
            )

            st.subheader("Threat Meter")

            st.plotly_chart(
                DashboardCharts.risk_meter(result["risk"]),
                use_container_width=True
            )
            # =====================================================
# HISTORY
# =====================================================

elif page == "History":

    st.title("📜 Analysis History")

    try:

        records = db.get_analysis()

    except:

        records = []

    if len(records) == 0:

        st.info("No analysis history available.")

    else:

        st.success(f"{len(records)} analysis record(s) found.")

        for row in records:

            with st.expander(f"📄 {row[1]}"):

                st.write("### SHA256")
                st.code(row[2])

                st.write("### Bitcoin Wallets")
                st.write(row[3])

                st.write("### Ethereum Wallets")
                st.write(row[4])

                st.write("### URLs")
                st.write(row[5])

                st.write("### IP Addresses")
                st.write(row[6])

                st.write("### Emails")
                st.write(row[7])

                st.write("### Risk")
                st.write(row[8])

                st.write("### Analysis Date")
                st.write(row[9])

# =====================================================
# PDF REPORT
# =====================================================

st.sidebar.markdown("---")

st.sidebar.subheader("📄 Generate Report")

if st.session_state.report is not None:

    if st.sidebar.button("Generate PDF"):

        pdf = PDFReport()

        try:

            pdf_file = pdf.generate(
                st.session_state.report,
                st.session_state.wallet
            )

        except:

            pdf_file = pdf.generate(
                st.session_state.report
            )

        st.sidebar.success("PDF Generated Successfully")

        with open(pdf_file, "rb") as f:

            st.sidebar.download_button(

                label="⬇ Download PDF",

                data=f,

                file_name=os.path.basename(pdf_file),

                mime="application/pdf"

            )

else:

    st.sidebar.info(
        "Run Static Analysis first."
    )

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.markdown(
"""
<div style="text-align:center;">

<h2 style="color:#00FF99;">
🛡 CryptoTraceX
</h2>

<h4>
Cryptocurrency Malware Tracking System
</h4>

<br>

<b>Open Ended Lab (OEL-1)</b>

<br><br>

<b>Developed By</b>

<h3 style="color:#00FF99;">
Mustafa Mehmood Javed
</h3>

<hr>

<p>
Version 1.0
</p>

<p>
© 2026 CryptoTraceX
</p>

</div>
""",
unsafe_allow_html=True
)
