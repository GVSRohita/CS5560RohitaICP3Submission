# # coding= UTF-8
# from stanfordcorenlp import StanfordCoreNLP
#
# # Preset
# host = 'http://localhost'
# port = 9000
# nlp = StanfordCoreNLP(host, port=port, timeout=30000)
#
#
# # The sentence you want to parse
# sentence1 = 'The dog saw John in the park.'
#
# # POS
# print('POS：', nlp.pos_tag(sentence1))
#
# # Tokenize
# print('Tokenize：', nlp.word_tokenize(sentence1))
#
# # NER
# print('NER：', nlp.ner(sentence1))
#
# # Parser
# print('Parser：')
# print(nlp.parse(sentence1))
# print(nlp.dependency_parse(sentence1))
#
# # Close Stanford Parser
# nlp.close()
#
# from stanfordcorenlp import StanfordCoreNLP
#
# # Preset
# host = 'http://localhost'
# port = 9000
# nlp = StanfordCoreNLP(host, port=port, timeout=30000)
#
#
# # The sentence you want to parse
# sentence2 = 'The little bear saw the fine fat trout in the rocky brook.'
#
# # POS
# print('POS：', nlp.pos_tag(sentence2))
#
# # Tokenize
# print('Tokenize：', nlp.word_tokenize(sentence2))
#
# # NER
# print('NER：', nlp.ner(sentence2))
#
# # Parser
# print('Parser：')
# print(nlp.parse(sentence2))
# print(nlp.dependency_parse(sentence2))
#
# # Close Stanford Parser
# nlp.close()
#
# # open and read from a file
# file = open("sample.txt", "r")
# for sentence in file:
#     print(sentence)
#     # POS
#     print('POS：', nlp.pos_tag(sentence))
#
#     # Tokenize
#     print('Tokenize：', nlp.word_tokenize(sentence))
#
#     # NER
#     print('NER：', nlp.ner(sentence))
#
#     # Parser
#     print('Parser：')
#     print(nlp.parse(sentence))
#     print(nlp.dependency_parse(sentence))
#
# # Close Stanford Parser
# nlp.close()


from stanfordcorenlp import StanfordCoreNLP
import logging
import json

class StanfordNLP:
    def __init__(self, host='http://localhost', port=9000):
        self.nlp = StanfordCoreNLP(host, port=port,
                                   timeout=30000)  # , quiet=False, logging_level=logging.DEBUG)
        self.props = {
            'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,depparse,dcoref,relation',
            'pipelineLanguage': 'en',
            'outputFormat': 'json'
        }

    def word_tokenize(self, sentence):
        return self.nlp.word_tokenize(sentence)

    def pos(self, sentence):
        return self.nlp.pos_tag(sentence)

    def ner(self, sentence):
        return self.nlp.ner(sentence)

    def parse(self, sentence):
        return self.nlp.parse(sentence)

    def dependency_parse(self, sentence):
        return self.nlp.dependency_parse(sentence)

    def annotate(self, sentence):
        return json.loads(self.nlp.annotate(sentence, properties=self.props))

    def co_reference(self, sentence):
        return self.nlp.coref(sentence)

if __name__ == '__main__':
    sNLP = StanfordNLP()
    text = 'The little bear saw the fine fat trout in the rocky brook'
    filename = 'sample.txt'
    with open(filename, 'r') as filehandle:
        filecontent = filehandle.read().replace('\n', '')
        res = sNLP.annotate(filecontent)
        for s in res["sentences"]:
            print("%d : '%s' : %s %s" % (
                s["index"], " ".join([t["word"] for t in s["tokens"]]), s["sentimentValue"], s["sentiment"]
            ))
   # print("Annotate:", sNLP.annotate(text))
   # print("POS:", sNLP.pos(text))
   # # print("Tokens:", sNLP.word_tokenize(text))
   # print("NER:", sNLP.ner(text))
   # # print("Parse:", sNLP.parse(text))
   # # print("Dep Parse:", sNLP.dependency_parse(text))
   # print("Co-reference:", sNLP.co_reference(text))
