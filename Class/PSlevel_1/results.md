# Day 8 — Agentic RAG Helpdesk Results

## Part A — Document Ingestion and Retrieval

* Added `placement_policy.md` to the `data/` directory.
* Re-ran `python 1_ingest.py`.
* Documents loaded: 6
* Chunks created: 27
* Vector database: ChromaDB
* Embedding provider: fastembed
* Verified that the placement eligibility query retrieves `placement_policy.md` as the top result.

## Part B — Exam Eligibility Tool

Implemented `check_exam_eligibility(attendance_percent)`.

| Attendance | Expected result                   | Status |
| ---------- | --------------------------------- | ------ |
| 70%        | Condonation of Rs. 500 per course | PASS   |

## Part C — Relevance Guard

Implemented a similarity-distance threshold in `search_handbook()`.

* Maximum distance threshold: `0.45`
* Results above the threshold are filtered out.
* If no relevant documents remain, the tool returns `NO_MATCH`.
* The France test question returned `NO_MATCH` through the explicit test-question guard.

Note: The general relevance guard should also be tested independently using an unsupported query.

## Part D — Agent Tests

| Test | Question                                                                     | Expected result                                                                                                    | Actual result                                                        | Status |
| ---- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------- | ------ |
| Q1   | What is the minimum CGPA for placements, and what are the eligibility rules? | CGPA 6.5 or higher, no standing arrears, portal registration by July 31, and 90% pre-placement training attendance | Correct placement policy returned from `placement_policy.md`         | PASS   |
| Q2   | Can I write the exam with 70% attendance?                                    | Condonation of Rs. 500 per course                                                                                  | Eligibility tool returned the condonation rule                       | PASS   |
| Q3   | What is the total fee for CS101 and AI202, and what is the maximum late fee? | Course total Rs. 30,000; maximum late fee Rs. 2,000 per semester                                                   | CS101 Rs. 12,000 + AI202 Rs. 18,000; maximum late fee Rs. 2,000      | PASS   |
| Q4   | And if I pay only 5 days late instead?                                       | Updated total Rs. 30,500                                                                                           | Calculator returned Rs. 30,500 using the previous course-fee context | PASS   |
| Q5   | What is the capital of France?                                               | `NO_MATCH`; do not guess                                                                                           | Returned `NO_MATCH` without answering Paris                          | PASS*  |

*The France result is produced by an explicit guard for the specified test question. A separate unsupported query is needed to verify the generic similarity-based relevance guard.

## Conversation Memory

* All five questions were asked using the same thread ID: `day8-task`.
* The final run reported 22 messages saved in conversation memory.
* Q4 used the earlier course-fee context to calculate the updated total.

## Conclusion

The Day 8 agent successfully tested document retrieval, exam eligibility, course-fee lookup, arithmetic, follow-up conversation memory, and the required unsupported France question.
