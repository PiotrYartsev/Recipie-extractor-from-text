from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

# Load pre-trained sentence transformer model
model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

# Sample sentences (replace with your actual recipe text)
sentences = ["KARL'S JERK CHICKEN", "4 to 6 whole Scotch bonnet peppers", 
             "Combine the peppers, scallions, garlic..."]

# Training data and corresponding labels
X_train = [
  "4 to 6 whole Scotch bonnet peppers",
  "1 thumb fresh ginger, chopped",
  "½ cup soy sauce",
  "Combine the peppers, scallions, garlic...",
  "Preheat the oven to 375 degrees Fahrenheit (190 degrees Celsius)",
  "KARL'S JERK CHICKEN",
  "Enjoy your delicious jerk chicken!",
  "Serve with rice and peas."
]

y_train = [
  "Ingredient",
  "Ingredient",
  "Ingredient",
  "Instruction",
  "Instruction",
  "Title",
  "Other",  # "Other" category for non-classifiable sentences
  "Instruction"
]

# Instantiate the vectorizer
vectorizer = TfidfVectorizer()

# Fit the vectorizer to the training data and transform
X_train_transformed = vectorizer.fit_transform(X_train)

# Instantiate the classifier
clf = SVC(kernel='linear')

# Train the classifier
clf.fit(X_train_transformed, y_train)

# Transform the sample sentences
sentences_transformed = vectorizer.transform(sentences)

# Predict the categories of the sample sentences
predictions = clf.predict(sentences_transformed)

print(predictions)