## Dependencies
You will need the following dependencies to run the project:
- Docker
- Docker Compose

## Installation
To start, simply run the compose file with
```sh
docker compose up
```

A folder called `airflow` will be created if it does not already exist.
You will need to change the permissions of the folder to your user:
```sh
# e.g.
sudo chown soonann -R airflow
```

Note that the DAGs are placed in the `airflow/dags` directory
Should you need to edit it, feel free to change anything there
```sh
vim airflow/dags
```

By default, the following services have been forwarded to the respective ports:
- MongoDB `localhost:27017`
- Airflow `localhost:8080`

## Credentials
The default credentials for MongoDB and Airflow are as follows:
```sh
# airflow
user: airflow
password: airflow

# mongodb
user: mongo
password: mongo
```
