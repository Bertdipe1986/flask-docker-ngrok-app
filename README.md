# Flask Docker Ngrok App

This is a minimal Flask application running in a Docker container, with [ngrok](https://ngrok.com/) support to expose your local development server to the internet.

## 🚀 Features

- Python Flask API (basic endpoint)
- Dockerized environment
- Exposes service using ngrok tunnel
- Suitable for quick API testing and demos

## 🛠️ Prerequisites

# Flask Docker App with ngrok

This is a simple Flask application containerized using Docker and exposed to the internet using [ngrok](https://ngrok.com). It’s perfect for testing or demoing your local app without deploying to a server.

---

## 🚀 Features

- Simple Flask API
- Dockerized for easy deployment
- `ngrok` used to expose app to the internet
- Ready for GitHub

---

## 📁 Project Structure

flask-app/
│
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── Dockerfile # Docker build instructions
└── README.md # Project documentation


---

## 🛠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Bertdipe1986/flask-docker-ngrok-app.git
cd flask-docker-ngrok-app

### 2. Build Docker Image

docker build -t flask-app .

### 3. Run the Docker Container

docker run -p 5000:5000 flask-app

### 4. Start ngrok to Expose Your App

### 4. Start ngrok to Expose Your App

ngrok config add-authtoken <your_ngrok_token>
ngrok http 5000

You’ll get a public HTTPS URL like:
https://your-subdomain.ngrok-free.app

 Example Endpoints
GET / – Home route

GET /api – Placeholder API route

🔒 Security Tips
NEVER commit your ngrok authtoken to GitHub

Add the following to your .gitignore:

*.env
config.yml

📄 License
This project is licensed under the MIT License.
