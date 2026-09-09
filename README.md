# mini-ai
A mini AI project
print("🤖 Мини-ИИ запущен!")
print("Напиши 'выход', чтобы закончить.")

name = input("Как тебя зовут? ")
print(f"Приятно познакомиться, {name}! 😊")

while True:
    user = input("\nТы: ").lower()

    if user == "выход":
        print("ИИ: Пока! 👋")
        break

    elif "привет" in user or "здравствуй" in user:
        print("ИИ: Привет! Рад тебя видеть 😄")

    elif "как дела" in user:
        print("ИИ: У меня всё отлично! А у тебя?")

    elif "как тебя зовут" in user:
        print("ИИ: Я мини-ИИ 🤖")

    elif "кто ты" in user:
        print("ИИ: Я маленький искусственный интеллект!")

    elif "спасибо" in user:
        print("ИИ: Пожалуйста! 😊")

    else:
        print("ИИ: Я пока не знаю ответа на этот вопрос 🤔")