"""
CryptoTraceX
Dynamic Malware Analysis Simulator

This module simulates malware behaviour in a safe way.
No real malicious actions are performed.
"""

import random
import time
from datetime import datetime


class DynamicAnalyzer:

    def __init__(self):
        self.logs = []

    def log(self, event, status):
        self.logs.append({
            "time": datetime.now().strftime("%H:%M:%S"),
            "event": event,
            "status": status
        })

    def clipboard_hijack(self):
        time.sleep(0.5)

        wallets = [
            "1BoatSLRHtKNngkdXEeobR76b53LETtpyT",
            "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh",
            "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
        ]

        self.log(
            "Clipboard wallet replacement",
            random.choice(wallets)
        )

    def credential_theft(self):
        time.sleep(0.5)

        browsers = [
            "Chrome",
            "Edge",
            "Firefox"
        ]

        self.log(
            "Browser Credential Access",
            random.choice(browsers)
        )

    def registry_persistence(self):
        time.sleep(0.5)

        self.log(
            "Registry Run Key Created",
            "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        )

    def startup_folder(self):
        time.sleep(0.5)

        self.log(
            "Persistence File",
            "Startup Folder"
        )

    def network_activity(self):
        time.sleep(0.5)

        servers = [
            "185.199.108.153",
            "91.218.114.21",
            "172.67.23.15",
            "104.26.10.78"
        ]

        self.log(
            "Command & Control Connection",
            random.choice(servers)
        )

    def dns_query(self):
        time.sleep(0.5)

        domains = [
            "evil-wallet.com",
            "crypto-update.net",
            "wallet-check.org"
        ]

        self.log(
            "DNS Request",
            random.choice(domains)
        )

    def file_drop(self):
        time.sleep(0.5)

        files = [
            "payload.exe",
            "update.dll",
            "wallet.dll"
        ]

        self.log(
            "Dropped File",
            random.choice(files)
        )

    def process_injection(self):
        time.sleep(0.5)

        processes = [
            "explorer.exe",
            "svchost.exe",
            "chrome.exe"
        ]

        self.log(
            "Process Injection",
            random.choice(processes)
        )

    def execute(self):

        self.logs = []

        self.clipboard_hijack()
        self.credential_theft()
        self.registry_persistence()
        self.startup_folder()
        self.network_activity()
        self.dns_query()
        self.file_drop()
        self.process_injection()

        return self.logs


if __name__ == "__main__":

    analyzer = DynamicAnalyzer()

    results = analyzer.execute()

    print("=" * 60)
    print("CryptoTraceX Dynamic Analysis")
    print("=" * 60)

    for item in results:
        print(
            f"[{item['time']}] {item['event']} --> {item['status']}"
        )