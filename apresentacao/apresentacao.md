# Apresentação do Trabalho - Fluxo Máximo

## Problema

O trabalho resolve o problema **UVA 820 - Internet Bandwidth**.

O objetivo é encontrar a **maior banda possível** entre um computador de origem e um de destino em uma rede com conexões de capacidade limitada.

## Ideia principal

Cada computador é representado por um vértice e cada conexão por uma aresta com capacidade.

Com isso, o problema é modelado como uma **rede de fluxo máximo**.

## Estratégia utilizada

A solução usa o algoritmo **Edmonds-Karp**:

1. encontra um caminho aumentante com BFS;
2. identifica o gargalo do caminho;
3. aumenta o fluxo;
4. repete até não existir mais caminho disponível.

## Resposta do problema

O valor final do fluxo é a **largura de banda máxima** entre a origem e o destino.

No exemplo testado no projeto, a resposta obtida foi:

```text
Network 1
The bandwidth is 25.
```

## Pontos importantes

- conexões repetidas são somadas;
- laços no próprio vértice são ignorados;
- a entrada termina com `0`, como no enunciado;
- a implementação trabalha com rede residual.

## Complexidade

O algoritmo Edmonds-Karp tem complexidade de tempo `O(nm^2)`, onde `n` é o número de vértices e `m` o número de conexões.
