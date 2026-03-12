<h1 align="center">🐍 ds-mysql-python</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" />
</p>

<p align="center">
  Projeto de estudo e referência para integração entre <strong>Python</strong> e <strong>MySQL</strong> utilizando <strong>Docker Compose</strong>, <strong>SQLAlchemy ORM</strong> e scripts SQL versionados.
</p>

---

## 📋 Sobre o Projeto

Este projeto demonstra como estruturar uma aplicação Python conectada a um banco de dados MySQL rodando em container Docker. Inclui:

- 🐳 Ambiente completo via **Docker Compose**
- 🗄️ Integração com **MySQL 8.0**
- 🔗 Mapeamento objeto-relacional com **SQLAlchemy**
- 📜 Scripts SQL versionados para criação de tabelas
- 🏗️ Padrão **Repository** para acesso a dados

---

## 🗂️ Estrutura do Projeto

```
ds-mysql-python/
├── app/
│   ├── Dockerfile
│   ├── main.py          # Ponto de entrada da aplicação
│   ├── models.py        # Modelos SQLAlchemy (ORM)
│   └── requirements.txt
├── scripts/
│   └── script.sql       # Scripts SQL versionados
├── docker-compose.yml
└── README.md
```

---

## 🚀 Como Executar

### Pré-requisitos

- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) instalados

### Passo 1 — Subir o ambiente

```bash
docker-compose up --build
```

> Aguarde o healthcheck do MySQL passar. O serviço `app` só inicia após o banco estar pronto.

### Passo 2 — Acessar o MySQL via terminal (opcional)

```bash
docker exec -it mysql_db bash
apt update && apt install -y mysql-client
mysql -h localhost -u user -ppassword contratacao
```

### Passo 3 — Conectar via DBeaver ou outro cliente SQL

| Parâmetro | Valor        |
|-----------|-------------|
| Host      | `localhost`  |
| Port      | `3306`       |
| Database  | `contratacao`|
| User      | `user`       |
| Password  | `password`   |

### Passo 4 — Executar scripts versionados

Rode os scripts da pasta `scripts/` para criar as tabelas e popular dados iniciais:

```bash
mysql -h localhost -u user -ppassword contratacao < scripts/script.sql
```

---

## � Executando a Aplicação Python Localmente

Caso queira rodar o `main.py` fora do Docker (ex: para desenvolvimento e debug), siga os passos abaixo.

### Pré-requisitos

- Python 3.11+ instalado
- MySQL rodando (pode usar apenas o serviço `db` do Docker Compose)

### Passo 1 — Subir somente o banco de dados

```bash
docker-compose up db -d
```

> Isso sobe apenas o MySQL, sem o container da aplicação.

### Passo 2 — Criar e ativar o ambiente virtual

```bash
# Criar o venv
python -m venv venv

# Ativar no macOS/Linux
source venv/bin/activate

# Ativar no Windows
venv\Scripts\activate
```

### Passo 3 — Instalar as dependências

```bash
pip install -r app/requirements.txt
```

### Passo 4 — Configurar as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto ou exporte as variáveis no terminal:

```bash
export DB_HOST=localhost
export DB_USER=user
export DB_PASSWORD=password
export DB_NAME=contratacao
```

> ⚠️ No `main.py` as variáveis estão atualmente com valores fixos. Para usar o `.env`, descomente as linhas com `os.getenv(...)` e comente as que têm os valores hardcoded.

### Passo 5 — Executar a aplicação

```bash
python app/main.py
```

Você verá no terminal o contrato cadastrado e os registros consultados no banco. ✅

---

## �🛠️ Tecnologias

| Tecnologia   | Versão  | Uso                          |
|-------------|---------|------------------------------|
| Python      | 3.11+   | Linguagem principal          |
| MySQL       | 8.0     | Banco de dados relacional    |
| SQLAlchemy  | Latest  | ORM / mapeamento de entidades|
| Docker      | Latest  | Containerização              |

---

## 📦 Variáveis de Ambiente

As variáveis abaixo podem ser configuradas no `docker-compose.yml` ou via `.env`:

```env
DB_HOST=db
DB_USER=user
DB_PASSWORD=password
DB_NAME=contratacao
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.

---

<p align="center">Feito com ❤️ por <strong>Daniel Smanioto</strong></p>