import jenkins
#Make connection with jenkins
server = jenkins.Jenkins('http://jenkins-url:8080/', username='username',
                         password='xxxxxxxxxxxxxxx')
#Declare empty list
job_names = []

#Definition of method to get job names
def list_job_name():
    jobs = server.get_all_jobs(folder_depth=None)
    for job in jobs:
        job_names.append(job['fullname'])


#Calling of funcition
list_job_name()
#Loop through get list and print 
for i in range(len(job_names)):
    print(job_names[i])
