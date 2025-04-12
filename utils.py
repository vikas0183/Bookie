import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

pt = pd.read_json("front_end_data/Book_vectors_for_reccomend.json")
similarities = cosine_similarity(pt)

def get_top_20_Books():
    df = pd.read_json("front_end_data/Master_average_data.json")
    top_20 = df.head(20)
    return top_20

def get_book_names():
    df = pd.read_json("../front_end_data/Master_Book_Vectors.json")
    return df
    pass


def recommend(book_name):
    books_list = []
    if book_name in pt.index:
        index = np.where(pt.index == book_name)[0][0]
        similar_books_list = sorted(
            list(enumerate(similarities[index])), key=lambda x: x[1], reverse=True)[1:11]

        print(f'Recommendations for the book {book_name}:')
        print('-' * 5)
        for book in similar_books_list:
            # print(pt.index[book[0]])
            books_list.append(pt.index[book[0]])
        print('\n')
        return books_list

    else:
        print('Book Not Found')
        print('\n')
        return books_list

def add_to_cart():
    print("In The cart")


if __name__ == "__main__":
    print(recommend("Harry Potter and the Goblet of Fire (Book 4)"))