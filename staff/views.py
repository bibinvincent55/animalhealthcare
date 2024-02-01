import os

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
from animalhealthcare import connect, cdate


def staffchangepassword(request):
    return render(request,"staffchangepassword.html")

def staffchangepassword1(request):
    s1=request.POST["t1"]
    s2=request.POST["t2"]
    con=connect()
    cursor=con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    staffid=""
    for row in records:
        staffid=row[0]

    s="select * from staff where password='"+ s1 +  "'  and staffid='"+ staffid +  "'"
    print(s)
    cursor.execute(s)
    if cursor.rowcount==0:
        msg='Wrong Existing Password'
        return render(request,"staffchangepassword.html",{'msg':msg})
    else:

        s="update staff set password='"+ s2 + "' where staffid='"+ staffid +  "'"
        cursor.execute(s)
        con.commit()
        msg='Successfully Updated'
        return render(request,"staffchangepassword.html",{'msg':msg})



def ownerreg1(request):
    return render(request,"ownerreg1.html")

def ownerreg2(request):
    s1=request.POST["t1"]
    s2=request.POST["t2"]
    s3 = request.POST["t3"]
    s4 = request.POST["t4"]
    s5 = request.POST["t5"]
    s6 = request.POST["t6"]
    s7 = request.POST["t7"]
    s8 = request.POST["t8"]
    con=connect()
    cursor=con.cursor()
    s="select * from session"

    cursor.execute(s)
    records=cursor.fetchall()
    staffid=""
    hospid=""
    for row in records:
        staffid=row[0]
        hospid=row[1]
    s = "select * from owner order by ownerid desc"

    ownerid = "O1000"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        ownerid = row[0]
        break

    x = ownerid[1:]
    y = int(x)
    y = y + 1
    ownerid = "O" + str(y)
    file = request.FILES['file']
    fs = FileSystemStorage()
    filename = fs.save("./adhar/" + file.name, file)
    filename = filename[8:]
    regdate=cdate()
    s = "insert into owner values('" + ownerid + "','" + s1 + "','" + s2 + "','" + s3 + "','" + s4 + "','" + s5 + "','" + s6 + "','" + hospid + "','" + s7 + "','" + s8 + "','" + ownerid +  "','" + regdate + "','"+ filename + "','" + staffid + "')"

    cursor.execute(s)
    con.commit()
    return render(request,"ownerreg2.html",{'ownerid':ownerid,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8})
    
    return HttpResponse("ok")

def animalapproval1(request):
    con = connect()
    cursor = con.cursor()
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    staffid = ""
    hospid = ""
    for row in records:
        staffid = row[0]
        hospid = row[1]
    s="select distinct(ownerid) from owneranimal where exist is null and ownerid in(select ownerid from owner where hospid='"+ hospid +"')"
    cursor.execute(s)
    records=cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])
    return render(request,"animalapproval1.html",{'l':l})


def animalapproval2(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["c1"]
    s="select anno,anname,breed from owneranimal where ownerid='"+ s1 + "' and exist is null"
    cursor.execute(s)
    records1=cursor.fetchall()

    s="select * from owner where ownerid='"+ s1 +"'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        ownername=row[1]
        hname=row[2]
        place=row[3]
        pin=row[4]
        phone=row[5]
        gender=row[6]


    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    staffid = ""
    hospid = ""
    for row in records:
        staffid = row[0]
        hospid = row[1]
    s="select distinct(ownerid) from owneranimal where exist is null and ownerid in(select ownerid from owner where hospid='"+ hospid +"')"
    cursor.execute(s)
    records=cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])
    return render(request,"animalapproval2.html",{'l':l,'s1':s1,'records1': records1,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender})




