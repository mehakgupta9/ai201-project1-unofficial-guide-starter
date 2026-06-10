# Project 1 Planning: The Unofficial Guide
---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
Unofficial Guide to UMD Computer Science Courses and Professors

My project focuses on unofficial student knowledge about UMD Computer Science courses and professors. This information is difficult to find because it is spread across sources like Rate My Professors, Reddit threads, and informal student discussions. The system will help students ask questions about workload, grading style, professor quality, exams, projects, and course difficulty.

Questions This System Should Answer
1. Who are the best UMD CS professors for teaching and lectures?
2. Which professors are good research mentors for undergraduates?
3. What do students think about a specific professor?
4. Which professors are known for difficult grading or challenging courses?
5. Which UMD CS professors are most respected for their research and accomplishments?

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| #  | Source             | Description                                                                                                                                                                                         | URL or location                                                                                                                                                                                  |
| -- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1  | Reddit (r/UMD)     | Discussion of the best CS professors at UMD, with students recommending instructors such as Larry Herman, Dave Mount, David Van Horn, and others based on teaching quality and course experiences.  | [https://www.reddit.com/r/UMD/comments/u2orir/cs_professors/](https://www.reddit.com/r/UMD/comments/u2orir/cs_professors/)                                                                       |
| 2  | Reddit (r/UMD)     | Student discussion about undergraduate research opportunities in CS, including recommendations for professors who are supportive of undergraduate researchers and advice for joining research labs. | [https://www.reddit.com/r/UMD/comments/i4baii/good_cs_professors_for_undergrads_to_do_research/](https://www.reddit.com/r/UMD/comments/i4baii/good_cs_professors_for_undergrads_to_do_research/) |
| 3  | Reddit (r/UMD)     | Discussion of CMSC414 with Michael Marsh, including student experiences regarding course workload, teaching style, assignments, and overall difficulty.                                             | [https://www.reddit.com/r/UMD/comments/ds979u/414_with_michael_marsh/](https://www.reddit.com/r/UMD/comments/ds979u/414_with_michael_marsh/)                                                     |
| 4  | Rate My Professors | Student ratings and reviews of Michael Marsh, including feedback on teaching effectiveness, course organization, grading, and difficulty.                                                           | [https://www.ratemyprofessors.com/professor/268534](https://www.ratemyprofessors.com/professor/268534)                                                                                           |
| 5  | Rate My Professors | Student evaluations and reviews of a UMD CS professor, discussing lecture quality, grading practices, course structure, and student satisfaction.                                                   | [https://www.ratemyprofessors.com/professor/2327417](https://www.ratemyprofessors.com/professor/2327417)                                                                                         |
| 6  | Rate My Professors | Student reviews and ratings of a UMD CS professor, highlighting teaching methods, workload expectations, and classroom experiences.                                                                 | [https://www.ratemyprofessors.com/professor/2361197](https://www.ratemyprofessors.com/professor/2361197)                                                                                         |
| 7  | Reddit (r/UMD)     | Discussion identifying highly accomplished and prestigious professors in UMD Computer Science, Mathematics, and Electrical Engineering based on research impact and academic recognition.           | [https://www.reddit.com/r/UMD/comments/18wa5xg/most_accomplished_professors_at_umd_csmathee/](https://www.reddit.com/r/UMD/comments/18wa5xg/most_accomplished_professors_at_umd_csmathee/)       |
| 8  | Reddit (r/UMD)     | Student discussion about the most difficult computer science courses at UMD, including experiences with advanced systems, theory, and graduate-level classes.                                       | [https://www.reddit.com/r/UMD/comments/1iwmq6y/what_is_the_hardest_cs_class_you_guys_took/](https://www.reddit.com/r/UMD/comments/1iwmq6y/what_is_the_hardest_cs_class_you_guys_took/)           |
| 9  | Reddit (r/UMD)     | Discussion about the difficulty and workload of UMD graduate-level computer science courses, including recommendations and experiences from graduate students.                                      | [https://www.reddit.com/r/UMD/comments/1tzvr3s/difficulty_of_cs_grad_classes_at_umd/](https://www.reddit.com/r/UMD/comments/1tzvr3s/difficulty_of_cs_grad_classes_at_umd/)                       |
| 10 | Rate My Professors | Student ratings and reviews of a UMD CS professor, including feedback on teaching style, course organization, difficulty level, and overall effectiveness.                                          | [https://www.ratemyprofessors.com/professor/2549134](https://www.ratemyprofessors.com/professor/2549134)                                                                                         |


---

## Initial Observations
The collected documents reveal strong student consensus around a few highly regarded professors, particularly Larry Herman, Nelson Padua-Perez, and Michael Marsh, who are frequently praised for their teaching quality, accessibility, and support for students. The reviews also highlight significant variation in student experiences, with some professors receiving consistently positive feedback while others are criticized for difficult grading, unclear instruction, or lack of support. Overall, the dataset provides a broad view of both teaching effectiveness and research reputation within the UMD Computer Science department.

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**
I will primarily chunk documents by individual reviews, Reddit comments, and discussion posts. Most reviews and comments will remain as a single chunk. For unusually long posts, I will split the text into chunks of approximately 150–180 words.

**Overlap:**
I will use an overlap of approximately 30 words when splitting longer posts into multiple chunks.

**Reasoning:**
My corpus consists mainly of Rate My Professor reviews and Reddit discussions about UMD Computer Science professors and courses. Since most reviews and comments already represent a complete thought, I will preserve them as individual chunks whenever possible rather than splitting them mechanically. This helps maintain the connection between the professor, course, and student opinion.

For longer discussion posts, I will use chunks of 150–180 words with a 30-word overlap. This provides enough context for semantic search while keeping the chunk focused on a specific topic. If chunks are too small, the retrieval system may return incomplete opinions or lose important context. If chunks are too large, multiple professors, courses, or viewpoints may be combined into a single chunk, reducing retrieval accuracy.

The overlap helps preserve information that appears near chunk boundaries and reduces the risk of separating important details from the surrounding context. This approach is well suited for a review-heavy corpus because it prioritizes complete student opinions and self-contained pieces of information that can be retrieved independently.

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
I will use all-MiniLM-L6-v2 from the sentence-transformers library to generate embeddings for my document chunks. I chose this model because it is free, runs locally, is easy to integrate with ChromaDB, and provides strong semantic search performance for a small-scale RAG system.

**Top-k:**
For each query, I will retrieve the top 4 most relevant chunks from the vector database.

**Reasoning:**
Since my corpus consists of student reviews and Reddit discussions, retrieving the top 4 chunks should provide enough context for the LLM to answer questions while keeping the retrieved information focused and relevant. If I retrieve too few chunks, the system may miss important evidence or alternative student perspectives. If I retrieve too many chunks, the context may include unrelated reviews or conflicting opinions, which could make the generated answer less accurate.

Semantic search is particularly useful for this project because students may ask questions using different wording than the original documents. For example, a query such as “Which professor explains concepts clearly?” may retrieve reviews that mention “amazing lectures,” “easy to understand explanations,” or “great teaching style,” even if the exact phrase “explains concepts clearly” never appears in the document. By comparing the meaning of the text rather than exact keywords, embeddings allow the system to find relevant information across different writing styles and vocabulary.

**Production tradeoff reflection:**
If I were deploying this system for real users and cost was not a constraint, I would compare different embedding models based on retrieval accuracy, latency, context understanding, and multilingual support. Larger models may provide better semantic understanding and improve retrieval quality, especially for complex or ambiguous queries, but they typically require more computational resources and slower processing times. I would also consider whether the model performs well on short, opinion-based text such as student reviews and Reddit discussions, since understanding informal language is important for this domain.


---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What do students say about Larry Herman? | Students describe Larry Herman very positively, calling him one of the best CS lecturers. They mention strong lectures, good project descriptions, useful practice exams, and tough but fair exams.|
| 2 | Which CMSC course was most frequently mentioned as difficult in the Reddit discussion about the hardest undergraduate CS classes? | CMSC451 (Algorithms) and CMSC351 were among the most frequently mentioned difficult courses, with students specifically discussing the challenges of algorithms and proofs. |
| 3 | What study advice do multiple students give for succeeding in Nelson Padua-Perez's CMSC131 and CMSC132 courses? | Students repeatedly advise starting projects early, avoiding procrastination, attending office hours, and studying practice exams because the coursework and exams can be challenging despite Nelson's strong teaching. |
| 4 | Which professor was recommended for undergraduate students interested in cybersecurity research? | Dave Levin was specifically recommended as a professor for students interested in research opportunities, particularly through his Breakerspace lab. |
| 5 | What concern do multiple students raise about Marine Carpuat's CMSC422 course? | Multiple reviews describe the grading as harsh and state that students struggled to receive sufficient support from the teaching assistants. |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. One challenge is that the documents are highly opinion-based and sometimes contain conflicting viewpoints. For example, one student may describe a professor as an excellent lecturer while another student may have a negative experience with the same professor. The system must present these opinions as student perspectives rather than objective facts.

2. Another challenge is retrieval accuracy. Many professors and courses are mentioned within the same Reddit thread, so the retrieval system may return chunks that are related to the general topic but not directly relevant to the user's question. This could lead to answers that include information about the wrong professor or course.

3. A third challenge is maintaining source attribution. Since the goal of the system is to provide grounded answers, every response must clearly reference the documents from which the information was retrieved. Missing or incorrect citations would reduce the trustworthiness of the system.

4. A final challenge is chunk boundaries. Important information such as a professor's name and the corresponding student opinion may appear near the boundary between two chunks. If the chunks are split poorly, the retrieval system may return incomplete information, resulting in answers that lack important context or supporting evidence.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

```text
Raw Documents
(Reddit threads, Rate My Professor reviews, text files)
        |
        v
Document Ingestion
(Python file loading + basic text cleaning)
        |
        v
Chunking
(By review/comment; 100–150 words for long posts)
        |
        v
Embedding + Vector Store
(sentence-transformers: all-MiniLM-L6-v2 + ChromaDB)
        |
        v
Retrieval
(Top-k = 4 most relevant chunks)
        |
        v
Generation
(Groq + Llama 3.3 70B with cited answers)
        |
        v
User Answer
(Grounded response with source attribution)
```

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

For the document ingestion stage, I will use Claude to help write Python code that loads `.txt` files from the `data/raw` folder, reads their contents, removes unnecessary whitespace, and stores document metadata such as the title, URL, and source. I will provide Claude with my Documents section and the project requirements for the document ingestion pipeline. I expect it to generate the file-loading and preprocessing code, and I will verify the output by ensuring all collected documents are successfully loaded and processed.

For the chunking stage, I will provide Claude with my Chunking Strategy section and ask it to implement a `chunk_text()` function. The function should preserve complete reviews, Reddit comments, and replies whenever possible, and only split longer posts into 100–150 word chunks with a 20–30 word overlap. I will verify the implementation by inspecting sample chunks to ensure that professor names, course names, and student opinions remain together.

For the embedding and vector storage stage, I will use Claude to help integrate the `all-MiniLM-L6-v2` embedding model with ChromaDB. I will provide my Retrieval Approach section and project requirements for semantic search. I expect Claude to generate code that creates embeddings, stores them in ChromaDB, and preserves metadata such as document source and chunk identifiers. I will verify this by confirming that all chunks are successfully stored and retrievable from the vector database.

For the retrieval stage, I will provide Claude with my Retrieval Approach section and ask it to implement semantic search that retrieves the top 4 most relevant chunks for a user query. I will verify retrieval quality by testing my evaluation questions and confirming that the returned chunks contain the information needed to answer the questions correctly.

For the generation stage, I will use Claude to help create a prompt template for the Groq Llama 3.3 70B model. I will provide the project requirements for grounded response generation and source attribution. I expect Claude to generate a prompt that instructs the model to answer only using the retrieved context and include citations. I will verify the output by checking that responses remain grounded in the retrieved documents and do not introduce unsupported information.


**Milestone 3 — Ingestion and chunking:**
After inspecting sample chunks, I found that preserving complete reviews and Reddit comments produced more meaningful chunks than fixed-size splitting. The final chunking strategy keeps most reviews and comments intact and only splits unusually long discussion posts. This resulted in chunks that were more self-contained and easier to retrieve accurately.

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
