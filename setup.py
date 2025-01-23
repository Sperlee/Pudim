import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup( 
    name = "Pudim Game",
    options = {'build_exe': {'packages': ['pygame'],
                            'include_files':['assets','Classes','fases','fontes','imagens','sprites','BaseClass.py','Lake Jupiter - John Patitucci (online-audio-converter.com).ogg','main.py','MenuClass.py','PerformanceClass.py','PlayClass.py','Transition.py','utils.py']}},
    executables = executables
)