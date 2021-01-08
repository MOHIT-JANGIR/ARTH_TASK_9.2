import os
import getpass
import subprocess
import json
import random
import getpass



  
vg="myvg"
keypairname="mykey"
lvname="mylv"
devname="xvdh"
itag="myos"
privatekey="slave1.pem"
ebsdb=[]
devdb=[]
subprocess.getoutput(" tput setaf 6")
loc=getpass.getpass("where you want to run this menu ?(local/remote) : ")
subprocess.getoutput(" tput setaf 7")

subprocess.getoutput(" tput setaf 4")  
passwd=getpass.getpass("enter file execution password for authentication(only once) : ")
subprocess.getoutput(" tput setaf 7")

if passwd!="12":
          print("incorrect password")
          exit()



def volume(itag):

          ebs_size=getpass.getpass("give your ebs size(in GB) to create ebs volume : ")
          random1=random.randint(1,1000)
          ebsname="lvm_ebs_{}".format(random1)

          if len(ebsdb)==0:
              ebsdb.append(ebsname)
              subprocess.getoutput("tput setaf 6")
              subprocess.getoutput("aws ec2 create-volume --availability-zone ap-south-1a --volume-type gp2 --size {} --tag-specifications ResourceType=volume,Tags=['{{Key=Name,Value={}}}']".format(ebs_size,ebsname))
              subprocess.getoutput("tput setaf 2")
              print("\n\n\t\t your ebs volume has been created successfully")
              subprocess.getoutput("tput setaf 7")



          else:
              for i in ebsdb:
                  if i!=ebsname:
                      ebsdb.append(ebsname)
                      subprocess.getoutput("tput setaf 6")
                      subprocess.getoutput("aws ec2 create-volume --availability-zone ap-south-1a --volume-type gp2 --size {} --tag-specifications ResourceType=volume,Tags=['{{Key=Name,Value={}}}']".format(ebs_size,ebsname))
                      subprocess.getoutput("tput setaf 2")
                      print("\n\n\t\t your ebs volume has been created successfully")
                      subprocess.getoutput("tput setaf 7")
                      break
          subprocess.getoutput("tput setaf 5")
          getpass.getpass("\n\n press enter to attach your newly created ebs volume : ")
          subprocess.getoutput("tput setaf 6")
          vol=subprocess.getoutput("aws ec2 describe-volumes --filters Name=tag-key,Values=Name Name=tag-value,Values={}".format(ebsname))
          vol=json.loads(vol)
          vol=vol["Volumes"][0]["VolumeId"]
          dev=["xvdf","xvdg","xvdh","xvdi","xvdj","xvdk","xvdl","xvdm","xvdo","xvdp","xvdn","xvdq","xvdr","xvds","xvdt","xvdu","xvdw","xvdx","xvdy","xvdz"]
          devname=random.choice(dev)
                  

          if len(devdb)==0:
              devdb.append(devname)
              subprocess.getoutput("tput setaf 3")
              x=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-key,Values=Name Name=tag-value,Values={}".format(itag))
              x=json.loads(x)
              osid=x["Reservations"][0]["Instances"][0]["InstanceId"]
              subprocess.getoutput("tput setaf 6")
              subprocess.getoutput("aws ec2 attach-volume --instance-id {} --volume-id {} --device /dev/{}".format(osid,vol,devname))
              subprocess.getoutput("tput setaf 2")
              print("\n\n\t\t your ebs created and attached  successfully" )
              subprocess.getoutput("tput setaf 7")




          else:
              for i in devdb:
                  if i!=devname:
                      devdb.append(devname)
                      subprocess.getoutput("tput setaf 3")
                      x=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-key,Values=Name Name=tag-value,Values={}".format(itag))
                      x=json.loads(x)
                      osid=x["Reservations"][0]["Instances"][0]["InstanceId"]
                      subprocess.getoutput("tput setaf 6")
                      subprocess.getoutput("aws ec2 attach-volume --instance-id {} --volume-id {} --device /dev/{}   ".format(osid,vol,devname))
                      subprocess.getoutput("tput setaf 2")
                      print("\n\n\t\t your ebs created and attached  successfully" )
                      subprocess.getoutput("tput setaf 7")
                      break


