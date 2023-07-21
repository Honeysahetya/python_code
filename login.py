print("""1.signup(add user)
2.login(check user)
3.delete user
4.exit""")





ulist = []
ch=0
while(ch!=4):
	if(ch==1):
		user = {}
		user['username']=input('enter user name:')
		user['pass']=input('enter passsword:')
		user['email']=input('email:')
		ulist.append(user)
		print("user created")
		
	if(ch==2):
		uname=input('enter username:')
		upass=input('enter passsword:')
		for u in ulist:
			if(u['username']==uname):
				print("user exist")

	if(ch==3):
		uname=input('enter username:')
		for u in ulist:
			if(u['username']==uname):
				ulist.remove(u)
				print('user deleted')
	ch=int(input('enter value'))



