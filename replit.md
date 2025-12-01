# Overview

Germot is a German A1-level language learning chatbot powered by Google's Gemini AI. The application provides an interactive chat interface where users can learn basic German through structured conversations. The bot responds in a consistent format: clear English explanations, simple German translations, practical examples, learning tasks, and helpful hints. It's designed specifically for beginners (A1 level) and maintains conversation history for each user session.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture

**Single-Page Application (SPA) Design**
- The application uses a simple, standalone HTML interface served by Flask
- Pure HTML/CSS/JavaScript implementation without frontend frameworks
- Custom CSS with gradient backgrounds and modern UI styling using the Poppins font family
- Responsive chat container (600px x 800px) with hover effects and smooth transitions
- Color scheme: Soft blues (#dae8fc, #668cff, #92a8ff) with warm accents for a friendly learning environment

**Bilingual Voice Assistant**
- Text-to-speech powered by Web Speech API with natural pronunciation
- Automatic language detection: German (de-DE) for German content, English (en-US) for English content
- Intelligent voice selection that matches detected language
- Speech rate optimized at 0.85 for clear, natural pronunciation
- Speaker button (▶️) on each bot response for easy audio playback
- Pause/resume functionality with visual button state feedback
- Clean text extraction that removes formatting characters (bullets, arrows) before speaking

**Rationale**: A frameworkless approach keeps the application lightweight and eliminates build complexity. The bilingual voice assistant enhances learning by providing native pronunciation examples and making the app more interactive and accessible.

## Backend Architecture

**Flask Web Server**
- Minimal Flask application serving both static content and API endpoints
- Template rendering for the chat interface
- RESTful API design for chat interactions
- CORS enabled for flexible deployment and potential future frontend separation

**Conversation Management**
- In-memory conversation history stored in a Python dictionary (`conversation_history`)
- Session-based tracking (likely using session IDs as keys, though implementation is incomplete)
- Stateful conversations allow context retention across multiple interactions

**Rationale**: Flask provides a lightweight, Python-native web framework perfect for small to medium applications. In-memory storage keeps the architecture simple for MVP stages, though this approach has limitations for production scaling (data lost on restart, not suitable for multi-instance deployments).

## AI Integration

**Google Gemini AI**
- Primary AI engine for natural language processing and German language instruction
- Configured via environment variable (`GEMINI_API_KEY`)
- Structured prompting system with `TEACHER_PROMPT` defining consistent response format

**Prompt Engineering Strategy**
- Hard-coded system prompt enforces strict response structure with 4-step learning format
- Format includes: English-only encouraging response, German-translated examples, learning tasks, and hints
- A1-level constraint ensures beginner-appropriate content
- Examples use "is called ... in German" format for natural voice pronunciation
- Bullet-point formatting for clarity and parseability
- Encouraging tone with positive feedback even for mistakes

**Learning Experience Features**
- Greeting system: Bot welcomes user and asks what topic to learn
- Encouraging feedback: All responses include positive reinforcement in English only
- Diverse examples: Three completely different examples per response to maximize learning variety
- Easy hints: Non-direct but accessible hints to guide learning
- Conversation history: Maintained per session for context awareness

**Rationale**: Gemini AI provides robust language understanding and generation capabilities. The structured prompt with 4-step format ensures consistent, pedagogically sound responses that follow language learning best practices. The voice assistant provides native pronunciation models, making learning more immersive and effective for A1 beginners.

## Deployment Configuration

**Production Server**
- Gunicorn WSGI server for production deployment
- Python 3.10 runtime specified for consistency
- Render platform deployment (indicated by environment variable usage)

**Rationale**: Gunicorn is production-grade and handles concurrent requests efficiently. Render provides simple deployment for Python web applications with environment variable management.

# External Dependencies

## Third-Party APIs

**Google Generative AI (Gemini)**
- Purpose: Core AI functionality for German language teaching
- Authentication: API key via `GEMINI_API_KEY` environment variable
- Integration: `google-generativeai` Python SDK

## Python Packages

**Flask** - Web framework for serving the application and handling HTTP requests

**Flask-CORS** - Cross-Origin Resource Sharing support for API flexibility

**google-generativeai** - Official Google SDK for Gemini AI integration

**gunicorn** - Production WSGI server for Flask applications

## Development Tools

**VS Code Configuration** - Python environment settings configured for system-level Python interpreter

## Infrastructure

**Render Platform** - Cloud hosting service for deployment (inferred from environment variable pattern)