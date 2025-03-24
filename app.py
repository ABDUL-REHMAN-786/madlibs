import streamlit as st
import random

# Function for basic Mad Libs game with user input (manual mode)
def mad_libs():
    st.title("Mad Libs Game (Manual Input)")
    st.write("Enter the following words:")

    # Ask for user input with Streamlit text input boxes
    adjective = st.text_input("Enter an adjective:")
    noun = st.text_input("Enter a noun:")
    verb = st.text_input("Enter a verb:")
    adjective2 = st.text_input("Enter another adjective:")
    noun2 = st.text_input("Enter another noun:")
    verb2 = st.text_input("Enter another verb:")

    # Check if all fields are filled
    if all([adjective, noun, verb, adjective2, noun2, verb2]):
        if st.button("Generate Story"):
            # Story template with placeholders
            story = f"""
            Once upon a time, there was a {adjective} {noun} who loved to {verb} every day. One day, it met a {adjective2} {noun2} who was also very good at {verb2}.
            """

            st.write("Here's your Mad Libs story!")
            st.write(story)

            # Option to save the story as a text file
            save_button = st.download_button(
                label="Download your story",
                data=story,
                file_name="mad_libs_story.txt",
                mime="text/plain"
            )

    else:
        st.warning("Please fill in all the inputs!")

# Function for Mad Libs with random words from predefined lists (random mode)
def mad_libs_with_random_words():
    st.title("Mad Libs Game (Random Words)")
    st.write("Here's a random Mad Libs story for you!")

    # Create lists of possible words
    adjectives = ["funny", "excited", "lazy", "brave", "strange", "silly", "beautiful", "brilliant"]
    nouns = ["dog", "robot", "city", "banana", "tree", "alien", "car", "pirate"]
    verbs = ["jump", "run", "dance", "play", "sing", "swim", "travel", "explore"]

    # Pick random words from the lists
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    adjective2 = random.choice(adjectives)
    noun2 = random.choice(nouns)
    verb2 = random.choice(verbs)

    # Story template with placeholders
    story = f"""
    Once upon a time, there was a {adjective} {noun} who loved to {verb} every day. One day, it met a {adjective2} {noun2} who was also very good at {verb2}.
    """

    st.write(story)

    # Option to save the random story as a text file
    save_button = st.download_button(
        label="Download this random story",
        data=story,
        file_name="random_mad_libs_story.txt",
        mime="text/plain"
    )

# Function to select the story template type
def choose_story_template():
    st.title("Welcome to Mad Libs Game!")
    
    choice = st.radio("Choose your Mad Libs game mode:", 
                      ("Manual Mad Libs (You provide the words)", 
                       "Random Mad Libs (Random words from a list)"))

    if choice == "Manual Mad Libs (You provide the words)":
        choose_template_manual()  # Run basic Mad Libs with user input
    elif choice == "Random Mad Libs (Random words from a list)":
        choose_template_random()  # Run random Mad Libs with predefined words

# Function to choose a manual story template
def choose_template_manual():
    story_templates = {
        "A Day at the Park": "Once upon a time, there was a {adjective} {noun} who loved to {verb} every day at the park.",
        "The Magical Adventure": "A {adjective} {noun} traveled to a distant land where it {verb} a magical creature named {noun2}.",
        "The Wild Journey": "The {adjective} {noun} decided to {verb} across the world, meeting a {adjective2} {noun2} who was also a master of {verb2}."
    }

    template_choice = st.selectbox("Select a story template:", list(story_templates.keys()))
    story_template = story_templates[template_choice]
    
    # Ask for input based on selected template
    adjective = st.text_input("Enter an adjective:")
    noun = st.text_input("Enter a noun:")
    verb = st.text_input("Enter a verb:")
    adjective2 = st.text_input("Enter another adjective (if needed):")
    noun2 = st.text_input("Enter another noun (if needed):")
    verb2 = st.text_input("Enter another verb (if needed):")

    if all([adjective, noun, verb, adjective2, noun2, verb2]) or all([adjective, noun, verb]):
        if st.button("Generate Story"):
            story = story_template.format(adjective=adjective, noun=noun, verb=verb, adjective2=adjective2, noun2=noun2, verb2=verb2)
            st.write("Here's your Mad Libs story!")
            st.write(story)

            # Option to save the story as a text file
            save_button = st.download_button(
                label="Download your story",
                data=story,
                file_name="mad_libs_story.txt",
                mime="text/plain"
            )
    else:
        st.warning("Please fill in all the necessary inputs!")

# Function to choose a random story template
def choose_template_random():
    story_templates_random = {
        "The Brave Hero": "The {adjective} {noun} set out on a quest to {verb} and defeat the {adjective2} {noun2}.",
        "Space Adventure": "The {adjective} {noun} boarded the spaceship to {verb} through the stars, meeting a {adjective2} {noun2}.",
        "Jungle Exploration": "The {adjective} {noun} ventured into the jungle to {verb}, where it encountered a {adjective2} {noun2} who could {verb2}."
    }

    template_choice = st.selectbox("Select a random story template:", list(story_templates_random.keys()))
    story_template = story_templates_random[template_choice]

    # Generate the story with random words
    adjectives = ["funny", "excited", "lazy", "brave", "strange", "silly", "beautiful"]
    nouns = ["dog", "robot", "city", "banana", "tree", "alien", "car"]
    verbs = ["jump", "run", "dance", "play", "sing", "swim", "travel"]
    
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    adjective2 = random.choice(adjectives)
    noun2 = random.choice(nouns)
    verb2 = random.choice(verbs)

    # Format the story using random words
    story = story_template.format(adjective=adjective, noun=noun, verb=verb, adjective2=adjective2, noun2=noun2, verb2=verb2)
    
    st.write(story)

    # Option to save the random story as a text file
    save_button = st.download_button(
        label="Download this random story",
        data=story,
        file_name="random_mad_libs_story.txt",
        mime="text/plain"
    )

# Main execution
if __name__ == "__main__":
    choose_story_template()
