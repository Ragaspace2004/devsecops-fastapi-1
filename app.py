from flask import Flask, request, jsonify

app = Flask(__name__)

# SECURITY ISSUE: Hardcoded secret (will be caught by Gitleaks)


@app.route("/api/users", methods=["GET"])
def get_users():
    # SECURITY ISSUE: SQL Injection vulnerability (will be caught by Bandit)
    # user_id = request.args.get("id")

    # FORMATTING ISSUE: Inconsistent spacing (will be caught by Black)
    users = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]

    return jsonify(users)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    # SECURITY ISSUE: Debug mode in production (will be caught by Bandit)
    app.run(debug=False)
