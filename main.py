import os
try:
    import requests, colorama, time, random, string
    from string import ascii_lowercase, digits
    from colorama import Fore, Back, Style
except ModuleNotFoundError:
    print("[!] Some Modules Not Found")
    print("[+] Installing....")
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install time")
    os.system("pip install random")
    os.system("pip install string")
    import requests, colorama, time, os
    from colorama import Fore, Back, Style
    print()
    print(Fore.GREEN + "[+] Modules Installed")
    time.sleep(1.5)

cyan = Fore.CYAN

def main():

    print(cyan + """
      _    _                  _____       _                 
     | |  | |                / ____|     (_)                
     | |  | |___  ___ _ __  | (___  _ __  _ _ __   ___ _ __ 
     | |  | / __|/ _ \ '__|  \___ \| '_ \| | '_ \ / _ \ '__|
     | |__| \__ \  __/ |     ____) | | | | | |_) |  __/ |   
      \____/|___/\___|_|    |_____/|_| |_|_| .__/ \___|_|   
                                         | |   Version 1.3             
                                         |_|              
        Made By ISellStuff
        9.Exit
          
        1.Roblox
        2.Fortnite (Patched)
        3.Recroom                                                  
                                            """)
    
    op = input(cyan + "[>] ")
    if op == '5':
        print(Fore.RED + "Closing....")
        time.sleep(1.5)
    else:
        print()
    
    if op == '1':
        roblox = input(cyan + "How Much Username Do You Want To Snipe? ")

        for i in range(int(roblox)):
            letters: str = digits + ascii_lowercase 
            username: str = "".join(random.choices(letters, k=5))
            find = requests.get(f"https://auth.roblox.com/v1/usernames/validate?birthday=1992-12-31T23:00:00.000Z&context=Signup&username={username}")
            
            if "Username is already in use" in find.text:
                print(Fore.RED + "[!] Username Not Available")
            elif "[!] Username Not Avaiable" in find.text:
                print(Fore.RED + "[!] Username Not Available")
            elif "Username is valid" in find.text:
                rblx = open('usernames.txt','a')
                rblx.write(f"[+] Valid Roblox User: {username}\n")
                print(Fore.GREEN + f"[+] Valid {username}")
            else:
                print(Fore.RED + "[!] Error")
            print()
        input("Press Enter To Close... ")

    if op == '2':
        print(Fore.YELLOW + "[!] Fortnite Username Patched Fixing Soon")
        time.sleep(1.5)
        quit()


    if op == '3':
        rec = input(Fore.CYAN + "\n[+] Ammount Of Usernames To Find: ")

        for i in range(int(rec)):
            letters: str = digits + ascii_lowercase 
            username2: str = "".join(random.choices(letters, k=4))

            r = requests.post(f"https://apim.rec.net/accounts/account?username={username2}", data={f'username={username2}'})
            if r.status_code == 404:
                recr = open('usernames.txt','a')
                recr.write(f"[+] Valid Recroom User: {username2}\n")
                print(Fore.GREEN + f"\n[+] Valid {username2}")
                print()
            else:
                print(Fore.RED + "[!] Invalid User\n")
        input("Press Enter To Close... ")
        


main()
