errors = ["Email is required", "Password is required", "Invalid phone format"]
print("Найдено ошибок:", len(errors))
if "Password is required" in errors:
    print("Критический баг: поле пароля обязательное!")
else:
    print("Проверка пароля пройдена")
errors.remove ("Password is required")
print (errors)
print (len(errors))
errors.clear()
if len(errors)==0:
    print("Все ошибки исправлены, форма готова к отправке!")
else:
    print("Остались неисправленные ошибки")