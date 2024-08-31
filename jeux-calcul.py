import random

nb1 = 6
nb2 = 10

nbi1 = 60
nbi2 = 100

nbd1 = 100
nbd2 = 500

qs = "5"
qs2 = "10"

core = 0
core2 = 0


print()
print()
print()
nom = input("Quel est votre nom ? : ")

choix = "0"
while not choix == "1000":
    print()
    print("JEUX CALCUL")
    print()
    print(f"Bienvenue {nom} !")
    print()
    print("Choissisez une operation : ")
    print()
    print("1 - ADITTION")
    print("2 - DIVISION")
    print("3 - MULTIPLICATION")
    print("4 - SOUSTRATION")
    print("5 - ALEATOIRE")


    choix = input("Votre choix est : ")

    if choix > "4":
                print("OUPS: vous devez choisir une option")
    try:
        choix4 = int(choix)
        #c = random.randint(choix)
        #choix == "{c}"
    except:
        print()
        print("OUPS: vous devez choisir une option")

  

    # ADDITTION
        
    if choix == "1":

        choix2 = "0"
        while not choix2 == "100":
            print()
            print("NIVEAU :")
            print()
            print("1 - facile")
            print("2 - intermediaire")
            print("3 - difficile")
            print("4 - Quitter")
            print()
            choix2 = input("Choisissez : ")
            try:
                choix4 = int(choix2)
            except:
                print()
                print("OUPS: vous devez choisir un NIVEAU")

            if choix2 >= "5":
                print("OUPS: vous devez choisir un niveau ou quitter")

            # FACILE
                
            if choix2 == "1":

                chx1 = "0"
                while not chx1 == "100" :

                    print()
                    print("Vous preferez :")
                    print()
                    print("1 - 5 QUESTIONS")
                    print("2 - 10 QUESTIONS")
                    print()
                    chx1 = input("Choisissez : ")
                    try:
                        chx10 = int(chx1)
                    except:
                        print()
                        print("OUPS: vous devez choisir une option")

                    if chx1 >= "3":
                        print("OUPS: vous devez choisir une option")


                    #5QS
                        
                    if chx1 == "1":

                        for i in range(0, 5):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs}")
                            print()
                            a = random.randint(nb1, nb2)
                            b = random.randint(nb1, nb2)

                            question = input(f"Calculez : {a} + {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a + b
                                if question_int == calcul:
                                    core = int(core) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core == 5:
                            print()
                            print(f"Bravo, votre score est de {str(core)}/5")
                        if core == 4:
                            print()
                            print(f"Excellent, votre score est de {str(core)}/5")

                        if core == 3:
                            print()
                            print(f"Pas mal, votre score est de {str(core)}/5")
                        if core < 3:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core)}/5")

                        break



                    #QS10
                            
                    if chx1 == "2":

                        for i in range(0, 10):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs2}")
                            print()
                            a = random.randint(nb1, nb2)
                            b = random.randint(nb1, nb2)

                            question = input(f"Calculez : {a} + {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a + b
                                if question_int == calcul:
                                    core2 = int(core2) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core2 == 10:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 9:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 6 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 7 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 8 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 5:
                            print()
                            print(f"Pas mal, votre score est de {str(core2)}/10")
                        if core2 < 5:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core2)}/10")

                        break

               
               
                     
            # INTERMEDIAIRE
                            
            if choix2 == "2":
                

                 chx1 = "0"
                 while not chx1 == "100" :

                    print()
                    print("Vous preferez :")
                    print()
                    print("1 - 5 QUESTIONS")
                    print("2 - 10 QUESTIONS")
                    print()
                    chx1 = input("Choisissez : ")
                    try:
                        chx10 = int(chx1)
                    except:
                        print()
                        print("OUPS: vous devez choisir une option")

                    if chx1 >= "3":
                        print("OUPS: vous devez choisir une option")


                    #5QS
                        
                    if chx1 == "1":

                        for i in range(0, 5):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs}")
                            print()
                            a = random.randint(nbi1, nbi2)
                            b = random.randint(nbi1, nbi2)

                            question = input(f"Calculez : {a} + {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a + b
                                if question_int == calcul:
                                    core = int(core) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core == 5:
                            print()
                            print(f"Bravo, votre score est de {str(core)}/5")
                        if core == 4:
                            print()
                            print(f"Excellent, votre score est de {str(core)}/5")

                        if core == 3:
                            print()
                            print(f"Pas mal, votre score est de {str(core)}/5")
                        if core < 3:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core)}/5")
                        
                        break



                    #QS10
                            
                    if chx1 == "2":

                        for i in range(0, 10):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs2}")
                            print()
                            a = random.randint(nbi1, nbi2)
                            b = random.randint(nbi1, nbi2)

                            question = input(f"Calculez : {a} + {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a + b
                                if question_int == calcul:
                                    core2 = int(core2) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core2 == 10:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 9:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 6 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 7 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 8 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 5:
                            print()
                            print(f"Pas mal, votre score est de {str(core2)}/10")
                        if core2 < 5:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core2)}/10")
                        
                        break

            # DIFFICILE

            if choix2 == "3":

                chx1 = "0"
                while not chx1 == "100" :

                    print()
                    print("Vous preferez :")
                    print()
                    print("1 - 5 QUESTIONS")
                    print("2 - 10 QUESTIONS")
                    print()
                    chx1 = input("Choisissez : ")
                    try:
                        chx10 = int(chx1)
                    except:
                        print()
                        print("OUPS: vous devez choisir une option")

                    if chx1 >= "3":
                        print("OUPS: vous devez choisir une option")


                    #5QS
                        
                    if chx1 == "1":

                        for i in range(0, 5):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs}")
                            print()
                            a = random.randint(nbd1, nbd2)
                            b = random.randint(nbd1, nbd2)

                            question = input(f"Calculez : {a} + {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a + b
                                if question_int == calcul:
                                    core = int(core) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core == 5:
                            print()
                            print(f"Bravo, votre score est de {str(core)}/5")
                        if core == 4:
                            print()
                            print(f"Excellent, votre score est de {str(core)}/5")

                        if core == 3:
                            print()
                            print(f"Pas mal, votre score est de {str(core)}/5")
                        if core < 3:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core)}/5")
                        
                        break


                    #QS10
                            
                    if chx1 == "2":

                        for i in range(0, 10):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs2}")
                            print()
                            a = random.randint(nbd1, nbd2)
                            b = random.randint(nbd1, nbd2)

                            question = input(f"Calculez : {a} + {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a + b
                                if question_int == calcul:
                                    core2 = int(core2) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core2 == 10:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 9:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 6 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 7 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 8 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 5:
                            print()
                            print(f"Pas mal, votre score est de {str(core2)}/10")
                        if core2 < 5:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core2)}/10")
                        
                        break


            #QUITTER
            if choix2 == "4":

               break





    # DIVISION
                            
    if choix == "2":
        choix2 = "0"
        while not choix2 == "4":
            print()
            print("NIVEAU :")
            print()
            print("1 - facile")
            print("2 - intermediaire")
            print("3 - difficile")
            print("4 - Quitter")
            print()
            choix2 = input("Choisissez : ")
            try:
                choix4 = int(choix2)
            except:
                print()
                print("OUPS: vous devez choisir un NIVEAU")

            if choix2 >= "5":
                print("OUPS: vous devez choisir un niveau ou quitter")

            # FACILE
                
            if choix2 == "1":

                chx1 = "0"
                while not chx1 == "100" :

                    print()
                    print("Vous preferez :")
                    print()
                    print("1 - 5 QUESTIONS")
                    print("2 - 10 QUESTIONS")
                    print()
                    chx1 = input("Choisissez : ")
                    try:
                        chx10 = int(chx1)
                    except:
                        print()
                        print("OUPS: vous devez choisir une option")

                    if chx1 >= "3":
                        print("OUPS: vous devez choisir une option")
                    


                    #5QS
                        
                    if chx1 == "1":

                        for i in range(0, 5):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs}")
                            print()
                            a = random.randint(nb1, nb2)
                            b = random.randint(nb1, nb2)

                            question = input(f"Calculez : {a} / {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a / b
                                if question_int == calcul:
                                    core = int(core) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core == 5:
                            print()
                            print(f"Bravo, votre score est de {str(core)}/5")
                        if core == 4:
                            print()
                            print(f"Excellent, votre score est de {str(core)}/5")

                        if core == 3:
                            print()
                            print(f"Pas mal, votre score est de {str(core)}/5")
                        if core < 3:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core)}/5")
                        
                        break



                    #QS10
                            
                    if chx1 == "2":

                        for i in range(0, 10):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs2}")
                            print()
                            a = random.randint(nb1, nb2)
                            b = random.randint(nb1, nb2)

                            question = input(f"Calculez : {a} / {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a / b
                                if question_int == calcul:
                                    core2 = int(core2) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core2 == 10:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 9:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 6 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 7 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 8 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 5:
                            print()
                            print(f"Pas mal, votre score est de {str(core2)}/10")
                        if core2 < 5:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core2)}/10")
                        
                        break

            # INTERMEDIAIRE
                            
            if choix2 == "2":

                chx1 = "0"
                while not chx1 == "100" :

                    print()
                    print("Vous preferez :")
                    print()
                    print("1 - 5 QUESTIONS")
                    print("2 - 10 QUESTIONS")
                    print()
                    chx1 = input("Choisissez : ")
                    try:
                        chx10 = int(chx1)
                    except:
                        print()
                        print("OUPS: vous devez choisir une option")

                    if chx1 >= "3":
                        print("OUPS: vous devez choisir une option")


                    #5QS
                        
                    if chx1 == "1":

                        for i in range(0, 5):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs}")
                            print()
                            a = random.randint(nbi1, nbi2)
                            b = random.randint(nbi1, nbi2)

                            question = input(f"Calculez : {a} / {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a / b
                                if question_int == calcul:
                                    core = int(core) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core == 5:
                            print()
                            print(f"Bravo, votre score est de {str(core)}/5")
                        if core == 4:
                            print()
                            print(f"Excellent, votre score est de {str(core)}/5")

                        if core == 3:
                            print()
                            print(f"Pas mal, votre score est de {str(core)}/5")
                        if core < 3:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core)}/5")
                        
                        break


                    #QS10
                            
                    if chx1 == "2":

                        for i in range(0, 10):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs2}")
                            print()
                            a = random.randint(nbi1, nbi2)
                            b = random.randint(nbi1, nbi2)

                            question = input(f"Calculez : {a} / {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a / b
                                if question_int == calcul:
                                    core2 = int(core2) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core2 == 10:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 9:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 6 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 7 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 8 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 5:
                            print()
                            print(f"Pas mal, votre score est de {str(core2)}/10")
                        if core2 < 5:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core2)}/10")
                        
                        break

            # DIFFICILE

            if choix2 == "3":

                chx1 = "0"
                while not chx1 == "100" :

                    print()
                    print("Vous preferez :")
                    print()
                    print("1 - 5 QUESTIONS")
                    print("2 - 10 QUESTIONS")
                    print()
                    chx1 = input("Choisissez : ")
                    try:
                        chx10 = int(chx1)
                    except:
                        print()
                        print("OUPS: vous devez choisir une option")

                    if chx1 >= "3":
                        print("OUPS: vous devez choisir une option")


                    #5QS
                        
                    if chx1 == "1":

                        for i in range(0, 5):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs}")
                            print()
                            a = random.randint(nbd1, nbd2)
                            b = random.randint(nbd1, nbd2)

                            question = input(f"Calculez : {a} / {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a / b
                                if question_int == calcul:
                                    core = int(core) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core == 5:
                            print()
                            print(f"Bravo, votre score est de {str(core)}/5")
                        if core == 4:
                            print()
                            print(f"Excellent, votre score est de {str(core)}/5")

                        if core == 3:
                            print()
                            print(f"Pas mal, votre score est de {str(core)}/5")
                        if core < 3:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core)}/5")

                        break

                    #QS10
                            
                    if chx1 == "2":

                        for i in range(0, 10):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs2}")
                            print()
                            a = random.randint(nbd1, nbd2)
                            b = random.randint(nbd1, nbd2)

                            question = input(f"Calculez : {a} / {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a / b
                                if question_int == calcul:
                                    core2 = int(core2) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core2 == 10:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 9:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 6 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 7 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 8 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 5:
                            print()
                            print(f"Pas mal, votre score est de {str(core2)}/10")
                        if core2 < 5:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core2)}/10")
                        
                        break

            #QUITTER
            if choix2 == "4":

               break

    # MULTIPLICATION

    if choix == "3":

        choix2 = "0"
        while not choix2 == "4":
            print()
            print("NIVEAU :")
            print()
            print("1 - facile")
            print("2 - intermediaire")
            print("3 - difficile")
            print("4 - Quitter")
            print()
            choix2 = input("Choisissez : ")
            try:
                choix4 = int(choix2)
            except:
                print()
                print("OUPS: vous devez choisir un NIVEAU")

            if choix2 >= "5":
                print("OUPS: vous devez choisir un niveau ou quitter")

            # FACILE
            if choix2 == "1":

                chx1 = "0"
                while not chx1 == "100" :

                    print()
                    print("Vous preferez :")
                    print()
                    print("1 - 5 QUESTIONS")
                    print("2 - 10 QUESTIONS")
                    print()
                    chx1 = input("Choisissez : ")
                    try:
                        chx10 = int(chx1)
                    except:
                        print()
                        print("OUPS: vous devez choisir une option")

                    if chx1 >= "3":
                        print("OUPS: vous devez choisir une option")


                    #5QS
                        
                    if chx1 == "1":

                        for i in range(0, 5):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs}")
                            print()
                            a = random.randint(nb1, nb2)
                            b = random.randint(nb1, nb2)

                            question = input(f"Calculez : {a} x {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a * b
                                if question_int == calcul:
                                    core = int(core) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core == 5:
                            print()
                            print(f"Bravo, votre score est de {str(core)}/5")
                        if core == 4:
                            print()
                            print(f"Excellent, votre score est de {str(core)}/5")

                        if core == 3:
                            print()
                            print(f"Pas mal, votre score est de {str(core)}/5")
                        if core < 3:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core)}/5")
                        
                        break



                    #QS10
                            
                    if chx1 == "2":

                        for i in range(0, 10):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs2}")
                            print()
                            a = random.randint(nb1, nb2)
                            b = random.randint(nb1, nb2)

                            question = input(f"Calculez : {a} x {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a * b
                                if question_int == calcul:
                                    core2 = int(core2) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core2 == 10:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 9:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 6 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 7 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 8 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 5:
                            print()
                            print(f"Pas mal, votre score est de {str(core2)}/10")
                        if core2 < 5:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core2)}/10")
                        
                        break


            # INTERMEDIAIRE
                            
            if choix2 == "2":

                chx1 = "0"
                while not chx1 == "100" :

                    print()
                    print("Vous preferez :")
                    print()
                    print("1 - 5 QUESTIONS")
                    print("2 - 10 QUESTIONS")
                    print()
                    chx1 = input("Choisissez : ")
                    try:
                        chx10 = int(chx1)
                    except:
                        print()
                        print("OUPS: vous devez choisir une option")

                    if chx1 >= "3":
                        print("OUPS: vous devez choisir une option")


                    #5QS
                        
                    if chx1 == "1":

                        for i in range(0, 5):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs}")
                            print()
                            a = random.randint(nbi1, nbi2)
                            b = random.randint(nbi1, nbi2)

                            question = input(f"Calculez : {a} x {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a * b
                                if question_int == calcul:
                                    core = int(core) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core == 5:
                            print()
                            print(f"Bravo, votre score est de {str(core)}/5")
                        if core == 4:
                            print()
                            print(f"Excellent, votre score est de {str(core)}/5")

                        if core == 3:
                            print()
                            print(f"Pas mal, votre score est de {str(core)}/5")
                        if core < 3:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core)}/5")
                        
                        break



                    #QS10
                            
                    if chx1 == "2":

                        for i in range(0, 10):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs2}")
                            print()
                            a = random.randint(nbi1, nbi2)
                            b = random.randint(nbi1, nbi2)

                            question = input(f"Calculez : {a} x {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a * b
                                if question_int == calcul:
                                    core2 = int(core2) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core2 == 10:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 9:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 6 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 7 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 8 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 5:
                            print()
                            print(f"Pas mal, votre score est de {str(core2)}/10")
                        if core2 < 5:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core2)}/10")
                        
                        break


            # DIFFICILE

            if choix2 == "3":

                chx1 = "0"
                while not chx1 == "100" :

                    print()
                    print("Vous preferez :")
                    print()
                    print("1 - 5 QUESTIONS")
                    print("2 - 10 QUESTIONS")
                    print()
                    chx1 = input("Choisissez : ")
                    try:
                        chx10 = int(chx1)
                    except:
                        print()
                        print("OUPS: vous devez choisir une option")

                    if chx1 >= "3":
                        print("OUPS: vous devez choisir une option")


                    #5QS
                        
                    if chx1 == "1":

                        for i in range(0, 5):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs}")
                            print()
                            a = random.randint(nbd1, nbd2)
                            b = random.randint(nbd1, nbd2)

                            question = input(f"Calculez : {a} x {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a * b
                                if question_int == calcul:
                                    core = int(core) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core == 5:
                            print()
                            print(f"Bravo, votre score est de {str(core)}/5")
                        if core == 4:
                            print()
                            print(f"Excellent, votre score est de {str(core)}/5")

                        if core == 3:
                            print()
                            print(f"Pas mal, votre score est de {str(core)}/5")
                        if core < 3:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core)}/5")

                        break


                    #QS10
                            
                    if chx1 == "2":

                        for i in range(0, 10):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs2}")
                            print()
                            a = random.randint(nbd1, nbd2)
                            b = random.randint(nbd1, nbd2)

                            question = input(f"Calculez : {a} x {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a * b
                                if question_int == calcul:
                                    core2 = int(core2) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core2 == 10:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 9:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 6 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 7 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 8 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 5:
                            print()
                            print(f"Pas mal, votre score est de {str(core2)}/10")
                        if core2 < 5:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core2)}/10")
                        
                        break

            #QUITTER
            if choix2 == "4":

               break

    # SOUSTRATION

    if choix == "4":

        choix2 = "0"
        while not choix2 == "4":
            print()
            print("NIVEAU :")
            print()
            print("1 - facile")
            print("2 - intermediaire")
            print("3 - difficile")
            print("4 - Quitter")
            print()
            choix2 = input("Choisissez : ")
            try:
                choix4 = int(choix2)
            except:
                print()
                print("OUPS: vous devez choisir un NIVEAU")

            if choix2 >= "5":
                print("OUPS: vous devez choisir un niveau ou quitter")


            # FACILE
                
            if choix2 == "1":

                chx1 = "0"
                while not chx1 == "100" :

                    print()
                    print("Vous preferez :")
                    print()
                    print("1 - 5 QUESTIONS")
                    print("2 - 10 QUESTIONS")
                    print()
                    chx1 = input("Choisissez : ")
                    try:
                        chx10 = int(chx1)
                    except:
                        print()
                        print("OUPS: vous devez choisir une option")

                    if chx1 >= "3":
                        print("OUPS: vous devez choisir une option")


                    #5QS
                        
                    if chx1 == "1":

                        for i in range(0, 5):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs}")
                            print()
                            a = random.randint(nb1, nb2)
                            b = random.randint(nb1, nb2)

                            question = input(f"Calculez : {a} - {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a - b
                                if question_int == calcul:
                                    core = int(core) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core == 5:
                            print()
                            print(f"Bravo, votre score est de {str(core)}/5")
                        if core == 4:
                            print()
                            print(f"Excellent, votre score est de {str(core)}/5")

                        if core == 3:
                            print()
                            print(f"Pas mal, votre score est de {str(core)}/5")
                        if core < 3:
                            print() 

                            print(f"Révisez vos maths, votre score est de {str(core)}/5")
                        
                        break



                    #QS10
                            
                    if chx1 == "2":

                        for i in range(0, 10):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs2}")
                            print()
                            a = random.randint(nb1, nb2)
                            b = random.randint(nb1, nb2)

                            question = input(f"Calculez : {a} - {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a - b
                                if question_int == calcul:
                                    core2 = int(core2) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core2 == 10:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 9:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 6 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 7 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 8 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 5:
                            print()
                            print(f"Pas mal, votre score est de {str(core2)}/10")
                        if core2 < 5:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core2)}/10")
                        
                        break


            # INTERMEDIAIRE
                            
            if choix2 == "2":

                chx1 = "0"
                while not chx1 == "100" :

                    print()
                    print("Vous preferez :")
                    print()
                    print("1 - 5 QUESTIONS")
                    print("2 - 10 QUESTIONS")
                    print()
                    chx1 = input("Choisissez : ")
                    try:
                        chx10 = int(chx1)
                    except:
                        print()
                        print("OUPS: vous devez choisir une option")

                    if chx1 >= "3":
                        print("OUPS: vous devez choisir une option")


                    #5QS
                        
                    if chx1 == "1":

                        for i in range(0, 5):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs}")
                            print()
                            a = random.randint(nbi1, nbi2)
                            b = random.randint(nbi1, nbi2)

                            question = input(f"Calculez : {a} - {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a - b
                                if question_int == calcul:
                                    core = int(core) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core == 5:
                            print()
                            print(f"Bravo, votre score est de {str(core)}/5")
                        if core == 4:
                            print()
                            print(f"Excellent, votre score est de {str(core)}/5")

                        if core == 3:
                            print()
                            print(f"Pas mal, votre score est de {str(core)}/5")
                        if core < 3:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core)}/5")
                        
                        break



                    #QS10
                            
                    if chx1 == "2":

                        for i in range(0, 10):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs2}")
                            print()
                            a = random.randint(nbi1, nbi2)
                            b = random.randint(nbi1, nbi2)

                            question = input(f"Calculez : {a} - {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a - b
                                if question_int == calcul:
                                    core2 = int(core2) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core2 == 10:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 9:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 6 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 7 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 8 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 5:
                            print()
                            print(f"Pas mal, votre score est de {str(core2)}/10")
                        if core2 < 5:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core2)}/10")
                        
                        break

            # DIFFICILE

            if choix2 == "3":

                chx1 = "0"
                while not chx1 == "100" :

                    print()
                    print("Vous preferez :")
                    print()
                    print("1 - 5 QUESTIONS")
                    print("2 - 10 QUESTIONS")
                    print()
                    chx1 = input("Choisissez : ")
                    try:
                        chx10 = int(chx1)
                    except:
                        print()
                        print("OUPS: vous devez choisir une option")

                    if chx1 >= "3":
                        print("OUPS: vous devez choisir une option")


                    #5QS
                        
                    if chx1 == "1":

                        for i in range(0, 5):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs}")
                            print()
                            a = random.randint(nbd1, nbd2)
                            b = random.randint(nbd1, nbd2)

                            question = input(f"Calculez : {a} - {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a - b
                                if question_int == calcul:
                                    core = int(core) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core == 5:
                            print()
                            print(f"Bravo, votre score est de {str(core)}/5")
                        if core == 4:
                            print()
                            print(f"Excellent, votre score est de {str(core)}/5")

                        if core == 3:
                            print()
                            print(f"Pas mal, votre score est de {str(core)}/5")
                        if core < 3:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core)}/5")
                        
                        break



                    #QS10
                            
                    if chx1 == "2":

                        for i in range(0, 10):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs2}")
                            print()
                            a = random.randint(nbd1, nbd2)
                            b = random.randint(nbd1, nbd2)

                            question = input(f"Calculez : {a} - {b} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                            else:
                                calcul = a - b
                                if question_int == calcul:
                                    core2 = int(core2) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calcul:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calcul)}")

                        if core2 == 10:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 9:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 6 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 7 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 8 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 5:
                            print()
                            print(f"Pas mal, votre score est de {str(core2)}/10")
                        if core2 < 5:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core2)}/10")
                        
                        break

            #QUITTER
            if choix2 == "4":

               break
    

    #ALEATOIRE
            
                            
    if choix == "5":
         
         choix2 = "0"
         while not choix2 == "100":
            print()
            print("NIVEAU :")
            print()
            print("1 - facile")
            print("2 - intermediaire")
            print("3 - difficile")
            print("4 - Quitter")
            print()
            choix2 = input("Choisissez : ")
            try:
                choix4 = int(choix2)
            except:
                print()
                print("OUPS: vous devez choisir un NIVEAU")

            if choix2 >= "5":
                print("OUPS: vous devez choisir un niveau ou quitter")


            # FACILE
                
            if choix2 == "1":

                chx1 = "0"
                while not chx1 == "100" :

                    print()
                    print("Vous preferez :")
                    print()
                    print("1 - 5 QUESTIONS")
                    print("2 - 10 QUESTIONS")
                    print()
                    chx1 = input("Choisissez : ")
                    try:
                        chx10 = int(chx1)
                    except:
                        print()
                        print("OUPS: vous devez choisir une option")

                    if chx1 >= "3":
                        print("OUPS: vous devez choisir une option")


                    #5QS
                        
                    if chx1 == "1":
                       
                        for i in range(0, 5):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs}")
                            print()
                            a = random.randint(nb1, nb2)
                            b = random.randint(nb1, nb2)


                            calcul = [a + b , a - b, a * b, a / b]
                            calculs = random.choice(calcul)

                            if calculs == a + b :
                                 question = input(f"Calculez : {a} + {b} = ")
                            
                            if calculs == a - b :
                                 question = input(f"Calculez : {a} - {b} = ")
                            
                            if calculs == a / b :
                                 question = input(f"Calculez : {a} / {b} = ")

                            if calculs == a * b :
                                 question = input(f"Calculez : {a} x {b} = ")
                            

                            #qsa = [f"{a} + {b} , {a} - {a}, {a} * {b}, {a} / {b}"]
                            #qar = random.choice(qsa)
                            #question = input(f"Calculez : {str(qar)} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                                print(f"La réponse était  {str(calculs)}")
                            else:
                                
                                if question_int == calculs:
                                    core = int(core) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calculs:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calculs)}")

                        if core == 5:
                            print()
                            print(f"Bravo, votre score est de {str(core)}/5")
                        if core == 4:
                            print()
                            print(f"Excellent, votre score est de {str(core)}/5")

                        if core == 3:
                            print()
                            print(f"Pas mal, votre score est de {str(core)}/5")
                        if core < 3:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core)}/5")

                        break


                    #QS10
                            
                    if chx1 == "2":

                        for i in range(0, 10):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs2}")
                            print()
                            a = random.randint(nb1, nb2)
                            b = random.randint(nb1, nb2)


                            calcul = [a + b , a - b, a * b, a / b]
                            calculs = random.choice(calcul)

                            if calculs == a + b :
                                 question = input(f"Calculez : {a} + {b} = ")
                            
                            if calculs == a - b :
                                 question = input(f"Calculez : {a} - {b} = ")
                            
                            if calculs == a / b :
                                 question = input(f"Calculez : {a} / {b} = ")

                            if calculs == a * b :
                                 question = input(f"Calculez : {a} x {b} = ")

                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                                print(f"La réponse était  {str(calculs)}")
                            else:
                                if question_int == calculs:
                                    core2 = int(core2) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calculs:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calculs)}")

                        if core2 == 10:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 9:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 6 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 7 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 8 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 5:
                            print()
                            print(f"Pas mal, votre score est de {str(core2)}/10")
                        if core2 < 5:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core2)}/10")
                        
                        break

            
            # INTERMEDIAIRE
                
            if choix2 == "2":

                chx1 = "0"
                while not chx1 == "100" :

                    print()
                    print("Vous preferez :")
                    print()
                    print("1 - 5 QUESTIONS")
                    print("2 - 10 QUESTIONS")
                    print()
                    chx1 = input("Choisissez : ")
                    try:
                        chx10 = int(chx1)
                    except:
                        print()
                        print("OUPS: vous devez choisir une option")

                    if chx1 >= "3":
                        print("OUPS: vous devez choisir une option")


                    #5QS
                        
                    if chx1 == "1":
                       
                        for i in range(0, 5):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs}")
                            print()
                            a = random.randint(nbi1, nbi2)
                            b = random.randint(nbi1, nbi2)


                            calcul = [a + b , a - b, a * b, a / b]
                            calculs = random.choice(calcul)

                            if calculs == a + b :
                                 question = input(f"Calculez : {a} + {b} = ")
                            
                            if calculs == a - b :
                                 question = input(f"Calculez : {a} - {b} = ")
                            
                            if calculs == a / b :
                                 question = input(f"Calculez : {a} / {b} = ")

                            if calculs == a * b :
                                 question = input(f"Calculez : {a} x {b} = ")
                            

                            #qsa = [f"{a} + {b} , {a} - {a}, {a} * {b}, {a} / {b}"]
                            #qar = random.choice(qsa)
                            #question = input(f"Calculez : {str(qar)} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                                print(f"La réponse était  {str(calculs)}")
                            else:
                                
                                if question_int == calculs:
                                    core = int(core) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calculs:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calculs)}")

                        if core == 5:
                            print()
                            print(f"Bravo, votre score est de {str(core)}/5")
                        if core == 4:
                            print()
                            print(f"Excellent, votre score est de {str(core)}/5")

                        if core == 3:
                            print()
                            print(f"Pas mal, votre score est de {str(core)}/5")
                        if core < 3:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core)}/5")

                        break


                    #QS10
                            
                    if chx1 == "2":

                        for i in range(0, 10):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs2}")
                            print()
                            a = random.randint(nbi1, nbi2)
                            b = random.randint(nbi1, nbi2)


                            calcul = [a + b , a - b, a * b, a / b]
                            calculs = random.choice(calcul)

                            if calculs == a + b :
                                 question = input(f"Calculez : {a} + {b} = ")
                            
                            if calculs == a - b :
                                 question = input(f"Calculez : {a} - {b} = ")
                            
                            if calculs == a / b :
                                 question = input(f"Calculez : {a} / {b} = ")

                            if calculs == a * b :
                                 question = input(f"Calculez : {a} x {b} = ")

                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                                print(f"La réponse était  {str(calculs)}")
                            else:
                                if question_int == calculs:
                                    core2 = int(core2) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calculs:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calculs)}")

                        if core2 == 10:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 9:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 6 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 7 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 8 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 5:
                            print()
                            print(f"Pas mal, votre score est de {str(core2)}/10")
                        if core2 < 5:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core2)}/10")
                        
                        break
            

            # DIFFICILE
                
            if choix2 == "3":

                chx1 = "0"
                while not chx1 == "100" :

                    print()
                    print("Vous preferez :")
                    print()
                    print("1 - 5 QUESTIONS")
                    print("2 - 10 QUESTIONS")
                    print()
                    chx1 = input("Choisissez : ")
                    try:
                        chx10 = int(chx1)
                    except:
                        print()
                        print("OUPS: vous devez choisir une option")

                    if chx1 >= "3":
                        print("OUPS: vous devez choisir une option")


                    #5QS
                        
                    if chx1 == "1":
                       
                        for i in range(0, 5):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs}")
                            print()
                            a = random.randint(nbd1, nbd2)
                            b = random.randint(nbd1, nbd2)


                            calcul = [a + b , a - b, a * b, a / b]
                            calculs = random.choice(calcul)

                            if calculs == a + b :
                                 question = input(f"Calculez : {a} + {b} = ")
                            
                            if calculs == a - b :
                                 question = input(f"Calculez : {a} - {b} = ")
                            
                            if calculs == a / b :
                                 question = input(f"Calculez : {a} / {b} = ")

                            if calculs == a * b :
                                 question = input(f"Calculez : {a} x {b} = ")
                            

                            #qsa = [f"{a} + {b} , {a} - {a}, {a} * {b}, {a} / {b}"]
                            #qar = random.choice(qsa)
                            #question = input(f"Calculez : {str(qar)} = ")
                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                                print(f"La réponse était  {str(calculs)}")
                            else:
                                
                                if question_int == calculs:
                                    core = int(core) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calculs:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calculs)}")

                        if core == 5:
                            print()
                            print(f"Bravo, votre score est de {str(core)}/5")
                        if core == 4:
                            print()
                            print(f"Excellent, votre score est de {str(core)}/5")

                        if core == 3:
                            print()
                            print(f"Pas mal, votre score est de {str(core)}/5")
                        if core < 3:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core)}/5")

                        break


                    #QS10
                            
                    if chx1 == "2":

                        for i in range(0, 10):
                            print()
                            print("C'EST PARTI !")
                            print(f"Question {i + 1}/{qs2}")
                            print()
                            a = random.randint(nbd1, nbd2)
                            b = random.randint(nbd1, nbd2)


                            calcul = [a + b , a - b, a * b, a / b]
                            calculs = random.choice(calcul)

                            if calculs == a + b :
                                 question = input(f"Calculez : {a} + {b} = ")
                            
                            if calculs == a - b :
                                 question = input(f"Calculez : {a} - {b} = ")
                            
                            if calculs == a / b :
                                 question = input(f"Calculez : {a} / {b} = ")

                            if calculs == a * b :
                                 question = input(f"Calculez : {a} x {b} = ")

                            try:
                                question_int = int(question)
                            except:
                                print("ERREUR: vous devez rentrer un nombre")
                                print(f"La réponse était  {str(calculs)}")
                            else:
                                if question_int == calculs:
                                    core2 = int(core2) + 1
                                    print()
                                    print("Vous avez reussi !")
                                #print(f"La réponse est  {str(calcul)}")

                                if not question_int == calculs:
                                    print()
                                    print("Vous avez échoué")
                                    print(f"La réponse était  {str(calculs)}")

                        if core2 == 10:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 9:
                            print()
                            print(f"Bravo, votre score est de {str(core2)}/10")
                        if core2 == 6 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 7 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 8 :
                            print()
                            print(f"Excellent, votre score est de {str(core2)}/10")
                        if core2 == 5:
                            print()
                            print(f"Pas mal, votre score est de {str(core2)}/10")
                        if core2 < 5:
                            print()
                            print(f"Révisez vos maths, votre score est de {str(core2)}/10")
                        
                        break

            
            #QUITTER
            if choix2 == "4":

               break