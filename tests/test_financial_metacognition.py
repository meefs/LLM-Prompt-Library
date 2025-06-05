import importlib
import spacy


def test_identify_financial_concepts(monkeypatch):
    monkeypatch.setattr(spacy, "load", lambda name: spacy.blank("en"))
    fm = importlib.import_module(
        "scripts.financial_metacognition.financial_metacognition"
    )
    result = fm.identify_financial_concepts(
        "Stocks rallied in the US market",
        "The US stocks show growth",
        region="US",
    )
    assert result["identified_concepts"]
    assert result["concept_coverage"]["coverage_percentage"] >= 0
