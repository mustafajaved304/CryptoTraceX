"""
CryptoTraceX
Dashboard Charts
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


class DashboardCharts:

    @staticmethod
    def ioc_chart(report):

        df = pd.DataFrame({

            "IOC": [

                "Bitcoin Wallets",
                "Ethereum Wallets",
                "URLs",
                "IPs",
                "Emails"

            ],

            "Count": [

                len(report["bitcoin"]),
                len(report["ethereum"]),
                len(report["urls"]),
                len(report["ips"]),
                len(report["emails"])

            ]

        })

        fig = px.bar(

            df,

            x="IOC",

            y="Count",

            text="Count",

            title="Extracted Indicators of Compromise"

        )

        fig.update_layout(

            template="plotly_dark",

            height=450

        )

        return fig

    @staticmethod
    def risk_meter(risk):

        if risk == "HIGH":

            value = 90
            color = "red"

        elif risk == "MEDIUM":

            value = 60
            color = "orange"

        else:

            value = 25
            color = "green"

        fig = go.Figure(go.Indicator(

            mode="gauge+number",

            value=value,

            title={"text": "Threat Level"},

            gauge={

                "axis": {"range": [0, 100]},

                "bar": {"color": color},

                "steps": [

                    {"range": [0, 35], "color": "green"},

                    {"range": [35, 70], "color": "yellow"},

                    {"range": [70, 100], "color": "red"}

                ]

            }

        ))

        fig.update_layout(

            template="plotly_dark",

            height=350

        )

        return fig

    @staticmethod
    def wallet_transactions(wallet):

        tx = wallet["history"]

        df = pd.DataFrame(tx)

        fig = px.bar(

            df,

            x=df.index,

            y="amount",

            text="amount",

            title="Wallet Transaction History"

        )

        fig.update_layout(

            template="plotly_dark",

            xaxis_title="Transaction",

            yaxis_title="Amount"

        )

        return fig

    @staticmethod
    def wallet_summary(wallet):

        labels = [

            "Balance",

            "Transactions"

        ]

        values = [

            wallet["balance"],

            wallet["transactions"]

        ]

        fig = px.pie(

            names=labels,

            values=values,

            hole=.55,

            title="Wallet Summary"

        )

        fig.update_layout(

            template="plotly_dark",

            height=400

        )

        return fig