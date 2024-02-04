# Sentiment-Analysis-on-IMDB-reviews-with-Machine-Learning
In this project, I developed classical Machine Learning models designed to analyze IMDB reviews, categorizing them as either positive or negative sentiments. Subsequently, a comprehensive performance comparison was conducted among the models, revealing Logistic Regression as the top-performing model with a notable cross-validation score of 86.74%. The chosen model was serialized using Pickle for seamless integration and deployment. The project culminated in the creation of a user-friendly interface using Streamlit, providing users with the capability to input text and receive sentiment classifications.

Key Models: Multinomial Naive Bayes, Logistic Regression, KNeighbors Classifier, RandomForest Classifier

Technologies Utilized: Python, Pandas, Matplotlib, Scikit Learn, NLTK, Pickle, Streamlit

## UI:
![qlkf8xe5](https://github.com/gurung-ajay/Sentiment-Analysis-on-IMDB-reviews-with-Machine-Learning/assets/135496373/071c9470-37f2-4831-b1f9-3ed4283d3892)
When the user enters the movie review in the text box and press the button 'Analyze Sentiment', it will print whether the review is positive or negative.


![xg8p5mro](https://github.com/gurung-ajay/Sentiment-Analysis-on-IMDB-reviews-with-Machine-Learning/assets/135496373/ecef0e8c-7d66-44be-91c0-2baf8e377acd)
![66nczmer](https://github.com/gurung-ajay/Sentiment-Analysis-on-IMDB-reviews-with-Machine-Learning/assets/135496373/d5bfe85f-299d-4ac0-aefc-79c1e5dbdbac)


## To run the streamplit app:
Prerequisites: Ensure that you have the Python libraries NLTK, Pickle, and Streamlit installed on your device.

To run the Streamlit app:

* Download the pickle file and 'ui.py', placing them in the same folder.
* Open the folder directory using the command prompt (cmd).
* Enter the command 'streamlit run ui.py'.
* Open the generated IP address from the command prompt in your browser to access the UI.


