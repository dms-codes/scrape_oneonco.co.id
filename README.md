# Web Scraper for Doctor Directory

This Python script is a web scraper that extracts and collects data about doctors from the OneOnCo website's doctor directory. It uses the requests library to fetch web pages, BeautifulSoup for parsing HTML, and writes the collected data to a CSV file.

## Prerequisites

Before running this script, make sure you have the following:

- Python installed on your system.
- The required Python libraries installed. You can install them using pip:
  ```bash
  pip install requests beautifulsoup4
  ```

## Usage

1. Clone this repository or download the script.

2. Open the script in a text editor or IDE.

3. Modify the script as needed to adjust the output filename, headers, or other settings.

4. Run the script using Python:
   ```bash
   python script_name.py
   ```

## Description

- The script starts by sending an HTTP GET request to the BASE_URL, which is the OneOnCo doctor directory.

- It uses a session for better performance when making multiple requests.

- The `fetch_doctor_details` function is used to extract data for a single doctor from their individual page. It fetches details such as name, specialization, sub-specialization, hospital, address, schedule, map, phone number, website, and additional details.

- The script then iterates through the pages of the doctor directory, fetching and parsing each doctor's details, and writing the data to a CSV file named 'data_dokter_oneonco.csv'.

## Customization

You can customize the script by adjusting the following variables in the code:

- `BASE_URL`: The URL of the OneOnCo doctor directory.
- `TIMEOUT`: The timeout value for HTTP requests.
- `HEADERS`: The user-agent header for HTTP requests.
- The structure of the CSV output, including the field names, can be adjusted in the `fieldnames` list.

## License

This code is provided under the MIT License. You can find the full license details in the `LICENSE` file.

## Disclaimer

This web scraping script is intended for educational and personal use only. Before using this script, please make sure to respect the website's terms of service and privacy policy. Unauthorized scraping may be against the website's terms of use.
