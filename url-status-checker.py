from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

template = """
<!DOCTYPE html>
<html>
<head>
    <title>URL Status Checker</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-fork-ribbon-css/0.2.3/gh-fork-ribbon.min.css" />
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            text-align: center;
            background-color: #6e6e80;
        }
        .container {
            max-width: 400px;
            margin: 0 auto;
        }
        .form-group {
            margin-bottom: 10px;
        }
        .btn {
            background-color: #2EA44F;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .result {
            padding: 10px;
            margin-top: 20px;
            border-radius: 4px;
        }
        .result.success {
            background-color: #2EA44F;
            color: white;
        }
        .result.error {
            background-color: #CB2431;
            color: white;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>URL Status Checker</h1>
        <form method="post">
            <div class="form-group">
                <input type="text" name="url" placeholder="Enter URL to check" required>
            </div>
            <button class="btn" type="submit">Check</button>
        </form>
        {% if result %}
        <div class="result {{ result.status }}">
            {{ result.message }}
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def url_status_checker():
    result = None

    if request.method == "POST":
        url = request.form["url"]
        try:
            response = requests.get(url)
            if response.status_code == 200:
                result = {"status": "success", "message": "URL is reachable."}
            else:
                result = {"status": "error", "message": f"Failed to access URL. Status code: {response.status_code}"}
