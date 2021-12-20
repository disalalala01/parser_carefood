import os, sys

sys.path.append(os.getcwd())
import json
from kafka import KafkaProducer
from carefood.config import Config


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(
    bootstrap_servers=[Config.KAFKA_IP], value_serializer=json_serializer
)
