from flask import Flask, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['POST'])
def json_input():
    req_data = request.get_json()

    test = req_data['DataReveived']

    return test

app.run()