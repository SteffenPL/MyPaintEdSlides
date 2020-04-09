from ora_reader import OraPresentation, OraReader

#p = OraPresentation("/tmp/build","output")

#p.load_from_folder(".")
#p.generate_slide(with_background=False, overwrite=True)

#ora = OraReader("/tmp/build","output")
#ora.load_file("test_slide.ora")
#ora.generate_slides(with_background=False, overwrite=False)

p = OraPresentation(buildDir="/tmp/build", outputDir="test_mypaint")
p.load_from_folder("test_slide.ora",with_background=False,overwrite=True)

p.write_html(html_template_filename="../html_templates/default.html_template")




p = OraPresentation(buildDir="/tmp/build", outputDir="test_krita")
p.load_from_folder("test/test_krita.ora",with_background=False,overwrite=True)

p.write_html(html_template_filename="../html_templates/default.html_template")
