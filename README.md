# Paper Folding Module

This Python module provides functionality to calculate the height of paper after a certain number of folds and determine the number of folds required to reach a desired height.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone or download the repository to your local machine.

2. Ensure you have Python 3.x installed.

3. To use the `PaperFolding` module in your Python scripts, import the `PaperFolding` class from the `paper_folding` module.

   ```python
   from paper_folding import PaperFolding
   ```

## Usage

You can use the `PaperFolding` class to calculate the height of paper after a certain number of folds or determine the number of folds required to reach a desired height.

```python
from paper_folding import PaperFolding

# Create an instance of the PaperFolding class
paper_folding = PaperFolding()

# Calculate the height of the paper after 5 folds in meters
result = paper_folding.calculate_paper_height(5, "m")
print(result)
```

## Examples

Check the [examples](examples/) directory for sample Python scripts demonstrating how to use the `PaperFolding` module.

## API Reference

### PaperFolding Class

#### `__init__(self, paper_thickness_cm: float = default_paper_thickness_cm, rounding_decimal: int = default_rounding_decimal)`

Initialize the PaperFolding class.

- `paper_thickness_cm` (float): Thickness of the paper in centimeters.
- `rounding_decimal` (int): Decimal places to round off the height.

#### `calculate_paper_height(self, fold_count: int, conversion_unit: str = "cm") -> dict`

Calculate the height of the paper after a given number of folds.

- `fold_count` (int): Number of folds.
- `conversion_unit` (str): Unit for height conversion (e.g., "cm", "m", "in", "ft", "km", "au").

Returns a dictionary with "height" (rounded height after folding) and "unit" (conversion unit).

#### `calculate_folds_required(self, desired_height: float, measurement_unit: str = "cm") -> dict`

Calculate the number of folds required to reach a desired height.

- `desired_height` (float): Desired height.
- `measurement_unit` (str): Unit for height measurement (e.g., "cm", "m", "in", "ft", "km", "au").

Returns a dictionary with "folds" (number of folds required) and "result" (height and unit after folding).

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow the [Contributing Guidelines](CONTRIBUTING.md).
#### Created and maintained by Arunraj P.



## License

This project is licensed under the [MIT License](LICENSE).
