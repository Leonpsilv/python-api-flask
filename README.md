# PYTHON-API-FLASK
## Running the project
    To run this project, just do a git clone and run the follow command:
-   pip install -r requirements.txt

## Running docker container
    To run the aplication's container, follow the nexts steps:
-   docker build -t *IMAGE_NAME* .
-   docker run -d -p *DOCKER_PORT* : *LOCAL_PORT* -e MYSQL_ROOT_PASSWORD=*Rootpasswordexample* -e MYSQL_DATABASE=*DATABASE_NAME* -e MYSQL_USER=*RootUserExample* -e MYSQL_PASSWORD=*Mysqlpasswordexample* *IMAGE_NAME*