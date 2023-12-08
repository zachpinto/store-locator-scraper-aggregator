# Eyewear Retailers Store Locator Data Aggregation

## Project Overview
This project involves scraping eyewear retailers' store locator data, primarily using APIs, with occasional use of BeautifulSoup for web scraping. The primary goal is to extract `name` and `address` pairs from various eyewear retailers and merge them into a consolidated dataset, ensuring accuracy and consistency in address formatting.

## Directory Structure
    .
    ├── .idea                   # IDE-specific configurations
    ├── data                    # Raw data from scraping
    ├── final_data              # Processed data ready for merging
    ├── merged_data             # Final merged dataset
    ├── scrapers                # Scripts for scraping store locators
    ├── utils                   # Utility scripts for data processing
    ├── README.md               # Project documentation
    └── requirements.txt        # Python dependencies

## Key Features
- **Data Scraping**: Tailored scripts for scraping store locator data using API requests and HTML parsing.
- **Data Processing**: Standardization and preprocessing scripts to ensure data consistency.
- **Data Merging**: Fuzzy string matching (Levenshtein distance) to merge datasets with consistent address formats.

## Getting Started
To set up and run this project locally, follow these steps:
1. Clone the repository:
```
git clone https://github.com/yourusername/your-repository-name.git
```

2. Navigate to the project:
```
cd python_store_locator_web_scraper
```

3. Install requirements:
```
pip install -r requirements.txt
```

## Usage
1. Run the scrapers:
```
python scrapers/<script_name>.py
```

2. Data Processing:
```
python utils/<script_name>.py
```

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
