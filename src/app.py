"""A flask app for the blabber api."""

from time import time
from uuid import uuid4

from flask import Flask, abort, jsonify, request

APP = Flask(__name__)

BLABS = {}


@APP.route("/api/blabs", methods=["GET"])
def get_blabs():
    """Get all blabs created since the specified timestamp."""
    since = int(request.args.get("createdSince", 0))

    return jsonify([blab for blab in BLABS.values() if blab["postTime"] >= since])


@APP.route("/api/blabs", methods=["POST"])
def post_blabs():
    """Add a new blab."""
    blab = request.json

    blab_id = uuid4()
    BLABS[blab_id] = blab

    blab["id"] = blab_id
    blab["postTime"] = int(time())

    return jsonify(status=201, result=blab)


@APP.route("/api/blabs/<id>", methods=["DELETE"])
def delete_blabs(blab_id):
    """Remove a blab with the given id."""
    try:
        del BLABS[blab_id]
    except KeyError:
        abort(404)
