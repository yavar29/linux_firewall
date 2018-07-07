import os
print(" \n WELCOME TO FIREWALL WIZARD \n")

while True:
	print(" ENTER YOUR CHOICE \n")
	choice=input(" CHOICE 1: BLOCK ALL TRAFIC \n CHOICE 2: UNBLOCK ALL TRAFFIC \n CHOICE 3: LIST FIREWALL RULES \n CHOICE 4: ADVANCED OPTION\n ")
	if choice=="1":
		os.system("sudo iptables -t filter -P FORWARD DROP")
		print("All traffic blocked\n")
	elif choice=="2":
		os.system("sudo iptables -t filter -F")
		os.system("sudo iptables -t filter -P FORWARD ACCEPT")
		print("All traffic unblocked\n")
	elif choice=="3":
		os.system("sudo iptables -t filter -L")
		print("\n")
	elif choice=="4":
		print("\n ENTER ADVANCE CHOICE \n ")
		choice2=input("\n CHOICE 1: BLOCK SPECIFIC IP ADDRESS\n CHOICE 2: UNBLOCK SPECIFIC IP ADDRESS \n CHOICE 3: BLOCK SSH TRAFFIC\n CHOICE 4: UNBLOCK SSH TRAFFIC \n")
		if choice2=="1":
			ip_add=input("\n Enter the ip address to be blocked\n")
			os.system("sudo iptables -t filter -A FORWARD -s {} -j DROP".format(ip_add))
			print("ip address {} blocked successfully\n".format(ip_add))
		elif choice2=="2":
			ip_add=input("\n Enter the ip address to be unblocked \n")
			os.system("sudo iptables -t filter -D FORWARD -s {} -j DROP".format(ip_add))
			print("ip address {} unblocked successfully\n".format(ip_add))
		elif choice2=="3":
			os.system("sudo iptables -A FORWARD -p tcp --destination-port 22 -j DROP")
			print("SSH traffic blocked successfully\n")
		elif choice2=="4":
			os.system=input("sudo iptables -D FORWARD -p tcp --destination-port 22 -j DRO")
			print("SSH traffic unblocked successfully\n")
		else:
			print("You have entered a wrong choice")
			
		

