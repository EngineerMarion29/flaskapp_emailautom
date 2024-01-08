**A. Email Sending Automation Web Application Using Python Flask**
![2](https://github.com/EngineerMarion29/flaskapp_emailautom/assets/126779390/e9871f3c-5d7f-46af-917e-055eecdd20df)
Web Application Purpose and Functions:

-This application release will enable users, primarily, email marketers, to (1) send multiple emails by composing their message to the web app as well as the multiple recipients and (2) send multiple templated messages by uploading a csv file containing hundreds of email recipients.

-The intended next release aims to integrate scheduling of sending functionality for time based automation.

-This is a proof of concept project aiming to utilize python flask for a web application build, together with email sending automation capability integration of python to SMTP service.


**B. Devops CI / CD Pipeline for Email Sending Web App**
![3](https://github.com/EngineerMarion29/flaskapp_emailautom/assets/126779390/c079e667-9a9d-460c-9c2a-2cdd82799e61)
Pipeline Used for CI / CD of this Email Sending Web App Project:

-Git is used to push code to GitHub

-GitHub is used as cloud codebase repository

-Jenkins is used to periodically check updates in the GitHub repo and pull codebase once changes were detected

-Jenkins use Pipeline Module to virtual env build and test the codebase using Python modules

-Once testing is successful, jenkins copies the codebase towards dockerhost 

--[[Tasks below are done via ansible playbook]]--

-Upon successful copying of artifacts towards target host, dockerization of the application is initiated by Ansible Server on the dockerhost env 

-Upon successful Dockerization build, docker image is pushed to docker hub

-Docker is pulled then, towards Dockerhost machine

-Docker is deployed to a container 
