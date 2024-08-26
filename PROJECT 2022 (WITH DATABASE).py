import mysql.connector as m
mycon=m.connect(host="localhost",user="root",passwd="admin",database="travel")
if mycon.is_connected():
    print("Connected")
f=mycon.cursor()
f.execute("create table Places(Sno char(10) primary key,Category Varchar(30), State VARCHAR(30), Destinations VARCHAR(100), Info char(255))")
f.execute("insert into Places values('01','Mountains','Uttrakhand','Roopkund Lake,','With a depth of about 3 meters, Roopkund is widely known for the hundreds of ancient human skeletons found at the edge of the lake. The human skeletal remains are visible at its bottom when the snow melts.')")
f.execute("insert into Places values('03','Mountains','Kashmir','Gulmarg,','Gulmarg is interpreted as meadow of flowers')")
f.execute("insert into Places values('02','Mountains','Himachal Pradesh','Khajjiar,','In 1992, Swiss Envoy Willy P. Blazer, Vice Counselor and Head of Chancery of Switzerland in India brought Khajjiar on the world tourism map by calling it, Mini Switzerland.')")
f.execute("insert into Places values('04','Mountains','Karnataka','Sirsi,','The town is surrounded by forest, and the region has a number of waterfalls')")
f.execute("insert into Places values('05','Mountains','Kerala','Munnar,','Munnar is called the, Kashmir of South India. The name Munnar is believed to mean, three rivers, referring to its location at the confluence of the Mudhirapuzha, Nallathanni and Kundali rivers.')")
f.execute("insert into Places values('06','Forests','Kochi','Athirapally,','Athirapally falls were featured in film Dil Se.. by Mani Ratnam, starring Shahrukh Khan, Manisha Koirala, and Preity Zinta, and featuring the song, Jiya Jale')")
f.execute("insert into Places values('07','Forests','Andra Pradesh','Nallamala Hills,','The Nallamala Forests are probably the largest stretch of undisturbed forest in South India apart from the Western Ghats and were particularly rich in game till the 1970s')")
f.execute("insert into Places values('08','Forests','Karnataka','Shettihalli,','It is said that a mixture of jaggery and eggs was also used in building the Rosary Church, and during monsoons, the entire church is submerged in water and once the water recedes, the church can be seen in its full glory.')")
f.execute("insert into Places values('09','Forests','Jharkhand','Saranda Forest,','Saranda is largest Sal Forest of Asia and pride of Jharkhand. An un-spoilt world, where nature rules supreme, it is the home of the endangered flying lizard')")
f.execute("insert into Places values('10','Beaches','Kerala','Varkala,','The beach is famous for its natural springs which are said to have medicinal qualities. The 2000-year-old Janardhanaswamy Temple along with the Sivagiri Mutt attract a steady stream of visitors all year long.')")
f.execute("insert into Places values('11','Beaches','Karnataka','Gakarna,','Besides the captivating beauty, the beach has gained popularity as a famed surfing and trekking site. You can enjoy a plethora of exciting activities and water sports at Gokarna Beach to make the most out of your trip.')")
f.execute("insert into Places values('12','Beaches','Kerala','Kovalam,','Kovalam is famous for its beaches, among the most pristine in India. Kovalam is extremely popular among westerners due to shallow waters and low tidal waves. ')")
f.execute("insert into Places values('13','Islands','Kerala','Munroe Island,','Munroe Island is a hidden pearl in the backwaters which is composed of a cluster of 8 islands. Each of them is separated by small water channels and lakes')")
f.execute("insert into Places values('14','Islands','Assam','Majuli,','It is the largest river island of the world and it attracts tourists from all over the world. Majuli is also a strong contender for a place in the World Heritage Sites of the UNESCO.')")
mycon.commit()
print("Record added")

