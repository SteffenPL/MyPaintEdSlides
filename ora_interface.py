import sys, argparse, os
from distutils.dir_util import copy_tree

from ora_reader import OraPresentation, OraReader
import tempfile

def main():
    parser = argparse.ArgumentParser(description="Converts .ora files into HTML presentations.")
    parser.add_argument("template", help="Template directory", type=str, default=os.path.join("html_templates","reveal_with_chalkboard","default.html_template"))
    parser.add_argument("input", help="All input files, either a single filer, or collected files via *.ora", type=str)
    parser.add_argument("output", help="Output directory", type=str)

    args = parser.parse_args()

    print(args.input, args.output)

    p = OraPresentation(outputDir=args.output, buildDir=tempfile.mkdtemp())
    p.load_from_folder(args.input, with_background=False, overwrite=True)
    
    copy_tree(os.path.dirname(args.template),args.output)
    p.write_html(html_template_filename= args.template)




if __name__ == "__main__":
    main()