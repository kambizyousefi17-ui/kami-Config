import urllib.request
import base64

# لیست کانال‌ها و منابع عمومی رایگان برای دریافت کانفیگ
SOURCES = [
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/Sub1.txt",
    "https://raw.githubusercontent.com/MrPooyaikia/V2Ray-Collector/main/combined-configs.txt"
]

def fetch_configs():
    all_configs = []
    for url in SOURCES:
        try:
            req = urllib.request.Request(
                url, 
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            with urllib.request.urlopen(req, timeout=10) as response:
                content = response.read().decode('utf-8')
                all_configs.append(content)
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            
    return "\n".join(all_configs)

if __name__ == "__main__":
    print("Fetching free configs...")
    raw_data = fetch_configs()
    
    if raw_data:
        # ذخیره در فایل خروجی برای استفاده نرم‌افزارها
        with open("sub.txt", "w", encoding="utf-8") as f:
            f.write(raw_data)
        print("Configs fetched and saved to sub.txt successfully!")
    else:
        print("No configs found.")
