from ora_reader import OraReader

ora = OraReader("/tmp/build","output")
ora.load_file("test_slide.ora")
ora.generate_slides(with_background=False, overwrite=False)