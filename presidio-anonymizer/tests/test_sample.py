import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def test_sample_run_anonymizer():
    result = AnonymizerEngine().anonymize(
        text="My name is Bond.",
        analyzer_results=[RecognizerResult(entity_type="PERSON", start=11, end=15, score=0.8)],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})}
    )
    assert sample_run_anonymizer("My name is Bond.", 11, 15)==result