number=int(input()) #Ο χρήστης εκχωρεί τον αριθμό
def F(number):  #Δημιουργώ μία συνάρτηση F
    global athroisma 
    athroisma = 0   #Αρχικοποιώ το άθροισμα
    number = number * 3
    number = number + 1
    while number > 0 :  #Ελέγχω αν θα χρειαστεί να συνεχίσει η διαδικασία
        upoloipo = number % 10
        athroisma = athroisma + upoloipo
        number = int(number/10)
    print(athroisma)
F(number)   #Καλώ τηνσυνάρτηση F
while athroisma >= 10 :
    F(athroisma)