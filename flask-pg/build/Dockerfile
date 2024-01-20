FROM registry.apps.ocp403p.eagledc.siemens.com/openshift/python38-siemens-eagle:latest

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
