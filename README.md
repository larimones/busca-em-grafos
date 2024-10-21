# busca-em-grafos
Testando algoritmos de busca em um grafo baseado na minha matrícula.


- nessário  python3;

- Para executar:
```sh
python3 nome_dometodo.py
```
### Floyd-Warshall:

Encontra as menores distâncias entre todos os pares de vértices em um grafo, vamos calcular duas matrizes:

**Matriz de Distâncias:** Mostra a menor distância entre cada par de vértices.

**Matriz de Predecessores:** Mostra o predecessor de cada vértice no caminho mais curto entre cada par de vértices.

**Algoritmo:**
Inicialize a matriz de distâncias com os pesos das arestas existentes, colocando infinito (inf) onde não há aresta direta.
Inicialize a matriz de predecessores com o índice do vértice de origem se houver uma aresta, e None onde não houver.
Para cada vértice intermediário
𝑘
k, verifique se o caminho passando por
𝑘
k é menor do que o caminho direto entre os pares de vértices
𝑖
i e
𝑗
j. Se for, atualize a matriz de distâncias e a matriz de predecessores.

### Bellman Ford:

O Algoritmo de Bellman-Ford foi implementado para calcular as menores distâncias a partir de um vértice de origem até todos os outros vértices.
O algoritmo relaxa as arestas várias vezes (o número de vértices - 1 vezes) e atualiza as distâncias e predecessores.
Depois disso, ele verifica se há ciclos de peso negativo no grafo.
O código imprime tanto o arranjo de distâncias quanto o de predecessores, e também a árvore de custo mínimo.

### Kruskal

Ordena todas as arestas do grafo pelos pesos.
Utiliza a estrutura de conjuntos disjuntos para adicionar arestas na Construção da Árvore Geradora Mínima (MST), garantindo que não haja ciclos.
Mostra as arestas da MST e o custo total.

### Passos para o Dijkstra:

**Inicializar as Distâncias e Predecessores**: Criar listas para armazenar as distâncias e os predecessores de cada nó.

**Algoritmo:**
Inicializar a distância do nó de origem como 0 e as demais como infinito.
Usar uma fila de prioridade para selecionar o próximo nó com a menor distância.
Atualizar as distâncias e predecessores dos vizinhos do nó selecionado.

**Construir a Árvore de Custo Mínimo:**  Usar os predecessores para construir a árvore de custo mínimo.

**Exibir os Resultados** : Mostrar o arranjo de distância, o de predecessores e a árvore de custo mínimo.
