# 🧮 Calculator | Python • Docker • GitHub Actions

A simple Python calculator project demonstrating **unit testing, Docker containerization, and Continuous Integration (CI) using GitHub Actions**.

The project supports basic arithmetic operations and automatically validates the code through unit tests and Docker-based test execution.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI-2088FF?logo=githubactions&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-8%20Passing-success)

## 📌 Project Overview

This project demonstrates how a Python application can be tested locally, packaged into a Docker image, and validated automatically through a GitHub Actions workflow.

Whenever code is pushed to the `main` branch or a pull request targets `main`, the CI pipeline runs the unit tests, builds the Docker image, and executes the tests inside the container.

## ✨ Features

- **Arithmetic Operations:** Addition, subtraction, multiplication, and division.
- **Input Validation:** Handles invalid input types and unsupported values.
- **Unit Testing:** Uses Python's built-in `unittest` framework.
- **Docker Containerization:** Runs tests in an isolated container.
- **Automated CI:** Uses GitHub Actions to validate changes.
- **Manual Workflow Trigger:** Supports running the pipeline manually from GitHub Actions.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Calculator implementation |
| `unittest` | Automated unit testing |
| Docker | Containerization and test execution |
| Git & GitHub | Version control and source-code hosting |
| GitHub Actions | Continuous Integration automation |

## 📂 Project Structure

```text
Calculator/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── lambda_app/
│   └── Calculator.py
├── test_calculator.py
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Install the following tools:

- Python 3.12 or a compatible version
- Docker Desktop
- Git

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd Calculator
```

Replace the placeholder with your actual GitHub repository URL.

### 2. Run the calculator

```bash
python lambda_app/Calculator.py
```

Follow the on-screen instructions to select an operation and enter the numbers.

### 3. Run unit tests locally

```bash
python -m unittest -v
```

The test suite checks arithmetic operations, division by zero, decimal division results, addition with zero, and subtraction with a negative result.

## 🐳 Run with Docker

Docker allows the test suite to run in a consistent, isolated environment.

### Build the image

```bash
docker build -t calculator .
```

### Execute the container

```bash
docker run --rm calculator
```

The Docker container automatically runs the unit tests. A successful run displays the test results and ends with `OK`.

## ⚙️ GitHub Actions CI Pipeline

The workflow is defined in `.github/workflows/ci-cd.yml`.

### Workflow Triggers

- **Push:** Runs when changes are pushed to `main`.
- **Pull Request:** Runs when a pull request targets `main`.
- **Manual Execution:** Can be started using `workflow_dispatch` in the GitHub Actions interface.

### Pipeline Workflow

```text
       Code Push / Pull Request
                  |
                  v
       Checkout Source Code
                  |
                  v
          Set Up Python 3.12
                  |
                  v
         Run Unit Tests
                  |
                  v
          Build Docker Image
                  |
                  v
       Run Tests Inside Docker
                  |
                  v
          Pipeline Result
```

### Pipeline Stages

| Stage | Description |
|---|---|
| Checkout | Retrieves the repository source code. |
| Python Setup | Configures Python 3.12 on the runner. |
| Unit Testing | Executes tests using `python -m unittest -v`. |
| Docker Build | Builds the calculator Docker image. |
| Container Testing | Runs the tests inside the Docker container. |

**Success criteria:** The workflow passes when all steps complete successfully, including both test runs and the Docker image build.

To view the results, open your GitHub repository and navigate to **Actions**.

## 🧪 Testing

The project currently contains **8 unit tests** covering:

- Addition
- Addition with zero
- Subtraction
- Subtraction producing a negative result
- Multiplication
- Division
- Division producing a decimal result
- Division by zero

All eight tests have passed in local execution and inside the Docker container.

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Python application development
- Writing and executing unit tests
- Building and running Docker images
- Using Git for version control
- Automating validation with GitHub Actions
- Understanding a basic CI workflow

## 📌 Project Scope

This project focuses on **Continuous Integration (CI)** through automated testing and Docker image building. AWS deployment and automated production deployment are not included in the current scope.
