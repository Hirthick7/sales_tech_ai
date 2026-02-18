"""
Technical Knowledge Base for SalesTech Copilot
Contains preloaded FAQs, technical explanations, and keyword mappings
"""

# Technical Knowledge Base - FAQs organized by category
TECHNICAL_FAQS = {
    "architecture": [
        {
            "question": "What is your system architecture?",
            "answer": "We use a modern microservices architecture with cloud-native components.",
            "simple_explanation": "Think of it like LEGO blocks - each piece does one job really well, and they all connect together. This means we can fix or upgrade one part without breaking everything else.",
            "keywords": ["architecture", "system design", "infrastructure", "microservices", "structure"]
        },
        {
            "question": "How does your platform scale?",
            "answer": "Our platform uses horizontal scaling with auto-scaling groups and load balancing.",
            "simple_explanation": "Imagine a restaurant that can instantly add more tables and chefs when it gets busy. We do the same with servers - more users means we automatically add more computing power.",
            "keywords": ["scale", "scaling", "performance", "load", "capacity", "growth"]
        },
        {
            "question": "What's your uptime guarantee?",
            "answer": "We guarantee 99.9% uptime with redundant systems across multiple availability zones.",
            "simple_explanation": "We're available 99.9% of the time - that's less than 9 hours of downtime per year. We have backup systems in different locations, so if one fails, another takes over instantly.",
            "keywords": ["uptime", "availability", "downtime", "reliability", "sla"]
        }
    ],
    "security": [
        {
            "question": "How do you protect our data?",
            "answer": "We use AES-256 encryption at rest and TLS 1.3 in transit, with regular security audits.",
            "simple_explanation": "Your data is locked in a military-grade safe (encryption) both when stored and when moving between systems. We also have security experts regularly check everything.",
            "keywords": ["security", "encryption", "protect", "data protection", "safe", "secure"]
        },
        {
            "question": "Are you compliant with regulations?",
            "answer": "Yes, we're SOC 2 Type II certified and GDPR compliant with annual audits.",
            "simple_explanation": "We follow strict international rules for handling data (like GDPR in Europe). Independent auditors verify this every year - it's like having a health inspector for data security.",
            "keywords": ["compliance", "gdpr", "soc2", "regulations", "audit", "certified"]
        },
        {
            "question": "How do you handle authentication?",
            "answer": "We support SSO, OAuth 2.0, SAML, and multi-factor authentication.",
            "simple_explanation": "You can log in using your existing company credentials (like Google or Microsoft), and we support extra security layers like phone codes to make sure it's really you.",
            "keywords": ["authentication", "login", "sso", "oauth", "saml", "mfa", "access"]
        }
    ],
    "integration": [
        {
            "question": "What integrations do you support?",
            "answer": "We offer REST APIs, webhooks, and pre-built connectors for Salesforce, HubSpot, and Slack.",
            "simple_explanation": "We connect easily with tools you already use. It's like having universal adapters - we can plug into Salesforce, HubSpot, Slack, and many others without custom coding.",
            "keywords": ["integration", "api", "connect", "salesforce", "hubspot", "slack", "webhook"]
        },
        {
            "question": "How long does implementation take?",
            "answer": "Typical implementation is 2-4 weeks with dedicated onboarding support.",
            "simple_explanation": "Most customers are up and running in 2-4 weeks. We assign you a dedicated expert who guides you through setup, training, and going live.",
            "keywords": ["implementation", "setup", "onboarding", "timeline", "deployment", "install"]
        },
        {
            "question": "Do you have an API?",
            "answer": "Yes, we provide a comprehensive REST API with detailed documentation and SDKs.",
            "simple_explanation": "Yes! Our API is like a menu of services your developers can use. We provide clear instructions and ready-made code libraries to make it easy.",
            "keywords": ["api", "rest", "sdk", "developer", "documentation"]
        }
    ],
    "pricing": [
        {
            "question": "What's your pricing model?",
            "answer": "We offer tiered subscription pricing based on users and features, with annual discounts.",
            "simple_explanation": "You pay monthly based on how many people use it and which features you need. It's like Netflix - different plans for different needs. Pay yearly and save 20%.",
            "keywords": ["pricing", "cost", "price", "subscription", "payment", "budget"]
        },
        {
            "question": "Is there a free trial?",
            "answer": "Yes, we offer a 14-day free trial with full feature access and no credit card required.",
            "simple_explanation": "Try everything free for 14 days - no credit card needed. It's a risk-free way to see if we're the right fit for your team.",
            "keywords": ["trial", "free", "demo", "test", "try"]
        }
    ],
    "support": [
        {
            "question": "What support do you provide?",
            "answer": "24/7 support via chat, email, and phone, with dedicated account managers for enterprise.",
            "simple_explanation": "We're here whenever you need us - day or night. Chat, email, or call us. Enterprise customers get a dedicated person who knows your account inside out.",
            "keywords": ["support", "help", "customer service", "assistance", "contact"]
        },
        {
            "question": "Do you provide training?",
            "answer": "Yes, we offer live training sessions, video tutorials, and comprehensive documentation.",
            "simple_explanation": "We'll teach your team everything they need. Live sessions with our experts, video tutorials you can watch anytime, and detailed guides.",
            "keywords": ["training", "learning", "education", "tutorial", "documentation"]
        }
    ]
}

# Keyword to category mapping for quick lookup
KEYWORD_CATEGORIES = {
    "architecture": ["architecture", "system", "infrastructure", "microservices", "design", "structure"],
    "security": ["security", "encryption", "protect", "safe", "secure", "compliance", "gdpr", "soc2", "authentication", "login"],
    "integration": ["integration", "api", "connect", "salesforce", "hubspot", "slack", "webhook", "implementation", "setup"],
    "pricing": ["pricing", "cost", "price", "subscription", "payment", "budget", "trial", "free", "demo"],
    "support": ["support", "help", "customer service", "assistance", "training", "learning", "documentation"]
}

def get_all_faqs():
    """Return all FAQs organized by category"""
    return TECHNICAL_FAQS

def search_knowledge_base(query):
    """
    Search the knowledge base for relevant answers based on query
    Returns the best matching FAQ with confidence score
    """
    query_lower = query.lower()
    words = query_lower.split()
    
    best_match = None
    best_score = 0
    
    # Search through all categories and FAQs
    for category, faqs in TECHNICAL_FAQS.items():
        for faq in faqs:
            score = 0
            # Check keyword matches
            for keyword in faq["keywords"]:
                if keyword in query_lower:
                    score += 2
            
            # Check word matches
            for word in words:
                if len(word) > 3:  # Only check meaningful words
                    if word in faq["question"].lower():
                        score += 1
                    if word in faq["answer"].lower():
                        score += 1
            
            if score > best_score:
                best_score = score
                best_match = {
                    "category": category,
                    "question": faq["question"],
                    "answer": faq["answer"],
                    "explanation": faq["simple_explanation"],
                    "score": score
                }
    
    # Determine confidence level based on score
    if best_match:
        if best_score >= 4:
            confidence = "High"
        elif best_score >= 2:
            confidence = "Medium"
        else:
            confidence = "Low"
        
        best_match["confidence"] = confidence
        return best_match
    
    # No match found - return a helpful default response
    return {
        "category": "general",
        "question": "General inquiry",
        "answer": "I'd be happy to help with that. Could you provide more specific details about what you're looking for?",
        "explanation": "This seems like a unique question. Let me connect you with our technical team who can give you a detailed answer tailored to your needs.",
        "confidence": "Low",
        "score": 0
    }
