# TabulaTalent Backend

## Setting up the Project
0. Make sure that you have [Python 3.11 or newer](https://www.python.org/downloads/) and [Docker](https://www.docker.com/) installed in your system. You must also have [Docker Account and login to Docker in the CLI](https://docs.docker.com/docker-hub/access-tokens/#use-an-access-token).

1. Clone this repository into your local machine.

2. Run the following command to initialize Python virtual environment.
   
    ```ps
    # Windows
    py -3 -m venv .venv
    ```

    ```shell
    # MacOS
    python3 -m venv .venv
    ```

3. Run the following command to activate the corresponding environment.

    ```ps
    # Windows
    .venv\Scripts\activate
    ```

    ```shell
    # MacOS
    . .venv/bin/activate
    ```

4. Run the following command to install necessary modules.
   
    ```ps
    # Windows
    pip install -r requirements.txt
    ```

    ```shell
    # MacOS
    pip3 install -r requirements.txt
    ```

5. Duplicate the `.env.example` and rename it to `.env`.
   
    ```ps
    # Windows
    copy .env.example .env
    ```

    ```shell
    # MacOS
    cp .env.example .env
    ```

6. Use the following command to run the application and database.

    ```shell
    docker compose up
    ```

* Press `ctrl + c` to stop the application.

## Developing this repository
If you already follow the setup instructions above, the next time you want to run the application, just run these commands:
```shell
docker compose up
```

### Modifying Python Modules or Dockerfile
If you wish to add, remove, or update any Python modules in this repository, you can use `pip` commands as usual. After you finish modifying Python modules or Dockerfile, run the following command:
```shell
docker compose up --build -d && docker image prune --force && docker compose stop;
```
The command above re-builds the Docker Image with the new python modules you modified and removes old Docker Image.
