Hello icentris

Please download the following project for the Star Wars starship task.

I've been able to run it using the following commands in the Docker Toolbox.

Copy project to a single folder on host. 

These commands should do the trick.

$ docker build -t icentrisapp .

$ docker run --name swapi icentrisapp
