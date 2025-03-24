# import streamlit as st
# import random

# # Function for basic Mad Libs game with user input (manual mode)
# def mad_libs():
#     st.title("Mad Libs Game (Manual Input)")
#     st.write("Enter the following words:")

#     # Ask for user input with Streamlit text input boxes
#     adjective = st.text_input("Enter an adjective:")
#     noun = st.text_input("Enter a noun:")
#     verb = st.text_input("Enter a verb:")
#     adjective2 = st.text_input("Enter another adjective:")
#     noun2 = st.text_input("Enter another noun:")
#     verb2 = st.text_input("Enter another verb:")

#     # Check if all fields are filled
#     if all([adjective, noun, verb, adjective2, noun2, verb2]):
#         if st.button("Generate Story"):
#             # Story template with placeholders
#             story = f"""
#             Once upon a time, there was a {adjective} {noun} who loved to {verb} every day. One day, it met a {adjective2} {noun2} who was also very good at {verb2}.
#             """

#             st.write("Here's your Mad Libs story!")
#             st.write(story)

#             # Option to save the story as a text file
#             save_button = st.download_button(
#                 label="Download your story",
#                 data=story,
#                 file_name="mad_libs_story.txt",
#                 mime="text/plain"
#             )

#     else:
#         st.warning("Please fill in all the inputs!")

# # Function for Mad Libs with random words from predefined lists (random mode)
# def mad_libs_with_random_words():
#     st.title("Mad Libs Game (Random Words)")
#     st.write("Here's a random Mad Libs story for you!")

#     # Create lists of possible words
#     adjectives = ["funny", "excited", "lazy", "brave", "strange", "silly", "beautiful", "brilliant"]
#     nouns = ["dog", "robot", "city", "banana", "tree", "alien", "car", "pirate"]
#     verbs = ["jump", "run", "dance", "play", "sing", "swim", "travel", "explore"]

#     # Pick random words from the lists
#     adjective = random.choice(adjectives)
#     noun = random.choice(nouns)
#     verb = random.choice(verbs)
#     adjective2 = random.choice(adjectives)
#     noun2 = random.choice(nouns)
#     verb2 = random.choice(verbs)

#     # Story template with placeholders
#     story = f"""
#     Once upon a time, there was a {adjective} {noun} who loved to {verb} every day. One day, it met a {adjective2} {noun2} who was also very good at {verb2}.
#     """

#     st.write(story)

#     # Option to save the random story as a text file
#     save_button = st.download_button(
#         label="Download this random story",
#         data=story,
#         file_name="random_mad_libs_story.txt",
#         mime="text/plain"
#     )

# # Function to select the story template type
# def choose_story_template():
#     st.title("Welcome to Mad Libs Game!")
    
#     choice = st.radio("Choose your Mad Libs game mode:", 
#                       ("Manual Mad Libs (You provide the words)", 
#                        "Random Mad Libs (Random words from a list)"))

#     if choice == "Manual Mad Libs (You provide the words)":
#         choose_template_manual()  # Run basic Mad Libs with user input
#     elif choice == "Random Mad Libs (Random words from a list)":
#         choose_template_random()  # Run random Mad Libs with predefined words

# # Function to choose a manual story template
# def choose_template_manual():
#     story_templates = {
#         "A Day at the Park": "Once upon a time, there was a {adjective} {noun} who loved to {verb} every day at the park.",
#         "The Magical Adventure": "A {adjective} {noun} traveled to a distant land where it {verb} a magical creature named {noun2}.",
#         "The Wild Journey": "The {adjective} {noun} decided to {verb} across the world, meeting a {adjective2} {noun2} who was also a master of {verb2}."
#     }

#     template_choice = st.selectbox("Select a story template:", list(story_templates.keys()))
#     story_template = story_templates[template_choice]
    
#     # Ask for input based on selected template
#     adjective = st.text_input("Enter an adjective:")
#     noun = st.text_input("Enter a noun:")
#     verb = st.text_input("Enter a verb:")
#     adjective2 = st.text_input("Enter another adjective (if needed):")
#     noun2 = st.text_input("Enter another noun (if needed):")
#     verb2 = st.text_input("Enter another verb (if needed):")

