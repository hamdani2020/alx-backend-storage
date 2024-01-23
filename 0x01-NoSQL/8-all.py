#!/usr/bin/env python3
"""The function lists all documents in a collection"""


def list_all(mongo_collection):
    """List all documents"""
    return [doc for doc in mongo_collection.find()]
