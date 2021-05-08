

from django.core.management import call_command
import glob, os, os.path
from django.conf import settings
import logging

logger = logging.getLogger("book.task")

def DB_backup_job():
    try:
        filelist = glob.glob(os.path.join(settings.DBBACKUP_STORAGE_OPTIONS["location"]))

        for f in os.listdir(settings.DBBACKUP_STORAGE_OPTIONS["location"]):
            logger.info(settings.DBBACKUP_STORAGE_OPTIONS["location"]+f)
            os.remove(settings.DBBACKUP_STORAGE_OPTIONS["location"]+f)
        call_command("dbbackup")

    except Exception as e :
        logger.info("Error")
        logger.info(str(e))
        pass
