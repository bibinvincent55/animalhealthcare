import os

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.
from animalhealthcare import connect, cdate


def ownerchangepassword(request):
    return render(request,"ownerchangepassword.html")

def ownerchangepassword1(request):
    s1=request.POST["t1"]
    s2=request.POST["t2"]
    con=connect()
    cursor=con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    ownerid=""
    for row in records:
        ownerid=row[0]

    s="select * from owner where password='"+ s1 +  "'  and ownerid='"+ ownerid +  "'"
    print(s)
    cursor.execute(s)
    if cursor.rowcount==0:
        msg='Wrong Existing Password'
        return render(request,"ownerchangepassword.html",{'msg':msg})
    else:

        s="update owner set password='"+ s2 + "' where ownerid='"+ ownerid +  "'"
        cursor.execute(s)
        con.commit()
        msg='Successfully Updated'
        return render(request,"ownerchangepassword.html",{'msg':msg})

def addanimal(request):
    con = connect()
    cursor = con.cursor()
    s = "select anname from animaltype"
    l = []
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        l.append(row[0])
    return render(request,"addanimal.html",{'l':l})


def addanimal1(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["c1"]
    s="select breed from animalbreed where anname='"+ s1 + "'"
    print(s)
    cursor.execute(s)
    records=cursor.fetchall()
    m=[]
    for row in records:
        m.append(row[0])
    s = "select anname from animaltype"
    l = []
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        l.append(row[0])
    return render(request,"addanimal1.html",{'l':l,'m':m,'s1':s1})


def addanimal2(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["c1"]
    s2=request.POST["t1"]
    s3 = request.POST["t2"]
    s4 = request.POST["t3"]
    s5 = request.POST["t4"]
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    ownerid=""
    for row in records:
        ownerid=row[0]

    s="select * from owneranimal where ownerid='"+ ownerid + "' order by anno desc"
    cursor.execute(s)
    records=cursor.fetchall()
    anno=0
    for row in records:
        anno=row[1]
        break
    anno=anno+1
    regdate=cdate()
    s="insert into owneranimal (ownerid,anno,anname,breed,age,ageunit,origin,regdate) values('" + ownerid + "'," + str(anno) + ",'" + s1 + "','" + s2 +  "','" + s3 + "','" + s4 + "','" + s5 + "','" + regdate +"')"
    cursor.execute(s)
    con.commit()
    s="select breed from animalbreed where anname='"+ s1 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    m=[]
    for row in records:
        m.append(row[0])
    s = "select anname from animaltype"
    l = []
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        l.append(row[0])

    msg='Success'
    return render(request,"addanimal2.html",{'l':l,'m':m,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'msg':msg})


def myanimals(request):
    con = connect()
    cursor = con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    ownerid=""
    for row in records:
        ownerid=row[0]
    s="select anno,anname,breed,age,ageunit,origin,regdate  from owneranimal where ownerid='" + ownerid + "' and exist='Y'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"myanimals.htm",{'records': records})


def ownerrequest1(request):
    con = connect()
    cursor = con.cursor()
    return render(request,"ownerrequest1.html")

def ownerrequest2(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["t1"]
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        ownerid=row[0]
    reqdate=cdate()
    reqno=0
    s="select * from ownerrequest order by reqno desc"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        reqno=row[0]
        break
    reqno=reqno+1
    s="insert into ownerrequest values("+ str(reqno) + ",'" + s1 + "','" + reqdate + "','" + ownerid+ "')"
    cursor.execute(s)
    con.commit()
    return render(request,"ownerrequest2.html",{'s1':s1,'reqno':reqno})


def viewreqresponse1(request):
    con=connect()
    cursor=con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        ownerid=row[0]

    s="select reqno,reqdate from ownerrequest where ownerid='"+ ownerid +  "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"viewreqresponse1.html",{'records':records})


def viewreqresponse2(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["t1"]
    s="select * from ownerrequest where reqno="+ s1
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        request1=row[1]
        reqdate=row[2]

    s="select * from response where reqno=" + s1
    cursor.execute(s)
    records=cursor.fetchall()
    response1=""
    staffid=""
    respdate=""

    for row in records:
        response1=row[1]
        staffid=row[2]
        respdate=row[3]
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        ownerid=row[0]

    s="select reqno,reqdate from ownerrequest where ownerid='"+ ownerid +  "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"viewreqresponse2.html",{'records':records,'s1':s1,'request1':request1,'reqdate':reqdate,'response1':response1,'respdate':respdate,'staffid':staffid})

def staffvisitdetails(request):
    con = connect()
    cursor = con.cursor()
    s="select * from session "
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        s1=row[0]

    s = "select * from owner where ownerid='" + s1 + "'"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        ownername = row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        phone = row[5]
        gender = row[6]
        district = row[8]
        email = row[9]
    s = "select vno,vstatus,staffid,vdetails,vdate from visit where ownerid='" + s1 + "'"
    cursor.execute(s)
    records = cursor.fetchall()
    return render(request, "staffvisitdetails.html",
                  {'records': records, 's1': s1, 'ownername': ownername, 'hname': hname, 'place': place, 'pin': pin,
                   'phone': phone, 'gender': gender, 'district': district, 'email': email})

def treatmentrequest1(request):
    con = connect()
    cursor = con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    ownerid=""
    for row in records:
        ownerid=row[0]
    s="select anno,anname,breed,age,ageunit,origin,regdate  from owneranimal where ownerid='" + ownerid + "' and exist='Y'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"treatmentrequest1.html",{'records': records})

def treatmentrequest2(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["t1"]
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    ownerid = ""
    for row in records:
        ownerid = row[0]
    s="select * from owneranimal where ownerid='"+ ownerid +"' and anno=" + s1
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        anname=row[2]
        breed=row[3]
        age=row[4]
        ageunit=row[5]
        origin=row[6]
        regdate=row[7]

    s="select anno,anname,breed,age,ageunit,origin,regdate  from owneranimal where ownerid='" + ownerid + "' and exist='Y'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"treatmentrequest2.html",{'records': records,'s1':s1,'anname':anname,'breed':breed,'age':age,'ageunit':ageunit,'origin':origin,'regdate':regdate})

def treatmentrequest3(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["t1"]
    s2 = request.POST["t2"]
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    ownerid = ""
    for row in records:
        ownerid = row[0]
    file = request.FILES['file']
    fs = FileSystemStorage()
    filename = fs.save("./uploads/" + file.name, file)
    filename = filename[10:]


    tno=0
    s="select * from treatment order by tno desc"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        tno=row[0]
        break
    tno=tno+1
    pdate=cdate()
    s="insert into treatment (tno,ownerid,anno,problem,pdate,phfname) values("+ str(tno) + ",'"+ ownerid + "',"+ s1 + ",'" + s2  + "','" + pdate + "','" + filename +    "')"

    cursor.execute(s)
    con.commit()
    s="select * from owneranimal where ownerid='"+ ownerid +"' and anno=" + s1
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        anname=row[2]
        breed=row[3]
        age=row[4]
        ageunit=row[5]
        origin=row[6]
        regdate=row[7]

    s="select anno,anname,breed,age,ageunit,origin,regdate  from owneranimal where ownerid='" + ownerid + "' and exist='Y'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"treatmentrequest3.html",{'tno':tno,'records': records,'s1':s1,'s2':s2,'anname':anname,'breed':breed,'age':age,'ageunit':ageunit,'origin':origin,'regdate':regdate})


def treatment11(request):
    con = connect()
    cursor = con.cursor()
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        ownerid = row[0]
    s = "select tno from treatment where ownerid='"+ ownerid + "'"
    cursor.execute(s)
    records = cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])
    return  render(request,"treatment11.html",{'l':l})


def treatment22(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["c1"]
    s="select * from treatment where tno="+ s1
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        ownerid=row[1]
        anno=row[2]
        problem=row[3]
        pdate=row[4]
        phfname=row[5]
        pfname=row[6]
        instruction=row[7]
        staffid=row[8]
        tdate=row[9]


    s="select * from owneranimal where ownerid='"+ ownerid +  "'  and anno="+  str(anno)
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        anname=row[2]
        breed=row[3]
        age=row[4]
        ageunit=row[5]
        origin=row[6]
        regdate=row[7]
        certificate=row[12]


    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        ownerid = row[0]
    s = "select tno from treatment where ownerid='" + ownerid + "'"
    cursor.execute(s)
    records = cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])
    return  render(request,"treatment22.html",{'pfname':pfname,'instruction':instruction,'staffid':staffid,'tdate':tdate,'l':l,'s1':s1,'ownerid':ownerid,'anno':anno,'problem':problem,'pdate':pdate,'phfname':phfname,'anname':anname,'breed':breed,'age':age,'ageunit':ageunit,'origin':origin,'regdate':regdate,'certificate':certificate})


def down33(request):
    s1=request.POST["t1"]
    file_path='./prescription/'+ s1
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def applyvaccineview22(request):
    con=connect()
    cursor=con.cursor()
    s="select * from session "
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        s1=row[0]
    s="select * from owner where ownerid='"+ s1 +  "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        ownername=row[1]
        hname=row[2]
        place=row[3]
        pin=row[4]
        phone=row[5]
        gender=row[6]
        district=row[8]
        email=row[9]

    s="select anno,anname,breed,age,ageunit,origin,regdate  from owneranimal where ownerid='" + s1 + "' and exist='Y'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"applyvaccineview22.html",{'records':records,'s1':s1,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})

def applyvaccineview33(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["t1"]
    s2 = request.POST["t2"]
    s="select * from owner where ownerid='"+ s1 +  "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        ownername=row[1]
        hname=row[2]
        place=row[3]
        pin=row[4]
        phone=row[5]
        gender=row[6]
        district=row[8]
        email=row[9]
    s = "select * from owneranimal where ownerid='" + s1 + "' and anno=" + s2
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        anname = row[2]
        breed = row[3]
        age = row[4]
        ageunit = row[5]
        origin = row[6]
        regdate = row[7]
    s = "select applyno,vacname,applydate,staffid from applyvaccine where ownerid='" + s1 + "' and anno='" + s2 + "'"


    cursor.execute(s)
    records22 = cursor.fetchall()

    return render(request,"applyvaccineview33.html",{'records22':records22,'anname':anname,'breed':breed,'age':age,'ageunit':ageunit,'origin':origin,'regdate':regdate,'s1':s1,'s2':s2,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})




def treatmentlist22(request):
    con=connect()
    cursor=con.cursor()
    s="select * from session "
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        s1=row[0]
    s="select * from owner where ownerid='"+ s1 +  "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        ownername=row[1]
        hname=row[2]
        place=row[3]
        pin=row[4]
        phone=row[5]
        gender=row[6]
        district=row[8]
        email=row[9]

    s="select anno,anname,breed,age,ageunit,origin,regdate  from owneranimal where ownerid='" + s1 + "' and exist='Y'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"treatmentlist22.html",{'records':records,'s1':s1,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})

def treatmentlist33(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["t1"]
    s2 = request.POST["t2"]
    s="select * from owner where ownerid='"+ s1 +  "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        ownername=row[1]
        hname=row[2]
        place=row[3]
        pin=row[4]
        phone=row[5]
        gender=row[6]
        district=row[8]
        email=row[9]
    s = "select * from owneranimal where ownerid='" + s1 + "' and anno=" + s2
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        anname = row[2]
        breed = row[3]
        age = row[4]
        ageunit = row[5]
        origin = row[6]
        regdate = row[7]
    s = "select tno,anno,problem,pdate from treatment where ownerid='" + s1 + "' and anno='" + s2 + "'"

    cursor.execute(s)
    records22 = cursor.fetchall()

    return render(request,"treatmentlist33.html",{'records22':records22,'anname':anname,'breed':breed,'age':age,'ageunit':ageunit,'origin':origin,'regdate':regdate,'s1':s1,'s2':s2,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})



def visitlist22(request):
    con=connect()
    cursor=con.cursor()
    s="select * from session "
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        s1=row[0]
    s="select * from owner where ownerid='"+ s1 +  "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        ownername=row[1]
        hname=row[2]
        place=row[3]
        pin=row[4]
        phone=row[5]
        gender=row[6]
        district=row[8]
        email=row[9]

    s="select anno,anname,breed,age,ageunit,origin,regdate  from owneranimal where ownerid='" + s1 + "' and exist='Y'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"visitlist22.html",{'records':records,'s1':s1,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})

def visitlist33(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["t1"]
    s2 = request.POST["t2"]
    s="select * from owner where ownerid='"+ s1 +  "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        ownername=row[1]
        hname=row[2]
        place=row[3]
        pin=row[4]
        phone=row[5]
        gender=row[6]
        district=row[8]
        email=row[9]
    s = "select * from owneranimal where ownerid='" + s1 + "' and anno=" + s2
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        anname = row[2]
        breed = row[3]
        age = row[4]
        ageunit = row[5]
        origin = row[6]
        regdate = row[7]
    s = "select vno,vstatus,staffid,vdetails,vdate from visit where ownerid='" + s1 + "'"

    cursor.execute(s)
    records22 = cursor.fetchall()

    return render(request,"visitlist33.html",{'records22':records22,'anname':anname,'breed':breed,'age':age,'ageunit':ageunit,'origin':origin,'regdate':regdate,'s1':s1,'s2':s2,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})
def ownersignout(request):
    return render(request,"ownersignout.html")