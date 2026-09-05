import time 
RESET = "\033[0m"
RED   = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PINK = "\033[35m"
CYAN = "\033[36m"
RED_BACK = "\033[41m"
GREEN_BACK = "\033[42m"
YELLOW_BACK = "\033[43m"
BLUE_BACK = "\033[44m"
PINK_BACK = "\033[45m"
CYAN_BACK = "\033[46m"
player_wallet = "5000"

print (f"{YELLOW}Welcome to the HORSE RPG{RESET}")

time.sleep (0.7)

print("Shopkeeper: Hello, sir! What horse would you like to buy?")

time.sleep (0.7)

print("Horses:")
time.sleep (0.2)
print("Joey")
time.sleep (0.2) 
print("Hammer")
time.sleep (0.2) 
print("Oldey")
while True:
	look = input("Who are you interested in?")
	if look == "joey":
			print(f"{RED}Joey:  Strength: [••••-----]{RESET}")
			time.sleep(0.2)
			print(f"{BLUE}Speed: [••-------]{RESET}")
			time.sleep(0.2)
			print(f"{PINK}Health: [•••------]{RESET}")
			time.sleep(0.2)
			print (f"{GREEN}Price: [2000]{RESET}")
			print(f"{GREEN_BACK}Your wallet after buying {look}:{RESET}")
			pfh = input(int(5000 - 2000))
	elif look == "hammer":
		print(f"Hammer: {RED}Strength : [•••••••--]{RESET}")
		time.sleep(0.2)
		print(f"{BLUE}Speed: [••••-----]{RESET}")
		time.sleep(0.2)
		print(f"{PINK}Health [•••••••••]{RESET}")
		print(f"{GREEN_BACK}Your wallet after buying {look}{RESET}:")
		print(f"{GREEN}Price [5000]{RESET}")
		pfh = input(int(5000 - 5000))
	elif look == "oldey":
		print(f"Oldey: {RED}Strength [••-------]{RESET}")
		time.sleep(0.2)
		print(f"{BLUE}Speed: [---------]{RESET}")
		time.sleep(0.2)
		print(f"{PINK}Health: [••-------]")
		print(f"{GREEN}Price: [500]{RESET}")
		print(f"{GREEN_BACK}Your wallet after buying {look}{RESET}:")
		pfh = input(int(5000 - 500))
	elif look == "nigga":
		print("GET OUT MY STORE! RIGHT. NOW.")
		break
	else:
		print("Never heard of that horse")
		break
	time.sleep(2.0)
	buyrequest = input(f"Would you like to buy {look} ?")
	if buyrequest == "yes":
		print("Shopkeeper: Hope this horse will serve you well!")
		break
	elif buyrequest == "no":
		print("Shopkeeper: Well did you want another horse?")
else:
	print("Shopkeeper: I expect a yes or no answer")
	if buyrequest == "yes":
		print(f"Let's go home, {look}")
	
		