# %%
import requests
import json
import pandas as pd
from datetime import datetime

# Load App IDs
with open("appids.json") as f:
    appids = json.load(f)

for appid in appids:
    url = f"https://steamdb.info/api/Graphs/?appid={appid}"
    resp = requests.get(url)
    data = resp.json()
    
    # Extract player counts
    players = data['data']['players']
    
    # Convert to DataFrame
    df = pd.DataFrame(players, columns=['timestamp', 'ccu'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df['appid'] = appid
    
    # Save to CSV (append mode)
    csv_name = f"ccu_data_{appid}.csv"
    df.to_csv(csv_name, index=False)
    print(f"Saved {csv_name} with {len(df)} rows")
# %%