def animalapproval3(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["c1"]
    s2=request.POST["c2"]


    s="select * from owner where ownerid='"+ s1 +"'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        ownername=row[1]
        hname=row[2]
        place=row[3]
        pin=row[4]
        phone=row[5]
        gender=row[6]
    s="select * from owneranimal where ownerid='"+ s1 +"'  and anno=" + str(s2)
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        anno=row[1]
        anname=row[2]
        breed=row[3]
        age=row[4]
        ageunit=row[5]
        origin=row[6]
        regdate=row[7]


    return render(request,"animalapproval3.html",{'s1':s1,'s2':s2,'anno':anno,'anname':anname,'breed':breed,'age':age,'ageunit':ageunit,'ageunit':ageunit,'origin':origin,'regdate':regdate,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender})




def animalapproval4(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["c1"]
    s2=request.POST["c2"]
    s3=request.POST["r1"]
    s4=request.POST["t1"]
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[0]
    appdate=cdate()
    if s3=="Y":
        s="update owneranimal set approval='" + s3 + "',details='" + s4 +"',staffid='"+ staffid  + "',appdate='" + appdate +"',exist='Y'  where ownerid='" + s1 + "' and anno=" + s2
    else:
        s = "update owneranimal set approval='" + s3 + "',details='" + s4 + "',staffid='" + staffid + "',appdate='" + appdate + "',exist='N'  where ownerid='" + s1 + "' and anno=" + s2


    cursor.execute(s)
    con.commit()

    s="select * from owner where ownerid='"+ s1 +"'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        ownername=row[1]
        hname=row[2]
        place=row[3]
        pin=row[4]
        phone=row[5]
        gender=row[6]
    s="select * from owneranimal where ownerid='"+ s1 +"'  and anno=" + str(s2)
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        anno=row[1]
        anname=row[2]
        breed=row[3]
        age=row[4]
        ageunit=row[5]
        origin=row[6]
        regdate=row[7]
    if s3=="Y":
        return render(request,"animalapproval4.html",{'s1':s1,'s2':s2,'s3':s3,'s4':s4,'anno':anno,'anname':anname,'breed':breed,'age':age,'ageunit':ageunit,'ageunit':ageunit,'origin':origin,'regdate':regdate,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender})
    else:
        return render(request, "animalapproval44.html",
                      {'s1': s1, 's2': s2,'s3':s3,'s4':s4, 'anno': anno, 'anname': anname, 'breed': breed, 'age': age,
                       'ageunit': ageunit, 'ageunit': ageunit, 'origin': origin, 'regdate': regdate,
                       'ownername': ownername, 'hname': hname, 'place': place, 'pin': pin, 'phone': phone,
                       'gender': gender})


def animalapproval5(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["c1"]
    s2=request.POST["c2"]
    s3=request.POST["r1"]
    s4=request.POST["t1"]

    s="select * from owner where ownerid='"+ s1 +"'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        ownername=row[1]
        hname=row[2]
        place=row[3]
        pin=row[4]
        phone=row[5]
        gender=row[6]
    s="select * from owneranimal where ownerid='"+ s1 +"'  and anno=" + str(s2)
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        anno=row[1]
        anname=row[2]
        breed=row[3]
        age=row[4]
        ageunit=row[5]
        origin=row[6]
        regdate=row[7]
    file = request.FILES['file']
    fs = FileSystemStorage()
    filename = fs.save("./animalproof/" + file.name, file)
    filename = filename[14:]
    s = "update owneranimal set certificate='" + filename + "'  where ownerid='" + s1 + "' and anno=" + s2

    cursor.execute(s)
    con.commit()

    return render(request,"animalapproval5.html",{'s1':s1,'s2':s2,'s3':s3,'s4':s4,'anno':anno,'anname':anname,'breed':breed,'age':age,'ageunit':ageunit,'ageunit':ageunit,'origin':origin,'regdate':regdate,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender})

def ownerslist(request):
    con=connect()
    cursor=con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        hospid=row[1]
    s="select ownerid,ownername,hname,place,pin,phone,gender,district,email  from owner where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"ownerslist.html",{'records':records})

def owneranimal1(request):
    con=connect()
    cursor=con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        hospid=row[1]
    s="select ownerid,ownername,hname,place,pin,phone,gender,district,email  from owner where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"owneranimal1.html",{'records':records})

def owneranimal2(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["t1"]
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

    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        hospid=row[1]
    s="select anno,anname,breed,age,ageunit,origin,regdate  from owneranimal where ownerid='" + s1 + "' and exist='Y'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"owneranimal2.html",{'records':records,'s1':s1,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})

def reqresponse1(request):
    con=connect()
    cursor=con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        hospid=row[1]

    s="select reqno,reqdate,ownerid from ownerrequest where ownerid in (select ownerid from owner where hospid='"+ hospid +  "') and reqno not in (select reqno from response)"


    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"reqresponse1.html",{'records':records})


def reqresponse2(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["t1"]
    s="select * from ownerrequest where reqno=" + s1
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        request1=row[1]
        reqdate=row[2]
        ownerid=row[3]
    s="select * from owner where ownerid='" + ownerid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        ownername=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        phone = row[5]
        gender = row[6]
        district = row[8]
        email = row[9]


    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        hospid=row[1]
    s = "select reqno,reqdate,ownerid from ownerrequest where ownerid in (select ownerid from owner where hospid='" + hospid + "') and reqno not in (select reqno from response)"

    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"reqresponse2.html",{'records':records,'s1':s1,'request1':request1,'reqdate':reqdate,'ownerid':ownerid,'ownername':ownername,'hanme':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})


def reqresponse3(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["t1"]
    s2 = request.POST["t2"]
    s="select * from ownerrequest where reqno=" + s1
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        request1=row[1]
        reqdate=row[2]
        ownerid=row[3]
    s="select * from owner where ownerid='" + ownerid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        ownername=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        phone = row[5]
        gender = row[6]
        district = row[8]
        email = row[9]


    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[0]
        hospid=row[1]
    respdate=cdate()
    s="insert into response values("+ s1 + ",'"+ s2 + "','"+ staffid + "','"+ respdate + "')"
    cursor.execute(s)
    con.commit()

    s = "select reqno,reqdate,ownerid from ownerrequest where ownerid in (select ownerid from owner where hospid='" + hospid + "') and reqno not in (select reqno from response)"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"reqresponse3.html",{'records':records,'s1':s1,'s2':s2,'request1':request1,'reqdate':reqdate,'ownerid':ownerid,'ownername':ownername,'hanme':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})



def visitentry1(request):
    con=connect()
    cursor=con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        hospid=row[1]
    s="select ownerid,ownername,hname,place,pin,phone,gender,district,email  from owner where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"visitentry1.html",{'records':records})


def visitentry2(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["t1"]
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

    return render(request,"visitentry2.html",{'s1':s1,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})



def visitentry3(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["t1"]
    s2 = request.POST["t2"]
    s3 = request.POST["t3"]
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
    s="select * from visit order by vno desc"
    cursor.execute(s)
    records=cursor.fetchall()
    vno=0
    for row in records:
        vno=row[0]
        break
    vno=vno +1
    vdate=cdate()
    s="select * from session "
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[0]
    s="insert into visit values("+ str(vno) + ",'" + s1 + "','" + s2 + "','" + staffid + "','" + s3 + "','" + vdate + "')"
    cursor.execute(s)
    con.commit()
    return render(request,"visitentry3.html",{'s1':s1,'s2':s2,'s3':s3,'vno':vno,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})


def visitdetails1(request):
    con=connect()
    cursor=con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        hospid=row[1]
    s="select ownerid,ownername,hname,place,pin,phone,gender,district,email  from owner where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"visitdetails1.html",{'records':records})

def visitdetails2(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["t1"]
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
    s="select vno,vstatus,staffid,vdetails,vdate from visit where ownerid='"+ s1  +"'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"visitdetails2.html",{'records':records,'s1':s1,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})


def treatment1(request):
    con = connect()
    cursor = con.cursor()
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        hospid = row[1]
    s = "select tno from treatment where ownerid in(select ownerid from owner where hospid='"+ hospid + "') and pfname is null"

    cursor.execute(s)
    records = cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])
    return  render(request,"treatment1.html",{'l':l})


def treatment2(request):
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
    s="select * from owner where ownerid='"+ ownerid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        ownername=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        phone = row[5]
        gender = row[6]
        district = row[8]
        email = row[9]

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
        hospid = row[1]
    s = "select tno from treatment where ownerid in(select ownerid from owner where hospid='"+ hospid + "')  and pfname is null"

    cursor.execute(s)
    records = cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])
    return  render(request,"treatment2.html",{'l':l,'s1':s1,'ownerid':ownerid,'anno':anno,'problem':problem,'pdate':pdate,'phfname':phfname,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email,'anname':anname,'breed':breed,'age':age,'ageunit':ageunit,'origin':origin,'regdate':regdate,'certificate':certificate})

def treatment3(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["c1"]
    s2 = request.POST["t2"]
    s="select * from treatment where tno="+ s1
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        ownerid=row[1]
        anno=row[2]
        problem=row[3]
        pdate=row[4]
        phfname=row[5]
    s="select * from owner where ownerid='"+ ownerid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        ownername=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        phone = row[5]
        gender = row[6]
        district = row[8]
        email = row[9]

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
    tdate=cdate()


    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid=row[0]
        hospid = row[1]
    file = request.FILES['file']
    fs = FileSystemStorage()
    filename = fs.save("./prescription/" + file.name, file)
    filename = filename[15:]

    s="update treatment set pfname='"+ filename +  "',instruction='"+s2 +  "',staffid='" + staffid + "',tdate='"+ tdate +"' where tno="+ s1
    cursor.execute(s)
    con.commit()


    return  render(request,"treatment3.html",{'s1':s1,'s2':s2,'ownerid':ownerid,'anno':anno,'problem':problem,'pdate':pdate,'phfname':phfname,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email,'anname':anname,'breed':breed,'age':age,'ageunit':ageunit,'origin':origin,'regdate':regdate,'certificate':certificate})


def down11(request):
    s1=request.POST["t1"]
    file_path='./uploads/'+ s1
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def down22(request):
    s1=request.POST["t1"]
    file_path='./animalproof/'+ s1
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def applyvaccine1(request):
    con=connect()
    cursor=con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        hospid=row[1]
    s="select ownerid,ownername,hname,place,pin,phone,gender,district,email  from owner where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"applyvaccine1.html",{'records':records})

def applyvaccine2(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["t1"]
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

    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        hospid=row[1]
    s="select anno,anname,breed,age,ageunit,origin,regdate  from owneranimal where ownerid='" + s1 + "' and exist='Y'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"applyvaccine2.html",{'records':records,'s1':s1,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})

def applyvaccine3(request):
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
    s = "select vacname from vaccinebreed where anname='" + anname + "'"

    cursor.execute(s)
    records = cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])

    return render(request,"applyvaccine3.html",{'l':l,'anname':anname,'breed':breed,'age':age,'ageunit':ageunit,'origin':origin,'regdate':regdate,'s1':s1,'s2':s2,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})


def applyvaccine4(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["t1"]
    s2 = request.POST["t2"]
    s3=request.POST["c1"]


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
    s = "select * from vaccinebreed where vacname='" + s3 + "' and anname='" + anname + "'"

    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        age1 = row[2]
        ageunit1 = row[3]
        ndos1 = row[4]
        vqty1 = row[5]
        details1 = row[6]

    s = "select vacname from vaccinebreed where anname='" + anname + "'"

    cursor.execute(s)
    records = cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])
    s="select * from applyvaccine where ownerid='"+ s1 + "' and anno=" + s2 + " and vacname='"+ s3 +"'"
    cursor.execute(s)
    records11=cursor.fetchall()
    dosno=0
    for row in records11:
        dosno=dosno+1
    if dosno>=ndos1:
        possible=""
    else:
        possible="Yes"


    return render(request,"applyvaccine4.html",{'dosno':dosno,'possible':possible,'age1':age1,'ageunit1':ageunit1,'ndos1':ndos1,'vqty1':vqty1,'details1':details1,'l':l,'anname':anname,'breed':breed,'age':age,'ageunit':ageunit,'origin':origin,'regdate':regdate,'s1':s1,'s2':s2,'s3':s3,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})


def applyvaccine5(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["t1"]
    s2 = request.POST["t2"]
    s3=request.POST["c1"]


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
    s = "select * from vaccinebreed where vacname='" + s3 + "' and anname='" + anname + "'"

    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        age1 = row[2]
        ageunit1 = row[3]
        ndos1 = row[4]
        vqty1 = row[5]
        details1 = row[6]

    s = "select vacname from vaccinebreed where anname='" + anname + "'"

    cursor.execute(s)
    records = cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])
    s="select * from applyvaccine order by applyno desc"
    applyno=0
    cursor.execute(s)
    records11=cursor.fetchall()
    for row in records11:
        applyno=row[0]
        break
    applyno=applyno+1
    s="select * from session "
    cursor.execute(s)
    records11=cursor.fetchall()
    for row in records11:
        staffid=row[0]
    applydate=cdate()
    s="insert into applyvaccine values("+ str(applyno)+",'"+ s1 + "','" + s2 + "','"+ s3 + "','" + applydate + "','"+ staffid +  "')"
    cursor.execute(s)
    con.commit()

    s="select * from applyvaccine where ownerid='"+ s1 + "' and anno=" + s2 + " and vacname='"+ s3 +"'"
    cursor.execute(s)
    records11=cursor.fetchall()
    dosno=0
    for row in records11:
        dosno=dosno+1


    return render(request,"applyvaccine5.html",{'dosno':dosno,'applyno':applyno,'age1':age1,'ageunit1':ageunit1,'ndos1':ndos1,'vqty1':vqty1,'details1':details1,'l':l,'anname':anname,'breed':breed,'age':age,'ageunit':ageunit,'origin':origin,'regdate':regdate,'s1':s1,'s2':s2,'s3':s3,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})

