# Gemini-AI-Chatbot
This project is a chatbot interface built using Google Generative AI (Gemini) and Gradio. The chatbot allows users to have interactive conversations and supports both text and image inputs.

FEATURES

Utilizes Google Generative AI (Gemini-1.5-pro) for intelligent responses.

Built with Gradio for an easy-to-use web-based interface.

Supports both text and image inputs for a more dynamic conversation.

Maintains chat history for a continuous conversation flow.

INSTALLATION

1. Clone the Repository

git clone https://github.com/alpersancili/Gemini-AI-Chatbot.git
cd Gemini-AI-Chatbot

2. Install Dependencies

Make sure you have Python installed, then run:

pip install -r requirements.txt

3. Set Up API Key

Create a .env file in the project directory and add your Gemini API key:

GEMINI_API_KEY=your_api_key_here

Alternatively, you can store the API key in a separate Python file (api_read.py) and import it:

from api_read import GEMINI_API_KEY

USAGE

Run the chatbot application with:

python app.py

This will launch the Gradio interface, allowing users to chat with the Gemini AI chatbot.

FİLE STRUCTURE

├── app.py              # Main application file

├── api_read.py         # Contains API key (or use .env file)

├── requirements.txt    # Required Python dependencies

├── README.md           # Project documentation

├── ...                 # Other files

DEPLOYMENT

You can deploy this chatbot on platforms like Hugging Face Spaces, Google Colab, or Streamlit Cloud.

CONTRIBUTING

Feel free to contribute! Open a pull request or report issues if you find any bugs.

