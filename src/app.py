"""A flask app for the blabber api."""

from time import time
from os import environ

from bson.objectid import ObjectId
from flask import Flask, abort, jsonify, request
from pymongo import MongoClient
from prometheus_flask_exporter import PrometheusMetrics

APP = Flask(__name__)

MONGO_CLIENT = MongoClient(_env_config("MONGO_URL_FILE", "mongo"))
BLABS = MONGO_CLIENT.blabber.blabs

METRICS = PrometheusMetrics(APP)


def _env_config(var: str, default: str) -> str:
    if filename := environ.get(var):
        with open(filename) as file:
            return file.read()
    return default


@APP.route("/api/blabs", methods=["GET"])
def get_blabs():
    """Get all blabs created since the specified timestamp."""
    since = int(request.args.get("createdSince", 0))

    blabs = list(BLABS.find({"postTime": {"$gte": since}}))

    for blab in blabs:
        blab["id"] = str(blab.pop("_id"))

    return jsonify(blabs)


@APP.route("/api/blabs", methods=["POST"])
@METRICS.counter("blabber_blabs", "Number of blabs created")
def post_blabs():
    """Add a new blab."""
    blab = request.json
    blab["postTime"] = int(time())

    BLABS.insert_one(blab)

    blab["id"] = str(blab.pop("_id"))

    return jsonify(status=201, result=blab)


@APP.route("/api/blabs/<id>", methods=["DELETE"])
def delete_blabs(blab_id):
    """Remove a blab with the given id."""
    query = {"_id": ObjectId(blab_id)}
    if BLABS.delete_one(query).deleted_count != 1:
        abort(404)
