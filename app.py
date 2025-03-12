from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        feet = int(request.form.get('feet', 0))
        inches = int(request.form.get('inches', 0))
        
        if feet < 0 or inches < 0:
            return jsonify({'success': False, 'message': 'Please enter positive numbers only.'})
        
        if inches >= 12:
            return jsonify({'success': False, 'message': 'Inches should be less than 12.'})
        
        total_inches = (feet * 12) + inches
        message = f'{feet} feet and {inches} inches = {total_inches} inches'
        
        return jsonify({'success': True, 'message': message, 'total_inches': total_inches})
    except ValueError:
        return jsonify({'success': False, 'message': 'Please enter valid numbers.'})

# Remove the if __name__ == '__main__' block for Vercel deployment 