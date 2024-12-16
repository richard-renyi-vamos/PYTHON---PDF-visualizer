import fitz  # PyMuPDF
from PIL import Image
import io

def visualize_pdf(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    num_pages = pdf_document.page_count

    print(f"PDF has {num_pages} pages.")

    for page_num in range(num_pages):
        # Select a page
        page = pdf_document.load_page(page_num)

        # Render the page to a pixel map
        pix = page.get_pixmap()

        # Convert to an image
        image = Image.open(io.BytesIO(pix.tobytes("png")))

        # Display the image
        image.show()

        # Wait for user input to proceed
        input(f"Displaying page {page_num + 1}/{num_pages}. Press Enter to continue...")

    # Close the PDF file
    pdf_document.close()

# Example usage
pdf_file_path = "example.pdf"  # Replace with your PDF file path
visualize_pdf(pdf_file_path)
