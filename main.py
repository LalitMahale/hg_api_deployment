from utils.vector_store import VectorStore
from utils.convert_embedding import GetEmbedding
import pandas as pd
import pickle
import random 
import numpy

# df = pd.read_csv(r"C:\Users\akrivia\Downloads\main.csv")
# df.answer = df.answer.map(lambda x : [x])

# # question = df.question.tolist()
# answer = df.answer.tolist()
# with open("answer.pkl","wb") as f:
#     pickle.dump(answer,f)

# vector_store = VectorStore().store_vectors(data=question)

def process(query):
    with open("answer.pkl","rb") as f:
        data = pickle.load(f)

    print(len(data))

    result = VectorStore().get_similary_search(query=query)

    print("Result ",result)

    print(data[result[0][0]])

def final_output(query):
    with open("answer.pkl","rb") as f:
        data = pickle.load(f)

    print(len(data))

    result = VectorStore().get_similary_search(query=query)

    print("Result ",result)

    result = data[result[0][0]]

    return random.choice(result)


if __name__ == "__main__":
    process(query = "What is your experience with computer vision?")