import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import PunktSentenceTokenizer
import language

def create_keyword(t):
	text1=t.lower()
	#text1=language.spell_check(text1)
	ps=PorterStemmer()
	tokens = nltk.word_tokenize(text1)
	text=[ps.stem(t) for t in tokens]
	wnl = nltk.WordNetLemmatizer()
	text = [wnl.lemmatize(t) for t in text]
	text=' '.join(text)
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(text)
	filtered_words = [w for w in tokens if not w in stopwords.words('english')]
	text=' '.join(filtered_words)
	#text=language.spell_check(text)
	return text
