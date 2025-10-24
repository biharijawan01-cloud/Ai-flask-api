from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)

# Initialize CORS to allow requests from any origin (Crucial fix for App Inventor)
CORS(app) 

@app.route('/', methods=['GET'])
def home():
    # Health check to ensure the server is running
    return jsonify({"message": "API is running! Use POST /ask.", "status": "online"}), 200

@app.route('/ask', methods=['POST'])
def handle_request():
    try:
        # Get the JSON payload
        data = request.get_json(silent=True) 
        
        # This check should now pass thanks to CORS
        if data is None:
            return jsonify({"error": "Failed to receive valid JSON payload"}), 400
        
        # Check for the 'question' key sent by App Inventor
        question = data.get('question') 
        
        if not question:
            return jsonify({"error": "Missing 'question' field"}), 400

        # --- Your AI Processing Logic Goes Here ---
        
        # Simple placeholder response
        ai_response = f"SUCCESS! Your question received on the stable server: '{question}'"
        
        # Return the successful response
        return jsonify({
            "answer": ai_response,
            "status": "success"
        }), 200

    except Exception as e:
        # Log and return internal server error
        print(f"Internal Server Error: {e}")
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500

if __name__ == '__main__':
    # Flask runs on port 5000 in many cloud environments
    app.run(host='0.0.0.0', port=5000)
  
