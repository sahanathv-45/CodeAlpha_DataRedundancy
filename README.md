from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    cleaned_data = ""
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file and uploaded_file.filename.endswith(".txt"):
            lines = uploaded_file.read().decode('utf-8').splitlines()
            unique_lines = list(dict.fromkeys(lines))  # preserves order

            # Prepare cleaned data as text
            cleaned_data = "\n".join(unique_lines)

            # Save to file for download
            with open("cleaned_file.txt", "w") as f:
                f.write(cleaned_data)

            return render_template('index.html', message="✅ Data cleaned below 👇", data=cleaned_data)
        else:
            return render_template('index.html', message="⚠️ Please upload a valid .txt file!")
    return render_template('index.html')

@app.route('/download')
def download_file():
    return send_file("cleaned_file.txt", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
