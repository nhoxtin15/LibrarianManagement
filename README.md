
# Library Management System

This is a Library Management System built using Odoo. The system helps manage books, borrowers, lending operations, and inventory within a library.

## Features
- Book Catalog Management
- Book's Copies Management
- Borrower and Borrowing Management
- Lending and Returning Operations

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Docker**: Make sure Docker is installed on your machine. If it's not installed, follow the installation instructions below.

## Installing Docker

### For Linux:

```bash
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```
### For MacOS:
1. Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/) for macOS.
### For Window:
1. Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/) for Window.
2. Ensure WSL 2 is enabled (required for Docker Desktop on Windows).

##Running the Application
1. Clone the repository:
```bash
git clone https://github.com/nhoxtin15/LibrarianManagement.git
cd LibrarianManagement
```
2. Build and start the application using Docker Compose:
```bash
docker-compose up --build
```
3. Access the application:
You can access the application by any web browser using the link https://localhost:8069/web


