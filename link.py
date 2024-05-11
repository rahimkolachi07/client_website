import requests

def get_access_token(client_id, client_secret):
    url = "https://www.linkedin.com/oauth/v2/accessToken"
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    response = requests.post(url, data=data)
    access_token = response.json()["access_token"]
    return access_token

def post_on_linkedin_page(access_token, page_id, message):
    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json"
    }
    data = {
        "author": f"urn:li:organization:{page_id}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": message
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Post successful!")
    else:
        print("Post failed:", response.text)

# Example usage
client_id = "77krtzupfybgcy"
client_secret = "iIrIblPq4PPf4gAQ"
page_id = "90700161"
message = "Hello LinkedIn Page! This is a test post from Python."

access_token = "AQXL_FO-A1VpmDFAfmuj_mD_JoZwHGpPJWm3hJtV4BL3Y7bnYU39pPLX-6zpGPTjvO49xWsYSYvCBy_iPhCkvanJNnHQqxDqPbx-AQcT63VXOqBz2uwYBR8KtBV1_ZMxaNy2MOyl7nfP6buixmvgftc_a-VE1vHupEHG3VpquKdpffI2bWam2qR8YLI0DmZOrvhzNiwHkXfONzTUc14F2EGUyWbBZfaH-jbxPIetR7whXR2osFQjiiEWBYaRkew3jPNFfneBwOkcPwRgSHV1rxZn3X8npiQ6yMNTS8uAiisf4DLb_FQi198wG2ULha-NjFumAeeeFUcfy6oVCL9DNpjNGf42eg"
post_on_linkedin_page(access_token, page_id, message)
