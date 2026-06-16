# Atividade de Acompanhamento – Fluxo Máximo

## Problema G – UVa 820: Internet Bandwidth

### Integrantes

* Caio Pacely
* Catarina Garcia
* Paulo de Tarso

---

# 1. Resumo do Problema

O problema consiste em determinar a largura de banda máxima que pode ser transmitida entre dois computadores de uma rede. Cada conexão possui uma capacidade máxima de transmissão de dados e os dados podem ser enviados simultaneamente por diferentes caminhos.

O objetivo é descobrir a quantidade máxima de fluxo que pode sair de um nó de origem e chegar a um nó de destino, respeitando as capacidades de todas as conexões da rede.

Esse problema pode ser modelado diretamente como um problema de **Fluxo Máximo**.

---

# 2. Interpretação da Entrada e da Saída

## Entrada

A entrada descreve uma rede de computadores.

Primeiramente é fornecido:

* `n`: quantidade de nós da rede;
* `s`: nó de origem;
* `t`: nó de destino;
* `c`: quantidade de conexões.

Em seguida aparecem `c` linhas no formato:

```text
u v capacidade
```

onde:

* `u` = primeiro nó da conexão;
* `v` = segundo nó da conexão;
* `capacidade` = largura de banda da conexão.

As conexões são bidirecionais e podem existir múltiplas conexões entre o mesmo par de nós.

---

## Saída

Para cada rede deve ser exibida a largura de banda máxima entre o nó de origem e o nó de destino.

Formato:

```text
Network X
The bandwidth is Y.
```

onde:

* `X` é o número do caso de teste;
* `Y` é o fluxo máximo encontrado.

---

# 3. Modelagem da Rede de Fluxo

## Vértices

Cada computador da rede será representado por um vértice.

```text
Computador 1 → Vértice 1
Computador 2 → Vértice 2
Computador 3 → Vértice 3
Computador 4 → Vértice 4
```

---

## Origem

O vértice correspondente ao nó `s`.

Neste exemplo:

```text
Origem = 1
```

---

## Sorvedouro

O vértice correspondente ao nó `t`.

Neste exemplo:

```text
Destino = 4
```

---

## Arestas

Cada conexão da entrada gera uma aresta com capacidade igual à largura de banda informada.

Exemplo:

```text
1 2 20
```

representa uma conexão entre os nós 1 e 2 com capacidade 20.

---

## Capacidades

As capacidades representam exatamente a quantidade máxima de dados que pode trafegar por cada conexão.

Dessa forma, as restrições do problema são modeladas corretamente pela rede de fluxo.

---

# 4. Justificativa da Escolha do Algoritmo

Foi escolhido o algoritmo **Edmonds-Karp**, uma implementação específica do algoritmo de Ford-Fulkerson.

A principal diferença é que o Edmonds-Karp utiliza uma **Busca em Largura (BFS)** para encontrar os caminhos aumentantes no grafo residual.

A escolha foi feita porque:

- Garante um comportamento determinístico;
- É mais fácil de implementar e depurar;
- Evita escolhas ruins de caminhos aumentantes;
- Possui prova formal de complexidade polinomial;
- É adequado para os limites do problema.

O algoritmo funciona da seguinte forma:

1. Executa uma BFS no grafo residual para encontrar um caminho da origem ao destino;
2. Determina o gargalo do caminho encontrado;
3. Envia fluxo igual ao gargalo;
4. Atualiza o grafo residual;
5. Repete o processo até que a BFS não encontre mais caminhos aumentantes.

Quando não existir mais caminho entre a origem e o destino no grafo residual, o fluxo encontrado será o fluxo máximo da rede.

---

# 5. Instância Pequena

Utilizaremos a rede apresentada no enunciado.

## Entrada

```text
4
1 4 5
1 2 20
1 3 10
2 3 5
2 4 10
3 4 20
```

## Representação da Rede

