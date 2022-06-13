# Grafos API with Python Flask

<p align="center">
    <img src= "https://berinhard.github.io/talks/tdc_grafos/images/full_graph.jpg" 
    width="400" height="200"/><br>
</p>

---
## Motivation

Montar uma API para tratar e representar Grafos de uma maneira mais simples usando Python.

---
## Dependencies

### Mandatory

- Python
- Docker
- Make

### Opcional

- [x] Insominia or similar to view API Requests Documentation
---

## How to run

### Running standalone

run only the API 

```sh
make run-locally
```

### Running with Docker

```sh
run-locally-docker
```
### How to test
Run tests and the coverage
```sh
make test-application
```
---
### Documentation

#### Padrão do projeto

A arquitetura desse projeto tenta reproduzir algo mais simplista de uma arq Hexagonal. As pastas seguem algo na ideia onde temos os *Handlers* como interface principal com mundo real e comunicando-se com os *controllers*. A partir deles temos os *repositories* com as funções de persistência dos dados e nossa regra de negócio e validações no *domain*.

### Banco de dados

Como há algo bem simples e não pensando em escalabilidade não houve a necessidade de adicionar um banco de dados, mas poderia facilmente adicionar um não-relacional, como o MongoDB e adicionar sua imagem ao docker-compose. Se adicionado teria que mudar algumas lógicas por trás das funções (utilizando o pandas). 

Nesse caso mais simples, apenas utiliza-se um json para fazer a persistência dos dados.


---

### Critique

Esse projeto dentém de algumas falhas:

- Falta de testes, que foram suprimidos. 

- Podemos ter um problema de perfomance principalmente no caso do *Get Grafos Level 2* pois estamos fazendo um processo O(nˆ2), não muito amigável caso nossos dados sejam muito grandes. Além desse processo a própria utilização do pandas para simplicar alguns processos há uma boa perda de desempenho.

- Numero limitado de usuários: caso tenha duas "Anas" a segunda não poderá ser adicionada, para corrigir isso poderíamos modificar os nomes por uuids únicos e a partir deles fazer o link com o nome da pessoa. Porém o escopo do projeto não preve tal situação. 