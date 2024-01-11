import streamlit as st
import requests

WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjUwNTY5MDYzMTA0MzI1MjY1NTUzMzUxMzci_pc"


# Function to post data to the webhook using argument unpacking
def post_to_webhook(**data):
    response = requests.post(WEBHOOK_URL, json=data)
    return response


st.title("🎬 Submit Your Video Idea")

st.markdown(
    """
Got a great idea for a video? I'd love to hear it! 🤔 Share your thoughts and help shape the content on 'Coding is Fun'.
Check out my [YouTube channel](https://youtube.com/@codingisfun) for more.
"""
)

with st.form(key="idea_form"):
    name = st.text_input("Name (optional)", placeholder="Your Name")
    email = st.text_input("Email (optional)", placeholder="Your Email")
    video_idea = st.text_area("Video Idea", placeholder="Describe your idea...")

    submit_button = st.form_submit_button(label="Submit Idea 🚀")

    if submit_button:
        if not video_idea.strip():
            st.error("Please enter a video idea. 💡")
            st.stop()

        data = {"name": name, "email": email, "video_idea": video_idea}
        response = post_to_webhook(**data)
        if response.status_code == 200:
            st.success("Thanks for your submission! 🌟")
        else:
            st.error("There was an error. Please try again. 🛠️")
