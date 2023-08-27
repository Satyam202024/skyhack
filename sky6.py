#used these to for finding  word is coming hight many times
file_path = 'comment.txt'
file_encoding = 'utf-8'
highlighted_words = {
    'not': 'red',
    'bad': 'blue',
    'hard': 'green',
    'Tasteless Food':'yellow',
    'Cold Meals':'orange',
    'Limited Options':'red',
    'Stale Snacks':'blue',
    'Unappetizing Presentation':'orange',
    'Slow Service':'green',
    'Inadequate Portions':'orange',
    'Allergic Reactions':'orange',
    'Wrong Orders':'orange',
    'Unsatisfactory Beverages':'orange',
    'Limited Drink Options':'pink',
    'Expired Items':'orange',
    'Unhealthy Options':'orange',
    'Meal Not Included':'orange',
    'Dirty Tableware':'orange',
    'Beverage Not Refreshing':'orange',
    'No Vegetarian/Vegan Options':'orange',
    'limited':'pink',
    'Fair at best' :'pink',
    'Lacking':'pink',
    'Not up to par':'pink',
    'couple sips':'pink',
    'Shortage':'print',
    'Cheap':'pink',
    'Spicy':'pink',
    'Too many grains':'pink',
    'Change up':'pink'

}

with open(file_path, 'r', encoding=file_encoding) as file:
    text = file.read()

for word, color in highlighted_words.items():
    text = text.replace(word, f'<span style="color: {color};">{word}</span>')


with open('formatted_text.html', 'w', encoding='utf-8') as output_file:
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Highlighted Text</title>
    </head>
    <body>
        <div>{text}</div>
    </body>
    </html>
    """
    output_file.write(html_template)

print("Formatted text with colors saved to 'formatted_text.html'.")