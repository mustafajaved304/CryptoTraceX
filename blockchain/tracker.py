"""
CryptoTraceX
Blockchain Wallet Tracker

This module simulates blockchain intelligence.
No real blockchain API is used.
"""

import random
from datetime import datetime


class BlockchainTracker:

    def __init__(self):
        pass

    def random_hash(self):

        chars = "abcdef0123456789"

        tx = ""

        for _ in range(64):
            tx += random.choice(chars)

        return tx

    def detect_blockchain(self, wallet):

        if wallet.startswith("0x"):
            return "Ethereum"

        return "Bitcoin"

    def generate_transactions(self, wallet):

        txs = []

        total = random.randint(3, 10)

        for i in range(total):

            txs.append({

                "txid": self.random_hash(),

                "amount": round(random.uniform(0.001, 4.5), 4),

                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

                "wallet": wallet

            })

        return txs

    def calculate_balance(self, txs):

        balance = 0

        for tx in txs:

            balance += tx["amount"]

        return round(balance, 4)

    def calculate_risk(self, balance, tx_count):

        score = 0

        if balance > 8:
            score += 50

        elif balance > 3:
            score += 30

        else:
            score += 10

        if tx_count > 7:
            score += 50

        elif tx_count > 4:
            score += 30

        else:
            score += 10

        if score >= 80:
            return "HIGH"

        elif score >= 50:
            return "MEDIUM"

        return "LOW"

    def lookup(self, wallet):

        blockchain = self.detect_blockchain(wallet)

        txs = self.generate_transactions(wallet)

        balance = self.calculate_balance(txs)

        risk = self.calculate_risk(balance, len(txs))

        return {

            "wallet": wallet,

            "blockchain": blockchain,

            "balance": balance,

            "transactions": len(txs),

            "risk": risk,

            "history": txs

        }


if __name__ == "__main__":

    tracker = BlockchainTracker()

    report = tracker.lookup(

        "1BoatSLRHtKNngkdXEeobR76b53LETtpyT"

    )

    print("=" * 60)

    print("Wallet Intelligence")

    print("=" * 60)

    print("Wallet :", report["wallet"])

    print("Blockchain :", report["blockchain"])

    print("Balance :", report["balance"])

    print("Transactions :", report["transactions"])

    print("Risk :", report["risk"])

    print()

    print("Transaction History")

    print("-" * 60)

    for tx in report["history"]:

        print(tx)