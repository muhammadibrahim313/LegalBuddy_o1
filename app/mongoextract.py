import pymongo
from sentence_transformers import SentenceTransformer
import numpy as np
import json
import streamlit as st
import os

def get_mongodb_data(query, top_k=4):
    # Connect to MongoDB
    client = pymongo.MongoClient(st.secrets["MONGODB_URI"])
    db = client["legelcase"]
    collection = db["casebuddy"]

    # Load the embedding model
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    # Function to search MongoDB
    def search_mongodb(query, top_k=3):
        # Generate embedding for the query
        query_embedding = model.encode([query])[0]

        # Perform vector search
        pipeline = [
            {
                "$vectorSearch": {
                    "index": "vector_index",
                    "path": "embedding",
                    "queryVector": query_embedding.tolist(),
                    "numCandidates": 100,
                    "limit": top_k
                }
            },
            {
                "$project": {
                    "text": 1,
                    "metadata": 1
                }
            }
        ]

        results = list(collection.aggregate(pipeline))
        return results

    # Perform a search
    search_results = search_mongodb(query, top_k)

    # Format the results
    formatted_results = [f"This is my case:'{query}'\n Past CASE Laws:"]
    for i, result in enumerate(search_results, 1):
        formatted_results.append(f"Case Law {i}:\n{result.get('text', 'No text available')}\n")

    # Close the MongoDB connection
    client.close()
    print("results from mongo:",formatted_results)
    return "\n".join(formatted_results)

# Example usage (commented out)
# if __name__ == "__main__":
#     query = """A liability analysis report assesses a personal injury claim filed by an individual who alleges tripping over a hose at a business establishment, resulting in serious injuries. The report evaluates the claim's merits, considering factors such as duty of care, breach of duty, causation, damages, and pre-existing conditions. The analysis highlights discrepancies in the claimant's account, lack of corroborating evidence, and the presence of significant pre-existing medical conditions, which complicate the claim."""
#     result = get_mongodb_data(query)
#     print(result)