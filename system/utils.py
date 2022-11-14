from datetime import datetime


author  = "YP522"
email   = "yp@ypetit.web-edu.fr"
version = "0.0.0"
prefix  = "[CTR]"
line    = "#######################################################################################"
good    = "[√]"
bad     = "[X]"
errors  = ["File Not found", "Not the same size"]

slogan = "One pixel can hide another"

#                                   TIME                                      #
now = datetime.now()
day = now.strftime("%d:%m:%Y")
time = now.strftime("%H:%M:%S")
dt_string = "output/"+now.strftime("%d-%m-%Y-%H-%M-%S")

#                                   CMDS                                      #


def log(elt):
    return print(f"{prefix} {elt}")


credits = f"{prefix} Create by {author}"


help = f"""
{line}
                  CaptionTextRemover {version} » HELP | What can I do to help you ?
{line}
    - help    : Get help for execute commands of CaptionTextRemover               {prefix}
    - version : Get current version of CaptionTextRemover                         {prefix}
    - about   : What is CaptionTextRemover ?                                      {prefix}
    - credits : Get current authors of CaptionTextRemover                         {prefix}
    - run [img] [alpha] : Run the caption text remover                            {prefix}
    - run-extra [img] [alpha] [...] : Run the caption text remover with options   {prefix}    
{line}
"""

about = f"""
{line}
                  CaptionTextRemover {version} » About | What is CaptionTextRemover  ?
{line}
    CaptionTextRemover is a free python project for "remove" a caption-text from a picture.

{line}
Credits : {credits}
"""