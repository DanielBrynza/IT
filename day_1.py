status_code=[200,404,500,200,302]
failed_codes=[]
for code in status_code:
    if code ==200:
        print("Запрос успешный", code)
    else:
        print("Ошибка или перенаправление:", code)
        failed_codes.append(code)
print(failed_codes)