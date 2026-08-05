"""
CryptoTraceX
Professional PDF Threat Report
"""

import os
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)


class PDFReport:

    def __init__(self):

        os.makedirs("reports/output", exist_ok=True)

    def generate(self, report, wallet=None):

        filename = f"reports/output/Threat_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        title = styles["Heading1"]
        title.alignment = TA_CENTER

        story = []

        story.append(
            Paragraph(
                "CryptoTraceX Threat Intelligence Report",
                title
            )
        )

        story.append(Spacer(1, 20))

        story.append(

            Paragraph(

                f"<b>Generated:</b> {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",

                styles["Normal"]

            )

        )

        story.append(Spacer(1, 20))

        ##################################################################

        malware_table = [

            ["Field", "Value"],

            ["File", report["filename"]],

            ["SHA256", report["sha256"]],

            ["Risk", report["risk"]],

            ["Bitcoin Wallets", ", ".join(report["bitcoin"]) or "None"],

            ["Ethereum Wallets", ", ".join(report["ethereum"]) or "None"],

            ["URLs", ", ".join(report["urls"]) or "None"],

            ["IPs", ", ".join(report["ips"]) or "None"],

            ["Emails", ", ".join(report["emails"]) or "None"]

        ]

        table = Table(malware_table, colWidths=[170, 340])

        table.setStyle(TableStyle([

            ("BACKGROUND", (0,0), (-1,0), colors.darkblue),

            ("TEXTCOLOR", (0,0), (-1,0), colors.white),

            ("GRID", (0,0), (-1,-1), 1, colors.black),

            ("BACKGROUND", (0,1), (0,-1), colors.lightgrey),

            ("BOTTOMPADDING", (0,0), (-1,0), 10),

            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),

            ("FONTNAME", (0,1), (0,-1), "Helvetica-Bold")

        ]))

        story.append(table)

        story.append(Spacer(1, 25))

        ###########################################################

        if wallet:

            story.append(

                Paragraph(

                    "<b>Blockchain Intelligence</b>",

                    styles["Heading2"]

                )

            )

            story.append(Spacer(1, 10))

            wallet_table = [

                ["Wallet", wallet["wallet"]],

                ["Blockchain", wallet["blockchain"]],

                ["Balance", str(wallet["balance"])],

                ["Transactions", str(wallet["transactions"])],

                ["Risk", wallet["risk"]]

            ]

            t = Table(wallet_table, colWidths=[170,340])

            t.setStyle(TableStyle([

                ("GRID",(0,0),(-1,-1),1,colors.black),

                ("BACKGROUND",(0,0),(0,-1),colors.lightgrey),

                ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold")

            ]))

            story.append(t)

        story.append(Spacer(1,20))

        ##########################################################

        story.append(

            Paragraph(

                "<b>Conclusion</b>",

                styles["Heading2"]

            )

        )

        story.append(

            Paragraph(

                """
                The malware sample was successfully analysed.

                Indicators of Compromise (IOCs) were extracted and
                correlated with simulated blockchain intelligence.

                CryptoTraceX classified the sample according to
                detected wallets, URLs, IP addresses and email
                addresses.

                This report can be used for cyber threat
                intelligence and digital forensic investigations.

                """,

                styles["BodyText"]

            )

        )

        doc.build(story)

        return filename


############################################################

if __name__ == "__main__":

    sample = {

        "filename":"sample_malware.txt",

        "sha256":"495432d62ca160722fbe1a0849",

        "bitcoin":[

            "1BoatSLRHtKNngkdXEeobR76b53LETtpyT"

        ],

        "ethereum":[

            "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"

        ],

        "urls":[

            "https://evil-wallet.com"

        ],

        "ips":[

            "185.199.108.153"

        ],

        "emails":[

            "attacker@evil.com"

        ],

        "risk":"HIGH"

    }

    pdf = PDFReport()

    output = pdf.generate(sample)

    print(output)