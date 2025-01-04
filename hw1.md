---
layout: default
img: 20news_tsne
caption: "t-Distributed Stochastic Neighbor Embedding (t-SNE) is a technique that is commonly used for the visualization of high-dimensional data such as 100d or 300d word vectors."
title: Homework 1 | Contextual Spell Checking
active_tab: homework
---

# Homework 1

<span class="text-info">Start on {{ site.hwdates[1].startdate }}</span> |
<span class="text-warning">Due on {{ site.hwdates[1].deadline }}</span>

## Homework Questions 1: Language models and text classification

<span class="text-info">Out on {{ site.hwdates[1].startdate }}.</span> 
{% if site.hwdates[1].hwc-url %}
<span>Posted on [Coursys]({{ site.hwdates[1].hwc-url }}).</span> 
{% endif %}

# Programming Homework 1: Contextual Spell Checking

### Getting Started

Get started:

    git clone https://github.com/angelxuanchang/nlp-class-hw.git
    cd nlp-class-hw/spellchk

Clone your repository if you haven’t done it already:

    git clone git@github.sfu.ca:USER/nlpclass-{{ site.semcode }}-g-GROUP.git

Then copy over the contents of the `spellchk` directory into your
`hw1` directory in your repository.

Set up the virtual environment:

    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt

Note that if you do not change the requirements then after you have
set up the virtual environment `venv` you can simply run the following
command to get started with your development for the homework:

    source venv/bin/activate

### Background

Given a sentence with a typo in it:

    it will put your maind into non-stop learning.

The task is to correct the typo word `maind` to the most plausible
substitution, e.g.:

    it will put your mind into non-stop learning.

There are many ways to solve this problem but we are going
to use a large language model to solve this task. We will
take the typo word and replace it with a `[MASK]` token
and ask the language model to suggest the most plausible
token it could be. Because the language model has been
trained on a lot of English data, it is able to capture
the semantic meaning of what should be in the `[MASK]`
position and use that to predict a token that fits in
this sentence.

Since this task is part of a setup homework, we will
simplify the task and include the indices of the typo
words in the sentence, so the words to be replaced
with the correct words have been provided to you.

The input contains a comma separated list of token
indices followed by a tab character and followed by
the sentence with at least one typo in it.

Here is an example input:

    0,3     thier house was father away from my place

The typo words are in position 0 (`thier`) and 3 (`father`). Notice
how the typo words can be found in a dictionary, so just using a
number of edits away from a dictionary word is not an approach that
will work for this task.

The input will be a file of such inputs with locations of the
typos and the sentence. The output should also include the
locations indices:

    0,3     their house was farther away from my place

We have provided a default solution for this task and all the
mechanisms for running your solution on two sets of data: dev and
test data. The answers for dev data are provided, but the answers
for test data are not distributed.

### Default solution

The default solution is provided in `default.py`. To use the default
as your solution:

    cp answer/default.py answer/spellchk.py
    cp answer/default.ipynb answer/spellchk.ipynb
    python3 zipout.py
    python3 check.py

Make sure that the command line options are kept as they are in
`default.py`. You can add to them but you must not delete any
command line options that exist in `default.py`.

