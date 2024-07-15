from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/api/abc", methods=["GET"])
def get_some_endpoint():
    return jsonify({"message": "GET request received"})


@app.route("/api/supplier/create_success", methods=["POST"])
def post_some_endpoint():
    return jsonify(
        {"code": 1, "message": "success", "data": {"supplierID": "supplierID_value"}}
    )

if __name__ == "__main__":
    app.run(debug=True)
