# TAKEN FROM: https://www.kaggle.com/scratchpad/notebook83d18696fc/edit

# https://betterprogramming.pub/extractive-text-summarization-using-spacy-in-python-88ab96d1fd97

import numpy as np # linear algebra
import spacy

from IPython.display import display
import re
from time import time
# from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS as stopwords
from nltk.corpus import stopwords
import nltk
import heapq

import pandas as pd

import warnings
warnings.filterwarnings('ignore')
import logging
logging.getLogger("lda").setLevel(logging.WARNING)

stopwords = stopwords.words('english')

nlp = spacy.load('en_core_web_lg')
def normalize_text(text):
    tm1 = re.sub('<pre>.*?</pre>', '', text, flags=re.DOTALL)
    tm2 = re.sub('<code>.*?</code>', '', tm1, flags=re.DOTALL)
    tm3 = re.sub('<[^>]+>', '', tm1, flags=re.DOTALL)
    return tm3.replace("\n", "")

# Body_Cleaned_1
text = """
State of Rhombus
Jack Firth, October 2021
Motivation
Today, Racket promises language-oriented programming to its users. But this promise has a constraint: if you want to build a macro-extensible language, your language has to use S-expressions. This constraint is unfairly limiting, as telling users “you can build any extensible language you want, as long as it uses S-expressions” is akin to Henry Ford telling Model-T buyers “your car can be any color you want, as long as it’s black.” We’d like to lift this limitation with a new programming language while taking this opportunity to improve Racket in backward-incompatible ways.
Overview
Rhombus is an experiment in building a macro-extensible general-purpose programming language with conventional surface syntax and improved libraries on top of the Racket platform.
Details
By “macro-extensible,” we mean that Rhombus users should be able to extend the syntax of Rhombus in much the same way that Racket users can extend the syntax of Racket. Complex syntactic extensions such as object and class systems, static type checkers, and pattern matching should be implemented as libraries while still providing a surface syntax familiar to users of these features in other languages.
By “conventional surface syntax,” we mean conventional to both users of widely-used programming languages as well as newcomers who are familiar with basic math notation. This leads us to the following constraints:
Arithmetic is infix, for example,
1+x
Function calls are written as a function expression followed by a parenthesized comma-separated list of arguments, such as
f(x, y, z)
Extra parentheses can be used freely to group things and disambiguate, such as
(1 + 2) * 3, without introducing new structures or semantics.
Dots are used for member selection, like
point.x
Syntactic forms are connected by adjacency rather than in a strict hierarchy. For example
do { } while ( )and
x where y = z. This is a kind of “infix” that is broader than just arithmetic.
By “improved libraries,” we mean that Rhombus should not be beholden to the backward compatibility constraints of Racket. Rhombus should be free to innovate in providing new standard libraries for features that are becoming commonplace in other languages, such as generic collections, stream processing, and asynchronous programming.
By “on top of the Racket platform,” we mean that Rhombus should be a
#lang like any other, and it should be possible for users to combine
Rhombus code and libraries with ordinary Racket code and libraries
seamlessly. Where we are now
A few surface syntax proposals have been brainstormed, and the proposals fit into two broad categories:
C-like surface syntaxes, which use braces and semicolons** to convey general structure. Jay’s C-expressions fit this category.
Python-like surface syntaxes, which use colons and indentation to convey general structure. Jay’s lexprs and Matthew’s shrubbery notation fit this category.
Separately, there’s the question of how much syntactic grouping the surface syntax should be responsible for versus how much grouping is left up to the macro system. Three options are possible:
The surface syntax is responsible for all grouping. This is roughly where traditional S-expressions lie, and it’s awkward enough that many Lisps relax the S-expressions-for-everything constraint and let macros create implicit groupings. For example, Clojure’s
letform implicitly groups binding-expression pairs based on adjacency, as in
(let [x 1 y 2] (+ x y)). Racket’s keyword arguments are a similar instance of relaxing this constraint. C-expressions are an attempt to have “conventional surface syntax” with this property.
The surface syntax is responsible for no grouping. This results in a Forth-like syntax where the program is just a flat sequence of tokens. This doesn’t satisfy our “conventional surface syntax” requirement.
The surface syntax is responsible for some grouping, but not all. This requires that the parser understand the program’s bindings and expand macros to get a complete picture of a program’s structure. Interleaving the parsing of a token stream with macro expansion in this fashion is called enforestation, and it allows macros to extend the syntax of conventional languages. The Honu research language pioneered this technique.
What’s Next
We’ve decided on a Python-like surface syntax with enforestation, specifically shrubbery notation, as the first proposal to advance to the next prototyping stage. This may not be the final direction that the Rhombus project takes, but it’s the direction we’re prioritizing for the time being. We made this decision based on the following factors:
Indentation sensitivity a la Python has the advantage that the visual grouping on the screen matches grouping for parsing, but it also leaves plenty of room for operator- and identifier-driven context-sensitive parsing.
Matthew tried several experiments and found Python-style notation most straightforward to work with, and he’s been the primary Rhombus implementor thus far.
Making the “correct” decision about surface syntax isn’t our goal at this stage. We’re still firmly in the prototyping phase of the Rhombus project. Our goal is to stake out territory in the design space and get a deeper understanding of what challenges lie ahead. For that reason, we plan to build a language around shrubbery notation next. We don’t believe that shrubbery notation is perfect. Still, we believe that the understanding gained from building a working programming language with shrubbery notation will help us further refine shrubbery notation. It will also be vital in determining what other surface syntaxes are worth exploring.
To build a language, we need to write libraries. The libraries we can work on fall into two broad categories: general-purpose and special-purpose. General-purpose libraries are necessary to define the APIs of many other libraries, such as a class system, concurrency abstractions, or generic collections. Special-purpose libraries are specific to a narrow (but practically useful) domain, such as text parsing or theorem proving. Special purpose libraries leverage domain-specific languages more heavily, so they’ll give us a good sense of how well shrubbery notation can cooperate with complex DSLs.
Libraries are an excellent place for new Rhombus contributors to jump in! We’re still in the early stages, so exploring multiple approaches to the same problem domain is valuable. There’s a wide variety of directions to explore. Below are some we’re already considering to varying degrees, but we encourage additional proposals.
Generic collections
General purpose. Volunteers: @jackfirth. Relevant GitHub issues: #19, #21, #28, #80, #102, #147.
Rhombus should provide common data structures for generic collections, such as lists, sets, maps, and the tools to abstract over different kinds of collections. Racket’s monomorphic approach to collections has been a long-standing complaint, and it’s one of the few areas the community almost universally agrees needs improvement.
Classes and structs
General purpose. Volunteers: none yet. Relevant GitHub issues: #57, #76, #151, #152.
Rhombus should provide a better, more unified system for defining new data types and interfaces than Racket’s current mishmash of structs, classes, generics, and structure type properties. There’s a lot of room to leverage shrubbery notation here, especially if we were to build some sort of dot transformer protocol for macros to use.
Other ideas
Concurrency and parallelism. Can we do better than Racket here?@jackfirth - Software transactional memory à la Clojure would be convenient.
Annotations, types, and contracts. Racket’s runtime contracts and Typed Racket’s static types are at two extreme ends of the dynamic-static correctness spectrum. Can Rhombus occupy a more user-friendly middle ground?
Multi-language Scribble. If we want Rhombus and Racket libraries to be seamlessly interoperable, we need a way for Scribble to translate library documentation for different surface syntaxes. In-source documentation might be worth exploring here too.
Redex, but better.
""".strip()


