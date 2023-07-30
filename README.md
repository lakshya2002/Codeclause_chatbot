# Codeclause_chatbot
# Chatbot Building and Design

## Description
This repository contains the code and resources for building a chatbot using Python. The chatbot is designed to interact with users, understand their queries, and provide appropriate responses based on predefined intents.

This is my Code Clause internship Golden project.

## Features
- The chatbot is built using natural language processing techniques to understand user input and generate relevant responses.
- It uses a Bag of Words approach to convert user messages into numerical vectors and predict the appropriate intent.
- The model is trained using a neural network with multiple layers, including dense layers with ReLU activation and a Softmax output layer.
- The training data includes a collection of predefined intents, each associated with a set of user messages.
- The chatbot is integrated into a web-based user interface using Flask, allowing users to interact with the chatbot through a web browser.
- The user interface provides a simple and intuitive design, allowing users to type messages and receive responses from the chatbot.

## Technologies Used
- Python
- Spacy
- TensorFlow
- Flask

## Getting Started
To run the chatbot and interact with it through the web interface, follow these steps:

1. Clone this repository to your local machine.
2. Install Python dependencies by running `pip install -r requirements.txt`.
3. Run the Flask app by executing `python app.py` in the terminal.
4. Open your web browser and navigate to `http://localhost:5000`.
5. Type a message in the chatbox and press Enter or click the Send button to receive a response from the chatbot.

## File Structure
- `app.py`: The main Flask application handles HTTP requests and responses.
- `chatbot.py`: The code for the chatbot logic, including predicting intents and generating responses.
- `templates/index.html`: The HTML template for the web-based user interface.
- `static/style.css`: The CSS file for styling the web page.
- `static/script.js`: The JavaScript file for handling user interactions on the web page.

## Acknowledgements
A chatbot was created as part of a project to learn about natural language processing and neural networks.


