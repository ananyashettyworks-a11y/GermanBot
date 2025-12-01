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

**Rationale**: A frameworkless approach keeps the application lightweight and eliminates build complexity, making it ideal for a simple chatbot interface. The modern CSS provides a polished user experience without additional dependencies.

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
- Hard-coded system prompt enforces strict response structure
- Format includes: English explanation, German translation, examples, learning tasks, and hints
- A1-level constraint ensures beginner-appropriate content
- Bullet-point formatting for clarity and parseability

**Rationale**: Gemini AI provides robust language understanding and generation capabilities. The structured prompt ensures consistent, pedagogically sound responses that follow language learning best practices. Environment-based API key management supports secure deployment.

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