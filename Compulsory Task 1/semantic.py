import spacy
nlp = spacy.load('en_core_web_md')

print(
"""

*********************
Similarity with Spacy
*********************
"""
     )
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(f"\n'cat' similarity to word 'monkey': {word1.similarity(word2)}")
print(f"\n'banana' similarity to 'monkey': {word3.similarity(word2)}")
print(f"\n'banana' similarity to 'cat': {word3.similarity(word1)}")

"""
The task already actually explained the similarities, but I'll rephrase in my own words.
Semantic similarity seems to be predicated on associations, thus 'cat' and 'monkey' have 
the most similarity because they are both animals. 'monkey' and 'banana' have a greater
similarity than 'cat' and 'banana' because monkeys are associated with bananas as a food.
Potentially if i included 'fish' there may be a stronger similarity with 'cat' because
not only are a cat and a fish animals, but fish are associated with cats as as a food.
"""

print(
"""

************************************
Similarity with Spacy (Own Examples)
************************************
"""
     )
word1 = nlp("Hawaii")
word2 = nlp("Potato")
word3 = nlp("Volcano")
word4 = nlp("Aloha")
print(f"\n'Hawaii' similarity to 'Potato': {word1.similarity(word2)}")
print(f"\n'Volcano' similarity to 'Potato': {word3.similarity(word2)}")
print(f"\n'Volcano' similarity to 'Hawaii': {word3.similarity(word1)}")
print(f"\n'Hawaii' similarity to 'Aloha': {word1.similarity(word4)}")

"""
Building on my prior comments, I explored the assocations between the above words.
I initially added 'Hawaii', 'Potato' and 'Volcano', expecting, of course, Hawaii to
have a Stronger association with Volcano than Potato. It did, but not as much as i 
exapected given one of the things Hawaii is famous for is Volcanos. I then added 'Aloha'
because I was sure that Spacy was performing as well as it should, however the association
between Aloha (Hawaiian greeting) and Hawaii, was extremely strong, coming in at greater 
than 1.
"""

print(
"""

********************
Working with vectors
********************
"""
     )
tokens = nlp('cat apple monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(f"\n{token1.text} similarity to {token2.text}: {token1.similarity(token2)}")

print(
"""

**********************
Working with sentences
**********************
"""
     )
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
print(f"\nReference Sentence: Why is my cat on the car\n")
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(
f"""
'{sentence}'. 
Similarity to reference: {similarity}
"""
         )