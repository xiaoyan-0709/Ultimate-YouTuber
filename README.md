# Ultimate-YouTuber

This is a folder for data/model files for the Ultimate-Youtuber project. 
This folder includes four part: 
(1)	youtube videos data containing information such as title, views number, likes number, dislikes number, description and comments. Dataset files contain data from USA videos, and Canada videos, names are “ca1.csv”, “ca2.csv”, “ca3.csv”, “us1.csv”, “us3.csv”, “us3.csv”.

(2)	Overview notebook: (a) EDA: Exploratory Data Analysis, explore correlation between each factor. (b) Data Cleaning part (Saved cleaned data called “new_data3”). (c) NLP/modeling part for whole dataset without separate by categories of videos. 

(3)	Separate NLP/modeling part for each category of videos. For each category of videos, we trained separate model on both titles and descriptions, and saved as sav pickle file. 

(4)	Pickle files: pipeline: divide training and test set, use CountVectorizer(), TfidfTransformer(), RandomForestClassifier().We did NLP model separately for “title” and “descriptions”, our main independent variables. Because we have 14 categories, so in total we have 28 Pickle files for 28 models. Names of pickle models are: “df_1_d.sav”, “df_1_t.sav”, “df_2_d.sav”, “df_2_t.sav”, …, “df_28_d.sav”, “df_28_t.sav”.

(5)	UI: “UI.py”: the procedure to run UI file is to download streamlit package. 
•	Put UI.py under cd directory
•	“streamlit run UI.py” in terminal




