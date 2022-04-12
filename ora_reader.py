import html
import zipfile
import os
import glob

import xml.etree.ElementTree as ET
from PIL import Image
import numpy as np
from copy import deepcopy

class Layer:
    def __init__(self, name):
        self.name = deepcopy(name)
        self.img_np : np.array = None
        self.x = 0.
        self.y = 0.
        self.z = 0.
        self.opacity = 1.

def image_to_array(img : Image ):
    return np.asarray(img, dtype=np.float32) / 255.

def array_to_image(img_np: Image ):
    return Image.fromarray(np.uint8( 255. * img_np ))


def over(fg : Image, offset, bg : Image, fg_opacity=1.) -> Image:
    x, y = offset
    h_fg, w_fg = fg.shape[:2]
    h_bg, w_bg = bg.shape[:2]

    # cut down to the background
    w = min(w_fg, w_bg-x)
    h = min(h_fg, h_bg-y)
    a = -min(x,0)
    b = -min(y,0)

    src_rgb = fg[b:h, a:w, :3]
    src_a = fg[b:h, a:w, 3] * fg_opacity
    dst_rgb = bg[y+b:y+h, x+a:x+w, :3]
    dst_a = bg[y+b:y+h, x+a:x+w, 3]

    out_a = src_a + dst_a * (1.0 - src_a)
    out_rgb = (src_rgb * src_a[...,None]
               + dst_rgb * (1.0 - src_a[..., None]))

    bg[y+b:y+h, x+a:x+w, :3] = out_rgb
    bg[y+b:y+h, x+a:x+w, 3] = out_a
    return bg

class OraReader:
    def __init__(self, buildDir, outputDir, use_groups):
        self.buildDir = buildDir
        self.outputDir = outputDir
        self.prefix = "slide"
        self.use_groups = use_groups

        if buildDir is None:
            # create temporary build dir
            pass

        if outputDir is None:
            outputDir = "slides"

        self.layers = []
        self.bg = None
        self.slide_defs = []
        self.height = 0
        self.width = 0

    def load_file(self, filename):

        self.prefix = os.path.basename(filename).replace(".ora","")
        unzip_dir = self.buildDir + "/" + self.prefix

        print("Load slide '%s'.\n" % filename )

        if not os.path.exists(filename):
            print("Slide not found at '%s'!\n" % filename)
            return

        zip_ref = zipfile.ZipFile(filename, 'r')
        zip_ref.extractall(unzip_dir)
        zip_ref.close()

        # open the xml file, which defines the layers and their position

        tree = ET.parse(unzip_dir + "/stack.xml")
        root = tree.getroot()

        self.height = int(root.attrib["h"])
        self.width = int(root.attrib["w"])

        z = 0

        if self.use_groups:
                
            last_slide = [0]
            current_slides = []
            
            
            def parse_stack(stack):
                nonlocal last_slide, current_slides
                
                last_slide[-1] += 1
                last_slide.append(0)
                
                for layer_elem in reversed(stack):
                    
                    if layer_elem.tag == 'stack':
                        parse_stack(layer_elem)
                    
                    if layer_elem.tag == 'layer':
                        img_path = unzip_dir + "/" + layer_elem.attrib["src"]

                        last_slide[-1] += 1
                        print("Create layer %s" % last_slide )
                        layer = Layer(last_slide)
                        layer.x = int(layer_elem.attrib["x"])
                        layer.y = int(layer_elem.attrib["y"])
                        layer.opacity = float(layer_elem.attrib["opacity"])
                        layer.img_np = image_to_array(Image.open(img_path, 'r'))
                        layer.z = z
            
                        if layer_elem.attrib["name"].lower() == "background":
                            self.bg = layer
                        else:
                            if not "(skip)" in layer_elem.attrib["name"].lower():
                                current_slides.append(deepcopy(last_slide))
                                self.slide_defs.append(deepcopy(current_slides))
                
                            self.layers.append(layer)
                    
                # remove all slides from the current group from the current_slides list
                group_level = len(last_slide)
                
                current_slides = [name for name in current_slides if len(name) < group_level]
                last_slide.pop()
            
            parse_stack(root)
            
        else:
    
            for layer_elem in reversed(root.findall(".//layer")):
                # load .png
                img_path = unzip_dir + "/" + layer_elem.attrib["src"]
                print(img_path)
    
                slide_content : str = layer_elem.attrib["name"]
                parts = slide_content.split(":", maxsplit=1)
                name = parts[0]
    
                print("Create layer %s" % name )
                layer = Layer(name)
                layer.x = int(layer_elem.attrib["x"])
                layer.y = int(layer_elem.attrib["y"])
                layer.opacity = float(layer_elem.attrib["opacity"])
                layer.img_np = image_to_array(Image.open(img_path, 'r'))
    
                if len(parts) == 2:
                    self.slide_defs.append(slide_content)
                layer.z = z
    
                if layer.name.lower() == "background":
                    self.bg = layer
                else:
                    self.layers.append(layer)
    
                z += 1

    def get_slide_filename(self, slide_number):
        return self.prefix + "_" + str(slide_number).zfill(4) + ".png"

    def generate_slides(self, with_background=False, overwrite=True):

        slide_number = 0

        if not os.path.exists(self.outputDir + "/images"):
            os.makedirs(self.outputDir + "/images", exist_ok=True)

        for slide_def in self.slide_defs:

            file_path = self.outputDir + "/images/" + self.get_slide_filename(slide_number)
            if overwrite or not os.path.exists(file_path):
                print("Generate slide: %s" % slide_def )

                if with_background:
                    img_np = self.bg.img_np.copy()
                else:
                    img_np = np.ones((self.height, self.width, 4), dtype=np.float32)
                    img_np[:,:,3] = 0


                for layer in self.layers:
                    if layer.name in slide_def:
                        img_np = over(layer.img_np, (layer.x, layer.y), img_np, fg_opacity=layer.opacity)

                slide_number += 1

                print("Write %s" % file_path )

                array_to_image(img_np).save(file_path)

    def delete_layers(self):
        self.layers = []

