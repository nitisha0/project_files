import cx_Oracle as dbms

db=dbms.connect("scott/niti123@orclpdb")
st=db.cursor()
try:
    st.execute("create sequence idgen")
    st.execute(" create table banking (bankid number default idgen.nextval primary key, name varchar2(15), balance number , phnumber  number , address varchar2(20)) ")
    while(True):
        print("welcome to our bank")
        print("select one of the option to continue")
        print("1.create an account", "2.deposit", "3.withdraw", "4.account info", "5.end application",sep='\n')
        userchoice=int(input())
        if userchoice==1:
            name=input("enter the name :- ")
            balance=int(input("enter the initial balance :- "))
            phno=int(input("enter the phone number :- "))
            add=input("enter address :- ")
            st.execute("select bankid from banking where name='{}'".format(name))
            if st.rowcount:
                print("the user already exits with bank account number",st.fetchone())
            else:
                st.execute("insert into banking(name,balance,phnumber,address) values ('{}' , {} , {} , '{}')".format(name,balance,phno,add))
                db.commit()
                st.execute("select idgen.currval from dual")
                print("your account is created with account number",st.fetchone(),"\n\n")
        elif userchoice==2:
            id = int(input("enter the your bank account number :- "))
            st.execute("select  balance from banking where bankid = {}".format(id))
            balance = st.fetchone()[0]
            dep = int(input("enter the amount to be deposited :- "))
            bal = balance+dep
            st.execute("update banking set balance = {} where bankid = {}".format(bal,id))
            db.commit()
            print("your amount id credited \nto check updated balance please use account info option\n\n")
        elif userchoice==3:
            id = int(input("enter your bank account number :- "))
            st.execute("select balance from banking where bankid = {}".format(id))
            balance = st.fetchone()[0]
            withd = int(input("enter the amount to be withdrawn :- "))
            if withd < balance:
                bal = balance - withd
                st.execute("update banking set balance = {} where bankid = {}".format(bal,id))
                db.commit()
                print("your amount is withdrawn \n to check updated balance please use account info option\n\n")
            else:
                print("insufficient balance!!")
        elif userchoice==4:
            id = int(input("enter your bank account number :- "))
            st.execute("select * from banking where bankid = {}".format(id))
            print("your details are as follows:id,name,balance")
            for i in st.fetchone():
                print(i)
        elif userchoice==5:
            break
except Exception as a:
    print("error message",a)
finally:
    st.execute("drop sequence idgen")
    st.execute("drop table banking")
