from flask import Flask, request
from html import escape
app = Flask(__name__)

@app.route("/hello")
def hello():
    name = request.args.get('name')
    name = escape(name)
    content = """
    <html>
        <head><title>Hello Website</title></head>
        <body>
            Hello {}
            <script>webgoat.customjs.phoneHome()</script>
            <script>alert.("XSS")</script>
        </body>
    </html>
    """.format(name)
    return content

if __name__ == "__main__":
    app.run()
