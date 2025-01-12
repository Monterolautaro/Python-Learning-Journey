### Ejercicio 1
# There is a saying that "Data scientists spend 80% of their time cleaning data, and 20% of their time complaining about
# cleaning data." Let's see if you can write a function to help clean US zip code data. Given a string, it should return
# whether or not that string represents a valid zip code. For our purposes, a valid zip code is any string consisting
# of exactly 5 digits.

# HINT: str has a method that will be useful here. Use help(str) to review a list of string methods.

def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    if len(zip_code) == 5 and zip_code.isdigit():
        return True
    else: 
        return False


### Ejercicio 2

# A researcher has gathered thousands of news articles. But she wants to focus her attention on articles 
# including a specific word. Complete the function below to help her filter her list of articles.

# Your function should meet the following criteria:

# Do not include documents where the keyword string shows up only as a part of a larger word. 
# For example, if she were looking for the keyword “closed”, you would not include the string “enclosed.”
# She does not want you to distinguish upper case from lower case letters. So the phrase “Closed the case.
# ” would be included when the keyword is “closed”
# Do not let periods or commas affect what is matched. “It is closed.” would be included when the keyword is
# “closed”. But you can assume there are no other types of punctuation.

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    res = []
    for str in doc_list:
        words = [parte for subcadena in str.lower().split(' ') for parte in subcadena.split(',')]
        valid = [word == keyword for word in words]
        last_valid = [word == f'{keyword}.' for word in words]
        if True in valid:
            res.append(doc_list.index(str))
        elif True in last_valid:
            res.append(doc_list.index(str))
    return res


### Ejercicio 3

# Now the researcher wants to supply multiple keywords to search for. Complete the function below to help her.

# (You're encouraged to use the word_search function you just wrote when implementing this function.
#  Reusing code in this way makes your programs more robust and readable - and it saves typing!)

def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    res = {}

    for keyword in keywords:
        res[keyword] = []  # inicializo una lista vacía para cada keyword

        for i, doc in enumerate(doc_list):
            # normalizo y proceso el documento en palabras
            words = [parte.strip('.,!?') for subcadena in doc.lower().split(' ') for parte in subcadena.split(',')]

            # Si la palabra clave está en las palabras procesadas, agrega el índice del documento
            if keyword in words:
                res[keyword].append(i)

    return res

# Check your answer
# q3.check()