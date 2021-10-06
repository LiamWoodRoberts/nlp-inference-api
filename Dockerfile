FROM amazon/aws-lambda-python:3.6

# Install System Dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Load NLP Models
COPY load_nlp.py
RUN python load_nlp.py
RUN python -m spacy download en_core_web_sm

# Copy Rest of Files
COPY . .

CMD ["app.handler"]