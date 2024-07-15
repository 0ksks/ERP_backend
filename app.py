from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/api/abc", methods=["GET"])
def get_some_endpoint():
    return jsonify({"message": "GET request received"})


@app.route("/supplier/create", methods=["POST"])
def post_some_endpoint():
    data = request.get_json()
    return jsonify({"message": "POST request received", "data": data})


if __name__ == "__main__":
    app.run(debug=True)
