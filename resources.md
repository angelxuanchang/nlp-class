---
layout: default
img: hal9k
img_link: http://en.wikipedia.org/wiki/HAL_9000
caption: "In 2001 A Space Odyssey, HAL 9000 speaks in a calm voice and conversational manner in constrast to the humans."
title: Resources and Tools
active_tab: resources
---

### Reference books

* There is no official textbook for the course, but if you would like to read further about NLP, here are some good reference books on NLP:
    * [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/) by [Dan Jurafsky](http://www.stanford.edu/~jurafsky) and [James Martin](http://www.cs.colorado.edu/~martin).
    * [Natural Language Processing](https://github.com/jacobeisenstein/gt-nlp-class/blob/master/notes/eisenstein-nlp-notes.pdf) by [Jacob Eisenstein](https://jacobeisenstein.github.io/)
    * [A Primer on Neural Network Models for Natural Language Processing](http://u.cs.biu.ac.il/~yogo/nnlp.pdf) by Yoav Goldberg (see also [Neural Network methods for Natural Language Processing](http://www.morganclaypool.com/doi/10.2200/S00762ED1V01Y201703HLT037)).

* To learn more about deep learning
    * [Deep learning](http://www.deeplearningbook.org/) by Ian Goodfellow and Yoshua Bengio and Aaron Courville
    * [Dive into deep learning](https://d2l.ai/index.html) by Aston Zhang, Zachary C. Lipton, Mu Li, and Alexander J. Smola

### Debugging Neural Networks
* [General tips from Andrej Karpathy for training neural networks](http://karpathy.github.io/2019/04/25/recipe/)
* [Tips from Graham Neubig (CMU CS11-747) for debugging NLP models](http://www.phontron.com/class/nn4nlp2020/assets/slides/nn4nlp-10-debugging.pdf)


### Podcasts
* [NLP highlights](https://player.fm/series/nlp-highlights) with Matt Gardner, Pradeep Dasigi, and Waleed Ammar 

### Tools

* Deep learning for NLP
    * [TorchText](https://torchtext.readthedocs.io/en/latest/)

* Sequence models
    * [FairSeq](https://github.com/facebookresearch/fairseq)

* Static Word Embeddings
    * [Word2Vec](https://code.google.com/archive/p/word2vec/)
    * [GloVe](https://nlp.stanford.edu/projects/glove/)
    * [FastText](https://fasttext.cc/) 

* Pretrained language models 
    * [HuggingFace course on transformers](https://huggingface.co/course/chapter1/1) 
       * [HuggingFace transformers](https://huggingface.co/transformers/) Docummentation for various transformer based models from HuggingFace
    * [OpenAI API](https://beta.openai.com/overview)
    * [Llama](https://github.com/facebookresearch/llama)

* Using LLMs
    * [Prompting Guide](https://www.promptingguide.ai/)
    * [LangChain](https://github.com/langchain-ai/langchain) / [LangGraph](https://langchain-ai.github.io/langgraph/) for building LLM agents

* Machine Translation
    * [SFUTranslate](https://github.com/sfu-natlang/SFUTranslate) SFU NLL's MT toolkit (designed to be modern and flexible) 
    * [JoeyNMT](https://github.com/joeynmt/joeynmt) Minimalist system for understanding NMT
    * [OpenNMT](https://opennmt.net/) Comprehensive NMT framework

* NLP pipelines
    * [AllenNLP](https://allennlp.org/) \[[demo](https://demo.allennlp.org/)\] Modern NLP tools using Pytorch from AI2 
    * [Spacy.io](https://spacy.io/) \[[demo](https://explosion.ai/demos/)\] Popular python based NLP pipeline
    * [Stanza](https://stanfordnlp.github.io/stanza) \[[demo](http://stanza.run/)\] Python NLP library from Stanford
    * [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/) \[[demo](http://corenlp.run/)\] Java NLP pipeline from Stanford
    * [NLTK](https://www.nltk.org/) \[[demo](http://text-processing.com/demo/)\] \[[book](http://www.nltk.org/book_1ed/)\] Useful basic Python tools for NLP



## Tasks and datasets

A list of shared task datasets are provided below.
In some cases you can also extend your homework code to produce innovative project ideas for these tasks.

### Shared Task Collections

* [Torchtext](https://torchtext.readthedocs.io/en/latest/)
* [Sebastian Ruder's curated collection](https://nlpprogress.com/)
* [Datasets for Natural Language Processing](https://machinelearningmastery.com/datasets-natural-language-processing/)
* [Kaggle NLP Tasks](https://www.kaggle.com/datasets?sortBy=hottest&group=public&page=1&pageSize=20&size=sizeAll&filetype=fileTypeAll&license=licenseAll&tagids=13204%2C11208%2C2107)

#### CoNLL Shared Tasks

* [CoNLL Shared Tasks](http://www.conll.org/previous-tasks)
* [CoNLL 2003 Named Entity Recognition Task](https://www.clips.uantwerpen.be/conll2003/ner/)
* [CoNLL 2000 Chunking Task](https://www.clips.uantwerpen.be/conll2000/chunking/)
* [CoNLL 2018 Multilingual Parsing](http://universaldependencies.org/conll18/)

#### SemEval Shared Tasks

* [SemEval 2018](http://alt.qcri.org/semeval2018/index.php?id=tasks)
* [SemEval 2017](http://alt.qcri.org/semeval2017/index.php?id=tasks)
* [SemEval 2016](http://alt.qcri.org/semeval2016/index.php?id=tasks)
* [SemEval 2015](http://alt.qcri.org/semeval2015/index.php?id=tasks)
* [SemEval 2014](http://alt.qcri.org/semeval2014/index.php?id=tasks)

### Classification Tasks

* [Toxic Comment Classification](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)
* [Fake News Challenge](https://github.com/FakeNewsChallenge/fnc-10)
* [Spam / Click-bait detection](https://www.kaggle.com/therohk/examine-the-examiner)

### Information Extraction

* [Drug-Drug Interaction Extraction](https://github.com/zha204/ddi-corpus-database)
* [Web named entities](http://nlp.uned.es/weps/weps-3/data)
* [Twitter sequence prediction tasks](http://www.cs.cmu.edu/~ark/TweetNLP/)
* [WNUT Emerging and Rare entity recognition shared task](http://noisy-text.github.io/2017/emerging-rare-entities.html)
* [Gun violence text data](http://gun-violence.org)

### Parsing

* [Universal Dependencies](http://universaldependencies.org)
* [WikiText](https://www.salesforce.com/products/einstein/ai-research/the-wikitext-dependency-language-modeling-dataset/)
* [Opinion mining](https://ikernels-portal.disi.unitn.it/projects/sentube/)

### Machine Translation

* [WMT 2018 Shared Task](http://www.statmt.org/wmt18/)
* [WMT 2017 Shared Task](http://www.statmt.org/wmt17/)
* [WMT 2016 Shared Task](http://www.statmt.org/wmt16/)
* [WMT 2015 Shared Task](http://www.statmt.org/wmt15/)
* [NMT 2018 Neural MT Shared Task](https://sites.google.com/site/wnmt18/shared-task)
* [Web Inventory of Transcribed and Translated Talks](https://wit3.fbk.eu/mt.php?release=2016-01)

### Unlabeled Data for Clustering, Language Models, etc.

* [Wikipedia XML data](http://www-connex.lip6.fr/%7Edenoyer/wikipediaXML/)
* [Web data](http://corpus.leeds.ac.uk/internet.html)
* [BootCat](http://bootcat.dipintra.it)

### Sentiment and Opinion Mining

* [Stanford Sentiment Treebank](https://nlp.stanford.edu/sentiment/treebank.html)
* [Movie reviews](http://ai.stanford.edu/~amaas/data/sentiment/)
* [Yelp Challenge](https://www.yelp.com/dataset/challenge)
* [Sentiment and opinion mining datasets](https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html)

### Natural Language Understanding and Inference

* [GLUE Benchmark](https://gluebenchmark.com)
* [RepEval 2017](https://repeval2017.github.io/shared/)
* [The Stanford Natural Language Inference (SNLI) Corpus](https://nlp.stanford.edu/projects/snli/)
* [Multi-Genre NLI](https://www.nyu.edu/projects/bowman/multinli/)
* [MedNLI](https://physionet.org/physiotools/mimic-code/mednli/)
* [XNLI](https://www.nyu.edu/projects/bowman/xnli/)

### Question Answering

* [Qanta shared task](https://sites.google.com/view/qanta/home) 
* [Algebra Question Answering with Rationales](https://github.com/deepmind/AQuA/)
* [Quora Question Pairs](https://www.kaggle.com/c/quora-question-pairs).
* Reverse QA: Jeopardy style QA. [json](https://drive.google.com/file/d/0BwT5wj_P7BKXb2hfM3d2RHU1ckE/view) and [csv](https://drive.google.com/file/d/0BwT5wj_P7BKXUl9tOUJWYzVvUjA/view)
* [CoQA](https://stanfordnlp.github.io/coqa/)
* [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/)
* [HotpotQA](https://hotpotqa.github.io/)
