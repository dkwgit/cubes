FROM 658387908230.dkr.ecr.us-east-1.amazonaws.com/dkw-dsml-image:latest

USER vscode
WORKDIR "/home/vscode"
COPY ./cubes.yml cubes.yml
RUN ["/bin/bash", "-ci", "conda env create -f cubes.yml; conda activate cubes"]
