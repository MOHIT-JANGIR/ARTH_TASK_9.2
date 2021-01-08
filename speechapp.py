import os
import getpass
import subprocess
import json
import random
import sys
from gtts import gTTS
import speech_recognition as sr
from playsound import playsound



  
vg="myvg"
keypairname="mykey"
lvname="mylv"
devname="xvdh"
itag="myos"
privatekey="slave1.pem"
ebsdb=[]
devdb=[]
def gtts(text):
    os.system("tput setaf 6")
    tts=gTTS(text)
    tts.save("speak.mp3")
    playsound("/root/arth/speak.mp3")
    print(text)
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("start say")
        audio=r.listen(source)
        print("speech done")
    data=r.recognize_google(audio)
    os.system(" tput setaf 7")
    return data

loc=gtts("where you want to run this menu ?local or remote : ")

os.system(" tput setaf 4")  
passwd=getpass.getpass("enter file execution password for authentication(only once) : ")
os.system(" tput setaf 7")

if passwd!="12":
          print("incorrect password")
          exit()

def stdout(file):
    original_stdout=sys.stdout
    with open('{}'.format(file),'w') as f:
        sys.stdout=f
        print(keypair)
        sys.stdout=original_stdout

def volume(itag):

          ebs_size=input("give your ebs size(in GB) to create ebs volume : ")
          random1=random.randint(1,1000)
          ebsname="lvm_ebs_{}".format(random1)

          if len(ebsdb)==0:
              ebsdb.append(ebsname)
              os.system("tput setaf 6")
              os.system("aws ec2 create-volume --availability-zone ap-south-1a --volume-type gp2 --size {} --tag-specifications ResourceType=volume,Tags=['{{Key=Name,Value={}}}']".format(ebs_size,ebsname))
              os.system("tput setaf 2")
              print("\n\n\t\t your ebs volume has been created successfully")
              os.system("tput setaf 7")



          else:
              for i in ebsdb:
                  if i!=ebsname:
                      ebsdb.append(ebsname)
                      os.system("tput setaf 6")
                      os.system("aws ec2 create-volume --availability-zone ap-south-1a --volume-type gp2 --size {} --tag-specifications ResourceType=volume,Tags=['{{Key=Name,Value={}}}']".format(ebs_size,ebsname))
                      os.system("tput setaf 2")
                      print("\n\n\t\t your ebs volume has been created successfully")
                      os.system("tput setaf 7")
                      break
          os.system("tput setaf 5")
          input("\n\n press enter to attach your newly created ebs volume : ")
          os.system("tput setaf 6")
          vol=subprocess.getoutput("aws ec2 describe-volumes --filters Name=tag-key,Values=Name Name=tag-value,Values={}".format(ebsname))
          vol=json.loads(vol)
          vol=vol["Volumes"][0]["VolumeId"]
          dev=["xvdf","xvdg","xvdh","xvdi","xvdj","xvdk","xvdl","xvdm","xvdo","xvdp","xvdn","xvdq","xvdr","xvds","xvdt","xvdu","xvdw","xvdx","xvdy","xvdz"]
          devname=random.choice(dev)
                  

          if len(devdb)==0:
              devdb.append(devname)
              os.system("tput setaf 3")
              x=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-key,Values=Name Name=tag-value,Values={}".format(itag))
              x=json.loads(x)
              osid=x["Reservations"][0]["Instances"][0]["InstanceId"]
              os.system("tput setaf 6")
              os.system("aws ec2 attach-volume --instance-id {} --volume-id {} --device /dev/{}".format(osid,vol,devname))
              os.system("tput setaf 2")
              print("\n\n\t\t your ebs created and attached  successfully" )
              os.system("tput setaf 7")




          else:
              for i in devdb:
                  if i!=devname:
                      devdb.append(devname)
                      os.system("tput setaf 3")
                      x=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-key,Values=Name Name=tag-value,Values={}".format(itag))
                      x=json.loads(x)
                      osid=x["Reservations"][0]["Instances"][0]["InstanceId"]
                      os.system("tput setaf 6")
                      os.system("aws ec2 attach-volume --instance-id {} --volume-id {} --device /dev/{}   ".format(osid,vol,devname))
                      os.system("tput setaf 2")
                      print("\n\n\t\t your ebs created and attached  successfully" )
                      os.system("tput setaf 7")
                      break


