# Level 1: Basic Document Retrieval
**Foundation RAG Pipeline with Keyword Matching**

## 🎯 Overview
This level implements a fundamental RAG (Retrieval-Augmented Generation) system using basic keyword matching and text preprocessing. It serves as the foundation for understanding core RAG concepts before moving to advanced semantic search.

## 🏗️ What You'll Build
A simple document retrieval system that:
- Stores multiple text documents
- Processes user queries
- Finds the most relevant document using word matching
- Returns results with similarity scores

## 📁 Project Structure
level-01-basic-retrieval/
├── documents/
│   ├── ai_technology.txt
│   ├── cooking_recipes.txt
│   └── space_exploration.txt
├── src/
│   ├── document_retriever.py
│ 
└── README.md

## 🔧 Core Components

### DocumentRetriever Functions
1. **`load_documents()`** - Reads all text files from documents folder
2. **`preprocess_text()`** - Cleans text (lowercase, remove punctuation, tokenize)
3. **`similarity()`** - Calculates word overlap between query and documents
4. **`retrieve()`** - Main interface for querying the system

## 🚀 How It Works

### Step 1: Document Loading
- Scans the documents folder for .txt files
- Reads file contents and preprocesses them
- Stores documents with their processed word lists

### Step 2: Query Processing
- Takes user input (e.g., "What is artificial intelligence?")
- Applies same preprocessing as documents
- Converts query to list of clean words

### Step 3: Similarity Calculation
- Compares query words with each document's words
- Counts matching words between query and document
- Calculates similarity score: matches / total document words

### Step 4: Result Retrieval
- Finds document with highest similarity score
- Returns best matching document with confidence score
- Provides user-friendly formatted output

## 💡 Key Concepts Learned
- **Text Preprocessing**: Cleaning and tokenizing text data
- **Basic Similarity**: Word-level matching algorithms  
- **Document Storage**: File handling and data structures
- **Retrieval Pipeline**: End-to-end query processing

## 🧪 Testing
Run queries like:
- "What is artificial intelligence?" → Returns AI document
- "How to cook pasta?" → Returns cooking document
- "Tell me about space exploration" → Returns space document

## 📊 Performance Characteristics
- **Pros**: Fast, simple, interpretable
- **Cons**: No semantic understanding, exact word matches only
- **Best For**: Keyword-heavy queries, exact term matching

## 🔄 Limitations of This Approach
- Requires exact word matches (doesn't understand synonyms)
- Cannot handle semantic similarity ("car" vs "automobile")
- Sensitive to different word forms ("run" vs "running")
- No context understanding

## ➡️ Next Level Preview
Level 2 will address these limitations by introducing:
- Vector embeddings for semantic understanding
- Bi-encoders for meaning-based similarity
- Cosine similarity instead of word counting

## 🎓 Skills Developed
✅ File I/O operations  
✅ Text preprocessing techniques  
✅ Basic similarity algorithms  
✅ Python class structure  
✅ RAG pipeline fundamentals  

---