class OraPresentation:
    def __init__(self, buildDir : None, outputDir : None):
        self.ora_slides = []
        self.outputDir = outputDir
        self.buildDir = buildDir

    def add_slide(self, ora_slide : OraReader):
        if self.outputDir is not None:
            if ora_slide.outputDir != self.outputDir:
                print("Error: Output directory of slide (%s) does not match presentations output dir (%)"
                      %(ora_slide.outputDir, self.outputDir))
                return
        else:
            self.outputDir = ora_slide.outputDir

        self.ora_slides.append(ora_slide)

    def load_from_folder(self, input_files, with_background=False, overwrite=True, use_groups=True):
        for file in sorted([one_file for pattern in input_files for one_file in glob.glob(pattern) ]):
            ora = OraReader(buildDir=self.buildDir, outputDir=self.outputDir, use_groups=use_groups)
            ora.load_file(file)
            ora.generate_slides(with_background=with_background, overwrite=overwrite)
            self.add_slide(ora)

    def write_html(self, html_template_filename=None):
        template = open(html_template_filename, mode="r")

        os.makedirs(self.outputDir, exist_ok=True)
        out = open(self.outputDir + "/index.html", mode="w")

        tab = 2

        def tabs():
            return "\t"*tab

        def open_tag(str):
            nonlocal tab
            out.write(tabs() + str + "\n")
            tab += 1

        def close_tag(str):
            nonlocal tab
            tab -= 1
            out.write(tabs() + str + "\n")

        def img_tag(fn):
            out.write(tabs() + ('<img data-src="images/%s"' % fn) + "/>\n" )
            out.write(tabs() + '<br/><br/><br/>\n')

        for line in template:
            if "<!--slides-->" in line:

                open_tag('<div class="reveal">')
                open_tag('<div class="slides">')

                for ora in self.ora_slides:

                    open_tag('<section data-transition="slide">')
                    for i in range(0, len(ora.slide_defs)):
                        open_tag('<section>')
                        img_tag(ora.get_slide_filename(i))
                        close_tag('</section>')

                    close_tag('</section>')

                close_tag('</div>')
                close_tag('</div>')
            else:
                out.write(line)
