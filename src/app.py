"""A flask app for the blabber api."""

from time import time

from bson.objectid import ObjectId
from flask import Flask, abort, jsonify, request
from pymongo import MongoClient

APP = Flask(__name__)

MONGO_CLIENT = MongoClient("mongo")
BLABS = MONGO_CLIENT.blabber.blabs


@APP.route("/api/blabs", methods=["GET"])
def get_blabs():
    """Get all blabs created since the specified timestamp."""
    since = int(request.args.get("createdSince", 0))

    blabs = list(BLABS.find({"postTime": {"$gte": since}}))

    for blab in blabs:
        blab["id"] = str(blab.pop("_id"))

    return jsonify(blabs)


@APP.route("/api/blabs", methods=["POST"])
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
