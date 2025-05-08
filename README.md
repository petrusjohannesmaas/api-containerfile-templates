# ECR API Templates

## Overview

**ECR API Templates** is a collection of lightweight, containerized API templates for **Python Flask**, **JavaScript (Express.js)**, and **Go (net/http)**, designed for deployment on **AWS Elastic Container Registry (ECR)**. These templates provide a simple starting point for creating and deploying backend services using **Podman**.

> **Note:** You can replace Podman commands with Docker, as both adhere to the Open Container Initiative (OCI) standards. Just swap `podman` with `docker` in the commands, and everything should work with minimal adjustments!

## How to Use This Repo

This is a template repository, allowing you to generate new repositories with the same structure, branches, and files—without including my commit history. For more details, check out GitHub's guide on creating repositories from templates:
[GitHub Docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)

You may also want to integrate this template with my [Development Database Deployer](https://github.com/petrusjohannesmaas/dev-database-deployer) project to quickly set up an API and database container. Modify the API code as needed to add packages or ORMs (e.g., `mongoose`, `pg`, `SQLAlchemy`, etc.).
Make sure to update the `requirements.txt` (for Python) or `package.json` (for JavaScript) files as well!

## Image Versions

Below are the latest stable, LTS, and major releases for **Python**, **Go**, and **JavaScript (Node.js)** that can be used in your **Containerfiles**:

### Python

* **Latest Stable:** Python 3.13.3 (April 8, 2025) [Download](https://www.python.org/downloads/)
* **Latest LTS:** Python 3.11 (Security updates until October 2027) [More Info](https://www.python.org/downloads/)
* **Upcoming Major Release:** Python 3.14 (Planned for October 2025) [Schedule](https://www.python.org/downloads/)

### Go

* **Latest Stable:** Go 1.24.3 (May 7, 2025) [Release Notes](https://devblogs.microsoft.com/go/go-1-24-3-1-and-1-23-9-1-microsoft-builds-now-available/)
* **Latest Major Release:** Go 1.24.0 (February 11, 2025) [Release History](https://go.dev/doc/devel/release)

### JavaScript (Node.js)

* **Latest Stable:** Node.js 21
* **Latest LTS:** Node.js 20
* **Upcoming LTS:** Node.js 22 (Expected October 2025)

> **Note:** For containerization, **LTS versions** are recommended for better stability.

## Clone the Repository

```sh
git clone https://github.com/petrusjohannesmaas/ECR-API-Templates.git
cd ECR-API-Templates
```

## Building Containers

### Flask (Python)

```sh
podman build -t flask-api -f Containerfile .
```

### Express (JavaScript)

```sh
podman build -t express-api -f Containerfile .
```

### Go

```sh
podman build -t go-api -f Containerfile .
```

## Running Containers

### Flask (Python) - Port 5000

```sh
podman run -d -p 5000:5000 flask-api
```

### Express (JavaScript) - Port 3000

```sh
podman run -d -p 3000:3000 express-api
```

### Go - Port 8080

```sh
podman run -d -p 8080:8080 go-api
```

## Testing APIs

You can test the APIs using `curl` or directly from your browser:

```sh
curl http://localhost:5000/  # Flask API
curl http://localhost:3000/  # Express API
curl http://localhost:8080/  # Go API
```

Or open these URLs in your browser:

* Flask: `http://localhost:5000/`
* Express: `http://localhost:3000/`
* Go: `http://localhost:8080/`

## Managing Containers

To manage your containers:

```sh
podman ps        # List running containers
podman stop <id> # Stop a container
podman rm <id>   # Remove a container
```

## Automating with GitHub Actions

You may want to set up **GitHub Actions** to automate container builds and deployments. Here's a guide on using **ECR with GitHub Actions**: [GitHub Docs](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-to-amazon-elastic-container-service)

## Pushing an Image to ECR Using Podman

1. **Authenticate with ECR**:

   ```sh
   aws ecr get-login-password --region <your-region> | podman login --username AWS --password-stdin <your-account-id>.dkr.ecr.<your-region>.amazonaws.com
   ```

2. **Create an ECR Repository** (if necessary):

   ```sh
   aws ecr create-repository --repository-name my-repository
   ```

3. **Build and Tag Your Podman Image**:

   ```sh
   podman build -t my-image .
   podman tag my-image:latest <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/my-repository:latest
   ```

4. **Push the Image to ECR**:

   ```sh
   podman push <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/my-repository:latest
   ```

5. **Verify the Image in ECR**:

   ```sh
   aws ecr list-images --repository-name my-repository
   ```

## Troubleshooting Podman Registry Issues

If Podman fails to find images (e.g., **Go** images), try defining a registry search in `/etc/containers/registries.conf`:

```sh
unqualified-search-registries = ["docker.io"]
```

Alternatively, you can use fully qualified names:

```sh
podman pull docker.io/golang:1.24
```
