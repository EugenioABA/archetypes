# this is the code for the model that predicts the archetype of a tagline.
#after saving the model, it can be loaded and used to predict the archetype of a new tagline without needing to retrain the model!

# def archetype_prediction(tagline): # tagline is the new tagline that we want to predict the archetype for
#     import joblib # joblib is used to save and load the model
#     # Load the saved model
#     loaded_model = joblib.load("archetype_classifier.pkl") # this should be the exact path where the model is saved, unless it is in the current working directory. 
#     # Predict the archetype for the new tagline
#     probabilities = loaded_model.predict_proba([tagline]) # predict the probabilities of each archetype for the new tagline
#     class_labels = loaded_model.classes_ # get the class labels of the model
#     predicted_archetype = loaded_model.predict([tagline]) # predict the archetype of the new tagline
#     probability = round(probabilities[0][list(class_labels).index(predicted_archetype[0])],2)*100
#      # return the predicted archetype and the probabilities pf the most likely archetype
#     #if the probability is less than 20%, assigned archetype as "Undefined"
#     if probability < 20:
#         return "Undefined", "This text lacks character 100"
#     else:
#         return predicted_archetype[0], probability
def archetype_prediction(tagline):
    import joblib
    loaded_model = joblib.load("archetype_classifier.pkl")
    probabilities = loaded_model.predict_proba([tagline])[0]
    class_labels = loaded_model.classes_

    # Pair each class label with its corresponding probability
    pairs = list(zip(class_labels, probabilities))

    # Sort the pairs in descending order of probability
    sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)

    # Get the top 3 pairs
    top_3_pairs = sorted_pairs[:3]

    # Extract the class labels and probabilities from the top 3 pairs
    top_3_archetypes = [pair[0] for pair in top_3_pairs]
    top_3_probabilities = [round(pair[1]*100, 2) for pair in top_3_pairs]

    return top_3_archetypes, top_3_probabilities