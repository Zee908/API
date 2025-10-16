import requests
def get_dollar_price():
    url = "https://apiv2.nobitex.ir/v3/orderbook/USDTIRT"  
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()  
        if data.get("status") == "ok":
            last_price = data["lastTradePrice"]  
            return last_price
        else:
            print("خطا ")
            return None
    else:
        print(f"خطا در درخواست HTTP: {response.status_code}")
        return None
price = get_dollar_price()
if price:
    print(f"قیمت دلار (USDT): {price} ریال")
else:
    print("قیمت دلار")


