import pandas as pd

# Load the Excel file
excel_file = 'products.xlsx'
df = pd.read_excel(excel_file)

# Template for the product detail page
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Details</title>
    <link rel="stylesheet" href="../styles.css">
</head>
<body>
    <div class="product-detail">
        <h1>{product_name}</h1>
        <p>Type: {product_type}</p>
        <p>Health: {product_health_label}</p>
        <a href="../index.html">Back to list</a>
    </div>
</body>
</html>
"""

# Generate individual product pages
for index, row in df.iterrows():
    product_code = row['product_code']
    html_content = template.format(
        product_name=row['product_name'],
        product_type=row['product_type'],
        product_health_label=row['product_health_label']
    )
    with open(f'products/{product_code}.html', 'w') as f:
        f.write(html_content)