#     if all([adjective, noun, verb, adjective2, noun2, verb2]) or all([adjective, noun, verb]):
#         if st.button("Generate Story"):
#             story = story_template.format(adjective=adjective, noun=noun, verb=verb, adjective2=adjective2, noun2=noun2, verb2=verb2)
#             st.write("Here's your Mad Libs story!")
#             st.write(story)

#             # Option to save the story as a text file
#             save_button = st.download_button(
#                 label="Download your story",
#                 data=story,
#                 file_name="mad_libs_story.txt",
#                 mime="text/plain"
#             )
#     else:
#         st.warning("Please fill in all the necessary inputs!")

# # Function to choose a random story template
# def choose_template_random():
#     story_templates_random = {
#         "The Brave Hero": "The {adjective} {noun} set out on a quest to {verb} and defeat the {adjective2} {noun2}.",
#         "Space Adventure": "The {adjective} {noun} boarded the spaceship to {verb} through the stars, meeting a {adjective2} {noun2}.",
#         "Jungle Exploration": "The {adjective} {noun} ventured into the jungle to {verb}, where it encountered a {adjective2} {noun2} who could {verb2}."
#     }

#     template_choice = st.selectbox("Select a random story template:", list(story_templates_random.keys()))
#     story_template = story_templates_random[template_choice]

#     # Generate the story with random words
#     adjectives = ["funny", "excited", "lazy", "brave", "strange", "silly", "beautiful"]
#     nouns = ["dog", "robot", "city", "banana", "tree", "alien", "car"]
#     verbs = ["jump", "run", "dance", "play", "sing", "swim", "travel"]
    
#     adjective = random.choice(adjectives)
#     noun = random.choice(nouns)
#     verb = random.choice(verbs)
#     adjective2 = random.choice(adjectives)
#     noun2 = random.choice(nouns)
#     verb2 = random.choice(verbs)

#     # Format the story using random words
#     story = story_template.format(adjective=adjective, noun=noun, verb=verb, adjective2=adjective2, noun2=noun2, verb2=verb2)
    
#     st.write(story)

#     # Option to save the random story as a text file
#     save_button = st.download_button(
#         label="Download this random story",
#         data=story,
#         file_name="random_mad_libs_story.txt",
#         mime="text/plain"
#     )

# # Main execution
# if __name__ == "__main__":
#     choose_story_template()







































# import streamlit as st
# import random
# import time

# # Custom CSS for colorful UI and footer
# st.markdown("""
#     <style>
#         .main {
#             background-color: #f8f9fa;
#             color: #333;
#         }
#         .sidebar .sidebar-content {
#             background-color: #4CAF50;
#             color: white;
#         }
#         h1, h2, h3 {
#             color: #ff6347;  /* Tomato */
#         }
#         .stButton>button {
#             background-color: #4CAF50;
#             color: white;
#             border-radius: 10px;
#             padding: 10px;
#             font-size: 16px;
#         }
#         .stButton>button:hover {
#             background-color: #45a049;
#         }
#         .footer {
#             position: fixed;
#             bottom: 0;
#             width: 100%;
#             background-color: #2f2f2f;
#             color: white;
#             text-align: center;
#             padding: 10px;
#         }
#         .footer a {
#             color: #ff6347;
#         }
#         .footer a:hover {
#             color: #ff4500;
#         }
#     </style>
#     """, unsafe_allow_html=True)

# # Function for basic Mad Libs game with user input (manual mode)
# def mad_libs():
#     st.title("Mad Libs Game (Manual Input)")
#     st.write("Enter the following words:")

#     # Ask for user input with Streamlit text input boxes
#     adjective = st.text_input("Enter an adjective:")
#     noun = st.text_input("Enter a noun:")
#     verb = st.text_input("Enter a verb:")
#     adjective2 = st.text_input("Enter another adjective:")
#     noun2 = st.text_input("Enter another noun:")
#     verb2 = st.text_input("Enter another verb:")

