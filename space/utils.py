import os
def NotesPath(instance, filename):
    return os.path.join(
        "%s" % instance.branch_name, "sem_" "%s" %instance.semester , "%s" % instance.pdf_file)