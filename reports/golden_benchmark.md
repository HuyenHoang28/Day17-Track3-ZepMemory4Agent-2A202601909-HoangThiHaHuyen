# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1340.2 ms**
- Average token reduction vs full source context: **4.2%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.4 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| G06 | long_term | PASS | 1563.5 | 1097 | 0.0% |  |
| G09 | semantic | PASS | 232.8 | 418 | 8.9% |  |
| G10 | semantic | PASS | 235.9 | 270 | 41.2% |  |
| G14 | mixed | PASS | 2129.9 | 581 | 0.0% |  |
| G03 | long_term | PASS | 2281.9 | 1664 | 0.0% |  |
| G04 | long_term | PASS | 1465.3 | 1675 | 0.0% |  |
| G07 | episodic | PASS | 360.5 | 564 | 0.0% |  |
| G08 | episodic | PASS | 290.0 | 578 | 0.0% |  |
| G11 | mixed | PASS | 2801.0 | 581 | 0.0% |  |
| G13 | mixed | PASS | 699.1 | 500 | 11.5% |  |
| G15 | mixed | PASS | 2229.6 | 831 | 0.0% |  |
| G16 | mixed | PASS | 1756.4 | 581 | 0.0% |  |
| G17 | mixed | PASS | 2156.1 | 581 | 0.0% |  |
| G18 | mixed | PASS | 571.9 | 500 | 11.5% |  |
| G19 | mixed | PASS | 2195.6 | 581 | 0.0% |  |
| G05 | long_term | PASS | 1682.9 | 1733 | 0.0% |  |
| G12 | mixed | PASS | 2119.6 | 560 | 11.4% |  |
| G20 | mixed | PASS | 2031.1 | 756 | 0.0% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G06 - long_term

`<PRIORITY_EVIDENCE> Summary: LOTUS-88 is a project. Lan Tran is associated with LOTUS-88 and prioritizes Java and Spring Boot for backend examples, not Python. }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend. The user's project is LOTUS-88. They prioritize Java and Spring Boot for their backend development and do not use Python for backend examples. Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples. }: Lan uu tien stack backend nao cho LOTUS-88? Summary: The user's project is LOTUS-88. They prioritize Java and Spring Boot for their backend development and do not use Python for bac`

### G09 - semantic

`EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3.","source":"lab-design-note","updated_at":"2026-08-13T00:00:00Z"} metadata= EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry `

### G10 - semantic

`EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3.","source":"lab-design-note","updated_at":"2026-08-13T00:00:00Z"} metadata= EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memo`

### G14 - mixed

`<LONG_TERM> <PRIORITY_EVIDENCE> Summary: LOTUS-88 is a project. Lan Tran is associated with LOTUS-88 and prioritizes Java and Spring Boot for backend examples, not Python. }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend. }: Lan uu tien stack backend nao cho LOTUS-88? The user's project is LOTUS-88. They prioritize Java and Spring Boot for their backend development and do not use Python for backend examples. Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples. Summary: Python is not used in the backend for the LOTUS-88 project. Summary: Lan Tran is working on the LOTUS-88 project. La`

### G03 - long_term

`<PRIORITY_EVIDENCE> Summary: For project BLUEBIRD-42, backend development must use TypeScript with NestJS; Python is not permitted. Minh Nguyen prefers Python for personal demos, specifically for project ORCHID-27. The scope has been clarified: BLUEBIRD-42 will use TypeScript/NestJS, and ORCHID-27 will... For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos like ORCHID-27. The user's personal project is named ORCHID-27. }: Voi demo ca nhan cua Minh, ngon ngu uu tien la gi? - Minh Nguyen is working on personal demos for project ORCHID-27. (2026-08-05 08:00:00) FACT: Minh Nguyen is working on personal demos for`

### G04 - long_term

`<PRIORITY_EVIDENCE> For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos like ORCHID-27. The user's personal project is named ORCHID-27. }: Minh con mot open-loop phai nop truoc deadline, dong thoi muon ghi chu retry payment dung so lan toi da theo policy. Nac lai ma task/deadline con dang do, va gioi han retry chinh thuc trong lab. Summary: Minh Nguyen needs to complete the benchmark report before Friday at 16:00. This is open loop LAB-REPORT-1600. Summary: Minh Nguyen's personal project is ORCHID-27. Minh Nguyen prefers Python over Java and requests short code examples. Minh Nguyen is learning async/await a`

### G07 - episodic

`EPISODE: Minh con mot open-loop phai nop truoc deadline, dong thoi muon ghi chu retry payment dung so lan toi da theo policy. Nac lai ma task/deadline con dang do, va gioi han retry chinh t EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nha`

### G08 - episodic

`EPISODE: Minh con mot open-loop phai nop truoc deadline, dong thoi muon ghi chu retry payment dung so lan toi da theo policy. Nac lai ma task/deadline con dang do, va gioi han retry chinh t EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurr`

### G11 - mixed

