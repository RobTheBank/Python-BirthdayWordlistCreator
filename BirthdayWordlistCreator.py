
import sys

start_year = raw_input("Start year: ")
end_year = raw_input("End year: ")

try:
	if not 1 <= int(start_year) <= int(end_year):
		sys.exit(0)

except :
	print "Have something wrong!"
	print "You Can try that."
	print "Start year:1990"
	print "End year:2020"
	sys.exit(0)

with open('birthday.txt','w') as f:
	for year in range(int(start_year), int(end_year) + 1):
		for month in range(1,13):
			end_day = 31
			if month in(1,3,5,7,8,10,12):
				end_day = 32

			elif month == 2:
				end_day = 29

				if abs(year-2020) % 4 == 0:
					end_day = 30

			for day in range(1,end_day):
				print >>f, str(year).zfill(4) + str(month).zfill(2) + str(day).zfill(2)

print "Finish! Check your birthday.txt."
