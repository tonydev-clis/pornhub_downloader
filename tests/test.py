from pathlib import Path
parent_path = Path(__file__).parents[1].resolve()
data_path = parent_path / 'data'
print(data_path.resolve())