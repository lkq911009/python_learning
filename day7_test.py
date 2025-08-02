from pathlib import Path

base = Path.home()
current_dir = Path(__file__).parent

europe_dir = Path(current_dir, "Europe")

for txt in Path(europe_dir).glob("*.txt"):
    with open(txt, "r") as file:
        content = file.read()
        print(f"Content of {txt.name}:\n{content}\n")