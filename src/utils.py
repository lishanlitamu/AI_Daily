from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

def extract_pdf_pages(input_path: str, output_path: str, start_page: int, end_page: int) -> None:
    """
    Extract specific pages from a PDF document and save them to a new PDF file.
    
    Args:
        input_path (str): Path to the input PDF file
        output_path (str): Path where the output PDF will be saved
        start_page (int): Starting page number (1-based index)
        end_page (int): Ending page number (1-based index)
        
    Raises:
        ValueError: If start_page is greater than end_page
        FileNotFoundError: If input file doesn't exist
    """
    # Convert to Path objects
    input_path = Path(input_path)
    output_path = Path(output_path)
    
    # Validate input file exists
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Validate page range
    if start_page > end_page:
        raise ValueError("start_page must be less than or equal to end_page")
    
    # Create PDF reader and writer objects
    reader = PdfReader(str(input_path))
    writer = PdfWriter()
    
    # Validate page numbers are within bounds
    if start_page < 1 or end_page > len(reader.pages):
        raise ValueError(f"Page range must be between 1 and {len(reader.pages)}")
    
    # Add selected pages to writer
    for page_num in range(start_page - 1, end_page):  # Convert to 0-based index
        writer.add_page(reader.pages[page_num])
    
    # Write the output file
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)
