#Write a program using match-case that takes a number (1–7) and prints the day of the week.

day=int(input("\nEnter The Day Count ?\n \n"))

match day:
	case 1 : print("\nMonday")
	case 2 : print("\nTuesday")
	case 3 : print("\nWednesday")
	case 4 : print("\n Thursday")
	case 5 :print("\nFriday")
	case 6 :print("\nSaturday")
	case 7 : print("\nSunday")
	case _ :  print("\n You Enter A undefind day")