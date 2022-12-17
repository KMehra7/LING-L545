# Using UDPipe

UDPipe is a trainable pipeline for tokenization, tagging, lemmatization and dependency parsing of CoNLL-U files. UDPipe is language-agnostic and can be trained given annotated data in CoNLL-U format.

Steps followed - 

```
$ git clone https://github.com/ufal/udpipe
$ cd udpipe/src
$ make
```

This will compile UDPipe, now put it (cp) somewhere in your $PATH, e.g. /usr/local/bin. You can find out what directories are in your $PATH by doing: echo $PATH.
Now download the UD_Finnish-TDT treebank.

```
$ git clone https://github.com/UniversalDependencies/UD_Finnish-TDT
```

If you go into the directory UD_Finnish-TDT, you will be able to train UDPipe with the following command:
```
$ cat fi_tdt-ud-train.conllu | udpipe --tokenizer=none --parser=none --train fi.udpipe
```

This will produce a model file fi.udpipe which you can then use for tagging:

```
$ cat fi_tdt-ud-test.conllu | udpipe --tag fi.udpipe > fi_tdt-ud-test_output.conllu
```

You can use the CoNLL-2017 evaluation script to evaluate the tagger performance:

```
$ python3 conll17_ud_eval.py --verbose fi_tdt-ud-test.conllu fi_tdt-ud-test_output.conllu
```
Output - 

```
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     94.63 |     94.63 |     94.63 |     94.63
XPOS       |     95.77 |     95.77 |     95.77 |     95.77
Feats      |     90.86 |     90.86 |     90.86 |     90.86
AllTags    |     89.82 |     89.82 |     89.82 |     89.82
Lemmas     |     84.86 |     84.86 |     84.86 |     84.86
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00
```

Using a (very) simple perceptron tagger for CoNLL-U files - 

Perceptron tagger uses supervised machine learning to tackle the POS problem. We can see that with defualt values the accuracy of the perceptron is less than UDPipe but if we can tweak the features, we can achieve better accuracy.

Steps followed - 

The objective of this task is to download and run a very basic averaged perceptron tagger (less than 300 lines of Python).

First download the code:

```
$ git clone https://github.com/ftyers/conllu-perceptron-tagger.git
```

Then download some data, feel free to replace UD_Finnish with any language in UD.

```
$ git clone https://github.com/UniversalDependencies/UD_Finnish-TDT
```

Then download the CoNLL shared task 2017 official evaluation script and unzip it:

```
$ wget http://universaldependencies.org/conll17/eval.zip
$ unzip eval.zip
```

Finally enter the directory of the perceptron tagger:

```
$ cd conllu-perceptron-tagger
```

You can train the tagger using the following command:
```
$cat ../fi_tdt-ud-train.conllu | python3 tagger.py -t fi-ud.dat
```
Output - 
```
163223
Iter 0: 131852/163223=80.78028219062264
163202
Iter 1: 145190/163223=88.95192466747946
163212
Iter 2: 152019/163223=93.13577130673985
163210
Iter 3: 155744/163223=95.41792516985964
163218
Iter 4: 158141/163223=96.8864682060739
```
Now you can run the tagger

```
$  cat ../fi_tdt-ud-test.conllu | python3 tagger.py fi-ud.dat > fi-ud-test.out
```

And evaluate:
```
$ python3 ../conll17_ud_eval.py --verbose ../fi_tdt-ud-test.conllu fi-ud-test.out
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     90.76 |     90.76 |     90.76 |     90.76
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     90.76 |     90.76 |     90.76 |     90.76
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00
```
# Comparative Study - 
UDPipe performs better versus the default perceptron based tagger.
UDPipe provides language-agnostic tokenization, tagging, lemmatization and dependency parsing of raw text, which is an essential part in natural language processing.
UDPipe allows to work with data in CONLL-U format .
Perceptron tagger uses supervised machine learning to tackle the POS problem. We can see that with defualt values the accuracy of the perceptron is less than UDPipe but if we tweak the features, we can achieve better accuracy.

By updating tagger.py to add 2 more features to the suffix- 
```
# New features
        add('i suffix2', word[-2:])
		add('i suffix3', word[-1:])
```
We can see that the UPOS value decreases with the addition of these features- 
```
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     90.26 |     90.26 |     90.26 |     90.26
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     90.26 |     90.26 |     90.26 |     90.26
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00
```

By updating tagger.py to add 2 more features to the prefix by replacing the above ones in the suffix- 
```
# New features
        add('i pref2', word[:1])
        add('i pref3', word[:2])
```
We can see that the UPOS value is still marginally lower than the value without these features but has increased with respect to the first two features - 
```
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     90.75 |     90.75 |     90.75 |     90.75
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     90.75 |     90.75 |     90.75 |     90.75
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00
```

However by adding another feature to the ones above we can see that the value improved.
By updating tagger.py to add 1 more feature - 
```
# New features
        add('i pref2', word[:1])
        add('i pref3', word[:2])
        add('i pref4', word[:3])
```
We can see that the UPOS value improves with the addition of this feature- 
```
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     91.46 |     91.46 |     91.46 |     91.46
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     91.46 |     91.46 |     91.46 |     91.46
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00
```

By updating tagger.py to add 1 more feature - 
```
# New features
        add('i pref2', word[:1])
        add('i pref3', word[:2])
        add('i pref4', word[:3])
        add('i pref5', word[:4])

```
We can see that the UPOS value increases further- 
```
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     92.42 |     92.42 |     92.42 |     92.42
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     92.42 |     92.42 |     92.42 |     92.42
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00
```