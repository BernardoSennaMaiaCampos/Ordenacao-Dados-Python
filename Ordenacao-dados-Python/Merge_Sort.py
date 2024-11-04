import time
inicio_contagem = time.time()

def merge_sort(lista):
   

    if len(lista) > 1: 
        mid = len(lista) // 2 
        esquerda = lista[:mid] 
        direita = lista[mid:] 

        merge_sort(esquerda) 
        merge_sort(direita) 

        i=0 
        j=0 
        k=0 
        while i < len(esquerda) and j < len(direita): 
            if esquerda[i] < direita[j]:
                lista[k]=esquerda[i]
                i=i+1

            else:
                lista[k]=direita[j]
                j=j+1

            k=k+1

        while i < len(esquerda):
            lista[k]=esquerda[i]
            i=i+1
            k=k+1

        while j < len(direita):
            lista[k]=direita[j]
            j=j+1
            k=k+1

    return lista



lista200 = [  65,	139,	172,	 20,	180,	190,	 51,	 -4,	 53,	 12,
 21,	 75,	126,	102,	167,	 22,	 18,	 -1,	 48,	197,
196,	 31,	142,	-18,	 83,	-26,	 46,	-13,	194,	155,
177,	109,	116,	-19,	 68,	158,	130,	 30,	 87,	 16,
 89,	144,	-24,	120,	103,	111,	-15,	-38,	  3,	 57,
-37,	-20,	-30,	125,	 69,	 50,	-12,	 15,	 64,	 55,
156,	131,	127,	-33,	 -3,	 61,	-23,	176,	135,	 36,
 79,	171,	193,	-21,	 80,	106,	 54,	168,	 60,	-36,
 77,	191,	153,	 25,	182,	 27,	  2,	119,	-45,	134,
122,	199,	 78,	-17,	129,	198,	184,	  4,	 44,	150,
 66,	143,	124,	-41,	 24,	-39,	141,	105,	181,	-27,
-10,	137,	 84,	175,	 91,	-28,	 70,	 11,	121,	195,
 13,	 -8,	118,	117,	-48,	183,	146,	169,	 86,	 10,
 42,	 99,	 -5,	160,	-25,	114,	 97,	113,	115,	 28,
-43,	163,	 94,	 19,	157,	128,	 93,	173,	 81,	148,
 63,	149,	-34,	 82,	 -9,	101,	 58,	174,	-22,	123,
187,	165,	-29,	107,	108,	 -2,	133,	152,	 74,	 72,
 39,	 59,	-31,	-11,	 37,	  0,	 35,	192,	 71,	 45,
-32,	 32,	 62,	178,	200,	 73,	-40,	112,	 26,	138,
 43,	 92,	 23,	  9,	 88,	170,	164,	-49,	 14,	 67]

print('\nLista antes do merge = {}'.format(lista200))

merge_sort(lista200)

print('\nLista depois do merge = {}'.format(lista200))

final_contagem = time.time()

elapsed_time = final_contagem - inicio_contagem

print(f"\nTempo: {elapsed_time:.10f} ms") 

