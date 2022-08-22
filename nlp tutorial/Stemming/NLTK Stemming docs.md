# Stemmers
Stemming is the process of producing morphological variants of a root/base word. Stemming programs are commonly referred to as stemming algorithms or stemmers. A stemming algorithm reduces the words “chocolates”, “chocolatey”, “choco” to the root word, “chocolate” and “retrieval”, “retrieved”, “retrieves” reduce to the stem “retrieve”. Stemming is an important part of the pipelining process in Natural language processing. The input to the stemmer is tokenized words. How do we get these tokenized words? Well, tokenization involves breaking down the document into different words.


# NLTK Stemmers

Interfaces used to remove morphological affixes from words, leaving
only the word stem.  Stemming algorithms aim to remove those affixes
required for eg. grammatical role, tense, derivational morphology
leaving only the stem of the word.  This is a difficult problem due to
irregular words (eg. common verbs in English), complicated
morphological rules, and part-of-speech and sense ambiguities
(eg. ``ceil-`` is not the stem of ``ceiling``).



# SnowballStemmer

The following languages are supported:
Arabic, Danish, Dutch, English, Finnish, French, German,
Hungarian, Italian, Norwegian, Portuguese, Romanian, Russian,
Spanish and Swedish.

The algorithm for English is documented here:

    Porter, M. "An algorithm for suffix stripping."
    Program 14.3 (1980): 130-137.

The algorithms have been developed by Martin Porter.
These stemmers are called Snowball, because Porter created
a programming language with this name for creating
new stemming algorithms. There is more information available
at http://snowball.tartarus.org/

The stemmer is invoked as shown below:

    >>> from nltk.stem import SnowballStemmer
    >>> print(" ".join(SnowballStemmer.languages)) # See which languages are supported
    arabic danish dutch english finnish french german hungarian
    italian norwegian porter portuguese romanian russian
    spanish swedish
    >>> stemmer = SnowballStemmer("german") # Choose a language
    >>> stemmer.stem("Autobahnen") # Stem a word
    'autobahn'

Invoking the stemmers that way is useful if you do not know the
language to be stemmed at runtime. Alternatively, if you already know
the language, then you can invoke the language specific stemmer directly:

    >>> from nltk.stem.snowball import GermanStemmer
    >>> stemmer = GermanStemmer()
    >>> stemmer.stem("Autobahnen")
    'autobahn'

:param language: The language whose subclass is instantiated.
:type language: str or unicode
:param ignore_stopwords: If set to True, stopwords are
                            not stemmed and returned unchanged.
                            Set to False by default.
:type ignore_stopwords: bool
:raise ValueError: If there is no stemmer for the specified
                        language, a ValueError is raised.



# PorterStemmer

A word stemmer based on the Porter stemming algorithm.

    Porter, M. "An algorithm for suffix stripping."
    Program 14.3 (1980): 130-137.

See https://www.tartarus.org/~martin/PorterStemmer/ for the homepage
of the algorithm.

Martin Porter has endorsed several modifications to the Porter
algorithm since writing his original paper, and those extensions are
included in the implementations on his website. Additionally, others
have proposed further improvements to the algorithm, including NLTK
contributors. There are thus three modes that can be selected by
passing the appropriate constant to the class constructor's `mode`
attribute:

- PorterStemmer.ORIGINAL_ALGORITHM

    An implementation that is faithful to the original paper.

    Note that Martin Porter has deprecated this version of the
    algorithm. Martin distributes implementations of the Porter
    Stemmer in many languages, hosted at:

    https://www.tartarus.org/~martin/PorterStemmer/

    and all of these implementations include his extensions. He
    strongly recommends against using the original, published
    version of the algorithm; only use this mode if you clearly
    understand why you are choosing to do so.

- PorterStemmer.MARTIN_EXTENSIONS

    An implementation that only uses the modifications to the
    algorithm that are included in the implementations on Martin
    Porter's website. He has declared Porter frozen, so the
    behaviour of those implementations should never change.

- PorterStemmer.NLTK_EXTENSIONS (default)

    An implementation that includes further improvements devised by
    NLTK contributors or taken from other modified implementations
    found on the web.

For the best stemming, you should use the default NLTK_EXTENSIONS
version. However, if you need to get the same results as either the
original algorithm or one of Martin Porter's hosted versions for
compatibility with an existing implementation or dataset, you can use
one of the other modes instead.


# RegexpStemmer

A stemmer that uses regular expressions to identify morphological
affixes.  Any substrings that match the regular expressions will
be removed.

    >>> from nltk.stem import RegexpStemmer
    >>> st = RegexpStemmer('ing$|s$|e$|able$', min=4)
    >>> st.stem('cars')
    'car'
    >>> st.stem('mass')
    'mas'
    >>> st.stem('was')
    'was'
    >>> st.stem('bee')
    'bee'
    >>> st.stem('compute')
    'comput'
    >>> st.stem('advisable')
    'advis'

:type regexp: str or regexp
:param regexp: The regular expression that should be used to
    identify morphological affixes.
:type min: int
:param min: The minimum length of string to stem




# LancasterStemmer

Lancaster Stemmer is the most aggressive stemming algorithm. It has an edge over other stemming techniques because it offers us the functionality to add our own custom rules in this algorithm when we implement this using the NLTK package. This sometimes results in abrupt results.


    >>> from nltk.stem.lancaster import LancasterStemmer
    >>> st = LancasterStemmer()
    >>> st.stem('maximum')     # Remove "-um" when word is intact
    'maxim'
    >>> st.stem('presumably')  # Don't remove "-um" when word is not intact
    'presum'
    >>> st.stem('multiply')    # No action taken if word ends with "-ply"
    'multiply'
    >>> st.stem('provision')   # Replace "-sion" with "-j" to trigger "j" set of rules
    'provid'
    >>> st.stem('owed')        # Word starting with vowel must contain at least 2 letters
    'ow'
    >>> st.stem('ear')         # ditto
    'ear'
    >>> st.stem('saying')      # Words starting with consonant must contain at least 3
    'say'
    >>> st.stem('crying')      #     letters and one of those letters must be a vowel
    'cry'
    >>> st.stem('string')      # ditto
    'string'
    >>> st.stem('meant')       # ditto
    'meant'
    >>> st.stem('cement')      # ditto
    'cem'
    >>> st_pre = LancasterStemmer(strip_prefix_flag=True)
    >>> st_pre.stem('kilometer') # Test Prefix
    'met'
    >>> st_custom = LancasterStemmer(rule_tuple=("ssen4>", "s1t."))
    >>> st_custom.stem("ness") # Change s to t
    'nest'


## StemmerI

A processing interface for removing morphological affixes from
words.  This process is known as stemming.