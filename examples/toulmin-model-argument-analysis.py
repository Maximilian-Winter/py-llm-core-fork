# -*- coding: utf-8 -*-
from typing import List
from dataclasses import dataclass
from llm_core.assistants import LLaMACPPAssistant


sample_paper = """
The following is a development plan for a system called MemGPT:


MemGPT introduces a novel approach to memory management in GPT, addressing the limitations of fixed context windows. It draws inspiration from traditional operating systems' hierarchical memory systems. Here's an overview:

1. **Main Context and External Context**: MemGPT distinguishes between two primary memory types: the main context (akin to RAM in operating systems) and external context (similar to disk storage). The main context represents the standard fixed-context window of modern LLMs, where all in-context data is processed. The external context holds out-of-context data, which can be brought into the main context through specific function calls.

2. **Self-Directed Editing and Retrieval**: The system autonomously updates and searches its memory, deciding when to move items between contexts. This process allows the LLM to adapt its main context to reflect evolving objectives and responsibilities. MemGPT implements this through explicit instructions guiding interactions with memory systems.

3. **Control Flow and Function Chaining**: Events such as user messages or system alerts trigger LLM inference in MemGPT. It processes these events and converts them into plain text messages, appending them to the main context for the LLM processor. Function chaining allows sequential execution of multiple functions before returning control to the user.

MemGPT's design enables it to handle unbounded context using LLMs with finite context windows, significantly enhancing their capability in tasks like document analysis and extended conversations.


###  Development Plan for MemGPT-Like System (Python Focus)

#### 1. Pythonic Class Design

- **Class: MainContext**
  - **Methods**:
    - Use Python's `list` or `deque` for `contextData` to maintain an ordered collection with efficient add/remove operations.
    - Consider using `@property` decorators for controlled access and updates to `contextSize` and `relevanceCriteria`.

- **Class: ExternalContext**
  - **Methods**:
    - Utilize Python's database connectivity (e.g., SQLite or SQLAlchemy) for `externalData` to manage large volumes of information.
    - Implement `retrievalAlgorithms` as a mix of custom functions and Python's built-in search and sort capabilities.

- **Class: ContextManager**
  - **Methods**:
    - Implement `transferPolicies` using Python's functional programming features like `lambda` and higher-order functions for dynamic decision-making.

- **Class: RetrievalSystem**
  - **Methods**:
    - Leverage Python's rich library ecosystem for `searchEngine`, possibly integrating Elasticsearch for advanced search capabilities.
    - Use a dictionary or `collections.OrderedDict` for `retrievalCache` to optimize lookups.

- **Class: MemoryPage**
  - **Methods**:
    - Use a Python `class` or `namedtuple` for `pageContent` to structure page data.
    - Implement `pageSize` logic using Python's memory management and data sizing techniques.

#### 2. Interface Design with Python

- **Interface: IMemoryManagement**
  - Use Python's Abstract Base Classes (ABC) from `abc` module to define the interface.
  - Employ Python's duck typing philosophy for flexible method implementations.

- **Interface: IContextUpdater**
  - Again, use Python's ABC for consistency.
  - Provide clear documentation on method expectations to guide implementation in Pythonic style.

#### 3. Data Flow and Control

- Emphasize clear and readable code following Python's Zen (PEP 20) for data flow implementation.
- Use Python's exception handling to manage flow control and error states.

#### 4. Additional Pythonic Considerations

- **Performance Optimization**: Utilize Python's profiling tools (like `cProfile`) to identify bottlenecks.
- **Scalability**: Leverage Python's multi-threading and multi-processing capabilities for handling large data and requests.
- **Learning and Adaptation**: Integrate machine learning libraries (like scikit-learn) for feedback mechanisms.





###  Implementation Plan for `MainContext` Class (Python Focus)

#### Purpose
`MainContext` manages the immediate, active memory space, handling dynamic data addition, removal, and context updating in a Pythonic way.

#### Pythonic Properties and Methods

1. **Properties**:
   - `context_data`: A Python `list` or `deque` for efficient data manipulation.
   - `context_size`: An integer, managed via a property decorator to encapsulate context size logic.

2. **Methods**:

   - `add_information(info)`: Adds new information to the main context.
     - Parameters:
       - `info`: The information to be added (Python object or structured data).
     - Implementation:
       - Append `info` to `context_data`.
       - If `context_data` exceeds `context_size`, trigger `update_context()`.
       - Maintain order based on relevance criteria.

   - `remove_information(info_id)`: Removes specific information from the main context.
     - Parameters:
       - `info_id`: Identifier for the information to remove.
     - Implementation:
       - Efficiently locate and remove the item from `context_data`.
       - Optional: Update context after removal.

   - `update_context()`: Updates the context based on relevance and current tasks.
     - Implementation:
       - Assess each item's relevance in `context_data` using defined criteria.
       - Move less relevant items to `ExternalContext` via `ContextManager`.

#### Pythonic Considerations

- **Efficiency**: Use Python list comprehensions for concise and efficient data manipulation.
- **Readability**: Follow PEP 8 naming conventions and Pythonic idioms for readability and maintainability.
- **Algorithmic Approach**: Implement relevance assessment using a combination of frequency analysis and topical relevance algorithms, leveraging Python's rich text processing capabilities.




###  Implementation Plan for `ExternalContext` Class (Python Focus)

#### Purpose
`ExternalContext` handles the storage and retrieval of information not actively used in the main context, employing Pythonic data structures and algorithms for efficient management.

#### Pythonic Properties and Methods

1. **Properties**:
   - `external_data`: A Python data structure or database connection to store external context information (e.g., SQLite or a Python ORM like SQLAlchemy for relational data).
   - `page_indexing`: A Python dictionary or a more sophisticated indexing system (like Elasticsearch) for efficient data categorization and retrieval.
   - `retrieval_algorithms`: Custom Python functions or built-in capabilities for information retrieval.

2. **Methods**:

   - `store_information(info)`: Stores information for long-term use.
     - Parameters:
       - `info`: The information to be stored.
     - Implementation:
       - Insert `info` into `external_data`.
       - Update `page_indexing` to efficiently categorize and index the new data.
       - Handle data integrity and duplication checks.

   - `retrieve_information(criteria)`: Retrieves information based on specific criteria.
     - Parameters:
       - `criteria`: Criteria for information retrieval (e.g., keywords, topics).
     - Implementation:
       - Use `retrieval_algorithms` to search in `external_data`.
       - Implement efficient sorting and prioritization of results.
       - Return the most relevant information for use in the main context.

#### Pythonic Considerations

- **Data Management**: Utilize Python's database connectivity for scalable data storage. Consider using ORMs for abstraction and ease of use.
- **Algorithmic Efficiency**: For `retrieval_algorithms`, leverage Python libraries like NumPy or Pandas for efficient data processing, and consider natural language processing libraries for advanced search capabilities.
- **Scalability and Performance**: Implement caching strategies (using Python's `functools.lru_cache` or similar) to improve retrieval performance, especially for frequently accessed data.




###  Implementation Plan for `ContextManager` Class (Python Focus)

#### Purpose
`ContextManager` acts as the mediator between the `MainContext` and `ExternalContext`, overseeing the transfer of information based on system requirements and context relevance.

#### Pythonic Properties and Methods

1. **Properties**:
   - `main_context`: A reference to an instance of the `MainContext` class.
   - `external_context`: A reference to an instance of the `ExternalContext` class.
   - `transfer_policies`: A set of rules or algorithms, possibly implemented as Python functions or using a strategy pattern for dynamic decision-making.

2. **Methods**:

   - `transfer_to_main_context(info_id)`: Moves information from the external to the main context.
     - Parameters:
       - `info_id`: Identifier of the information to transfer.
     - Implementation:
       - Retrieve the information from `external_context`.
       - If `main_context` is at capacity, trigger its `update_context()` method.
       - Add the retrieved information to `main_context`.

   - `transfer_to_external_context(info_id)`: Moves information from the main to the external context.
     - Parameters:
       - `info_id`: Identifier of the information to transfer.
     - Implementation:
       - Retrieve the information from `main_context`.
       - Store it in `external_context`.
       - Update `transfer_policies` as needed for future optimizations.

#### Pythonic Considerations

- **Dynamic Policy Implementation**: Use Python's dynamic and functional features (like lambda functions and decorators) to implement `transfer_policies` that can adapt to different scenarios.
- **Efficient Data Handling**: Employ Python's built-in data structures and algorithms for efficient data transfer and management between contexts.
- **Error Handling**: Implement robust error handling and logging (using Python's `logging` module) to ensure system stability and ease of debugging.





###  Implementation Plan for `RetrievalSystem` Class (Python Focus)

#### Purpose
`RetrievalSystem` enables efficient searching and retrieval of information from `ExternalContext`, using Pythonic data structures and algorithms to handle these operations effectively.

#### Pythonic Properties and Methods

1. **Properties**:
   - `external_context`: A reference to an instance of the `ExternalContext` class.
   - `search_engine`: A sophisticated search algorithm or library, potentially integrating Python libraries like Elasticsearch for advanced capabilities.
   - `retrieval_cache`: A cache system, implemented using Python dictionaries or `collections.OrderedDict` for fast access to recently retrieved information.

2. **Methods**:

   - `search_information(criteria)`: Conducts a search in the external context.
     - Parameters:
       - `criteria`: The criteria for the search (e.g., keywords, tags).
     - Implementation:
       - Utilize `search_engine` to perform the search within `external_context`.
       - Sort and rank the results based on relevance, leveraging Python's sorting capabilities.
       - Update `retrieval_cache` with the results for quicker future access.

   - `retrieve_information(info_id)`: Retrieves specific information based on its identifier.
     - Parameters:
       - `info_id`: The identifier of the information to retrieve.
     - Implementation:
       - First, check `retrieval_cache` for the information.
       - If not in cache, access `external_context` to retrieve the data.
       - Update `retrieval_cache` as needed.

#### Pythonic Considerations

- **Algorithmic Efficiency**: Leverage Python's powerful libraries for efficient search and retrieval operations.
- **Cache Optimization**: Use Python's `functools.lru_cache` or a similar mechanism for efficient caching strategies.
- **Robust Error Handling**: Implement comprehensive error handling to manage exceptions and maintain system stability.



###  Implementation Plan for `MemoryPage` Class (Python Focus)

#### Purpose
`MemoryPage` handles segments of memory within the `ExternalContext`, organizing information in a structured and efficient manner, using Pythonic data structures and algorithms.

#### Pythonic Properties and Methods

1. **Properties**:
   - `page_id`: A unique identifier for the memory page, possibly a UUID or a simple integer ID.
   - `page_content`: The actual data stored in the memory page, implemented as a Python list or dictionary, depending on the nature of the data.
   - `page_size`: The maximum size or capacity of the page, defined as an integer.
   - `last_accessed`: A timestamp (using Python's `datetime` module) to track when the page was last accessed.

2. **Methods**:

   - `store_info(info)`: Stores information in the memory page.
     - Parameters:
       - `info`: The information to be stored.
     - Implementation:
       - Append or add `info` to `page_content`, ensuring it doesn't exceed `page_size`.
       - Update `last_accessed` upon each addition of information.

   - `retrieve_info()`: Retrieves all information stored in the memory page.
     - Implementation:
       - Return the contents of `page_content`.
       - Update `last_accessed` to the current time.

#### Pythonic Considerations

- **Data Structuring**: Utilize Python's native data structures for storing and managing `page_content`, ensuring efficient access and modification.
- **Efficient Memory Usage**: Implement logic to optimize the use of `page_size`, potentially using Python's memory management tools to track and manage the size of `page_content`.
- **Timestamp Management**: Use Python's `datetime` module for accurate and efficient handling of `last_accessed`.

###  Implementation Plan for `IMemoryManagement` Interface (Python Focus)

#### Purpose
`IMemoryManagement` serves as a foundational interface for standardizing memory management operations within the system, ensuring consistency and flexibility in handling memory-related tasks.

#### Pythonic Interface Definition

1. **Using Abstract Base Classes (ABC)**:
   - Leverage Python’s `abc` module to define `IMemoryManagement` as an abstract base class, ensuring that any class implementing this interface provides concrete implementations of its methods.

2. **Method Definitions**:

   - `add_to_context(info)`: Adds information to a context (main or external).
     - Parameters:
       - `info`: The information to be added (Python object or structured data).
     - Implementation Requirements:
       - Define an abstract method that must be overridden by concrete classes, ensuring they provide a tailored addition logic based on the context's nature.

   - `remove_from_context(info_id)`: Removes information from a context based on its identifier.
     - Parameters:
       - `info_id`: Identifier of the information to be removed.
     - Implementation Requirements:
       - Specify an abstract method that enforces the implementation of efficient removal logic in concrete classes.

   - `search_context(criteria)`: Searches for information within a context based on given criteria.
     - Parameters:
       - `criteria`: Criteria for searching information.
     - Implementation Requirements:
       - Design an abstract method that must be implemented to provide context-specific search functionality, using Python's rich searching and filtering capabilities.

#### Pythonic Considerations

- **Flexibility and Robustness**: Ensure that the interface is flexible enough to accommodate various types of context-specific memory management strategies, while also enforcing a robust and consistent approach across different implementations.
- **Pythonic Naming and Style**: Adhere to Python’s naming conventions and style guide (PEP 8) for method names and parameters, enhancing readability and maintainability.
- **Documentation and Type Hints**: Provide clear documentation for each method, including Python type hints, to guide developers in implementing the interface correctly and efficiently.


### Implementation Plan for `IMemoryManagement` Interface

#### Purpose
`IMemoryManagement` serves as a contract for memory management operations, dictating the essential methods that must be present in any class that manages parts of the system's memory.

#### Method Definitions

1. **add_to_context(info)**
   - **Purpose**: Adds information to a context (main or external).
   - **Parameters**:
     - `info`: The information to be added.
   - **Implementation Requirements**:
     - Ensure that the implementation accounts for the context's size and relevance criteria.
     - Include checks and balances to maintain the integrity and order of the stored information.

2. **remove_from_context(info_id)**
   - **Purpose**: Removes information from a context based on its identifier.
   - **Parameters**:
     - `info_id`: The identifier of the information to be removed.
   - **Implementation Requirements**:
     - Implement the method to locate and remove the specified information efficiently.
     - Consider updates or adjustments needed to the context post-removal.

3. **search_context(criteria)**
   - **Purpose**: Searches for information within a context based on given criteria.
   - **Parameters**:
     - `criteria`: The criteria used to search for information.
   - **Implementation Requirements**:
     - Define how the search is conducted, considering factors like relevance, recency, and content type.
     - Ensure that the search method is optimized for speed and accuracy.

#### Additional Considerations
- **Flexibility**: Allow for different implementations of these methods in `MainContext` and `ExternalContext`, reflecting their distinct roles.
- **Consistency**: Ensure that despite different implementations, the interface provides a consistent set of operations that can be expected from any memory-managing component of the system.
- **Integration**: Design the interface to be easily integrated with other components of the system, particularly those that interact with memory management operations.

"""


