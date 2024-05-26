from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize

def tfidfcosine_similarity(query, data):
    
    stack = []
    stack.append(query)

    for i in data:
        stack.append(i)
    
    sentences= []
   # vocab = []
    for row in stack:
        x = word_tokenize(row)
        sentence = ""
        for w in x:
            if w.isalpha():
                if len(sentence) ==0:
                    sentence += w.lower()
                    
                else:
                    sentence+= " "+ w.lower()
                    #sentence.append(w.lower())
                
        sentences.append(sentence)
        
        
        #print(x)
    #print(sentences)
    #print(vocab)

    #query = "cats, dogs are nice"

    sentence = ""
    for w in x:
        if w.isalpha():
            if len(sentence) ==0:
                sentence += w.lower()
                
            else:
                sentence+= " "+ w.lower()
    #print(x)


        
    tfidf_vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)
    
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix)
    #print(tfidf_matrix[0])
    return similarity.flatten(), sentences

def sort(my_list):
    size = len(my_list)
    for i in range(size):
        for j in range(size-i-1):
            if(my_list[j][1] > my_list[j+1][1]):
                tmp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = tmp
    return my_list 
def closest_match(data, cos_sim, n):

    

    
    n = len(data)
    elpos = []
    index = 0
    for i in cos_sim:
        elpos.append((index, i))
        index += 1
    elpos.pop(0)
    #print(elpos)

    elpos = sort(elpos)
    
    #print(elpos)
    #print(elpos[n-2][0])
    index_ = elpos[n-2][0]
    similaritychecker = elpos[n-2][1]
    most_similar =data[index_]
    return most_similar,index_,similaritychecker

questions = ['In Rome, which animal is protected under the law?',
             'Which type of animal is known to be the fastest bird in the world?', 
             'Which Mammal Has The Most Powerful Bite In The World?', 'Who Is The World�s Fastest Land Animal?', 'What Color Is Octopus Blood?'] 
query = "In Rome, which animal is protected under the law?"
similarity,data = tfidfcosine_similarity(query, questions)

answer = closest_match(data, similarity, len(data))

#print(answer)