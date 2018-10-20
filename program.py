import time
import subprocess
import validate_email

subprocess.call("clear")

print("Checking if SENDEMAIL application is installed...\n")
subprocess.call(["apt", "list", "--installed", "|", "grep", "sendemail"])
print("\nIf the sendemail application is not showing above please exit this application and install it.")

time.sleep(5)

subprocess.call("clear")

print("GODFEAR EMAIL APPLICATION\n")

fromAddress = input("Enter the From Address: ")
toAddress = input("Enter the To Address: ")
subject = input("Enter the Subject: ")
message = input("Enter the Message: ")

file = open("credentials", "r")
userPass = file.readlines(1)
print(userPass)

username = ""
for x in userPass:
    if x == "['":
        pass
    elif x == "']":
        pass
    elif x == " ":
        break
    else:
        username = username + x

print(username)

creds = username.split(" ")

subprocess.call("clear")

print("PREVIEW: ")
print("FROM: {}".format(fromAddress))
print("TO: {}".format(toAddress))
print("SUBJECT: {}".format(subject))
print("MESSAGE: ")
print(message)
input("\nHit Enter to Send...")

subprocess.call("clear")

print("Checking if email address is valid...")

isValid = validate_email.validate_email(toAddress)

print(isValid)

subprocess.call(["sendemail", "-t", toAddress, "-f", fromAddress, "-u", subject, "-m", message, "-s", "mail.smtp2go.com:2525", "-xu", creds[0], "-xp", creds[1]])
