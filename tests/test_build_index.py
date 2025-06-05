from pathlib import Path
import scripts.build_index as build_index
from scripts.build_index import extract_title


def test_extract_title_heading(tmp_path: Path):
    file = tmp_path / "example.md"
    file.write_text("# Heading\nContent")
    assert extract_title(file) == "Heading"


def test_extract_title_fallback(tmp_path: Path):
    file = tmp_path / "Example_File.md"
    file.write_text("No heading here")
    assert extract_title(file) == "Example File"


def test_build_site_sections(tmp_path: Path, monkeypatch):
    category = tmp_path / "cats"
    category.mkdir()
    prompt = category / "foo.md"
    prompt.write_text("# Meow")

    monkeypatch.setattr(build_index, "PROMPTS_DIR", tmp_path)
    html = build_index.build_site_sections()
    assert "<!-- CATS (1) -->" in html
    assert "prompts/cats/foo.md" in html
