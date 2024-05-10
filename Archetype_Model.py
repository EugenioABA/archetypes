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
