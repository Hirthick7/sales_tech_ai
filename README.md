# SalesTech Copilot

A real-time AI assistant that helps salespeople answer technical customer questions during live sales calls with instant, simple, and accurate responses.

## 🎯 Overview

SalesTech Copilot empowers non-technical sales teams to confidently handle technical questions about security, integrations, architecture, and more during live customer conversations. No more saying "I'll get back to you" and losing deal momentum.

## ✨ Features

- **Live Call Assistant**: Real-time conversation analysis with instant answers
- **Confidence Indicators**: Know how reliable each answer is (High/Medium/Low)
- **Simple Explanations**: Technical answers translated into sales-friendly language
- **Knowledge Base**: Comprehensive technical FAQs organized by category
- **Search & Filter**: Quickly find answers by keyword or category
- **Beautiful UI**: Modern SaaS design with 3D animations and smooth interactions

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd "c:/Users/mhirt/OneDrive/Documents/vs code/sales"
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser**:
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
sales/
├── app.py                      # Flask application & API endpoints
├── knowledge_base.py           # Technical knowledge database
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── templates/
│   ├── base.html              # Base template with navigation
│   ├── index.html             # Home page
│   ├── assistant.html         # Live Call Assistant
│   ├── knowledge.html         # Product Knowledge Base
│   └── about.html             # Why This Matters page
└── static/
    ├── css/
    │   └── style.css          # All styling & animations
    └── js/
        └── main.js            # JavaScript interactions
```

## 🔌 API Endpoints

### POST `/api/analyze`
Analyze customer conversation and return AI-powered response.

**Request Body**:
```json
{
  "conversation": "How does your platform handle data encryption?"
}
```

**Response**:
```json
{
  "success": true,
  "answer": "We use AES-256 encryption at rest and TLS 1.3 in transit...",
  "explanation": "Your data is locked in a military-grade safe...",
  "confidence": "High",
  "category": "Security",
  "original_question": "How do you protect our data?"
}
```

### GET `/api/knowledge`
Get all technical knowledge FAQs organized by category.

**Response**:
```json
{
  "success": true,
  "faqs": {
    "architecture": [...],
    "security": [...],
    "integration": [...],
    "pricing": [...],
    "support": [...]
  }
}
```

### GET `/api/health`
Health check endpoint.

**Response**:
```json
{
  "status": "healthy",
  "service": "SalesTech Copilot API",
  "version": "1.0.0"
}
```

## 💡 How It Works

1. **Customer asks a technical question** during your sales call
2. **Type the question** into the Live Call Assistant
3. **AI analyzes** the question using keyword detection and knowledge base matching
4. **Get instant answer** with:
   - Sales-friendly technical answer
   - Simple explanation/analogy
   - Confidence score (High/Medium/Low)
   - Related category

## 🎨 Design Features

- **Professional SaaS Design**: Clean, modern interface
- **3D Animations**: CSS-based 3D effects on cards and buttons
- **Smooth Interactions**: Hover effects, transitions, and animations
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Color Palette**: 
  - Primary: Indigo (#4F46E5)
  - Secondary: Purple (#7C3AED)
  - Accent: Cyan (#06B6D4)

## 📚 Knowledge Base Categories

- **Architecture**: System design, scalability, uptime
- **Security**: Encryption, compliance, authentication
- **Integration**: APIs, connectors, implementation
- **Pricing**: Subscription models, trials, discounts
- **Support**: Customer service, training, documentation

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **Styling**: Custom CSS with 3D transforms and animations
- **API**: RESTful JSON API

## 📝 Usage Examples

### Example 1: Security Question
**Input**: "What security measures do you have in place?"

**Output**:
- **Answer**: "We use AES-256 encryption at rest and TLS 1.3 in transit, with regular security audits."
- **Explanation**: "Your data is locked in a military-grade safe (encryption) both when stored and when moving between systems."
- **Confidence**: High

### Example 2: Integration Question
**Input**: "Can you integrate with Salesforce?"

**Output**:
- **Answer**: "Yes, we offer REST APIs, webhooks, and pre-built connectors for Salesforce, HubSpot, and Slack."
- **Explanation**: "We connect easily with tools you already use. It's like having universal adapters."
- **Confidence**: High

## 🎯 Benefits

- **Increase Win Rates**: Close more deals by answering questions confidently
- **Faster Sales Cycles**: Eliminate delays from "I'll get back to you"
- **Empower Non-Technical Reps**: Give everyone expert-level knowledge
- **Consistent Messaging**: Ensure accurate answers every time

## 🔧 Customization

### Adding New FAQs

Edit `knowledge_base.py` and add new entries to the `TECHNICAL_FAQS` dictionary:

```python
{
    "question": "Your question here",
    "answer": "Technical answer",
    "simple_explanation": "Sales-friendly explanation",
    "keywords": ["keyword1", "keyword2", "keyword3"]
}
```

### Changing Colors

Edit `static/css/style.css` and modify the CSS variables in `:root`:

```css
:root {
    --primary: #4F46E5;
    --secondary: #7C3AED;
    /* ... */
}
```

## 📄 License

This project is provided as-is for demonstration purposes.

## 🤝 Support

For questions or issues, please contact the development team.

---

**Built with ❤️ for sales teams who deserve better tools**