def applyvaccineview1(request):
    con=connect()
    cursor=con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        hospid=row[1]
    s="select ownerid,ownername,hname,place,pin,phone,gender,district,email  from owner where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"applyvaccineview1.html",{'records':records})

def applyvaccineview2(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["t1"]
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

    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        hospid=row[1]
    s="select anno,anname,breed,age,ageunit,origin,regdate  from owneranimal where ownerid='" + s1 + "' and exist='Y'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"applyvaccineview2.html",{'records':records,'s1':s1,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})

def applyvaccineview3(request):
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

    return render(request,"applyvaccineview3.html",{'records22':records22,'anname':anname,'breed':breed,'age':age,'ageunit':ageunit,'origin':origin,'regdate':regdate,'s1':s1,'s2':s2,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})


def treatmentlist1(request):
    con=connect()
    cursor=con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        hospid=row[1]
    s="select ownerid,ownername,hname,place,pin,phone,gender,district,email  from owner where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"treatmentlist1.html",{'records':records})

def treatmentlist2(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["t1"]
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

    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        hospid=row[1]
    s="select anno,anname,breed,age,ageunit,origin,regdate  from owneranimal where ownerid='" + s1 + "' and exist='Y'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"treatmentlist2.html",{'records':records,'s1':s1,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})

def treatmentlist3(request):
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

    return render(request,"treatmentlist3.html",{'records22':records22,'anname':anname,'breed':breed,'age':age,'ageunit':ageunit,'origin':origin,'regdate':regdate,'s1':s1,'s2':s2,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})


def visitlist1(request):
    con=connect()
    cursor=con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        hospid=row[1]
    s="select ownerid,ownername,hname,place,pin,phone,gender,district,email  from owner where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"visitlist1.html",{'records':records})

def visitlist2(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["t1"]
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

    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        hospid=row[1]
    s="select anno,anname,breed,age,ageunit,origin,regdate  from owneranimal where ownerid='" + s1 + "' and exist='Y'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"visitlist2.html",{'records':records,'s1':s1,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})

def visitlist3(request):
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
    return render(request,"visitlist3.html",{'records22':records22,'anname':anname,'breed':breed,'age':age,'ageunit':ageunit,'origin':origin,'regdate':regdate,'s1':s1,'s2':s2,'ownername':ownername,'hname':hname,'place':place,'pin':pin,'phone':phone,'gender':gender,'district':district,'email':email})

def staffsignout(request):
    return render(request,"staffsignout.html")