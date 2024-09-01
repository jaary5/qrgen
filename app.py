from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)

# Ensure the 'images' directory exists
os.makedirs(os.path.join('static', 'images'), exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            # Generate QR code
            img = qrcode.make(url)
            img_path = os.path.join('images', 'qrcode.png')  # Update the relative path
            img.save(os.path.join('static', img_path))

            return render_template("result.html", img_path=img_path)

    return render_template("index.html")


@app.route("/download")
def download():
    path = os.path.join('static', 'images', 'qrcode.png')
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
