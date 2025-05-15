### 🛠️ Install Prerequisites on EC2 ###
sudo yum update -y
sudo yum install -y git python3
sudo yum install python3-pip -y
sudo pip3 install virtualenv

git clone https://github.com/aws-ug-ensenada/workshop-sessions.git
cd workshop-sessions/

### Backend App ###
cd network/app/backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 init_db.py  # ⬅️ This creates your schema
python3 app.py      # or run with gunicorn

### Optional to run in background ###
nohup python3 app.py > backend.log 2>&1 &
