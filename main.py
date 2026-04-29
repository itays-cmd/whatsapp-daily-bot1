import requests
import json

# שנה את הפרמטרים האלו לנתונים שלך
ID_INSTANCE = "7107604629"
API_TOKEN = "8fd010ad67b1446187956bcb2ef4b5b9bb6d963371bf447f8a"
# עבור קבוצה ה-ID נראה כך: 120363XXXXXXXX@g.us
# עבור מספר פרטי זה נראה כך: 97250XXXXXXX@c.us
CHAT_ID = "CkwyRjF2nt6GzMPBzCN6ZJ@g.us" 

url = f"https://api.green-api.com/waInstance{ID_INSTANCE}/sendMessage/{API_TOKEN}"

payload = {
    "chatId": CHAT_ID,
    "message": "בוקר טוב! הודעה אוטומטית מגיטהאב."
}

headers = { 'Content-Type': 'application/json' }

response = requests.post(url, headers=headers, data=json.dumps(payload))
print("Response:", response.text)
