# SQLite Tutorial

How to recovert data from a Docker container.
<br>

# Docker Container Running

In the API the database is configured to be stored in the current directory with this line:
<br>

```bash
DATABASE_URL = "sqlite:///./snake_game.db"
```  

To access the database from the Docker container, you need to search for the API container and retrieve its identifier to access the database.
<br>

```bash
$ sudo docker ps
$ sudo docker exec -it <container_id_or_name> /bin/bash
$ ls
```  

To download the database from the Docker container, you need to be out of Docker container and do the command below:
```bash
$ pwd
/path
$ sudo docker cp <container_id_or_name>:/path/database.db /path/to/download
```  

