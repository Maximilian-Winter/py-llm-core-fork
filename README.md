# PyLLMCore

## Overview

PyLLMCore is a light-weighted structured interface with Large Language Models 
with native support for [llama.cpp](http://github.com/ggerganov/llama.cpp) and OpenAI API.

The design decisions behind PyLLMCore are:

- Sane defaults
- Clear abstractions and terminology
- Out of the box utility classes

## Main benefits of using PyLLMCore

- Pythonic API
- Simple to use
- You need structures *everywhere* (provided by the standard library `dataclasses` module)
- High-level API with the `assistants` module
- Switching between models has never been easier

## Why you shouldn't use PyLLMCore

- You need a lot of external integrations: Take a look at [langchain](https://github.com/langchain-ai/langchain)
- You need tremendous performance: Take a look at [vllm](https://github.com/vllm-project/vllm)
- You don't need OpenAI: Take a look a [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) (which is integrated in PyLLMCore)
- You use Pydantic and don't use the dataclasses module


## Models supported

Besides OpenAI API, the following models are supported for local inference using the [llama.cpp](http://github.com/ggerganov/llama.cpp):

- LLaMA
- LLaMA 2
- Falcon
- [Alpaca](https://github.com/ggerganov/llama.cpp#instruction-mode-with-alpaca)
- [GPT4All](https://github.com/ggerganov/llama.cpp#using-gpt4all)
- [Chinese LLaMA / Alpaca](https://github.com/ymcui/Chinese-LLaMA-Alpaca) and [Chinese LLaMA-2 / Alpaca-2](https://github.com/ymcui/Chinese-LLaMA-Alpaca-2)
- [Vigogne (French)](https://github.com/bofenghuang/vigogne)
- [Vicuna](https://github.com/ggerganov/llama.cpp/discussions/643#discussioncomment-5533894)
- [Koala](https://bair.berkeley.edu/blog/2023/04/03/koala/)
- [OpenBuddy 🐶 (Multilingual)](https://github.com/OpenBuddy/OpenBuddy)
- [Pygmalion 7B / Metharme 7B](#using-pygmalion-7b--metharme-7b)
- [WizardLM](https://github.com/nlpxucan/WizardLM)
- [Baichuan-7B](https://huggingface.co/baichuan-inc/baichuan-7B) and its derivations (such as [baichuan-7b-sft](https://huggingface.co/hiyouga/baichuan-7b-sft))
- [Aquila-7B](https://huggingface.co/BAAI/Aquila-7B) / [AquilaChat-7B](https://huggingface.co/BAAI/AquilaChat-7B)
- [Starcoder models](https://github.com/ggerganov/llama.cpp/pull/3187)
- [Mistral AI v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1)

## Use cases

PyLLMCore covers a narrow range of use cases and serves as a building brick:

- Parsing: see the `parsers` module
- Summarizing: see the `assistants.summarizers` module
- Question answering: see the `assistants.analyst` module
- Hallucinations reduction: see the `assistants.verifiers` module
- Context size management: see the `splitters` module
- Tokenizing, encoding, decoding: see the `token_codecs` module


## Changelog

- 2.0.0: 
    + Refactored code
    + Dynamically enable GPU offloading on MacOS
    + Added configuration option for storing local models (MODELS_CACHE_DIR)
    + Updated documentation

- 1.4.0: Free up resources in LLamaParser when exiting the context manager
- 1.3.0: Support for LLaMA based models (llama, llama2, Mistral Instruct)
- 1.2.0: Chain of density prompting implemented with OpenAI
- 1.1.0: Chain of Verification implemented with OpenAI
- 1.0.0: Initial version

## Install

### Quick start

```shell
pip install py-llm-core

# Add you OPENAI_API_KEY to the environment
export OPENAI_API_KEY=sk-<replace with your actual api key>

# For local inference with GGUF models, store your models in MODELS_CACHE_DIR
mkdir -p ~/.cache/py-llm-core/models
cd ~/.cache/py-llm-core/models
wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf

```

### Troubleshooting

The `llama-cpp-python` dependency may improperly detects the architecture and raise an error `an incompatible architecture (have 'x86_64', need 'arm64'))`.

If that's the case, run the following in your virtual env:

```shell
CMAKE_ARGS="-DCMAKE_OSX_ARCHITECTURES=arm64" pip3 install --upgrade --verbose --force-reinstall --no-cache-dir llama-cpp-python
```


## Documentation

### Parsing

#### Use Parser classes

Available parsers:

- `parsers.OpenAIParser`
- `parsers.LLaMACPPParser`

#### Using a local model : Mistral AI Instruct

```python
from dataclasses import dataclass
from llm_core.parsers import LLaMACPPParser

@dataclass
class Book:
    title: str
    summary: str
    author: str
    published_year: int

text = """Foundation is a science fiction novel by American writer
Isaac Asimov. It is the first published in his Foundation Trilogy (later
expanded into the Foundation series). Foundation is a cycle of five
interrelated short stories, first published as a single book by Gnome Press
in 1951. Collectively they tell the early story of the Foundation,
an institute founded by psychohistorian Hari Seldon to preserve the best
of galactic civilization after the collapse of the Galactic Empire.
"""


with LLaMACPPParser(Book, model="mistral-7b-instruct-v0.1.Q4_K_M.gguf") as parser:
    book = parser.parse(text)
    print(book)
```

```python
Book(
    title='Foundation',
    summary="""Foundation is a science fiction novel by American writer
        Isaac Asimov. It is the first published in his Foundation Trilogy
        (later expanded into the Foundation series). Foundation is a
        cycle of five interrelated short stories, first published as a
        single book by Gnome Press in 1951. Collectively they tell the
        early story of the Foundation, an institute founded by 
        psychohistorian Hari Seldon to preserve the best of galactic
        civilization after the collapse of the Galactic Empire.""",
    author='Isaac Asimov',
    published_year=1951
)
```

#### Using OpenAI

```python
from dataclasses import dataclass
from llm_core.parsers import OpenAIParser


@dataclass
class Book:
    title: str
    summary: str
    author: str
    published_year: int


text = """Foundation is a science fiction novel by American writer
Isaac Asimov. It is the first published in his Foundation Trilogy (later
expanded into the Foundation series). Foundation is a cycle of five
interrelated short stories, first published as a single book by Gnome Press
in 1951. Collectively they tell the early story of the Foundation,
an institute founded by psychohistorian Hari Seldon to preserve the best
of galactic civilization after the collapse of the Galactic Empire.
"""


with OpenAIParser(Book) as parser:
    book = parser.parse(text)
    print(book)
```

```python
Book(
    title='Foundation',
    summary="""Foundation is a cycle of five interrelated
    short stories, first published as a single book by Gnome Press in 1951.
    Collectively they tell the early story of the Foundation, an institute
    founded by psychohistorian Hari Seldon to preserve the best of galactic
    civilization after the collapse of the Galactic Empire.""",
    author='Isaac Asimov',
    published_year=1951
)
```


### Perform advanced tasks

#### Overview

To perform generic tasks, you will use the `assistants` module that provides generic assistants:

- `assistants.OpenAIAssistant`
- `assistants.LLaMACPPAssistant`

Using these assistants, you can take a look at how the utilities are built:

- `assistants.analysts.Analyst`
- `assistants.verifiers.Doubter`
- `assistants.verifiers.ConsistencyVerifier`
- `assistants.summarizers.Summarizer`


#### Create your own utility

There are 3 items required to build and run a utility:

- A language model (any compatible model)
- An assistant class: This is where your logic is written
- A results class: This is the structure you need. It also contains the prompt.

Here is an example where `Recipe` is the results class. We'll use the 
Mistral AI Instruct model.

```python
from typing import List
from dataclasses import dataclass

# LLaMACPPAssistant is needed to instanciate Mistral Instruct
from llm_core.assistants import LLaMACPPAssistant

# Make sure that ~/.cache/py-llm-core/models contains the following file
model = "mistral-7b-instruct-v0.1.Q4_K_M.gguf"

@dataclass
class Recipe:
    system_prompt = "You are a world-class chef"
    prompt = "Write a step-by-step recipe to make {dish}"

    title: str
    steps: List[str]
    ingredients: List[str]


class Chef:
    def generate_recipe(self, dish):
        with LLaMACPPAssistant(Recipe, model=model) as assistant:
            recipe = assistant.process(dish=dish)
            return recipe

chef = Chef()
recipe = chef.generate_recipe("Boeuf bourguignon")
print(recipe)

```

#### Summarizing

```python
import wikipedia
from llm_core.assistants import Summarizer, LLaMACPPAssistant


summarizer = Summarizer(
    model="mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    assistant_cls=LLaMACPPAssistant
)

text = wikipedia.page("Foundation from Isaac Asimov").content

# To summarize only with 50% of the model context size
partial_summary = summarizer.fast_summarize(text)

# Iterative summaries on the whole content
for summary in summarizer.summarize(text):
    print(summary)

```

The partial summary generated is:

```python
SimpleSummary(
    content="""The Foundation series is a science fiction book series written
        by Isaac Asimov. It was first published as a series of short stories and
        novellas in 1942-50, and subsequently in three collections in 1951-53.
        ...
    """
)
```

#### Reduce hallucinations using the verifiers module

This example implements loosely the Chain of Verification (CoVe).

To reduce hallucinations in the LLM completions, you can use the following example
as a starting point:

```python
import requests
from llm_core.splitters import TokenSplitter
from llm_core.assistants import (
    Analyst,
    Doubter,
    ConsistencyVerifier,
    LLaMACPPAssistant,
)

pizza_dough_recipe_url = (
    "https://raw.githubusercontent.com/hendricius/pizza-dough/main/README.md"
)

model = "mistral-7b-instruct-v0.1.Q4_K_M.gguf"
assistant_cls = LLaMACPPAssistant

# Utilities
analyst = Analyst(model, assistant_cls)
doubter = Doubter(model, assistant_cls)
verifier = ConsistencyVerifier(model, assistant_cls)

# Fetch some content 
splitter = TokenSplitter(model=model, chunk_size=3_000)
pizza_dough_recipe = requests.get(pizza_dough_recipe_url).text
context = splitter.first_extract(pizza_dough_recipe)


query = "Write 3 advices when making pizza dough."

analyst_response = analyst.ask(query, context)

question_collection = doubter.verify(query, analyst_response.content)
questions = question_collection.questions

answers = []

for question in questions:
    response = analyst.ask(question, context=context)
    answers.append(response.content)

for question, answer in zip(questions, answers):
    verifications = verifier.verify(
        question=question, context=context, answer=response.content
    )

```

Here is a summary of what's been printed:

```txt
> Baseline answer:

When making pizza dough, it is important to choose high-protein flour such as bread or all-purpose flour.
The dough should be mixed and kneaded for a long time to develop flavor and gluten.
It is also important to let the dough rest and rise before shaping it into pizza balls.

> Questions

1. Is bread or all-purpose flour a good choice for making pizza dough?
2. How long should the dough be mixed and kneaded for flavor development and gluten formation?
3. Should the dough be allowed to rest and rise before shaping it into pizza balls?
4. What is the purpose of mixing and kneading the dough?
5. Is there a specific step in making pizza dough that can be skipped?

> Consistency checks

1.

Bread or all-purpose flour is a good choice for making pizza dough.
The rule of thumb is to pick a flour that has high protein content.

AnswerConsistency(is_consistent=True, is_inferred_from_context=True)


2.

The dough should be mixed and kneaded for around 5 minutes.
The mixing process starts the germination of the flour, which develops the flavor of the dough.
Kneading helps to form the gluten network that gives the dough its elasticity and structure.

AnswerConsistency(is_consistent=True, is_inferred_from_context=True)

...

```

From there, you can further process answers to remove any hallucinations or inconsistencies.


#### Using the assistants module

The following example using the `assistants.analysts` module shows how to use assistants to generate a simple recommendation.

```python
from dataclasses import dataclass
from llm_core.assistants import Analyst, Answer, LLaMACPPAssistant

context = """
Foundation is a science fiction novel by American writer
Isaac Asimov. It is the first published in his Foundation Trilogy (later
expanded into the Foundation series). Foundation is a cycle of five
interrelated short stories, first published as a single book by Gnome Press
in 1951. Collectively they tell the early story of the Foundation,
an institute founded by psychohistorian Hari Seldon to preserve the best
of galactic civilization after the collapse of the Galactic Empire.
----
The user likes the movie Interstellar
"""

@dataclass
class Recommendation(Answer):
    is_recommended: bool


analyst = Analyst(
    model="mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    assistant_cls=LLaMACPPAssistant,
    results_cls=Recommendation,
)

response = analyst.ask("Should we recommend Foundation ?", context=context)
print(response)
```

```python
Recommendation(
    content='Foundation is a science fiction novel by Isaac Asimov that tells the early story of the Foundation, an institute founded by psychohistorian Hari Seldon to preserve the best of galactic civilization after the collapse of the Galactic Empire. The user has not mentioned any specific reasons for liking or disliking the movie Interstellar, so it is difficult to determine if they would also enjoy Foundation. However, if the user enjoys science fiction and exploring complex ideas about the future of humanity, then Foundation may be a good recommendation.',
    is_recommended=True
)
```


## Tokenizer

Tokenizers are registered as a codecs within the Python
codecs registry :

```python
import llm_core
import codecs

text = """Foundation is a science fiction novel by American writer
Isaac Asimov. It is the first published in his Foundation Trilogy (later
expanded into the Foundation series). Foundation is a cycle of five
interrelated short stories, first published as a single book by Gnome Press
in 1951. Collectively they tell the early story of the Foundation,
an institute founded by psychohistorian Hari Seldon to preserve the best
of galactic civilization after the collapse of the Galactic Empire.
"""


# You can encode the text into tokens like that:


# tokens = codecs.encode(text, 'gpt-3.5-turbo')
tokens = codecs.encode(text, 'mistral-7b-instruct-v0.1.Q4_K_M.gguf')

print(tokens)
[19137, 374, 264, 8198, ... 627]

print(len(tokens))

100
```


## Chunking and splitting

```python
from llm_core.splitters import TokenSplitter


text = """Foundation is a science fiction novel by American writer
Isaac Asimov. It is the first published in his Foundation Trilogy (later
expanded into the Foundation series). Foundation is a cycle of five
interrelated short stories, first published as a single book by Gnome Press
in 1951. Collectively they tell the early story of the Foundation,
an institute founded by psychohistorian Hari Seldon to preserve the best
of galactic civilization after the collapse of the Galactic Empire.
"""


splitter = TokenSplitter(model="mistral-7b-instruct-v0.1.Q4_K_M.gguf", chunk_size=50, chunk_overlap=0)

for chunk in splitter.chunkify(text):
    print(chunk)

```
