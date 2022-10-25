from copy import error
import os as cln
import copy
import time as clock

def SortTypeMethods():
    
    #---------------Options to choose the sort function type |||or the explain option|||----------------#

        def optionsToSort(a):
            a = int(a)
            while True:

                if a==1:
                    quickSort(lista)
                    break

                elif a==2:
                    bubbleSort(lista)
                    break

                elif a==3:
                    selectionSort(lista)
                    break
            
                elif a==4:
                    insertionSort(lista)
                    break

#----------------------EXPLAIN TYPE OF SORT---------------------#

    #     def descriptions():
        
    #         cln.system("cls")
        
    #         a = int( input("""Select the method to explain\n\n    
    # >>>   Quick Sort o Bubble Sort (1, 2, 3, 4)  >>> """) )

    #         while True:
            
    #             if a == 1:
                
    #                 cln.system("cls")
                
    #                 QuickSortExplain()
    #                 break


        #----------------------QUICK-SORT---------------------#
        def quickSort(lista):

            listBeforeTheChange = dup

            cln.system("cls")

            print( f"\n\n The list before the change>>> {listBeforeTheChange} ")
            input( "Press \"ENTER\" to continue..." )

            cln.system("cls")

            pivote=( len(lista) // 2)

            leftList=[]

            rigthList=[]

            for i in range( len(lista) ):

                if lista[i] <= int( pivote ):

                    leftList.append( lista[i] )

                else:

                    rigthList.append( lista[i] )

            n = 0
            
            while n == 0:
            
                n = 1
            
                for i in range( len( leftList) - 1 ):

                    if leftList[i] > leftList[ ( i + 1 ) ]:

                        aux = leftList[ ( i + 1 ) ]

                        leftList[ ( i + 1 ) ] = leftList[i]

                        leftList[i] = aux
                        n = 0

                for j in range ( len(rigthList) - 1 ):

                    if rigthList[j] > rigthList[ (j + 1) ]:

                        aux = rigthList[ (j+1) ]

                        rigthList[ (j+1) ] = rigthList[j]

                        rigthList[j] = aux

                        n=0

            cln.system("cls")
        
            print(f"\n QUICK SORT>>>>>>>>>>>  {leftList + rigthList}\n")
        
       

        #----------------------BUBBLE-SORT---------------------#

        def bubbleSort(lista):


            listaAnterior = dup

            cln.system("cls")
        
            print("\n\n The list before the change>>> ", listaAnterior )
        
            input("Press \"ENTER\" to continue...")
        
            cln.system("cls")
        
            bubbleList=lista
        
            n = 0


            while n == 0:
            
                n=1
            
                for i in range ( len(bubbleList)-1 ):
                
                    if bubbleList[i] > bubbleList[ (i+1) ]:

                        aux = bubbleList[ (i+1) ]

                        bubbleList[ (i+1) ] = bubbleList[i]

                        bubbleList[ (i) ] = aux

                        n = 0



            cln.system("cls")
        
            print("\n BUBBLE SORT>>>>>>>>>>   ", bubbleList, " \n")

        #----------------------SELECTION-SORT---------------------#

        def selectionSort(lista):

            listaAnterior = dup

            cln.system("cls")
        
            print("\n\n The list before the change>>> ", listaAnterior )
        
            input("Press \"ENTER\" to continue...")
        
            cln.system("cls")

            n = len(lista)


            for  i in range( n - 1 ):

                print("\nThe actual list is >>> ", lista )

                menor = i
                cambios=i

                print("\nThe actual index to compare is ", menor)

                for j in range ( i + 1, n ):

                    if lista[j] < lista[menor]:

                        menor = j

                        print(f"\nTraveling the list. Index {menor} is lesss ", )

                temporal = lista[menor]

                lista[menor]=lista[i]

                lista[i]=temporal

                print("\n We change the element", lista[menor], " by the element", lista[i])
                print("\n\tCHANGES", cambios + 1)
            print("\n\n SELECTION SORT>>>>>>>>>>   ", lista, " \n")

        #----------------------INSERTION-SORT---------------------#

        def insertionSort(lista):
        
            listaAnterior = dup
        
            cln.system("cls")
            print("\n\n The list before the change>>> ", listaAnterior )
        
            input("Press \"ENTER\" to continue...")
        
            cln.system("cls")
        
            length = len(lista)

            for i in range(length - 1):

                numToCompare = lista[i]

                for j  in range(i+1, length):

                    compare= lista[j]

                    print("The value to compare is {}, and the number with wich it is compared is {} \n ".format(numToCompare, compare)  )
                
                    if (lista[i] > lista[j]):
                    
                        aux = lista[j]

                        lista[j] = lista[i]

                        lista[i] = aux

                        print("--"*5,f"""Whe have changed the element {lista[j]} {"--"*5} 
                    {"--"*5} with the number {lista[i]} ""","--"*5, "\n" )
            print("\n\n INSERTION SORT>>>>>>>>>>   ", lista, " \n")

#---------------------------------------------#---------------------------------------------#


        while True:
            options=["1","2","3","4"]

            x = input("Insert values separated by commas ','>>> ")
        
            cln.system("cls")

            lista=x.split(",")
            print(lista)
            cln.system("pause")

            lista= [int(z) for z in lista]

            print ( f"\n\tlista>>>> {lista}" )

            dup = copy.copy(lista)

            while True:

                cln.system("cls")

                print ( f"\n\tlista>>>>  {dup}")

                a=str(input("""\nHello, Choose a option  (1, 2, 3, 4)\n\n
    >>>   (1)Quick Sort , (2)Bubble Sort , (3)Selection Sort, (4)Insertion Sort. \n"""))

                if a in options:
                    break


            optionsToSort(a)

            if True:

                while True: 

                
                    print("Do you want try it again?\n")
                
                    again=input("(y o n)>>> ").lower()
                    cln.system("cls")
                    if str(again) == "y":
                        reUse=(input("¿Do you want do it with the same list? Type (y , n)>>> ")).lower()
                    else:
                        exit()
                        break
                    if reUse == "y":

                        cln.system("cls")
                    
                        print ( "\n\tlista>>>>   ", dup)

                        while True:
                        
                            cln.system("cls")
                        
                            print ( "\n\tlista>>>>   ", dup )
                        
                            a=str(input("""\nHello, Choose a option  (1, 2, 3, 4, ?)\n\n
    >>>   (1)Quick Sort , (2)Bubble Sort , (3)Selection Sort, (4)Insertion Sort. \n"""))
        
                            if a in options:
                            
                                optionsToSort(a)
                            
                                break
                            
                        
                            else:
                                True
                    else:
                        cln.system("cls")
                        break

SortTypeMethods()




#______________________ORDENAMIENTO CON PIVOTE____________________#




# def agregar(lista):
#     pivot=int(len(lista)/2)
#     lista_izq=[]
#     lista_der=[]
#     aux=[]

#     for i in range(len(lista)):
#         if lista[i]<pivot:
#             lista_izq.append(lista[i])
#         if lista[i]>pivot:
#             lista_der.append(lista[i])
#     print(lista_izq, "  lista izq")
#     print(lista_der, "  lista der")

#     n=0
#     while n==0:
#         n=1
#         for i in range(len(lista_izq)-1):
#             if lista_izq[(i+1)]<lista_izq[i]:
#                 aux=lista_izq[(i+1)]
#                 lista_izq[(i+1)]=lista_izq[i]
#                 lista_izq[(i)]=aux
#                 n=0


#         for i in range(len(lista_der)-1):
#             if lista_der[(i)]>lista_der[(i+1)]:
#                 aux=lista_der[(i+1)]
#                 lista_der[(i+1)]=lista_der[i]
#                 lista_der[i]=aux
#                 n=0
#     if pivot in lista:
#         lista_cen=[pivot]

#         print("La lista ordenada es >>>> ", lista_izq+lista_cen+lista_der)


#     return ""
# lista=[1,5,6,1,2,3,1,79,8,7,0]

# print(agregar(lista))

# # # print(ordenar(lista))
