# Feet & Inches to Inches Converter

A simple web app that converts feet and inches measurements to total inches.

## Quick Start

1. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install and run:
```bash
pip install -r requirements.txt
python app.py
```

3. Open `http://localhost:5000` in your browser

## How to Use

1. Enter feet and inches
2. Click "Convert"
3. See the total inches result

## Tech Stack

- Python/Flask
- Tailwind CSS
- HTML/JavaScript

## Features

- Convert feet and inches to total inches
- Modern, responsive UI built with Tailwind CSS
- Real-time input validation
- Clear error handling
- Mobile-friendly design
- Smooth animations and transitions
- No JavaScript dependencies (except Tailwind)

## Development

The application structure is organized as follows:
- `app.py` - Main Flask application and routes
- `templates/index.html` - Frontend template with Tailwind CSS styling
- `requirements.txt` - Python dependencies

## Error Handling

The application includes validation for:
- Non-numeric inputs
- Negative numbers
- Inches greater than 11
- Empty fields

## Browser Support

Works in all modern browsers including:
- Chrome
- Firefox
- Safari
- Edge 