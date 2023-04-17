piezas_Blancas = ['PnB1','PnB2','PnB3','PnB4','PnB5','PnB6','PnB7','PnB8','TrB1','TrB2','CbB1','CbB2','AfB1','AfB2','Rey0','DamB']
piezas_Negras =  ['PnN1','PnN2','PnN3','PnN4','PnN5','PnN6','PnN7','PnN8','TrN1','TrN2','CbN1','CbN2','AfN1','AfN2','Rey1','DamN']

f8 = ['TrN1','CbN1','AfN1','Rey1','DamN','AfN2','CbN2','TrN2']
f7 = ['PnN1','PnN2','PnN3','PnN4','PnN5','PnN6','PnN7','PnN8']
f6 = ['    ','    ','    ','    ','    ','    ','    ','    ']
f5 = ['    ','    ','    ','    ','    ','    ','    ','    ']
f4 = ['    ','    ','    ','    ','    ','    ','    ','    ']
f3 = ['    ','    ','    ','    ','    ','    ','    ','    ']
f2 = ['PnB1','PnB2','PnB3','PnB4','PnB5','PnB6','PnB7','PnB8']
f1 = ['TrB1','CbB1','AfB1','Rey0','DamB','AfB2','CbB2','TrB2']

tablero = [f1,f2,f3,f4,f5,f6,f7,f8]

#Elimina la pieza de su ubicación anterior antes de ser movida
def eliminarPieza(pieza):
    if pieza in f1:
        columa = f1.index(pieza)
        f1[columa] = '    '
    elif pieza in f2:  
        columa=f2.index(pieza)
        f2[columa] = '    '
    elif pieza in f3:
        columa=f3.index(pieza)
        f3[columa] = '    '
    elif pieza in f4:
        columa=f4.index(pieza)
        f4[columa] = '    '
    elif pieza in f5:  
        columa=f5.index(pieza)
        f5[columa] = '    '
    elif pieza in f6:
        columa=f6.index(pieza)
        f6[columa] = '    '
    elif pieza in f7:  
        columa=f7.index(pieza)
        f7[columa] = '    '
    elif pieza in f8:
        columa=f8.index(pieza)
        f8[columa] = '    '
    
#Localiza filas de la pieza
def mapeoPieza(pieza):
    if pieza in f1:
        fila = 1
        columa = f1.index(pieza)
        return fila,columa+1
    elif pieza in f2:  
        fila = 2
        columa=f2.index(pieza)
        return fila,columa+1
    elif pieza in f3:
        fila = 3
        columa=f3.index(pieza)
        return fila,columa+1
    elif pieza in f4:
        fila = 4
        columa=f4.index(pieza)
        return fila,columa+1
    elif pieza in f5:  
        fila = 5
        columa=f5.index(pieza)
        return fila,columa+1
    elif pieza in f6:
        fila = 6
        columa=f6.index(pieza)
        return fila,columa+1
    elif pieza in f7:  
        fila = 7
        columa=f7.index(pieza)
        return fila,columa+1
    elif pieza in f8:
        fila = 8
        columa=f8.index(pieza)
        return fila,columa+1
        
def moverPieza(columna,fila,pieza):
    if fila  == 6:
        f6[columna-1] = pieza
        imprimirTablero()
    elif fila == 5:
        f5[columna-1] = pieza
        imprimirTablero()
    elif fila == 4:
        f4[columna-1] = pieza
        imprimirTablero()
    elif fila == 3:
        f3[columna-1] = pieza
        imprimirTablero()
    else:
        print("Columna o fila inválida")   
            
def localizarPieza(columa,fila):
    intColuma = {
        'a':1,
        'b':2,
        'c':3,
        'd':4,
        'e':5,
        'f':6,
        'g':7,
        'h':8
    }
    encuentraPieza = {
        8 : f8[intColuma[columa]-1],
        7 : f7[intColuma[columa]-1],
        6 : f6[intColuma[columa]-1],
        5 : f5[intColuma[columa]-1],
        4 : f4[intColuma[columa]-1],
        3 : f3[intColuma[columa]-1],
        2 : f2[intColuma[columa]-1],
        1 : f1[intColuma[columa]-1]
    }
    if encuentraPieza[fila] == "    ":
        print("No hay pieza")
        return ""
    else:
        print("La pieza que corresponde: "+encuentraPieza[fila])
        print("Notación ajedrez "+columa+str(fila))
        return encuentraPieza[fila]

