import os
from flask import Flask, request, render_template
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

app = Flask(__name__)

def init():
    global index
    persist_dir = "./storage"
    data_dir = "./data"
    if os.path.exists(persist_dir):
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        index = load_index_from_storage(storage_context)
    else:
        documents = SimpleDirectoryReader(data_dir).load_data()
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        index = GPTVectorStoreIndex.from_documents(documents, storage_context=storage_context)
        storage_context.persist(persist_dir)

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html'), 200

@app.route("/", methods=["POST"])
def form():
    global index
    query_text = request.form.get("q") 
    query_engine = index.as_query_engine()
    response = query_engine.query(str(query_text))
    return render_template('index.html', response=response, q=query_text), 200

init()