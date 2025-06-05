import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from llm_prompt_library.financial_metacognition.financial_metacognition import main

if __name__ == "__main__":
    main()
