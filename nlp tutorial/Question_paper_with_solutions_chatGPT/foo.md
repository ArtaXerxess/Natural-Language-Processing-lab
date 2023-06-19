
## 3c. POS Tagging

Part-of-speech (POS) tagging is the process of assigning grammatical labels (such as noun, verb, adjective, etc.) to words in a text corpus. While POS tagging can be a useful task in natural language processing, it does come with certain challenges. Here are some common challenges faced in POS tagging:

1. Ambiguity: Many words in natural language can have multiple meanings or can function as different parts of speech depending on the context. For example, the word "run" can be a noun (e.g., "a morning run") or a verb (e.g., "to run a race"). Resolving such ambiguities accurately can be challenging.

2. Out-of-vocabulary (OOV) words: POS taggers are typically trained on a labeled corpus, and they may struggle with words that are not present in their training data. OOV words are often encountered in domains or languages that are not well-represented in the training data.

3. Idiomatic expressions and colloquial language: POS tagging models may struggle with idiomatic expressions, slang, or colloquial language that deviates from standard grammar. These linguistic variations can be difficult to capture accurately.

4. Word boundary detection: In some languages, there may not be clear spaces or delimiters between words. This makes it challenging to identify word boundaries, which can affect the accuracy of POS tagging.

5. Cross-lingual variations: POS tagging models trained on one language may not perform well when applied to another language due to variations in grammar, word order, and word classes. Transferring models across languages requires addressing these linguistic differences.

6. Domain-specific challenges: POS tagging models trained on general text may not perform well on domain-specific texts. For instance, medical or legal texts often have specialized terminology and language patterns that can pose challenges for POS tagging.

7. Error propagation: Errors made during POS tagging can propagate to downstream tasks, such as parsing or machine translation, affecting their performance. Therefore, accurate POS tagging is crucial to the overall accuracy of natural language processing systems.

Addressing these challenges often involves training POS taggers on diverse and representative datasets, incorporating contextual information, leveraging morphological features, and using advanced machine learning techniques like neural networks or statistical models.

It's important to note that the field of natural language processing is constantly evolving, and researchers are continuously working to overcome these challenges and improve the accuracy of POS tagging models.


## 3b. Yarowski bootstrapping approach to semi supervised learning

The Yarowsky bootstrapping approach is a technique used in semi-supervised learning to leverage a small amount of labeled data along with a larger amount of unlabeled data to improve the performance of a machine learning model. It is a method in NLP to improve the accuracy of the classifier used for word sense disambiguation. It works by using a small amount of manually labeled data to train a classifier to automatically label a larger amount of unlabelled data.

The Yarowsky bootstrapping algorithm follows an iterative process and can be summarized in the following steps:

1. Initialization: Initially, a small labeled dataset is provided, where a subset of the data points is labeled with their corresponding classes. The remaining data points are unlabeled. In addition, a machine learning model, such as a classifier, is also initialized.

2. Training: The model is trained on the labeled data using supervised learning techniques. This step aims to create an initial model that can make predictions based on the available labeled data.

3. Labeling: The trained model is used to predict labels for the unlabeled data points. These predictions are not guaranteed to be accurate since the model is trained on limited labeled data. However, these predictions are treated as pseudo-labels for the unlabeled data.

4. Expansion: The pseudo-labeled data is added to the labeled dataset, increasing the amount of labeled data for the next iteration. The augmented labeled dataset is then used to retrain the model.

5. Iteration: Steps 3 and 4 are repeated for a fixed number of iterations or until convergence is achieved. In each iteration, the model is trained on the expanded labeled dataset, and pseudo-labels are assigned to the unlabeled data based on the current model's predictions.

6. Convergence: The algorithm terminates when the model's performance on the unlabeled data stops improving or reaches a predefined threshold. At this point, the model is considered to have achieved a stable and accurate representation of the data.

The Yarowsky bootstrapping approach takes advantage of the labeled data to train a model initially and then uses the model's predictions on the unlabeled data to iteratively expand the labeled dataset. By gradually incorporating more reliable pseudo-labels into the training process, the model can learn from the initially small labeled dataset and generalize better to the larger unlabeled dataset.

It is important to note that the Yarowsky bootstrapping approach assumes that the initial labeled data is reasonably accurate and that the unlabeled data is representative of the true distribution. Therefore, the effectiveness of the approach heavily relies on the quality and representativeness of the available data.


