# Cash Register Pi
Raspberry Pi audio alerts for Stripe events

Currently it will play ka-ching.mp3 for each new charge.succeeded event, and squad-goin-up.mp3 for each new customer.subscription.created event.

# Installation instructions
This was tested on a Raspberry Pi 2 B, but should work on others.

1. Install "Raspberry Pi OS (32-bit) with desktop and recommended software" from https://www.raspberrypi.org/downloads/raspberry-pi-os/
2. Log in to the desktop, complete setup, run updates
3. Under Settings > Preferences > Raspberry Pi configuration > Interfaces I enabled SSH and VNC
4. I'm using an Etekcity Roverbeats T3 Bluetooth speaker, so I paired that under Bluetooth > Add device and right clicked on the volume control to change the audio output to that device.
5. Open a terminal and run the following commands, make sure to set your Stripe API key in the last command:
cd /home/pi
git clone https://github.com/reillychase/cash-register-pi.git
pip3 install stripe
export cash_register_pi_stripe_api_key=sk_live_yourkey
6. Set up a cronjob to check for new Stripe events every minute:
crontab -e
* * * * * /usr/bin/python3 /home/pi/cash-register-pi/main.py
CTRL+X then y to save
