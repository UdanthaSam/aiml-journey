
"""
WEEK 3 - PANDAS PRACTICE
========================

LESSONS:
1. Creating, Reading and Writing
2. Indexing, Selecting and Assigning
3. Summary Functions and Maps
4. Grouping and Sorting
5. Data Types and Missing Values

Install pandas:
    pip install pandas

Keep sample_wine_reviews.csv in the same folder.
Run:
    python week3_pandas_practice.py
"""

from pathlib import Path
import pandas as pd

DATA_FILE = Path(__file__).resolve().parent / "sample_wine_reviews.csv"
OUTPUT_FILE = Path(__file__).resolve().parent / "week3_review_results.csv"


def section(name):
    print("\n" + "=" * 65)
    print(name)
    print("=" * 65)


def main():

    # =========================================================
    # LESSON 1: CREATING, READING AND WRITING
    # =========================================================

    section("1. CREATING, READING AND WRITING")

    # Create a DataFrame using a list
    fruits = pd.DataFrame(
        [[30, 21]],
        columns=["Apples", "Bananas"]
    )

    print("Fruits:")
    print(fruits)

    # Create a DataFrame with custom row labels
    fruit_sales = pd.DataFrame(
        [[35, 21], [41, 34]],
        index=["2017 Sales", "2018 Sales"],
        columns=["Apples", "Bananas"]
    )

    print("\nFruit Sales:")
    print(fruit_sales)

    # Create a Series
    ingredients = pd.Series(
        ["4 cups", "1 cup", "2 large", "1 can"],
        index=["Flour", "Milk", "Eggs", "Spam"],
        name="Dinner"
    )

    print("\nIngredients:")
    print(ingredients)

    # Create a DataFrame using a dictionary
    animals = pd.DataFrame(
        {
            "Cows": [12, 20],
            "Goats": [22, 19]
        },
        index=["Year 1", "Year 2"]
    )

    print("\nAnimals:")
    print(animals)

    # Read data from a CSV file
    # index_col=0 uses the first CSV column as row labels.
    reviews = pd.read_csv(DATA_FILE, index_col=0)

    # Display the first five rows
    print("\nFirst Five Reviews:")
    print(reviews.head())

    # Display the size of the dataset
    print("\nDataset Shape:")
    print(reviews.shape)

    # Display column names
    print("\nColumn Names:")
    print(reviews.columns.tolist())


    # =========================================================
    # LESSON 2: INDEXING, SELECTING AND ASSIGNING
    # =========================================================

    section("2. INDEXING, SELECTING AND ASSIGNING")

    # Select a single column
    desc = reviews["description"]

    print("\nDescription Column:")
    print(desc.head())

    # Select the first value using iloc
    first_description = reviews["description"].iloc[0]

    print("\nFirst Description:")
    print(first_description)

    # Select the first complete row
    first_row = reviews.iloc[0]

    print("\nFirst Row:")
    print(first_row)

    # Select the first 10 descriptions
    first_descriptions = reviews["description"].iloc[:10]

    print("\nFirst 10 Descriptions:")
    print(first_descriptions)

    # Select specific rows using index labels
    sample_reviews = reviews.loc[[1, 2, 3, 5, 8]]

    print("\nSelected Reviews:")
    print(sample_reviews)

    # Select specific rows and columns
    selected_locations = reviews.loc[
        [0, 1, 10],
        ["country", "province", "region_1", "region_2"]
    ]

    print("\nSelected Locations:")
    print(selected_locations)

    # Select the first 10 rows and two columns
    first_ten_country_variety = reviews.iloc[:10][
        ["country", "variety"]
    ]

    print("\nCountry and Variety:")
    print(first_ten_country_variety)

    # Conditional filtering
    # Select wines from Italy
    italian_wines = reviews.loc[
        reviews["country"] == "Italy"
    ]

    print("\nItalian Wines:")
    print(italian_wines[["title", "points"]])

    # Multiple conditions using & (AND) and isin()
    top_oceania_wines = reviews.loc[
        (reviews["points"] >= 95)
        &
        (reviews["country"].isin(["Australia", "New Zealand"]))
    ]

    print("\nTop Oceania Wines:")
    print(top_oceania_wines[["title", "points"]])

    # Assign a new column
    reviews["score_category"] = "Unclassified"

    # Update values based on a condition
    reviews.loc[
        reviews["points"] >= 95,
        "score_category"
    ] = "Excellent"

    print("\nScore Categories:")
    print(reviews[["title", "points", "score_category"]])


    # =========================================================
    # LESSON 3: SUMMARY FUNCTIONS AND MAPS
    # =========================================================

    section("3. SUMMARY FUNCTIONS AND MAPS")

    # Calculate the median
    median_points = reviews["points"].median()

    print("\nMedian Points:")
    print(median_points)

    # Calculate the mean
    # Missing values are ignored automatically.
    mean_price = reviews["price"].mean()

    print("\nMean Price:")
    print(round(mean_price, 2))

    # Find unique countries
    countries = reviews["country"].unique()

    print("\nUnique Countries:")
    print(countries)

    # Count how many reviews belong to each country
    reviews_per_country = reviews["country"].value_counts()

    print("\nReviews Per Country:")
    print(reviews_per_country)

    # Generate summary statistics
    print("\nPoints Summary:")
    print(reviews["points"].describe())

    # Subtract the average price from each wine price
    centered_price = reviews["price"] - mean_price

    print("\nCentered Prices:")
    print(centered_price.head())

    # Find the best value-for-money wine
    # Exclude missing and zero prices.
    valid_prices = (
        reviews["price"].notna()
        &
        (reviews["price"] > 0)
    )

    value_for_money = (
        reviews.loc[valid_prices, "points"]
        /
        reviews.loc[valid_prices, "price"]
    )

    bargain_idx = value_for_money.idxmax()

    bargain_wine = reviews.loc[bargain_idx, "title"]

    print("\nBest Bargain Wine:")
    print(bargain_wine)

    # Count descriptions containing particular words
    descriptor_counts = pd.Series({
        word: reviews["description"].fillna("").map(
            lambda description: word in description
        ).sum()
        for word in ["tropical", "fruity"]
    })

    print("\nDescriptor Counts:")
    print(descriptor_counts)

    # MAP FUNCTION
    # map() transforms each value in a Series.
    reviews["price_label"] = reviews["price"].map(
        lambda price:
            "Unknown" if pd.isna(price)
            else "Budget" if price < 30
            else "Premium"
    )

    print("\nPrice Labels:")
    print(reviews[["title", "price", "price_label"]])

    # APPLY FUNCTION
    # apply(axis=1) processes one complete row at a time.
    def stars(row):

        if row["country"] == "Canada" or row["points"] >= 95:
            return 3

        elif row["points"] >= 85:
            return 2

        return 1

    reviews["stars"] = reviews.apply(stars, axis=1)

    print("\nWine Star Ratings:")
    print(reviews[["title", "points", "stars"]])


    # =========================================================
    # LESSON 4: GROUPING AND SORTING
    # =========================================================

    section("4. GROUPING AND SORTING")

    # Group reviews by the reviewer's Twitter handle
    reviews_written = reviews.groupby(
        "taster_twitter_handle"
    )["taster_twitter_handle"].count()

    print("\nReviews Written Per Handle:")
    print(reviews_written)

    # Find the highest points for each price
    best_rating_per_price = (
        reviews.groupby("price")["points"]
        .max()
        .sort_index()
    )

    print("\nBest Rating Per Price:")
    print(best_rating_per_price)

    # AGGREGATION
    # Find minimum and maximum prices for each variety
    price_extremes = reviews.groupby(
        "variety"
    )["price"].agg(["min", "max"])

    print("\nMinimum and Maximum Prices:")
    print(price_extremes)

    # SORTING
    # Sort using multiple columns in descending order
    sorted_varieties = price_extremes.sort_values(
        by=["min", "max"],
        ascending=[False, False]
    )

    print("\nSorted Wine Varieties:")
    print(sorted_varieties)

    # Calculate each reviewer's average rating
    reviewer_mean_ratings = reviews.groupby(
        "taster_name"
    )["points"].mean()

    print("\nReviewer Mean Ratings:")
    print(reviewer_mean_ratings)

    # Display summary statistics of reviewer averages
    print("\nReviewer Rating Summary:")
    print(reviewer_mean_ratings.describe())

    # Group using multiple columns
    # size() counts all rows in each group.
    country_variety_counts = (
        reviews.groupby(["country", "variety"])
        .size()
        .sort_values(ascending=False)
    )

    print("\nCountry and Variety Counts:")
    print(country_variety_counts)


    # =========================================================
    # LESSON 5: DATA TYPES AND MISSING VALUES
    # =========================================================

    section("5. DATA TYPES AND MISSING VALUES")

    # Check data types of every column
    print("\nColumn Data Types:")
    print(reviews.dtypes)

    # Check the data type of one column
    points_dtype = reviews["points"].dtype

    print("\nPoints Data Type:")
    print(points_dtype)

    # Convert numerical values into strings
    point_strings = reviews["points"].astype(str)

    print("\nPoints Converted to Strings:")
    print(point_strings.head())

    # Find rows where price is missing
    missing_price_reviews = reviews[
        reviews["price"].isnull()
    ]

    print("\nReviews with Missing Prices:")
    print(missing_price_reviews[["title", "price"]])

    # Count missing prices
    n_missing_prices = len(missing_price_reviews)

    print("\nNumber of Missing Prices:")
    print(n_missing_prices)

    # Count missing values in every column
    missing_by_column = reviews.isna().sum()

    print("\nMissing Values Per Column:")
    print(missing_by_column)

    # FILLNA
    # Replace missing region names with 'Unknown'
    # without modifying the original region_1 column.
    reviews["region_1_clean"] = reviews["region_1"].fillna(
        "Unknown"
    )

    print("\nCleaned Region Names:")
    print(reviews[["region_1", "region_1_clean"]])

    # Count regions after replacing missing values
    reviews_per_region = (
        reviews["region_1"]
        .fillna("Unknown")
        .value_counts()
        .sort_values(ascending=False)
    )

    print("\nReviews Per Region:")
    print(reviews_per_region)


    # =========================================================
    # SAVE FINAL RESULTS
    # =========================================================

    section("SAVING RESULTS")

    # Save the updated DataFrame to a new CSV file
    # index_label specifies the name of the index column.
    reviews.to_csv(
        OUTPUT_FILE,
        index_label="review_id"
    )

    print("\nProcessed CSV saved to:")
    print(OUTPUT_FILE)

    print("\nWEEK 3 PRACTICE COMPLETED!")


# Run main() only when this file is executed directly.
if __name__ == "__main__":
    main()
