#A ordenação por seleção é um algoritmo bom, mas não é muito rápido.
#O QuickSort é um algoritmo de ordenação mais eficiente, que tem tempo de execução médio de O(n log n).
 
#Exemplo de codigo
def buscaaMenor(arr):
    menor = arr[0]
    menor_indice = 0    
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacaoporSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaaMenor(arr)  # Corrigido o nome da função
        novoArr.append(arr.pop(menor))
    return novoArr  # Corrigido a indentação do return

print(ordenacaoporSelecao([5, 3, 6, 2, 10]))  # Corrigido a chamada da função
