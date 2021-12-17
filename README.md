# Website Blocker

This is a simple python script that organizations can use in their office computers to block certain websites, for example, www.bing.com or www.facebook.com, during their working hours.

first, you need to make some administration changes in the host file, which is located 

for windows

<img width="598" alt="image" src="https://user-images.githubusercontent.com/95688723/146385521-d40f1828-c67b-4bc6-9aa2-90d84b85125b.png">

C:\Windows\System32\drivers\etc\hosts

right-click on the host file and click properties

<img width="268" alt="image" src="https://user-images.githubusercontent.com/95688723/146385605-37f891f5-0c2e-4d52-9da3-cb4a574394cf.png">

after that, click on the safety 

<img width="266" alt="image" src="https://user-images.githubusercontent.com/95688723/146385682-f66a16e6-0ead-44e2-8431-d9d371e5d4c8.png">

then in the groups or usernames box, select all applications packages 

<img width="266" alt="image" src="https://user-images.githubusercontent.com/95688723/146385875-9a0ee9e7-e0d8-4864-a337-16595598ca26.png">



, click on edit, then in the permission for users box, 



click on write permission


now you need to schedule this script 

Scheduling in Windows: Scheduling of above script is little bit trick but I will guide you step by step-

1.First of all change the extension of your script from “.py” to “.pyw”.
2.Now open task scheduler. Task scheduler should look like this:

![image](https://user-images.githubusercontent.com/95688723/146499388-d583dc13-2635-487a-9e00-926814d92d61.png)


You may see website blocker already scheduled because I have already scheduled in my computer for my testing purpose. Follow further instruction of scheduling carefully in order to schedule website blocker in your computer.

3.Click on “create task”. Fill the name of your choice and flag “Run with highest privilege”.

![image](https://user-images.githubusercontent.com/95688723/146499466-c8a63918-2c90-408b-ab1e-e43db2516798.png)

![image](https://user-images.githubusercontent.com/95688723/146499514-f60c0c34-6274-42a1-8fb6-a4ec459021cf.png)

Now go to triggers, select “At startup” for begin the task.

Go to Action bar and create a new action and give path of your script.



Go to conditions bar and unflag the power section.



Press ok and you can see the script scheduled.

Finally restart your computer and see the magic.

Note: You can also check instantly by clicking run button.







