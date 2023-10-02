# Sentiment-Analysis-on-IMDB-reviews-with-Machine-Learning
* In this project, I built classical Machine Learning models that trains on data about IMDB reviews which are classified as positive or negative.
* Then I compared the models performance to find the best one.
* I then exported that model using pickle.
* Finally, I made a simple UI with streamlit to provide an interface to allow users to insert text and classify them.

The models I created are: MultinominalNB, LogisticRegression, KNeighborsClassifier and RandomForestClassifier

After evaluation, Logistic Regression emerged to be the best performing model with cross validation score of 86.74%

Tools used: Python, Pandas, Matplotlib, Scikit Learn, NLTK, Pickle, Streamlit

## This is how my app looks:
![ui](https://github.com/gurung-ajay/Sentiment-Analysis-on-IMDB-reviews-with-Machine-Learning/assets/135496373/2324d7ff-0379-493e-94ee-bd20baebf329)
When you enter the movie review in the text box and press the button 'Analyze Sentiment', it will print whether the review is positive or negative.


![prediction](https://github.com/gurung-ajay/Sentiment-Analysis-on-IMDB-reviews-with-Machine-Learning/assets/135496373/d44db32b-7271-4ea1-8e10-27ef6b00f6ed)

## To run the streamplit app:
* Download the pickle file and ui.py and put them in same folder.
* Open the folder with compiler like VisualStudioCode.
* Now open ui.py from the directory.
* Open the terminal and type: streamlit run ui.py
* You will see that the terminal will give you an ip address. Copy the ip address and run it in your browser. It should open the UI.



