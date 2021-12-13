# 6sem
 aplicação criada para avaliação do 6° semetre do curso de ciencia da computação 

esta aplicação tem por objetivo realiza as interaçoe do usuario com o banco de dados mysql, que por sua vez  esta a rodar em um conteiner docker, o objetivo final sera alcançado quando a aplicação for capaz de listar, inserir e editar infomaçoes do banco de dados estando tambem sendo execudada em um conteiner docker 


# Venv
esta aplicação necessitou de uma bliblioteca para conecxão com o banco de dados

    pip install mysql-connector-python
    
# Docker 
foi utilizado um conteine para a Mysql para armazenar os dados e um conteiner PhpMyAdmin para gerenciar, ambos criados atraves do seguinte Compose:

    version: '3'
    services:
        db:
            image: mysql:5.7
            environment:
                MYSQL_ROOT_PASSWORD: "Cloud21!"
                MYSQL_DATABASE: "appdb"
            ports:
                - "3306:3306"
            volumes:
                - ./Volumes/MySql:/var/lib/mysql
            networks:
                - mysql-network
        phpmyadmin:
            image: phpmyadmin
            ports:
                - 8080:80
            networks:
                - mysql-network
            environment:
                - PMA_ARBITRARY=1
        networks: 
            mysql-network:
                driver: bridge