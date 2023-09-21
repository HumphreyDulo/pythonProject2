# Project Title
Learning pycharm

## Project Description

This project aims to address a series of programming challenges and tasks related to data processing, file manipulation, and more. The project involves using various Python libraries and tools to achieve specific objectives.

## Data Source

The project uses the following data sources:

- Test Files (Stored as .xlsx files)

## Libraries

The following Python libraries are utilized in this project:

- Pandas
- Numpy
- LaBSE (for advanced text processing)
- Tensorflow (Note: Requires a Python downgrade)
- Google API (for cloud storage, used in the final step of the solution)

## Project Tasks

1. **Create a New Environment**: Set up a new Python environment for the project.

2. **Import Test Files**: Import the test files in .xlsx format into the project.

3. **Generate Email Addresses**: Generate email addresses for students based on their names in the format: `jdoe@gmail.com`. Ensure uniqueness and handle special characters.

4. **GitHub Collaboration**: Push the project to GitHub for collaboration.

5. **File Organization**: Organize project files as follows:
   - Functions: functions.py
   - Constraints: constraints.py
   - Main Program: main.py
   - Output Files: TSV and CSV
   - Log Files: To save computations

6. **Data Processing**: Perform data processing tasks such as generating separate lists of male and female students.

7. **Logging**: Create logs to track the number of male and female students.

8. **Special Characters**: Identify and list student names with special characters using regex.

9. **Similarity Analysis**: Use LaBSE to run a similarity matrix on male vs. female names. Save results in a JSON file with at least 50% similarity.

10. **File Merging**: Merge all project documents into one file. Shuffle names using Pandas and save as a JSON file. Save another copy as a JSONL file.

11. **Backup**: Generate a Google API key and save project files in Google Drive for backup.

## Usage

- Clone this repository to your local machine.
- Set up the required Python environment with the specified libraries.
- Execute the main program (`main.py`) to run the project tasks.

## Author

[Your Name]

## License

This project is licensed under the [License Name] License - see the [LICENSE.md](LICENSE.md) file for details.
