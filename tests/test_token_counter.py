import os
from pytest import approx

from llm_prompt_library.token_counter import TokenCounter

def test_extract_content_strip_markdown():
    text = "# Title\nSome *bold* text\n- item"
    tc = TokenCounter(include_markdown=False)
    assert tc.extract_content(text) == "Some bold text"


def test_extract_content_keep_markdown():
    text = "# Title\nSome *bold* text\n- item"
    tc = TokenCounter(include_markdown=True)
    assert tc.extract_content(text) == text


def test_extract_content_remove_code_block():
    text = "# Title\n\n```python\nprint('hi')\n```\nAfter code"
    tc = TokenCounter(include_markdown=False, include_code_blocks=False)
    assert tc.extract_content(text) == "After code"


def test_count_tokens_fallback():
    tc = TokenCounter(tokenizer="other")
    assert tc.count_tokens("hello world") == 2


def test_analyze_all_aggregation(tmp_path):
    root = tmp_path / "prompts"
    cat1 = root / "cat1"
    cat1.mkdir(parents=True)
    cat2 = root / "cat2"
    cat2.mkdir(parents=True)

    (cat1 / "file1.md").write_text("hello world")
    (cat1 / "file2.md").write_text("more words here")
    (cat2 / "file3.md").write_text("another file example")

    tc = TokenCounter(root_dir=str(root), tokenizer="other", include_markdown=True)
    results = tc.analyze_all()

    assert results["total"]["files"] == 3
    assert results["total"]["tokens"] == 8
    assert results["total"]["avg_tokens_per_file"] == approx(8 / 3)

    assert results["by_category"]["cat1"]["files"] == 2
    assert results["by_category"]["cat1"]["tokens"] == 5
    assert results["by_category"]["cat1"]["avg_tokens_per_file"] == approx(2.5)
    assert results["by_category"]["cat2"]["files"] == 1
    assert results["by_category"]["cat2"]["tokens"] == 3
    assert results["by_category"]["cat2"]["avg_tokens_per_file"] == approx(3)

    file1_rel = os.path.relpath(cat1 / "file1.md", start=os.getcwd())
    file2_rel = os.path.relpath(cat1 / "file2.md", start=os.getcwd())
    file3_rel = os.path.relpath(cat2 / "file3.md", start=os.getcwd())

    assert results["by_file"][file1_rel] == 2
    assert results["by_file"][file2_rel] == 3
    assert results["by_file"][file3_rel] == 3
