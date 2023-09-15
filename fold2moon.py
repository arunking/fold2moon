class PaperFolding:
    # Default values for paper thickness and decimal rounding
    default_paper_thickness_cm = 0.1
    default_rounding_decimal = 2

    # Conversion constants for different units
    conversion_constant = {
        "cm": 1,
        "m": 100,
        "km": 100000,
        "in": 2.54,
        "ft": 30.48,
        "au": 14959787070000
    }

    def __init__(self, paper_thickness_cm: int | float = default_paper_thickness_cm,
                 rounding_decimal: int = default_rounding_decimal):
        # Initialize the class with default values for paper thickness and rounding decimal
        self.paper_thickness_cm = paper_thickness_cm
        self.rounding_decimal = rounding_decimal
        # Validate if the paper thickness is a positive integer or float
        if ((not isinstance(paper_thickness_cm, int) and not isinstance(paper_thickness_cm, float))
                or paper_thickness_cm < 0):
            raise TypeError(
                "Paper thickness should be represented in centimeters and can only be either positive integer or float")
        # Validate if the decimal points to round off is a positive integer
        if not isinstance(rounding_decimal, int) or rounding_decimal < 0:
            raise TypeError("Decimal points to round off the float response should only be a positive integer")

    def calculate_paper_height(self, fold_count: int, conversion_unit: str = "cm") -> dict:
        # Validate if the fold count is a positive integer
        if not isinstance(fold_count, int) or fold_count < 0:
            raise TypeError("Fold count should only be a positive integer")
        # Validate if the conversion unit is available in the conversion_constant dictionary
        if conversion_unit not in self.conversion_constant.keys():
            raise ValueError("Incorrect conversion unit. The support formats are {}"
                             .format(list(self.conversion_constant.keys())))
        try:
            # Calculate the height of the paper after a given number of folds
            return {
                "height": ((((2 ** fold_count) * self.paper_thickness_cm) / self.conversion_constant[conversion_unit])
                           .__round__(self.rounding_decimal)),
                "unit": conversion_unit
            }
        except Exception as errors:
            raise Exception(errors)

    def calculate_folds_required(self, desired_height: int | float, measurement_unit: str = "cm") -> dict:
        # Validate if the desired height is a positive integer or float
        if (not isinstance(desired_height, int) and not isinstance(desired_height, float)) or desired_height < 0:
            raise TypeError("Desired height can only be either positive integer or float")
        # Calculate the number of folds required to reach a given height
        folds = 0
        while self.calculate_paper_height(folds, measurement_unit)["height"] < desired_height:
            folds += 1
        return {
            "folds": folds,
            "result": self.calculate_paper_height(folds, measurement_unit)
        }


if __name__ == "__main__":
    print("\nThis program let you calculate the number of paper folders required to reach a certain height\n"
          "Here are the supported formats:", ("{}, " * 6).format(*list(PaperFolding.conversion_constant.keys())),
          "[Eg: 23m]")
    raw_input = input("\nEnter the height you would like to compare with paper folding in unit format: ")
    try:
        if raw_input[-2:] in PaperFolding.conversion_constant.keys():
            height = int(raw_input[:-2])
            unit = raw_input[-2:]
        elif raw_input[-1:] in PaperFolding.conversion_constant.keys():
            height = int(raw_input[:-1])
            unit = raw_input[-1]
        else:
            raise ValueError("Incorrect unit. The support formats are {}"
                             .format(list(PaperFolding.conversion_constant.keys())))
        if isinstance(height, int) and height > 0:
            # Create an instance of the PaperFolding class and call its methods to perform the desired calculations
            paper_folding = PaperFolding()
            response = paper_folding.calculate_folds_required(height, unit)
            print("With {} folds you can reach {}{}".format(response["folds"],
                                                            response["result"]["height"], response["result"]["unit"]))
        else:
            raise TypeError("Height should be a positive integer")
    except Exception as unexpected_error:
        raise Exception(unexpected_error)
