s = open("speech.txt","r")  #Άνοιγμα αρχείου s
for line in s :
    print(line)
    for word in line.split():   #Χωρίζω τις λέξεις
        if len(word) > 3 : 
            word = word[1:] + word[0] #Το πρώτο γράμμα φεύγει και πάει στο τέλος της λέξης
            word = word + "ay"  #Προσθέτω την κατάληξη "ay" στο τέλος της λέξης
        print(word) 
