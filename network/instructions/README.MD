### 🛠️ Install Prerequisites on EC2 ###
sudo yum update -y
sudo yum install -y git python3 nodejs
sudo yum install python3-pip -y
curl -sL https://rpm.nodesource.com/setup_18.x | sudo bash -
sudo yum install -y nodejs
sudo pip3 install virtualenv


### Frontend App ###
cd frontend
npm install axios