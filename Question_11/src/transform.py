from datetime import datetime

def transform_un_to_st(data):
    clean_doc={}

# ---------------- Simple fields ---------------------------

    clean_doc['Project_Id']=data.get('project_id','NA')
    clean_doc['Project_Name']=data.get('project_name','Unknown')
    clean_doc['Status']=data.get('status','NA')

# ----------------- Client -----------------------------

    Client=data.get('client',{})
    clean_doc['Name']=Client.get('name','Unknown')
    clean_doc['Industry']=Client.get('industry','Unknown')
    Client_loc=Client.get('location',{})
    clean_doc['City']=Client_loc.get('city','Unknown')
    clean_doc['Country']=Client_loc.get('country','Unknown')

# ----------------- Technologies -------------------- 

    tech=data.get('technologies',[])
    for i, t in enumerate(tech):
        clean_doc[f'tech_{i}']=t
            
# ------------------ Team ---------------------------

    Team=data.get('team',{})
    clean_doc['Project_Manager']=Team.get('project_manager','Unknown')

    Members=Team.get('members',[])
    for idx, member in enumerate(Members):     
        clean_doc[f'Member_Name_{idx}']=member.get('name','Unknown')
        clean_doc[f'Member_Role_{idx}']=member.get('role','NA')

# --------------------- Milestones -------------------

    Milestones=data.get('milestones',[])
    for index,mem in enumerate(Milestones):
        clean_doc[f'Milestones_Name_{index}']=mem.get('name','NA')
        date=mem.get('due_date')
        clean_doc[f'Milestones_Due_Date_{index}']=datetime.fromisoformat(date) if date else None

    return clean_doc