from pdf2image import convert_from_path
from pyzbar.pyzbar import decode

pdf_path = "test.pdf"

# Convert PDF pages to images
pages = convert_from_path(pdf_path)

all_links = []

for page_num, page_image in enumerate(pages, start=1):
    decoded_objects = decode(page_image)
    
    print(f"Page {page_num} QR codes:")
    for obj in decoded_objects:
        data = obj.data.decode('utf-8')
        print(f" - {data}")
        all_links.append(data)

print("\nAll extracted QR code links:")
for link in all_links:
    print(link)

