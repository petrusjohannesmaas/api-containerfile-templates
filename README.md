# 🐳 API Containerfile Templates

## 🚀 Overview

A collection of production-ready containerized API templates for:

* **Python Flask**
* **JavaScript (Express.js)**
* **Go (net/http)**

These templates offer a simple yet powerful starting point for building and deploying backend APIs using **Docker** or **Podman**.

> 💡 **Tip:** Podman can be used as a drop-in replacement for Docker. Just swap `docker` with `podman`—they both follow the [OCI standards](https://opencontainers.org/).

---

## 📦 Repository Usage

This repository is a **template**—you can generate your own project from it without copying my commit history. For help, refer to [GitHub’s Template Repo Guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

Want to include a database too? Use it alongside my [`dev-database-deployer`](https://github.com/petrusjohannesmaas/dev-database-deployer) for a full API + database dev environment.

---

## 🛠 Image Versions

Choose from stable or long-term support (LTS) versions when customizing your `Containerfile`.

### 🐍 Python

| Version  | Notes                             |
| -------- | --------------------------------- |
| `3.13.3` | Latest Stable (April 2025)        |
| `3.11`   | LTS (Sec. updates until Oct 2027) |
| `3.14`   | Upcoming (Oct 2025)               |

### 🦫 Go

| Version  | Notes                    |
| -------- | ------------------------ |
| `1.24.3` | Latest Stable (May 2025) |
| `1.24.0` | Major Release (Feb 2025) |

### ⚙️ Node.js

| Version | Notes                   |
| ------- | ----------------------- |
| `21.x`  | Latest Stable           |
| `20.x`  | LTS                     |
| `22.x`  | Upcoming LTS (Oct 2025) |

> ✅ **Recommended:** Use LTS versions for stability in production environments.

---

## 📂 Clone the Repository

```bash
git clone https://github.com/petrusjohannesmaas/api-containerfile-templates.git
cd api-containerfile-templates
```

---

## 🏗️ Building the Containers

### Flask (Python)

```bash
docker build -t flask-api -f Containerfile .
```

### Express (JavaScript)

```bash
docker build -t express-api -f Containerfile .
```

### Go (net/http)

```bash
docker build -t go-api -f Containerfile .
```

---

## ▶️ Running the Containers

### Flask (Port `5000`)

```bash
docker run -d -p 5000:5000 flask-api
```

### Express (Port `3000`)

```bash
docker run -d -p 3000:3000 express-api
```

### Go (Port `8080`)

```bash
docker run -d -p 8080:8080 go-api
```

---

## 🔍 Testing the APIs

Use `curl` or open in your browser:

```bash
curl http://localhost:5000/  # Flask
curl http://localhost:3000/  # Express
curl http://localhost:8080/  # Go
```

Or visit:

* [http://localhost:5000](http://localhost:5000) – Flask
* [http://localhost:3000](http://localhost:3000) – Express
* [http://localhost:8080](http://localhost:8080) – Go

---

## 📤 Pushing to Docker Hub

To share your image publicly:

### 1. Log in to Docker Hub

```bash
docker login
```

### 2. Tag your image

```bash
docker tag flask-api yourusername/flask-api:latest
```

### 3. Push the image

```bash
docker push yourusername/flask-api:latest
```

Repeat the steps for other images (`express-api`, `go-api`) as needed.

> 📝 Replace `yourusername` with your Docker Hub username.

---

## 🧰 Managing Containers

```bash
docker ps                # List active containers
docker stop <container>  # Stop container
docker rm <container>    # Remove container
```

---

## 📈 Future Enhancements

* Add more language templates (e.g., Rust, Java)
* Add support for **Docker Compose**
* Add support for **Kubernetes** deployment files
* Improve Go template to support third-party packages
* **Incorporate CI/CD processes** (e.g., GitHub Actions, GitLab CI)

---

## 📄 License

MIT License © [Petrus Johannes Maas](https://github.com/petrusjohannesmaas)