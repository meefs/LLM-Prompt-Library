import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from llm_prompt_library.validate_prompts import main

if __name__ == "__main__":
    main()
