import requests

def send_request(url, headers, method, payload=None, params=None):
    loop_count = 0
    while True:
        try:
            if payload is not None:
                response = requests.request(method, url, headers=headers, json=payload)
                if response.status_code == 200:
                    result = response.json()
                    return result
                else:
                    if loop_count >= 10:
                        print(response)
                        print(f"RequestError.ErrorCode{response.status_code}")
                        return 
            else:
                response = requests.get(url, headers=headers, params=params)
                if response.status_code == 200:
                    result = response.text
                    return result
                else:
                    if loop_count >= 10:
                        print(response)
                        print(f"RequestError.ErrorCode{response.status_code}")
                        return 
            
            
        except Exception as e:
            if loop_count >= 10:
                print(e)
                return
        loop_count += 1
