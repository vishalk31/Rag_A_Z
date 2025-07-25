import os
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss


class knn_retriever():

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.content = []

    def embed_text(self,text):
        embedded_text = self.model.encode(text)
        return(embedded_text)

    def create_faiss_index(self):
    	dimension = 384  # Our embedding size
    	# Create FAISS index for cosine similarity
    	self.index = faiss.IndexFlatIP(dimension)
    	return self.index

    def add_documents_to_index(self):
        embeddings = []
        filenames = []
        for filename, embedding in self.content:
            embeddings.append(embedding)
            filenames.append(filename)
    
        # Convert to numpy array for FAISS
        embeddings_array = np.array(embeddings).astype('float32')
    
        # Add to FAISS index
        self.index.add(embeddings_array)
    
        # Store filenames for later retrieval
        self.filenames = filenames
  

    def knn_search(self, query, k=1):
        embedded_text = self.model.encode(query)
        query_array = np.array(embedded_text).astype("float32")  # Fix: embedded_text not embedding
        query_vector = query_array.reshape(1, -1)  # Fix: Need to reshape for FAISS
        scores, indices = self.index.search(query_vector, k)  # Fix: query_vector not query_vector
        return(float(scores[0][0]), int(indices[0][0]),self.filenames[int(indices[0][0])])
        #return (self.filenames[indices[0]], scores)  # Fix: Use filenames not content
         
        

    def load_and_embed_documents(self):
        #content = []
        current_dir = os.path.dirname(os.path.abspath(__file__))
        documents_dir = os.path.abspath(os.path.join(current_dir, '..', 'documents'))
        document_path = os.listdir(documents_dir)
        docments =  [os.path.join(documents_dir,files) for files in document_path]
        for files in docments:
            with open(files,mode="r") as f:
                content_data = f.read()
                self.content.append((files, self.embed_text(content_data)))
        return(self.content)
        





KR = knn_retriever()
KR.create_faiss_index()  # Create index first
document = KR.load_and_embed_documents()  # Load documents
KR.add_documents_to_index()  # Add to index
result = KR.knn_search("where is my pasta", k=1)  # Search
print(result)
