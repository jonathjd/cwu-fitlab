 # Central Washington University Fitlab

Cwu-Fitlab is a full stack web application created for the upper level practicum fitlab. CWU FitLab is a comprehensive fitness assessment experience provided by trained CWU students pursuing a degree in Exercise Science. This application makes it easier to manage client scheduling, track client progress over time, and provide access to client assessment data.

Link to application: https://cwu-fitlab.streamlit.app/

![fitlab-img](https://user-images.githubusercontent.com/66283742/215290444-fe8bf3c0-a421-4cca-bdda-af77c0356243.png)

# How it's Made:
**Tech Used:** Python (Streamlit), GCP Firestore, Some injected HTML and CSS (lol)



![alt-text](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)


Fitlab is a great culminating experience for undergraduate students at CWU, however, it has always been plagued with scheduling issues, waning participation rates, and a subpar client experience with regard to data access. There are a few things that we've found increased participation rates quarter after quarter that being ease of scheduling (no going back and forth over email), as well as being able to track client progress over time. These were the two main issues that this application was aiming to solve. Scheduling, by providing a dedicated calendly link on the sidebar of the home page with all available times, and tracking client progress by allowing the clients to access their results from past visits via a dashboard on the Dasboard page.

Streamlit was for the front end for rapid development time and ease of use. GCP firestore was used for the database because of it's NoSQL schema, and ease of use for the GUI. This would allow students to be rapidly training on how to manaully remove erroneous data or client information if need be. Another reason Streamlit was used is for the easy deployment via Streamlit's hosting services, although Heroku and GCP were also considered for hosting.

# Optimizations

Many of the visualizations rely on (relatively) large NHANES datasets that were cleaned and visualized via plotly. Due to the nature of Streamlit running the script each time a widget is interacted with by the user, this dataset is reuploaded from Github each time a slider is adjusted, or text is interacted with. This makes the application slow to run and cumbersome. To overcome this the dataset is fetched and cached at the beginning of the script.

Another optimization that is currently under development is the fetching of the client data from the Firebase backend. Currently the data is fetched once the client enters in their client ID and stored in a dictionary where the values can be accessed. However this makes visualizing the clients progress over time difficult as these values are also stored as a string datatype. To optimize this process the clients data will be fetched, stored as a pandas DataFrame, and cached. This will make it much easier to visualize, and download to a csv if the client so chooses. 

# Lessons Learned

1. A big lesson that I learned was how important it is to plan out the db schema before implementation of the database backend. Keeping in mind scaling the application is critical so that refactoring is kept to a minimum. 
2. Another lesson learned was that this is a deployed application and that downtime must be minimized so that the user experience is seamless. 
3. Finally, importing helper functions from another script makes debugging much easier down the road.
