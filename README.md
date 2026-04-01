# Kafka 101 - Producer & Consumer Learning Application

A simple Kafka learning application with a web interface for sending messages and a consumer for receiving them. Perfect for understanding Kafka producer-consumer patterns!

![Kafka Learning App](https://img.shields.io/badge/Kafka-Learning-blue) ![Python](https://img.shields.io/badge/Python-3.7+-green) ![Flask](https://img.shields.io/badge/Flask-3.0-red)

## 📋 Table of Contents

- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Confluent Cloud Setup](#-confluent-cloud-setup)
- [Application Setup](#-application-setup)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Troubleshooting](#-troubleshooting)
- [Learning Objectives](#-learning-objectives)
- [License](#-license)

## ✨ Features

- 🌐 **Beautiful Web Interface** - Send messages through an intuitive web UI
- 📝 **Command Line Producer** - Send messages via CLI for automation
- 👂 **Real-time Consumer** - Watch messages arrive in real-time
- 🔐 **Secure Configuration** - Credentials protected with .gitignore
- 📊 **Message Counter** - Track how many messages you've sent
- 🎨 **Responsive Design** - Works on desktop and mobile

## 📋 Prerequisites

- **Python 3.7+**
- **Confluent Cloud account** (free tier available with $400 credits)
- **Git** (for cloning the repository)

## ☁️ Confluent Cloud Setup

### Step 1: Create Confluent Cloud Account

1. Go to [https://confluent.cloud](https://confluent.cloud)
2. Click **"Start Free"** and sign up
3. Verify your email
4. You'll get **$400 in free credits** (valid for 30 days)

### Step 2: Create a Kafka Cluster

1. Click **"Create cluster"**
2. Select **"Basic"** cluster (free tier eligible)
3. Choose your cloud provider (AWS/GCP/Azure)
4. Select a region close to you
5. Name your cluster (e.g., "kafka-learning-cluster")
6. Click **"Launch cluster"**
7. Wait 5-10 minutes for provisioning

### Step 3: Create a Topic

1. In your cluster, click **"Topics"** in the left sidebar
2. Click **"Create topic"**
3. Name it: `user_messages`
4. Keep default settings (1 partition is fine)
5. Click **"Create with defaults"**

### Step 4: Generate API Keys

**⚠️ IMPORTANT: You'll only see the API Secret once!**

1. Click **"API keys"** in the left sidebar
2. Click **"Create key"**
3. Select **"Global access"**
4. Click **"Next"**
5. **Save both values immediately:**
   - **API Key** (username) - Example: `SWS674XAQY3UZ7UA`
   - **API Secret** (password) - Example: `cflt3+Yq9sWFnl4baGWz1ACrA4arImOtZtehIIDaMkkSDX5AXd7d13CczVcirw/Q`
6. Click **"Download and continue"** to save them
7. Store them securely (never commit to Git!)

### Step 5: Get Bootstrap Server

1. Go to **"Cluster settings"** or **"Cluster overview"**
2. Find **"Bootstrap server"**
3. Copy the address (format: `pkc-xxxxx.region.provider.confluent.cloud:9092`)

## 🚀 Application Setup

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd kafka-101-consumers
```

### 2. Configure Credentials

Copy the example configuration:

```bash
cp config/config.ini.example config/config.ini
```

Edit `config/config.ini` with your Confluent Cloud credentials:

```ini
[default]
# Paste your bootstrap server from Step 5
bootstrap.servers=pkc-xxxxx.us-east1.gcp.confluent.cloud:9092

security.protocol=SASL_SSL
sasl.mechanisms=PLAIN

# Paste your API Key from Step 4
sasl.username=YOUR_API_KEY_HERE

# Paste your API Secret from Step 4
sasl.password=YOUR_API_SECRET_HERE

[consumer]
group.id=python_kafka101_group_1
auto.offset.reset=earliest
```

**⚠️ Security Note:** `config/config.ini` is in `.gitignore` and will never be committed to Git.

### 3. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 4. Install Dependencies

**On macOS (install librdkafka first):**
```bash
brew install librdkafka
source .venv/bin/activate
pip install -r requirements.txt
```

**On Linux/Windows:**
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

**Using uv (faster alternative):**
```bash
source .venv/bin/activate
uv pip install -r requirements.txt
```

### 5. Verify Installation

Test that everything is installed:

```bash
pip list | grep -E "confluent-kafka|flask"
```

You should see:
```
confluent-kafka    2.3.0
flask             3.0.0
```

## 🎯 Usage

### Method 1: Web Interface (Recommended)

**Terminal 1 - Start Consumer:**
```bash
source .venv/bin/activate
python src/consumer.py config/config.ini
```

**Terminal 2 - Start Web App:**
```bash
source .venv/bin/activate
python src/app.py
```

**Open Browser:**
- Navigate to: **http://localhost:5001**
- Type a message in the text field
- Click "Send to Kafka"
- Watch it appear in the consumer terminal! 🎉

### Method 2: Command Line Producer

**Send a single message:**
```bash
source .venv/bin/activate
python src/producer.py config/config.ini -m "Hello Kafka!"
```

**Interactive mode (type multiple messages):**
```bash
source .venv/bin/activate
python src/producer.py config/config.ini
# Type messages and press Enter
# Press Ctrl+C to exit
```

## 📁 Project Structure

```
kafka-101-consumers/
├── .gitignore              # Protects sensitive files
├── LICENSE                 # MIT License
├── README.md              # This file
├── requirements.txt       # Python dependencies
│
├── config/
│   └── config.ini.example # Template for credentials
│
├── docs/                   # Documentation (if needed)
│
├── src/
│   ├── __init__.py        # Makes src a Python package
│   ├── app.py             # Flask web application
│   ├── consumer.py        # Kafka consumer script
│   └── producer.py        # Kafka producer script
│
└── templates/
    └── index.html         # Web interface
```

## 🛠️ Troubleshooting

### Authentication Errors

**Error:** `SASL authentication error: Authentication failed`

**Solutions:**
- ✅ Verify API Key and Secret are correct (no extra spaces)
- ✅ Check that you copied the full secret (it's very long!)
- ✅ Ensure the API key is for the correct cluster
- ✅ Verify your cluster is "Healthy" in Confluent Cloud

### Topic Not Found

**Error:** `Topic 'user_messages' doesn't exist`

**Solutions:**
- ✅ Create the topic in Confluent Cloud console
- ✅ Check spelling (topics are case-sensitive)
- ✅ Wait a few seconds after creating the topic

### Import Errors

**Error:** `ModuleNotFoundError: No module named 'confluent_kafka'`

**Solutions:**
- ✅ Activate virtual environment: `source .venv/bin/activate`
- ✅ Reinstall dependencies: `pip install -r requirements.txt`
- ✅ Check you're using the right Python: `which python`

### Build Errors (macOS)

**Error:** `fatal error: 'librdkafka/rdkafka.h' file not found`

**Solutions:**
- ✅ Install librdkafka: `brew install librdkafka`
- ✅ Or use environment variables:
  ```bash
  C_INCLUDE_PATH=/opt/homebrew/include LIBRARY_PATH=/opt/homebrew/lib pip install confluent-kafka
  ```

### Port Already in Use

**Error:** `Address already in use`

**Solutions:**
- ✅ Check what's using port 5001: `lsof -i :5001`
- ✅ Kill the process or change port in `app.py`

### Consumer Shows "Waiting..." But No Messages

**Solutions:**
- ✅ Verify producer is sending to the same topic (`user_messages`)
- ✅ Check both use the same `config.ini`
- ✅ Look for errors in the producer output
- ✅ Check messages in Confluent Cloud console (Topics → user_messages → Messages)

### Connection Timeout

**Error:** `Failed to connect to broker`

**Solutions:**
- ✅ Check your internet connection
- ✅ Verify bootstrap server address is correct
- ✅ Ensure cluster is "Healthy" in Confluent Cloud
- ✅ Check if firewall is blocking port 9092

## 🎓 Learning Objectives

This application helps you understand:

- ✅ **Producer Pattern** - How to send messages to Kafka topics
- ✅ **Consumer Pattern** - How to read messages from Kafka topics  
- ✅ **Message Flow** - See real-time message delivery
- ✅ **Configuration** - How to configure Kafka clients
- ✅ **Error Handling** - Delivery reports and error management
- ✅ **Consumer Groups** - How consumers work in groups
- ✅ **Security** - SASL/SSL authentication with Confluent Cloud

## 📚 Next Steps

Once you're comfortable with the basics, try:

1. **Add Message Keys** - Modify producer to send keyed messages for partitioning
2. **Multiple Consumers** - Run multiple consumer instances to see consumer groups
3. **JSON Messages** - Send structured data instead of plain text
4. **Error Handling** - Add retry logic and better error handling
5. **Monitoring** - Add logging and metrics
6. **Avro/Protobuf** - Use schema registry for structured data

## 💰 Cost Management

### Free Tier Tips

- ✅ Basic cluster is free tier eligible
- ✅ You get $400 in credits for 30 days
- ✅ Monitor usage in Confluent Cloud → Billing
- ✅ Delete cluster when done learning to save credits

### Deleting Your Cluster

When you're done:
1. Go to Cluster Settings
2. Scroll to bottom
3. Click "Delete cluster"
4. Confirm deletion

**Note:** This deletes all topics and data!

## 🤝 Contributing

This is a learning project! Feel free to:
- Fork and experiment
- Add new features
- Try different message formats
- Share your improvements

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details.

---

## 🆘 Need Help?

- **Confluent Documentation:** https://docs.confluent.io
- **Kafka Documentation:** https://kafka.apache.org/documentation/
- **Confluent Community:** https://forum.confluent.io
- **Python Kafka Client:** https://docs.confluent.io/kafka-clients/python/current/overview.html

---

**Happy Learning! 🎓**

Made with ❤️ for learning Apache Kafka