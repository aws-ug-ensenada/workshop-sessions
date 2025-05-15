### 🛠️ Install Prerequisites on EC2 ###
sudo yum update -y
sudo yum install -y git python3 nodejs
sudo yum install python3-pip -y
curl -sL https://rpm.nodesource.com/setup_18.x | sudo bash -
sudo yum install -y nodejs
sudo pip3 install virtualenv

git clone https://github.com/aws-ug-ensenada/workshop-sessions.git

### Backend App ###
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python init_db.py  # ⬅️ This creates your schema
python app.py      # or run with gunicorn

### Optional to run in background ###
nohup python3 app.py > backend.log 2>&1 &
