import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class SemanticRetriever():

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.content = []

    def embed_text(self,text):
        embedded_text = self.model.encode(text)
        return(embedded_text)

    def cosine_similar(self,vector1):
        max_Score = 0.0
        vector1 = vector1.reshape(1, -1)  # Becomes [[0.1, 0.2, 0.3, ...]]
        output = ""
        #vector2.reshape(1, -1)  # Becomes [[0.2, 0.1, 0.4, ...]]
        for values in self.content:
            vector2 = values[1]
            vector2 = vector2.reshape(1, -1)
            final = cosine_similarity(vector1,vector2)
            if (final[0][0])*100> max_Score:
                max_Score = (final[0][0])*100 
                output = (values[0],max_Score)
        return(output)
        
        

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
        





SR = SemanticRetriever()
embed_text = SR.embed_text("what is ai")
document  = SR.load_and_embed_documents()
similarity = SR.cosine_similar(embed_text)
