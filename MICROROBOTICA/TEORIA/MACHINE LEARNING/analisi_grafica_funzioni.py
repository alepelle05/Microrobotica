def analisi_grafica(target,dati,features=None,dropna=True,alpha=1):
    '''
    funzione che analizza graficamente una fuinzione data in input
    
    parametri:
    traget: nome della colonna targhet della funzione
    dati: dataframe
    fratures: defaul value-> None, da passare se si vuole specificaere su quali colonne analizzare il dataframe, se si 
    lascia non verrà analizzato sulle colonne numeriche
    dropna: defaul value-> True
    alpha: defaul value->1 dare diverso valore per cambiare la trasparenza
    '''
    
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    
    
    
    colonne=np.array(dati.columns)
    colonne_num=[]
    
    if features==None:
        for colonna in colonne:

            if (str(type(dati[colonna][1]))[8:19] == 'numpy.float') or (str(type(dati[colonna][1]))[8:17] == 'numpy.int'):
                
                colonne_num.append(colonna)
        
    else:
        colonne_num=features
        
    colonne_num=np.array(colonne_num).flatten()
    dataframe=dati.copy()
    if dropna:
        dataframe=dataframe.dropna(axis="index",subset=colonne_num)

    col_specie={}
    for specie in dataframe[target]:
        col_specie[specie]=np.random.uniform(0,1,3)
    colori=[]
    for specie in dataframe[target]:
        colori.append(col_specie[specie])
    colori=np.array(colori)

    n=np.size(colonne_num)
    fig, axs=plt.subplots(ncols=n, nrows=n, figsize=(15,17))
    for riga in range(n):
        for colonna in range(n):
            if riga==colonna:
                for specie in col_specie.keys():
                    axs[riga, colonna].hist(dataframe[dataframe[target]==specie][colonne_num[riga]].values, color=col_specie[specie], label=specie,alpha=alpha)
                    axs[riga, colonna].set_xlabel(colonne_num[riga])
                    axs[riga, colonna].set_ylabel("Frequenza")
            else:
                for specie in col_specie.keys():
                    axs[riga, colonna].scatter(dataframe[dataframe[target]==specie][colonne_num[riga]].values, dataframe[dataframe[target]==specie][colonne_num[colonna]].values, color=col_specie[specie], s=10, label=specie)
                    axs[riga, colonna].set_xlabel(colonne_num[riga])
                    axs[riga, colonna].set_ylabel(colonne_num[colonna])
                    
    plt.legend(loc='upper left', bbox_to_anchor=(0, 1))
    
    plt.show()
