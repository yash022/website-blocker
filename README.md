# Website Blocker

This is a simple python script that organizations can use in their office computers to block certain websites, for example, www.bing.com or www.facebook.com, during their working hours.

to change the webiste you need to block , open the py file in any code editor , replace the webiste in this line 

<img width="812" alt="image" src="https://user-images.githubusercontent.com/95688723/146500465-4668bf61-af1d-446c-b19c-504df23ee171.png">

and save it as pyw file .

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

, click on edit, then in the permission for users box,  click on write permission

<img width="264" alt="image" src="https://user-images.githubusercontent.com/95688723/146499962-240fe3d1-42da-408f-a168-22333978497e.png">

now click on ok

now you need to schedule this script 

Scheduling in Windows: Scheduling of above script is little bit trick but I will guide you step by step-

1.First of all change the extension of your script from “.py” to “.pyw”.
2.Now open task scheduler. Task scheduler should look like this:

![image](https://user-images.githubusercontent.com/95688723/146499388-d583dc13-2635-487a-9e00-926814d92d61.png)


You may see website blocker already scheduled because I have already scheduled in my computer for my testing purpose. Follow further instruction of scheduling carefully in order to schedule website blocker in your computer.

3.Click on “create task”. Fill the name of your choice and flag “Run with highest privilege”.

![image](https://user-images.githubusercontent.com/95688723/146499466-c8a63918-2c90-408b-ab1e-e43db2516798.png)

![image](https://user-images.githubusercontent.com/95688723/146499514-f60c0c34-6274-42a1-8fb6-a4ec459021cf.png)

4. Now go to triggers, select “At startup” for begin the task.

![image](https://user-images.githubusercontent.com/95688723/146499683-52a8b59d-7aa8-4a40-91e6-7cd285ee2c67.png)


5.Go to Action bar and create a new action and give path of your script.

![image](https://user-images.githubusercontent.com/95688723/146499704-33402297-d715-4f2b-84ed-bac4fded02e3.png)

![image](https://user-images.githubusercontent.com/95688723/146499719-84a08c0e-c907-4952-817e-1449915a8ac6.png)


6. Go to conditions bar and unflag the power section.

![image](https://user-images.githubusercontent.com/95688723/146499742-39a6f312-b034-4b82-8b9a-7e4f12bbadc1.png)

![image](https://user-images.githubusercontent.com/95688723/146499750-04654719-0062-489c-a62c-6d8263976e5b.png)


7. Press ok and you can see the script scheduled.

![image](https://user-images.githubusercontent.com/95688723/146499769-3a7324a7-5066-44a7-a80f-7cc60eaa9f10.png)


8. Finally restart your computer and see the magic.

![image](https://user-images.githubusercontent.com/95688723/146499810-0772d631-9092-4b3b-b3f5-395086699108.png)


Note: You can also check instantly by clicking run button.



