FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
# Run training once to generate MLflow logs
RUN python train.py
ENV PORT 8080
EXPOSE 8080
CMD streamlit run app.py --server.port 8080 --server.address 0.0.0.0