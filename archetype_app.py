from Archetype_Model import archetype_prediction
import streamlit as st

st.set_page_config(page_title="Archetype App", page_icon="https://upload.wikimedia.org/wikipedia/commons/7/7d/Abawikilogo.png", layout="centered", initial_sidebar_state="collapsed")

st.image('https://upload.wikimedia.org/wikipedia/commons/7/7d/Abawikilogo.png', width=80)
#developed by 
st.write('Developed by Business Intelligence | Marketing Analytics Team')
st.title('Archetype App')


archetype_descriptions = {
    "Innocent": "Texts are characterized by an uplifting, optimistic tone that speaks to simplicity and purity. Language is straightforward, avoiding complexities or cynicism, promoting an idealistic and trouble-free world that appeals to a sense of nostalgia and comfort.",
    "Everyday": "The language is conversational, friendly, and approachable, with an emphasis on building community and belonging. It employs colloquialisms and a familiar tone to create a sense of connection and relatability, appealing to common, everyday values.",
    "Hero": "Characterized by an inspiring, bold narrative that encourages action and resilience. Language is strong, decisive, and often uses metaphors of battle or achievement. It emphasizes courage and proactive behavior in overcoming challenges and adversity.",
    "Outlaw": "Texts challenge the status quo and embrace rebellion, using provocative or confrontational language that appeals to a sense of freedom and non-conformity. It often advocates for breaking rules, defying traditional norms, and revolutionary change.",
    "Explorer": "Focused on adventure and discovery, the language used is vivid, detailed, and curious, often describing journeys, explorations, and new experiences. It promotes a sense of wanderlust and the thrill of breaking new ground or venturing into the unknown.",
    "Creator": "Innovative and artistic, the text emphasizes creativity, imagination, and the process of creation. Language is often poetic, filled with metaphors about crafting and designing, and aims to inspire others to think differently and embrace originality.",
    "Ruler": "Exudes authority and control, with a language that is formal, commanding, and polished. It often relates to themes of power, stability, and leadership, promoting an image of luxury and exclusivity that appeals to an elite audience.",
    "Magician": "Uses mystical or visionary language that is enchanting and rich with imagery of transformation and magical outcomes. Texts often speak of dreams coming true, the impossible being made possible, and the mystical elements that evoke wonder and curiosity.",
    "Lover": "Evocative and emotive, focusing on themes of passion, pleasure, and intimacy. The language is rich, sensory, and detailed, aiming to connect deeply with the reader's emotions and desires, often promoting beauty, love, and relationships.",
    "Caregiver": "Compassionate and nurturing, with a warm, supportive language that emphasizes safety, care, and reliability. It appeals to the reader's sense of empathy and altruism, often focused on providing help and comfort to others in a gentle and reassuring tone.",
    "Jester": "Light-hearted and humorous, using witty, playful language that includes puns, jokes, and a cheerful tone. It aims to entertain and amuse, providing a respite from serious or mundane aspects of life, often through clever and unexpected twists in the narrative.",
    "Sage": "Wise and knowledgeable, characterized by a use of factual, insightful language that seeks to educate and provide clarity. It appeals to the reader's intellect, offering expert advice, analysis, or explanations that help make sense of complex topics or data."
}

# Get tagline input from the user
tagline = st.text_input('Enter Tagline', placeholder='Defending Liberty Pursuing Justice')

# Predict the archetype for the tagline
# if st.button('Predict Archetype'):
#     if tagline == '':
#         st.warning('Please enter a tagline to identify the archetype.')
#     elif tagline != '':
#         top_3_archetypes, top_3_probabilities = archetype_prediction(tagline)

#         # Display the most probable archetype and its description
#         highest_probability_archetype = top_3_archetypes[0]
#         highest_probability = top_3_probabilities[0]
#         if highest_probability < 20:
#             st.error(f"Identified Archetype: {highest_probability_archetype}, Probability: {highest_probability}%")
#         elif 20 <= highest_probability <= 50:
#             st.warning(f"Identified Archetype: {highest_probability_archetype}, Probability: {highest_probability}%")
#         else:
#             st.success(f"Identified Archetype: {highest_probability_archetype}, Probability: {highest_probability}%")
#         st.info(archetype_descriptions[highest_probability_archetype])

#         # Display the other top 2 archetypes
#         for i in range(1, 3):
#             if top_3_probabilities[i] < 20:
#                 st.error(f"Identified Archetype {i+1}: {top_3_archetypes[i]}, Probability: {top_3_probabilities[i]}%")
#             elif 20 <= top_3_probabilities[i] <= 50:
#                 st.warning(f"Identified Archetype {i+1}: {top_3_archetypes[i]}, Probability: {top_3_probabilities[i]}%")
#             else:
#                 st.success(f"Identified Archetype {i+1}: {top_3_archetypes[i]}, Probability: {top_3_probabilities[i]}%")


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
                st.success(f"##### Identified Archetype: {highest_probability_archetype} \n\n Probability: **{highest_probability}%**. ✅ \n\n {archetype_descriptions[highest_probability_archetype]}" )
            #st.write(archetype_descriptions[highest_probability_archetype])

            # Display the other top 2 archetypes
            for i in range(1, 3):
                if top_3_probabilities[i] < 20:
                    st.error(f"Identified Archetype {i+1}: {top_3_archetypes[i]}, Probability: {top_3_probabilities[i]}%")
                elif 20 <= top_3_probabilities[i] <= 50:
                    st.warning(f"Identified Archetype {i+1}: {top_3_archetypes[i]}, Probability: {top_3_probabilities[i]}%")
                else:
                    st.success(f"Identified Archetype {i+1}: {top_3_archetypes[i]}, Probability: {top_3_probabilities[i]}%")