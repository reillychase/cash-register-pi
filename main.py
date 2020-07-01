import stripe
import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
stripe.api_key = os.environ.get('cash_register_pi_stripe_api_key')
events = stripe.Event.list(limit=100)
last_event = config["Default"]["LastEvent"]

for event in events:
    print(event["id"])
    if event["id"] == last_event:
        break
    if event["type"] == "charge.succeeded":
        os.system("cvlc sounds/ka-ching.mp3 -q --play-and-exit")
    if event["type"] == "customer.subscription.created":
        os.system("cvlc sounds/squad-goin-up.mp3 -q --play-and-exit")

config["Default"]["LastEvent"] = events.data[0]["id"]
with open('config.ini', 'w') as configfile:
    config.write(configfile)
