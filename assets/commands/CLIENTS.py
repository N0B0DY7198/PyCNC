if len(args) == 3:
  send(client, "[MAIN] Checking admin credentials...")
  if admin(args[1], args[2])==True:
    send(client, "[MAIN] credentials verified!")
    with open('logins.txt') as f:
         line_count = 0
         for line in f:
             line_count += 1
    send(client, f"Current Clients: {line_count}")
  else:
    send(client, "[MAIN] credentials wrong")
else:
  send(client, "[MAIN] Missing admin credentials!")
