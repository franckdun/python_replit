def ReplitLoginSystem ():
  # Username and password
  while True:    
      username = input("What is your username?: ").lower()
      password = input("What is your password?: ")
      if username == "david" and password == "bald":
        print("Welcome to Replit!")
        break
      else:
        print("Whoops! I don't recognize that username or password. Try again!")
        continue

ReplitLoginSystem ()
