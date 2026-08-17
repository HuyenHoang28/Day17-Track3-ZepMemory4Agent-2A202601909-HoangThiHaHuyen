# Lab 17 Submission

## Phân tích memory

Trong bộ test này, **long-term memory** quan trọng nhất vì phục vụ bốn case trực tiếp (E02, E03, E08, E09) và là một nửa của case mixed E07. Short-term chỉ phù hợp với thông tin còn trong thread hiện tại.

Context Block/Zep Cloud cung cấp user graph, Context Block, episode/fact retrieval và xử lý relevance/recency mà không phải tự xây toàn bộ pipeline. Redis + Qdrant local cho quyền kiểm soát dữ liệu, chi phí và độ trễ tốt hơn, nhưng nhóm phải tự thiết kế schema, embedding, ranking, namespace và compaction.

Guardrail chống memory poisoning gồm consent/opt-in, redact PII, user-scoped namespace, lưu source/timestamp/confidence/validity, ưu tiên fact mới trong đúng scope, và human review cho preference có tác động lớn. Heartbeat không được tự cấp quyền hoặc ghi instruction mới.

## Benchmark

Golden set `G01-G20` đạt **20/20 PASS**, tương đương bonus **+10/10**.

Student đạt **11/11 PASS (100%)**, trong đó mỗi layer đều đạt 100% trên các case của layer; không có layer nào có hit rate thấp hơn. No-memory chỉ đạt **2/11 (18.2%)**, cho thấy token reduction không đồng nghĩa retrieval đúng.

E02 retrieve nhiều token nhất (**1,384 tokens**). E07 cần kết hợp **long-term + semantic**: evidence bắt buộc là preference `Python` và policy `Idempotency-Key`.

Memory-enabled giảm trung bình **14.2%** token so với full source context; no-memory giảm **81.8%** vì gần như trả context rỗng, nên rẻ nhưng sai.

E08 dùng recency + scope: `TypeScript/NestJS` mới nhất cho `BLUEBIRD-42` override preference Python chung trong project đó, nhưng không xóa preference Python của `ORCHID-27`. E10 compaction giữ durable note `REVIEW-DEADLINE-1600`, `Friday`, `16:00` cùng recent turns; buffer không có giới hạn nên không phù hợp khi transcript tăng dài.
