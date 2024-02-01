from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from animalhealthcare import connect


def home(request):
    return render(request,"home.html")

def adminlogin(request):
    return render(request,"adminlogin.html")

def adminlogin1(request):
    s1=request.POST["t1"]
    s2=request.POST["t2"]
    con=connect()
    cursor=con.cursor()
    s="select * from login where userid='" + s1 +"'  and password='"+ s2 +"'"

    cursor.execute(s)
    if cursor.rowcount==0:
        msg="Invalid ID or Password"
        return render(request,"adminlogin.html",{'msg':msg})
    else:
        return render(request,'adminprocess.html')


def hospitals(request):
    con=connect()
    cursor=con.cursor()
    s="select hospid,location,place,pin,phone,district,hosptype from hospital"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"hospitals.html",{'records':records})


def animals(request):
    con=connect()
    cursor=con.cursor()
    s="select anname,antype,production,specification from animaltype"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"animals.html",{'records':records})






def animalbreed1(request):
    con = connect()
    cursor = con.cursor()
    s = "select anname from animaltype"
    l=[]
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        l.append(row[0])

    return render(request,"animalbreed1.html",{'l': l})


def animalbreed2(request):
    s1=request.POST["c1"]
    con = connect()
    cursor = con.cursor()
    s="select * from animaltype where  anname='" + s1 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        antype=row[1]
        production=row[2]
        specification=row[3]

    s = "select anname from animaltype"
    l=[]
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        l.append(row[0])
    s="select breed,foodsp,annature,anhusbandary from animalbreed where anname='"+ s1 +  "'"
    cursor.execute(s)
    records1=cursor.fetchall()
    return render(request,"animalbreed2.html",{'records1':records1,'l': l,'s1':s1,'antype':antype,'production':production,'specification': specification})


def stafflogin(request):
    return render(request,"stafflogin.html")

def stafflogin1(request):
    s1=request.POST["t1"]
    s2=request.POST["t2"]
    con=connect()
    cursor=con.cursor()
    s="select * from staff where staffid='" + s1 +"'  and password='"+ s2 +"'"
    cursor.execute(s)
    if cursor.rowcount==0:
        msg="Invalid ID or Password"
        return render(request,"stafflogin.html",{'msg':msg})
    else:
        hospid=""
        s="delete from session"
        cursor.execute(s)
        con.commit()
        s="select * from staffwork where staffid='"+ s1 +"' order by eno desc"
        cursor.execute(s)
        records=cursor.fetchall()
        for row in records:
            hospid=row[2]
            break
        s="insert into session values('"+ s1 + "','"+ hospid + "')"
        cursor.execute(s)
        con.commit()

        return render(request,'staffprocess.html')



def ownerlogin1(request):
    return render(request,"ownerlogin.html")

def ownerlogin2(request):
    s1=request.POST["t1"]
    s2=request.POST["t2"]
    con=connect()
    cursor=con.cursor()
    s="select * from owner where ownerid='" + s1 +"'  and password='"+ s2 +"'"
    cursor.execute(s)
    if cursor.rowcount==0:
        msg="Invalid ID or Password"
        return render(request,"ownerlogin.html",{'msg':msg})
    else:
        hospid=""
        records = cursor.fetchall()
        for row in records:
            hospid = row[7]
            break
        s="delete from session"
        cursor.execute(s)
        con.commit()



        s="insert into session values('"+ s1 + "','"+ hospid + "')"
        cursor.execute(s)
        con.commit()

        return render(request,'ownerprocess.html')


def viewvaccine1(request):
    con = connect()
    cursor = con.cursor()
    s="select vacname from vaccine"
    cursor.execute(s)
    records=cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])

    return render(request,"viewvaccine1.html",{'l':l})

def viewvaccine2(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["c1"]
    s="select anname,age,ageunit,ndos,vqty,details from vaccinebreed where vacname='" + s1 + "'"
    cursor.execute(s)
    records1=cursor.fetchall()

    s="select vacname from vaccine"
    cursor.execute(s)
    records=cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])

    return render(request,"viewvaccine2.html",{'l':l,'records1':records1})


def viewvaccine11(request):
    con = connect()
    cursor = con.cursor()
    s="select anname from animaltype"
    cursor.execute(s)
    records=cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])

    return render(request,"viewvaccine11.html",{'l':l})

def viewvaccine22(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["c1"]
    s="select vacname,age,ageunit,ndos,vqty,details from vaccinebreed where anname='" + s1 + "'"
    cursor.execute(s)
    records1=cursor.fetchall()

    s = "select anname from animaltype"
    cursor.execute(s)
    records=cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])

    return render(request,"viewvaccine22.html",{'l':l,'records1':records1})





def medicinelist(request):
    con = connect()
    cursor = con.cursor()
    s="select medid,medname,medtype,content,medcategory,medunit,company  from medicine"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"medicinelist.html",{'records':records})

def about(request):
    return render(request,"about.html")