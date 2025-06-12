# ds-mysql-python


## Passo 1 - rodar docker para iniciar o banco de dados
`docker-compose up --build` 


## Passo 2 - Conectar via bash no mysql

`docker exec -it mysql_db bash`
`apt update && apt install -y mysql-client`
`mysql -h db -uuser -ppassword contratacao`

## Passo 3 - Conectar no mysql dbeaver 

## Passo 4 - Rodas os scripts versionados para criar tabelas 

## Passo 5 - Fim