# coding= UTF-8
from stanfordcorenlp import StanfordCoreNLP

# Preset
host = 'http://localhost'
port = 9000
nlp = StanfordCoreNLP(host, port=port, timeout=30000)


# The sentence you want to parse
sentence1 = 'The dog saw John in the park.'

# POS
print('POS：', nlp.pos_tag(sentence1))

# Tokenize
print('Tokenize：', nlp.word_tokenize(sentence1))

# NER
print('NER：', nlp.ner(sentence1))

# Parser
print('Parser：')
print(nlp.parse(sentence1))
print(nlp.dependency_parse(sentence1))

# Close Stanford Parser
nlp.close()

from stanfordcorenlp import StanfordCoreNLP

# Preset
host = 'http://localhost'
port = 9000
nlp = StanfordCoreNLP(host, port=port, timeout=30000)


# The sentence you want to parse
sentence2 = 'The little bear saw the fine fat trout in the rocky brook.'

# POS
print('POS：', nlp.pos_tag(sentence2))

# Tokenize
print('Tokenize：', nlp.word_tokenize(sentence2))

# NER
print('NER：', nlp.ner(sentence2))

# Parser
print('Parser：')
print(nlp.parse(sentence2))
print(nlp.dependency_parse(sentence2))

# Close Stanford Parser
nlp.close()

# open and read from a file
file = open("sample.txt", "r")
for sentence in file:
    print(sentence)
    # POS
    print('POS：', nlp.pos_tag(sentence))

    # Tokenize
    print('Tokenize：', nlp.word_tokenize(sentence))

    # NER
    print('NER：', nlp.ner(sentence))

    # Parser
    print('Parser：')
    print(nlp.parse(sentence))
    print(nlp.dependency_parse(sentence))

# Close Stanford Parser
nlp.close()

