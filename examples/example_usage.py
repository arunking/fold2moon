# example_usage.py

from paper_folding import PaperFolding

moon_distance_km = 384400

def main():
    # Create an instance of the PaperFolding class
    paper_folding = PaperFolding()

    # Example usage
    result = paper_folding.calculate_paper_height(moon_distance_km, "km")
    print(result)

if __name__ == "__main__":
    main()