def function(req):
    if req==1:
        osname = getpass.getpass("Enter the container name :")
        oimage = getpass.getpass("Enter the container image :")
        subprocess.getoutput("tput setaf 2")
        print("\t\t----------------------")
        subprocess.getoutput("tput setaf 7")
        cmd= "sudo docker run -dit --name {} {}".format(osname,oimage)
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status==0:
            print("\n")
            print("Docker OS launched..!!")
            print("Container  Name : {}".format(osname))
            print("Container  Image : {}".format(oimage))
            subprocess.getoutput("tput setaf 2")
            print("\t\t------------------------")
            subprocess.getoutput("tput setaf 7")
            s = subprocess.getoutput("sudo docker ps -a")
            print(s)

        else:
            print("error : {}".format(out))

    elif req == 2 :
        print("All Containers which are stopped and running currently : \n")
        subprocess.getoutput("sudo docker ps -a")
        subprocess.getoutput("tput setaf 3")
        print("\t\t\****************")
        subprocess.getoutput("tput setaf 7 ")
        print("\n")
        osname = getpass.getpass ("Enter the container name which you want to start : ")
        cmd="sudo docker start {}".format(osname)
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]
        if status==0:
            print ("Container {}  Started...!!".format(osname))
        else:
            print("error : {}".format(out))

    elif req == 3:
        print("Containers already running :\n")
        subprocess.getoutput("sudo docker ps")
        subprocess.getoutput("tput setaf 3")
        print("\t\t\t\t--------------------")
        subprocess.getoutput("tput setaf 7")
        print("\n")
        osname = getpass.getpass("Enter the container name which you want to stop :")
        cmd= "sudo docker stop {}".format(osname)
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status==0:
            print("Container {} Stopped..!!!".format(osname))
        else:
            print("error : {}".format(out))

    elif req ==4:
        print("Container Available:  \n")
        subprocess.getoutput("sudo docker ps -a")
        subprocess.getoutput("tput setaf 3")
        print("\t\t\t******************")
        subprocess.getoutput("tput setaf 7")
        print("\n")
        osname = getpass.getpass("Enter the container name which you want to delete :")
        cmd= "sudo docker container rm -f {}".format(osname)
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status==0:
            print("{} Container Removed..!!".format(osname))

        else:
            print("error : {}".format(out))

    elif req ==5:
        cmd= "sudo docker rm -f $(docker ps -aq)"
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status == 0:
            print("All Containers removed Successfully...!!")

        else:
            print("Error :{}".format(out))

    elif req == 6:
        cmd = "sudo docker ps"
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status == 0:
            print(out)

        else:
            print("error : {}".format(out))

    elif req == 7:
        cmd = "sudo docker ps -a"
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status ==0:
            print(out)

        else:
            print("Error :{}".format(out))

    elif req ==8:
        oimage = getpass.getpass("Enter the image name and it's version which you want to pull :")
        cmd = "docker pull {}".format(oimage)
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status ==0:
            print("Image Pulled Successfully..!!")
        else:
            print("error : {}".format(out))


    elif req == 9:
        cmd = "sudo docker images"
        output = subprocess.getstatusoutput(cmd)

        status=output[0]
        out = output[1]

        if status==0:
            print(out)

        else:
            print("error :{}".format(out))

    elif req ==10:
        print("\n\n\t\t please run minimum 1 container to create your docker image ")
        print()
        osname=getpass.getpass("Enter the Container name of which you want to create image:")
        iname = getpass.getpass("Enter the Image Name :")
        iversion= getpass.getpass("Enter the Image Version :")
        subprocess.getoutput("tput setaf 2")
        print("--------------------")
        subprocess.getoutput("tput setaf 7")
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

    elif req == 11:
        print("Images Available :\n")
        subprocess.getoutput("sudo docker images")
        subprocess.getoutput("tput setaf 3")
        print("\t\t\t***********************")
        subprocess.getoutput("tput setaf 7")
        print("\n")
        oimage=getpass.getpass("Enter the Image name and it's version which you want to delete :")
        cmd = "docker rmi -f {}".format(oimage)
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status ==0:
            print("Image deleted Successfully...!!")

        else:
            print("error :{}".format(out))
    

    
    elif req==13:
            exit()
    else :
            print("entered invalid option")
    




