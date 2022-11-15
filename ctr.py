# _____________________________________________________________________________________________________________________________________________________________ #
#                                                                                                                                                               #
#        ________      _________                   ________      _______       _____ ______       ________      ___      ___  _______       ________            #   
#       |\   ____\    |\___   ___\                |\   __  \    |\  ___ \     |\   _ \  _   \    |\   __  \    |\  \    /  /||\  ___ \     |\   __  \           #    
#       \ \  \___|    \|___ \  \_|  ____________  \ \  \|\  \   \ \   __/|    \ \  \\\__\ \  \   \ \  \|\  \   \ \  \  /  / /\ \   __/|    \ \  \|\  \          #  
#        \ \  \            \ \  \  |\____________\ \ \   _  _\   \ \  \_|/__   \ \  \\|__| \  \   \ \  \\\  \   \ \  \/  / /  \ \  \_|/__   \ \   _  _\         # 
#         \ \  \____        \ \  \ \|____________|  \ \  \\  \|   \ \  \_|\ \   \ \  \    \ \  \   \ \  \\\  \   \ \    / /    \ \  \_|\ \   \ \  \\  \|        #
#          \ \_______\       \ \__\                  \ \__\\ _\    \ \_______\   \ \__\    \ \__\   \ \_______\   \ \__/ /      \ \_______\   \ \__\\ _\        #
#           \|_______|aption  \|__|ext                \|__|\|__|    \|_______|    \|__|     \|__|    \|_______|    \|__|/        \|_______|    \|__|\|__|       #
#                                                                                                                                                               #
# _____________________________________________________________________________________________________________________________________________________________ #

from system import utils as u
import system.ctr_S as s
import typer
#################################################################################################################################################################


class main():

    # Start Script
    app = typer.Typer()

    # Open help
    @app.command()
    def help():
        typer.echo(u.help)

    # Get the current version
    @app.command()
    def version():
        typer.echo(f"{u.prefix} CaptionTextRemover version : {u.version}")

    # Learn more about CaptionTextRemover
    @app.command()
    def about():
        typer.echo(u.about)

    # Learn more about CaptionTextRemover
    @app.command()
    def credits():
        typer.echo(u.credits)

    # Start the CTR execution with your image and rgba color estimation
    @app.command()
    def run(img: str, r: int, g: int, b: int, a:int, value_correction:int):
        alpha = (a+value_correction)
        rgba = r,g,b,-alpha
        s.run(img, rgba)
        
    # Start the CTR execution with your image and rgba color estimation
    @app.command()
    def run_extra(img: str, r: int, g: int, b: int, a:int, value_correction:int, tv1:int, mv1:int, ip1:int, tv2:int, mv2:int, sz:int, ip2:int):
        alpha = (a+value_correction)
        rgba = r,g,b,-alpha
        s.run_extra(img, rgba, tv1, mv1, ip1, tv2, mv2, sz, ip2)

    # init app
    if __name__ == "__main__":
        app()