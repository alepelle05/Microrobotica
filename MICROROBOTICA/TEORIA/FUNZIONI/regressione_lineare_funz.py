def regressione(dataframe,target):
    
    '''
    funzione che analizza graficamente la regressione lineare di una funzione
    
    parametri:
    traget: nome della colonna targhet della funzione
    dataframe: dataframe
    '''
    
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.linear_model import LinearRegression
    
    d=dataframe.copy()
    colonne=np.array(d.columns)
    d.dropna(inplace=True)
    
    d=d.values
    x=d[:,0]
    y=d[:,1]
    regressione=LinearRegression()
    regressione.fit(x[:,np.newaxis],y)
    score=regressione.score(x[:,np.newaxis],y)
    
    coef_angolare=regressione.coef_[0]
    term_noto=regressione.intercept_
    
    array_x=np.linspace(np.min(x),np.max(x),100)
    array_y=coef_angolare*array_x+term_noto
    
    colonna=str(colonne[colonne!=target][0])
    fig,ax=plt.subplots(figsize=(6,6))
    ax.scatter(x,y,c="k",s=1.,alpha=0.5)
    ax.plot(array_x,array_y,color="r",linewidth=2.)
    ax.set_xlabel(colonna)
    ax.set_ylabel(target)
    ax.grid()
    plt.show()
