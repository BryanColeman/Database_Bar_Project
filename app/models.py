from app import login


@login.user_loader
def load_user(id):
    print('temp')
    #query db to load user