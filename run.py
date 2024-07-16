from model import create_app
from flask import make_response
from flask_cors import CORS

app = create_app()

app.config["JSON_AS_ASCII"] = False


@app.after_request
def after(resp):
    resp = make_response(resp)
    resp.headers["Access-Control-Allow-Origin"] = "*"  # 允许跨域地址
    resp.headers["Access-Control-Allow-Methods"] = "*"  # 请求 ‘*’ 就是全部
    resp.headers["Access-Control-Allow-Headers"] = (
        "x-requested-with,content-type"  # 头部
    )
    resp.headers["Access-Control-Allow-Credentials"] = "True"
    return resp


CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

if __name__ == "__main__":
    app.run(debug=True)
