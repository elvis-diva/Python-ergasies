from datetime import datetime
print("Give the date you want as follows 'day/month/year'")
day = int(input())  #Ο χρήστης εκχωρεί τις τιμές της ημερομηνίας που επιθυμεί
month = int(input())
years = int(input())
now = datetime.now()    #Εκχωρώ της σηερινή ημερομηνία του υπολογιστή    
date = datetime(years,month,day)
dif = now - date
print ("They differ",dif.days,"days." )
print ("They differ",dif.total_seconds()/3600,"hours.") 
print ("They differ",dif.total_seconds(),"seconds.")  
from calendar import monthrange
monthdays = monthrange (years,month)    #Βρίσκω πόσες μέρες έχει ο μήνας που μου έδωσε ο χρήστης
print("This month contains", monthdays[1],"days")
