'''
import requests

def fetch_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
       user_data = data["data"]
       user_name = user_data["login"]["username"]
       country = user_data["location"]["country"]
       age = user_data["dob"]["age"]
       return user_name , country , age
    else:
        raise Exception("Data is not fetched!")

def main():
    try:
        user_name ,country , age = fetch_user()
        print(f"Username : {user_name} \n Country : {country} \n Age: {age}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
'''

 #Second API :   

import requests

def get_info_books():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    response  = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_name = data["data"]
        info = user_name["volumeInfo"]["title"]
        for_sale = user_name["saleInfo"]["saleability"]
        return info , for_sale

def main():
    try:
        info , for_sale = get_info_books()
        print(f"Information : {info} \n Saleability : {for_sale}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()