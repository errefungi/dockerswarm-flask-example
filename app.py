from flask import Flask, request, render_template_string
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        message = request.form.get('msg', 'Hello from the worker node!')
        print(message, file=sys.stderr)
        return message
    else:
        with open("form.html", "r") as f:
            form_html = f.read()
        return render_template_string(form_html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

