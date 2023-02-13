class Test:
    def get_header_file_header_title(self) -> bool:
        """ Check and get if the title of the header of the header file has changed """
            for i in range(self.argc):
                if (("-ht" == self.argv[i].lower()) and (i+1 <= self.argc-1)):
                    if (self.argv[i+1][0] != '-'):
                        self.headerfile_options["header_name"] = self.argv[i+1]
                        # self.headerfile_header_title = self.argv[i+1]
                        return True
        return False
