FROM python:3.9-slim
WORKDIR /app
RUN pip install selenium flask
COPY ScoreFile/MainScores.py .
COPY ScoreFile/Utils.py .
COPY ScoreFile/Scores.txt .
EXPOSE 5000
CMD ["python", "MainScores.py"]

