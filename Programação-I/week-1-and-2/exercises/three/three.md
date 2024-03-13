Quais são os dois principais processos de tradução de linguagens de alto nível para linguagem de máquina? Diferencie-os.

Interpretação e compilação. 

Um interpretador é um programa que recebe como entrada um arquivo contendo um programa fonte e lê linha a linha este arquivo de entrada, executando uma a uma as instruções que estão nele programadas. Um programa pode ser executado em qualquer máquina, desde que haja o interpretador disponível para utilização. Se houver algum erro de no código (que vá contra as definições da linguagem), o programa será interrompido abruptamente com um erro. 

Um compilador é um programa (ou um conjunto de programas) que recebe como entrada um programa fonte e cria um novo arquivo como saída: o arquivo de entrada é o código fonte escrito pelo programador; o arquivo que o compilador produz é normalmente identificado como código objeto e contém instruções de baixo nível, traduzidas para a linguagem de máquina. O código produzido não é portável para qualquer arquitetura e diferentes compiladores são construídos para as diferentes arquiteturas de processadores (diferentes famílias de processadores possuem conjuntos diferentes de instruções). Além disso, o compilador somente gera corretamente o código objeto caso não tenha encontrado um erro de compilação. 
