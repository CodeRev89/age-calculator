breakout = None

while breakout is None:
    user_option = input("Do you want to leave:\n ")
    if user_option == 'yes':
        breakout = True
    else:
        print('invalid')