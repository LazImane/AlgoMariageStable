#exemple manuel juste pour tester

etudiants_ex = {
    "E0": {
        "preferences": ["P1", "P0", "P2"]
    },
    "E1": {
        "preferences": ["P0", "P1", "P2"]
    },
    "E2": {
        "preferences": ["P0", "P1", "P2"]
    }
}

etablissements_ex = {
    "P0": {
        "capacite": 1,
        "preferences": ["E0", "E2", "E1"]
    },
    "P1": {
        "capacite": 1,
        "preferences": ["E1", "E0", "E2"]
    },
    "P2": {
        "capacite": 1,
        "preferences": ["E1", "E0", "E2"]
    }
}

def mariage_stable(etudiants, etablissement):
    priorite = 0 #nb de priorite
    liste_rejetee= list(etudiants.keys())
    acceptes_temp = {p: [] for p in etablissement} 
    """
    acceptes temp gives back something of this form:
    acceptes_temp = {
    "P0": [],
    "P1": [],
    "P2": []
}
    """

    while liste_rejetee:# = not empty? 
        for i in (liste_rejetee):
            print(i)
            liste_pref= etudiants[i]["preferences"] #liste des preferences de l'etudiant i
            etabl = etablissement[liste_pref[priorite]] #find the matching etablissement in etablissements
            #etabl_accept = acceptes_temp[liste_pref[priorite]] #THIS!!! NEEDS TO BE CHANGED
            print(liste_pref)
            print(etabl)
            #print(etabl_accept)
            print("len(acceptes_temp[liste_pref[priorite]])" , len(acceptes_temp[liste_pref[priorite]]) , "VS", "etabl[capacite]" , etabl["capacite"])
        
            if len(acceptes_temp[liste_pref[priorite]]) < etabl["capacite"]:
                print("passed!")
                liste_rejetee.remove(i)
                acceptes_temp[liste_pref[priorite]].append(i)
                print("on vient d'ajouter (cas etablissement vide)", i, " à ", liste_pref[priorite])
                print("accepted for now: ", acceptes_temp)
                

            else:
                
                for j in (acceptes_temp[liste_pref[priorite]]):
                                    if plus_prefere(i, j,etabl["preferences"]): #sinon il reste dans les rejetes? 
                                        liste_rejetee.append(j)
                                        liste_rejetee.remove(i)
                                        acceptes_temp[liste_pref[priorite]].remove(j)
                                        acceptes_temp[liste_pref[priorite]].append(i)
                                        print("on vient d'ajouter (cas etablissement plein)", i)
                                        print("accepted students for ", j , " are: " ,acceptes_temp[liste_pref[priorite]])
                                        print("REJETEE",liste_rejetee)
                                    else:
                                        priorite+=1 #idk wether i should make this a list for each individual candidate or not im trying this first 
                                        print("priorite:", priorite)
    return acceptes_temp

def plus_prefere(i1,i2,liste_priorite):
    for i in range (len(liste_priorite)):
        if liste_priorite[i] == i1 :
            print(i1 , "plus prefere à ", i2)
            return True #i1>i2
        else:
            if liste_priorite[i] == i2: #i2>i1
                print(i2 , "plus prefere à ", i1)
                return False
    return True

print("resultats: ",mariage_stable(etudiants_ex,etablissements_ex))


            

        