f.execute("create table Movies(Sno char(10) primary key, Genre VARCHAR(30), Name Varchar(100), Link char(254))")
f.execute("insert into Movies values('01','Adventure','Journey 2:The Mysterious Island ','https://sflix.pro/movie/journey-2-the-mysterious-island-zpwl/1-full')")
f.execute("insert into Movies values('02','Adventure','Jumanji: Next Level','https://sflix.pro/movie/jumanji-the-next-level-0q9q7/1-full')")
f.execute("insert into Movies values('03','Adventure','Charlies Angels','https://sflix.pro/movie/charlies-angels-zxw2p/1-full')")
f.execute("insert into Movies values('04','Comedy','Oceans 8','https://sflix.pro/movie/oceans-8-l37lm/1-full')")
f.execute("insert into Movies values('05','Comedy','Baywatch','https://sflix.pro/movie/baywatch-jvmq4/1-full')")
f.execute("insert into Movies values('06','Comedy','Hera Pheri','https://www.youtube.com/watch?v=TIQ5hrfermg')") 
f.execute("insert into Movies values('07','Comedy','Bhagam Bhag','https://www.youtube.com/watch?v=zloKjQXmwhE')")
f.execute("insert into Movies values('08','Horror','The Conjuring','https://sflix.pro/movie/the-conjuring-91wq/1-full')")
f.execute("insert into Movies values('09','Horror','It','https://sflix.pro/movie/it-5kkom/1-fullhd')")
f.execute("insert into Movies values('10','Horror','Insidious','https://sflix.pro/movie/insidious-qjkw/1-full')")
f.execute("insert into Movies values('11','Action','Avengers:Infinity War','https://sflix.pro/movie/avengers-infinity-war-z12k2/1-full')")
f.execute("insert into Movies values('12','Action','Kingsman: The Secret Service','https://sflix.pro/movie/kingsman-the-secret-service-9218/1-full')")
mycon.commit()
print("Record added")

f.execute("create table Songs(Sno char(10) primary key, Category varchar(30), Singer Varchar(30), Name varchar(50), Link char(254))")
f.execute("insert into Songs values('01','International pop','Jaymes','Infinity','https://www.youtube.com/watch?v=Co72yW9C_Uw')")
f.execute("insert into Songs values('02','International pop','Katy Pery','Harleys in Hawaii','https://www.youtube.com/watch?v=sQEgklEwhSo')")
f.execute("insert into Songs values('03','International pop','Glass Animals','Heat waves','https://www.youtube.com/watch?v=mRD0-GxqHVo')")
f.execute("insert into Songs values('04','International pop','Ed Sheeran','Shivers','https://www.youtube.com/watch?v=Il0S8BoucSA')")
f.execute("insert into Songs values('05','Bollywood','OAFF','Doobey','https://www.youtube.com/watch?v=6eGCi4SVy94')")
f.execute("insert into Songs values('06','Bollywood','A.R. Rehman','Rait Zara si','https://www.youtube.com/watch?v=U-oThzLxFck')")
f.execute("insert into Songs values('07','Bollywood','Priya Saraiya','Kalle Kalle','https://www.youtube.com/watch?v=raPwjc8br1U')")
f.execute("insert into Songs values('08','Bollywood','Javed Ali','Srivalli','https://www.youtube.com/watch?v=hcMzwMrr1tE')")
f.execute("insert into Songs values('09','Indie music','Aditya A','Chand Baaliyan','https://www.youtube.com/watch?v=7c3-Gei5j4w')")
f.execute("insert into Songs values('10','Indie music','Kavita','Rang Sari','https://www.youtube.com/watch?v=jY8mAWdQFOA')")
mycon.commit()
print("Record added")

