# Project: Airflow Twitter Data Extraction and CSV Storage

## Description:
The project involved installing Apache Airflow on an EC2 instance in AWS and developing a Python script to extract today's 10 tweets containing specific keywords from the Twitter API. The extracted tweets were then saved to a CSV file. Additionally, a DAG (Directed Acyclic Graph) file was created to automate the execution of the data extraction function on a daily basis and save the data to the EC2 instance.

## Project Steps:

### EC2 Instance Setup:
        Created an EC2 instance in AWS.
        Connected to the EC2 instance using SSH.

### Airflow Installation on EC2:
#### Updated the package lists and upgraded existing packages by running the following commands:
        sudo apt update
        sudo apt upgrade

### Installed the necessary dependencies for Airflow:
       sudo apt install -y python3 python3-pip
       sudo apt install -y libmysqlclient-dev

### Installed Airflow and its dependencies using pip:
       export AIRFLOW_HOME=~/airflow
       pip3 install apache-airflow

### Initialized the Airflow database:
       airflow db init
### Create an admin user:
In the terminal, navigate to the directory where you installed Airflow (AIRFLOW_HOME).
Run the following command to create an admin user:

        airflow users create \
              --username admin \
              --firstname <YourFirstName> \
              --lastname <YourLastName> \
              --role Admin \
              --email admin@example.com

Replace <YourFirstName> and <YourLastName> with your desired values for the admin user's first name and last name.
Enter a password for the admin user when prompted.

#### Start the Airflow webserver:

##### In the terminal, navigate to the directory where you installed Airflow (AIRFLOW_HOME).
Run the following command to start the webserver:
 

    airflow webserver --port 8080

##### The webserver will start running and will be accessible at http://<your_ec2_instance_public_ip>:8080.

#### Start the Airflow scheduler:

Open a new terminal session.
In the terminal, navigate to the directory where you installed Airflow (AIRFLOW_HOME).
Run the following command to start the scheduler:
      airflow scheduler

#### The scheduler will start running and will be responsible for executing the DAGs based on the defined schedule.
#### Access the Airflow UI:
Open a web browser and navigate to 
        http://<your_ec2_instance_public_ip>:8080.
You will see the Airflow UI, where you can monitor the status of your DAGs, trigger manual DAG runs, and view logs and task execution details.
Log in using the admin username and the password you set during the admin user creation step.

##### With the webserver and scheduler running, you can now manage and monitor your Airflow DAGs through the Airflow UI. You can trigger DAG runs manually or let the scheduler execute them based on the defined schedule.
#### Twitter API Integration:
        Obtained Twitter API credentials (consumer key, consumer secret, access token, access token secret).
        Created a Python script that utilized the Tweepy library to authenticate with the Twitter API using the obtained credentials.

#### Data Extraction and CSV Storage:
        Developed a Python function to extract today's 10 tweets containing the keywords 'margin' and 'borrowable' from the Twitter API.
        Utilized the Tweepy library to perform the API request and retrieve the desired tweets.
        Implemented logic to check for and exclude repetitive tweets from the extracted data.
        Saved the extracted tweets to a CSV file using the CSV module or a library like pandas.

#### Airflow DAG Creation:
        Created a new DAG file within the Airflow DAGs directory.
        Defined the DAG with a suitable dag_id and other necessary attributes.
        Configured the DAG to run on a daily schedule using the schedule_interval parameter.
        Defined a task within the DAG to execute the previously developed Python function for data extraction and CSV storage.
        Configured any required dependencies between tasks using the set_upstream or set_downstream methods.
        Saved the DAG file in the appropriate directory for Airflow to detect and execute it.

##### DAG Execution and Data Storage:
        Started the Airflow webserver and scheduler to begin DAG execution.
        Monitored the Airflow UI or used the Airflow CLI to verify that the DAG was running successfully.
        Checked the specified directory on the EC2 instance to ensure that the extracted data was being saved to the CSV file on a daily basis.

###### The completed project allows for the automatic extraction of tweets containing specific keywords from the Twitter API on a daily schedule, with the data being stored in a CSV file on the EC2 instance. This setup can be further customized and expanded to include additional functionality or data processing as per your requirements.
