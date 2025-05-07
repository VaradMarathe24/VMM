import streamlit as st

# Page setup
st.set_page_config(page_title="CricBot - Cricket Chatbot", layout="centered")
st.title("🏏 CricBot - Your Cricket Assistant")
st.markdown("Ask me about matches, players, tickets, or cricket merchandise!")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Response logic
def generate_response(user_input):
    user_input = user_input.lower()

    if "match" in user_input or "score" in user_input:
        return "The next match is India vs Australia on April 15th at 7:00 PM."
    elif "virat" in user_input or "kohli" in user_input:
        return "Virat Kohli is a top-order batsman and former Indian captain."
    elif "rohit" in user_input or "sharma" in user_input:
        return "Rohit Sharma is the current Indian captain and a dynamic opener."
    elif "bumrah" in user_input or "jasprit" in user_input:
        return "I only believe in Jassi Bhai. Game-changing player he is!"
    elif "ticket" in user_input or "book" in user_input:
        return "You can book tickets at www.bcci.tv or Paytm Insider."
    elif "merchandise" in user_input or "jersey" in user_input:
        return "Official jerseys and caps are available at shop.bcci.tv."
    elif "bye" in user_input or "exit" in user_input:
        return "Thank you for chatting! Enjoy the match! "
    else:
        return "I'm still learning! Please rephrase your question."

# User input
user_input = st.text_input("You:", placeholder="Ask something about cricket...")

# If user sends a message
if user_input:
    response = generate_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("CricBot", response))

# Show chat history
for sender, msg in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {msg}")
