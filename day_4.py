def validate_password(password):
    if len(password)>=8:
        return "Valid"
    else:
        return "Invalid: Too short"
result=validate_password("super_secret_123")
print(result)

user_1 = {"username": "alex", "email": "alex@test.com", "is_active": True}
user_2 = {"username": "sam", "is_active": False}

def is_user_ready(user_dict):
    if "email" in user_dict and user_dict["is_active"]==True:
        return True
    else:
        return False

result=is_user_ready(user_1)
print(result)
result=is_user_ready(user_2)
print(result)

def get_passed_tests(test_results):
    passed=[]
    for result in test_results:
        if result=="PASSED":
            passed.append(result)
    return passed
status=["PASSED", "FAILED", "PASSED", "SKIPPED"]
print(get_passed_tests(status))

def get_critical_open_bugs(bugs_list):
    critical_bugs=[]
    for bug in bugs_list:
        if bug["severity"]=="CRITICAL" and bug["status"]=="OPEN":
            critical_bugs.append(bug)
    return critical_bugs
all_bugs = [
    {"id": 1, "severity": "CRITICAL", "status": "OPEN"},
    {"id": 2, "severity": "LOW", "status": "OPEN"},
    {"id": 3, "severity": "CRITICAL", "status": "CLOSED"},
    {"id": 4, "severity": "CRITICAL", "status": "OPEN"}
]

# Вызови функцию с этим списком и выведи результат в консоль через print()

print(get_critical_open_bugs(all_bugs))