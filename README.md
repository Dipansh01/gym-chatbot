# 🏋️ Gym Assistant Chatbot

A modern, interactive gym assistant chatbot built with Flask backend and vanilla HTML/CSS/JavaScript frontend. The chatbot helps users with workout routines, gym information, membership plans, class schedules, and fitness advice using Google's Gemini AI.

## ✨ Features

- **AI-Powered Conversations**: Powered by Google Gemini 1.5 Flash for intelligent responses
- **Gym Information**: Provides detailed information about:
  - Membership plans and pricing
  - Class schedules and programs  
  - Gym hours and equipment
  - Workout routines and fitness advice
  - Nutrition guidance
  - Safety tips and gym etiquette
- **Modern UI**: Beautiful, responsive chat interface with animations
- **Chat Management**: Save and clear chat history
- **Quick Questions**: Pre-built quick question buttons
- **Real-time Typing Indicators**: Enhanced user experience
- **Cross-platform**: Works on desktop and mobile devices

## 🛠️ Tech Stack

**Backend:**
- Python 3.7+
- Flask (Web framework)
- Flask-CORS (Cross-origin requests)
- Google Generative AI (Gemini 1.5 Flash)
- python-dotenv (Environment variables)

**Frontend:**
- HTML5
- CSS3 (with modern features like gradients, animations)
- Vanilla JavaScript (ES6+)
- Responsive design

## 📋 Prerequisites

Before running the application, make sure you have:

- Python 3.7 or higher installed
- A Google Gemini API key (free from Google AI Studio)
- Git (optional, for cloning)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd gym-chatbot
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv gym_bot_env
source gym_bot_env/bin/activate  # On Windows: gym_bot_env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install flask flask-cors google-generativeai python-dotenv
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

**Getting a Gemini API Key:**
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key to your `.env` file

### 5. Run the Application
```bash
python app.py
```

The server will start on `http://localhost:5000`

### 6. Access the Chatbot
Open your web browser and navigate to:
- **API Documentation**: `http://localhost:5000/`
- **Chat Interface**: `http://localhost:5000/templates/font.html`

## 📁 Project Structure

```
gym-chatbot/
│
├── app.py                 # Flask backend application
├── .env                   # Environment variables (not in repo)
├── .gitignore            # Git ignore file
├── .gitattributes        # Git attributes
├── README.md             # Project documentation
│
├── templates/
│   └── font.html         # Main chat interface
│
├── conversations/        # Saved chat histories (auto-created)
│
└── gym_bot_env/         # Virtual environment (auto-created)
```

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information and available endpoints |
| POST | `/chat` | Send message to chatbot |
| POST | `/clear` | Clear chat history |
| GET | `/history` | Get chat history |
| GET | `/health` | Health check |
| GET | `/gym_data` | Get gym information data |
| POST | `/save_conversation` | Save conversation to server |

### Example API Usage

**Send a message:**
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What are your membership plans?"}'
```

**Response:**
```json
{
  "response": "Here are our membership plans...",
  "status": "success"
}
```

## 🏋️ Gym Data

The chatbot includes comprehensive gym information:

**Membership Plans:**
- Basic: $29.99/month
- Premium: $49.99/month  
- Elite: $79.99/month

**Equipment Available:**
- Cardio machines (treadmills, ellipticals, bikes)
- Strength equipment (free weights, machines)
- Functional training tools

**Class Schedule:**
- Daily classes including Yoga, HIIT, CrossFit, Pilates
- Different times throughout the week

## 🎨 UI Features

- **Modern Design**: Gradient backgrounds, glass morphism effects
- **Smooth Animations**: Message slides, button hover effects
- **Responsive Layout**: Works on all screen sizes
- **Dark/Light Contrast**: Easy to read in any lighting
- **Status Indicators**: Online status and typing indicators
- **Quick Actions**: Pre-built question buttons for common queries

## 🔧 Customization

### Adding New Gym Data
Edit the `gym_data` dictionary in `app.py`:

```python
self.gym_data = {
    "membership_plans": {
        # Add new plans here
    },
    "class_schedule": {
        # Modify schedule here
    }
    # Add more data categories
}
```

### Modifying the AI Context
Update the `gym_context` in `app.py` to change how the AI responds:

```python
self.gym_context = """
Your custom instructions here...
"""
```

### Styling Changes
Modify the CSS in `templates/font.html` to customize the appearance.

## 🚨 Troubleshooting

### Common Issues:

1. **"GEMINI_API_KEY environment variable is required"**
   - Make sure you created the `.env` file
   - Verify your API key is correct
   - Check for typos in the variable name

2. **"Cannot connect to the server"**
   - Ensure Flask app is running (`python app.py`)
   - Check the port (default: 5000)
   - Verify no firewall blocking localhost

3. **CORS Issues**
   - Flask-CORS is installed and configured
   - Check browser console for specific errors

4. **API Rate Limits**
   - Google Gemini has usage limits
   - Check your API quota in Google Cloud Console

## 🔒 Security Considerations

- Keep your `.env` file secure and never commit it to version control
- The `.gitignore` file excludes sensitive files
- Consider rate limiting for production use
- Validate and sanitize user inputs

## 📱 Mobile Compatibility

The chatbot is fully responsive and works well on:
- Desktop computers
- Tablets
- Mobile phones
- Different screen orientations

## 🚀 Deployment

For production deployment:

1. **Environment Variables**: Set up proper environment variables
2. **WSGI Server**: Use Gunicorn or similar for production
3. **Reverse Proxy**: Configure Nginx or Apache
4. **HTTPS**: Implement SSL certificates
5. **Database**: Consider adding persistent storage

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is open source. Feel free to use, modify, and distribute as needed.

## 👏 Acknowledgments

- Google for providing the Gemini AI API
- Flask community for the excellent web framework
- Contributors and testers

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the Flask and Gemini API documentation
3. Create an issue in the repository
4. Contact the development team

---

**Made with ❤️ for fitness enthusiasts and gym-goers!** 🏋️‍♀️💪