![Representação da Rede](https://github.com/user-attachments/assets/bcd1e962-7d96-451c-ae47-4f7ecacb6958)

---

# 6. Execução Manual do Algoritmo Edmonds-Karp

## Estado Inicial

Fluxo total:

```text
0
```

Capacidades iniciais:

```text
1→2 = 20
1→3 = 10
2→3 = 5
2→4 = 10
3→4 = 20
```

---

## Iteração 1

A BFS parte do vértice 1.

Os vértices alcançados são:

```text
1 → 2
1 → 3
```

Ao expandir o vértice 2, a BFS encontra o destino 4.

Assim, o primeiro caminho aumentante encontrado é:

```text
1 → 2 → 4
```

Capacidades:

```text
1→2 = 20
2→4 = 10
```

### Gargalo

```text
min(20,10) = 10
```

### Fluxo enviado

```text
10
```

### Fluxo acumulado

```text
10
```

### Atualização do Grafo Residual

```text
1→2 = 10
2→4 = 0

2→1 = 10
4→2 = 10
```

---

## Iteração 2

Executamos novamente a BFS.

Partindo do nó 1:

```text
1 → 3
```

Ao expandir o vértice 3, alcançamos o destino 4.

Caminho aumentante:

```text
1 → 3 → 4
```

Capacidades:

```text
1→3 = 10
3→4 = 20
```

### Gargalo

```text
min(10,20) = 10
```

### Fluxo enviado

```text
10
```

### Fluxo acumulado

```text
20
```

### Atualização do Grafo Residual

```text
1→3 = 0
3→4 = 10

3→1 = 10
4→3 = 10
```

---

## Iteração 3

Executamos novamente a BFS.

A partir do nó 1 ainda existe capacidade para chegar ao nó 2.

A BFS encontra:

```text
1 → 2 → 3 → 4
```

Capacidades residuais:

```text
1→2 = 10
2→3 = 5
3→4 = 10
```

### Gargalo

```text
min(10,5,10) = 5
```

### Fluxo enviado

```text
5
```

### Fluxo acumulado

```text
25
```

### Atualização do Grafo Residual

```text
1→2 = 5
2→3 = 0
3→4 = 5
```

---

## Iteração 4

Executamos uma nova BFS.

Partindo do nó 1:

```text
1 → 2
```

Porém:

```text
2→4 = 0
2→3 = 0
```

Não existe caminho que alcance o nó 4.

Portanto, a BFS falha em encontrar um novo caminho aumentante.

O algoritmo é encerrado.

---

## Resumo das Iterações

| Iteração | Caminho Encontrado pela BFS | Gargalo | Fluxo Acumulado |
|-----------|---------------------------|----------|-----------------|
| 1 | 1 → 2 → 4 | 10 | 10 |
| 2 | 1 → 3 → 4 | 10 | 20 |
| 3 | 1 → 2 → 3 → 4 | 5 | 25 |
---

# 7. Verificação da Resposta Final

Os fluxos enviados foram:

```text
1 → 2 → 4      = 10
1 → 3 → 4      = 10
1 → 2 → 3 → 4  = 5
```

Somando os fluxos:

```text
10 + 10 + 5 = 25
```

Logo:

```text
Fluxo Máximo = 25
```

Portanto, a largura de banda máxima entre os nós 1 e 4 é igual a **25**.

## Saída Esperada

```text
Network 1
The bandwidth is 25.
```

## Interpretação do Resultado

Isso significa que a rede consegue transmitir até 25 unidades de dados por unidade de tempo do nó 1 para o nó 4 utilizando simultaneamente diferentes caminhos da rede sem violar nenhuma restrição de capacidade.

---

# Conclusão

O problema **Internet Bandwidth** pode ser modelado diretamente como uma rede de fluxo, onde os computadores são representados por vértices e as conexões da rede por arestas com capacidades correspondentes à largura de banda máxima permitida.

Utilizando o algoritmo **Edmonds-Karp**, foi possível encontrar sucessivos caminhos aumentantes por meio da **Busca em Largura (BFS)**. A cada iteração, foi identificado o gargalo do caminho, enviado o fluxo correspondente e atualizado o grafo residual até que não existissem mais caminhos disponíveis entre a origem e o destino.

Ao final do processo, o fluxo acumulado obtido foi de **25 unidades**, representando a largura de banda máxima que pode ser transmitida entre os nós 1 e 4, respeitando todas as restrições de capacidade da rede.
