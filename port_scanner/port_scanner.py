import os


def basic_scan():
    os.system("nmap " +target_ip)

def system():
    os.system("nmap -O " +target_ip)

def service():
    os.system("nmap -sS -sV " + target_ip)

def detail():
    os.system("nmap -sS -sV -sC " + target_ip)

def port():
    os.system("nmap -Pn -sS -n -v --reason --open "+ target_ip)

def scan_ip():
    x = target_ip.rfind(".")
    a = target_ip[x + 1]
    b = target_ip[x + 2]
    result = target_ip.replace(a + b, "0")
    os.system("nmap " +result+"/24")


os.system("figlet DarkScanner")
target_ip = input("Enter Target Ip :")
cont = True
while cont:
    print("""
    1-)Basic Scan
    2-)Operating System Information
    3-)Service and Version Information
    4-)Detail Scan
    5-)Show open ports
    6-)Scan Close IPs
    If you want to exit please enter e
    """)
    choose = str(input("Enter your selection : "))

    if (choose =="e"):
        os.system("clear")
        os.system("figlet Bye Bye")
        cont = False
    elif(choose == "1"):
        basic_scan()
    elif(choose == "2"):
        system()
    elif(choose == "3"):
        service()
    elif(choose == "4") :
        detail()
    elif(choose == "5"):
        port()
    elif(choose == "6"):
        scan_ip()
    else:
        print("Please enter correct number or letter ")


