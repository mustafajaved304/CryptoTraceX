from static_analysis.analyzer import MalwareAnalyzer


class IOCExtractor:

    def __init__(self, filepath):
        self.filepath = filepath

    def extract(self):

        analyzer = MalwareAnalyzer(self.filepath)

        result = analyzer.analyze()

        report = {

            "filename": self.filepath.split("/")[-1].split("\\")[-1],

            "sha256": result["sha256"],

            "bitcoin": result["bitcoin"],

            "ethereum": result["ethereum"],

            "urls": result["urls"],

            "ips": result["ips"],

            "emails": result["emails"],

            "risk": result["risk"]

        }

        return report


if __name__ == "__main__":

    sample = IOCExtractor("malware_samples/sample_malware.txt")

    print(sample.extract())