f.execute("create table Recipies(Name varchar(30) primary key, Ingredients char(254), Recipe char(254))")
f.execute("insert into Recipies values('Bhel Puri','1. Fatafat Bhel(Haldiram)or any chips,2. An onion,3. A tomato,4. Cheese(optional),5. Boiled eggs(optional)','1. Chop the onion tomato and boiled egg, 2. Add them in the packet,3. Grate cheese at the top,4. Mix well')")
f.execute("insert into Recipies values('Omellete ','1. Eggs(as per requirement),2. Electric kettle,3. Some oil/Butter','1. Wisk the eggs,2. Grease the kettle,3. pour the eggs in portions,4. Cook each side')")
f.execute("insert into Recipies values('Boiled eggs ','1. Eggs(as per requirement),2. Water,3. Electric Kettle','1. Fill the kettle with water,2. Place the eggs (take care of the maximum water level mentioned in the kettle),3. Boil for 10-13 mins,4. Keep checking them')")
mycon.commit()

f.execute("create table Menu(Sno char(10) primary key, Category varchar(30), Name Varchar(100), Estimated_Time char(254), foreign key(Name) references Recipies(Name))")
f.execute("insert into Menu values('01','Sweet&Savoury','Bhel Puri','3 min ')")
f.execute("insert into Menu values('02','Savoury','Omellete','15 min ')")
f.execute("insert into Menu values('03','Savoury','Boiled eggs','5 min ')")
mycon.commit()
print("Record added")

def enterplaces():
    n=int(input("Enter the no of records to be added"))
    for i in range(n):
        f.execute("select*from Places order by Sno asc")
        q=f.fetchall()
        s=len(q)+1
        c=input("Enter the category")
        st=input("Enter the state")
        d=input("Enter the destination")
        i=input("Enter the information(not more than 250 characters")
        values=(s,c,st,d,i)
        c="INSERT INTO Places VALUES(%s,%s,%s,%s,%s)"
        f.execute(c,values)
        mycon.commit()
    print("Record added")
def entermovies():
    n=int(input("Enter the no of records to be added"))
    for i in range(n):
        f.execute("select*from movies order by Sno asc")
        q=f.fetchall()
        s=len(q)+1
        nm=input("Enter the name")
        g=input("Enter the genre ")
        l=input("Enter the link ")
        values=(s,g,nm,l)
        c="INSERT INTO Movies VALUES(%s,%s,%s,%s)"
        f.execute(c,values)
        mycon.commit()
    print("Record added")
def entersongs():
    n=int(input("Enter the no of records to be added"))
    for i in range(n):
        f.execute("select*from songs order by Sno asc")
        q=f.fetchall()
        sn=len(q)+1
        c=input("Enter the category ")
        s=input("Enter the singer ")
        nm=input("Enter the name ")
        l=input("Enter the link ")
        values=(sn,c,s,nm,l)
        c="INSERT INTO Songs VALUES(%s,%s,%s,%s,%s)"
        f.execute(c,values)
        mycon.commit()
    print("Record added")
def enterrecipes():
    n=int(input("Enter the no of records to be added "))
    for i in range(n):
        f.execute("select*from menu order by Sno asc")
        q=f.fetchall()
        s=len(q)+1
        ca=input("Enter the category ")
        nm=input("Enter the name ")
        e=input("Enter the Estimated time ")
        ing=input("Enter the ingredients with serial numbers and seperate them using commas(,)")
        rec=input("Enter the recipe steps with serial numbers and separate them using commas(,)")
        val=(nm,ing,rec)
        c="INSERT INTO Recipies VALUES(%s,%s,%s);"
        f.execute(c,val)
        values=(s,ca,nm,e)
        c="INSERT INTO Menu VALUES(%s,%s,%s,%s);"
        f.execute(c,values)
        mycon.commit()
    print("Record added")
