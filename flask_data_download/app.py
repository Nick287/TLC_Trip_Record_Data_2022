from flask import Flask, send_file, jsonify  
import os
  
app = Flask(__name__)  
  
@app.route('/', methods = ['GET', 'POST'])  
def hello():  
    return 'Flask is running!'  

@app.route('/api/download/<path:filename>', methods=['GET'])  
def download_file(filename):
    base_path = 'TLC Trip Record Data'  
    file_path = os.path.join(base_path, filename)  
      
    if os.path.exists(file_path):  
        return send_file(file_path, as_attachment=True)  
    else:  
        return jsonify({'error': 'file not found'}), 404  
   
if __name__ == '__main__':  
   app.run(debug=True)  