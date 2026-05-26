import pytest
from unittest.mock import patch, AsyncMock
from pydantic_ai_triage.database import MockDatabase
from pydantic_ai_triage.models import TriageOutput, TriageDependencies
from pydantic_ai_triage.agent import create_triage_agent
from pydantic_ai_triage.main import run_triage

def test_mock_database_returns_patient_name():
    db = MockDatabase()
    assert db.get_patient_name(42) == "John"

def test_mock_database_returns_unknown_for_invalid_id():
    db = MockDatabase()
    assert db.get_patient_name(999) == "Bilinmeyen Hasta"

def test_triage_output_has_required_fields():
    output = TriageOutput(
        response_text="Dikkatli olun",
        escalate=True,
        urgency=8
    )
    assert output.escalate is True
    assert output.urgency == 8
    assert output.response_text == "Dikkatli olun"

def test_triage_output_validation_rejects_invalid_urgency():
    with pytest.raises(Exception):
        TriageOutput(response_text="test", escalate=False, urgency=15)

def test_triage_dependencies_stores_patient_id_and_db():
    db = MockDatabase()
    deps = TriageDependencies(patient_id=42, db=db)
    assert deps.patient_id == 42
    assert deps.db is db

@pytest.mark.asyncio
async def test_triage_agent_initialization():
    agent = create_triage_agent()
    assert agent.name == "triage_agent"
    assert agent.output_type == TriageOutput

@pytest.mark.asyncio
@patch('pydantic_ai_triage.main.create_triage_agent')
async def test_run_triage_returns_structured_output(mock_create_agent):
    # Setup mock
    mock_agent = AsyncMock()
    mock_result = AsyncMock()
    mock_result.data = TriageOutput(
        response_text="Test response",
        escalate=False,
        urgency=5
    )
    mock_agent.run.return_value = mock_result
    mock_create_agent.return_value = mock_agent

    result = await run_triage(42, "Test message")

    assert result.response_text == "Test response"
    assert result.escalate is False
    assert result.urgency == 5
