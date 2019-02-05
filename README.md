***************************************************************************************
--------------------------------- INITIAL PROCEDURES-----------------------------------
	
"IMPORTANT" 
repo id: https://github.com/415ec080/finalPrj.git
"everything inside < > is the cmd to copy and paste on the cmd "


1. Please ensure that you have verified your account
2. Make a new folder where ever you want
3. Open terminal or cmd (considering that git cli is installed), go to the new folder created
4. clone the repository by using the command
	<git clone https://github.com/415ec080/finalPrj.git>
5. This would have created a copy of the repository in the new folder created. It would also consist of .git 'hidden' folder and 		README.md folder
6. Now make a new folder there with your name similarly as in the repo
7. To test if ypu have push access, go to your folder (the folder created with your name) and make a new file. (say 'test.txt')
8. In the home directory (the cloned dir with .git folder is called home directory form now), type
	<git remote add origin https://github.com/415ec080/finalPrj.git>
		to create remote access to the repository
9. Next pull the repository to sync all the files and folder in the server
	<git pull origin>
10. Now add all the new files you have created
	<git add .>
11. Commit to the changes
	<git commit -m "any_name">
		inside "" any name can be given. But for the sake of ease please use the following standard:
			"first_3_letters_of_your_name_varsion_number"
			ex: "pra_V1", "san_V2","adi_V420" etc
			please do increment the version number for each commit or else you cant revert back.
12. now push the changes to the server using remote
	<git push origin master>
13. give all the necessory credentials to login and it must not throw any error.
	usually correct o/p will end with some id followed by "master -> master"