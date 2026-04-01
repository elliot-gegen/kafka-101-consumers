#!/usr/bin/env python
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Producer
import sys

def delivery_report(err, msg):
    """
    Callback function called once for each message produced to indicate delivery result.
    Triggered by poll() or flush().
    """
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def create_producer(config_file):
    """Create and return a Kafka producer instance."""
    # Parse the configuration
    config_parser = ConfigParser()
    config_parser.read_file(config_file)
    config = dict(config_parser['default'])
    
    # Create Producer instance
    producer = Producer(config)
    return producer

def produce_message(producer, topic, key, value):
    """Produce a message to Kafka topic."""
    try:
        # Produce message
        producer.produce(
            topic,
            key=key,
            value=value,
            callback=delivery_report
        )
        # Wait for any outstanding messages to be delivered and delivery reports received
        producer.flush()
        return True
    except Exception as e:
        print(f"Error producing message: {e}")
        return False

if __name__ == '__main__':
    # Parse the command line
    parser = ArgumentParser()
    parser.add_argument('config_file', type=FileType('r'), help='Path to configuration file')
    parser.add_argument('-t', '--topic', default='user_messages', help='Kafka topic name (default: user_messages)')
    parser.add_argument('-k', '--key', help='Message key (optional)')
    parser.add_argument('-m', '--message', help='Message to send')
    args = parser.parse_args()

    # Create producer
    producer = create_producer(args.config_file)
    
    if args.message:
        # Send single message from command line
        key = args.key.encode('utf-8') if args.key else None
        value = args.message.encode('utf-8')
        produce_message(producer, args.topic, key, value)
    else:
        # Interactive mode - read messages from stdin
        print(f"Kafka Producer started. Type messages to send to topic '{args.topic}'.")
        print("Press Ctrl+C to exit.\n")
        
        try:
            while True:
                message = input("Enter message: ")
                if message.strip():
                    key = None
                    value = message.encode('utf-8')
                    produce_message(producer, args.topic, key, value)
        except KeyboardInterrupt:
            print("\nShutting down producer...")
        finally:
            producer.flush()

# Made with Bob
