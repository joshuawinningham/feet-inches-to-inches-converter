from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        feet = int(request.form.get('feet', 0))
        inches = int(request.form.get('inches', 0))
        
        # Convert to total inches
        total_inches = (feet * 12) + inches
        
        # Create visualization data
        # Each foot will be represented as a full block
        # Remaining inches will be represented as partial blocks
        full_feet = total_inches // 12
        remaining_inches = total_inches % 12
        
        return jsonify({
            'success': True,
            'total_inches': total_inches,
            'message': f'{feet} feet and {inches} inches is equal to {total_inches} inches',
            'visualization': {
                'feet': full_feet,
                'inches': remaining_inches
            }
        })
    except ValueError:
        return jsonify({
            'success': False,
            'message': 'Please enter valid numbers'
        }), 400

if __name__ == '__main__':
    app.run(debug=True) 