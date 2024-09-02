# SQLite Tutorial
<br>
How to recovert data from a Docker container.
<br>
<br>

# Docker Container Running
<br>
In the API the database is configured to be stored in the current directory with this line:
<br>

```bash
DATABASE_URL = "sqlite:///./snake_game.db"
```  
<br>
To access the database from the Docker container, you need to search for the API container and retrieve its identifier to access the database.
<br>
<br>

```bash
sudo docker ps
sudo docker exec -it <container_id_or_name> /bin/bash
ls
```  