import requests
import json

# שנה את הפרמטרים האלו לנתונים שלך
ID_INSTANCE = "1101XXXXXX"
API_TOKEN = "your_token_here"
# עבור קבוצה ה-ID נראה כך: 120363XXXXXXXX@g.us
# עבור מספר פרטי זה נראה כך: 97250XXXXXXX@c.us
CHAT_ID = "120363XXXXXXXX@g.us" 

url = f"https://api.green-api.com/waInstance{ID_INSTANCE}/sendMessage/{API_TOKEN}"

payload = {
    "chatId": CHAT_ID,
    "message": "בוקר טוב! הודעה אוטומטית מגיטהאב."
}

headers = { 'Content-Type': 'application/json' }

response = requests.post(url, headers=headers, data=json.dumps(payload))
print("Response:", response.text)
