# DALLE3-fastapi
Create a FastAPI application that returns DALL-E 3 generated images in both URL and base64 formats.


The following are the commands I initially used when setting up my AWS Linux server.


    sudo yum install python3 python3-pip
    pip3 install fastapi
    pip3 install uvicorn
    pip3 install openai
    pip3 install python-dotenv # Used for utilizing environment variables in Python

Gunicorn is used for running in the background. 
    
    pip install gunicorn
    
After installation, a service file is created in the path etc/systemd/system/ named image.service, with configurations tailored to individual needs. 


    [Unit]
    Description=gunicorn daemon
    After=network.target

    [Service]
    User=ec2-user
    Group=ec2-user
    WorkingDirectory=/home/ec2-user
    ExecStart=/home/ec2-user/.local/bin/gunicorn \
              --workers 4 \
              --worker-class uvicorn.workers.UvicornWorker \
              --timeout 120 \
              --bind 0.0.0.0:8000 image_generator:app \
    [Install]
    WantedBy=multi-user.target

Then, executing sudo systemctl start image.service enables running in the background.