# Body_Cleaned
# Clean text before feeding it to spaCy
punctuations = '!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~'
# Define function to cleanup text by removing personal pronouns, stopwords, and puncuation
def cleanup_text(docs):
    texts = []
    doc = nlp(docs, disable=['parser', 'ner'])
    tokens = [tok.lemma_.lower().strip() for tok in doc if tok.lemma_ != '-PRON-']
    tokens = [tok for tok in tokens if tok not in stopwords and tok not in punctuations]
    tokens = ' '.join(tokens)
    texts.append(tokens)
    return pd.Series(texts)

t = normalize_text(text)
t2 = cleanup_text(t)

# this is function for text summarization

def generate_summary(text_without_removing_dot, cleaned_text):
    sample_text = text_without_removing_dot
    doc = nlp(sample_text)
    sentence_list=[]
    for idx, sentence in enumerate(doc.sents): # we are using spacy for sentence tokenization
        sentence_list.append(re.sub(r'[^\w\s]','',str(sentence)))

    stopwords = nltk.corpus.stopwords.words('english')

    word_frequencies = {}  
    for word in nltk.word_tokenize(cleaned_text):  
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1


    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)


    sentence_scores = {}  
    for sent in sentence_list:  
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]


    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

    summary = ' '.join(summary_sentences)
    print("Original Text::::::::::::\n")
    print(text_without_removing_dot)
    print('\n\nSummarized text::::::::\n')
    print(summary)  