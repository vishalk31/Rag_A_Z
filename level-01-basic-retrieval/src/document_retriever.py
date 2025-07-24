import os



def load_documents():
    content = []
    current_dir = os.path.dirname(os.path.abspath(__file__))
    documents_dir = os.path.abspath(os.path.join(current_dir, '..', 'documents'))
    document_path = os.listdir(documents_dir)
    docments =  [os.path.join(documents_dir,files) for files in document_path]
    
    for files in docments:
        with open(files,mode="r") as f:
            content_data = f.read()
            content.append((files,preprocess_text(content_data)))
    return(content)


def preprocess_text(content):
    stop_words = ["!","@","#","$","%","^","&","*","(",")","{","}","the", "and", "is"]
    for words in stop_words:
        content=content.replace(words,"")
    content = content.lower()
    content =content.split(" ")
    content =[data for data in content if len(data)>1]
    return(content)

def similarity (prompt,database_Content):
    #prompt_preprocessed = preprocess_text(prompt)
    max_score = 0
    output = ()
    for data in database_Content:
        matching_data_len = len([prompt_sep for prompt_sep in prompt if prompt_sep in data[1]])
        matching_score = matching_data_len/len(data[1])
        if matching_score>max_score:
            max_score = matching_score
            output = (data[0],data[1],max_score*100)
    return(output)
            
        
        
        
def retrieve(query):
    print("content given for vector search : ",query)
    query = preprocess_text(query)
    print("Cleaned content for vector search : ", query)
    similary_match = similarity(query,load_documents())
    print("matched_result : ",similary_match)
    return(similary_match)
    

content = load_documents()
print(retrieve("What is artificial intelligence?"))
print(retrieve("Cooking brings together science?"))
print(retrieve("Tell me about space exploration"))

        
    
