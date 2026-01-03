"""LangGraph checkpointer using PostgreSQL.

Provides conversation memory across requests using database persistence.

NOTE: Checkpointing is currently disabled due to connection management complexity.
This will be properly implemented in a future update.
"""

from typing import Optional

from langgraph.checkpoint.base import BaseCheckpointSaver


async def get_checkpointer() -> Optional[BaseCheckpointSaver]:
    """
    Get PostgreSQL checkpointer for LangGraph.
    
    Currently returns None (checkpointing disabled).
    
    Returns:
        None (checkpointing disabled for now)
    """
    # TODO: Implement proper async checkpointer with connection pooling
    # For now, return None to disable checkpointing
    return None
