s = open("speech.txt","r")  #Άνοιγμα αρχείου s
for line in s :
    print(line)
    for word in line.split():   #Χωρίζω τις λέξεις
        print(word)
        bad=0   #μετράει τα "κακά" γράμματα
        good=0  #μετράει τα "καλά" γράμματα
        for letter in word:
            if(letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u'
            or letter=='A' or letter=='E' or letter=='I' or letter=='O' or letter=='U'):
               pass
            else:
                if (letter=='f' or letter=='c' or letter=='r' or letter=='k' 
                or letter=='F' or letter=='C' or letter=='R' or letter=="K") :
                    bad = bad + 1
                else:
                    good = good + 1
        if bad > good : 
            print ("The word is bad.")
        else:
            print ("The word is good.")