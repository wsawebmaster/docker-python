# Ambiente para desenvolvimento Python com Docker

### Passo a passo
Clonar Repositório
```sh
git clone https://github.com/wsawebmaster/docker-python.git
```

```sh
cd docker-python
```

Subir os containers do projeto
```sh
docker-compose up -d
```

Acessar o projeto
[http://localhost:5000](http://localhost:5000)


Caso quira acessar o container python
```sh
docker-compose exec python bash
```

Executar arquivo teste.py
```sh
python teste.py
```

Sair do container
```sh
exit
```
---
---


### Remover todos os contêineres, redes e volumes definidos no arquivo docker-compose.yml

    docker-compose down

### Remover contêineres, imagens e limpar redes não utilizadas.

    [ "$(docker ps -q)" ] && docker stop $(docker ps -q); [ "$(docker ps -aq)" ] && docker rm $(docker ps -aq); [ "$(docker images -q)" ] && docker rmi $(docker images -q); docker network prune -f


---
---

### 📧 Contato

[LinkedIn](https://www.linkedin.com/in/wsawebmaster/)

[wsawebmaster@yahoo.com.br](mailto:wsawebmaster@yahoo.com.br)