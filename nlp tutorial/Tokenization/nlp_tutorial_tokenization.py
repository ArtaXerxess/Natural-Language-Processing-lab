from nltk import tokenize

quote="Bravery comes along as a gradual accumulation of discipline. -Buzz Aldrin, born 1930"

def tokenizer(quote):
    print(quote,"\n\n")
    word_tokens = tokenize.word_tokenize(text=quote)
    print("word tokens = ",word_tokens,"\n\n")
    casual_tokens=tokenize.casual_tokenize(text=quote)
    print("casual tokens = ",casual_tokens,'\n\n')
    sent_tokens = tokenize.sent_tokenize(text=quote)
    print("sentence tokens = ",sent_tokens,"\n\n")
    whitespace_tokens = tokenize.WhitespaceTokenizer().tokenize(text=quote)
    print("White space tokens = ",whitespace_tokens,"\n\n\n")


tokenizer(quote=quote)

foo = """\
What is a Token? How is it created?
Tokenization substitutes snesitive information with equivalent non senitive information. The nonsensitive, replacement information is called a token.

Tokens can be created in various ways
1. using a mathematically reversible cryptographic function with a key
2. using a non reversible function such as a hash function
3. using an index function or randomly generated number
"""


tokenizer(quote=foo)