def function(req):
    if "launch docker" in data and (("OS" in data) or ("container" in data)):
        osname = input("Enter the container name :")
        oimage = input("Enter the container image :")
        os.system("tput setaf 2")
        print("\t\t----------------------")
        os.system("tput setaf 7")
        cmd= "sudo docker run -dit --name {} {}".format(osname,oimage)
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status==0:
            print("\n")
            print("Docker OS launched..!!")
            print("Container  Name : {}".format(osname))
            print("Container  Image : {}".format(oimage))
            os.system("tput setaf 2")
            print("\t\t------------------------")
            os.system("tput setaf 7")
            s = os.system("sudo docker ps -a")
            print(s)

        else:
            print("error : {}".format(out))

    elif "start container" in data :
        print("All Containers which are stopped and running currently : \n")
        os.system("sudo docker ps -a")
        os.system("tput setaf 3")
        print("\t\t\****************")
        os.system("tput setaf 7 ")
        print("\n")
        osname = input ("Enter the container name which you want to start : ")
        cmd="sudo docker start {}".format(osname)
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]
        if status==0:
            print ("Container {}  Started...!!".format(osname))
        else:
            print("error : {}".format(out))

    elif "stop running container" in data:
        print("Containers already running :\n")
        os.system("sudo docker ps")
        os.system("tput setaf 3")
        print("\t\t\t\t--------------------")
        os.system("tput setaf 7")
        print("\n")
        osname = input("Enter the container name which you want to stop :")
        cmd= "sudo docker stop {}".format(osname)
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status==0:
            print("Container {} Stopped..!!!".format(osname))
        else:
            print("error : {}".format(out))

    elif "delete container" in data:
        print("Container Available:  \n")
        os.system("sudo docker ps -a")
        os.system("tput setaf 3")
        print("\t\t\t******************")
        os.system("tput setaf 7")
        print("\n")
        osname = input("Enter the container name which you want to delete :")
        cmd= "sudo docker container rm -f {}".format(osname)
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status==0:
            print("{} Container Removed..!!".format(osname))

        else:
            print("error : {}".format(out))

    elif "remove all containers" in data:
        cmd= "sudo docker rm -f $(docker ps -aq)"
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status == 0:
            print("All Containers removed Successfully...!!")

        else:
            print("Error :{}".format(out))

    elif "show all running containers" in data:
        cmd = "sudo docker ps"
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status == 0:
            print(out)

        else:
            print("error : {}".format(out))

    elif "show all containers" in data:
        cmd = "sudo docker ps -a"
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status ==0:
            print(out)

        else:
            print("Error :{}".format(out))

    elif "pull docker image" in data:
        oimage = input("Enter the image name and it's version which you want to pull :")
        cmd = "docker pull {}".format(oimage)
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status ==0:
            print("Image Pulled Successfully..!!")
        else:
            print("error : {}".format(out))

    elif "show all docker images" in data:
        cmd = "sudo docker images"
        output = subprocess.getstatusoutput(cmd)

        status=output[0]
        out = output[1]

        if status==0:
            print(out)

        else:
            print("error :{}".format(out))

    elif "create docker image" in data:
        print("\n\n\t\t please run minimum 1 container to create your docker image ")
        print()
        osname=input("Enter the Container name of which you want to create image:")
        iname = input("Enter the Image Name :")
        iversion= input("Enter the Image Version :")
        os.system("tput setaf 2")
        print("--------------------")
        os.system("tput setaf 7")
        print("--------------------")
        cmd = "sudo docker commit {} {}:{}".format(osname,iname,iversion)
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status ==0:
            print("\n")
            print("Image Created...!!!")
            print("Image Name : {}".format(iname))
            print("Image Version : {}".format(iversion))

        else:
            print("error :{}".format(out))

    elif "delete docker image" in data:
        print("Images Available :\n")
        os.system("sudo docker images")
        os.system("tput setaf 3")
        print("\t\t\t***********************")
        os.system("tput setaf 7")
        print("\n")
        oimage=input("Enter the Image name and it's version which you want to delete :")
        cmd = "docker rmi -f {}".format(oimage)
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status ==0:
            print("Image deleted Successfully...!!")

        else:
            print("error :{}".format(out))
    

    
    elif "exit" in data:
            exit()
    else :
            print("entered invalid option")
    




