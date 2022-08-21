from datetime import date


def get_dob():
	year =int("what year were you born?")
	month = int ("what month were you born?")
	day = int ("what day were you born?")
	return date (year, month, day)
    
	

def get_current_date(dob):
 diff= date.today()-dob
 return diff.days//365 
 



def main():
	dob=get_dob()
	if dob <=date.today():
     age=get_age(dob)
     print (f"You are {age} years old.")
 else:
     print("invalid birthdate. try again")
     

	


if __name__ == '__main__':
    main()
