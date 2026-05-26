from typing import Dict, Any
from pydantic_ai import Agent, RunContext
from pydantic_ai_triage.models import TriageDependencies, TriageOutput


def create_triage_agent() -> Agent[TriageDependencies, TriageOutput]:
    """Creates and configures the Triage Agent."""

    # Initialize the agent
    agent = Agent(
        'openai:gpt-4o',
        deps_type=TriageDependencies,
        output_type=TriageOutput,
        system_prompt=(
            "Sen hastalara yardımcı olan bir triyaj asistanısın. "
            "Net tavsiyeler ver ve aciliyeti değerlendir. "
            "Mümkün olduğunda hastanın adını kullan."
        ),
        name="triage_agent"
    )

    # Dynamic System Prompt
    @agent.system_prompt
    def add_patient_name(ctx: RunContext[TriageDependencies]) -> str:
        patient_name = ctx.deps.db.get_patient_name(ctx.deps.patient_id)
        return f"Şu anki hastanın adı: {patient_name}"

    # Tool for getting vitals
    @agent.tool
    def get_latest_vitals(ctx: RunContext[TriageDependencies]) -> Dict[str, Any]:
        """Mevcut hastanın en son alınan yaşamsal bulgularını (nabız, tansiyon vb.) getirir."""
        return ctx.deps.db.get_latest_vitals(ctx.deps.patient_id)

    return agent