#     # Check if all fields are filled
#     if all([adjective, noun, verb, adjective2, noun2, verb2]):
#         if st.button("Generate Story"):
#             # Story template with placeholders
#             story = f"""
#             Once upon a time, there was a {adjective} {noun} who loved to {verb} every day. One day, it met a {adjective2} {noun2} who was also very good at {verb2}.
#             """

#             st.write("Here's your Mad Libs story!")
#             st.write(story)

#             # Option to save the story as a text file
#             save_button = st.download_button(
#                 label="Download your story",
#                 data=story,
#                 file_name="mad_libs_story.txt",
#                 mime="text/plain"
#             )

#     else:
#         st.warning("Please fill in all the inputs!")

# # Function for Mad Libs with random words from predefined lists (random mode)
# def mad_libs_with_random_words():
#     st.title("Mad Libs Game (Random Words)")
#     st.write("Here's a random Mad Libs story for you!")

#     # Create lists of possible words
#     adjectives = ["funny", "excited", "lazy", "brave", "strange", "silly", "beautiful", "brilliant"]
#     nouns = ["dog", "robot", "city", "banana", "tree", "alien", "car", "pirate"]
#     verbs = ["jump", "run", "dance", "play", "sing", "swim", "travel", "explore"]
#     places = ["mountain", "forest", "desert", "ocean", "castle", "cave", "village"]
#     emotions = ["happy", "angry", "excited", "nervous", "scared", "sad", "confused"]
#     creatures = ["dragon", "troll", "goblin", "vampire", "werewolf", "fairy", "griffin"]
#     plural_nouns = ["trees", "bottles", "rocks", "birds", "books", "apples", "dollars"]

#     # Pick random words from the lists
#     adjective = random.choice(adjectives)
#     noun = random.choice(nouns)
#     verb = random.choice(verbs)
#     adjective2 = random.choice(adjectives)
#     noun2 = random.choice(nouns)
#     verb2 = random.choice(verbs)
#     place = random.choice(places)
#     emotion = random.choice(emotions)
#     creature = random.choice(creatures)
#     plural_noun = random.choice(plural_nouns)

#     # Long story template with placeholders
#     story = f"""
#     The Great Adventure
#     ---------------------
#     A young adventurer, full of excitement, set off on a quest to find the {adjective} {noun} hidden deep in the {place}. Along the way, the adventurer met a {adjective2} {noun2} who was {verb} and {emotion}. Together, they faced many challenges, including crossing a {adjective} river full of {noun}s, and navigating a {adjective2} forest filled with {plural_noun}. After a long journey, they finally reached the {noun}, only to discover that it was guarded by a {adjective} {creature}. The adventurer and the creature had an epic battle, and only one would come out victorious. What happened next? Only you can decide!
#     """

#     st.write(story)

#     # Option to save the random story as a text file
#     save_button = st.download_button(
#         label="Download this random story",
#         data=story,
#         file_name="random_mad_libs_story.txt",
#         mime="text/plain"
#     )

# # Function to allow users to select a category for story words
# def choose_category():
#     st.sidebar.header("Choose Your Mad Libs Categories")
#     categories = ["Animals", "Foods", "Emotions", "Fantasy Creatures", "Adjectives", "Verbs"]
#     selected_category = st.sidebar.selectbox("Pick a word category for your story:", categories)

#     return selected_category

# # Function to get words from a selected category
# def get_words_from_category(category):
#     word_categories = {
#         "Animals": ["dog", "cat", "elephant", "tiger", "panda", "lion", "bear", "unicorn"],
#         "Foods": ["pizza", "burger", "apple", "sushi", "cake", "ice cream", "burrito", "salad"],
#         "Emotions": ["happy", "sad", "angry", "excited", "nervous", "scared", "confused"],
#         "Fantasy Creatures": ["dragon", "elf", "goblin", "vampire", "werewolf", "fairy", "mermaid"],
#         "Adjectives": ["funny", "strong", "brave", "elegant", "lazy", "beautiful", "weird", "cute"],
#         "Verbs": ["run", "jump", "sing", "dance", "swim", "read", "play", "explore"]
#     }

#     return word_categories[category]

