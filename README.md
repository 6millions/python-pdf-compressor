# 🐍 Python PDF Compressor

A simple and lightweight tool to compress PDF files by converting each page into high-quality, compressed JPEG images. Useful for scanned documents like bank slips, medical reports, or official papers when you need to reduce file size (e.g. under 3MB) for uploading or sharing.

---

## ✨ Features

- Compresses scanned/image-based PDFs by converting pages to JPEG  
- Adjustable image quality (`1-100`) and DPI for fine control  
- Outputs a clean, compressed PDF file  
- Built with Python using [PyMuPDF](https://github.com/pymupdf/PyMuPDF) and [Pillow](https://python-pillow.org/)

---

## 🧰 Requirements

- Python 3.6+
- pip

### 📦 Install Dependencies

```bash
pip install pymupdf pillow
```

Alternatively, use:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Use

### 1. Place your input PDF in the project folder  
(e.g. `input.pdf`)

### 2. Run the script

```bash
python resize.py
```

### 3. Output

- A compressed PDF will be saved as `compressed.pdf` in the same folder.
- You can modify file names and parameters as needed:

```python
compress_pdf("input.pdf", "output.pdf", image_quality=85)
```

---

## ⚙️ Parameters

| Parameter        | Type    | Description                                  |
|------------------|---------|----------------------------------------------|
| `image_quality`  | int     | JPEG quality (1–100). Default: `85`          |
| `dpi`            | int     | Dots-per-inch for page rendering. Default: `300` (set inside the script) |

💡 **Tip**: Use `image_quality=85` and `dpi=200–300` for balance between size and clarity.

---

## 📁 Example Usage

```python
compress_pdf("input.pdf", "input_compressed.pdf", image_quality=85)
```

---

## 🧪 Example Results

| Setting               | File Size    | Note                       |
|------------------------|--------------|-----------------------------|
| 150 DPI, quality 40    | ~1.5 MB      | Smaller but blurrier text  |
| 200 DPI, quality 85    | ~2.5 MB      | Good balance               |
| 300 DPI, quality 100   | ~5+ MB       | Max clarity, less compression |

---

## 🔒 Limitations

- This method rasterizes each page — result is **not text-searchable**
- Best suited for scanned or image-based PDFs

---

## 📌 Project Structure

```
python-pdf-compressor/
├── resize.py              # Main script
├── requirements.txt       # Dependency list
├── README.md              # You are here
```

---

## 🧑‍💻 Author

Made with ❤️ by [6millions](https://github.com/6millions)

---

## 📄 License

MIT License — free to use, modify, and share.

---

## 🌐 GitHub

Feel free to star ⭐ or fork 🍴 this repo if you find it useful!

👉 https://github.com/6millions/python-pdf-compressor
