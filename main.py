import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

def main():
    """Mini AI Chatbot - простой чат-бот с использованием Claude API"""
    
    client = anthropic.Anthropic()
    
    print("🤖 Mini AI Chatbot")
    print("=" * 50)
    print("Введи свой вопрос (для выхода напиши 'exit' или 'выход')")
    print("=" * 50)
    
    conversation_history = []
    
    while True:
        user_input = input("\nТы: ").strip()
        
        if user_input.lower() in ['exit', 'выход', 'quit']:
            print("\n👋 До свидания!")
            break
        
        if not user_input:
            continue
        
        conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        try:
            response = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                system="Ты полезный и дружелюбный ассистент. Отвечай коротко и по делу.",
                messages=conversation_history
            )
            
            assistant_message = response.content[0].text
            
            conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            print(f"\n🤖 AI: {assistant_message}")
            
        except Exception as e:
            print(f"❌ Ошибка: {str(e)}")
            conversation_history.pop()

if __name__ == "__main__":
    main()