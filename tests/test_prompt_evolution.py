from pathlib import Path
from scripts.prompt_evolution import PromptEvolution


def test_evolution_simulation(tmp_path: Path) -> None:
    evo = PromptEvolution(
        task_description="say hello",
        output_dir=str(tmp_path),
        population_size=2,
        max_iterations=1,
        verbose=False,
        model="simulate",
    )
    results = evo.evolve()
    assert results["best_prompt"]
    # ensure output files were created
    assert any(p.suffix == ".md" for p in tmp_path.iterdir())
