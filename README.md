# rabbitmq-message-queue

A simple message queue system using RabbitMQ and Python for asynchronous messaging.

## 🚀 Features
- Uses **RabbitMQ** for message queuing.
- Implements **producer-consumer pattern** for asynchronous processing.
- Lightweight and scalable for distributed systems.

## 📂 Project Structure
```
rabbitmq-message-queue/
│── src/
│   ├── producer.py  # Sends messages to RabbitMQ
│   ├── consumer.py  # Consumes messages from RabbitMQ
│── requirements.txt  # Dependencies
│── README.md
```

## 🛠 Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/tktarun03/rabbitmq-message-queue.git
   cd rabbitmq-message-queue
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start RabbitMQ (Docker recommended):
   ```bash
   docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
   ```

4. Run the consumer (waiting for messages):
   ```bash
   python src/consumer.py
   ```

5. Send a message using the producer:
   ```bash
   python src/producer.py
   ```

6. The **consumer will receive and process the message asynchronously**.

## 👨‍💻 About the Author

🚀 Created by [Arunkumar Thamilarasu](https://github.com/tktarun03) | UI Technical Architect | Messaging & Asynchronous Processing Expert

## ⭐ Contribute & Support
- Fork & Star this repository! ⭐
- Submit Issues and PRs to improve the message queue.

---
🎯 **Follow me on GitHub**: [@tktarun03](https://github.com/tktarun03)
