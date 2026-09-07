bugs = [
    {"id": 1, "severity": "CRITICAL", "status": "OPEN"},
    {"id": 2, "severity": "LOW", "status": "CLOSED"},
    {"id": 3, "severity": "HIGH", "status": "OPEN"}
]
open_bugs=[]
for bug in bugs:
    if bug["status"] == "OPEN":
        open_bugs.append(bug)
print(len(open_bugs))
print(open_bugs)    
