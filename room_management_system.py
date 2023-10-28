
import cx_Oracle as niti
import datetime


db = niti.connect("scott/niti123@orclpdb")
st = db.cursor()
try:
    st.execute("create table checkin(names varchar2(30) ,roomtypenumber varchar2(15) , days number , aadharcard float(64) , join_date date)")
    def checkin():
        name = input("enter names :- ")
        tp = input("enter room type and number :- ")
        d = input("enter number of days :- ")
        ad = float(input("enter aadharcard number :- "))
        j = input("enter the checkin date (YYYY-MM-DD):- ")
        join_date = datetime.datetime.strptime(j, "%Y-%m-%d").date()
        st.execute("insert into checkin(names, roomtypenumber, days, aadharcard, join_date) values(:1, :2, :3, :4, :5)",(name, tp, d, ad, join_date))
        db.commit()
        print("data entered properly")
        main()
    st.execute("create table checkout (custname varchar2(20) , roomtype varchar2(20) , guests number , fare number , days number , bill number , checkout_date date)")
    def checkout():
        cn = input("enter customer name :- ")
        rm = input("enter room type and number :- ")
        tg = int(input("total guests :- "))
        f = int(input("total fare :- "))
        dy= int(input("total days :- "))
        data=(tg*f*dy)
        j = input("enter the checkin date (YYYY-MM-DD):- ")
        cd = datetime.datetime.strptime(j, "%Y-%m-%d").date()
        st.execute("insert into checkout(custname, roomtype, guests, fare, days, bill, checkout_date) values (:1, :2, :3, :4, :5, :6, :7)",(cn, rm, tg, f, dy, data, cd))
        db.commit()
        print("data inputed properly")
        main()
    def rooms():
        print("executive = 5000/guest/day")
        print(" ")
        print("facilities = wifi,tv,AC,bathroom with tub and gyser,breakfast,lunch,dinner")
        print(" ")
        print("deluxe = 2500/guest/day")
        print(" ")
        print("facilities - wifi,tv,ac,bathroom wih tub and gyser")
        print(" ")
        print("simple = 1000/guest/day")
        print(" ")
        print("facilities = wifi,tv,bathroom with gyser")
        main()
    def main():
        print("1.checkin")
        print("2.checkout")
        print("3.fare and eminities")
        c = int(input("choice : "))
        if c == 1:
            checkin()
        elif c == 2:
            checkout()
        elif c == 3:
            rooms()
        else:
            print("enter correct choice")
        main()
    main()
except Exception as a:
    print("error message",a)
finally:
    st.execute("drop table checkin")
    st.execute("drop table checkout")
