# The Unofficial Guide — Project 1

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

Unofficial Guide to UMD Computer Science Courses and Professors

My project focuses on unofficial student knowledge about UMD Computer Science courses and professors. This information is difficult to find because it is spread across sources like Rate My Professors, Reddit threads, and informal student discussions. The system will help students ask questions about workload, grading style, professor quality, exams, projects, and course difficulty.

Questions This System Should Answer
1. Who are the best UMD CS professors for teaching and lectures?
2. Which professors are good research mentors for undergraduates?
3. What do students think about a specific professor?
4. Which professors are known for difficult grading or challenging courses?
5. Which UMD CS professors are most respected for their research and accomplishments?

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

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
| 10 | Rate My Professors | Student ratings and reviews of a UMD CS professor, including feedback on teaching style, course organization, difficulty level, and overall effectiveness.                                          | [https://www.ratemyprofessors.com/professor/2549134](https://www.ratemyprofessors.com/professor/2549134) 

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**
I primarily chunked documents by individual reviews, Reddit comments, and discussion posts. Most reviews and comments remain as a single chunk. For unusually long posts, I split the text into chunks of approximately 150–180 words.

**Overlap:**
I use an overlap of approximately 30 words when splitting longer posts into multiple chunks.

**Why these choices fit your documents:**
My corpus consists mainly of Rate My Professor reviews and Reddit discussions about UMD Computer Science professors and courses. Since most reviews and comments already represent a complete thought, I preserve them as individual chunks whenever possible rather than splitting them mechanically. This helps maintain the connection between the professor, course, and student opinion.

For longer discussion posts, I use chunks of 150–180 words with a 30-word overlap. This provides enough context for semantic search while keeping the chunk focused on a specific topic. If chunks are too small, the retrieval system may return incomplete opinions or lose important context. If chunks are too large, multiple professors, courses, or viewpoints may be combined into a single chunk, reducing retrieval accuracy.

The overlap helps preserve information that appears near chunk boundaries and reduces the risk of separating important details from the surrounding context. This approach is well suited for a review-heavy corpus because it prioritizes complete student opinions and self-contained pieces of information that can be retrieved independently.

**Final chunk count:**
87

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**
I use all-MiniLM-L6-v2 from the sentence-transformers library to generate embeddings for my document chunks. I chose this model because it is free, runs locally, is easy to integrate with ChromaDB, and provides strong semantic search performance for a small-scale RAG system.

**Production tradeoff reflection:**

If I were deploying this system for real users and cost was not a constraint, I would compare different embedding models based on retrieval accuracy, latency, context understanding, and multilingual support. Larger models may provide better semantic understanding and improve retrieval quality, especially for complex or ambiguous queries, but they typically require more computational resources and slower processing times. I would also consider whether the model performs well on short, opinion-based text such as student reviews and Reddit discussions, since understanding informal language is important for this domain.

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**
The system prompt explicitly instructs the LLM to answer questions using only the retrieved document context. The prompt states:

"Answer the user's question using ONLY the provided retrieved context. Do not use outside knowledge. If the context does not contain enough information, say 'I don't have enough information in the collected documents to answer that.'"

The retrieved chunks are included directly in the prompt along with their source filenames. This ensures that the model's response is based on the retrieved documents rather than its general training knowledge. By requiring the model to decline questions that lack sufficient evidence, the system reduces the risk of hallucinations and unsupported answers.

**How source attribution is surfaced in the response:**
Each retrieved chunk is stored with metadata containing its source document name. After retrieval, the source filenames are passed alongside the chunk text and are displayed separately in the interface under a "Retrieved From" section. In addition, the prompt instructs the model to mention the source documents used when generating its answer. This provides transparency by allowing users to see exactly which Reddit threads or Rate My Professor reviews were used to generate the response. Source attribution is therefore supported both programmatically through metadata and through the generated response itself.

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | What do students say about Larry Herman? | Students describe Larry Herman very positively, calling him one of the best CS lecturers. They mention strong lectures, good project descriptions, useful practice exams, and tough but fair exams. | Larry Herman was described as one of the best CS instructors, with students praising his lectures, project organization, practice exams, and fair but challenging assessments. | Relevant | Accurate |
| 2 | Which CMSC course was most frequently mentioned as difficult in the Reddit discussion about the hardest undergraduate CS classes? | CMSC451 (Algorithms) and CMSC351 were among the most frequently mentioned difficult courses, with students specifically discussing the challenges of algorithms and proofs. | The system identified CMSC451 and CMSC351 as the courses most frequently described as difficult, highlighting algorithms, proofs, and heavy workloads. | Relevant | Accurate |
| 3 | What study advice do multiple students give for succeeding in Nelson Padua-Perez's CMSC131 and CMSC132 courses? | Students repeatedly advise starting projects early, avoiding procrastination, attending office hours, and studying practice exams because the coursework and exams can be challenging despite Nelson's strong teaching. | The system summarized that students recommend starting projects early, using office hours, avoiding procrastination, and preparing with practice exams. | Relevant | Accurate |
| 4 | Which professor was recommended for undergraduate students interested in cybersecurity research? | Dave Levin was specifically recommended as a professor for students interested in research opportunities, particularly through his Breakerspace lab. | The system identified Dave Levin as a recommended professor for cybersecurity research and referenced opportunities in his research lab. | Relevant | Accurate |
| 5 | What concern do multiple students raise about Marine Carpuat's CMSC422 course? | Multiple reviews describe the grading as harsh and state that students struggled to receive sufficient support from the teaching assistants. | The system reported recurring concerns about strict grading and limited TA support in CMSC422. | Relevant | Accurate |

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**
"What programming language is primarily used in CMSC414 with Michael Marsh?"

**What the system returned:**
I don't have enough information in the collected documents to answer that.

The provided context does not contain information about the programming language used in CMSC414 with Michael Marsh. The sources (doc3.txt, doc9.txt, doc8.txt, doc10.txt) mention Michael Marsh and various CMSC courses, but they do not specify the programming language used in CMSC414.

**Root cause (tied to a specific pipeline stage):**
This failure happened during the retrieval stage. The relevant information exists in the documents, but retrieval did not return the exact chunk that says CMSC414 is mainly taught in C. Instead, it retrieved broader chunks about Michael Marsh and CMSC414 that mentioned the course but not the programming language. Because the generation prompt only allows the LLM to answer from retrieved context, the model correctly refused to answer instead of guessing.

**What you would change to fix it:**
I would improve retrieval by increasing top_k from 4 to 5 or 6 so the system has a better chance of retrieving the specific chunk about programming language. I would also consider using hybrid search, combining semantic search with keyword matching for terms like “C,” “Java,” “Python,” and “language.” This would help factual questions that depend on exact keywords rather than broad semantic similarity.

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
The planning document helped guide the overall design of the system before implementation began. Defining the chunking strategy, retrieval approach, and evaluation questions early made it easier to build each component of the pipeline in a structured way. The evaluation plan was particularly useful because it provided concrete queries that I could use to test retrieval quality and identify problems before adding generation.

**One way your implementation diverged from the spec, and why:**
My implementation diverged from the original chunking plan. Initially, I planned to use fixed-size chunks for all documents, but after inspecting the Reddit discussions and Rate My Professor reviews, I found that many important opinions were being split across chunk boundaries. To address this, I modified the implementation to preserve complete reviews, comments, and replies whenever possible and only split unusually long discussion posts. This change produced more self-contained chunks and improved retrieval quality for review-style documents.

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

### Instance 1

- **What I gave the AI:**  
  I provided Claude with my Chunking Strategy section from `planning.md`, including the requirement to preserve complete Reddit comments and Rate My Professor reviews whenever possible. I also provided examples of my documents so the AI could understand that the corpus consisted primarily of short, opinion-based reviews and discussion posts.

- **What it produced:**  
  Claude generated a chunking function that split documents into fixed-size chunks based on word count and overlap.

- **What I changed or overrode:**  
  After inspecting the generated chunks, I found that several comments were being split in the middle of a student's opinion, creating fragmented chunks that lacked context. I modified the implementation so that complete reviews, comments, and replies remained together whenever possible and only split unusually long discussion posts. This produced more meaningful and self-contained chunks for retrieval.

### Instance 2

- **What I gave the AI:**  
  I provided Claude with my Retrieval Approach section and architecture diagram, specifying the use of the `all-MiniLM-L6-v2` embedding model, ChromaDB as the vector store, and top-k retrieval with source metadata.

- **What it produced:**  
  Claude generated code for embedding document chunks, storing them in ChromaDB, and retrieving the most relevant chunks using semantic similarity search.

- **What I changed or overrode:**  
  I extended the generated code to store additional metadata such as source filenames and chunk indices so that source attribution could be displayed in the final response. I also experimented with different top-k values and added retrieval debugging output, including similarity scores and retrieved chunk inspection, to improve retrieval quality for my evaluation questions.
