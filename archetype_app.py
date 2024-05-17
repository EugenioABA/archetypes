from Archetype_Model import archetype_prediction
from Archetype_Descriptions import archetype_descriptions
import streamlit as st

st.set_page_config(page_title="Archetype App", page_icon="https://upload.wikimedia.org/wikipedia/commons/7/7d/Abawikilogo.png", layout="centered", initial_sidebar_state="collapsed")

st.image('https://upload.wikimedia.org/wikipedia/commons/7/7d/Abawikilogo.png', width=80)
#developed by 
st.write('Developed by Business Intelligence')
st.title('Archetype App')

# Title
st.header("Welcome!")

# Introduction
st.write("""
Discover the essence of your communications with our Brand Archetype Predictor! This tool helps ABA marketing staff analyze text to identify which of the 12 brand archetypes it best represents. Whether you're crafting outreach or internal messages, gain actionable insights to enhance engagement.
""")

st.write("""
This tool can help you to:
- **Clarify Brand Identity**: Understand the core personality of our communications.
- **Enhance Strategies**: Align messages with our identified archetype for consistency.
- **Foster Connections**: Build stronger relationships by speaking our audience's language.
""")

# How It Works
st.header("How It Works")
st.write("""
1. **Input Text**: Enter text that embodies the ABA's voice.
2. **Analyze**: Our model evaluates your text against 12 archetypes.
3. **Discover**: Get a report on the best-matched archetype and insights for branding.
""")
st.markdown("---")


#########################################################################################################################################################################
#    The app will display a text input box for the user to enter a tagline or a piece of text that they want to identify the archetype for.
#    The user can enter the tagline in the text input box and click the "Predict Archetype" button to get the predicted archetype.
#########################################################################################################################################################################

# Get tagline input from the user
tagline = st.text_input('Enter the text you want to idendify the archetype for', placeholder='Defending Liberty Pursuing Justice')

if st.button('Idendify Archetype'):
    if tagline == '':
        st.warning('Please enter text to identify the archetype.⚠️')
    elif tagline != '':
        top_3_archetypes, top_3_probabilities = archetype_prediction(tagline)

#########################################################################################################################################################################
#    In case the probability of the most likely archetype is less than 15%, the app will display a warning message indicating that the text does not match any archetype.
#########################################################################################################################################################################

        # Check if the highest probability is less than 15
        if top_3_probabilities[0] < 15:
            st.info("This text does not match any archetype  ⚠️ \n\n This might be the case if the text is too short, lacks character, or has conflicting features. \n\n Please try a different text.")
        
#########################################################################################################################################################################
#    In case the probability of the most likely archetype is less then 50%, the app will display the top 3 archetypes with their probabilities in a vertical order.
#########################################################################################################################################################################        
                
        else:
            # Display the most probable archetype and its description
            highest_probability_archetype = top_3_archetypes[0]
            highest_probability = top_3_probabilities[0]
            if highest_probability <= 50:
                # Display all archetypes in a vertical order
                for i in range(3):
                    if top_3_probabilities[i] < 20:
                        st.error(f"Identified Archetype {i+1}: {top_3_archetypes[i]} ⚠️\n\n Match: {top_3_probabilities[i]}%")
                    elif 20 <= top_3_probabilities[i] <= 50:
                        st.warning(f"Identified Archetype {i+1}: {top_3_archetypes[i]} ⚠️\n\n Match: {top_3_probabilities[i]}%")
                    else:
                        st.success(f"Identified Archetype {i+1}: {top_3_archetypes[i]} \n\n Match: {top_3_probabilities[i]}%")

#########################################################################################################################################################################
#    In case the probability of the most likely archetype is greater than 50%, 
#    the app will display the most probable archetype with its image and description on the left side of the screen,
#    and the other top 2 archetypes with their probabilities on the right side of the screen.
#########################################################################################################################################################################

            else:
                col1, col2 = st.columns([3,7])
                with col1:
                    st.image(archetype_descriptions[highest_probability_archetype]["image"], use_column_width=True)
                with col2:
                    st.success(f"##### Identified Archetype: {highest_probability_archetype} \n\n Match: **{highest_probability}%**. ✅ \n\n {archetype_descriptions[highest_probability_archetype]['description']}")
                    
                    # Display the other top 2 archetypes
                    col3, col4 = st.columns([1,1])
                    for i in range(1, 3):
                        with (col3 if i == 1 else col4):
                            if top_3_probabilities[i] < 20:
                                st.error(f"Identified Archetype {i+1}:\n\n {top_3_archetypes[i]} \n\n Match: {top_3_probabilities[i]}%")
                            elif 20 <= top_3_probabilities[i] <= 50:
                                st.warning(f"Identified Archetype {i+1}:\n\n {top_3_archetypes[i]} \n\n Match: {top_3_probabilities[i]}%")
                            else:
                                st.success(f"Identified Archetype {i+1}:\n\n {top_3_archetypes[i]} \n\n Match: {top_3_probabilities[i]}%")



               