The default solution uses a large language model from the `transformers`
library by [huggingface](https://huggingface.co) and a mask token
replacement task which is a task used to train the language model
on Wikipedia and the Books corpus.

Here is how the default solution uses the recommended language
model to solve this task:

    from transformers import pipeline
    fill_mask = pipeline('fill-mask', model='distilbert-base-uncased')
    mask = fill_mask.tokenizer.mask_token
    print(fill_mask(f"it will put your {mask} into non-stop learning.")[0])

This will produce the output:

    {
        'score': 0.11389569193124771,
        'token': 2568,
        'token_str': 'mind',
        'sequence': 'it will put your mind into non - stop learning.'
    }

In this case, the output is correct, but the most plausible
substitution is not always the best candidate for a correction.


<div class="alert alert-danger" role="alert"><i class="fa fa-exclamation-circle"></i>
Use the <code>distilbert-base-uncased</code> language model for this homework.
</div>

### The Challenge

Your task is to improve the accuracy on this task as much as possible.
The definition of accuracy is provided below.  You cannot use any
external data sources. You can use a Python 3 library that provides
some helper functions but not any spelling correction modules or
models.

You can get a much higher accuracy by changing the function
`select_correction` with 1-2 lines to take into account something
that isn't taken into account by the default solution. Even
though, it is 1-2 lines, the solution may not be obvious or
trivial.

You should approach this challenge based on a careful examination
of the source code of the default solution and the output of the
default solution on the various inputs.

### Data files

The data files provided are:

* `data/input` -- input files `dev.tsv` and `test.tsv`
* `data/reference/dev.out` -- the reference output for the `dev.tsv` input file

### Required files

You must create the following files:

* `answer/spellchk.py` -- this is your solution to the homework. start by copying `default.py` as explained below.
* `answer/spellchk.ipynb` -- this is the Python notebook that will be your write-up for the homework.

### Run your solution on the data files

To create the `output.zip` file for upload to {{ site.hwsubmit.name }} do:

    python3 zipout.py

For more options:

    python3 zipout.py -h

### Check your accuracy

After you have run `zipout.py` you can check your accuracy on the
dev set:

    python3 check.py

The score reported is the accuracy of getting the typo word corrected
to the right token in the reference file.

For more options:

    python3 check.py -h

In particular use the log file to check your output evaluation:

    python3 check.py -l log

The accuracy on `data/input/test.tsv` will not be shown.  We will
evaluate your output on the test input after the submission deadline.

First run `zipout.py` to get the `output.zip` file.

    $ python3 zipout.py -r default.py
    Warning: output already exists. Existing files will be over-written.
    running on input data/input/dev.tsv
    running on input data/input/test.tsv
    output.zip created

Once you have `output.zip` you can run the scorer. The default
solution gets a very poor accuracy on the dev and test set:

    $ python3 check.py
    test.out score: 0.22
    dev.out score: 0.23

It is fairly easy to reach a higher score with some fairly minor
changes to the default solution.

    $ python3 check.py
    test.out score: 0.70
    dev.out score: 0.68


## Preparing your report

You should prepare a short (1-2 pages) report on what you did in this assignment.  
Your report should be organized into clear sections, with grammatical English (full sentences).  
Use figures, graphs, tables to compare results of different experiments.  

The report should include the following:
* Group name with names of group members
* A summary of the task you are addressing and what you are aiming to achieve 
* Short description of your method 
* Results (both quantitative and qualitative) comparing your method to the baseline (default) solution 
* Discussion of alternative methods you tried and how well they worked (or didn't work)
* Breakdown of contributions by each group member

Your report should be submitted as `report.pdf` to [{{site.hwp-report-submit.name}}]({{site.hwdates[1].hwp-report-submit-url}}). 
Using LaTex for preparing your reports is recommended (see [Overleaf](https://www.overleaf.com) for online editing of LaTex documents), but not required.

## Submit your homework on {{ site.hwsubmit.name }}

Once you are done with your homework submit all the relevant materials
to {{ site.hwsubmit.name }} for evaluation.

#### Create output.zip

Once you have a working solution in `answer/spellchk.py` create
the `output.zip` for upload to Coursys using:

    python3 zipout.py

#### Create source.zip

To create the `source.zip` file for upload to {{ site.hwsubmit.name }} do:

    python3 zipsrc.py

You must have the following files or `zipsrc.py` will complain about it:

* `answer/spellchk.py` -- this is your solution to the homework. start by copying `default.py` as explained below.
* `answer/spellchk.ipynb` -- this is the Python notebook that will be your write-up for the homework.

In addition, each group member should write down a short description
of what they did for this homework in the Python notebook.

### Upload to {{ site.hwsubmit.name }}

Go to `Programming Homework 1` on {{ site.hwsubmit.name }} and do a group submission:

* Upload `output.zip` and `source.zip` [{{ site.hwsubmit.name }}]({{ site.hwsubmit.url }}/+hwp1/)
{% if site.hwdates[1].hwp-report-submit-url %}
* Please upload your `report.pdf` to [{{site.hwp-report-submit.name}}]({{site.hwdates[1].hwp-report-submit-url}}) HW1-P Report.
Only one person need to submit for the group, but please [add your group members]({{site.hwp-report-submit.specify-group-url}})
so that they can see the submission and specify the name of your group in the report.
{% endif %}
* Make sure your `source.zip` matches your Github repository.
* Make sure you have documented your approach in `answer/spellchk.ipynb`.
* Make sure each member of your group has documented their contribution to this homework in `answer/README.username` where `username` is your CSIL/Github username.

## Grading

The grading is split up into the following components:

* dev scores (see Table below)
* test scores (see Table below)
* Report quality 
* Code content and quality
  * Make sure that iterative search algorithm is implemented as described in the Baseline section above
* Check if each group member has a `answer/README.username`.
* Make sure that your have updated your Github repository with your submission source code.

Your accuracy should be equal to or greater than the scores listed
for dev and test data to obtain the corresponding marks (dev and
test sets are marked separately).

| **dev accuracy** | **test accuracy** | **Marks** | **Grade** |
| .00 | .00 | 0   | F  |
| .23 | .22 | 55  | D  |
| .30 | .28 | 60  | C- |
| .36 | .34 | 65  | C  |
| .42 | .40 | 70  | C+ |
| .48 | .46 | 75  | B- |
| .54 | .52 | 80  | B  |
| .60 | .58 | 85  | B+ |
| .65 | .64 | 90  | A- |
| .68 | .70 | 95  | A  |
| .76 | .78 | 100 | A+ |
{: .table}


The score will be normalized to the marks on {{ site.hwsubmit.name }} for the dev and test scores.

