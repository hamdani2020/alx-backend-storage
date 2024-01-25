#!/usr/bin/env python3
"""Module for task 12"""
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    """Returns Nginx logs"""
    print("{} logs".format(nginx_collection.count_documents({})))
    print("Methods")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        request_count = len(list(nginx_collection.find({"method": method})))
        print("\tmethod {}: {}".format(method, request_count))
    status = len(list(
        nginx_collection.find({"method: "GET", "path": "/status"})))
    print("{} status check".format(status))


def run():
    """Provides some status"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    print_nginx_request_logs(client.logs.nginx)


if __name__ == "__main__":
    run()

