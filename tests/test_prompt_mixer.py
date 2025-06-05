from pathlib import Path
from scripts.prompt_mixer import PromptMixer


def create_prompt(path: Path, title: str, instruction: str) -> None:
    content = f"# {title}\n\n```markdown\n`reset`\n`no quotes`\n\n{instruction}\n```\n"
    path.write_text(content)


def test_mixer_combines_sections(tmp_path: Path) -> None:
    root = tmp_path / "prompts"
    root.mkdir()
    prompt_a = root / "a.md"
    prompt_b = root / "b.md"

    create_prompt(prompt_a, "Alpha", "You should respond briefly.")
    create_prompt(prompt_b, "Beta", "Your task is to compute numbers.")

    mixer = PromptMixer(root_dir=str(root), output_dir=str(tmp_path))
    mixer.scan_prompts()

    output = mixer.create_mixed_prompt(
        title="Mixed", use_instructions_from="a.md", use_output_from="b.md"
    )
    assert output is not None
    mixed_content = Path(output).read_text()
    assert "You should respond briefly." in mixed_content
    assert "b.md" in mixed_content
