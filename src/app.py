#!/usr/bin/env python
from flask import Flask, render_template, request, jsonify
from configparser import ConfigParser
from confluent_kafka import Producer
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Set template folder to be one level up from src/
template_dir = os.path.join(script_dir, '..', 'templates')

app = Flask(__name__, template_folder=template_dir)

# Global producer instance
producer = None
topic = 'user_messages'

def delivery_report(err, msg):
    """Callback for message delivery reports."""
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def init_producer():
    """Initialize Kafka producer with config from config.ini"""
    global producer
    
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Build path to config file (one level up, then into config directory)
    config_path = os.path.join(script_dir, '..', 'config', 'config.ini')
    
    config_parser = ConfigParser()
    config_parser.read(config_path)
    config = dict(config_parser['default'])
    
    producer = Producer(config)
    print("Kafka producer initialized successfully")

@app.route('/')
def index():
    """Render the main page with message input form."""
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    """Handle message submission and send to Kafka."""
    try:
        data = request.get_json()
        message = data.get('message', '').strip()
        
        if not message:
            return jsonify({'success': False, 'error': 'Message cannot be empty'}), 400
        
        # Produce message to Kafka
        producer.produce(
            topic,
            key=None,
            value=message.encode('utf-8'),
            callback=delivery_report
        )
        
        # Trigger delivery reports
        producer.poll(0)
        
        return jsonify({
            'success': True,
            'message': 'Message sent to Kafka successfully',
            'topic': topic
        })
        
    except Exception as e:
        print(f"Error sending message: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({'status': 'healthy', 'producer': 'connected' if producer else 'not initialized'})

if __name__ == '__main__':
    # Initialize producer on startup
    init_producer()
    
    # Run Flask app
    print("Starting Flask web application...")
    print("Open http://localhost:5001 in your browser")
    app.run(debug=True, host='0.0.0.0', port=5001)

# Made with Bob
