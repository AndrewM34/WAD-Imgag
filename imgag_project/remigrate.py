from os.path import join, exists
from os import remove
from subprocess import Popen
import glob
import shutil

if __name__ == '__main__':
    PYTHON = "python"
    MANAGE_PY = "manage.py"

    DB_PATH = "db.sqlite3"
    UPLOADED_FILE_PATHS = [join("media", folder) for folder in ["profile_images", "uploads", "category_images"]]
    MIGRATIONS_PATH = join("imgag", "migrations")
    MAKE_MIGRATE_ARGS = [PYTHON, MANAGE_PY, "makemigrations", "imgag"]
    MIGRATE_ARGS = [PYTHON, MANAGE_PY, "migrate"]

    print("Removing DB...")
    if exists(DB_PATH):
        remove(DB_PATH)
    print("Removing file from media/uploads,media/profile_images and media/categories...")
    for folder_to_delete in UPLOADED_FILE_PATHS:
        if exists(folder_to_delete):
            shutil.rmtree(folder_to_delete)
    print("Removing migrations...")
    if exists(MIGRATIONS_PATH):
        shutil.rmtree(MIGRATIONS_PATH)
    print("Making migrations for imgag...")
    p = Popen(MAKE_MIGRATE_ARGS)
    p.communicate(input=None)
    print("Migrating...")
    p = Popen(MIGRATE_ARGS)
    p.communicate(input=None)

    print("There, you should now have clean DB.")
