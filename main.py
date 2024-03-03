try:
    import requests, colorama, time, os, random, string
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
                                         | |   Version 1.1             
                                         |_|              
        Made By ISellStuff
        5.Exit
          
        1.Roblox
        2.Fortnite                                                   
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
            session = requests.Session()
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
        fn = input(cyan + "How Much Usernames Do You Want To Snipe? " )

        for i in range(int(fn)):
            letters: str = digits + ascii_lowercase 
            fnuser: str = "".join(random.choices(letters, k=5))

            findf = requests.get(f"https://fortnitetracker.com/profile/search?q={fnuser}")
            if findf.status_code == 404:
                print(Fore.GREEN + f"[+] {fnuser} is Available")
                fnu = open('usernames.txt','a')
                fnu.write(f"[+] Valid FN User {username}\n")
            else:
                print(Fore.RED + "[!] User Not Available")
            print()

        input("Press Enter To Close... ")

    if op == '9':
        letters: str = digits + ascii_lowercase 
        username: str = "".join(random.choices(letters, k=4))

        r = requests.post(f'https://www.snapchat.com/add/{username}')
        print(r.text)


main()
