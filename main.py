import base64
import urllib.request

# لینک‌های منابع (می‌توانید لینک‌های دلخواه و سالم را اینجا قرار دهید)
SOURCES = [
    "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/mix",
    "https://raw.githubusercontent.com/MrPooyaikia/V2Ray-Collector/main/vless.txt"
]

def fetch_configs():
    all_configs = ""
    for url in SOURCES:
        try:
            print(f"Fetching from {url}...")
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=15) as response:
                content = response.read().decode('utf-8')
                if content.strip():
                    all_configs += content + "\n"
        except Exception as e:
            print(f"Error fetching {url}: {e}")
    return all_configs

if __name__ == "__main__":
    raw_data = fetch_configs()
    
    if not raw_data.strip():
        print("⚠️ هشدار: هیچ کانفیگی از لینک‌ها دریافت نشد!")
    
    # کدگذاری Base64 (استاندارد لازم برای فایل‌های سابسکریپشن)
    encoded_data = base64.b64encode(raw_data.encode('utf-8')).decode('utf-8')
    
    with open("sub.txt", "w", encoding="utf-8") as f:
        f.write(encoded_data)
        
    print("Done. Configs successfully written to sub.txt.")
