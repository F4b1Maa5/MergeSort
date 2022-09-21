def mergeSort(array):
    #Überprüfen ob das Array mehr als ein Element hat wichtig für spätere Rekursion
    if len(array) > 1:

        #Die Mitte des Array ermitteln
        mittelpunkt = len(array) // 2

        #Übergebenes Array in eine Linke und Rechte Hälfte teilen
        linkesArray = array[:mittelpunkt]
        rechtesArray = array[mittelpunkt:]

        #Rekursive merge Sort aufrufen mit der jeweiligen Teilhäfte. Bis das übergebene Array nur 2 oder 3 Elemente enthält und so im Rechten und Linken Array jeweils nur 1 Element exestiert
        mergeSort(linkesArray)
        mergeSort(rechtesArray)

        #Initialisierung temporärer Variablen
        o = 0
        p = 0

        # Es wird geprüft ob welcher Wert aus dem Linken oder Rechten Array nun der kleinere ist. Dieser wird nun an die
        # erste Stelle des Arrays geschriebn nun wird die Variable für das jeweilige Subarray inkrementiert.
        # Nun geht es weiter für die Nächte Stelle des Array und nun wird die 0te des einen Subarrays und die 1ste Stelle des anderen Subarrays überprüft
        #
        # Likes 3, 4 Rechtes 1, 5
        # Array [0] = Likes[0] (3) < Rechte[0] (1)
        # Array [0] = 1
        # Array [1] = Likes [0] (3) < Rechte[1] (5)
        # Array [1] = 3
        #...
        for i in range(len(array)):
            if o < len(linkesArray) and p < len(rechtesArray):
                if linkesArray[o] < rechtesArray[p]:
                    array[i] = linkesArray[o]
                    o = o+1
                else:
                    array[i] = rechtesArray[p]
                    p = p+1
            elif o < len(linkesArray):
                array[i] = linkesArray[o]
                o = o + 1
            else:
                array[i] = rechtesArray[p]
                p = p + 1


#Array eingeben und die Methode mergeSort aufrufen und dort das Array übergeben
def __main__():
    array = [9, 5, 40, 2, 10, 15, 8, 99, 1]
    print("Das eingegeben Array sieht wie folgt aus:")
    print(array)
    mergeSort(array)
    print()
    print("Das sortierte Array sieht wie folgt aus:")
    print(array)

__main__()