while True:
  subprocess.getoutput("clear")
  subprocess.getoutput("tput setaf 5")
  subprocess.getoutput("echo 'Welcome to Python Menu' | figlet -f cybermedium -d ./figletfonts40/ ")
  subprocess.getoutput("tput setaf 7")
  print("\n\n\n-----------------------------------------------------------------------------------------------------------------------------------------") 
  subprocess.getoutput("tput setaf 6")
  subprocess.getoutput("\n\n\n\t\t\t echo MAIN MENU | figlet -f wideterm -d ./figletfonts40/")
  subprocess.getoutput("tput setaf 3")

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



  subprocess.getoutput("tput setaf 7")


  if loc=="local":

      
    ch=getpass.getpass("Enter your choice : ")





    if int(ch)==1:
     while True: 

        subprocess.getoutput("clear")
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
        
        p = getpass.getpass("Enter your Choice :")

        if int(p) == 1 :
                print("\n\n\t")
                subprocess.getoutput("date")
        elif int(p) == 2 :
                print("\n\n\t")
                subprocess.getoutput("cal")
        elif int(p) == 3 :
                path=getpass.getpass("Enter the path of the folder you want to see the list :")
                list_dir=subprocess.getoutput("ls "+path)
                print("\n")
                print(list_dir)

        elif int(p) == 4 :
                print("\n\n\t")
                subprocess.getoutput("df -h")
        elif int(p) == 5 :
                print("\n\n\t")
                subprocess.getoutput("free -m")
        elif int(p) == 6 :
                print("\n\n\t")
                subprocess.getoutput("lscpu")
        elif int(p) == 7 :
                print("\n\n\t")
                subprocess.getoutput("whoami")
        elif int(p) == 8 :
                print("\n\n\t")
                subprocess.getoutput("echo 'echo' & ")
                subprocess.getoutput("jobs")
                print("\n\n\t\t only echo is running ")
        elif int(p) == 9 :
                print("\n\n\t")
                user = getpass.getpass("Enter user name :")
                s=subprocess.getstatusoutput("useradd "+user)
                status=s[0]
                output=s[1]
                if status==0 :
                    subprocess.getoutput("passwd {}".format(user))
                    print("Password Created Successfully!!!")
                else :
                    print("Error : {}".format(output))

        elif int(p)==10:
                cmd = getpass.getpass("Enter your command :")
                s=subprocess.getstatusoutput(cmd)
                status=s[0]
                output=s[1]
                print(output)
        

        elif int(p)==11:
            print("\n\n\t")
            subprocess.getoutput("df -h")
        
        elif int(p) == 12 :
                break
        elif int(p)==13:
            exit()
        else :
                print("entered invalid option")        
        getpass.getpass("\n\n\t\t press enter to keep using this sub-menu : ")   


    elif int(ch)==6:
     while True:
        subprocess.getoutput("clear")

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
        ch1 = getpass.getpass("Enter your choice :")
        subprocess.getoutput("tput setaf 2 ")
        print("\t\t\t\t\t********************")
        print("\n")
        subprocess.getoutput("tput setaf 7")
        if int(ch1)==12:
            break
        function(int(ch1))
        getpass.getpass("press enter to keep using this sub-menu : ")
    

    elif int(ch)==7:
        print("warning !!!! user should have sklearn and joblib pre-installed ,if it is not then use 'pip3 install sklearn' & 'pip3 install joblib'(as a pre-requisite) ")

        getpass.getpass("plz enter ur csv file name(with extension) as a dataset to use ml(linear regression) to create model and predict the things :               ")
        import joblib
        model=joblib.load("salary.pkl")
        exp=getpass.getpass("Enter ur experience(in years) to predict salary : ")
        predicted_value=model.predict([[int(exp)]])
        print("\n\n")
        print(predicted_value)
        subprocess.getoutput("tput setaf 2")
        print("\n\n\t\t this result is ur predicted salary ml linear regression model")
        subprocess.getoutput("tput setaf 7")


    elif int(ch)==8:
        subprocess.getoutput("init 0")

    elif int(ch)==9:
     import webbrowser   
     while True:
        subprocess.getoutput("clear")

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
        ch1 = getpass.getpass("Enter your choice :")
     
        if int(ch1)==1:
            print("\n\n\t")
            webbrowser.open("https://mail.google.com")
        if int(ch1)==2:
            print("\n\n\t")
            webbrowser.open("https://www.linkedin.com")
        if int(ch1)==3:
            print("\n\n\t")
            webbrowser.open("https://www.google.com")
        if int(ch1)==4:
            print("\n\n\t")
            webbrowser.open("https://drive.google.com")
        if int(ch1)==5:
            print("\n\n\t")
            webbrowser.open("https://www.github.com")
        if int(ch1)==6:
            print("\n\n\t")
            webbrowser.open("https://aws.amazon.com")
        if int(ch1)==7:
            print("\n\n\t")
            webbrowser.open("https://zoom.us")
        if int(ch1)==8:
            print("\n\n\t")
            webbrowser.open("https://www.hotstar.com")
        if int(ch1)==10:
            exit()
        if int(ch1)==9:
            break
        getpass.getpass("\n\n\t\tpress enter to keep using this sub-menu : ")

    elif int(ch)==2:
        while True:
         subprocess.getoutput("clear")
         subprocess.getoutput("tput setaf 1")
         print('\n\n  REMINDER !!! YOU SHOULD RUN "aws configure" CMD ONCE BEFORE USING THIS AUTOMATED MENU SO THAT AWS CAN AUTHENTICATE U ')
         subprocess.getoutput("tput setaf 7")
         subprocess.getoutput("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         subprocess.getoutput("tput setaf 4")
         name = "\"AWS TUI\""
         subprocess.getoutput("echo {0} | figlet -f smmono12 -d ./figletfonts40/".format(name))
         subprocess.getoutput("tput setaf 2")
         subprocess.getoutput("echo AWS TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
         subprocess.getoutput("tput setaf 2")
         print("\t\t\t\t\t\t\t\t...Do things of AWS with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         subprocess.getoutput("tput setaf 6")
         print("\t\t\t\t\tAWS Menu ")
         print("\t\t\t\t\t----")
         subprocess.getoutput("tput setaf 3")
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
         subprocess.getoutput("tput setaf 7")
         p=getpass.getpass("Enter your choice :")

         if int(p)==1:
          print("you should be ready with your credentials like access and secret key to use cli \n\n")   
          subprocess.getoutput("aws configure")
         
         elif int(p)==2:
          username=getpass.getpass("plz give ur new iam user name")   
          subprocess.getoutput("aws iam create-user --user-name {}".format(username))
          subprocess.getoutput("tput setaf 2")
          print("\n\n new iam user has been created successfully")
          subprocess.getoutput("tput setaf 7")
         
         elif int(p)==3:
          subprocess.getoutput("aws iam attach-user-policy --user-name {} --policy-arn arn:aws:iam::aws:policy/PowerUserAccess ".format(username))
          subprocess.getoutput("tput setaf 2")
          print("\n\n user policy has been attached successfully")
          subprocess.getoutput("tput setaf 7")
         
         elif int(p)==4:
          subprocess.getoutput("tput setaf 6 ")
          print('\n\n ATTENTION REQUIRED!!! YOU SHOULD KEEP THESE CREDENTIALS SAFE AND COPIED IN 1 FILE ,FOR UR CONVINIENCE THE OUTPUT IS BY DEFAULT SAVED IN "IAM_CRED_<iam username here(vary as per your choice)>.txt" ')
          subprocess.getoutput("tput setaf 7 ")
          username=getpass.getpass("plz give ur desired username to generate credentials : ")
          subprocess.getoutput("aws iam create-access-key --user-name {0} > IAM_CRED_{0}.pem".format(username))   
          subprocess.getoutput("tput setaf 2")
          print("\n\n new access key for this user {} has been generated successfully".format(username))
          subprocess.getoutput("tput setaf 7")
         
         elif int(p)== 5:
          keypairname=getpass.getpass("plz enter ur key pair name : ")
          subprocess.getoutput("aws ec2 create-key-pair --key-name {0} > {0}.pem".format(keypairname))
          #x=json.loads(x)
          #keypair=x['KeyMaterial']
          #subprocess.getoutput("echo $keypair | {}.pem".format(keypairname))
          subprocess.getoutput("tput setaf 2")
          print("\n\n new key pair created successfully")
          subprocess.getoutput("tput setaf 7")





         elif int(p)== 6:
             
          sg=getpass.getpass("plz enter your desired name to new security group : ")
          subprocess.getoutput('aws ec2 create-security-group --description "allow all" --group-name {} --tag-specifications ResourceType="security-group",Tags=["{{Key=Name,Value=menu-sg}}"]'.format(sg))
          subprocess.getoutput("tput setaf 2")
          print(" \n\n new security group created successfully") 
          subprocess.getoutput("tput setaf 7")


         elif int(p)== 7:
          x=subprocess.getoutput("aws ec2 describe-security-groups --filters Name=tag-key,Values=Name Name=tag-value,Values=menu-sg")
          x=json.loads(x)
          gid=x["SecurityGroups"][0]["GroupId"]
          port=getpass.getpass("\n\n enter the port on which u want to allow the outside world to ur os : ")
          subprocess.getoutput("aws ec2 authorize-security-group-ingress --group-id {} --protocol all --port {} --cidr 0.0.0.0/0 ".format(gid,port))
          subprocess.getoutput("tput setaf 2")
          print("\n\n security group ingress rule has been added successfully")
          subprocess.getoutput("tput setaf 7")


      

         elif int (p)==8:
          y=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-value,Values=slave1")
          y=json.loads(y)
          localostag=y['Reservations'][0]['Instances'][0]['Tags'][0]['Value']   
          x=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-key,Values=Name Name=tag-value,Values={}".format(localostag))
          x=json.loads(x)
          osid=x["Reservations"][0]["Instances"][0]["InstanceId"]   
          subprocess.getoutput("aws ec2 modify-instance-attribute --instance-id {}  --groups {}".format(osid,gid))
          subprocess.getoutput("tput setaf 2")
          print("\n\n new security has been attached to your running local os successfully")
          subprocess.getoutput("tput setaf 7")
             
         elif int(p)== 9:
          x=subprocess.getoutput("aws ec2 describe-security-groups --filters Name=tag-key,Values=Name Name=tag-value,Values=menu-sg")
          x=json.loads(x)
          gid=x["SecurityGroups"][0]["GroupId"]
          cnt=int(getpass.getpass("plz give getpass.getpass how many instances u want to launch : "))
          itag=getpass.getpass("plz give your new os a tag : ")
          subprocess.getoutput("aws ec2 run-instances --security-group-ids {} --instance-type t2.micro --count {} --image-id ami-0e306788ff2473ccb --key-name {} --tag-specifications ResourceType=instance,Tags=['{{Key=Name,Value={} }}'] ".format(gid,cnt,keypairname,itag))
          subprocess.getoutput("tput setaf 2")
          print("\n\n yay,ur new full flash aws instance is launched and ready to use")
          subprocess.getoutput("tput setaf 7")
      

         elif int(p)==10:
          volume("{}".format(itag))





         elif int(p)==11:
          subprocess.getoutput("tput setaf 6")
          itag="slave1"   
          volume("{}".format(itag))
          subprocess.getoutput("tput setaf 7")
         

         elif int(p)==12:
             hd1=subprocess.getoutput("aws ec2 describe-volumes --filters Name=tag-value,Values={}".format(ebsdb[0]))
             hd1=json.loads(hd1)
             hd1=hd1["Volumes"][0]["Attachments"][0]["Device"]
             subprocess.getoutput("fdisk {}".format(hd1))
             print("\n\n successfully created partition")
             getpass.getpass("\n\n press Enter to format this partition : ")
             subprocess.getoutput("mkfs.ext4 {}1".format(hd1))
             print("\n\n successfully formatted partition")
             getpass.getpass("\n\n press Enter to mount this partition : ")
             folder=getpass.getpass("plz give ur folder name/path where u want to mount : ")
             subprocess.getoutput("mkdir /{}".format(folder))
             subprocess.getoutput("mount {}1 /{}".format(hd1,folder))
             subprocess.getoutput("tput setaf 2")
             print("\n\n partition mounted successfully and now u can store data in {} directory and all data will be persistent even if ur subprocess.getoutput/root hard disk get corrupt ".format(folder))
             subprocess.getoutput("tput setaf 7")
             subprocess.getoutput("df -h")
             print("here 'type' term means do you want to type : ")
             getpass.getpass1=getpass.getpass("what u have to put in  : file/type ")
             
             if getpass.getpass1=="file":
              source=getpass.getpass("plz give ur file name/path to copy in ur directory {}".format(folder))   
              subprocess.getoutput("cp {} {}".format(source,folder))   
              print("\n\n\t\t file copied successfully")

             else:
              print('here press Enter to go to next line and ctrl+d to stop writing and save code in "arth.txt"  ')
              subprocess.getoutput("cat > /{}/arth.txt".format(folder))
              print("\n\n\t\t ur code saved succesfully")
              
             
                 
         elif int(p)==13:
          hd1=subprocess.getoutput("aws ec2 describe-volumes --filters Name=tag-value,Values={}".format(ebsdb[0]))
          hd1=json.loads(hd1)
          hd1=hd1["Volumes"][0]["Attachments"][0]["Device"]
          x=subprocess.getoutput("umount {}1".format(hd1))
          subprocess.getoutput("e2fsck -f  {}1".format(hd1)) 
          subprocess.getoutput("fdisk {}".format(hd1))
          print('give more size(in GIB) to extend partition and give no when it gives an option like "do u want to remove ur signature" so that we dont lose previous data ')
          print("\n\n press enter to check ur partition consistency like inode tables,references or some internal metadata is stable or giving some error")
          subprocess.getoutput("resize2fs {}1".format(hd1))
          folder=getpass.getpass("plz give ur folder name/path where u want to mount : ")
          subprocess.getoutput("mkdir /{}".format(folder))
          subprocess.getoutput("mount {}1 /{}".format(hd1,folder))
          subprocess.getoutput("cd /{};cat arth.txt".format(folder))
          print("see here,ur data is there and it has not been lost ")
          subprocess.getoutput("df -h")
          subprocess.getoutput("tput setaf 2")
          print("\n\n ur static partition size is also extended now with the same data ,see above")
          subprocess.getoutput("tput setaf 7")
         
         
         elif int(p)==14:
          bucket=getpass.getpass("plz enter a new bucket name")
          subprocess.getoutput("aws s3 mb s3://{} --region ap-south-1".format(bucket))
          subprocess.getoutput("tput setaf 2")
          print("\n\n s3 bucket created successfully ")
          subprocess.getoutput("tput setaf 7")

         elif int(p)==15:
          print("for ur convenience, i am listing all the files so that u can filter what to upload in bucket ")
          subprocess.getoutput("ls")
          img=getpass.getpass("plz enter ur object name to upload to s3 bucket")   
          subprocess.getoutput("aws s3 cp {} s3://{} --acl public-read ".format(img,bucket))
          subprocess.getoutput("tput setaf 2")
          print("\n\n succcesfully uploaded ur object to s3 bucket")
          subprocess.getoutput("tput setaf 7")
         
         elif int(p)==16:
          x=subprocess.getoutput("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com".format(bucket))
          x=json.loads(x)
          x=x['Distribution']['DomainName']
          cloudfront_url="https://{}/{}".format(x,img)
          subprocess.getoutput("tput setaf 2")
          print("\n\n ur cloudfront distribution has been created successfully")
          print("\n\n ur cloudfront url is : {}".format(cloudfront_url))
          print("\n\n plz copy this url as u can use this url in ur web server to display this object by giving this url in webpages for faster content delivery and very less latency all across the world")
          subprocess.getoutput("tput setaf 7")
          
         elif int(p) == 17 :
                break
         elif int(p)==18 :
            exit()
         else :
                print("entered invalid option")
         getpass.getpass("press enter to keep using this sub-menu : ")


    elif int(ch)==3:
        while True:
         subprocess.getoutput("clear")   
         subprocess.getoutput("tput setaf 3")
         print("\n\n REMINDER !!! ,IF U WANT TO EXTEND VG THEN FIRST ATTACH NEW EBS VOLUME ,FOR THAT GO TO OPTION 3 IF U HAVEN'T DONE YET")   
         subprocess.getoutput("tput setaf 7")
         subprocess.getoutput("tput setaf 2")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         subprocess.getoutput("tput setaf 4")
         name = "\"LVM  TUI\""
         subprocess.getoutput("echo {0} | figlet -f smmono12 -d ./figletfonts40/ ".format(name))
         subprocess.getoutput("tput setaf 3")
         subprocess.getoutput("echo   LVM  TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
         subprocess.getoutput("tput setaf 5")
         print("\t\t\t\t\t\t\t\t...Do things of LVM with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         subprocess.getoutput(" tput setaf 2")
         print("...LVM Main Menu...")
         subprocess.getoutput(" tput setaf 3 ")
         print("""
\n\n
press 6 : to create LVM partition
press 7 : to extend lv size
press 8 : to reduce lv size
press 9 : to extend VG size
press 10 : to go to the base menu
press 11 : to exit
""")     
         subprocess.getoutput(" tput setaf 7")
         p=getpass.getpass("plz enter ur choice : ")


         if int(p) == 6:
          subprocess.getoutput("tput setaf 2")   
          hd1=subprocess.getoutput("aws ec2 describe-volumes --filters Name=tag-value,Values={}".format(ebsdb[0]))
          hd2=subprocess.getoutput("aws ec2 describe-volumes --filters Name=tag-value,Values={}".format(ebsdb[1]))
          hd1=json.loads(hd1)
          hd2=json.loads(hd2)
          hd1=hd1["Volumes"][0]["Attachments"][0]["Device"]
          hd2=hd2["Volumes"][0]["Attachments"][0]["Device"]
          subprocess.getoutput("tput setaf 5")
          subprocess.getoutput("pvcreate {}".format(hd1))
          subprocess.getoutput("pvdisplay {}".format(hd1))
          subprocess.getoutput("tput setaf 6")
          subprocess.getoutput("pvcreate {}".format(hd2))
          subprocess.getoutput("pvdisplay {}".format(hd2))
          subprocess.getoutput("tput setaf 3")
          vg=getpass.getpass("enter your vg name : ")
          subprocess.getoutput("tput setaf 4")
          subprocess.getoutput("vgcreate {} {} {}".format(vg,hd1,hd2))
          subprocess.getoutput("vgdisplay {}".format(vg))
          subprocess.getoutput("tput setaf 3")
          lvname=getpass.getpass("enter your lv name : ")
          lvsize=getpass.getpass("enter your lv size : ")
          subprocess.getoutput("tput setaf 3")
          subprocess.getoutput("lvcreate --size {}GB --name {} {}".format(lvsize,lvname,vg))
          subprocess.getoutput("tput setaf 2")
          print("successfully created logical volume")
          subprocess.getoutput("tput setaf 7")
          subprocess.getoutput("tput setaf 4")
          subprocess.getoutput("lvdisplay /dev/{}/{}".format(vg,lvname))
          subprocess.getoutput("tput setaf 3")
          getpass.getpass("press enter to format your lv {}  : ".format(lvname))
          subprocess.getoutput("mkfs.ext4 /dev/{}/{}".format(vg,lvname))
          subprocess.getoutput("tput setaf 3")
          print("your lv {} succesfully formatted".format(lvname))
          subprocess.getoutput("tput setaf 4")
          dir=getpass.getpass("enter new folder to create where this lv will be mounted : ")
          subprocess.getoutput("mkdir /{}".format(dir))
          subprocess.getoutput("mount /dev/{}/{} /{}".format(vg,lvname,dir))
          subprocess.getoutput("tput setaf 6")
          print("successfully mounted your lv {} to folder {}".format(lvname,dir))
          subprocess.getoutput("tput setaf 2")
          print("\n\n do you want to extend this lv size ,go for option 7")
          subprocess.getoutput("tput setaf 7")




         elif int(p) == 7:
          subprocess.getoutput("tput setaf 3")
          extended_size=getpass.getpass("plz enter how much size(in GB) U want to extend to ur lv : ")
          subprocess.getoutput("tput setaf 6")
          subprocess.getoutput("lvextend --size +{}GB /dev/{}/{}".format(extended_size,vg,lvname)) 
          subprocess.getoutput("resize2fs /dev/{}/{}".format(vg,lvname))
          subprocess.getoutput("tput setaf 2")
          print("\n\n successfully extended your lv")
          subprocess.getoutput("tput setaf 7")

     
         elif int(p) == 8:
          subprocess.getoutput("tput setaf 5")
          reduced_size=getpass.getpass("plz enter how much size(in GB) U want to reduce to ur lv : ")
          subprocess.getoutput("tput setaf 3")
          subprocess.getoutput("lvreduce --size -{}GB /dev/{}/{}".format(extended_size,vg,lvname))
          subprocess.getoutput("resize2fs /dev/{}/{}".format(vg,lvname))
          subprocess.getoutput("tput setaf 2")
          print("\n\n successfully reduced your lv")
          subprocess.getoutput("tput setaf 7")


         elif int(p) == 9:
          subprocess.getoutput("tput setaf 1")   
          print("REMINDER !!! ,IF U WANT TO EXTEND VG THEN FIRST ATTACH NEW EBS VOLUME ,FOR THAT GO TO OPTION 3 IF U HAVEN'T DONE YET")
          
          hd3=subprocess.getoutput("aws ec2 describe-volumes --filters Name=tag-value,Values={}".format(ebsdb[2]))
          hd3=json.loads(hd3)
          devname=hd3["Volumes"][0]["Attachments"][0]["Device"]
          vg=getpass.getpass("enter your old vg name : ")
          subprocess.getoutput("tput setaf 6")
          subprocess.getoutput("pvcreate {}".format(devname))
          subprocess.getoutput("pvdisplay {}".format(devname))
          subprocess.getoutput("vgextend {} {}".format(vg,devname))
          subprocess.getoutput("vgdisplay {}".format(vg))
          subprocess.getoutput("tput setaf 5")
          sizelv=getpass.getpass("plz enter ur size to extend in lv : ")
          subprocess.getoutput("lvextend --size +{}GB /dev/{}/{}".format(sizelv,vg,lvname))
          subprocess.getoutput("resize2fs /dev/{}/{}".format(vg,lvname))
          subprocess.getoutput("tput setaf 2")
          print("\n\n successsfully extended your vg and lv through new ebs volume")
          subprocess.getoutput("tput setaf 7")
         

         elif int(p) == 10 :
                break
         elif int(p)==11:
            exit()
         else : 
                subprocess.getoutput("tput setaf 1")
                print("entered invalid option")
         subprocess.getoutput("tput setaf 4")       
         getpass.getpass("press enter to keep using this sub-menu : ")
         subprocess.getoutput("tput setaf 7")

    elif int(ch)==4:
        while True:
         subprocess.getoutput("clear")
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
         p=getpass.getpass("plz enter ur choice : ")

         if int(p)==12:
          subprocess.getoutput("rpm -ivh jdk-8u171-linux-x64.rpm ")
          subprocess.getoutput("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force ")
          randomnumber=random.randint(1,100)
          subprocess.getoutput("mkdir /dn{}".format(randomnumber))
          pubip=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-value,Values=master")
          pubip=json.loads(pubip)
          pubip=pubip['Reservations'][0]['Instances'][0]['PublicIpAddress']
          subprocess.getoutput("sed -i 's/dn/dn{}/g' hdfs-site.xml".format(randomnumber))
          subprocess.getoutput("sed -i 's/masterip/{}/g' core-site.xml".format(pubip))
          subprocess.getoutput("cp hdfs-site.xml /etc/hadoop/hdfs-site.xml  ")
          subprocess.getoutput("cp core-site.xml /etc/hadoop/core-site.xml  ")
          subprocess.getoutput("hadoop-daemon.sh start datanode")
          subprocess.getoutput("jps")
          subprocess.getoutput("tput setaf 2")
          print("\n\n\t\t succesfully configured slave node")
          subprocess.getoutput("tput setaf 7")
          getpass.getpass("press enter to see how many slaves are connected to master")
          subprocess.getoutput("hadoop dfsadmin -report")
          subprocess.getoutput("sed -i 's/dn{}/dn/g' hdfs-site.xml".format(randomnumber))
          subprocess.getoutput("sed -i 's/{}/masterip/g' core-site.xml".format(pubip))   
             
     
    




         elif int(p)==11:   
          subprocess.getoutput("rpm -ivh jdk-8u171-linux-x64.rpm ")
          subprocess.getoutput("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force ")
          randomnumber=random.randint(1,100)
          subprocess.getoutput("mkdir /nn{}".format(randomnumber))
          subprocess.getoutput("sed -i 's/masterip/0.0.0.0/g' core-site-master.xml")
          subprocess.getoutput("sed -i 's/data/name/g' hdfs-site-master.xml")
          subprocess.getoutput("sed -i 's/dn/nn{}/g' hdfs-site-master.xml".format(randomnumber))
          subprocess.getoutput("cp hdfs-site-master.xml /etc/hadoop/hdfs-site.xml")
          subprocess.getoutput("cp core-site-master.xml /etc/hadoop/core-site.xml")
          subprocess.getoutput("hadoop namenode -format")
          subprocess.getoutput("hadoop-daemon.sh start namenode")
          subprocess.getoutput("jps")
          subprocess.getoutput("tput setaf 2")
          print("\n\n\t\t succesfully configured master node")
          subprocess.getoutput("tput setaf 7")
          getpass.getpass("press enter to see how many slaves are connected to master")
          subprocess.getoutput("hadoop dfsadmin -report")
          subprocess.getoutput("sed -i 's/0.0.0.0/masterip/g' core-site-master.xml")
          subprocess.getoutput("sed -i 's/name/data/2' hdfs-site-master.xml")
          subprocess.getoutput("sed -i 's/nn{}/dn/g' hdfs-site-master.xml".format(randomnumber))

      

         elif int(p)==13:
          pubip=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-value,Values=master")
          pubip=json.loads(pubip)
          pubip=pubip['Reservations'][0]['Instances'][0]['PublicIpAddress']
          
          subprocess.getoutput("rpm -ivh jdk-8u171-linux-x64.rpm ")
          subprocess.getoutput("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force ")
          subprocess.getoutput("sed -i 's/masterip/{}/g' core-site-client.xml".format(pubip))
          subprocess.getoutput("cp core-site-client.xml /etc/hadoop/core-site.xml")
          subprocess.getoutput("tput setaf 2")
          print("\n\n\t\t succesfully configured client node")
          subprocess.getoutput("tput setaf 7")




                  
         elif int(p)==9:
          subprocess.getoutput("tput setaf 1")
          print("it seems you have exited,see u again")
          subprocess.getoutput("tput setaf 7")
          exit()


      

         elif int(p)==15:
          print("here 'type' term means do you want to type : ")
          getpass.getpass1=getpass.getpass("what u have to put in web server : file/type ")
          if getpass.getpass1=="file":
              file=getpass.getpass("plz enter your file name/path to upload from client : ")
              subprocess.getoutput("hadoop fs -put {} /".format(file))
              print("file uploaded successfully")
          
          else:
              print('press "Enter" to go to next line and "ctrl+d" to stop writing and save ur code')
              subprocess.getoutput("cat > web.html")
              subprocess.getoutput("hadoop fs -put {} /".format(web.html))
              print("file uploaded successfully")
         elif int(p)==16:
          file=getpass.getpass("plz enter your file name/path to upload from client : ")
          subprocess.getoutput("hadoop fs -cat /{}".format(file))
      
         elif int(p)==14:
          subprocess.getoutput("hadoop dfsadmin -safemode get")
          subprocess.getoutput("hadoop dfsadmin -safemode leave")
          print("successfully left safe mode")
      

         elif int(p)==17:
          subprocess.getoutput("tcpdump -i eth0 -n tcp port not 22 > pkt.txt")
          print("press ctrl+c to stop this cmd")
      
         elif int(p)==18:
          subprocess.getoutput("vim pkt.txt")
         
         elif int(p) == 19 :
          break
         elif int(p)==20:
          exit()
         else :
          print("entered invalid option")
         getpass.getpass("press enter to keep using this sub-menu : ")

    elif int(ch)==5:
          pubip=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-value,Values=slave1")
          pubip=json.loads(pubip)
          pubip=pubip['Reservations'][0]['Instances'][0]['PublicIpAddress']
          print("here 'type' term means do you want to type : ")
          getpass.getpass1=getpass.getpass("what u have to put in web server : file/type :  ")
          if getpass.getpass1=="file":
              print("wait till the time respective software is downloading ")
              subprocess.getoutput("yum install httpd -y")
              getpass.getpass1=getpass.getpass("plz getpass.getpass ur file/path to show as web pages in web server : ")
              subprocess.getoutput("chmod 777 /var/www/html/")
              subprocess.getoutput("cp {} /var/www/html/".format(getpass.getpass1))
              subprocess.getoutput("systemctl start httpd")
              subprocess.getoutput("systemctl enable httpd")
              print("ur web server configured successfully")
              getpass.getpass("press enter to connect to ur new webserver while it is working or not : ")
              subprocess.getoutput("curl http://{}:/{}".format(pubip,getpass.getpass1))
          else:
              subprocess.getoutput("cat > web1.html")
              subprocess.getoutput("yum install httpd -y")
              subprocess.getoutput("chmod 777 /var/www/html/")
              subprocess.getoutput("cp web1.html /var/www/html/")
              subprocess.getoutput("systemctl start httpd")
              print("ur web server configured successfully")
              getpass.getpass("press enter to connect to ur new webserver while it is working or not : ")
              subprocess.getoutput("curl http://{}:/{}".format(pubip,getpass.getpass1))

          getpass.getpass("press enter to go to the base menu : ")
          break   



    elif int(ch)==10:
        pubip=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-value,Values=slave2")
        pubip=json.loads(pubip)
        pubip=pubip['Reservations'][0]['Instances'][0]['PublicIpAddress']
        subprocess.getoutput("tput setaf 1")
        print("it seems you have exited,hope to see u again ")
        subprocess.getoutput("tput setaf 3")
        print("\n\n\t\tREQUEST!!!!! U ARE OUR VALUABLE AND FOREMOST/PRIORITY CUSTOMER/USER ,YOUR FEEDBACK MATTERS FOR US ,PLZ GIVE UR SOME TIME TO GIVE FEEDBACK TO THIS MENU AS UR FEEDBACK WILL KEEP ON MAKING THIS MENU MORE AND MORE USER FRIENDLY : \n\t ")
        subprocess.getoutput("tput setaf 7")
        random1=random.randint(1,100)
        subprocess.getoutput("cat > feedback{}.txt".format(random1))
        print("\n\n\t")
        subprocess.getoutput("scp -i slave1.pem feedback{}.txt ec2-user@{}:/home/ec2-user".format(random1,pubip))
        print("\n\n\t\t your valuable feedback has been reached to us via network,thanks,\n we hope u will come again soon to give us one more chance to serve you more comparatively better")
        exit()

    
    else:
        subprocess.getoutput("tput setaf 1")
        print("\n\n you have entered an invalid option !!! ,don't worry try menu option correctly again, it is so easy to use ")
        subprocess.getoutput("tput setaf 7")



    subprocess.getoutput("tput setaf 6")
    getpass.getpass("\n\n press Enter to continue using BASE menu : ")
    subprocess.getoutput("tput setaf 7")
  



  if loc=="remote":
    pubip=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-value,Values=master")
    pubip=json.loads(pubip)
    pubip=pubip['Reservations'][0]['Instances'][0]['PublicIpAddress']  


    ch=getpass.getpass("Enter your choice : ")





    if int(ch)==1:
     while True:

        subprocess.getoutput("clear")
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

        p = getpass.getpass("Enter your Choice :")

        if int(p) == 1 :
            subprocess.getoutput("ssh -i slave1.pem ec2-user@{} date".format(pubip))
        elif int(p) == 2 :
                subprocess.getoutput("ssh -i slave1.pem ec2-user@{} cal".format(pubip))
        elif int(p) == 3 :
                path=getpass.getpass("Enter the path of the folder you want to see the list :")
                list_dir=subprocess.getoutput("ssh -i slave1.pem ec2-user@{} ls {}".format(pubip,path))
                print("\n")
                print(list_dir)

        elif int(p) == 4 :
                subprocess.getoutput("ssh -i slave1.pem ec2-user@{} df -h".format(pubip))
        elif int(p) == 5 :
                subprocess.getoutput("ssh -i slave1.pem ec2-user@{} free -m".format(pubip))
        elif int(p) == 6 :
                subprocess.getoutput("ssh -i slave1.pem ec2-user@{} lscpu".format(pubip))
        elif int(p) == 7 :
                subprocess.getoutput("ssh -i slave1.pem ec2-user@{} whoami".format(pubip))
        elif int(p) == 8 :
                subprocess.getoutput("ssh -i slave1.pem ec2-user@{} echo 'echo' &".format(pubip))
                subprocess.getoutput("ssh -i slave1.pem ec2-user@{} jobs".format(pubip))
                print("\n\n\t\t only echo is running ")

        elif int(p) == 9 :
                user = getpass.getpass("Enter user name :")
                s=subprocess.getstatusoutput("ssh -i slave1.pem ec2-user@{} useradd {}".format(pubip,user))
                status=s[0]
                output=s[1]
                if status==0 :
                    subprocess.getoutput("ssh -i slave1.pem ec2-user@{} passwd {}".format(pubip,user))
                    print("Password Created Successfully!!!")
                else :
                    print("Error : {}".format(output))

        elif int(p)==10:
                cmd = getpass.getpass("Enter your command :")
                s=subprocess.getstatusoutput("ssh -i slave1.pem ec2-user@{} {}".format(pubip,cmd))
                status=s[0]
                output=s[1]
                print(output)


        elif int(p)==11:
            subprocess.getoutput("ssh -i slave1.pem ec2-user@{} df -h".format(pubip))

        elif int(p) == 12 :
                break
        elif int(p)==13:
            exit()
    
    elif int(ch)==5:
        while True:  
          print("here 'type' term means do you want to type : ")
          getpass.getpass1=getpass.getpass("what u have to put in web server : file/type ")
          if getpass.getpass1=="file":
              print("wait till the time respective software is downloading ")
              subprocess.getoutput("ssh -i slave1.pem ec2-user@{} sudo yum install httpd -y".format(pubip))
              print("\n\n\t\t ur software is downloaded successfully : ")
              getpass.getpass1=getpass.getpass("\n\t\tplz getpass.getpass ur file/path to show as web pages in web server : ")
              subprocess.getoutput("ssh -i slave1.pem ec2-user@{} sudo chmod 777 /var/www/html".format(pubip))
              subprocess.getoutput("scp -i slave1.pem {} ec2-user@{}:/var/www/html/".format(getpass.getpass1,pubip))
              subprocess.getoutput("ssh -i slave1.pem ec2-user@{} sudo systemctl start httpd".format(pubip))
              subprocess.getoutput("ssh -i slave1.pem ec2-user@{} sudo systemctl enable httpd".format(pubip))
              print("ur web server configured successfully")
              getpass.getpass("press enter to connect to ur new webserver while it is working or not : ")
              subprocess.getoutput("curl http://{}:/{}".format(pubip,getpass.getpass1))
              print("this is ur code ,see above")

          else:
              subprocess.getoutput("cat > web1.html")
              print("wait till the time respective software is downloading ")
              subprocess.getoutput("ssh -i slave1.pem ec2-user@{} sudo yum install httpd -y".format(pubip))
              print("\n\n\t\t ur software is downloaded successfully : ")
              subprocess.getoutput("ssh -i slave1.pem ec2-user@{} sudo chmod 777 /var/www/html".format(pubip))
              subprocess.getoutput("scp -i slave1.pem web1.html ec2-user@{}:/var/www/html/".format(pubip))
              subprocess.getoutput("ssh -i slave1.pem ec2-user@{} sudo systemctl start httpd".format(pubip))
              subprocess.getoutput("ssh -i slave1.pem ec2-user@{} sudo systemctl enable httpd".format(pubip))
              print("ur web server configured successfully")
              getpass.getpass("press enter to connect to ur new webserver while it is working or not : ")
              subprocess.getoutput("curl http://{}:/{}".format(pubip,getpass.getpass1))
              print("this is ur code ,see above")

          getpass.getpass("press enter to go to the base menu : ")
          break

    elif int(ch)==4:
        while True:
         subprocess.getoutput("clear")
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
         p=getpass.getpass("plz enter ur choice : ")
         if int(p)==11:
          subprocess.getoutput("scp -i slave1.pem jdk-8u171-linux-x64.rpm ec2-user@{}:/home/ec2-user/".format(pubip))
          subprocess.getoutput("scp -i slave1.pem hadoop-1.2.1-1.x86_64.rpm ec2-user@{}:/home/ec2-user/".format(pubip))   
          subprocess.getoutput("ssh -i slave1.pem ec2-user@{} sudo rpm -ivh /home/ec2-user/jdk-8u171-linux-x64.rpm".format(pubip))
          subprocess.getoutput("ssh -i slave1.pem ec2-user@{} sudo rpm -ivh /home/ec2-user/hadoop-1.2.1-1.x86_64.rpm --force ".format(pubip))
          subprocess.getoutput("ssh -i slave1.pem ec2-user@{} sudo mkdir /nn".format(pubip))
          subprocess.getoutput("sed -i 's/masterip/0.0.0.0/g' /home/ec2-user/core-site-master-remote.xml")
          subprocess.getoutput("sed -i 's/data/name/g' /home/ec2-user/hdfs-site-master-remote.xml")
          subprocess.getoutput("sed -i 's/dn/nn/g' /home/ec2-user/hdfs-site-master-remote.xml")
          subprocess.getoutput("ssh -i slave1.pem ec2-user@{} sudo chmod -R 777 /etc/hadoop/".format(pubip))
          subprocess.getoutput("scp -i slave1.pem hdfs-site-master-remote.xml ec2-user@{}:/etc/hadoop/hdfs-site.xml".format(pubip))
          subprocess.getoutput("scp -i slave1.pem core-site-master-remote.xml ec2-user@{}:/etc/hadoop/core-site.xml".format(pubip))
          subprocess.getoutput("ssh -i slave1.pem ec2-user@{} sudo hadoop namenode -format".format(pubip))
          subprocess.getoutput("ssh -i slave1.pem ec2-user@{} sudo hadoop-daemon.sh start namenode".format(pubip))
          subprocess.getoutput("ssh -i slave1.pem ec2-user@{} sudo jps".format(pubip))
          subprocess.getoutput("tput setaf 2")
          print("\n\n\t\t succesfully configured master node")
          subprocess.getoutput("tput setaf 7")
          getpass.getpass("press enter to see how many slaves are connected to master")
          subprocess.getoutput("ssh -i slave1.pem ec2-user@{} sudo hadoop dfsadmin -report".format(pubip))
          subprocess.getoutput("sed -i 's/0.0.0.0/masterip/g' /home/ec2-user/core-site-master-remote.xml")
          subprocess.getoutput("sed -i 's/name/data/2' /home/ec2-user/hdfs-site-master-remote.xml")
          subprocess.getoutput("sed -i 's/nn/dn/g' /home/ec2-user/hdfs-site-master-remote.xml")
         
         elif int(p)==19:
             break
         
         elif int(p)==20:
             exit()
         getpass.getpass("\n\n\t\tpress Enter to keep using sub-menu : ")    


    subprocess.getoutput("tput setaf 6")
    getpass.getpass("\n\n press Enter to continue using BASE menu : ")
    subprocess.getoutput("tput setaf 7")
