import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk
from sklearn.cluster import KMeans
#import random

myData = 'TEST.xlsx'
AIMov = pd.DataFrame(data=None, index=range(5), columns=range(7))

try:
    MAINMOV = pd.read_excel(myData)
    movies = MAINMOV
    #randIndices = random.sample(range(0,len(movies)),5) Perfect Storm, 
    AIMov = movies.sample(n=5)#grabs a random qset of 7 features
    #Acts as an AI model in order to calculate 5 'favorite movies'
    movies.head(print(MAINMOV))
    nextSample = movies.sample(n=10)#test for another data frame
    kVal = 4 #value to be deduced later?

    print(AIMov)
    print("End of Program")

except Exception as e:
    print(f"Something went wrong...{e}")

