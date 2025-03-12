import google.generativeai as genai # Import the Google Generative AI model
import gradio as gr # Import Gradio to create a web-based user interface (UI)
from api_read import GEMINI_API_KEY # Import the API key for Gemini API from an external file

# Configure Google Generative AI with the API key
genai.configure(api_key=GEMINI_API_KEY) # Set the API key for authentication

# Initialize the generative model
model = genai.GenerativeModel("gemini-1.5-pro") # Create a model instance using Gemini's specific version

def chat_interface(user_input, image_input, chat_state):
    # Check if the chat_state is None (first time interaction)
    if chat_state is None:
        chat_state = {"history": []} # Initialize an empty chat history
    
    # If user input is empty, return an empty response and the chat history
    if not user_input.strip():
        # Curate history from the existing conversation and return
        messages = [{"role": "user", "content": u} for u, a in chat_state["history"]]
        messages += [{"role": "assistant", content: a} for u, a in chat_state["history"]]
        curated_history = "\n\n".join([f"*user*: {u}\n\n*assistant*: {a}" for u, a in chat_state["history"]])
        return "", messages, curated_history, chat_state

    # Create a prompt for the model by combining chat history and user input
    prompt = "\n".join([f"User: {u}\nAssistant: {a}" for u, a in chat_state["history"]])
    prompt += f"\nUser: {user_input}\nAssistant: "

    # If an image is provided, include it in the prompt for the model to process
    if image_input:
        response = model.generate_content([image_input, prompt])
    else:
        # If no image is provided, just send the prompt text to the model
        response = model.generate_content(prompt)

    # Get the model's response (assistant's reply)
    reply = response.text

    # Update the chat history with the new user input and assistant's reply
    chat_state["history"].append((user_input, reply))

    # Prepare messages for the chatbot UI
    messages = [{"role": "user", "content": u} for u, a in chat_state["history"]]
    messages +=[{"role": "assistant", "content": a} for u, a in chat_state["history"]]

    # Curate and format the chat history
    curated_history = "\n\n".join(f"*user*: {u}\n*assistant*: {a}" for u, a in chat_state["history"])

    # Return updated UI elements : empty input box, chatbot messages, chat history, and updated chat state
    return "", messages, curated_history, chat_state

# Create Gradio UI for the chat_interface
with gr.Blocks() as demo:
    gr.Markdown("##Gemini 2.0 Flash Chat") # Add title to the UI

    chat_state = gr.State() # Store the current state of the chat, including history

    with gr.Row(): # Organize elements in a row (side by side)
        with gr.Column(): # First column for the chat area
            chatbot = gr.Chatbot(label="Conversation", type="messages") # Display chat messages
            user_input = gr.Textbox(label="Your Message") # Input box for user messages
            submit_btn = gr.Button("Gönder") # Submit button for sending messages
            attach_button = gr.Button("Resim Ekle", scale=1) # Button to attach images
            image_input = gr.Image(type="pil", label="Resim Yükle", visible=False, scale=1) # Hidden image upload area
        
        with gr.Column(): # Second column for displaying the raw chat history
            raw_history = gr.Markdown("*Conversation History") # Display formatted chat history
    
    # Define the function to toggle the visibility of the image upload area
    def toggle_image_upload():
        return gr.update(visible=True) # Make the image upload area visible
    
    # Link the attach button to the toggle_image_upload function
    attach_button.click(toggle_image_upload, [], [image_input])

    # Set the submit button to trigger the chat_interface function with inputs
    submit_btn.click(chat_interface, [user_input, image_input, chat_state], [user_input, chatbot, raw_history, chat_state])

    # Set the textbox to trigger the chat_interface function when Enter is pressed
    user_input.submit(chat_interface, [user_input, image_input, chat_state], [user_input, chatbot, raw_history, chat_state])

# Launch the Gradio interface (web app) and show errors if they occur
demo.launch(show_errors=True)