ans='yes'
ww=0
while ans in 'yes,Yes,yEs,yeS,YEs,yES,YeS,YES':
    if ww<1:
        print('''_____________________________________________________________________________________________________________________________________________________________________TRAVELLER's ASSISTANT__________________________________________________________________________________________________________________________________________________________________
    ''')
    print("_____________________________________________________________________________________________________________________")
    print('''                                                                                                    COURSE OF ACTION
_____________________________________________________________________________________________________________________''')
    p=int(input('''                                                                                                  What do you wish to do?
                                                    1.Add on                                                                                           2.Take a tour 
                                                                                                                   '''))
    print("_____________________________________________________________________________________________________________________")
    if p==1:
        t=int(input('''
                1.Places                                             2.Movies                                                          3.Songs                                             4.Recipies
                
What would you like to update?'''))
        if t==1:
            enterplaces()
        elif t==2:
            entermovies()
        elif t==3:
            entersongs()
        elif t==4:
            enterrecipes()
        else:
            print("Inappropriate input")
    elif p==2:
        print("_____________________________________________________________________________________________________________________")
        print('''                                                                                        WHAT  YOU HAVE IN MIND?
                    1.Places                                                                     2.Entertaintment                                                                     3.Recipies
        ''')
        x=int(input("Enter the desired option number: "))
        print()
        zz=0
        if x==1:
            if zz<1:
                print('''_____________________________________________________________________________________________________________________

                                        There are bound to be some unexplored secrets waiting to be unraveled and discovered.
                            India has tons of secrets buried deep in some bizarre places, most of which will leave you awestruck
                                                                        and with an unquenchable thirst for learning more.
        We have listed some of these mysterious places in India here that are worth a visit if your inner detective is already stirring up!\n''')
            print('''_____________________________________________________________________________________________________________________''')
            print('''
                                                                                                                OPTIONS
        1.Mountain areas                                      2. Beaches                                                    3. Islands                                                     4. Forests
        ''')
            s=input("Which kind of place would you like to visit?:  ")
            print('''_____________________________________________________________________________________________________________________
                                                                                         SUGGESTED DESTINATIONS''')
    
            if s=="1":
                f.execute("select*from Places ")
                q=f.fetchall()
                n=0
                for i in q:
                    if i[1] in 'mountains,Mountains':
                        n+=1
                        print('''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
                        print(n,i[3],i[2])
                        print('''
''',i[4],'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
            elif s=="2":
                f.execute("select*from Places ")
                q=f.fetchall()
                n=0
                for e in q:
                    if e[1] in 'beaches     ,Beaches     ':
                        n+=1
                        print('''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
                        print(n,e[3],e[2])
                        print('''
''',e[4],'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
            elif s=="3":
                f.execute("select*from Places ")
                q=f.fetchall()
                n=0
                for e in q:
                    if e[1] in 'islands,Islands':
                        n+=1
                        print('''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
                        print(n,e[3],e[2])
                        print('''
''',e[4],'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
            elif s=="4":
                f.execute("select*from Places ")
                q=f.fetchall()
                n=0
                for e in q:
                    if e[1] in 'forests,Forests':
                        n+=1
                        print('''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
                        print(n,e[3],e[2])
                        print('''
''',e[4],'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
            else:
                print("Inappropriate input")
        elif x==2:
            print("_____________________________________________________________________________________________________________________")
            print('''                                                                                                            OPTIONS
                                                                    1.Movies                                                                                        2.Songs
  [Please copy the link and paste it in the browser for watching your desired movies or song from the list of options that are provided]''')
            w=int(input("What would you like?: "))
            if w==1:
                print("_____________________________________________________________________________________________________________________")
                print('''
                                                                                                                OPTIONS
        1. Adventure                                      2. Comedy                                                    3. Horror                                                     4. Action
        ''')
                s=int(input("Which genre do you feel like watching?: "))
                print("_____________________________________________________________________________________________________________________")
                if s==1:
                    f.execute("select*from Movies")
                    q=f.fetchall()
                    print("         S.no.      Genre                          Name                                                                   Link")
                    for i in q:
                        if i[1] in 'Adventure':
                            print("         ",i[0],"  ",i[1],i[2],i[3])
                elif s==2:
                    f.execute("select*from Movies")
                    q=f.fetchall()
                    print("  S.no.      Genre               Name                                                                   Link")
                    for i in q:
                        if i[1] in 'Comedy':
                            print("  ",i[0],"       ",i[1],i[2],i[3])
                elif s==3:
                    f.execute("select*from Movies")
                    q=f.fetchall()
                    print("  S.no.      Genre                          Name                                                                   Link")
                    for i in q:
                        if i[1] in 'Horror':
                            print("  ",i[0],"      ",i[1],i[2],i[3])
                elif s==4:
                    f.execute("select*from Movies")
                    q=f.fetchall()
                    print("  S.no.    Genre                          Name                                                                   Link")
                    for i in q:
                        if i[1] in 'Action':
                            print("  ",i[0],"    ",i[1],i[2],i[3])
            elif w==2:
                print("_____________________________________________________________________________________________________________________")
                print('''
                                                                                                                OPTIONS
               1. International Pop                                                           2. Bollywood                                                          3. Indie Music                          
        ''')
                s=int(input("Which genre do you feel like listening?: "))
                print("_____________________________________________________________________________________________________________________")
                if s==1:
                    f.execute("select*from Songs")
                    q=f.fetchall()
                    print("  S.no.      Category                   Singer                               Song name                                                          Link")
                    for i in q:
                        if i[1] in 'International pop,international pop':
                            print("  ",i[0],"         ",i[1],"     ",i[2],"       ",i[3],"        ",i[4])
                elif s==2:
                    f.execute("select*from Songs")
                    q=f.fetchall()
                    print("  S.no.      Category                 Singer                               Song name                                                          Link")
                    for i in q:
                        if i[1] in 'Bollywood':
                            print("  ",i[0],"         ",i[1],"     ",i[2],"       ",i[3],"        ",i[4])
                elif s==3:
                    f.execute("select*from Songs")
                    q=f.fetchall()
                    print("  S.no.      Category                 Singer                               Song name                                                          Link")
                    for i in q:
                        if i[1] in 'Indie music':
                            print("  ",i[0],"         ",i[1],"     ",i[2],"       ",i[3],"        ",i[4])
        elif x==3:
            print("_____________________________________________________________________________________________________________________")
            print('''                                                                                                          OPTIONS
                                           1.Savoury                                                 2.Sweet                                                        3.Sweet&Savoury                                                                     
        ''')
            s=int(input("What would you like to eat?: "))
            print()
            if s==1:
                f.execute("select*from menu")
                q=f.fetchall()
                n=0
                for i in q:
                    if i[1] in 'Savoury':
                        n+=1
                        print('''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
                        print(n,i[2].upper(),i[3])
                    f.execute("select*from Recipies")
                    y=f.fetchall()
                    for j in y:
                        if j[0]==i[2]:
                            print('''
Ingredients
''',j[1],'''
Recipe
''',j[2],'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
            elif s==2:
                f.execute("select*from menu")
                q=f.fetchall()
                n=0
                for i in q:
                    if i[1] in 'Sweet':
                        n+=1
                        print('''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
                        print(n,i[2].upper(),i[3])
                        f.execute("select*from recipies")
                        y=f.fetchall()
                        for j in y:
                            if j[0]==i[2]:
                                print('''
Ingredients
''',j[1],'''
Recipe
''',j[2],'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
            elif s==3:
                f.execute("select*from menu")
                q=f.fetchall()
                n=0
                for i in q:
                    if i[1] in 'Sweet&Savoury':
                        n+=1
                        print('''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
                        print(n,i[2].upper(),i[3])
                        f.execute("select*from recipies")
                        y=f.fetchall()
                        for j in y:
                            if j[0]==i[2]:
                                print('''
Ingredients
''',j[1],'''
Recipe
''',j[2],'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
    print("_____________________________________________________________________________________________________________________")
    ans=input("Do you wish to continue?(yes/no) ")
    ww+=1
else:
    print('''_____________________________________________________________________________________________________________________________________________________________________THANK YOU___________________________________________________________________________________________________________________________________________________________________________''')



        



    
