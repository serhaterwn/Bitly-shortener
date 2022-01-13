import requests
from colorama import Fore, init

init(autoreset=True)
print(Fore.BLUE+"""


██████╗░██╗████████╗██╗░░░░░██╗░░░██╗  ░██████╗██╗░░██╗░█████╗░██████╗░████████╗███████╗███╗░░██╗███████╗██████╗░
██╔══██╗██║╚══██╔══╝██║░░░░░╚██╗░██╔╝  ██╔════╝██║░░██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝████╗░██║██╔════╝██╔══██╗
██████╦╝██║░░░██║░░░██║░░░░░░╚████╔╝░  ╚█████╗░███████║██║░░██║██████╔╝░░░██║░░░█████╗░░██╔██╗██║█████╗░░██████╔╝
██╔══██╗██║░░░██║░░░██║░░░░░░░╚██╔╝░░  ░╚═══██╗██╔══██║██║░░██║██╔══██╗░░░██║░░░██╔══╝░░██║╚████║██╔══╝░░██╔══██╗
██████╦╝██║░░░██║░░░███████╗░░░██║░░░  ██████╔╝██║░░██║╚█████╔╝██║░░██║░░░██║░░░███████╗██║░╚███║███████╗██║░░██║
╚═════╝░╚═╝░░░╚═╝░░░╚══════╝░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝

""")

url = input("Shortened Link: ")
client = requests.session()
#GetWebsite
data = {
    "url": url,
}
headers = {
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": "_xsrf=bbdfff5c0c074dd493975b250c18efda; anon_u=cHN1X19jNjg2ZGY4Yy0xM2E1LTRiMTMtYWVhNi00Njc0YzBkYTJiZjE=|1642089112|13e9be3eb2ce07f4e68530fccd0c4f6816ccb362; 2fa=|1642089116|8ccd651e1c014932e36ee5f624f1e10262b41eca; session=ZGI2M2QzZGYtNjAzNS00NmQ5LWIyNzktMzQ2MjliN2EyMzNj|1642089116|15826da88e67693663c953a2d2c632952496c1af; user=|1642089116|508867fd5ceee36446a95f63b2045830c2d0534c",
    "origin": "https://bitly.com",
    "referer": "https://bitly.com/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    "x-xsrftoken": "bbdfff5c0c074dd493975b250c18efda"
}
try:
    login = client.post('https://bitly.com/data/anon_shorten',data=data,headers=headers)
    all = login.json()["data"]
    link = all["link"]
    init(autoreset=True)
    print(Fore.RED+"Abbreviation Link: {}".format(link)+ " |Shortened URL: {} ".format(url))
    file = open('bit_ly.txt','a')
    file.write("Abbreviation Link: {}".format(link)+ " |shortened URL: {} ".format(url)+'\n')
except:
    print('An unexpected error has occurred. Try again.')

input('Process completed. Press enter to exit.\n')