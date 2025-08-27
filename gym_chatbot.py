from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import json
from typing import Dict, List

# Import your existing GymChatbot class
class GymChatbot:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
        self.gym_context = """
        You are a helpful gym assistant chatbot. You provide information about:
        - Workout routines and exercises
        - Gym equipment usage and safety
        - Nutrition and diet advice
        - Membership plans and gym services
        - Class schedules and programs
        - Fitness goals and training plans
        - Injury prevention and recovery
        - Gym etiquette and rules
        
        Always be encouraging, professional, and safety-focused in your responses.
        If asked about medical conditions, always recommend consulting healthcare professionals.
        """
        
        self.gym_data = {
            "membership_plans": {
                "basic": {"price": "$29.99/month", "benefits": ["Access to cardio and strength equipment", "Locker room access"]},
                "premium": {"price": "$49.99/month", "benefits": ["All basic benefits", "Group classes", "Personal training session"]},
                "elite": {"price": "$79.99/month", "benefits": ["All premium benefits", "24/7 access", "Nutrition consultation"]}
            },
            "class_schedule": {
                "monday": ["Yoga 9AM", "HIIT 6PM", "Strength Training 7PM"],
                "tuesday": ["Pilates 8AM", "Cardio Blast 5:30PM", "Zumba 7PM"],
                "wednesday": ["CrossFit 7AM", "Yoga 12PM", "Boxing 6PM"],
                "thursday": ["Strength Training 9AM", "Dance Fitness 6PM"],
                "friday": ["HIIT 8AM", "Yoga 5PM", "Weekend Warrior 7PM"],
                "saturday": ["Bootcamp 9AM", "Pilates 11AM", "Open Gym 2PM"],
                "sunday": ["Yoga Flow 10AM", "Recovery Session 4PM"]
            },
            "gym_hours": {
                "weekdays": "5:00 AM - 11:00 PM",
                "weekends": "6:00 AM - 10:00 PM"
            },
            "equipment": [
                "Treadmills", "Elliptical machines", "Stationary bikes", "Rowing machines",
                "Free weights", "Cable machines", "Smith machines", "Squat racks",
                "Bench press", "Dumbbells", "Resistance bands", "Medicine balls"
            ]
        }
        
        self.chat_history = []
    
    def format_gym_info(self, query: str) -> str:
        query_lower = query.lower()
        formatted_info = ""
        
        if any(word in query_lower for word in ["membership", "plan", "price", "cost"]):
            formatted_info += "\n**MEMBERSHIP PLANS:**\n"
            for plan, details in self.gym_data["membership_plans"].items():
                formatted_info += f"• {plan.title()}: {details['price']}\n"
                for benefit in details["benefits"]:
                    formatted_info += f"  - {benefit}\n"
        
        if any(word in query_lower for word in ["schedule", "class", "time", "when"]):
            formatted_info += "\n**CLASS SCHEDULE:**\n"
            for day, classes in self.gym_data["class_schedule"].items():
                formatted_info += f"• {day.title()}: {', '.join(classes)}\n"
        
        if any(word in query_lower for word in ["hours", "open", "close", "time"]):
            formatted_info += f"\n**GYM HOURS:**\n"
            formatted_info += f"• Weekdays: {self.gym_data['gym_hours']['weekdays']}\n"
            formatted_info += f"• Weekends: {self.gym_data['gym_hours']['weekends']}\n"
        
        if any(word in query_lower for word in ["equipment", "machine", "weights"]):
            formatted_info += f"\n**AVAILABLE EQUIPMENT:**\n"
            formatted_info += "• " + "\n• ".join(self.gym_data["equipment"])
        
        return formatted_info
    
    def get_response(self, user_message: str) -> str:
        try:
            gym_info = self.format_gym_info(user_message)
            
            full_prompt = f"""
            {self.gym_context}
            
            Gym Information Available:
            {gym_info}
            
            Chat History:
            {self.format_chat_history()}
            
            User Question: {user_message}
            
            Please provide a helpful, accurate response about gym-related topics.
            Use the gym information provided above when relevant.
            """
            
            response = self.model.generate_content(full_prompt)
            
            self.chat_history.append({
                "user": user_message,
                "bot": response.text
            })
            
            return response.text
            
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"
    
    def format_chat_history(self, last_n: int = 3) -> str:
        if not self.chat_history:
            return "No previous conversation."
        
        history_text = ""
        recent_history = self.chat_history[-last_n:]
        
        for exchange in recent_history:
            history_text += f"User: {exchange['user']}\n"
            history_text += f"Bot: {exchange['bot']}\n\n"
        
        return history_text
    
    def clear_history(self):
        self.chat_history = []

# Flask App Setup
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize the chatbot with your API key
API_KEY = "AIzaSyDfuo1TijR4tnunaRQfTClnlwNHHNB0t9U"  # Your API key from the original code
chatbot = GymChatbot(API_KEY)

@app.route('/')
def home():
    return jsonify({
        "message": "Gym Chatbot API is running!",
        "endpoints": [
            "POST /chat - Send message to chatbot",
            "POST /clear - Clear chat history",
            "GET /history - Get chat history"
        ]
    })

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({'error': 'Message is required'}), 400
        
        user_message = data['message'].strip()
        
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Get response from chatbot
        response = chatbot.get_response(user_message)
        
        return jsonify({
            'response': response,
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'error': f'Internal server error: {str(e)}',
            'status': 'error'
        }), 500

@app.route('/clear', methods=['POST'])
def clear_chat():
    try:
        chatbot.clear_history()
        return jsonify({
            'message': 'Chat history cleared successfully',
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': f'Error clearing chat: {str(e)}',
            'status': 'error'
        }), 500

@app.route('/history', methods=['GET'])
def get_history():
    try:
        return jsonify({
            'history': chatbot.chat_history,
            'count': len(chatbot.chat_history),
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': f'Error getting history: {str(e)}',
            'status': 'error'
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'Gym Chatbot API is running'
    })

@app.route('/save_conversation', methods=['POST'])
def save_conversation():
    try:
        data = request.get_json()
        filename = data.get('filename', 'gym_conversation.json')
        
        # Save conversation to server
        with open(f'conversations/{filename}', 'w') as f:
            json.dump(chatbot.chat_history, f, indent=2)
        
        return jsonify({
            'message': f'Conversation saved as {filename}',
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': f'Error saving conversation: {str(e)}',
            'status': 'error'
        }), 500

@app.route('/gym_data', methods=['GET'])
def get_gym_data():
    """Get all gym data for frontend display"""
    try:
        return jsonify({
            'data': chatbot.gym_data,
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': f'Error getting gym data: {str(e)}',
            'status': 'error'
        }), 500

if __name__ == '__main__':
    # Create conversations directory if it doesn't exist
    import os
    os.makedirs('conversations', exist_ok=True)
    
    print("🏋️ Starting Gym Chatbot API Server...")
    print("📡 API will be available at: http://localhost:5000")
    print("🌐 Frontend should connect to: http://localhost:5000")
    print("=" * 50)
    
    app.run(host='0.0.0.0', port=5000, debug=True)