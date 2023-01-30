import os

try:
    os.system('cmd /k "cd.."')
except:
    print('error')

try:
    os.system('cmd /k "app\\Scripts\\activate.bat"')
except:
    print('error')

try:
    os.system('cmd /k "pip install django"')
except:
    print('error')

try:
    os.system('cmd /k "cd proiect_comun"')
except:
    print('error')

try:
    os.system('cmd /k "py manage.py runserver"')
except:
    print('error')