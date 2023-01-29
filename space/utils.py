import os
def NotesPath(instance, filename):
    return os.path.join(
        "%s" % instance.branch_name, "sem_" "%s" %instance.semester , "%s" % instance.pdf_file)
def ArticlePath(instance, filename):
    return os.path.join(
      "University Updates"  "%s" % instance.headline , "%s" % instance.dp_image)
def PyqPath(instance, filename):
    return os.path.join(
        "%s" % instance.branch_name,  "sem_" "%s" %instance.semester , "Previous Year Question" , "%s" % instance.pdf_file)