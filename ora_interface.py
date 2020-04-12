import sys, argparse

from ora_reader import OraPresentation, OraReader
import tempfile

def main():
    parser = argparse.ArgumentParser(description="Converts .ora files into HTML presentations.")
    parser.add_argument("input", help="All input files, either a single filer, or collected files via *.ora", type=str)
    parser.add_argument("output", help="Output directory", type=str)

    args = parser.parse_args()

    print(args.input, args.output)

    p = OraPresentation(outputDir=args.output, buildDir=tempfile.mkdtemp())
    p.load_from_folder(args.input, with_background=False, overwrite=True)
    p.write_html(html_template_filename="./html_templates/default.html_template")



if __name__ == "__main__":
    main()