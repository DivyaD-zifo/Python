import os
import requests
from bs4 import BeautifulSoup
import pdfkit

# Function to scrape links from a page
def scrape_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

# Function to save a webpage as a PDF
def save_as_pdf(url, output_path):
    pdfkit.from_url(url, output_path)

# Main function
def main():
    # Replace this URL with the Wikipedia page you want to scrape
    index_url = 'https://en.wikipedia.org/wiki/Main_Page'
    links = scrape_links(index_url)
    output_directory = 'output_pdfs'  # Specify the output directory
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        
    for link in links:
        if link.startswith('/wiki/'):  # Check if it's a valid Wikipedia link
            try:
                # Construct absolute URL
                full_url = 'https://en.wikipedia.org' + link
                pdf_file_name = link.split('/')[-1] + '.pdf'  # Extract filename
                output_path = os.path.join(output_directory, pdf_file_name)
                save_as_pdf(full_url, output_path)
                print(f"PDF saved for {full_url}")
            except Exception as e:
                print(f"Error processing {full_url}: {e}")

if __name__ == "__main__":
    main()
