from Def import f6,f5,f4,f3,f1,f2,f7,f8,imprimirTablero,moverPieza,mapeoPieza
from Def import localizarPieza,imprimirTablero,validarPiezaBlanca,validarPiezaNegra,validarJugada,validarJugadaBlanca,tablero

print("------------------------------")
print("        LEGEND CHESS          ")
print("------------------------------")
print("Esto es un avance")

x=0
imprimirTablero()
while x<5:
    try:
        print("TURNO DE JUGAR BLANCAS")
        imprimirTablero()
        elegirPieza = input("Elija una pieza\n")
        if elegirPieza in f1 or elegirPieza in f2 or elegirPieza in f7 or elegirPieza in f8 or elegirPieza in f3:
            print("ELIJA SU MOVIMIENTO 1")
            columna = int(input("Número de columa: "))
            fila    = int(input("Número de fila: "))     
            validarJugadaBlanca(columna,fila,elegirPieza) 
            
        elif elegirPieza in f3 or elegirPieza in f4 or elegirPieza in f5 or elegirPieza in f6:
            print("ELIJA MOVIMIENTO DE LA PIEZA YA MOVIDA")
            columna = int(input("Número de columa: "))
            fila    = int(input("Número de fila: "))
            validarJugadaBlanca(columna,fila,elegirPieza)
        else:
            print("No me encuentro")
    except ValueError:
            print("Movimiento inválido")
    x=x+1
        
        



# imprimirTablero()
# pieza=int(input("Elija pieza"))
# # print("Donde quiere mover")
# # fila= int(input("Fila: "))
# # columna= input("Columna: ")
# # pLoca=localizarPieza(columna,fila)
# # print(validarJugada(p))
# validarJugadaBlanca(pieza)




# x=0

# while x<4:
#     flag=True
#     
#     while flag == True:
        
                
#     flag=True
#     print("TURNO DE JUGAR NEGRAS")
#     elegirPieza = input("Elija una pieza\n")
#     while flag == True:
#         try:
#             if elegirPieza in f7 or elegirPieza in f8:
#                 print("ELIJA SU MOVIMIENTO")
#                 columna = int(input("Número de columa: "))
#                 fila    = int(input("Número de fila: "))
#                 mapeoPieza(elegirPieza)
#                 moverPieza(columna,fila,elegirPieza)
#                 flag=False
#             elif elegirPieza in f6 or elegirPieza in f5 or elegirPieza in f4 or elegirPieza in f3:
#                 print("ELIJA MOVIMIENTO DE LA PIEZA YA MOVIDA")
#                 columna = int(input("Número de columa: "))
#                 fila    = int(input("Número de fila: "))
#                 mapeoPieza(elegirPieza)
#                 moverPieza(columna,fila,elegirPieza)
#                 flag=False
#         except ValueError:
#             print("Movimiento inválido")
    
#     x=x+1    
        