# # Function for handling user profile and preferences
# def user_profile():
#     st.sidebar.header("User Profile")
#     name = st.sidebar.text_input("Enter your name:")
#     favorite_template = st.sidebar.selectbox("Pick your favorite Mad Libs template:", ["A Day at the Park", "Magical Adventure", "Wild Journey"])
    
#     if st.sidebar.button("Save Profile"):
#         st.sidebar.write(f"Profile saved! Welcome back, {name}. Your favorite template is: {favorite_template}")

# # Function to add a timer challenge to the Mad Libs game
# def timer_challenge():
#     st.sidebar.header("Timer Challenge")
#     timer = st.sidebar.slider("Set your timer (in seconds):", 10, 60, 30)
    
#     st.sidebar.write(f"You have {timer} seconds to complete the Mad Libs game!")
    
#     start_button = st.sidebar.button("Start Timer")
#     if start_button:
#         start_time = time.time()
#         while True:
#             elapsed_time = time.time() - start_time
#             if elapsed_time > timer:
#                 st.sidebar.write("Time's up! Please submit your Mad Libs answers.")
#                 break

# # Main function to allow the user to choose between manual or random Mad Libs
# def choose_story_template():
#     st.title("Welcome to Mad Libs Game!")
    
#     # Display user profile
#     user_profile()

#     # Timer challenge
#     timer_challenge()

#     # Choose story template
#     choice = st.radio("Choose your Mad Libs game mode:", 
#                       ("Manual Mad Libs (You provide the words)", 
#                        "Random Mad Libs (Random words from a list)"))

#     if choice == "Manual Mad Libs (You provide the words)":
#         mad_libs()  # Run basic Mad Libs with user input
#     elif choice == "Random Mad Libs (Random words from a list)":
#         mad_libs_with_random_words()  # Run random Mad Libs with predefined words

# # Footer for developer info
# def footer():
#     st.markdown("""
#         <div class="footer">
#             <p>Developed by <a href="https://www.linkedin.com/in/abdul-rehman-xyz">Abdul Rehman</a></p>
#         </div>
#     """, unsafe_allow_html=True)

# # Main execution
# if __name__ == "__main__":
#     choose_story_template()
#     footer()





































import streamlit as st
import random
import time

