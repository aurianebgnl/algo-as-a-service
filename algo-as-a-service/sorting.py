def bubble_sort(arr, ascending=True):
    a = arr.copy() # on copie la liste pour ne pas modifier l'originale
    n = len(a)
    for i in range(n): # boucle externe - répéter les comparaisons
        for j in range(0, n-i-1): # boucle interne - comparaison élément par élément
            # condition de tri selon ascending == True or not
            if (ascending and a[j] > a[j+1]) or (not ascending and a[j] < a[j+1]):
                # échange de position dans la liste
                a[j], a[j+1] = a[j+1], a[j]
    return a