## 5A Word Sense Disambiguation
Word sense disambiguation, in natural language processing (NLP), may be defined as the ability to determine which meaning of word is activated by the use of word in a particular context. Lexical ambiguity, syntactic or semantic, is one of the very first problem that any NLP system faces. Part-of-speech (POS) taggers with high level of accuracy can solve Word’s syntactic ambiguity. On the other hand, the problem of resolving semantic ambiguity is called WSD (word sense disambiguation). Resolving semantic ambiguity is harder than resolving syntactic ambiguity.

For example, consider the two examples of the distinct sense that exist for the word “bass” −

I can hear bass sound.

He likes to eat grilled bass.

The occurrence of the word bass clearly denotes the distinct meaning. In first sentence, it means frequency and in second, it means fish. Hence, if it would be disambiguated by WSD then the correct meaning to the above sentences can be assigned as follows −

I can hear bass/frequency sound.

He likes to eat grilled bass/fish.

## 5B Hobbs Algorithm

[article](https://medium.com/analytics-vidhya/hobbs-algorithm-pronoun-resolution-7620aa1af538)

The Hobbs algorithm is a pronoun resolution algorithm proposed by William A. Hobbs in 1978. It aims to determine the antecedent (the noun phrase to which a pronoun refers) for a pronoun in a given text. The algorithm follows a set of rules based on syntactic and semantic cues to make an educated guess about the intended antecedent.

Here is a simplified explanation of the Hobbs algorithm:

1. Start from the position of the pronoun: The algorithm begins by identifying the pronoun in the text and takes note of its position in the sentence.

2. Traverse the parse tree: The algorithm traverses the parse tree of the sentence, moving upward from the pronoun's position. It follows specific paths in the tree to search for potential antecedents.

3. Move to the nearest noun phrase: The algorithm moves up the parse tree to the nearest noun phrase that could potentially serve as the antecedent. This noun phrase is often found in the sentence containing the pronoun.

4. Check for prepositional phrases: If the noun phrase found in step 3 is followed by a prepositional phrase, the algorithm moves to the prepositional phrase and considers the noun phrase within it as a potential antecedent.

5. Handle relative clauses: If the noun phrase found in step 3 is part of a relative clause (a subordinate clause beginning with a relative pronoun like "who" or "that"), the algorithm moves to the clause and considers the noun phrase within it as a potential antecedent.

6. Handle coordination: If the noun phrase found in step 3 is part of a coordinated structure (e.g., "John and Mary"), the algorithm considers the entire coordination as a potential antecedent.

7. Repeat steps 3-6: The algorithm repeats steps 3 to 6, moving further up the parse tree to find additional potential antecedents.

8. Apply syntactic and semantic constraints: At each potential antecedent, the algorithm applies syntactic and semantic constraints to assess the likelihood of it being the correct antecedent. These constraints can include grammatical agreement, animacy, and discourse coherence.

9. Choose the most likely antecedent: After considering all potential antecedents, the algorithm selects the most likely one based on the applied constraints. The chosen antecedent is then considered the resolved reference for the pronoun.

The Hobbs algorithm provides a systematic approach to pronoun resolution by considering the hierarchical structure of the sentence and incorporating syntactic and semantic cues. However, it has limitations and may not always produce accurate results, especially in cases where there are multiple plausible antecedents or complex sentence structures.

In the Hobbs algorithm, a parse tree represents the syntactic structure of a sentence. To create a parse tree, you can follow these simple steps:

1. Start with the sentence: Take the sentence you want to analyze and break it down into individual words.

2. Identify the parts of speech: Assign a part of speech (such as noun, verb, adjective, etc.) to each word in the sentence. This step helps determine the grammatical role of each word.

3. Determine the sentence structure: Analyze the relationship between words to identify the sentence structure. This involves identifying the subject, verb, and other elements in the sentence.

4. Create a hierarchical structure: Construct a hierarchical structure by grouping words together based on their syntactic relationships. This structure is represented as a tree, with the main sentence at the top and its constituent parts branching out below.

5. Assign labels: Label each node in the parse tree with the appropriate part of speech or syntactic category.

By following these steps, you can create a parse tree that visually represents the syntactic structure of a sentence. The parse tree is then used in the Hobbs algorithm to navigate and analyze the sentence for pronoun resolution.

