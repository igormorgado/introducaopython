# Introdução a Computação Científica com Python

Bem vindo. Neste curso você irá aprender o mínimo necessário para utilizar uma linguagem de computação para resolver problemas comuns dentro da sua vida acadêmica como computações simples, criação de gráficos e inserção dos gráficos em um artigo.

Leia este texto com atenção até o final, ele terá instruções em como proceder e preparar o seu ambiente para o início de cada aula (ou para refazer as aulas em casa).

Vamos nos divertir.


## Por que Python?

"Por que não?" seria uma ótima contra pergunta, mas também poderiamos dizer o mesmo para C, Ruby, C#, Java, Julia, Fortran ou C++. Todas estas são [linguagens conhecidas][Python_vs_World], que gozam de uma ótima reputação (independente das opiniões do autor) e competentes para serem utilizadas neste cenário, nenhuma destas possui a versatilidade, simplicidade e foco em computação numérica como o Python.

Existe uma piada interna dos desenvolvedores Python que diz:

*"O Python é a segunda melhor lingaguem para qualquer coisa" -- Autor Desconhecido*

Pode parecer ruim, mas apesar de tudo é um ótimo mérito. Ao aprender Python você pode não obter a performance esperada e extrair o máximo do seu hardware ([e isso é também um debate][IBM_C_vs_Python_vs_Julia]), mas terá uma performance satisfatória (e muito boa se programar da forma correta). Pode não possuir todas as estruturas esperadas de uma linguagem orientada a objetos (como o C++/Java) ou Funcional (como o Elixir ou Haskell), mas permite trabalhar com os três paradigmas mais comuns da atualidade em uma única linguagem, o que é bastente poderoso. É uma linguagem bastente expressiva, com tipagem dinâmica (que é uma vantagem ao mesmo tempo que uma desvantagem), onde é possivel escrever ideias com o minimo de código possível sem perder a expressividade. Python lhe dará o poder de criar interfaces gráficas dignas de aplicações profissionais como o [Glade][Python_Glade] e o [QT][Python_QT] (sem ter aquela aparencia de que seu programa nao encaixa com o ambiente), permite o desenvolvemento de ferramentas para automação de tarefas como no [Blender][Blender_API] e [GIMP][Python_Fu]. 

Esses são alguns dos motivos para aprender Python como uma ferramenta do dia a dia. Nosso foco será a computação científica.

## Computação Científica com Python

O Python começou a emergir como uma ferramenta de computação Científica com o surgimento do projeto [SciPy][SciPy] em especial da biblioteca [NumPy][NumPy], que permitiu ao Python realizar operações vetoriais e matriciais com performance compatível a linguagens compiladas como o C e o Fortran (que ainda é o rei neste segmento). Após o NumPy diversos projetos se seguiram, como a [MatplotLib][MatplotLib] que é uma biblioteca para gráficos, [Pandas][Pandas] uma biblioteca para manipulação de dados tabulares e séries temporais e mais recentemente [Scikit-Learn][scikit], [TensorFlow][tensorflow] e [OpenCV][opencv] bibliotecas usadas em aprendizagem de máquina, redes profundas e visão computacional. O número de aplicações para Python não para de crescer e hoje é sem dúvidas a linguagem número um para prototipação na pesquisa em redes de aprendizagem profunda.

Esse é o motivo pelo qual o Python foi escolhido para este curso. 

## Conteúdo do Curso

O curso é dividido em 3 aulas de 2 horas que apresenta o básico da linguagem Python e formas de representar, visualizar e operar com os dados numéricos. Também iremos aprender em como exportar estes gráficos dentro de um artigo científico de forma manter a coerência textual e a aparência.

### Aula 1

* Obtendo o Python
* Acessando o Jupyter Notebook
* Estrutura básica da linguagem Python
* Manipulando cadeias
* Visualizando dados unidimensionais

### Aula 2

* Definindo funções puras
* Manipulando e visualizando matrizes
* Laços temporais e espaciais
* Operando com submatrizes

### Aula 3

* Operações de disco com dados numéricos
* Anatomia de um gráfico
* Embelezando o gráfico
* Exportando para um artigo


## Iniciando o ambiente do curso:

1. Abra um terminal

2. Vá para um diretório onde vá trabalhar (preferencialmente um pendrive particular).

    ```
    cd /media/<MEUPENDRIVE>
    ```

3. Clone o repositório do curso

    ```
    git clone https://github.com/igormorgado/introducaopython
    ```

4. Entre no diretório do curso

    ```
    cd introduçãopython
    ```

5. Execute o teste de ambiente

    ```
    chmod 755 ./testenv.sh
    ./testenv.sh
    ```

6. Se voce não ver um OK bem grande na tela após alguns minutos de teste, comunique imediatamente.


[Python_vs_World]: https://www.python.org/doc/essays/comparisons/
[IBM_C_vs_Python_vs_Julia]: https://www.ibm.com/developerworks/community/blogs/jfp/entry/A_Comparison_Of_C_Julia_Python_Numba_Cython_Scipy_and_BLAS_on_LU_Factorization?lang=en
[Python_Glade]: https://glade.gnome.org/
[Python_Fu]: https://www.ibm.com/developerworks/br/library/os-autogimp/index.html
[Blender_API]: https://docs.blender.org/api/current/
[Python_QT]: https://www.qt.io/qt-for-python
[SciPy]: https://www.scipy.org/
[NumPy]: http://www.numpy.org/
[Matplotlib]: https://matplotlib.org/
[Pandas]: http://pandas.pydata.org/
[scikit]: https://scikit-learn.org/stable/
[tensorflow]: https://www.tensorflow.org/
[opencv]: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html

