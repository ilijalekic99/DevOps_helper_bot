from datetime import datetime

def sample_responses(input_text):
  user_message = str(input_text).lower()

  if user_message in ("hello", "hi", "sup"):
    return "Hey! How's it going?"

  if user_message in ("who are you", "who are you?"):
    return "I am a DevOps helper bot!"

  if user_message in ("time", "time?"):
    now = datetime.now()
    date_time = now.strftime("%d/%m/%y, %H:%M:S")

    return str(date_time)


  if user_message in ("db", "mariadb?", "mariadb"):
    return "check this link: https://www.digitalocean.com/community/tutorials/how-to-install-mariadb-on-ubuntu-20-04"

  if user_message in ("db to ec2", "db aws", "mariadb to aws", "db_to_ec2"):
    return "check this link:  https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToMariaDBInstance.html and this one: https://docs.amazonaws.cn/en_us/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateWebServer.html"

  if user_message in ("apache", "apache2", "apache?", "apache2?"):
    return "This is how to set an apache webserver:  https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04"

  if user_message in ("php", "php-fpm", "phpfpm", "php prerequisites"):
    return "This are the php prerequisites: https://www.linode.com/docs/guides/how-to-install-and-configure-fastcgi-and-php-fpm-on-ubuntu-18-04/"

  if user_message in ("lamp", "lamp stack", "lamp-stack"):
    return "This might help: https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-22-04"

  if user_message in ("AWS_LB", "aws_load_balancer", "lb", "alb", "terraform", "terraform?", "tg", "target group"):
    return "This is how to set up Automatic load balancer on AWS: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lb and check this link also: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lb_target_group aaaaand this one: https://medium.com/@sampark02/application-load-balancer-and-target-group-attachment-using-terraform-d212ce8a38a0"

  if user_message in ("cool_devops_github"):
    return "This guys know their stuff: \n " \
           "https://github.com/MichaelCade/90DaysOfDevOps \n" \
           "https://github.com/ilekicgrid \n"

  if user_message in ("ssh", "ssh keygen", "keygen"):
    return "How to make ssg-keygen: 42 ssh-keygen -t rsa -f tutorial_kp_new"

  if user_message in ("jenkins", "jenkins on docker"):
    return "This is everything i know about Jenkins: https://linuxhint.com/install_jenkins_docker_ubuntu/  ,  https://www.cloudlaya.com/blog/push-docker-to-ecr-with-jenkins/  ,  https://octopus.com/blog/jenkins-docker-ecr "

  if user_message in ("docker", "docker commands"):
    return "1 : docker build -f Dockerfile -t xxx_repo . \n" \
           "2(Run docker where Jenkins is in privilaged mode):  docker run --privileged -v /var/run/docker.sock:/var/run/docker.sock -p 8080:8080 -p 50000:50000 --name=jenkins-master --mount=source=jenkins-log,target=/var/log/jenkins --mount=source=jenkins-data,target=/var/jenkins_home -d myjenkins \n" \
           "3(exec into docker as root): docker exec -u 0 -it mycontainer bash \n" \
           "4: docker logs \n" \
           "5: docker images \n" \
           "6: docker ps -a  (for all running containers) \n" \
           "7: docker ps \n"

  if user_message in ("aws", "aws credentials"):
    return "1: aws ecr get-login --region eu-central-1 --no-include-email"

  if user_message in ("processes", "ps"):
    return "ps -aux"

  if user_message in ("commands_list"):
    return "This is the list of all of my commands master: \n" \
           "ps \n" \
           "docker \n" \
           "jenkins \n" \
           "ssh \n" \
           "cool_devops_githubs \n" \
           "alb or aws_load_balancer \n" \
           "lamp \n" \
           "php \n" \
           "apache \n" \
           "db_to_ec2 \n" \
           "mariadb \n" \
           "db \n" \
           "time \n" \
           "tutorials\n"

  if user_message in ("tutorials"):
    return "This is pretty usefull:\n" \
           "https://www.interviewbit.com/courses/fast-track-python/functionals-regex/ \n" \
           "https://www.hackerrank.com/domains/shell?filters%5Bstatus%5D%5B%5D=unsolved \n" \
           "https://devhints.io/bash \n" \
           "https://www.markdownguide.org/basic-syntax/ \n"


  return "I dont understand you."

