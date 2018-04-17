import sys, argparse

from ora_reader import OraPresentation, OraReader

def main():
    parser = argparse.ArgumentParser(description="Converts .ora files into HTML presentations.")
    parser.add_argument("input", help="All input files, either a single filer, or collected files via *.ora", type=str)
    parser.add_argument("output", help="Output directory", type=str)

    args = parser.parse_args()

    p = OraPresentation(outputDir=args.output)
    p.load_from_folder(args.input)
    p.write_html(html_template_filename=)


if __name__ == "__main__":
    main()