def validarPiezaBlanca(pieza):
    Flag = False
    if pieza in piezas_Blancas:
        Flag = True
        return Flag
    else:
        return Flag
        
def validarPiezaNegra(pieza):
    flag = False
    if pieza in piezas_Negras:
        flag = True
        return flag
    else:
        return flag
    
def validarJugadaBlanca(columna,fila,pieza):
    #Obtengo las coordenas de antes y después de las piezas
    flaPiezaAnt,ClmnaPiezaAnt = mapeoPieza(pieza)
    flaPiezaDsp,ClmnaPiezaDsp = fila,columna
    
    Sur = flaPiezaDsp-flaPiezaAnt
    Norte = flaPiezaDsp-flaPiezaAnt
    Este = ClmnaPiezaAnt-ClmnaPiezaDsp #+1
    Oeste = ClmnaPiezaDsp-ClmnaPiezaAnt #+1
    
    #Movimiento Peon
    if pieza in piezas_Blancas[0:7]:
        if Norte == 1 or Norte == 2:
            moverPieza(columna,fila,pieza)
            eliminarPieza(pieza)
            print("Es un peon")
        else:
            print("Movimiento peon Inválido")
    #Movimiento Caballo
    elif pieza in piezas_Blancas[10:11]:
        if Norte == 2 and Este == 1 or Norte == 2 and Oeste == 1:
            eliminarPieza(pieza)
            moverPieza(columna,fila,pieza)
            print("Es un caballo")
        else:
            print("Movimiento caballo inválido")
    #Movimiento alfil
    elif pieza in piezas_Blancas[12:13]:
        for x in range(-7,8,1):
            if Norte == x and Este  == x or Norte == x and Oeste == x:
                eliminarPieza(pieza)
                moverPieza(columna,fila,pieza)
                print("Movimiento exito Es un alfil")
                break
            else:
                print("Movimiento alfil inválido")
    #Movimiento Torre
    elif pieza in piezas_Blancas[8:9]:
        for x in range(-7,8,1):
            print(Norte)
            print(Oeste)
            print
            if Norte == x and Oeste == 0 or Oeste == x and Norte == 0:
                print(x)
                eliminarPieza(pieza)
                moverPieza(columna,fila,pieza)
                print("Movimiento exito Es una torre")
                break
    #Movimiento Dama
    elif pieza in piezas_Blancas[15]:
        for x in range(-7,8,1):
            print(x)
            if Norte == x and Oeste == 0 or Oeste == x and Norte == 0 or Norte == x and Este  == x or Norte == x and Oeste == x:
                eliminarPieza(pieza)
                moverPieza(columna,fila,pieza)
                print("Movimiento Dama exitoso")
                break
            else:
                print("Movimiento Dama inválido")
    #Movimiento Rey
    elif pieza in piezas_Blancas[14]:
        print(Norte)
        print(Oeste)
        print(Este)
        if Norte == 1 and Oeste == 0 and Este == 0 or Norte == -1 and Este == 0 and Oeste == 0:
            eliminarPieza(pieza)
            moverPieza(columna,fila,pieza)
            print("Movimiento exitoso")
        else:
            print("Movimiento Rey inválido")
    else:
        print("Movimiento inválido general")
        
def validarJugadaNegra(pieza):
    print("Hola")
    
def validarJugada(pieza):
    vPN = validarPiezaBlanca(pieza)
    vPB = validarPiezaNegra(pieza)
    mensage = "Movimiento éxitoso"
    
    if vPB == True:
        return mensage
    elif validarPiezaBlanca(pieza) == False:
        print("")
    
    if vPN == True:
        return mensage
    elif validarPiezaNegra(pieza) == False:
        print("")

def imprimirTablero():
    print("      ' a  ','  b  ','  c  ','  d  ','  e  ','  f  ','  g  ','  h  '")
    print("Fila8"+str(f8))
    print("Fila7"+str(f7))
    print("Fila6"+str(f6))
    print("Fila5"+str(f5))
    print("Fila4"+str(f4))
    print("Fila3"+str(f3))
    print("Fila2"+str(f2))
    print("Fila1"+str(f1))