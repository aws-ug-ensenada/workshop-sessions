# Check the current logged-in user
whoami  

# Display the system's hostname
hostname  

# Show Linux distribution and version details
cat /etc/os-release  

# Print the current working directory
pwd  

# Create a directory named "my_folder"
mkdir my_folder  

# Remove "my_folder" and its contents (if not empty)
rm -rf my_folder  

# Create an empty file named "myfile.txt"
touch myfile.txt  

# Display the contents of "myfile.txt"
cat myfile.txt  

# Display real-time system processes and resource usage
top  

# Show disk space usage in a human-readable format
df -h  

# Display memory usage in megabytes
free -m  

# Test network connectivity to google.com
ping google.com  

# Update all installed packages (for Amazon Linux, CentOS, or RHEL)
sudo yum update -y  

# Install the Nginx web server
sudo yum install -y nginx  

# Start the Nginx service
sudo systemctl start nginx  

# Open the index.html file in the vi editor (to edit the Nginx homepage)
vi /usr/share/nginx/html/index.html  

# Installs Git on the system using the yum package manager. The -y flag automatically confirms the installation without user intervention.
sudo yum install -y git

# Displays the currently installed version of Git to verify it's installed and working properly.
git --version

# Installs Python 3 using the yum package manager, with the -y flag to confirm installation automatically.
yum install -y python3

# Displays the installed version of Python 3 to verify the correct version is installed.
python3 --version

# Clones the python-weather-app repository from GitHub to your local machine for further development or usage.
git clone https://github.com/lunabacilio/python-weather-app.git

# Installs pip, the package manager for Python 3, allowing you to install Python packages from the Python Package Index (PyPI).
sudo yum install python3-pip

# Installs all Python packages listed in the requirements.txt file, which typically includes all dependencies for the project.
pip3 install -r requirements.txt

# Searches for PostgreSQL packages in the DNF repository and filters the output to show server-related packages.
sudo dnf search postgresql | grep server

# Installs the PostgreSQL 15 server package using the DNF package manager, with the -y flag for automatic confirmation.
sudo dnf install -y postgresql15-server

# Creates the necessary data directory for PostgreSQL 15 to store its data files. The -p flag ensures the parent directories are created if they do not already exist.
# Changes the ownership of the PostgreSQL data directory to the postgres user and group, ensuring PostgreSQL has the correct permissions.
# Initializes the PostgreSQL database in the specified data directory (/var/lib/pgsql/15/data) under the postgres user, preparing it for use.
sudo mkdir -p /var/lib/pgsql/15/data
sudo chown -R postgres:postgres /var/lib/pgsql/15
sudo su - postgres -c "/usr/bin/initdb -D /var/lib/pgsql/15/data"

# Switches to the postgres user, the default PostgreSQL superuser, to perform database management tasks.
sudo su - postgres

# Opens the PostgreSQL command-line interface (psql) to interact with the database.
psql

# Create a Database
CREATE DATABASE awsugensenda;

CREATE USER alonso WITH PASSWORD 'mypassword';

# List All Databases
\l

# List All Users
\du

# Exit PostgreSQL CLI
\q
