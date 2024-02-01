from django.shortcuts import render
from    django.http import HttpResponse
# Create your views here.
from animalhealthcare import connect, cdate


def adminchangepassword(request):
    return render(request,"adminchangepassword.html")

def adminchangepassword1(request):
    s1=request.POST["t1"]
    s2=request.POST["t2"]
    con=connect()
    cursor=con.cursor()
    s="select * from login where password='"+ s1 +  "'"
    cursor.execute(s)
    if cursor.rowcount==0:
        msg='Wrong Existing Password'
        return render(request,"adminchangepassword.html",{'msg':msg})
    else:
        s="update login set password='"+ s2 + "'"
        cursor.execute(s)
        con.commit()
        msg='Successfully Updated'
        return render(request,"adminchangepassword.html",{'msg':msg})




def hospitalreg1(request):
    return render(request,"hospitalreg1.html")

def hospitalreg2(request):
    s1=request.POST["t1"]
    s2 = request.POST["t2"]
    s3 = request.POST["t3"]
    s4 = request.POST["t4"]
    s5 = request.POST["t5"]
    s6 = request.POST["t6"]

    con=connect()
    cursor=con.cursor()
    s="select * from hospital order by hospid desc"
    hospid="H100"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        hospid=row[0]
        break
    x=hospid[1:]
    y=int(x)
    y=y+1
    hospid="H" + str(y)
    s="insert into hospital values('"+ hospid + "','" + s1 + "','" + s2 + "','" + s3 + "','" + s4 + "','" + s5 + "','" + s6  +"')"
    cursor.execute(s)
    con.commit()
    return render(request,"hospitalreg2.html",{'s1':s1 , 's2':s2 , 's3':s3 , 's4':s4 , 's5':s5 , 's6':s6,'hospid': hospid })


def staffreg1(request):
    con = connect()
    cursor = con.cursor()
    s = "select hospid from hospital"
    l=[]
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        l.append(row[0])
    s = "select hospid,location,place,pin,phone,district,hosptype from hospital"
    cursor.execute(s)
    records = cursor.fetchall()

    return render(request,"staffreg1.html",{'l':l,'records': records})


def staffreg2(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST['t1']
    s2 = request.POST['t2']
    s3 = request.POST['t3']
    s4 = request.POST['t4']
    s5 = request.POST['t5']
    s6 = request.POST['t6']
    s7 = request.POST['t7']
    s8 = request.POST['t8']
    s9 = request.POST['t9']
    s10 = request.POST['t10']
    regdate=cdate()
    s="select * from staff order by staffid desc"
    staffid = "s1000"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        break
    x = staffid[1:]
    y = int(x)
    y = y + 1
    staffid = "S" + str(y)
    s = "insert into staff values('" + staffid + "','" + s1 + "','" + s2 + "','" + s3 + "','" + s4 + "','" + s5 + "','" + s6 + "','" + s7+ "','" + s8+ "','" + s9 + "','" + staffid + "')"
    cursor.execute(s)
    con.commit()
    eno=0
    s="select * from staffwork where staffid='"+ staffid + "' order by eno desc"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        eno=row[0]
        break
    eno=eno+1

    s="insert into staffwork values('" + staffid + "',"+ str(eno) + ",'" + s10 + "','" + regdate +"')"

    cursor.execute(s)
    con.commit()

    s = "select hospid,location,place,pin,phone,district,hosptype from hospital"
    cursor.execute(s)
    records = cursor.fetchall()
    return render(request, "staffreg2.html",
                  {'records':records,'s1': s1, 's2': s2, 's3': s3, 's4': s4, 's5': s5, 's6': s6,'s7': s7,'s8': s8,'s9': s9,'s10': s10, 'staffid': staffid})


def medreg1(request):
    return render(request,"medreg1.html")


def medreg2(request):

    s1=request.POST["t1"]
    s2 = request.POST["t2"]
    s3 = request.POST["t3"]
    s4 = request.POST["t4"]
    s5 = request.POST["t5"]
    s6 = request.POST["t6"]

    con=connect()
    cursor=con.cursor()
    s="select * from medicine order by medid desc"
    medid="M1000"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        medid=row[0]
        break
    x=medid[1:]
    y=int(x)
    y=y+1
    medid="M" + str(y)
    s="insert into medicine values('"+ medid + "','" + s1 + "','" + s2 + "','" + s3 + "','" + s4 + "','" + s5 + "','" + s6  +"')"
    cursor.execute(s)
    con.commit()
    return render(request,"medreg2.html",{'s1':s1 , 's2':s2 , 's3':s3 , 's4':s4 , 's5':s5 , 's6':s6,'medid': medid })


def antypereg1(request):
    return render(request,"antypereg1.html")



def antypereg2(request):
    s1 = request.POST["t1"]
    s2 = request.POST["t2"]
    s3 = request.POST["t3"]
    s4 = request.POST["t4"]


    con = connect()
    cursor = con.cursor()
    s = "select * from animaltype where anname='"+ s1 +"'"
    cursor.execute(s)
    if cursor.rowcount>0:
        msg="This animal/Bird Name exist....."
    else:
        s="insert into animaltype values('" + s1 + "','" + s2 + "','"+ s3 + "','" + s4 + "')"
        cursor.execute(s)
        con.commit()
        msg="Details Stored"
    return render(request,"antypereg2.html",{'msg':msg,'s1':s1,'s2':s2,'s3':s3,'s4':s4})



def animalbreedreg1(request):
    con = connect()
    cursor = con.cursor()
    s = "select anname from animaltype"
    l=[]
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        l.append(row[0])

    return render(request,"animalbreedreg1.html",{'l': l})


def animalbreedreg2(request):
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
    s="select breed from animalbreed where anname='"+ s1 +  "'"
    cursor.execute(s)
    records1=cursor.fetchall()
    m=[]
    for row in records1:
        m.append(row[0])


    return render(request,"animalbreedreg2.html",{'m':m,'l': l,'s1':s1,'antype':antype,'production':production,'specification': specification})



def animalbreedreg3(request):
    s1 = request.POST["c1"]
    s2 = request.POST["t1"]
    s3 = request.POST["t2"]
    s4 = request.POST["t3"]
    s5 = request.POST["t4"]

    con = connect()
    cursor = con.cursor()
    s="select * from animalbreed where anname='"+ s1 + "'  and breed='"+ s2 +"'"
    cursor.execute(s)
    if cursor.rowcount>0:
        msg='This Breed Already Enteed'
    else:
        s="insert into animalbreed values('"+ s1 + "','" + s2 + "','" + s3 + "','" + s4 + "','" + s5+ "')"
        cursor.execute(s)
        con.commit()
        msg='Success........'

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
    s="select breed from animalbreed where anname='"+ s1 +  "'"
    cursor.execute(s)
    records1=cursor.fetchall()
    m=[]
    for row in records1:
        m.append(row[0])


    return render(request,"animalbreedreg3.html",{'msg':msg,'m':m,'l': l,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'antype':antype,'production':production,'specification': specification})


def vreg1(request):
    return render(request,"vreg1.html")

def vreg2(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["t1"]
    s2=request.POST["t2"]
    s="select * from vaccine where vacname='"+ s1  +"'"
    cursor.execute(s)
    if cursor.rowcount>0:
        msg="This vaccine already registered"
    else:
        s="insert into vaccine values('" + s1 + "','" + s2 + "')"
        cursor.execute(s)
        con.commit()
        msg="Registered"

    return render(request,"vreg2.html",{'s1':s1,'s2':s2,'msg':msg})

def allotvaccine1(request):
    con = connect()
    cursor = con.cursor()
    s="select vacname from vaccine"
    cursor.execute(s)
    records=cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])
    s = "select anname from animaltype"
    cursor.execute(s)
    records = cursor.fetchall()
    m = []
    for row in records:
        m.append(row[0])

    return render(request,"allotvaccine1.html",{'l':l,'m':m})


