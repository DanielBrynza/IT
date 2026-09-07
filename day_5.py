import json

test_report = {
    "total_tests": 10,
    "passed": 8,
    "failed": 2,
    "status": "COMPLETED"
}

# Запись в файл в Python:
with open("report.json", "w") as file:
    json.dump(test_report, file, indent=4)