# 代码生成时间: 2025-10-20 00:36:48
import streamlit as st
import coverage
from coverage import Coverage
from coverage.data import CoverageData
from typing import List

"""
A Streamlit app to perform test coverage analysis.
"""

# Initialize the Coverage object
cov = Coverage()

# Define the path to the coverage data file
COVERAGE_DATA_FILE = 'coverage_data.xml'

# Define the path to the HTML report file
COVERAGE_HTML_REPORT = 'coverage_html_report.html'

"""
Function to load coverage data from file
:param file_path: Path to the coverage data file
:return: CoverageData object
"""
def load_coverage_data(file_path: str) -> CoverageData:
    try:
        # Load the coverage data from the XML file
        cov.load()
        cov.get_data()  # Ensure data is loaded
        return cov.get_data()
    except Exception as e:
        # Handle errors in loading coverage data
        st.error(f"Failed to load coverage data: {str(e)}")
        return None

"""
Function to generate HTML report from coverage data
:return: HTML report file path
"""
def generate_html_report(data: CoverageData) -> str:
    try:
        # Generate the HTML report
        cov.html_report(directory=COVERAGE_HTML_REPORT)
        return COVERAGE_HTML_REPORT
    except Exception as e:
        # Handle errors in generating HTML report
        st.error(f"Failed to generate HTML report: {str(e)}")
        return None

"""
Function to display coverage statistics
:param data: CoverageData object
"""
def display_coverage_statistics(data: CoverageData):
    try:
        # Display the total coverage percentage
        total_percentage = data.pc_covered()
        st.write(f"Total Coverage Percentage: {total_percentage}%")

        # Display the coverage percentage for each file
        for file, file_data in data.measured_files().items():
            percentage = file_data.pc_covered
            st.write(f"Coverage for {file}: {percentage}%")
    except Exception as e:
        # Handle errors in displaying coverage statistics
        st.error(f"Failed to display coverage statistics: {str(e)}")

"""
Main function to run the Streamlit app
"""
def main():
    st.title('Test Coverage Analysis')

    # Load the coverage data from file
    data = load_coverage_data(COVERAGE_DATA_FILE)
    if data is None:
        return

    # Generate the HTML report
    html_report_path = generate_html_report(data)
    if html_report_path is None:
        return

    # Display the coverage statistics
    display_coverage_statistics(data)

    # Provide a link to download the HTML report
    st.download_button(
        label='Download Coverage Report',
        data=open(html_report_path, 'rb').read(),
        file_name='coverage_report.html',
        mime='text/html'
    )

if __name__ == '__main__':
    main()