#Kevin Moncada
#DATA 200
#Final Project- Part II
#13 December 2024
import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

#this method converts the categories except the titles into numerical values for the kmeans algorithm
def get_kmeans(df: pd.DataFrame,x: int, y: int, k: int):
    le = LabelEncoder()
    #converts the dataframe from strings to integers to use in kmeans
    for column in ["Genre", "Production Studio", "Year", "Rating", "Theme", "Cinematic Style"]:
        df[column] = le.fit_transform(df[column])
    temp = df.drop(columns=["Movie Title"])

    #executes the kmeans algorithm
    kmeans = KMeans(n_clusters=k, random_state=0, n_init="auto").fit(temp[[x,y]])
    centers = kmeans.cluster_centers_
    labels = kmeans.labels_
    df['k-means'] = labels #adds the kmean labels to the dataset
    return df #returns the converted dataset

#   Plot the clusters in 2D. A general graph of the data with k clusters
def plot(df: pd.DataFrame,x: int, y: int):
    plt.figure(figsize=(6, 8))
    plt.scatter(df[x], df[y], c=df['k-means'], cmap='plasma', label=df['k-means'], s=100)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title("The Plot of " + x +" versus "+ y)
    #plt.colorbar(label=df['k-means']) 
    plt.show()

#   MainFunction 
def main():
    myData = 'Data_TEST.xlsx'#Movie Dataset

    try:
        movies= pd.read_excel(myData, header = 0)
        MAINAI = movies.copy(deep=True) #immutable copy of movies

        x_val = 'Rating' #Preset Variables
        y_val = 'Production Studio'
        k_val = 5  #number of clusters
        n_val = 5 #number of movies
        
        print("This is a 2 part python program that focuses on \n1. finding the k-means of the movie dataset and \n2. Finds recommended movies using the kmeans value")
        print("DISCLAIMER: The program assumes all input values are perfect.")
        user_input = input("\nDo you want to continue? (y/n):\t")

        if user_input.lower() == 'y':
            user_input = input("\nPart 1:\tK-Means\nInput the amount of clusters to be used.\t")
            k_val = int(user_input) #user inputted cluster value

            print("Possible values: 'Genre', 'Production Studio', 'Year', 'Rating', 'Theme', 'Cinematic Style'")
            user_input = input("\nPlease enter the value for the x-axis.\t")
            x_val = user_input

            user_input = input("Please enter the value for the y-axis.\t")
            x_val = user_input

            movies = get_kmeans(movies,x_val,y_val,k_val)#calls the method and gets the k-means*
            #Plot the clusters in 2D. A general graph of the data with k clusters
            
            user_input = input("\nK-means has been calculated. Do you want to display the plot from the k-means algorithm (y/n):\t")
            if user_input.lower() == 'y':
                plot(movies,x_val,y_val)  
            
            user_input = input("\n\n\nPart 2: Movie Recommendations\nPress ENTER to continue:\t")

            ai_Mov = movies.sample(n=n_val)
            #finds the most common cluster in the chosen dataset
            print("\nThese are your selected favorite movies:\n")    
            print(ai_Mov['Movie Title'])

            user_input = input("Press ENTER to continue:\t")

            print("\nNow finding the best movies to watch based on the common k-means value within your selection")
            movies = movies[movies['k-means'] == max(ai_Mov["k-means"])]#most common cluster value

            user_input = input("Do you want to display the value of the cluster your movies mostly share? (y/n):\t")
            if user_input.lower() == 'y':
                print("The most common cluster value was\t" + str(max(ai_Mov["k-means"])))
                user_input = input("\nPress ENTER to continue:\t")

            for title in ai_Mov['Movie Title']:
                movies = movies[movies['Movie Title'] != title]

            if len(movies) >= n_val:
                ai_Mov = movies.sample(n_val, replace=False)#gets new movies while avoiding duplicates
            else:
                print('There are not enough movies in the cluster. Try another cluster value')

            print("\nHere are a list of five movies that you may enjoy, based on your preferences and k-means.")
            print(ai_Mov['Movie Title'])#final list of recommended movies
            print("\nEnd of Program")
        
        else:
            print("Program Terminated.")

    except Exception as e:
        print(f"\nAn Error has occured.\n{e}")

if __name__ == "__main__":
    main()
