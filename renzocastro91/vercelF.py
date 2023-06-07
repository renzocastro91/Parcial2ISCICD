import os
import requests

def handler(request, response):
    slack_webhook_url = os.environ.get("https://hooks.slack.com/services/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")
    if slack_webhook_url:
        send_slack_notification(slack_webhook_url)
    return "Success"

def send_slack_notification(webhook_url):
    payload = {
        "text": "El despliegue en Vercel se ha completado exitosamente."
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, json=payload, headers=headers)
    response.raise_for_status()

if __name__ == "__main__":
    handler(None, None)
