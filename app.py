"""
SalesTech Copilot - Flask Backend
Real-time AI assistant for sales teams
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from knowledge_base import search_knowledge_base, get_all_faqs
import re

app = Flask(__name__)
CORS(app)

# Configure Flask
app.config['SECRET_KEY'] = 'salestech-copilot-secret-key-2024'

# ==================== Routes ====================

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/assistant')
def assistant():
    """Live Call Assistant page"""
    return render_template('assistant.html')

@app.route('/knowledge')
def knowledge():
    """Product Knowledge page"""
    faqs = get_all_faqs()
    return render_template('knowledge.html', faqs=faqs)

@app.route('/about')
def about():
    """About / Why This Matters page"""
    return render_template('about.html')

# ==================== API Endpoints ====================

@app.route('/api/analyze', methods=['POST'])
def analyze_conversation():
    """
    Analyze customer conversation and return AI-powered response
    
    Expected JSON input:
    {
        "conversation": "customer question or statement"
    }
    
    Returns:
    {
        "success": true,
        "answer": "sales-friendly answer",
        "explanation": "simple explanation/analogy",
        "confidence": "High/Medium/Low",
        "category": "topic category",
        "original_question": "detected question"
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'conversation' not in data:
            return jsonify({
                "success": False,
                "error": "No conversation text provided"
            }), 400
        
        conversation = data['conversation'].strip()
        
        if not conversation:
            return jsonify({
                "success": False,
                "error": "Conversation text is empty"
            }), 400
        
        # Use knowledge base to find best answer
        result = search_knowledge_base(conversation)
        
        # Format response
        response = {
            "success": True,
            "answer": result["answer"],
            "explanation": result["explanation"],
            "confidence": result["confidence"],
            "category": result["category"].title(),
            "original_question": result["question"]
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"An error occurred: {str(e)}"
        }), 500

@app.route('/api/knowledge', methods=['GET'])
def get_knowledge():
    """
    Get all technical knowledge FAQs
    
    Returns:
    {
        "success": true,
        "faqs": {
            "category1": [...],
            "category2": [...]
        }
    }
    """
    try:
        faqs = get_all_faqs()
        return jsonify({
            "success": True,
            "faqs": faqs
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"An error occurred: {str(e)}"
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "SalesTech Copilot API",
        "version": "1.0.0"
    })

# ==================== Error Handlers ====================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        "success": False,
        "error": "Internal server error"
    }), 500

# ==================== Main ====================

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 SalesTech Copilot - Starting Server")
    print("=" * 60)
    print("📍 Server running at: http://localhost:5000")
    print("📚 API Endpoints:")
    print("   - POST /api/analyze - Analyze conversation")
    print("   - GET  /api/knowledge - Get all FAQs")
    print("   - GET  /api/health - Health check")
    print("=" * 60)
    print("Press CTRL+C to stop the server")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
