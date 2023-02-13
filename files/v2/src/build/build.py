##
## EPITECH PROJECT, 2022
## v2
## File description:
## build.py
##

class Build:
    """ The build class of the build section of the program """
    def __init__(self) -> None:
        self.data_build = "ee"

    def makefile_appearance(self):
        """ Create the appearance of the makefile """
        res = list()
        res.append("##")
        res.append("## EPITECH PROJECT, 2022")
        res.append("## v2")
        res.append("## File description:")
        res.append("## build.py")
        res.append("##")
        return res
    
    def usr_options(self, argv:list[str], existing:list[str]) -> dict[str:bool]:
        """ Get the options from the user """
        res = dict()
        for i in enumerate(argv):
            if i[1] in existing:
                res[i[1]] = True
            else:
                res[i[1]] = False
        # res["-h"] = False
        # res["-f"] = False
        # res["-d"] = False
        # res["-l"] = False
        # res["-i"] = False
        # res["-c"] = False
        # res["-t"] = False
        # res["-o"] = False
        # res["-g"] = False
        # res["-s"] = False
        # res["-a"] = False
        # res["-e"] = False
        # res["-r"] = False
        # res["-p"] = False
        # res["-u"] = False
        # res["-m"] = False
        # res["-n"] = False
        # res["-b"] = False
        # res["-v"] = False
        # res["-w"] = False
        # res["-x"] = False
        # res["-y"] = False
        # res["-z"] = False
        # res["-q"] = False
        # res["-j"] = False
        # res["-k"] = False
        return res
