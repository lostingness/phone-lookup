from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

@app.route("/lookup", methods=["POST"])
def lookup():
    number = request.json.get("number")

    session = requests.Session()
    login_url = "https://lottery811.cyou/login.php"
    login_data = {
        "email": "safexera@gmail.com",
        "password": "Ram@883215"
    }
    session.post(login_url, data=login_data)

    lookup_url = "https://lottery811.cyou/phone-number-info.php"
    lookup_data = {"mobile": number}
    response = session.post(lookup_url, data=lookup_data)

    soup = BeautifulSoup(response.text, "html.parser")
    result_box = soup.find("textarea", {"id": "copyText"})

    if result_box:
        result = result_box.text.strip()
        return jsonify({"status": "success", "result": result})
    else:
        return jsonify({"status": "fail", "result": "No data found or session error"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
