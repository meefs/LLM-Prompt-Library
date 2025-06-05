from scripts import prompt_analyzer


def test_evaluate_improves_score(monkeypatch) -> None:
    monkeypatch.setattr(prompt_analyzer, "NLTK_AVAILABLE", False)
    analyzer = prompt_analyzer.PromptAnalyzer()
    bad_prompt = "This is not clear."
    good_prompt = "# Title\n\n```markdown\nreset\n```\nYour task is to be clear."
    assert analyzer.evaluate(good_prompt) > analyzer.evaluate(bad_prompt)
