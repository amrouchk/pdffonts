# pdffonts
Here’s a clean, well-formatted `README.md` file that documents your script:

---

````markdown
# PDF Font Size Analyzer

This Python script analyzes the **font sizes used in the first page** of all PDF files in the current directory. It identifies the most common font size (usually the body text) and the largest distinct font size (usually the title), then generates a summary report.

---

## 📄 What It Does

- Scans all `.pdf` files in the current folder
- Extracts text and font size information from the **first page** of each PDF
- Determines:
  - **Main text font size** (most frequent size)
  - **Title font size** (largest font size different from main text)
- Maps font sizes to **Word-style labels** like “Title”, “Heading 1”, “Body Text”, etc.
- Saves a report: `all_fonts_comparison.txt`

---

## 📦 Requirements

- Python 3.6+
- [`pdfplumber`](https://pypi.org/project/pdfplumber/)

Install with:

```bash
pip install pdfplumber
````

---

## 🚀 How to Use

1. Place the script in a folder containing your `.pdf` files.
2. Run the script:

```bash
python font_size_analyzer.py
```

3. After execution, it will generate:

```
all_fonts_comparison.txt
```

with output like:

```
File: example.pdf
  - Main text font size: 9.96 pt (Small Text (9–10 pt))
  - Title font size:     28.5 pt (Title (≈ 28–36 pt))
```

---

## 🧠 Font Size Labeling

Font sizes are mapped to Word-style categories:

| Font Size Range | Label               |
| --------------- | ------------------- |
| ≥ 28 pt         | Title               |
| 22–27.99 pt     | Heading 1           |
| 16–21.99 pt     | Heading 2           |
| 13–15.99 pt     | Heading 3           |
| 11–12.99 pt     | Body Text           |
| 9–10.99 pt      | Small Text          |
| ≤ 9 pt          | Footnote or Caption |

---

## ⚠️ Notes

* Only the **first page** is analyzed.
* Some PDFs may produce errors if they are encrypted, corrupted, or contain no extractable font data.
* Output includes `"Error"` if a file fails to process.

---

## 📁 Output Example

```
Font Size Report for All PDFs (First Page Only)
============================================================

File: paper1.pdf
  - Main text font size: 9.96 pt (Small Text (9–10 pt))
  - Title font size:     28.5 pt (Title (≈ 28–36 pt))

File: draft_submission.pdf
  - Main text font size: 8.97 pt (Footnote or Caption (≤ 9 pt))
  - Title font size:     25.19 pt (Heading 1 (≈ 22–28 pt))
```

---

## 👨‍💻 Author

Script created by \Amrouchk.

If you use or modify this script, feel free to credit or extend it.

---

```

---

```
