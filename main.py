import urllib.request

SOURCES = [
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/Sub1.txt",
    "https://raw.githubusercontent.com/MrPooyaikia/V2Ray-Collector/main/combined-configs.txt"
]

def fetch_configs():
    all_configs = ""
    for url in SOURCES:
        try:
            print(f"Trying to fetch from: {url}")
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=20) as response:
                content = response.read().decode('utf-8')
                if content.strip():
                    print(f"Successfully fetched {len(content)} characters.")
                    all_configs += content + "\n"
                else:
                    print(f"Content from {url} was empty.")
        except Exception as e:
            print(f"Error fetching {url}: {e}")
    return all_configs

if __name__ == "__main__":
    print("Starting config collection...")
    raw_data = fetch_configs()
    
    print(f"Total collected data length: {len(raw_data)}")
    
    with open("sub.txt", "w", encoding="utf-8") as f:
        f.write(raw_data)
    print("sub.txt file updated.")
