We can use JenkinsAPI with python to automate whole jenkins process .

Installation of Jenkins API :

pip3 install python-jenkins ( I am using python3 for my code)

After that just import the Jenkins api in file and make connection to jenkins server. 

<h5>
import jenkins </br>
#Make connection with jenkins</br>
server = jenkins.Jenkins('http://jenkins-url:8080/', username='username',
                         password='xxxxxxxxxxxxxxx')
<h5>

