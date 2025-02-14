def friendly_reminder(func):
 
    '''Reminder for husband'''
 
    func()
    print('Don\'t forget to bring your wallet!')
 
def action():
 
    print('I am going to the store buy you something nice.')
 
# Calling the friendly_reminder function with the action function used as an argument.
 
friendly_reminder(action)