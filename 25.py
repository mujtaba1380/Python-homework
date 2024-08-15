class Report:
    def __init__(self, file_path):
        self.file_path = file_path
    def generate_report(self):
        try:
            with open (self.file_path, "r") as file:
                data = file.read()
                report = f"Report generated from file {self.file_path}:\n\n{data}"
                return report
        except FileNotFoundError:
            return f"Error: File {self.file_path} not found"
        except IOError as e:
            return f"Error reading file {self.file_path: {e}}"
report_gen = Report("C:\\Users\\Mujtaba\\Desktop\\programming homework\\Mujtaba.txt")
report = report_gen.generate_report()
print(report)