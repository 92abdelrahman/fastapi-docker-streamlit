from fastapi import FastAPI, Request
import requests

# Replace 'YOUR_BOT_API_TOKEN' with your Telegram Bot API token
bot_token = '6092786649:AAH3hbNKWEwZ3n7F9kYz1CQ2sVXJ7gFxpu0'

# Replace '801280384' with the chat ID of the recipient
chat_id = '801280384'

# URL for sending a message using the Telegram Bot API
url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

# Message content
message_text = 'Hello, this is a message from your bot!'

# Parameters for the POST request
params = {
    'chat_id': chat_id,
    'text': message_text,
}

app = FastAPI()

@app.post("/")
async def receive_updates(request: Request):
    data = await request.json()
    print("Received Update:")
    print(data)
    try:
        response = requests.post(url, data=params)
        data = response.json()
        if data['ok']:
            print(f'Message sent to {chat_id}: {message_text}')
        else:
            print(f'Failed to send the message. Telegram API response: {data}')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
    return {"status": "ok"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=7860)
