import fitz  # PyMuPDF
from PIL import Image
import io

def compress_pdf(input_path, output_path, image_quality=40):
    original_pdf = fitz.open(input_path)
    new_pdf = fitz.open()  # create new PDF

    for page in original_pdf:
        # Convert page to image
        pix = page.get_pixmap(dpi=300)  # adjust DPI as needed
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Compress the image using Pillow
        img_buffer = io.BytesIO()
        img.save(img_buffer, format="JPEG", quality=image_quality)
        img_buffer.seek(0)

        # Create a new page the same size as the original
        rect = fitz.Rect(0, 0, pix.width, pix.height)
        new_page = new_pdf.new_page(width=rect.width, height=rect.height)
        new_page.insert_image(rect, stream=img_buffer.read())

    new_pdf.save(output_path)
    new_pdf.close()
    original_pdf.close()
    print(f"✅ Compressed PDF saved to: {output_path}")

# Example usage
compress_pdf("input.pdf", "input_compress.pdf", image_quality=50)
