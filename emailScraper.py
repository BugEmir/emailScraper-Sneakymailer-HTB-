#!/usr/bin/python3

# collect alle e-mail addressen van bestand team.php in CTF challenge
# Email collecter van website [Sneakymailer hackthebox]
# Gemaakt voor SneakyMailer [Emirhan Sarikaya]

# We gebruiken python3 omdat bs4 makkelijker is..

from bs4 import BeautifulSoup
import requests
import sys
import time

targetIP = sys.argv[1] # http://dev.sneakycorp.htb/team.php

print("""\033[36m
\n\n [!] Je bent een script kiddy! \n
[!] Moet ik het weer voor je uitvogelen jaa..
\033[0m
""")
time.sleep(2)

with requests.Session() as req:
    request = req.get(targetIP)
    outputHTML = request.text

    soup = BeautifulSoup(outputHTML, 'html.parser')
    data = soup.find_all('table', id='dataTable')
    for d in data:
        for number in range(3,231,4):
            emails = d.find_all('td')[number]
            for email in emails:
                time.sleep(1)
                print(email)
print("\n\n\033[34m [!] YES! emails gevonden, danku voor het gebruik -emir \033[0m \n\n")
