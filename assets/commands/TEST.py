#plan lookup command
if len(args) == 2:
    pln=getdata(args[1], "plan")
    send(client, f"Grabbed plan: {pln}")
elif len(args) != 2:
    send(client, f"Usage: {args[0]} [username]")
