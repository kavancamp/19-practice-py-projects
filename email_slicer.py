#collect email from user 
#split the email by @  

def main():
  print("Welcome to the email slicer ")
  print("")
  email_input = input("Enter your email address: ")

  (username, domain) = email_input.split("@")
  (domain, extension) = domain.split(".")

  print("Username: ", username)
  print("Domain: ", domain)
  print("Extension: ", extension)

main()
