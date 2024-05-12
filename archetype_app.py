from Archetype_Model import archetype_prediction
from Archetype_Descriptions import archetype_descriptions
import streamlit as st

st.set_page_config(page_title="Archetype App", page_icon="https://upload.wikimedia.org/wikipedia/commons/7/7d/Abawikilogo.png", layout="centered", initial_sidebar_state="collapsed")

st.image('https://upload.wikimedia.org/wikipedia/commons/7/7d/Abawikilogo.png', width=80)
#developed by 
st.write('Developed by Business Intelligence | Marketing Analytics Team')
st.title('Archetype App')


# Get tagline input from the user
tagline = st.text_input('Enter Tagline', placeholder='Defending Liberty Pursuing Justice')

if st.button('Predict Archetype'):
    if tagline == '':
        st.warning('Please enter a tagline to identify the archetype.⚠️')
    elif tagline != '':
        top_3_archetypes, top_3_probabilities = archetype_prediction(tagline)

        # Check if the highest probability is less than 15
        if top_3_probabilities[0] < 15:
            st.info("This text does not match any archetype  ⚠️")
        else:
            # Display the most probable archetype and its description
            highest_probability_archetype = top_3_archetypes[0]
            highest_probability = top_3_probabilities[0]
            if highest_probability < 20:
                st.error(f"Identified Archetype: {highest_probability_archetype}, Probability: {highest_probability}%  ❓")
            elif 20 <= highest_probability <= 50:
                st.warning(f"Identified Archetype: {highest_probability_archetype}, Probability: {highest_probability}% ⚠️")

            else:
                col1, col2 = st.columns([3,7])
                with col1:
                    st.image(archetype_descriptions[highest_probability_archetype]["image"], use_column_width=True)
                with col2:
                    st.success(f"##### Identified Archetype: {highest_probability_archetype} \n\n Probability: **{highest_probability}%**. ✅ \n\n {archetype_descriptions[highest_probability_archetype]['description']}")
                    
                    # Display the other top 2 archetypes
                    col3, col4 = st.columns([1,1])
                    for i in range(1, 3):
                        with (col3 if i == 1 else col4):
                            if top_3_probabilities[i] < 20:
                                st.error(f"Identified Archetype {i+1}:\n\n {top_3_archetypes[i]} \n\n Probability: {top_3_probabilities[i]}%")
                            elif 20 <= top_3_probabilities[i] <= 50:
                                st.warning(f"Identified Archetype {i+1}:\n\n {top_3_archetypes[i]} \n\n Probability: {top_3_probabilities[i]}%")
                            else:
                                st.success(f"Identified Archetype {i+1}:\n\n {top_3_archetypes[i]} \n\n Probability: {top_3_probabilities[i]}%")

                