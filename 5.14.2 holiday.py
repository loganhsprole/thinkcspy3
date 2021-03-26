def trip_end(trip_begin, trip_len):
	return_day = trip_begin + (trip_len % 7)

	if return_day == 7:
		print("Sunday")
	elif return_day == 1:
		print("Monday")
	elif return_day == 2:
		print("Tuesday")
	elif return_day == 3:
		print("Wednesday")
	elif return_day == 4:
		print("Thursday")
	elif return_day == 5:
		print("Friday")
	elif return_day == 6:
		print("Saturday")
	else:
		return


leave_day = int(input("Enter day left number: "))
length_stay = int(input("Enter length of stay: "))

trip_end(leave_day, length_stay)
