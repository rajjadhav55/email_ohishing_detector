from flask import Flask, request, render_template
from email_analyzer import predict_email
from website_scanner import scan_website

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email_text = request.form.get("email")
        url = request.form.get("url")
        
        if email_text:
            result = predict_email(email_text)
            return f"Email Result: {result}"
        elif url:
            result = scan_website(url)
            return f"Website Result: {result}"
    
    return render_template("index.html")  # Basic HTML form

if __name__ == "__main__":
    app.run(debug=True)