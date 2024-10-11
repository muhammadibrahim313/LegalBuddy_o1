import pymongo
from mongoextract import get_mongodb_data
import streamlit as st

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://bilal77511:Q2c8DUzehnkGGWiF@cluster0.i8m2xyz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["legelcase"]
collection = db["casebuddy"]

def test_mongoextract():
    # Test query
    test_query = "Liability in personal injury cases"
    
    #print(f"Testing get_mongodb_data with query: '{test_query}'")
    
    try:
        results = get_mongodb_data(test_query)
        print("Results:")
        print(results)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    test_mongoextract()