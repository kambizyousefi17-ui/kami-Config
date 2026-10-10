import urllib.request

SOURCES = [
    "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/base64/mix",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/Sub1.txt"
]

def fetch_configs():
    all_configs = ""
    for url in SOURCES:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=15) as response:
                content = response.read().decode('utf-8')
                all_configs += content + "\n"
        except Exception as e:
            print(f"Error fetching {url}: {e}")
    return all_configs

if __name__ == "__main__":
    print("Fetching configs...")
    raw_data = fetch_configs()
    
    with open("sub.txt", "w", encoding="utf-8") as f:
        f.write(raw_data)
    print("Configs saved to sub.txt successfully.")
