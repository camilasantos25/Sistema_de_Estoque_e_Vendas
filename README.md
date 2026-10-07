# Sistema de Estoque e Vendas

Sistema de linha de comando, feito em Python, para controlar produtos,
vendas e relatórios de estoque. O projeto foi desenvolvido para praticar
Estrutura de Dados: vetores ordenados e não ordenados, busca linear,
busca binária e Big-O.

## Funcionalidades

- Cadastrar produtos (código, nome, categoria, preço e quantidade)
- Código de produto único (não permite duplicados)
- Editar e remover produtos
- Buscar produto por código (busca binária)
- Buscar produtos por nome (busca linear)
- Listar produtos ordenados por código
- Listar produtos por categoria
- Registrar vendas, com validação de estoque
- Relatório de estoque baixo, com limite configurável
- Salvar e carregar os dados em arquivo CSV

### Regras de negócio

- Não é permitido cadastrar código duplicado.
- O preço deve ser maior que zero.
- A quantidade não pode ser negativa.
- Não é permitido vender mais unidades do que existem em estoque.

## Tecnologias

- Python 3
- Módulo `csv` (biblioteca padrão do Python)

## Estrutura dos arquivos

```
sistema_estoque/
├── main.py       # menu e interação com o usuário
├── produto.py    # classe Produto e validações de preço e quantidade
├── estoque.py    # classe Estoque: listas e operações (cadastro, buscas, vendas)
├── arquivos.py   # salvar e carregar os dados em CSV
├── dados.csv     # dados de exemplo
└── testes/
    └── dados_ruim.csv   # arquivo com linhas inválidas, usado em testes
```

Cada arquivo tem uma responsabilidade:

- **`main.py`**: é o único que conversa com o usuário (`print` e `input`).
- **`produto.py`**: define o que é um produto e valida preço e quantidade.
- **`estoque.py`**: guarda os produtos nas listas e implementa as operações.
- **`arquivos.py`**: só lê e escreve no disco, sem regras de negócio.

## Como executar

1. Tenha o Python 3 instalado.
2. No terminal, entre na pasta do projeto.
3. Execute:

```
python main.py
```

Ao escolher a opção `0` (Salvar e sair), os dados são gravados em `dados.csv`.
Se o arquivo não existir, o sistema começa vazio.

**Atenção:** os dados só são salvos ao sair pela opção `0`. Se o programa for
fechado de outra forma, as alterações da sessão são perdidas.

## Exemplo de uso

```
===== Sistema de Estoque e Vendas =====
1 - Listar produtos (por código)
2 - Buscar produto por código
3 - Buscar produtos por nome
4 - Listar produtos por categoria
5 - Cadastrar produto
6 - Editar produto
7 - Remover produto
8 - Registrar venda
9 - Relatório de estoque baixo
10 - Configurar limite de estoque baixo
0 - Salvar e sair
Escolha: 2
Código: 50
  50 | Caneta Azul | Papelaria | R$ 2.5 | qtd: 100
```

## Formato do arquivo de dados

O arquivo `dados.csv` tem uma linha por produto, com cabeçalho:

```
codigo,nome,categoria,preco,quantidade
7,"Caneta, Preta",Papelaria,3.0,60
12,Caderno,Papelaria,15.9,40
```

Ao carregar, linhas inválidas (preço negativo, texto no lugar de número,
campos faltando, código repetido) são ignoradas e o sistema mostra um aviso
com o número da linha.

## Como os vetores são utilizados

O `Estoque` mantém **duas listas** (vetores) que guardam os **mesmos objetos**
`Produto`. Não são cópias: as duas listas apontam para os mesmos produtos,
então uma alteração (como reduzir a quantidade numa venda) aparece nas duas.

### Vetor não ordenado: `produtos`

Os produtos ficam na ordem em que foram cadastrados, sem nenhuma regra de
organização. Inserir é rápido, pois o novo produto vai direto para o final.
Esta lista é usada na busca por nome.

### Vetor ordenado: `produtos_ordenados`

Os produtos ficam sempre em ordem crescente de código. Ao cadastrar, o sistema
descobre a posição correta e insere o produto ali, empurrando os seguintes
para a direita. Assim a lista nunca precisa ser reordenada. Esta lista é usada
na busca por código e nas listagens.

### Remoção

Remover um produto exige tirá-lo das **duas** listas. Em cada uma, os itens
seguintes são puxados uma posição para a esquerda.

### Por que duas listas?

Nenhuma das duas estruturas é melhor em tudo. A lista ordenada permite busca
rápida por código, mas custa mais para manter. Usar as duas permite comparar
as vantagens e desvantagens de cada uma.

## Como funcionam as buscas

### Busca por nome: busca linear

O sistema percorre a lista `produtos` um item por vez, verificando se o texto
digitado está contido no nome do produto (sem diferenciar maiúsculas de
minúsculas). Não há atalho: o nome não segue nenhuma ordem na lista, e a busca
pode encontrar vários produtos, então ela sempre olha a lista inteira.

Complexidade: **O(n)**.

### Busca por código: busca binária

A lista `produtos_ordenados` está em ordem crescente de código. A busca olha o
item do meio:

- se o código do meio é o procurado, terminou;
- se é menor que o procurado, o item só pode estar à direita, então a metade
  esquerda é descartada;
- se é maior, o item só pode estar à esquerda, então a metade direita é
  descartada.

O processo se repete com o que sobrou, até achar o item ou não restar mais
nada para olhar. Cada passo elimina metade da lista, por isso ela é tão rápida.

**A lista precisa estar ordenada.** Numa lista bagunçada, olhar o item do meio
não diz nada sobre onde o procurado está, e não seria possível descartar
nenhuma metade com segurança.

Complexidade: **O(log n)**.

### Comparação

| Itens na lista | Busca linear (O(n)) | Busca binária (O(log n)) |
|---|---|---|
| 10 | até 10 verificações | cerca de 4 |
| 1.000 | até 1.000 | cerca de 10 |
| 1.000.000 | até 1.000.000 | cerca de 20 |

## Complexidade das operações

| Operação | Estrutura | Custo |
|---|---|---|
| Cadastrar (adicionar no fim da lista não ordenada) | `produtos` | O(1) |
| Cadastrar (inserir mantendo a ordem) | `produtos_ordenados` | O(n) |
| Buscar por código | `produtos_ordenados` | O(log n) |
| Buscar por nome | `produtos` | O(n) |
| Editar | busca binária + troca de valores | O(log n) |
| Vender | busca binária + troca de valor | O(log n) |
| Remover | busca binária + remoção nas duas listas | O(n) |
| Listar por código | `produtos_ordenados` (já ordenada) | O(n) |
| Listar por categoria | `produtos_ordenados` | O(n) |
| Relatório de estoque baixo | `produtos_ordenados` | O(n) |

O cadastro completo custa **O(n)**, porque a inserção ordenada domina o custo
das outras etapas.
