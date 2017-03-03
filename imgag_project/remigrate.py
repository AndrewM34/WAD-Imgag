from os.path import join
from subprocess import Popen, DEVNULL, STDOUT
import glob

if __name__ == '__main__':
    PYTHON = "python"
    MANAGE_PY = "manage.py"
    RM = "rm"

    RM_DB_ARGS = [RM, "db.sqlite3"]
    RM_UPLOADED_FILES = [RM, "-rfv", "profile_images", "uploads"]
    RM_MIGRATIONS_ARGS = [RM] + glob.glob(join(join("imgag", "migrations"), "*.py"))
    MAKE_MIGRATE_ARGS = [PYTHON, MANAGE_PY, "makemigrations", "imgag"]
    MIGRATE_ARGS = [PYTHON, MANAGE_PY, "migrate"]
    CREATE_SUPER_USER_ARGS = [PYTHON, MANAGE_PY, "createsuperuser"]

    print("Removing DB...")
    p = Popen(RM_DB_ARGS, stdout=DEVNULL, stderr=STDOUT)
    p.communicate(input=None)
    print("Removing file from media/uploads and media/profile_images...")
    p = Popen(RM_UPLOADED_FILES, stdout=DEVNULL, stderr=STDOUT)
    p.communicate(input=None)
    print("Removing migrations...")
    p = Popen(RM_MIGRATIONS_ARGS, stdout=DEVNULL, stderr=STDOUT)
    p.communicate(input=None)
    print("Making migrations for imgag...")
    p = Popen(MAKE_MIGRATE_ARGS, stdout=DEVNULL, stderr=STDOUT)
    p.communicate(input=None)
    print("Migrating...")
    p = Popen(MIGRATE_ARGS, stdout=DEVNULL, stderr=STDOUT)
    p.communicate(input=None)

    print("There, you should now have clean DB (stdout of commands was sent to DEVNULL, so let's hope).")
