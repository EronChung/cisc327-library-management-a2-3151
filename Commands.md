python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

playwright install --with-deps
playwright codegen localhost:5000
pytest .\tests\test_e2e.py --headed --slowmo 100

docker build -t library-app .
docker container run -p 5000:5000 library-app

docker tag library-app eronchung/library-app:v1
docker push eronchung/library-app:v1
docker rmi eronchung/library-app:v1
docker pull eronchung/library-app:v1
docker run -p 5000:5000 eronchung/library-app:v1