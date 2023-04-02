FROM python:3.9-slim
WORKDIR /app
RUN pip install flask
COPY ScoreFile/MainScores.py .
COPY Utils.py .
EXPOSE 5000
COPY Scores.txt .
CMD ["python", "mainscore.py"]
