from flask import Flask, render_template, request, jsonify
from spoiler_main import is_spoiler

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/check-spoiler', methods=['POST'])
def check_spoiler():
    text = request.json.get('text', '')
    prediction = is_spoiler(text)
    
    response = {
        'result': None,
        'class': 'neutral'
    }
    
    if prediction == "Spoiler":
        response['result'] = "⚠️ This text contains spoilers!"
        response['class'] = 'warning'
    elif prediction == "Non-Spoiler":
        response['result'] = "✅ This text is safe - no spoilers detected"
        response['class'] = 'success'
    else:
        response['result'] = "❌ Error in processing"
        response['class'] = 'error'
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5001)