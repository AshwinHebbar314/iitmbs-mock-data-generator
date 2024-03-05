#%%
import random
from faker import Faker

fake = Faker('en_IN')

def random_blank(string):
    if random.random() < 0.8:
        return string
    else:
        return ''

def term():
    years = [
        '2021',
        '2022',
        '2023',
        '2024',
    ]
    terms = [
        't1',
        't2',
        't3',
    ]
    
    year = random.choice(years)
    
    output = year + random.choice(terms)

    return output

def name():
    return fake.name()

def email():
    years = [
        '21',
        '22',
        '23',
        '24',
    ]
    terms = [
        'f1',
        'f2',
        'f3',
    ]
    no = int(random.random()*1000//1)
    return f"{random.choice(years)}{random.choice(terms)}00{no:04d}@ds.study.iitm.ac.in"

def cgpa():
    return round(random.uniform(6, 10), 2)

def videourl():
    characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
    result = ''
    for _ in range(11):
        result += random.choice(characters)

    youtube_url = "https://www.youtube.com/watch?v=" + result
    return random_blank(youtube_url)

def profilepic():
    gender = [
        'men',
        'women'
    ]
    no = int(random.random()*100//1)
    url = f"https://randomuser.me/api/portraits/{random.choice(gender)}/{no}.jpg"
    return random_blank(url)

def public_profile_url():
    return random_blank(fake.url())

def project_url():
    # generate a fake gdrive link
    characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
    result = ''
    for _ in range(11):
        result += random.choice(characters)
    
    gdrive_url = "https://drive.google.com/file/d/" + result
    
    return random_blank(gdrive_url)

def domain_expertise():
    domains = [
        'Placement Cell',
        'Research',
        'Software Development',
        'Data Science',
    ]
    return random.choice(domains)
    
def description():
    return " ".join(fake.sentences(nb = 3))

def alum_email():    
    return fake.email()

def graduation_quote():
    quotes = [
        "I am grateful for the opportunities I received at IIT Madras.",
        "I am proud to be an IITian.",
        "I am grateful for the friends I made at IIT Madras.",
        "I am grateful for the faculty at IIT Madras.",
    ]
    
    return random_blank(random.choice(quotes))

class Topper:
    def __init__(self, term, name, email, cgpa, videourl, profilepic, public_profile_url):
        self.term = term
        self.name = name
        self.email = email
        self.cgpa = cgpa
        self.videourl = videourl
        self.profilepic = profilepic
        self.public_profile_url = public_profile_url

    def __str__(self):
        return f"{self.term} - {self.name} - {self.email} - {self.cgpa} - {self.videourl} - {self.profilepic} - {self.public_profile_url}"

    def to_dict(self):
        return {
            "term": self.term,
            "name": self.name,
            "email": self.email,
            "cgpa": self.cgpa,
            "videourl": self.videourl,
            "profilepic": self.profilepic,
            "public_profile_url": self.public_profile_url
        }
        
    def csv_entry(self):
        return f"{self.term},{self.name},{self.email},{self.cgpa},{self.videourl},{self.profilepic},{self.public_profile_url}"

class BestProject:
    def __init__(self, term, subject, name, email, cgpa, videourl, project_url, profilepic, public_profile_url):
        self.term = term
        self.subject = subject
        self.name = name
        self.email = email
        self.cgpa = cgpa
        self.videourl = videourl
        self.project_url = project_url
        self.profilepic = profilepic
        self.public_profile_url = public_profile_url
    
    def __str__(self):
        return f"{self.term} - {self.subject} - {self.name} - {self.email} - {self.cgpa} - {self.videourl} - {self.project_url} - {self.profilepic} - {self.public_profile_url}"
        
    def to_dict(self):
        return {
            "term": self.term,
            "subject": self.subject,
            "name": self.name,
            "email": self.email,
            "cgpa": self.cgpa,
            "videourl": self.videourl,
            "project_url": self.project_url,
            "profilepic": self.profilepic,
            "public_profile_url": self.public_profile_url
        }
        
    def csv_entry(self):
        return f"{self.term},{self.subject},{self.name},{self.email},{self.cgpa},{self.videourl},{self.project_url},{self.profilepic},{self.public_profile_url}"
        
class TeachingAssistant:
    def __init__(self, term, subject, name, email, profilepic, public_profile_url):
        self.term = term
        self.subject = subject
        self.name = name
        self.email = email
        self.profilepic = profilepic
        self.public_profile_url = public_profile_url
    
    # should follow the same order as the __init__ method
    def __str__(self):
        return f"{self.term} - {self.subject} - {self.name} - {self.email} - {self.profilepic} - {self.public_profile_url}"
    
    def to_dict(self):
        return {
            "term": self.term,
            "subject": self.subject,
            "name": self.name,
            "email": self.email,
            "profilepic": self.profilepic,
            "public_profile_url": self.public_profile_url
        }
    
    def csv_entry(self):
        return f"{self.term},{self.subject},{self.name},{self.email},{self.profilepic},{self.public_profile_url}"
    
class Intern:
    def __init__(self, term, domain, name, email, cgpa, profilepic, public_profile_url, description):
        self.term = term
        self.domain = domain
        self.name = name
        self.email = email
        self.cgpa = cgpa
        self.profilepic = profilepic
        self.public_profile_url = public_profile_url
        self.description = description
    
    def __str__(self):
        return f"{self.term} - {self.domain} - {self.name} - {self.email} - {self.cgpa} - {self.profilepic} - {self.public_profile_url} - {self.description}"
    
    def to_dict(self):
        return {
            "year": self.term[:4],
            "term": self.term,
            "domain": self.domain,
            "name": self.name,
            "email": self.email,
            "cgpa": self.cgpa,
            "profilepic": self.profilepic,
            "public_profile_url": self.public_profile_url,
            "description": self.description
        }
        
    def csv_entry(self):
        return f"{self.term[:4]},{self.term},{self.domain},{self.name},{self.email},{self.cgpa},{self.profilepic},{self.public_profile_url},{self.description}"
       
class Alumni:
    def __init__(self, name, email, alum_email, cgpa, profilepic, public_profile_url, graduation_quote):
        self.name = name
        self.email = email
        self.alum_email = alum_email
        self.cgpa = cgpa
        self.profilepic = profilepic
        self.public_profile_url = public_profile_url
        self.graduation_quote = graduation_quote
        
    def __str__(self):
        return f"{self.name} - {self.email} - {self.alum_email} - {self.cgpa} - {self.profilepic} - {self.public_profile_url} - {self.graduation_quote}"
    
    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "alum_email": self.alum_email,
            "cgpa": self.cgpa,
            "profilepic": self.profilepic,
            "public_profile_url": self.public_profile_url,
            "graduation_quote": self.graduation_quote
        }
        
    def csv_entry(self):
        return f"{self.name},{self.email},{self.alum_email},{self.cgpa},{self.profilepic},{self.public_profile_url},{self.graduation_quote}"

subjects = {'cs2003p': "MAD1",
            'cs2006p': "MAD2",
            'cs2008p': "MLP",
            'ms2001p': "BDM",
        }


# generate 100 toppers and save it as a csv file with same headers as the class


# %%
toppers = []
for _ in range(25):
    toppers.append(Topper(term(), name(), email(), cgpa(), videourl(), profilepic(), public_profile_url()))

with open('toppers.csv', 'w') as f:
    f.write("term,name,email,cgpa,videourl,profilepic,public_profile_url\n")
    for topper in toppers:
        f.write(topper.csv_entry() + "\n")

# for each subject, generate 25 best projects and save it as a csv file with same headers as the class, each subject should have it's own csv file with the file name as the best_project_subjectcode.csv

for subject in subjects:
    best_projects = []
    for _ in range(25):
        best_projects.append(BestProject(term(), subjects[subject], name(), email(), cgpa(), videourl(), project_url(), profilepic(), public_profile_url()))
    
    with open(f'best_project_{subject}.csv', 'w') as f:
        f.write("term,subject,name,email,cgpa,videourl,project_url,profilepic,public_profile_url\n")
        for best_project in best_projects:
            f.write(best_project.csv_entry() + "\n")

# generate 25 teaching assistants and save it as a csv file with same headers as the class
tas = []
for _ in range(25):
    tas.append(TeachingAssistant(term(), random.choice(list(subjects.values())), name(), email(), profilepic(), public_profile_url()))
    
with open('teaching_assistants.csv', 'w') as f:
    f.write("term,subject,name,email,profilepic,public_profile_url\n")
    for ta in tas:
        f.write(ta.csv_entry() + "\n")

# generate 25 interns and save it as a csv file with same headers as the class
interns = []
for _ in range(25):
    interns.append(Intern(term(), domain_expertise(), name(), email(), cgpa(), profilepic(), public_profile_url(), description()))
    
with open('interns.csv', 'w') as f:
    f.write("term,domain,name,email,cgpa,profilepic,public_profile_url,description\n")
    for intern in interns:
        f.write(intern.csv_entry() + "\n")
        
# generate 50 alumni and save it as a csv file with same headers as the class
alumnis = []
for _ in range(50):
    alumnis.append(Alumni(name(), email(), alum_email(), cgpa(), profilepic(), public_profile_url(), graduation_quote()))

with open('alumni.csv', 'w') as f:
    f.write("name,email,alum_email,cgpa,profilepic,public_profile_url,graduation_quote\n")
    for alumni in alumnis:
        f.write(alumni.csv_entry() + "\n")
# %%
# %%
tas = []
for _ in range(100):
    tas.append(TeachingAssistant(term(), random.choice(list(subjects.values())), name(), email(), profilepic(), public_profile_url()))
    
with open('teaching_assistants.csv', 'w') as f:
    f.write("term,subject,name,email,profilepic,public_profile_url\n")
    for ta in tas:
        f.write(ta.csv_entry() + "\n")
# %%
interns = []
for _ in range(50):
    interns.append(Intern(term(), domain_expertise(), name(), email(), cgpa(), profilepic(), public_profile_url(), description()))

with open('interns.csv', 'w') as f:
    f.write("year,term,domain,name,email,cgpa,profilepic,public_profile_url,description\n")
    for intern in interns:
        f.write(intern.csv_entry() + "\n")
# %%
