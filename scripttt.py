import pandas as pd
from fpdf import FPDF
from master import * 
import dataframe_image as dfi

# Calling functions to create plots

plot_hist() 
plot_ECDF()
plot_change()


### Creating PDF ###


# 1. Set up the PDF doc basics

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)

# 2. Layout the PDF doc contents

## Title
pdf.cell(200, 20, f'{stock} Covered Call Stats Report', align='C')

## Line breaks
pdf.ln(10)

## Images 
pdf.image(f'{stock}-hist.png', 5, 40, 100)
pdf.image(f'{stock}-ECDF.png', 100, 40, 100)
pdf.image(f'{stock}-change.png', 100, 130, 100)

## Line breaks
pdf.ln(20)

## ECDF table as image and adding to report

dfi.export(ecdf_data, f'{stock}-table.png')

pdf.image(f'{stock}-table.png', 30, 140, 40)

## 

# Save the PDF file
pdf.output(f'{stock}-CoveredCall-Report.pdf', 'F')



