import requests
import json
from datetime import datetime
import pytz

# تحديد تاريخ اليوم بتوقيت مصر/مكة
tz = pytz.timezone('Africa/Cairo')
today = datetime.now(tz).strftime('%Y-%m-%d')

url = f"https://api-ar.ysscores.com/api/matches/matches_date_get/{today}/[]/[]/[]/180"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Referer": "https://ysscores.com/"
}

try:
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # حفظ البيانات في ملف json
    with open('matches.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print(f"Success! Data for {today} saved.")
except Exception as e:
    print(f"Error: {e}")
