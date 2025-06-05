from flask import Flask, request, jsonify
from routine_logic import calculate_h5_score

app = Flask(__name__)

@app.route("/score", methods=["POST"])
def score_routine():
    data = request.get_json()
    routine = data.get("elements", [])

    try:
        result = calculate_h5_score(routine)
        return jsonify(result)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
