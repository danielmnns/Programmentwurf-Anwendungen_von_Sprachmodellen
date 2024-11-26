from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Frontend-HTML

@app.route('/api/process', methods=['POST'])
def process():
    data = request.json
    result = {"output": data["input"] + " processed by Python"}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
