# geeksdata
Geeksdata code - Environment and example code
Welcome to the Geeksdata repository! This repository contains code and examples for various data engineering and data science projects. To get started with our environment, you'll need to have Docker installed on your machine.

### Setting Up the Environment

1. **Install Docker**: If you haven't already, make sure to install Docker on your machine. Visit the [official Docker website](https://docs.docker.com/get-docker/) for installation instructions.

2. **Clone the Repository**: Clone this repository to your local machine using the following command:
   ```
   git clone https://github.com/your-repository/geeksdata.git
   ```

3. **Navigate to the Repository**: Change your directory to the cloned repository:
   ```
   cd geeksdata
   ```

4. **Start Docker Compose**: To set up and start the environment, run the following command:
   ```
   docker compose up -d
   ```
   This command will build and start all the necessary Docker containers in detached mode.

### Accessing the Services

- **Jupyter Notebook**: Once the Docker containers are up and running, you can access the Jupyter Notebook at `http://localhost:8888`.
- **Kafka UI**: To view Kafka topics and messages, access the Kafka UI at `http://localhost:8080`.

### Stopping the Environment
To stop the environment and remove the containers, networks, and volumes defined by `docker-compose.yml`, run the following command:
```
docker compose down -v 
```
