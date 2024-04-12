# G2_PS_2 Solution Team Prisase

# Problem Statement
G2_PS_2 aims to address the challenge of analyzing customer reviews from G2 Marketing solutions and extracting the feature sets that customers are looking for. With over 2.5 million reviews, identifying key features from this data can significantly benefit buyers and software vendors in decision-making processes.

# Solution Overview
# Data Collection and Preprocessing
- Utilized the G2 API to fetch reviews of G2 Marketing solutions in batches of 100.
- Stored the fetched data into a CSV file named survey_responses.csv.
- **Preprocessed the data**:
  - Extracted relevant columns: id, hate, love. (As a Dataframe)
  - Removed stopwords, punctuation, and special characters from the hate column. (using nltk module and then the result is stored in an intermediate csv file)
  - Filtered out positive sentiments from the hate column to focus on areas of improvement or customer issues. (using textblob we have done sentimental analysis)
# Feature Extraction
- Identified the most common adjective from the love column and stored it in a love_key.csv file.(for keyword searches)
- Conducted **part-of-speech(POS)** tagging to extract singular and plural nouns.
- We extract the **Hyphenated Adjective-Noun, Verb-Noun, Noun-Noun Compound, Proper Noun followed by a common noun, Proper Noun followed by a common noun, Adjective-Noun Pairing**.
- Performed two-word feature extraction for better understanding.
- Pruned irrelevant features and nouns.
- Categorized extracted features into 8 different categories: **ROI, Social, Information, Affordability, Pages, Needs, Security, Technical**.
- Extracted top features and stored them in result.csv.
# User Interface
- Developed a user-friendly React application named **g2_ps_2**.
 ![image](https://github.com/samarth0104/G2_Prisase/assets/144517774/8ac54b67-00f2-46eb-b6d1-e0efe2b38dd0)
_
 ![image](https://github.com/samarth0104/G2_Prisase/assets/144517774/b97062df-2ae3-46e8-8fd4-f727dd5c0bde)
_
 ![image](https://github.com/samarth0104/G2_Prisase/assets/144517774/803f3885-8101-49a7-a1fa-2aebaf4370a9)
# Components:
- **Feature.js**: Displays top features of each category and associated reviews for better understanding.
- **Review.js**: Shows the first 3 top-rated reviews of G2 Marketing Solutions with a nice UI.
- **PieChart.js**: Generates a pie chart representing the percentage of positive, neutral, and negative reviews.
- **Statistics.js**: Gives a Rating Bar and allows searching for reviews based on keywords and also has 10 inbuilt keyword buttons(which are adjectives).
- **App.js**: Main page that handles all components.
# Dependencies
- Utilized various Python libraries including Pandas, NLTK, Ast, TextBlob, Itertools, and Re.
- All the csv files are read using  PapaParse and Fetch method  in the React application.
# How to Run
- Update the paths for loading components in Feature.js and Review.js to match your local directory.
- The below 3 paths have to be changed:
- Feature.js:
  - **import Data from 'C:/Users/samar/OneDrive/Desktop/PESU/Extra/G2/g2_ps_2/src/csv_files/result.csv';**
  - **import SurveyData from 'C:/Users/samar/OneDrive/Desktop/PESU/Extra/G2/g2_ps_2/src/csv_files//survey_responses.csv'**
- Review.js:
  - **import anonImage from 'C:/Users/samar/OneDrive/Desktop/PESU/Extra/G2/g2_ps_2/src/images/anon.jpg'**
- Make sure the paths are correct.
- Few dependencies to be installed before running:
  - **npm install react-scripts --save-dev**
  - **npm install papaparse**
  - **npm install @mui/material @emotion/react @emotion/styled**
- Navigate to the g2_ps_2 directory using the command **cd g2_ps_2**.
- Run the React application using **npm start**.
# Note
- Ensure all dependencies are installed and paths are correctly configured before running the code.
- There are two sets of codes saved in two different way, one is the **g2_v3.ipynb** and the second is the folder **python_codes**. 
- Both the things have same code and python_code has some extra codes for formatting or rearranging the csv files. 
- The css of the React App might change because of **laptop screen size** because we have used the **"px"** instead of **"%"** for all the dimensions of div box(**requires 15.6inch laptop for proper css**). 

