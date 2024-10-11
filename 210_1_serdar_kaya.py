#1)Define two variables:
#--The first variable should hold the year s/he was born (e.g., 2001)
#--The other variable should hold the current year (i.e., 2021)
bornYear = 2001
currentYear = 2021

#2)Define two variables:
#--The first variable should hold the month s/he was born (e.g., 9)
#--The other variable should hold the current month (i.e., 12)
#For this assignment, we assume that current month is greater than the month you was born.
bornMonth = 9
currentMonth = 12

#3)Define two variables:
#--The first variable should hold the day you s/he born (e.g., 4)
#--The other variable should hold the current day (i.e., 6)
#For this assignment, we assume that current day is greater than the day you was born.
bornDay = 4
currentDay = 6

#3)Compute the total number of days that s/he has been alive (in other words, the age in terms of days).
#Assign the computation result into a new variable.
#If you have problems with the computation logic, do not hesitate to ask your question in Slack.
daysAlive = (currentYear - bornYear) * 365 + (currentMonth - bornMonth) * 30 + currentDay - bornDay

#4)Print the total number of days as shown in the example below.
#The person has been living for 13684 days.
print(daysAlive)

#5)Compute the total number of hours that s/he has been alive (in other words, the age in terms of hours).
#You can use the total number of days to compute the hours easily.
#Assign the computation result into a new variable.
hoursAlive = daysAlive * 24

#6)Print the total number of hours as shown in the example below.
#The person has been living for 326496 hours.
print(hoursAlive)
