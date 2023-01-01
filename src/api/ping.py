# src/api/ping.py

from flask import Blueprint
from flask_restx import Api, Namespace, Resource

ping_namespace = Namespace("ping")


class Ping(Resource):
    def get(self):
        return {
            "status": "success",
            "message": "pong",
            "project_state": "remaining routes done and tested locally",
        }


ping_namespace.add_resource(Ping, "")
