from transformers import pipeline
from transformers import GPT2Tokenizer, GPT2Model
import nltk
from nltk.corpus import wordnet as wn


#brining a pipeline from Hugging face library
generator = pipeline('text-generation', model='gpt2')
# getting a tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
#getting the model that the inputs will be based off of
model = GPT2Model.from_pretrained('gpt2')

#sample sequence
sequence = "jane will write it because john is getting the mango"

word = sequence.split()[-1]
tokens = tokenizer.tokenize(word)
ids = tokenizer.convert_tokens_to_ids(tokens)


# ****** i need to not replace it with a synonmym but instead something that can replace it
synsets = wn.synsets(word)
first_synset = synsets[0]

for example in first_synset.lemmas():
    print(example.name())

worked = False

if len(ids) > 1:
    for lemma in first_synset.lemmas():
        tokens2 = tokenizer.tokenize(lemma.name())
        ids2 = tokenizer.convert_tokens_to_ids(tokens2)
        if len(ids2) == 1:
            worked = True
            word = lemma.name()
            break
else:
    worked = True
            
if(worked == False):
    print("failed")
else:
    truck = " ".join(sequence.split()[:-1]) + " "+ word
    print(truck)
    


