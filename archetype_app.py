from Archetype_Model import archetype_prediction
import streamlit as st

st.set_page_config(page_title="Archetype App", page_icon="https://upload.wikimedia.org/wikipedia/commons/7/7d/Abawikilogo.png", layout="centered", initial_sidebar_state="collapsed")

st.image('https://upload.wikimedia.org/wikipedia/commons/7/7d/Abawikilogo.png', width=80)
#developed by 
st.write('Developed by Business Intelligence | Marketing Analytics Team')
st.title('Archetype App')

archetype_descriptions = {
    "Innocent": {
        "description": "Texts are characterized by an uplifting, optimistic tone that speaks to simplicity and purity. Language is straightforward, avoiding complexities or cynicism, promoting an idealistic and trouble-free world that appeals to a sense of nostalgia and comfort.",
        "image": "images/Innocent.png"
    },
    "Everyday": {
        "description": "The language is conversational, friendly, and approachable, with an emphasis on building community and belonging. It employs colloquialisms and a familiar tone to create a sense of connection and relatability, appealing to common, everyday values.",
        "image": "images/Everyman.png"
    },
    "Everyman": {
        "description": "The language is conversational, friendly, and approachable, with an emphasis on building community and belonging. It employs colloquialisms and a familiar tone to create a sense of connection and relatability, appealing to common, everyday values.",
        "image": "images/Everyman.png"
    },
    "Hero": {
        "description": "Characterized by an inspiring, bold narrative that encourages action and resilience. Language is strong, decisive, and often uses metaphors of battle or achievement. It emphasizes courage and proactive behavior in overcoming challenges and adversity.",
        "image": "images/Hero.png"
    },
    "Outlaw": {
        "description": "Texts challenge the status quo and embrace rebellion, using provocative or confrontational language that appeals to a sense of freedom and non-conformity. It often advocates for breaking rules, defying traditional norms, and revolutionary change.",
        "image": "images/Outlaw.png"
    },
    "Explorer": {
        "description": "Focused on adventure and discovery, the language used is vivid, detailed, and curious, often describing journeys, explorations, and new experiences. It promotes a sense of wanderlust and the thrill of breaking new ground or venturing into the unknown.",
        "image": "images/Explorer.png"
    },
    "Creator": {
        "description": "Innovative and artistic, the text emphasizes creativity, imagination, and the process of creation. Language is often poetic, filled with metaphors about crafting and designing, and aims to inspire others to think differently and embrace originality.",
        "image": "images/Creator.png"
    },
    "Ruler": {
        "description": "Exudes authority and control, with a language that is formal, commanding, and polished. It often relates to themes of power, stability, and leadership, promoting an image of luxury and exclusivity that appeals to an elite audience.",
        "image": "images/Ruler.png"
    },
    "Magician": {
        "description": "Uses mystical or visionary language that is enchanting and rich with imagery of transformation and magical outcomes. Texts often speak of dreams coming true, the impossible being made possible, and the mystical elements that evoke wonder and curiosity.",
        "image": "images/Magician.png"
    },
    "Lover": {
        "description": "Evocative and emotive, focusing on themes of passion, pleasure, and intimacy. The language is rich, sensory, and detailed, aiming to connect deeply with the reader's emotions and desires, often promoting beauty, love, and relationships.",
        "image": "images/Lover.png"
    },
    "Caregiver": {
        "description": "Compassionate and nurturing, with a warm, supportive language that emphasizes safety, care, and reliability. It appeals to the reader's sense of empathy and altruism, often focused on providing help and comfort to others in a gentle and reassuring tone.",
        "image": "images/Caregiver.png"
    },
    "Jester": {
        "description": "Light-hearted and humorous, using witty, playful language that includes puns, jokes, and a cheerful tone. It aims to entertain and amuse, providing a respite from serious or mundane aspects of life, often through clever and unexpected twists in the narrative.",
        "image": "images/Jester.png"
    },
    "Sage": {
        "description": "Wise and knowledgeable, characterized by a use of factual, insightful language that seeks to educate and provide clarity. It appeals to the reader's intellect, offering expert advice, analysis, or explanations that help make sense of complex topics or data.",
        "image": "images/Sage.png"
    }
}



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

                
