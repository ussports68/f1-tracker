import requests
import json
import os

STATUS_FILE = "status.json"

def get_status():
    try:
        url = "https://api.openf1.org/v1/session_status"
        data = requests.get(url).json()
        return data[-1]['status']
    except:
        return None

def load_last_status():
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, "r") as f:
            return json.load(f).get("status")
    return None

def save_status(status):
    with open(STATUS_FILE, "w") as f:
        json.dump({"status": status}, f)

def send_alert(message):
    print("ALERT:", message)

def main():
    current_status = get_status()
    last_status = load_last_status()

    print("Current:", current_status)
    print("Previous:", last_status)

    if current_status and current_status != last_status:

        if current_status == "Started":
            send_alert("🚦 Race Started")

        elif current_status == "SafetyCar":
            send_alert("🚧 Safety Car")

        elif current_status == "RedFlag":
            send_alert("🛑 Red Flag")

        elif current_status == "Finished":
            send_alert("🏁 Race Finished")

        save_status(current_status)

if __name__ == "__main__":
    main()
