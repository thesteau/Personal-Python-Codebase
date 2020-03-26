# By Steven Au

import pathlib as pl
import platform as pf

def pathing_library_mojo(some_file, file_convert='csv'):
    """ Parse the file string and extract all necessawry elements to breakdown and conert a file to a desired format name.
        Note: This function's purposes is only taking an input file and return the original path and newly converted file path
        Parameters:
            OPTIONAL File_convert
                csv is the default file extension. For any other file extensions, just add what is needed
                Note:
                    Do not add a "." to any desired file extension when using this function
        Returns:
            orig_file_path:
                The direct file path like "c:"
            new_export:
                This is the new file name - default is CSV
        You need to import two standard libraries: pathlib and platform
            pathlib is the bread and butter of the function
            platform is just to check the operating system and perform a simple conversion
    """
    str(orig_file_path) = pl.Path(some_file)
    parent_path = orig_file_path.parent
    new_filename = orig_file_path.stem + '.' + file_convert

    directory_pathing = '/'
    if pf.system().lower() == 'windows':
        directory_pathing = '\\'

    new_export = parent_path + directory_pathing + new_filename

    return orig_file_path, new_export