`<LONG_TERM> <PRIORITY_EVIDENCE> }: Toi nay minh viet tool ca nhan de tai hien su co HTTP roi sua dung playbook. Can ba manh: ngon ngu minh thich khi lam mot minh, ma su co async lan truoc, va buoc playbook truoc khi tang timeout. Scope Minh, dung tron Lan. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos like ORCHID-27. The user's personal project is named ORCHID-27. - Minh Nguyen references the incident ASYNC-FIX-20. (2026-08-03 10:03:00) - Minh Nguyen is updating the company project BLUEBIRD-42 to require TypeScript for the backend. (2026-08-05 08:00:00) FACT: Minh Nguyen references the incident ASYNC-F`

### G13 - mixed

`<EPISODIC> EPISODE: Minh con mot open-loop phai nop truoc deadline, dong thoi muon ghi chu retry payment dung so lan toi da theo policy. Nac lai ma task/deadline con dang do, va gioi han retry chinh t EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connect`

### G15 - mixed

`<LONG_TERM> <PRIORITY_EVIDENCE> For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos like ORCHID-27. The user's personal project is named ORCHID-27. }: Chuan bi demo ca nhan: ten/ma project rieng cua Minh la gi, va lan async HTTP truoc minh reuse client nhu the nao (kem ma su co)? Khong can policy domain chung, chi memory cua Minh. - Minh Nguyen references the incident ASYNC-FIX-20. (2026-08-03 10:03:00) FACT: Minh Nguyen references the incident ASYNC-FIX-20. [valid_at=2026-08-03T10:03:00Z, invalid_at=None] - Minh Nguyen failed to debug async HTTP even after increasing the timeout to 60s. (2026-08-03 10:00:00`

### G16 - mixed

`<LONG_TERM> <PRIORITY_EVIDENCE> }: Minh sap giai thich coroutine cho ban, dong thoi can nhac policy retry payment vao vi du. Minh hoc kieu nao thi de nho? Va request retry payment phai mang header nao? Dung lay style hay stack cua nguoi khac. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos like ORCHID-27. The user's personal project is named ORCHID-27. Summary: Minh Nguyen needs to complete the benchmark report before Friday at 16:00. This is open loop LAB-REPORT-1600. Summary: Minh Nguyen's personal project is ORCHID-27. Minh Nguyen prefers Python over Java and requests short code examples. Minh Nguyen `

### G17 - mixed

`<LONG_TERM> <PRIORITY_EVIDENCE> For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos like ORCHID-27. The user's personal project is named ORCHID-27. }: Trong thread nay minh vua nhac constraint gio standup. Lat nua minh se them retry payment vao dung backend du an cong ty. Ghep ba manh: constraint standup con hieu luc trong thread, stack bat buoc cua backend cong ty, va cach danh dau request payment de khong trung don. Summary: Minh Nguyen's personal project is ORCHID-27. Minh Nguyen prefers Python over Java and requests short code examples. Minh Nguyen is learning async/await and confuses coroutine with Task`

### G18 - mixed

`<EPISODIC> EPISODE: Minh sap viet script ca nhan de tai hien su co latency, muon code dung ngon ngu minh thich khi lam mot minh, dong thoi bam sat playbook incident cua lab chu dung vo tang timeout. G EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. EPISODE: Toi se uu tien timeline khi giai thich coroutine va Task. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout thresh`

### G19 - mixed

`<LONG_TERM> <PRIORITY_EVIDENCE> For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos like ORCHID-27. The user's personal project is named ORCHID-27. }: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. - Minh Nguyen is working on personal demos for project ORCHID-27. (2026-08-05 08:00:00) FACT: Minh Nguyen is working on personal demos for project ORCHID-27. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] - Minh Nguyen's personal project is ORCHID-27. (2026-08-01 09:00:00) - Minh Nguyen is updatin`

### G05 - long_term

`<PRIORITY_EVIDENCE> Summary: For project BLUEBIRD-42, backend development must use TypeScript with NestJS; Python is not permitted. Minh Nguyen prefers Python for personal demos, specifically for project ORCHID-27. The scope has been clarified: BLUEBIRD-42 will use TypeScript/NestJS, and ORCHID-27 will... }: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user prefers Python for personal demos like ORCHID-27. The user's personal project is named ORCHID-27. Sum`

### G12 - mixed

`<LONG_TERM> <PRIORITY_EVIDENCE> Summary: For project BLUEBIRD-42, backend development must use TypeScript with NestJS; Python is not permitted. Minh Nguyen prefers Python for personal demos, specifically for project ORCHID-27. The scope has been clarified: BLUEBIRD-42 will use TypeScript/NestJS, and ORCHID-27 will... Summary: ORCHID-27 is the name of Minh Nguyen's personal project. While the company project BLUEBIRD-42 requires a backend using TypeScript with NestJS, Minh Nguyen's personal project ORCHID-27 continues to prefer Python. }: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dun`

### G20 - mixed

`<SHORT_TERM> <SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Filler about dashboard widgets. | assistant: Filler. | user: Filler about CSS variables. | assistant: Filler. | user: Filler about copy review. | assistant: Filler. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler about empty charts. assistant: Filler. user: Filler about telemetry. assistant: Filler. user: Filler about a11y labels. assistant: Filler. </RECENT_TURNS> </SHORT_TERM>`
