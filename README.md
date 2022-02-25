# Pokemon: apanhá-los todos

## Problema

O Ash está a apanhar pokémons num mundo que consiste numa grelha bidimensional infinita de casas.
Em cada casa há exatamente um pokémon.

O Ash começa por apanhar o pokémon que está na casa onde começa. A seguir, move-se para a casa
imediatamente a norte, sul, este ou oeste de onde se encontra e apanha o pokémon que aí se encontrar,
e assim sucessivamente. Atenção: se ele passar numa casa onde já passou (e, portanto, onde já apanhou
um pokémon), já lá não está um pokémon para ele apanhar!

O que queremos saber é: começando com um mundo cheio de pokémons (um em cada casa!), quantos
pokémons o Ash apanha para uma dada sequência de movimentos?

### Formato do input

O programa deve ler uma linha do stdin, que contém uma sequência de movimentos. Cada movimento é
descrito por uma letra N, S, Eou O(respetivamente: norte, sul, este, oeste)

### Formato do output

O programa deve escrever uma linha para o stdout, apenas com um número: quantos pokémons o Ash
apanhou?

### Exemplos

Input | Output |
--- | --- |
E | 2 |
NESO | 4 |
NSNSNSNSNS | 2 |

### Considerações técnicas
- Podes usar a linguagem / stack tecnológica que preferires. No entanto, é preciso que, com o teu
código-fonte, nos forneças o comando completo que permite compilar (se necessário) e executar
a tua solução.
- A tua solução deve ser correta (do ponto de vista funcional) e eficiente (tempo gasto, memória
ocupada, etc.). Sugerimos portanto que escrevas testes que ponham à prova a tua solução para lá
dos inputs de exemplo (inputs de maior dimensão, casos bicudos, etc.), e que os incluas no
código-fonte que enviares.
- Também damos (muito) valor ao quão compreensível e organizado é o teu código.

## Solução proposta

 - Iniciamos dois contadores, `x_counter` e `y_counter`, que representam a posição X e Y de Ash no grid bidimensional
 - Iniciamos um dicionário, `visited_positions`, que ira armanezar as posições em que Ash já passou. Aqui utilizamos o `defaultdict` para indicar que _keys_ que não existem no dicionário devem começar com o valor `0`. Chaves do dicionário serão tuplas com a posição que se deseja verificar se foi visitada (exemplo para verificar a posição 0 em X e 0 em Y, utilizariamos `visited_positions[(0,0)]`)
 - Indicamos que a posição inicial já começa visitada e iniciamos a variável de quantidade de pokemons capturados em 1
 - Iteramos sobre cada um dos movimentos adquiridos do _stdin_
 - Utilizamos _ifs_ para atualizar a posição de Ash 
    - Movimentos para norte acrescentam em 1 o contador de Y
    - Movimentos para sul decresem em 1 o contador de Y
    - Movimentos para este acrescentam em 1 o contador de X
    - Movimentos para oeste decresem em 1 o contador de X
 - Verificamos se a posição após o movimento já foi visitada
    - Se a posição não foi visitada seu valor no dicionário é 0 e portanto atualizamos para 1 e acrescentamos 1 para o contador de pokemons capturados.
    - Se a posição já foi visitada seu valor no dicionário é 1 e o códido passa para o próximo movimento
 - No final do _for_ printamos a quantidade de pokemons capturados

 Complexidade temporal da solução proposta é O(N) onde N é quantidade de movimentos de Ash pois utlizamos apenas um _for loop_ e utilizamos dicionários (que possuem tempo de localização ~O(1))

 Código foi escrito em Python3 e não possui nenhuma dependência. Para rodar a solução basta executar o seguinte comanda na pasta raiz:
 
 ```bash
 python pokemon.py
 ```
 
  Para rodar os testes basta executar o seguinte comando na pasta raiz:

 ```bash
 python tests.py
 ```
