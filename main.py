import urllib.request

SOURCES = [
    "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/mix",
    "https://raw.githubusercontent.com/MrPooyaikia/V2Ray-Collector/main/vless.txt"
]

def fetch_configs():
    all_configs = ""
    for url in SOURCES:
        try:
            print(f"Fetching from {url}")
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=15) as response:
                content = response.read().decode('utf-8')
                if content.strip():
                    all_configs += content + "\n"
        except Exception as e:
            print(f"Error: {e}")
    return all_configs

if __name__ == "__main__":
    raw_data = fetch_configs()
    with open("sub.txt", "w", encoding="utf-8") as f:
        f.write(raw_data)
    print("Done.")
