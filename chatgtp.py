import openai

openai.api_key = "Aqui va tu key"
completion = openai.ChatCompletion()

#Función para hablar con la IA
def askgpt(question, chat_log=None):
    if chat_log is None:
        chat_log = [{
            'role': 'system',
            'content': 'You are a helpful, upbeat and funny assistant.',
        }]
    chat_log = [{'role': 'user', 'content': question}]
    response = completion.create(model='gpt-3.5-turbo', messages=chat_log)
    answer = response.choices[0]['message']['content']
    chat_log.append({'role': 'assistant', 'content': answer})
    return answer

# Ejecutar la IA de forma infinita
while True:
    print(askgpt(input("Pregunta: ")))