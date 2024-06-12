from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ultrasonic', methods=['POST'])
def ultrasonic():
    if request.is_json:
        data = request.get_json()
        distance = data.get('distance', None)
        if distance is not None:
            print(f"Received distance: {distance} cm")
            return jsonify({"status": "success", "distance": distance}), 200
        else:
            return jsonify({"status": "fail", "message": "No distance provided"}), 400
    else:
        return jsonify({"status": "fail", "message": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True )
