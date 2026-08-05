import hashlib
import re


class MalwareAnalyzer:

    def __init__(self, filepath):

        self.filepath = filepath

        with open(filepath, "r", errors="ignore") as file:

            self.content = file.read()

    def sha256(self):

        sha = hashlib.sha256()

        with open(self.filepath, "rb") as file:

            while True:

                chunk = file.read(4096)

                if not chunk:
                    break

                sha.update(chunk)

        return sha.hexdigest()

    def bitcoin(self):

        return re.findall(
            r"\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b",
            self.content
        )

    def ethereum(self):

        return re.findall(
            r"0x[a-fA-F0-9]{40}",
            self.content
        )

    def urls(self):

        return re.findall(
            r"https?://[^\s]+",
            self.content
        )

    def ips(self):

        return re.findall(
            r"(?:\d{1,3}\.){3}\d{1,3}",
            self.content
        )

    def emails(self):

        return re.findall(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            self.content
        )

    def risk(self):

        score = 0

        score += len(self.bitcoin()) * 40
        score += len(self.ethereum()) * 40
        score += len(self.urls()) * 10
        score += len(self.ips()) * 5
        score += len(self.emails()) * 5

        if score >= 80:
            return "HIGH"

        elif score >= 40:
            return "MEDIUM"

        return "LOW"

    def analyze(self):

        return {

            "sha256": self.sha256(),

            "bitcoin": self.bitcoin(),

            "ethereum": self.ethereum(),

            "urls": self.urls(),

            "ips": self.ips(),

            "emails": self.emails(),

            "risk": self.risk()

        }