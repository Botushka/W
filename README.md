
# How to Run

1. Clone the repository to your local machine

2. Make sure you have Docker installed

3. Open a terminal or command prompt and navigate to the project directory

4. Build the Docker image by running the following command:

## Commands

docker build -t name .

example -> docker build -t hello-world .

Run the Docker container by running the following command:

docker run -p 5000:5000 name

example  -> docker run -p 5000:5000 hello-world

Access the application by opening a web browser and navigating to http://localhost:5000
