STEP 1 - 
cd employee_crud


STEP 2 - 
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser


STEP 3 - 
On Windows (Command Prompt):
venv\Scripts\activate

On Windows (PowerShell):
.\venv\Scripts\Activate


STEP 4 - 
pip install django mysqlclient


STEP 5 - 
python manage.py makemigrations
python manage.py migrate


Step 6 - 
Create Superuser (for Django Admin)
python manage.py createsuperuser


Step 7 - 
Run Server
python manage.py runserver