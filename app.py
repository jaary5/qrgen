from flask import Flask, render_template, request, send_file, abort
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
            try:
                # Generate QR code
                img = qrcode.make(url)
                img_path = os.path.join('static', 'images', 'qrcode.png')
                img.save(img_path)

                return render_template("result.html", img_path='images/qrcode.png')
            except Exception as e:
                print(f"Error generating QR code: {e}")
                abort(500)  # Internal Server Error

    return render_template("index.html")

@app.route("/download")
def download():
    path = os.path.join('static', 'images', 'qrcode.png')
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    else:
        abort(404)  # File not found

if __name__ == "__main__":
    app.run(debug=True)
