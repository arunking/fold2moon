# example_usage.py

from fold2moon import PaperFolding

moon_distance = 384400
unit = "km"


def main():
    # Create an instance of the PaperFolding class
    paper_folding = PaperFolding()

    # Example usage
    response = paper_folding.calculate_folds_required(moon_distance, unit)
    print("To reach a height of {}{}, you'll need to fold the paper {} times and will reach a height of {}{}"
          .format(moon_distance, unit, response["folds"], response["result"]["height"], response["result"]["unit"]))


if __name__ == "__main__":
    main()
