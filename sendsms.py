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
