# Sistema WEB - Jogos Digitais (FATEC Carapicuíba)

### Instruções para sistemas Debian
## Preparando

### Baixe as dependências
> sudo apt-get install \
>      apt-transport-https \
>      ca-certificates \
>      curl \
>      gnupg2 \
>      software-properties-common

### Adicione a chave do repositório:
> curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -

### Adicione o repositório:
> sudo add-apt-repository \
>    "deb [arch=amd64] https://download.docker.com/linux/debian \
>    $(lsb_release -cs) \
>    stable"

### Atualize os repositórios e instale o Docker-CE:
> sudo apt-get update && sudo apt-get install docker-ce

### Para executar comandos sem precisar de sudo(Necessário encerrar a sessão):
> sudo usermod -aG docker $USER

### Baixe o docker-compose:
> sudo curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)" \
    -o /usr/local/bin/docker-compose

### Altere as permissões para executar:
> sudo chmod +x /usr/local/bin/docker-compose


## Executando
### Na pasta raiz inicializar os containers:
> docker-compose up


Acessar o site em http://localhost:5000
