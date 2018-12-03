print("Vacation accrual tracker")

initial_vacation_time = input("\nWhat are your current vacation hours?: ")
accrual_rate = input("What is your vacation accrual rate?: ")

date = input("\nWhat is the current date (XX/XX/XXXX)?: ")
str_date = str(date)
cur_mo = str_date[:2]
cur_day = str_date[3:5]
cur_yr = str_date[-4:]

vac_date = input("What is the date you need vacation by (XX/XX/XXXX)? ")
str_vac_date = str(vac_date)
vac_mo = str_vac_date[:2]
vac_day = str_vac_date[3:5]
vac_yr = str_vac_date[-4:]


if vac_yr > cur_yr:
    vac_mo = int(vac_mo) + 12
else:
    vac_mo = vac_mo
    
"This calculation is for a bi-monthly pay schedule"
if (0 < int(cur_day) < 16 and 0 < int(vac_day) < 16) or (15 < int(cur_day) < 32 and 15 < int(vac_day) < 32):
    paydays = (int(vac_mo) - int(cur_mo))*2
    
            
else:
    paydays = (int(vac_mo) - int(cur_mo))*2.5
    
    
vacation_time = float(initial_vacation_time) + (int(paydays)*float(accrual_rate))
print("\nYou will have" + " " + str(paydays) + " " + "paydays by this time")
print("You will have accrued" + " " + str(vacation_time) + " " + "hours of vacation time")
