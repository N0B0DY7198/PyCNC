# -*- coding: UTF-8 -*-
#This is the help menu command, Also its a small example on how to make custom commands
helpbaner=open("assets/branding/help.cnc", "r", encoding='utf-8').read()
for help in helpbaner.split("\n"):
    send(client, help)