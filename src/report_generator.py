# src/report_generator.py
from fpdf import FPDF

def generate_report(table_summaries, visual_paths):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for table, summary in table_summaries.items():
        pdf.cell(200, 10, txt=f"Summary for {table}", ln=True)
        pdf.multi_cell(200, 10, txt=summary)
        
        for path in visual_paths.get(table, []):
            pdf.add_page()
            pdf.image(path, x=10, y=10, w=190)
    
    pdf.output("output/report.pdf")
