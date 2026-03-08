import fitz
import os


def extract_images_from_pdf(pdf_path: str, output_folder: str):

    os.makedirs(output_folder, exist_ok=True)

    doc = fitz.open(pdf_path)

    images = []

    for page_index in range(len(doc)):

        page = doc.load_page(page_index)

        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list):

            xref = img[0]

            base_image = doc.extract_image(xref)

            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            image_name = f"page_{page_index+1}_img_{img_index}.{image_ext}"

            image_path = os.path.join(output_folder, image_name)

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            images.append({
                "page": page_index + 1,
                "path": image_path
            })

    return images