from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# ---------------- HOME PAGE ----------------
@app.route("/", methods=["GET"])
def home():
    return render_template_string("""
    <h1>Novautics-Gihanda</h1>
    <p>Video Intercom Installation & Remote Gate Access</p>

    <h2>Place an Installation Order</h2>
    <form action="/order" method="post">
        <label>Name:</label><br>
        <input type="text" name="customer" required><br><br>

        <label>Address:</label><br>
        <input type="text" name="address" required><br><br>

        <button type="submit">Place Order</button>
    </form>
    """)


# ---------------- FORM HANDLER ----------------
@app.route("/order", methods=["POST"])
def order_form():
    customer = request.form.get("customer")
    address = request.form.get("address")

    return render_template_string(f"""
    <h2>Order Submitted Successfully</h2>
    <p><strong>Customer:</strong> {customer}</p>
    <p><strong>Address:</strong> {address}</p>
    <p>A Novautics technician will contact you shortly.</p>
    <a href="/">Back</a>
    """)


# ---------------- REST API: CREATE ORDER ----------------
@app.route("/api/orders", methods=["POST"])
def create_order():
    data = request.get_json()
    return jsonify({
        "message": "Installation order created",
        "order": data
    }), 201


# ---------------- REST API: LIST ORDERS ----------------
@app.route("/api/orders", methods=["GET"])
def list_orders():
    return jsonify({
        "orders": []
    }), 200


# ---------------- REST API: OPEN GATE ----------------
@app.route("/api/gate/open", methods=["POST"])
def open_gate():
    return jsonify({
        "action": "open_gate",
        "status": "Command sent to IoT device"
    }), 200


# ---------------- REST API: CLOSE GATE ----------------
@app.route("/api/gate/close", methods=["POST"])
def close_gate():
    return jsonify({
        "action": "close_gate",
        "status": "Command sent to IoT device"
    }), 200


# ---------------- REST API: TELEMETRY ----------------
@app.route("/api/telemetry", methods=["POST"])
def telemetry():
    data = request.get_json()
    return jsonify({
        "message": "Telemetry received",
        "data": data
    }), 200


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
