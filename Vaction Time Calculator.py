print("Vacation accrual tracker")

initial_vacation_time = 27.75
accrual_rate = 3.25


cur_mo = input("\nWhat is the current month (XX)?: ")
cur_day = input("What is the current day (XX)?: ")
cur_yr = input("What is the current year (XXXX)?: ")


print("\nWhat is the date you need vacation by? ")
vac_mo = input("Month (XX)?: ")
vac_day = input("Day (XX)?: ")
vac_yr = input("Year (XXXX)?: ")


if vac_yr > cur_yr:
    vac_mo = int(vac_mo) +12

else:
    vac_mo = vac_mo
    

if (0 < int(cur_day) < 16 and 0 < int(vac_day) < 16) or (15 < int(cur_day) < 32 and 15 < int(vac_day) < 32):
    paydays = (int(vac_mo) - int(cur_mo))*2
    
            
else:
    paydays = (int(vac_mo) - int(cur_mo))*2.5
    
    
vacation_time = initial_vacation_time + (int(paydays)*float(accrual_rate))
print("\nYou will have" + " " + str(paydays) + " " + "paydays by this time")
print("You will have accrued" + " " + str(vacation_time) + " " + "hours of vacation time")