while True:
  os.system("clear")
  os.system("tput setaf 5")
  os.system("echo 'Welcome to Python Menu' | figlet -f cybermedium -d ./figletfonts40/ ")
  os.system("tput setaf 7")
  print("\n\n\n-----------------------------------------------------------------------------------------------------------------------------------------") 
  os.system("tput setaf 6")
  os.system("\n\n\n\t\t\t echo MAIN MENU | figlet -f wideterm -d ./figletfonts40/")
  os.system("tput setaf 3")

  print("""
    \n\n
    Press 1 :Linux Commands
    Press 2 :AWS Services
    Press 3 :LVM Partition
    Press 4 :Hadoop
    Press 5 :Configuration Of Web Server 
    Press 6 :Docker
    press 7 :To predict through machine learning model(linear regression)
    Press 8 :To Reboot
    press 9 :To open any website to login like gmail & many more
    Press 10 :To Exit
    """)

  if "local" in loc:
      loc="local"

  os.system("tput setaf 7")
  if loc=="local":

    data=gtts("please tell us which technology you want to use from above shown menu : ")

    




    ch="0"
    if "Linux" in data:
     while True: 

        os.system("clear")
        os.system("tput setaf 2")
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        os.system("tput setaf 4")
        name = "\"LINUX TUI\""
        os.system("echo {0} | figlet -f smmono12 -d ./figletfonts40/ ".format(name))
        os.system("tput setaf 3")
        os.system("echo DOCKER TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
        os.system("tput setaf 5")
        print("\t\t\t\t\t\t\t\t...Do things of LINUX with a click")
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        os.system("tput setaf 2")
        print("...LINUX Main Menu...")
        os.system("tput setaf 3")
        print("""
            \n
            Press 1 :date
            Press 2 :cal
            Press 3 :list
            Press 4 :available Storage
            Press 5 :free Ram
            Press 6 :Cpu usage
            Press 7 :whoami
            Press 8 :jobs
            Press 9 :To add User
            Press 10 :To run any command of Linux
            press 11: to see all mounted devices/volumes
            Press 12 :To go to base menu
            press 13 :to exit
            """)
        
        data=gtts("please tell which Linux command you want to use : ")
        
        if "date" in data:
                print("\n\n\t")
                os.system("date")
        elif "cal" in data or "calender" in data :
                print("\n\n\t")
                os.system("cal")
        elif (("list" in data) or ("directory" in data)):
                path=input("Enter the path of the folder you want to see the list :")
                list_dir=subprocess.getoutput("ls "+path)
                print("\n")
                print(list_dir)

        elif "storage" in data:
                print("\n\n\t")
                os.system("df -h")
        elif "Ram" in data or "ram" in data:
                print("\n\n\t")
                os.system("free -m")
        elif "CPU" in data:
                print("\n\n\t")
                os.system("lscpu")
        elif "current" in data and "user" in data:
                print("\n\n\t")
                os.system("whoami")
        elif "jobs" in data :
                print("\n\n\t")
                os.system("echo 'echo' & ")
                os.system("jobs")
                print("\n\n\t\t only echo is running ")
        elif "add" in data and "user" in data:
                print("\n\n\t")
                user = input("Enter user name :")
                s=subprocess.getstatusoutput("useradd "+user)
                status=s[0]
                output=s[1]
                if status==0 :
                    os.system("passwd {}".format(user))
                    print("Password Created Successfully!!!")
                else :
                    print("Error : {}".format(output))

        elif "run" in data and "any" in data and "Linux" in data:
                cmd = input("Enter your command :")
                s=subprocess.getstatusoutput(cmd)
                status=s[0]
                output=s[1]
                print(output)
        

        elif "all mounted devices" in data:
            print("\n\n\t")
            os.system("df -h")
        
        elif "base menu" in data or "main menu" in data  :
                break
        elif "exit" in data:
            exit()
        else :
                print("entered invalid option")        
        input("\n\n\t\t press enter to keep using this sub-menu : ")   


    elif "docker" in data:
     while True:
        os.system("clear")
        os.system("tput setaf 2")
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        os.system("tput setaf 4")
        name = "\"DOCKER TUI\""
        os.system("echo {0} | figlet -f smmono12 -d ./figletfonts40/ ".format(name))
        os.system("tput setaf 3")
        os.system("echo DOCKER TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
        os.system("tput setaf 5")
        print("\t\t\t\t\t\t\t\t...Do things of DOCKER with a click")
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        os.system("tput setaf 2")
        print("...DOCKER Main Menu...")
        os.system("tput setaf 3")
        print("""
            Press 1  : To Launch docker Container
            Press 2  : To Start docker  Container
            Press 3  : To Stop docker Container
            Press 4  : To Delete docker Container
            Press 5  : To Delete all  docker Container at once
            Press 6  : To Show all docker running Containers
            Press 7  : To Stop all docker Container
            Press 8  : To Pull docker Images
            Press 9  : To Show docker Images
            Press 10 : To Create docker Images
            Press 11 : To delete docker Images
            press 12 : To go to the base menu
            press 13 : To exit
            """)
        data=gtts("please choose any of the docker option ashown above in the menu")
        print(data)
        os.system("tput setaf 2 ")
        print("\t\t\t\t\t********************")
        print("\n")
        os.system("tput setaf 7")
        if "base menu" in data or "main menu" in data or "previous menu" in data:
            break
        function(data)
        input("press enter to keep using this sub-menu : ")
    

    elif int(ch)==7:
        os.system("tput setaf 2")
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        os.system("tput setaf 4")
        name = "\"MACHINE LEARNING TUI\""
        os.system("echo {0} | figlet -f smmono12 -d ./figletfonts40/ ".format(name))
        os.system("tput setaf 3")
        os.system("echo MACHINE LEARNING TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
        os.system("tput setaf 5")
        print("\t\t\t\t\t\t\t\t...Do things of ML with a click")
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        os.system("tput setaf 2")
        print("...MACHINE LEARNING Main Menu...")
        os.system("tput setaf 3")
        print("\t\twarning !!!! user should have sklearn and joblib pre-installed ,if it is not then use 'pip3 install sklearn' & 'pip3 install joblib'(as a pre-requisite) ")

        input("plz enter ur csv file name(with extension) as a dataset to use ml(linear regression) to create model and predict the things :               ")
        import joblib
        model=joblib.load("salary.pkl")
        exp=input("Enter ur experience(in years) to predict salary : ")
        predicted_value=model.predict([[int(exp)]])
        print("\n\n\t\t", predicted_value)
        os.system("tput setaf 2")
        print("\n\n\t\t this result is ur predicted salary ml linear regression model")
        os.system("tput setaf 7")


    elif "reboot" in data:
        os.system("init 0")

    elif "open website" in data:
     import webbrowser   
     while True:
        os.system("clear")
        os.system("tput setaf 2")
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        os.system("tput setaf 4")
        name = "\"WEB TUI\""
        os.system("echo {0} | figlet -f smmono12 -d ./figletfonts40/ ".format(name))
        os.system("tput setaf 3")
        os.system("echo WEB TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
        os.system("tput setaf 5")
        print("\t\t\t\t\t\t\t\t...Do things of any Web with a click")
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        os.system("tput setaf 2")
        print("...WEBSITES Main Menu...")
        os.system("tput setaf 3")

        print("""
          \n\n
          press 1:to open gmail
          press 2:to open linkedin
          press 3:to open google
          press 4:to open google drive
          press 5:to open github
          press 6:to open aws cloud console
          press 7:to open zoom
          press 8:to open hotstar
          press 9:to go to the base menu
          press 10:to exit
            """)
        data=gtts("please give your desired website to open in browser for simply login")
        if "Gmail" in data:
            print("\n\n\t")
            webbrowser.open("https://mail.google.com")
        if "Linkedin" in data:
            print("\n\n\t")
            webbrowser.open("https://www.linkedin.com")
        if "Google" in data:
            print("\n\n\t")
            webbrowser.open("https://www.google.com")
        if "Google Drive" in data:
            print("\n\n\t")
            webbrowser.open("https://drive.google.com")
        if "Github" in data:
            print("\n\n\t")
            webbrowser.open("https://www.github.com")
        if "a WS" in data or "a w s" in data and "cloud console" in data:
            print("\n\n\t")
            webbrowser.open("https://aws.amazon.com")
        if "Zoom" in data:
            print("\n\n\t")
            webbrowser.open("https://zoom.us")
        if "Hotstar" in data:
            print("\n\n\t")
            webbrowser.open("https://www.hotstar.com")
        if "exit" in data:
            exit()
        if "main menu" in data or "base menu" in data or "previous menu" in data:
            break
        input("\n\n\t\tpress enter to keep using this sub-menu : ")

    elif "AWS" in data or "a w s" in data or "A WS" in data:
        while True:
         os.system("clear")
         os.system("tput setaf 1")
         print('\n\n  REMINDER !!! YOU SHOULD RUN "aws configure" CMD ONCE BEFORE USING THIS AUTOMATED MENU SO THAT AWS CAN AUTHENTICATE U ')
         os.system("tput setaf 7")
         os.system("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\"AWS TUI\""
         os.system("echo {0} | figlet -f smmono12 -d ./figletfonts40/".format(name))
         os.system("tput setaf 2")
         os.system("echo AWS TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 2")
         print("\t\t\t\t\t\t\t\t...Do things of AWS with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 6")
         print("\t\t\t\t\tAWS Menu ")
         print("\t\t\t\t\t----")
         os.system("tput setaf 3")
         print("""
\n\n
press 1 : to configure aws cli
press 2 : to create iam user
press 3 : to attach user-policy to newly created iam user
press 4 : to generate access key and secret key for this user
press 5 : to create key pair
press 6 : to create security group
press 7 : to add ingress rule to created security group
press 8 : to attach this newly created security group to local os
press 9 : to launch new instance attaching newly created key pair and security group
press 10 : to create and attach new ebs volume to new launched os
press 11 : to create and attach new ebs volume to local os
press 12 : to create new partition from newly attached ebs and format and mount it 
press 13 : to extend static partition size without deleting data 
press 14 : to create s3 bucket
press 15 : to upload some object file in this s3 bucket
press 16 : to create cloudfront distribution for this s3 origin and to retrieve cloudfront url for object
press 17 : to go to the base menu
press 18 : to exit
""")
         os.system("tput setaf 7")
         data=gtts("plz tell which aws service you want to use")
         print(data)

         if "configure" in data or "aws" in data or "cli" in data:
          print("you should be ready with your credentials like access and secret key to use cli \n\n")   
          os.system("aws configure")
         
         elif "create" in data and "i a m" in data or "a m" in data and "user" in data:
          username=input("plz give ur new iam user name : ")   
          os.system("aws iam create-user --user-name {}".format(username))
          os.system("tput setaf 2")
          print("\n\n new iam user has been created successfully")
          os.system("tput setaf 7")
         
         elif "attach" in data and "user" in data and "policy" in data or "i a m" in data:
          os.system("aws iam attach-user-policy --user-name {} --policy-arn arn:aws:iam::aws:policy/PowerUserAccess ".format(username))
          os.system("tput setaf 2")
          print("\n\n user policy has been attached successfully")
          os.system("tput setaf 7")
         
         elif "generate" in data and "access" in data and "secret" in data:
          os.system("tput setaf 6 ")
          print('\n\n ATTENTION REQUIRED!!! YOU SHOULD KEEP THESE CREDENTIALS SAFE AND COPIED IN 1 FILE ,FOR UR CONVINIENCE THE OUTPUT IS BY DEFAULT SAVED IN "IAM_CRED_<iam username here(vary as per your choice)>.txt" ')
          os.system("tput setaf 7 ")
          username=input("plz give ur desired username to generate credentials : ")
          os.system("aws iam create-access-key --user-name {0} > IAM_CRED_{0}.txt".format(username))   
          os.system("tput setaf 2")
          print("\n\n new access key for this user {} has been generated successfully".format(username))
          os.system("tput setaf 7")
         
         elif "create" in data and "key" in data and "pair" in data:
          keypairname=input("plz enter ur key pair name : ")
          x=subprocess.getoutput("aws ec2 create-key-pair --key-name {0}".format(keypairname))
          x=json.loads(x)
          keypair=x['KeyMaterial']
          file="{}.pem".format(keypairname)
          stdout(file)
          os.system("sed -i 's/[\\]n/\\n/g' {}".format(file))
          os.system("chmod 400 {}".format(file))
          os.system("tput setaf 2")
          print("\n\n\t\t new key pair created successfully")
          os.system("tput setaf 7")





         elif "create" in data and "security" in data and "group" in data:
             
          sg=input("plz enter your desired name to new security group : ")
          os.system('aws ec2 create-security-group --description "allow all" --group-name {} --tag-specifications ResourceType="security-group",Tags=["{{Key=Name,Value=menu-sg}}"]'.format(sg))
          os.system("tput setaf 2")
          print(" \n\n new security group created successfully") 
          os.system("tput setaf 7")


         elif "add" in data and "Ingress" in data and "rule" in data:
          x=subprocess.getoutput("aws ec2 describe-security-groups --filters Name=tag-key,Values=Name Name=tag-value,Values=menu-sg")
          x=json.loads(x)
          gid=x["SecurityGroups"][0]["GroupId"]
          port=input("\n\n enter the port on which u want to allow the outside world to ur os : ")
          os.system("aws ec2 authorize-security-group-ingress --group-id {} --protocol all --port {} --cidr 0.0.0.0/0 ".format(gid,port))
          os.system("tput setaf 2")
          print("\n\n security group ingress rule has been added successfully")
          os.system("tput setaf 7")


      

         elif "attach" in data and "new security group" in data and "local OS" in data:
          y=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-value,Values=slave1")
          y=json.loads(y)
          localostag=y['Reservations'][0]['Instances'][0]['Tags'][0]['Value']   
          x=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-key,Values=Name Name=tag-value,Values={}".format(localostag))
          x=json.loads(x)
          osid=x["Reservations"][0]["Instances"][0]["InstanceId"]   
          os.system("aws ec2 modify-instance-attribute --instance-id {}  --groups {}".format(osid,gid))
          os.system("tput setaf 2")
          print("\n\n new security has been attached to your running local os successfully")
          os.system("tput setaf 7")
             
         elif "launch" in data and "new" in data and( "a w s" in data or "A WS" in data) and "instance" in data:
          x=subprocess.getoutput("aws ec2 describe-security-groups --filters Name=tag-key,Values=Name Name=tag-value,Values=menu-sg")
          x=json.loads(x)
          gid=x["SecurityGroups"][0]["GroupId"]
          cnt=int(input("plz give input how many instances u want to launch : "))
          itag=input("plz give your new os a tag : ")
          os.system("aws ec2 run-instances --security-group-ids {} --instance-type t2.micro --count {} --image-id ami-0e306788ff2473ccb --key-name {} --tag-specifications ResourceType=instance,Tags=['{{Key=Name,Value={} }}'] ".format(gid,cnt,keypairname,itag))
          os.system("tput setaf 2")
          print("\n\n yay,ur new full flash aws instance is launched and ready to use")
          os.system("tput setaf 7")
      

         elif "create and attach" in data and "new EBS" in data and "new OS" in data:
          volume("{}".format(itag))





         elif "create and attach" in data and "new EBS" in data and "local OS" in data:
          os.system("tput setaf 6")
          itag="slave1"   
          volume("{}".format(itag))
          os.system("tput setaf 7")
         

         elif "new partition" in data or "format" in data or "mount" in data:
             hd1=subprocess.getoutput("aws ec2 describe-volumes --filters Name=tag-value,Values={}".format(ebsdb[0]))
             hd1=json.loads(hd1)
             hd1=hd1["Volumes"][0]["Attachments"][0]["Device"]
             os.system("fdisk {}".format(hd1))
             print("\n\n successfully created partition")
             input("\n\n press Enter to format this partition : ")
             os.system("mkfs.ext4 {}1".format(hd1))
             print("\n\n successfully formatted partition")
             input("\n\n press Enter to mount this partition : ")
             folder=input("plz give ur folder name/path where u want to mount : ")
             os.system("mkdir /{}".format(folder))
             os.system("mount {}1 /{}".format(hd1,folder))
             os.system("tput setaf 2")
             print("\n\n partition mounted successfully and now u can store data in {} directory and all data will be persistent even if ur os/system/root hard disk get corrupt ".format(folder))
             os.system("tput setaf 7")
             os.system("df -h")
             print("here 'type' term means do you want to type : ")
             input1=input("what u have to put in  : file/type ")
             
             if input1=="file":
              source=input("plz give ur file name/path to copy in ur directory {}".format(folder))   
              os.system("cp {} {}".format(source,folder))   
              print("\n\n\t\t file copied successfully")

             else:
              print('here press Enter to go to next line and ctrl+d to stop writing and save code in "arth.txt"  ')
              os.system("cat > /{}/arth.txt".format(folder))
              print("\n\n\t\t ur code saved succesfully")
              
             
                 
         elif "extend" in data and "static" in data and "partition" in data:
          hd1=subprocess.getoutput("aws ec2 describe-volumes --filters Name=tag-value,Values={}".format(ebsdb[0]))
          hd1=json.loads(hd1)
          hd1=hd1["Volumes"][0]["Attachments"][0]["Device"]
          x=subprocess.getoutput("umount {}1".format(hd1))
          os.system("e2fsck -f  {}1".format(hd1)) 
          os.system("fdisk {}".format(hd1))
          print('give more size(in GIB) to extend partition and give no when it gives an option like "do u want to remove ur signature" so that we dont lose previous data ')
          print("\n\n press enter to check ur partition consistency like inode tables,references or some internal metadata is stable or giving some error")
          os.system("resize2fs {}1".format(hd1))
          folder=input("plz give ur folder name/path where u want to mount : ")
          os.system("mkdir /{}".format(folder))
          os.system("mount {}1 /{}".format(hd1,folder))
          os.system("cd /{};cat arth.txt".format(folder))
          print("see here,ur data is there and it has not been lost ")
          os.system("df -h")
          os.system("tput setaf 2")
          print("\n\n ur static partition size is also extended now with the same data ,see above")
          os.system("tput setaf 7")
         
         
         elif "create S3 bucket" in data:
          bucket=input("plz enter a new bucket name")
          os.system("aws s3 mb s3://{} --region ap-south-1".format(bucket))
          os.system("tput setaf 2")
          print("\n\n s3 bucket created successfully ")
          os.system("tput setaf 7")

         elif "upload object to S3" in data:
          print("for ur convenience, i am listing all the files so that u can filter what to upload in bucket ")
          os.system("ls")
          img=input("plz enter ur object name to upload to s3 bucket")   
          os.system("aws s3 cp {} s3://{} --acl public-read ".format(img,bucket))
          os.system("tput setaf 2")
          print("\n\n succcesfully uploaded ur object to s3 bucket")
          os.system("tput setaf 7")
         
         elif "create cloudfront distribution" in data:
          x=subprocess.getoutput("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com".format(bucket))
          x=json.loads(x)
          x=x['Distribution']['DomainName']
          cloudfront_url="https://{}/{}".format(x,img)
          os.system("tput setaf 2")
          print("\n\n ur cloudfront distribution has been created successfully")
          print("\n\n ur cloudfront url is : {}".format(cloudfront_url))
          print("\n\n plz copy this url as u can use this url in ur web server to display this object by giving this url in webpages for faster content delivery and very less latency all across the world")
          os.system("tput setaf 7")
          
         elif "main menu" in data or "previous menu" in data or "base menu" in data:
                break
         elif "exit" in data:
            exit()
         else :
                print("entered invalid option")
         input("press enter to keep using this sub-menu : ")


    elif "lvm" in data:
        while True:
         os.system("clear")   
         os.system("tput setaf 3")
         print("\n\n REMINDER !!! ,IF U WANT TO EXTEND VG THEN FIRST ATTACH NEW EBS VOLUME ,FOR THAT GO TO OPTION 3 IF U HAVEN'T DONE YET")   
         os.system("tput setaf 7")
         os.system("tput setaf 2")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\"LVM  TUI\""
         os.system("echo {0} | figlet -f smmono12 -d ./figletfonts40/ ".format(name))
         os.system("tput setaf 3")
         os.system("echo   LVM  TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 5")
         print("\t\t\t\t\t\t\t\t...Do things of LVM with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system(" tput setaf 2")
         print("...LVM Main Menu...")
         os.system(" tput setaf 3 ")
         print("""
\n\n
press 6 : to create LVM partition
press 7 : to extend lv size
press 8 : to reduce lv size
press 9 : to extend VG size
press 10 : to go to the base menu
press 11 : to exit
""")     
         os.system(" tput setaf 7")
         data=gtts("could you please tell what lvm option you want to use")

         if "create lvm partition" in data:
          os.system("tput setaf 2")   
          hd1=subprocess.getoutput("aws ec2 describe-volumes --filters Name=tag-value,Values={}".format(ebsdb[0]))
          hd2=subprocess.getoutput("aws ec2 describe-volumes --filters Name=tag-value,Values={}".format(ebsdb[1]))
          hd1=json.loads(hd1)
          hd2=json.loads(hd2)
          hd1=hd1["Volumes"][0]["Attachments"][0]["Device"]
          hd2=hd2["Volumes"][0]["Attachments"][0]["Device"]
          os.system("tput setaf 5")
          os.system("pvcreate {}".format(hd1))
          os.system("pvdisplay {}".format(hd1))
          os.system("tput setaf 6")
          os.system("pvcreate {}".format(hd2))
          os.system("pvdisplay {}".format(hd2))
          os.system("tput setaf 3")
          vg=input("enter your vg name : ")
          os.system("tput setaf 4")
          os.system("vgcreate {} {} {}".format(vg,hd1,hd2))
          os.system("vgdisplay {}".format(vg))
          os.system("tput setaf 3")
          lvname=input("enter your lv name : ")
          lvsize=input("enter your lv size : ")
          os.system("tput setaf 3")
          os.system("lvcreate --size {}GB --name {} {}".format(lvsize,lvname,vg))
          os.system("tput setaf 2")
          print("successfully created logical volume")
          os.system("tput setaf 7")
          os.system("tput setaf 4")
          os.system("lvdisplay /dev/{}/{}".format(vg,lvname))
          os.system("tput setaf 3")
          input("press enter to format your lv {}  : ".format(lvname))
          os.system("mkfs.ext4 /dev/{}/{}".format(vg,lvname))
          os.system("tput setaf 3")
          print("your lv {} succesfully formatted".format(lvname))
          os.system("tput setaf 4")
          dir=input("enter new folder to create where this lv will be mounted : ")
          os.system("mkdir /{}".format(dir))
          os.system("mount /dev/{}/{} /{}".format(vg,lvname,dir))
          os.system("tput setaf 6")
          print("successfully mounted your lv {} to folder {}".format(lvname,dir))
          os.system("tput setaf 2")
          print("\n\n do you want to extend this lv size ,go for option 7")
          os.system("tput setaf 7")




         elif "extend lv size" in data:
          os.system("tput setaf 3")
          extended_size=input("plz enter how much size(in GB) U want to extend to ur lv : ")
          os.system("tput setaf 6")
          os.system("lvextend --size +{}GB /dev/{}/{}".format(extended_size,vg,lvname)) 
          os.system("resize2fs /dev/{}/{}".format(vg,lvname))
          os.system("tput setaf 2")
          print("\n\n successfully extended your lv")
          os.system("tput setaf 7")

     
         elif "reduce lv size" in data:
          os.system("tput setaf 5")
          reduced_size=input("plz enter how much size(in GB) U want to reduce to ur lv : ")
          os.system("tput setaf 3")
          os.system("lvreduce --size -{}GB /dev/{}/{}".format(extended_size,vg,lvname))
          os.system("resize2fs /dev/{}/{}".format(vg,lvname))
          os.system("tput setaf 2")
          print("\n\n successfully reduced your lv")
          os.system("tput setaf 7")


         elif "extend vg size" in data:
          os.system("tput setaf 1")   
          print("REMINDER !!! ,IF U WANT TO EXTEND VG THEN FIRST ATTACH NEW EBS VOLUME ,FOR THAT GO TO OPTION 3 IF U HAVEN'T DONE YET")
          
          hd3=subprocess.getoutput("aws ec2 describe-volumes --filters Name=tag-value,Values={}".format(ebsdb[2]))
          hd3=json.loads(hd3)
          devname=hd3["Volumes"][0]["Attachments"][0]["Device"]
          vg=input("enter your old vg name : ")
          os.system("tput setaf 6")
          os.system("pvcreate {}".format(devname))
          os.system("pvdisplay {}".format(devname))
          os.system("vgextend {} {}".format(vg,devname))
          os.system("vgdisplay {}".format(vg))
          os.system("tput setaf 5")
          sizelv=input("plz enter ur size to extend in lv : ")
          os.system("lvextend --size +{}GB /dev/{}/{}".format(sizelv,vg,lvname))
          os.system("resize2fs /dev/{}/{}".format(vg,lvname))
          os.system("tput setaf 2")
          print("\n\n successsfully extended your vg and lv through new ebs volume")
          os.system("tput setaf 7")
         

         elif "main menu" in data or "previous menu" in data or "base menu" in data:
                break
         elif "exit" in data:
            exit()
         else : 
                os.system("tput setaf 1")
                print("entered invalid option")
         os.system("tput setaf 4")       
         input("press enter to keep using this sub-menu : ")
         os.system("tput setaf 7")

    elif "hadoop" in data:
        while True:
         os.system("clear")
         os.system("tput setaf 2")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\"HADOOP  TUI\""
         os.system("echo {0} | figlet -f smmono12 -d ./figletfonts40/ ".format(name))
         os.system("tput setaf 3")
         os.system("echo   HADOOP  TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 5")
         print("\t\t\t\t\t\t\t\t...Do things of Hadoop with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system(" tput setaf 2")
         print("...HADOOP Main Menu...")
         os.system(" tput setaf 3 ")
         print("""
\n\n
press 11 : to configure hadoop master node
press 12 : to configure hadoop slave node
press 13 : to configure hadoop client node
press 14 : to leave hadoop safe mode
press 15 : to upload file from client
press 16 : to read file from client
press 17 : to run tcpdump to save packets coming to your ip in a file
press 18 : to see packets coming to your ip
press 19 : to go to the base menu
press 20 : to exit
""")
         data=gtts("please tell which hadoop option do you want to use that is shown above")
         if "master" in data:
          os.system("rpm -ivh jdk-8u171-linux-x64.rpm ")
          os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force ")
          randomnumber=random.randint(1,100)
          os.system("mkdir /dn{}".format(randomnumber))
          pubip=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-value,Values=slave1")
          pubip=json.loads(pubip)
          pubip=pubip['Reservations'][0]['Instances'][0]['PublicIpAddress']
          os.system("sed -i 's/dn/dn{}/g' hdfs-site.xml".format(randomnumber))
          os.system("sed -i 's/masterip/{}/g' core-site.xml".format(pubip))
          os.system("cp hdfs-site.xml /etc/hadoop/hdfs-site.xml  ")
          os.system("cp core-site.xml /etc/hadoop/core-site.xml  ")
          os.system("hadoop-daemon.sh start datanode")
          os.system("jps")
          os.system("tput setaf 2")
          print("\n\n\t\t succesfully configured slave node")
          os.system("tput setaf 7")
          input("press enter to see how many slaves are connected to master")
          os.system("hadoop dfsadmin -report")
          os.system("sed -i 's/dn{}/dn/g' hdfs-site.xml".format(randomnumber))
          os.system("sed -i 's/{}/masterip/g' core-site.xml".format(pubip))
     
    




         elif "slave" in data:   
          os.system("rpm -ivh jdk-8u171-linux-x64.rpm ")
          os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force ")
          randomnumber=random.randint(1,100)
          os.system("mkdir /nn{}".format(randomnumber))
          os.system("sed -i 's/masterip/0.0.0.0/g' core-site-master.xml")
          os.system("sed -i 's/data/name/2' hdfs-site-master.xml")
          os.system("sed -i 's/dn/nn{}/g' hdfs-site-master.xml".format(randomnumber))
          os.system("cp hdfs-site-master.xml /etc/hadoop/hdfs-site.xml")
          os.system("cp core-site-master.xml /etc/hadoop/core-site.xml")
          os.system("hadoop namenode -format")
          os.system("hadoop-daemon.sh start namenode")
          os.system("jps")
          os.system("tput setaf 2")
          print("\n\n\t\t succesfully configured master node")
          os.system("tput setaf 7")
          input("press enter to see how many slaves are connected to master")
          os.system("hadoop dfsadmin -report")

      

         elif "configure client" in data:
          pubip=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-value,Values=slave1")
          pubip=json.loads(pubip)
          pubip=pubip['Reservations'][0]['Instances'][0]['PublicIpAddress']
          
          os.system("rpm -ivh jdk-8u171-linux-x64.rpm ")
          os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force ")
          os.system("sed -i 's/masterip/{}/g' core-site-client.xml".format(pubip))
          os.system("cp core-site-client.xml /etc/hadoop/core-site.xml")
          os.system("tput setaf 2")
          print("\n\n\t\t succesfully configured client node")
          os.system("tput setaf 7")




                  
         elif "exit" in data:
          os.system("tput setaf 1")
          print("it seems you have exited,see u again")
          os.system("tput setaf 7")
          exit()


      

         elif "upload file" in data:
          print("here 'type' term means do you want to type : ")
          input1=input("what u have to put in web server : file/type ")
          if input1=="file":
              file=input("plz enter your file name/path to upload from client : ")
              os.system("hadoop fs -put {} /".format(file))
              print("file uploaded successfully")
          
          else:
              print('press "Enter" to go to next line and "ctrl+d" to stop writing and save ur code')
              os.system("cat > web.html")
              os.system("hadoop fs -put {} /".format(web.html))
              print("file uploaded successfully")
         elif "read file" in data:
          file=input("plz enter your file name/path to read from hadoop cluster : ")
          os.system("hadoop fs -cat /{}".format(file))
      
         elif "leave hadoop safe mode" in data:
          os.system("hadoop dfsadmin -safemode get")
          os.system("hadoop dfsadmin -safemode leave")
          print("successfully left safe mode")
      

         elif "tcpdump" in data:
          os.system("tcpdump -i eth0 -n tcp port not 22 > pkt.txt")
          print("press ctrl+c to stop this cmd")
      
         elif "see packets" in data:
          os.system("vim pkt.txt")
         
         elif "main menu" in data or "base menu" in data or "previous menu" in data:
          break
         
         else :
          print("entered invalid option")
         input("press enter to keep using this sub-menu : ")

    elif "configure web server" in data:
          pubip=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-value,Values=slave1")
          pubip=json.loads(pubip)
          pubip=pubip['Reservations'][0]['Instances'][0]['PublicIpAddress']
          print("here 'type' term means do you want to type : ")
          input1=input("what u have to put in web server : file/type :  ")
          if input1=="file":
              print("wait till the time respective software is downloading ")
              os.system("yum install httpd -y")
              input1=input("plz input ur file/path to show as web pages in web server : ")
              os.system("chmod 777 /var/www/html/")
              os.system("cp {} /var/www/html/".format(input1))
              os.system("systemctl start httpd")
              os.system("systemctl enable httpd")
              print("ur web server configured successfully")
              input("press enter to connect to ur new webserver while it is working or not : ")
              os.system("curl http://{}:/{}".format(pubip,input1))
          else:
              os.system("cat > web1.html")
              os.system("yum install httpd -y")
              os.system("chmod 777 /var/www/html/")
              os.system("cp web1.html /var/www/html/")
              os.system("systemctl start httpd")
              print("ur web server configured successfully")
              input("press enter to connect to ur new webserver while it is working or not : ")
              os.system("curl http://{}:/{}".format(pubip,input1))

          input("press enter to go to the base menu : ")
          break   



    elif "exit" in data:
        pubip=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-value,Values=slave2")
        pubip=json.loads(pubip)
        pubip=pubip['Reservations'][0]['Instances'][0]['PublicIpAddress']
        os.system("tput setaf 1")
        print("it seems you have exited,hope to see u again ")
        os.system("tput setaf 3")
        print("\n\n\t\tREQUEST!!!!! U ARE OUR VALUABLE AND FOREMOST/PRIORITY CUSTOMER/USER ,YOUR FEEDBACK MATTERS FOR US ,PLZ GIVE UR SOME TIME TO GIVE FEEDBACK TO THIS MENU AS UR FEEDBACK WILL KEEP ON MAKING THIS MENU MORE AND MORE USER FRIENDLY : \n\t ")
        os.system("tput setaf 7")
        random1=random.randint(1,100)
        os.system("cat > feedback{}.txt".format(random1))
        print("\n\n\t")
        os.system("scp -i slave1.pem feedback{}.txt ec2-user@{}:/home/ec2-user".format(random1,pubip))
        print("\n\n\t\t your valuable feedback has been reached to us via network,thanks,\n we hope u will come again soon to give us one more chance to serve you more comparatively better")
        exit()

    
    else:
        os.system("tput setaf 1")
        print("\n\n you have entered an invalid option !!! ,don't worry try menu option correctly again, it is so easy to use ")
        os.system("tput setaf 7")



    os.system("tput setaf 6")
    input("\n\n press Enter to continue using BASE menu : ")
    os.system("tput setaf 7")
  



  if loc=="remote":
    pubip=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-value,Values=slave2")
    pubip=json.loads(pubip)
    pubip=pubip['Reservations'][0]['Instances'][0]['PublicIpAddress']  


    ch=input("Enter your choice : ")





    if int(ch)==1:
     while True:

        os.system("clear")
        print("""
            \n
            Press 1 :date
            Press 2 :cal
            Press 3 :list
            Press 4 :Storage
            Press 5 :free Ram
            Press 6 :Cpu usage
            Press 7 :whoami
            Press 8 :jobs
            Press 9 :To add User
            Press 10 :To run any command of Linux
            press 11: to see all mounted devices/volumes
            Press 12 :To go to base menu
            press 13 :to exit
            """)

        p = input("Enter your Choice :")

        if int(p) == 1 :
            os.system("ssh -i slave1.pem ec2-user@{} date".format(pubip))
        elif int(p) == 2 :
                os.system("ssh -i slave1.pem ec2-user@{} cal".format(pubip))
        elif int(p) == 3 :
                path=input("Enter the path of the folder you want to see the list :")
                list_dir=subprocess.getoutput("ssh -i slave1.pem ec2-user@{} ls {}".format(pubip,path))
                print("\n")
                print(list_dir)

        elif int(p) == 4 :
                os.system("ssh -i slave1.pem ec2-user@{} df -h".format(pubip))
        elif int(p) == 5 :
                os.system("ssh -i slave1.pem ec2-user@{} free -m".format(pubip))
        elif int(p) == 6 :
                os.system("ssh -i slave1.pem ec2-user@{} lscpu".format(pubip))
        elif int(p) == 7 :
                os.system("ssh -i slave1.pem ec2-user@{} whoami".format(pubip))
        elif int(p) == 8 :
                os.system("ssh -i slave1.pem ec2-user@{} echo 'echo' &".format(pubip))
                os.system("ssh -i slave1.pem ec2-user@{} jobs".format(pubip))
                print("\n\n\t\t only echo is running ")

        elif int(p) == 9 :
                user = input("Enter user name :")
                s=subprocess.getstatusoutput("ssh -i slave1.pem ec2-user@{} useradd {}".format(pubip,user))
                status=s[0]
                output=s[1]
                if status==0 :
                    os.system("ssh -i slave1.pem ec2-user@{} passwd {}".format(pubip,user))
                    print("Password Created Successfully!!!")
                else :
                    print("Error : {}".format(output))

        elif int(p)==10:
                cmd = input("Enter your command :")
                s=subprocess.getstatusoutput("ssh -i slave1.pem ec2-user@{} {}".format(pubip,cmd))
                status=s[0]
                output=s[1]
                print(output)


        elif int(p)==11:
            os.system("ssh -i slave1.pem ec2-user@{} df -h".format(pubip))

        elif int(p) == 12 :
                break
        elif int(p)==13:
            exit()
    
    elif int(ch)==5:
        while True:  
          print("here 'type' term means do you want to type : ")
          input1=input("what u have to put in web server : file/type ")
          if input1=="file":
              print("wait till the time respective software is downloading ")
              os.system("ssh -i slave1.pem ec2-user@{} sudo yum install httpd -y".format(pubip))
              print("\n\n\t\t ur software is downloaded successfully : ")
              input1=input("\n\t\tplz input ur file/path to show as web pages in web server : ")
              os.system("ssh -i slave1.pem ec2-user@{} sudo chmod 777 /var/www/html".format(pubip))
              os.system("scp -i slave1.pem {} ec2-user@{}:/var/www/html/".format(input1,pubip))
              os.system("ssh -i slave1.pem ec2-user@{} sudo systemctl start httpd".format(pubip))
              os.system("ssh -i slave1.pem ec2-user@{} sudo systemctl enable httpd".format(pubip))
              print("ur web server configured successfully")
              input("press enter to connect to ur new webserver while it is working or not : ")
              os.system("curl http://{}:/{}".format(pubip,input1))
              print("this is ur code ,see above")

          else:
              os.system("cat > web1.html")
              print("wait till the time respective software is downloading ")
              subprocess.getoutput("ssh -i slave1.pem ec2-user@{} sudo yum install httpd -y".format(pubip))
              print("\n\n\t\t ur software is downloaded successfully : ")
              os.system("ssh -i slave1.pem ec2-user@{} sudo chmod 777 /var/www/html".format(pubip))
              os.system("scp -i slave1.pem web1.html ec2-user@{}:/var/www/html/".format(pubip))
              os.system("ssh -i slave1.pem ec2-user@{} sudo systemctl start httpd".format(pubip))
              os.system("ssh -i slave1.pem ec2-user@{} sudo systemctl enable httpd".format(pubip))
              print("ur web server configured successfully")
              input("press enter to connect to ur new webserver while it is working or not : ")
              os.system("curl http://{}:/{}".format(pubip,input1))
              print("this is ur code ,see above")

          input("press enter to go to the base menu : ")
          break

    elif int(ch)==4:
        while True:
         os.system("clear")
         print("""
\n\n
press 11 : to configure hadoop master node
press 12 : to configure hadoop slave node
press 13 : to configure hadoop client node
press 15 : to upload file from client
press 16 : to read file from client
press 14 : to leave hadoop safe mode
press 17 : to run tcpdump to save packets coming to your ip in a file
press 18 : to see packets coming to your ip
press 19 : to go to the base menu
press 20 : to exit
""")
         p=input("plz enter ur choice : ")
         if int(p)==11:
          os.system("ssh -i slave1.pem ec2-user@{} sudo rpm -ivh jdk-8u171-linux-x64.rpm".format(pubip))
          os.system("ssh -i slave1.pem ec2-user@{} sudo rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force ".format(pubip))
          os.system("ssh -i slave1.pem ec2-user@{} sudo mkdir /nn1".format(pubip))
          os.system("sed -i 's/masterip/0.0.0.0/g' /home/ec2-user/core-site-master-remote.xml".format(pubip))
          os.system("sed -i 's/data/name/g' /home/ec2-user/hdfs-site-master-remote.xml".format(pubip))
          os.system("sed -i 's/dn/nn1/g' /home/ec2-user/hdfs-site-master.xml".format(pubip))
          os.system("scp -i slave1.pem hdfs-site-master-remote.xml ec2-user@{}:/etc/hadoop/hdfs-site.xml".format(pubip))
          os.system("scp -i slave1.pem core-site-master-remote.xml ec2-user@{}:/etc/hadoop/core-site.xml".format(pubip))
          os.system("ssh -i slave1.pem ec2-user@{} sudo hadoop namenode -format".format(pubip))
          os.system("ssh -i slave1.pem ec2-user@{} sudo hadoop-daemon.sh start namenode".format(pubip))
          os.system("ssh -i slave1.pem ec2-user@{} sudo jps".format(pubip))
          os.system("tput setaf 2")
          print("\n\n\t\t succesfully configured master node")
          os.system("tput setaf 7")
          input("press enter to see how many slaves are connected to master")
          os.system("ssh -i slave1.pem ec2-user@{} sudo hadoop dfsadmin -report".format(pubip))
         
         elif int(p)==19:
             break
         
         elif int(p)==20:
             exit()
         input("\n\n\t\tpress Enter to keep using sub-menu : ")    


    os.system("tput setaf 6")
    input("\n\n press Enter to continue using BASE menu : ")
    os.system("tput setaf 7")