def allotvaccine2(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["c1"]
    s2=request.POST["c2"]
    s="select * from vaccine where vacname='"+ s1 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        details=row[1]
    s="select * from animaltype where anname='" + s2 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        antype=row[1]
        production=row[2]
        specification=row[3]

    s="select vacname from vaccine"
    cursor.execute(s)
    records=cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])
    s = "select anname from animaltype"
    cursor.execute(s)
    records = cursor.fetchall()
    m = []
    for row in records:
        m.append(row[0])
    s="select * from vaccinebreed where vacname='"+ s1 + "' and anname='" + s2 + "'"
    cursor.execute(s)
    aa=""
    if cursor.rowcount>0:
        aa=""
        msg="This vaccine already alloted to this Anmal"
    else:
        msg=""
        aa="Yes"

    return render(request,"allotvaccine2.html",{'msg':msg,'aa':aa,'l':l,'m':m,'s1':s1,'s2':s2,'details':details,'antype':antype,'production':production,'specification':specification})

def allotvaccine3(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["c1"]
    s2=request.POST["c2"]

    s3 = request.POST["t1"]
    s4 = request.POST["t2"]
    s5 = request.POST["t3"]
    s6 = request.POST["t4"]
    s7 = request.POST["t5"]

    s="select * from vaccine where vacname='"+ s1 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        details=row[1]
    s="select * from animaltype where anname='" + s2 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        antype=row[1]
        production=row[2]
        specification=row[3]

    s="select vacname from vaccine"
    cursor.execute(s)
    records=cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])
    s = "select anname from animaltype"
    cursor.execute(s)
    records = cursor.fetchall()
    m = []
    for row in records:
        m.append(row[0])
    s="select * from vaccinebreed where vacname='"+ s1 + "' and anname='" + s2 + "'"
    cursor.execute(s)
    aa=""
    if cursor.rowcount>0:
        aa=""
        msg="This vaccine already alloted to this Anmal"
    else:
        msg=""
        aa="Yes"
    s="insert into vaccinebreed values('"+ s1 + "','" + s2 + "','" + s3 + "','" + s4 + "','" +s5 + "','" + s6 + "','" + s7 +  "')"
    cursor.execute(s)
    con.commit()

    return render(request,"allotvaccine3.html",{'msg':msg,'aa':aa,'l':l,'m':m,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'details':details,'antype':antype,'production':production,'specification':specification})


def stafflist(request):
    con = connect()
    cursor = con.cursor()
    s="select staffid,name,hname,place,pin,ph,gender,email,qlfn,designation  from staff"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"stafflist.html",{'records':records})

def adminsignout(request):
    return render(request,"adminsignout.html")