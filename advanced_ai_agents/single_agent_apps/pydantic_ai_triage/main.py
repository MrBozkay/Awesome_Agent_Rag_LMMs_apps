from pydantic_ai_triage.agent import create_triage_agent
from pydantic_ai_triage.database import MockDatabase
from pydantic_ai_triage.models import TriageDependencies, TriageOutput


async def run_triage(patient_id: int, message: str) -> TriageOutput:
    """Run triage agent for a given patient."""
    db = MockDatabase()
    agent = create_triage_agent()
    deps = TriageDependencies(patient_id=patient_id, db=db)

    result = await agent.run(message, deps=deps)
    return result.data


if __name__ == "__main__":
    import asyncio
    asyncio.run(run_triage(42, "Kendimi hiç iyi hissetmiyorum."))
