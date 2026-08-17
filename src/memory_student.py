from __future__ import annotations

import re
from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty
from .zep_common import prime_eval_thread, render_graph_search


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    @staticmethod
    def _priority_evidence(text: str, query: str) -> str:
        """Put query-relevant facts/markers before budget trimming.

        Zep Context Blocks can place a useful open-loop or preference fact near
        the tail of a large block. The lab budget keeps the head, so expose a
        compact, evidence-only prefix while retaining the complete context for
        direct retrieval and provenance inspection.
        """
        query_terms = {
            token
            for token in re.findall(r"[a-z0-9][a-z0-9_-]{3,}", query.casefold())
        }
        marker_pattern = re.compile(
            r"\b(?=[A-Z0-9-]{5,}\b)(?=[A-Z0-9-]*[-0-9])[A-Z][A-Z0-9-]{4,}\b"
        )

        scored: list[tuple[int, int, str]] = []
        seen: set[str] = set()
        for index, raw_line in enumerate(text.splitlines()):
            line = raw_line.strip()
            if not line or line in seen:
                continue
            seen.add(line)
            lowered = line.casefold()
            normalized = re.sub(r"[-_]", " ", lowered)
            overlap = sum(
                1
                for term in query_terms
                if term in lowered or term.replace("-", " ") in normalized
            )
            markers = marker_pattern.findall(line)
            if overlap == 0 and not markers:
                continue
            score = overlap * 10 + len(markers) * 25
            if line.startswith("FACT:") or line.startswith("-"):
                score += 2
            scored.append((score, -index, line))

        if not scored:
            return ""
        selected = [line for _, _, line in sorted(scored, reverse=True)[:10]]
        return "<PRIORITY_EVIDENCE>\n" + "\n".join(selected) + "\n</PRIORITY_EVIDENCE>"

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        # LAB TODO 1/4
        # 1) prime_eval_thread(...) has already been provided as scaffolding.
        # 2) call thread.get_user_context(thread_id=...)
        # 3) return the .context string.
        # Bonus: append graph.search(scope="edges", limit>=20) facts with
        #        validity ranges (a low limit can miss deadline/open-loop facts).
        prime_eval_thread(self.client, user_id, thread_id, query)
        user_context = self.client.thread.get_user_context(thread_id=thread_id)
        context_block = getattr(user_context, "context", "") or ""

        try:
            facts = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="edges",
                limit=20,
            )
            fact_text = render_graph_search(facts)
        except Exception:
            # Keep Context Block retrieval usable if edge search is unavailable.
            fact_text = ""

        complete_context = join_nonempty([context_block, fact_text], sep="\n\n")
        priority = self._priority_evidence(complete_context, query)
        return join_nonempty([priority, complete_context], sep="\n\n")

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        # LAB TODO 2/4
        # Use client.graph.search(user_id=..., query=cap_query(query),
        #     scope="episodes", limit=...) then render_graph_search(...).
        # Tip: verbose session episodes can crowd out concise, marker-bearing
        # reflections under the tight episodic budget — render_graph_search
        # accepts an `episode_char_cap` to keep more distinct episodes.
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=15,
        )
        return render_graph_search(results, episode_char_cap=180)

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        # LAB TODO 3/4
        # Search the standalone graph (graph_id, NOT user_id).
        # Recommended: scope="episodes" — it returns raw document text that keeps
        # literal markers (e.g. PAYMENT-RULE-3). The "auto" scope returns
        # extracted facts that DROP those literal codes, so avoid it here.
        # Fallback: scope="nodes".
        capped_query = cap_query(query)
        try:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=capped_query,
                scope="episodes",
                limit=8,
            )
        except Exception:
            # Compatibility fallback for indexes exposing nodes only.
            results = self.client.graph.search(
                graph_id=graph_id,
                query=capped_query,
                scope="nodes",
                limit=8,
            )
        return render_graph_search(results)

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        # LAB TODO 4/4
        # Use ContextBudgetManager to enforce 10/4/3/3 budget and priority order.
        return self.budget.assemble(layers)