# Custom CSS for colorful UI and footer
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
            color: #333;
        }
        .sidebar .sidebar-content {
            background-color: #4CAF50;
            color: white;
        }
        h1, h2, h3 {
            color: #ff6347;  /* Tomato */
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #2f2f2f;
            color: white;
            text-align: center;
            padding: 10px;
        }
        .footer a {
            color: #ff6347;
        }
        .footer a:hover {
            color: #ff4500;
        }
    </style>
    """, unsafe_allow_html=True)

# List of categories with options for users to select
adjectives = ["funny", "excited", "lazy", "brave", "strange", "silly", "beautiful", "brilliant"]
nouns = ["dog", "robot", "city", "banana", "tree", "alien", "car", "pirate"]
verbs = ["jump", "run", "dance", "play", "sing", "swim", "travel", "explore"]
places = ["mountain", "forest", "desert", "ocean", "castle", "cave", "village"]
emotions = ["happy", "angry", "excited", "nervous", "scared", "sad", "confused"]
creatures = ["dragon", "troll", "goblin", "vampire", "werewolf", "fairy", "griffin"]
plural_nouns = ["trees", "bottles", "rocks", "birds", "books", "apples", "dollars"]

# Function for Mad Libs with user input for word selection
def mad_libs_with_user_input():
    st.title("Mad Libs Game (With Word Selection)")

    # Select words from each category
    adjective = st.selectbox("Choose an adjective:", adjectives)
    noun = st.selectbox("Choose a noun:", nouns)
    verb = st.selectbox("Choose a verb:", verbs)
    adjective2 = st.selectbox("Choose another adjective:", adjectives)
    noun2 = st.selectbox("Choose another noun:", nouns)
    verb2 = st.selectbox("Choose another verb:", verbs)
    place = st.selectbox("Choose a place:", places)
    emotion = st.selectbox("Choose an emotion:", emotions)
    creature = st.selectbox("Choose a creature:", creatures)
    plural_noun = st.selectbox("Choose a plural noun:", plural_nouns)

    if st.button("Generate Story"):
        # Long story template with placeholders
        story = f"""
        The Great Adventure
        ---------------------
        A young adventurer, full of excitement, set off on a quest to find the {adjective} {noun} hidden deep in the {place}. 
        Along the way, the adventurer met a {adjective2} {noun2} who was {verb} and {emotion}. 
        Together, they faced many challenges, including crossing a {adjective} river full of {noun}s, and navigating a {adjective2} forest filled with {plural_noun}. 
        After a long journey, they finally reached the {noun}, only to discover that it was guarded by a {adjective} {creature}. 
        The adventurer and the creature had an epic battle, and only one would come out victorious.
        """

        st.write(story)

        # Option to save the generated story as a text file
        save_button = st.download_button(
            label="Download your story",
            data=story,
            file_name="mad_libs_story.txt",
            mime="text/plain"
        )

# Function for random Mad Libs with predefined word categories
def mad_libs_with_random_words():
    st.title("Random Mad Libs Game")

    # Randomly select words from the predefined lists
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    adjective2 = random.choice(adjectives)
    noun2 = random.choice(nouns)
    verb2 = random.choice(verbs)
    place = random.choice(places)
    emotion = random.choice(emotions)
    creature = random.choice(creatures)
    plural_noun = random.choice(plural_nouns)

    # Random story template with placeholders filled in
    story = f"""
    The Great Adventure
    ---------------------
    A young adventurer, full of excitement, set off on a quest to find the {adjective} {noun} hidden deep in the {place}. 
    Along the way, the adventurer met a {adjective2} {noun2} who was {verb} and {emotion}. 
    Together, they faced many challenges, including crossing a {adjective} river full of {noun}s, and navigating a {adjective2} forest filled with {plural_noun}. 
    After a long journey, they finally reached the {noun}, only to discover that it was guarded by a {adjective} {creature}. 
    The adventurer and the creature had an epic battle, and only one would come out victorious.
    """

    st.write(story)

    # Option to save the random story as a text file
    save_button = st.download_button(
        label="Download your random story",
        data=story,
        file_name="random_mad_libs_story.txt",
        mime="text/plain"
    )

# Function for handling user profile and preferences
def user_profile():
    st.sidebar.header("User Profile")
    name = st.sidebar.text_input("Enter your name:")
    favorite_template = st.sidebar.selectbox("Pick your favorite Mad Libs template:", ["A Day at the Park", "Magical Adventure", "Wild Journey"])
    
    if st.sidebar.button("Save Profile"):
        st.sidebar.write(f"Profile saved! Welcome back, {name}. Your favorite template is: {favorite_template}")

# Function to add a timer challenge to the Mad Libs game
def timer_challenge():
    st.sidebar.header("Timer Challenge")
    timer = st.sidebar.slider("Set your timer (in seconds):", 10, 60, 30)
    
    st.sidebar.write(f"You have {timer} seconds to complete the Mad Libs game!")
    
    start_button = st.sidebar.button("Start Timer")
    if start_button:
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time > timer:
                st.sidebar.write("Time's up! Please submit your Mad Libs answers.")
                break

# Main function to allow the user to choose between manual or random Mad Libs
def choose_story_template():
    st.title("Welcome to Mad Libs Game!")
    
    # Display user profile
    user_profile()

    # Timer challenge
    timer_challenge()

    # Choose story template
    choice = st.radio("Choose your Mad Libs game mode:", 
                      ("Mad Libs with Word Selection (Choose words)", 
                       "Random Mad Libs (Random words from a list)"))

    if choice == "Mad Libs with Word Selection (Choose words)":
        mad_libs_with_user_input()  # Run Mad Libs with user input
    elif choice == "Random Mad Libs (Random words from a list)":
        mad_libs_with_random_words()  # Run random Mad Libs with predefined words

# Footer for developer info
def footer():
    st.markdown("""
        <div class="footer">
            <p>Developed by <a href="https://www.linkedin.com/in/abdul-rehman-xyz">Abdul Rehman</a></p>
        </div>
    """, unsafe_allow_html=True)

# Main execution
if __name__ == "__main__":
    choose_story_template()
    footer()
