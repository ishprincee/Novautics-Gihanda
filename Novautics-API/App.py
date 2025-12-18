from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "company": "Novautics-Gihanda",
        "description": "Cloud platform for video intercom installation and remote gate access using IoT."
    })

@app.route("/api/orders", methods=["POST"])
def create_order():
    data = request.json
    return jsonify({
        "message": "Installation order received",
        "customer": data
    }), 201

@app.route("/api/orders", methods=["GET"])
def get_orders():
    return jsonify({
        "orders": []
    })

@app.route("/api/gate/open", methods=["POST"])
def open_gate():
    return jsonify({"status": "Gate open command sent"}), 200

@app.route("/api/gate/close", methods=["POST"])
def close_gate():
    return jsonify({"status": "Gate close command sent"}), 200

@app.route("/api/telemetry", methods=["POST"])
def telemetry():
    data = request.json
    return jsonify({
        "status": "Telemetry received",
        "data": data
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
