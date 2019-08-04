from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
import string
import json

colors = ['blue', 'green', 'black', 'black-green', 'purple', 'pink', 'black-black-white', 'black-white',
          'grey-blue-silver', 'grey'
    , 'silver']
gen = ['men', 'boys', 'boy', 'girl', 'girls', 'women']


def nlp_treatment(s1):
    '''
    :param s1:
    :return:
    '''
    s1 = s1.lower()
    result = re.sub(r'\d+', '', s1)
    # translator = str.maketrans('', '', string.punctuation)
    # result = result.translate(translator)
    result = re.sub(r'[^\w\s]', ' ', result)
    result = result.strip()
    # print("post number, punctuation,space removal ={0}".format(result))
    return result


def remove_stop_words(s1):
    '''
    :param s1:
    :return:
    '''
    stop_words = set(stopwords.words('english'))
    stop_words.update(['show', 'list', 'search', 'want', 'see', 'help', 'awesome', 'best'])
    word_tokens = word_tokenize(s1)
    # print('with stop words {}'.format(s1))
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    # print('post stop word removal ={0}'.format(filtered_sentence))
    return filtered_sentence


def lemiatize(s1):
    '''
    :param s1:
    :return:
    '''
    lemmatizer = WordNetLemmatizer()
    lem_words = [lemmatizer.lemmatize(w) for w in s1]
    # print('post lematize = {0}'.format(lem_words))
    return lem_words


def preprocess(s1):
    '''
    :param s1:
    :return:
    '''
    nums = re.findall(r'\d+', s1)
    s1 = nlp_treatment(s1)
    s1 = remove_stop_words(s1)
    s1 = lemiatize(s1)
    res = {}
    res['query'] = s1
    res['gender'] = ''
    res['color'] = ''
    res['range'] = '' if not nums else nums[0]
    for q in s1:
        if q in gen:
            res['gender'] = q
        if q in colors:
            res['color'] = q
    return res


def preprocess_cool(s1):
    '''
    :param s1:
    :return:
    '''
    s1 = nlp_treatment(s1)
    s1 = remove_stop_words(s1)
    s1 = lemiatize(s1)
    return s1
