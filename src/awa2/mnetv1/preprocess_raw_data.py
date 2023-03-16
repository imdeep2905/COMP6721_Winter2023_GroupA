import splitfolders

from pathlib import Path

RAW_DATASET_PATH = Path(
    "../../../dataset/raw/awa2/AwA2-data/Animals_with_Attributes2/JPEGImages"
)
PROCESSED_DATASET_PATH_MNETV1 = Path("../../../dataset/processed/awa2/mnetv1")


def split_raw_data():
    # From raw folder create train, test and val folder
    splitfolders.ratio(
        RAW_DATASET_PATH,
        output=PROCESSED_DATASET_PATH_MNETV1,
        seed=42,
        ratio=(0.8, 0.1, 0.1),
    )


def main():
    split_raw_data()


if __name__ == "__main__":
    main()
