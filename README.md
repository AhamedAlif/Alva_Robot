# Robots.txt Analyzer

A Python script to analyze URLs disallowed by the robots.txt file and check their response status.

## Description

This script fetches the "robots.txt" file from a given URL, extracts the disallowed paths, and then checks the status of those paths by sending HTTP requests. It provides color-coded output to indicate the status of each path.

## Usage

1. Make sure you have Python installed on your system.
2. Install the required dependency using the following command:

    ```
    pip install requests
    ```
   
3. Run the script by executing the following command:

    ```
    python AlvaRobot.py
    ```

4. The script will prompt you to enter the URL for analysis.

## Output Legend

- Green: Successful response (HTTP status code 200)
- Red: Not Found (HTTP status code 404) or Forbidden (HTTP status code 403)
- Yellow: Server Error (HTTP status code 500) or Redirect (HTTP status code 302)

## Disclaimer

This script is designed for educational and analysis purposes. Use it responsibly and only on websites where you have proper authorization.

## Author

Your Name

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
