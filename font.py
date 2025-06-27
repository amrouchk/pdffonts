import os
import pdfplumber
from collections import Counter

def extract_font_sizes(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        chars = first_page.chars
        font_sizes = [round(char["size"], 2) for char in chars]
        text_by_size = {}
        for char in chars:
            size = round(char["size"], 2)
            text_by_size.setdefault(size, []).append(char["text"])
        return font_sizes, text_by_size

def analyze_fonts(font_sizes, text_by_size):
    counter = Counter(font_sizes)
    most_common = counter.most_common()
    if not most_common:
        return None, None
    main_text_size = most_common[0][0]
    title_candidates = [size for size in sorted(counter.keys(), reverse=True) if size != main_text_size]
    title_size = title_candidates[0] if title_candidates else None
    return main_text_size, title_size

def word_label(size):
    if size is None:
        return "N/A"
    if size >= 28:
        return "Title (≈ 28–36 pt)"
    elif size >= 22:
        return "Heading 1 (≈ 22–28 pt)"
    elif size >= 16:
        return "Heading 2 (≈ 16–22 pt)"
    elif size >= 13:
        return "Heading 3 (≈ 13–16 pt)"
    elif size >= 11:
        return "Body Text (11–12 pt)"
    elif size >= 9:
        return "Small Text (9–10 pt)"
    else:
        return "Footnote or Caption (≤ 9 pt)"

# Get all PDF files in the current folder
pdf_files = [f for f in os.listdir() if f.lower().endswith(".pdf")]

# Process all PDFs
font_data = []
for pdf in pdf_files:
    try:
        sizes, texts = extract_font_sizes(pdf)
        main, title = analyze_fonts(sizes, texts)
        font_data.append((pdf, main, word_label(main), title, word_label(title)))
    except Exception as e:
        font_data.append((pdf, None, "Error", None, "Error"))

# Write report
with open("all_fonts_comparison.txt", "w", encoding="utf-8") as f:
    f.write("Font Size Report for All PDFs (First Page Only)\n")
    f.write("=" * 60 + "\n\n")
    for pdf, main, main_label, title, title_label in font_data:
        f.write(f"File: {pdf}\n")
        f.write(f"  - Main text font size: {main} pt ({main_label})\n")
        f.write(f"  - Title font size:     {title} pt ({title_label})\n\n")

print("✅ Font comparison report saved as 'all_fonts_comparison.txt'")
