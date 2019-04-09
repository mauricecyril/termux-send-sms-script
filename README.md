# Termux Send SMS Script
A quick script to send an SMS message to a list of recipients using Termux-API and Python3  on an Android device.

# No Longer WORKS with Latest Android PIE Updates.

# Installation Instructions
1. Install the Termux app from the Google Play Store: [https://play.google.com/store/apps/details?id=com.termux](https://play.google.com/store/apps/details?id=com.termux)

1. Once installed, run Termux

1. Update Apt
```ash
apt-get update
```

1. Install Termux-API
```bash
apt-get install termux-api
```

1. Test the SMS send command in Termux and allow Android to access the SMS functions on the phone
```bash
termux-sms-send -n [replace with phone number] [SMS message]
```

1. Install Python
```bash
apt-get install python
```

1. Install Nano text editor
```bash
apt-get install nano
```

1. Create the python Script
```bash
nano sendsms.py
```

1. Write the script
```python
import subprocess

# Add Entries to the address book dictionary. Key = Name, Value = Phone Number
addressbook = {"Name1" : "+15551234567"
                "Name2" : "+15551234568"
                }
                
# Loop through the addressbook dictionary and send each number the message
for (k,v) in addressbook.items():
    
    # SMS Message Template (try to keep to within 150 characters)
    smsmessage = str("Hi " + k + " your phone number is " + v)
    
    # Use Subprocess Run Function to send SMS
    subprocess.run(["termux-sms-send", "-n", phonenumber, smsmessage])
    
    # Print confirmation of each send
    print("Sent Message to " + k + " via " + v)


# Print end of process message
print("Message sending complete")
```

1. Save the python script and exit nano by pressing CTRL+X in Nano

1. Run the script in Termux
```bash
python sendsms.py
```

The termux terminal will display the following
```bash
Sent Message to Name1 via +15551234567
Sent Message to Name2 via +15551234568
Message sending complete
```
