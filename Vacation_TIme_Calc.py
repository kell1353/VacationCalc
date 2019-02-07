import datetime
import sys

print("Vacation accrual tracker")
initial_vacation_time = input("\nWhat are your current vacation hours?: ")
accrual_rate = input("What is your accrual rate?: ")

cur_date = datetime.date.today().strftime('%m/%d/%Y')
#cur_date = input("What is the current date  (XX/XX/XXXX)?: ")
str_date = str(cur_date)
cur_mo = str_date[:2]
cur_day = str_date[3:5]
cur_yr = str_date[-4:]

vac_date = input("What is the date you need vacation by (XX/XX/XXXX)?: ")
str_vac_date = str(vac_date)
vac_mo = str_vac_date[:2]
vac_day = str_vac_date[3:5]
vac_yr = str_vac_date[-4:]


#Error checking for the input of the vacation date.
if len(str_vac_date) != 10:
    print("This is not a valid date, date needs to be in this format (XX/XX/XXXX). Please retry program.")
    sys.exit()
if (int(vac_mo) < int(cur_mo) and vac_yr == cur_yr) or \
    int(vac_yr) < int(cur_yr) or (int(vac_mo) == int(cur_mo) and int(vac_day) < int(cur_day) and vac_yr == cur_yr):
    print("This is not a valid date, date must be after " + str_date + ". Please retry program.")
    sys.exit()
if int(vac_mo) > 12 or int(vac_day) > 31:  
    print("This is not a valid day or month. Please retry program.")
    sys.exit()


if vac_yr > cur_yr:
    yr_differential = int(vac_yr) - int(cur_yr)
    vac_mo = int(vac_mo) + 12*(yr_differential)
else:
    vac_mo = vac_mo

    
"This calculation is for a bi-monthly pay schedule"
if (0 < int(cur_day) < 15 and 0 < int(vac_day) < 15) or (15 <= int(cur_day) < 32 and 15 <= int(vac_day) < 32):
    paydays = (int(vac_mo) - int(cur_mo))*2
    
if (0 < int(cur_day) < 15 and 15 <= int(vac_day) < 32):
    paydays = ((int(vac_mo) - int(cur_mo))*2) + 1
    
if (15 <= int(cur_day) < 32 and 0 < int(vac_day) < 15):
    paydays = ((int(vac_mo) - int(cur_mo))*2) - 1


    
vacation_amount_cap = 120    
    
vacation_time = float(initial_vacation_time) + (int(paydays)*float(accrual_rate))

if vacation_time > vacation_amount_cap:
    print("\nYou will have" + " " + str(paydays) + " " + "paydays by this time.")
    print("You will have maxed out vacation time at a total of " + str(vacation_amount_cap) + " hours of vacation time on this date.")
else:
    print("\nYou will have" + " " + str(paydays) + " " + "paydays by this time.")
    print("You will have a total of " + str(vacation_time) + " hours of vacation time on this date.")
