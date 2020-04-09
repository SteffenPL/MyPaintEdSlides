from ora_reader import OraReader



ora = OraReader("/tmp/build","test_krita",True)
ora.load_file("test/test_krita.ora")
ora.generate_slides(with_background=False, overwrite=False)




ora = OraReader("/tmp/build","output")
ora.load_file("test_slide.ora")
ora.generate_slides(with_background=False, overwrite=False)

