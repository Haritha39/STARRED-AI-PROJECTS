import nltk
from nltk.tokenize import RegexpTokenizer
from string import punctuation
from nltk.corpus import stopwords , words, wordnet
from nltk.stem import WordNetLemmatizer 

def preprocessData( code ,logger ):

    try:
        # code = open("code.txt" , "r")
        # code = code.read()


        # Converting to lower case
        code = code.lower()


        # Removing underscore and combining with space
        udrscr = ' '.join(code.split("_"))

        # Removing Numbers
        output = ''.join(c for c in udrscr if not c.isdigit())

        # Removing Punctuations 
        punctTokenizer = RegexpTokenizer('\w+')
        punct = punctTokenizer.tokenize(output)


        # Removing stop words 
        stopword = stopwords.words('english')
        removed = ' '.join(c for c in punct if c not in stopword and len(c) > 1 )

        #  Removing non-dictionary words
        wordsList = set(words.words())
        textList = nltk.word_tokenize(removed)
        nondic = ' '.join( c for c in textList if c not in wordsList and len(c) > 3 )

        # Removing duplictes
        textList = nltk.word_tokenize(nondic)
        noduplicate = list(set(textList))
        # print(len(noduplicate),"\n\n")

        # Lemmatizer
        pos = nltk.pos_tag(noduplicate)
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV
                }

        lema = []
        lt = WordNetLemmatizer()
        for each in pos:
            postag = each[1][0].upper()
            # print(each[1],"  ",postag)
            # print(tag_dict.get(postag, wordnet.NOUN))
            val = lt.lemmatize(each[0] , tag_dict.get(postag,wordnet.NOUN))
            lema.append(val)
        # print(lema)

        logger.info(" Prepocessing is completed successfully ")
        return lema
    except Exception as error:
        logger.error(" classificationModel - preprocesser.py {}".format(error) )