@dataclass
class ToulminArgumentAnalysis:
    system_prompt = "You are a argumentation analysis expert"
    prompt = """
    Developed by philosopher Stephen E. Toulmin, the Toulmin
    method is a style of argumentation that breaks arguments down into six
    component parts:

    - claim
    - grounds
    - warrant
    - qualifier
    - rebuttal
    - backing.

    In Toulmin’s method, every argument begins with three fundamental parts:
    - the claim
    - the grounds
    - the warrant

    A claim is the assertion that authors would like to prove to their audience.
    It is, in other words, the main argument.

    The grounds of an argument are the evidence and facts that help support the claim.

    Finally, the warrant, which is either implied or stated explicitly,
    is the assumption that links the grounds to the claim.

    Backing refers to any additional support of the warrant.
    In many cases, the warrant is implied, and therefore the backing provides
    support for the warrant by giving a specific example that justifies the warrant.

    The qualifier shows that a claim may not be true in all circumstances.
    Words like “presumably,” “some,” and “many” help your audience understand
    that you know there are instances where your claim may not be correct.

    The rebuttal is an acknowledgement of another valid view of the situation.

    Here is a text we'd like to analyze:
    ```
    {content}
    ```

    > Perform a Toulmin analysis on the previous text.
    """
    claim: str
    grounds: str
    warrant: str
    qualifier: str
    rebuttal: str
    backing: str

    @classmethod
    def analyze(cls, content):
        with LLaMACPPAssistant(cls, model="mistral") as assistant:
            analysis = assistant.process(content=content)
            return analysis


if __name__ == "__main__":
    analysis = ToulminArgumentAnalysis.analyze(sample_paper)
    print(f"Claim: {analysis.claim}")
    print(f"Grounds: {analysis.grounds}")
    print(f"Warrant: {analysis.warrant}")
    print(f"Qualifier: {analysis.qualifier}")
    print(f"Rebuttal: {analysis.rebuttal}")
    print(f"Backing: {analysis.backing}")
