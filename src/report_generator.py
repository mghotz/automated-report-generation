# src/report_generator.py
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Automated Data Report', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_image(self, image_path):
        self.image(image_path, x=10, w=190)
        self.ln(10)

def generate_report(table_summaries, visual_paths):
    pdf = PDF()
    pdf.add_page()

    for table, summary in table_summaries.items():
        pdf.chapter_title(f'Summary for {table}')
        pdf.chapter_body(summary)
        for image_path in visual_paths.get(table, []):
            pdf.add_page()
            pdf.add_image(image_path)

    pdf.output('output/report.pdf')
