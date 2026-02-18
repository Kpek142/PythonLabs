login = input()
email = input()

if "@" not in login and "@" in email:
    print("КОРРЕКТНО")
else:
    print("НЕКОРРЕКТНО")