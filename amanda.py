import shutil
from mako.template import Template
from mako.lookup import TemplateLookup

mylookup = TemplateLookup(directories=['.'], module_directory='/tmp/mako_modules')

def serve_www(filename, templatename, **kwargs):
    st=serve_template(templatename, **kwargs)
    ofile = open(filename,"w")
    ofile.write(st)
    ofile.close()


def add_url(cats):
    for c in cats:
        url = c[1]
        url = url.replace('&', '')
        url = url.replace(' ', '')
        url = url.replace('\'', '')
        url = url + '.html'
        c.append(url)

def serve_template(templatename, **kwargs):
    mytemplate = mylookup.get_template(templatename)
    return mytemplate.render(**kwargs)

title="Amanda Catlin Representation"

copy_files=['style.css',
            'example.css'
            ]

for c in copy_files:
    shutil.copy(c, 'www/'+c)

specials=[['Now Designs, Danica Studio, Stitch & Shuttle, Coca-Cola',
           'Orders of $350 or more qualify for a 10% Freight Cap',
           'Orders of $1,200 or more qualify for Full Freight Deduct when invoice is paid within terms', 
           'images/LogoNowDesigns.png'],

            ['Collapse-It',
             'Orders of $350 or more qualify for a 10% Freight Cap',
             'Orders of $1,500 or more qualify for Free Freight', 'images/LogoCollapseIt.png'],
            ['Progressive',
             'Orders of $750 or more qualify for Free Freight', 'images/LogoProgressive.png'],
            ['Click Clack & Strahl',
             'Orders of $500 or more qualify for Free Freight', 'images/LogoStrahl.jpg'],
            ['The Cheeseknife',
             'Orders of 144 knives qualify for Free Freight', 'images/LogoCheeseKnife.png'],
            ['Signature Housewares',
             'Orders of $500 or more qualify for 10% Freight Cap',
             'Orders of $1,000 or more qualify for Free Freight', 'images/LogoSignature.png'], 
             ['Chef\'n',
              'Orders of $500 or more qualify for 50% off Freight Charges', 
              'Orders of $750 or more qualify for Free Freight', 'images/LogoChefn.png'
],
           ['BIA & Danesco',
            'Orders of $500 or more qualify for 50% off freight charges when invoice is paid within terms',
            'Orders of $1,000 or more qualify for Full Freight Deduct when invoice is paid within terms', 'images/LogoBIA.jpg']
]


categories=[['Home','index.html'],
            ['Current Specials', 'CurrentSpecials.html'],
           ['Crossroads Sales','CrossroadsSales.html'],
           ['Norwest Marketing','NorwestMarketing.html'],
           ['Shows','Shows.html'],
           ['About','About.html'],
           ['Contact','Contact.html'],
           ['Blog' , 'http://amandacatlin.wordpress.com/'],
            ]

crossroads_images=[['images/CSArtland.jpg','Artland'],
['images/CSBoska.jpg', 'Boska'],
['images/CSCalphalon.jpg', 'Calphalon'],
['images/CSClickClackStrahl.jpg', 'Click Clack & Strahl'],
#['images/CSCuriousChef.jpg', 'Curious Chef'],
['images/CSEdgeware.jpg','Kitchen IQ & FireWire'],
['images/CSEuroline.jpg', 'Euroline'],
['images/CSInterDesign.jpg', 'InterDesign'],
['images/CSIslandBamboo.jpg', 'Island Bamboo'],
['images/CSMavea.jpg', 'Mavea'],
['images/CSMetrokane.jpg', 'Metrokane'],
['images/CSNowDesigns.jpg', 'Now Designs, Danica Studio, Stitch and Shuttle, Les Touristes & Coca-Cola'],
['images/CSPackIt.jpg', 'Pack It!'],
['images/CSQSquared.jpg', 'Q Squared'],
['images/CSRiedel.jpg', 'Riedel, Spiegelau & Nachtmann'],
['images/CSSage.jpg', 'Sage'],
['images/CSTheCheeseKnife.jpg', 'The Cheese Knife'],
['images/CSTripar.jpg', 'Tripar'],
['images/CSZoku.jpg', 'Zoku']]

norwest_images=[['images/NWBiaDanesco.jpg','Bia & Danesco'],
['images/NWCasabella.jpg', 'Casabella'],
['images/NWChefn.jpg', 'Chef\'n'],
['images/NWJKAdams.jpg', 'J.K. Adams'],
['images/NWJosephJoseph.jpg', 'Joseph Joseph'],
['images/NWJuraCapresso.jpg', 'Jura Capresso'],
['images/NWMUKitchen.jpg', 'MU Kitchen'],
['images/NWProgressive.jpg', 'Progressive'],
['images/NWRestonLloyd.jpg', 'Reston Lloyd'],
['images/NWShunKai.jpg', 'Shun & Kai'],
['images/NWSignature.jpg', 'Signature Housewares'],
['images/NWUSAPan.jpg', 'USA Pan']]

add_url(crossroads_images)
add_url(norwest_images)

serve_www('www/CurrentSpecials.html', 'CurrentSpecials_template.html', title="Current Specials", categories=categories, specials=specials)
serve_www('www/About.html', 'About_template.html', title="About", categories=categories)
serve_www('www/Shows.html', 'Shows_template.html', title="Shows", categories=categories)
serve_www('www/Contact.html', 'Contact_template.html', title="Contact", categories=categories)
serve_www('www/index.html', 'index_template.html',title=title, categories=categories)
serve_www('www/CrossroadsSales.html', 'CrossroadsSales_template.html', title="Crossroads Sales", categories=categories, images=crossroads_images, imgurl=crossroads_images[0][0])

for cx in crossroads_images:
    serve_www("www/" + cx[2], "CrossroadsSales_template.html", title="Crossroads Sales", categories=categories, images=crossroads_images, imgurl=cx[0])

serve_www("www/NorwestMarketing.html", "CrossroadsSales_template.html", title="Norwest Marketing", categories=categories, images=norwest_images, imgurl=norwest_images[0][0])

for cx in norwest_images:
    serve_www("www/" + cx[2], "CrossroadsSales_template.html", title="Norwest Marketing", categories=categories, images=norwest_images, imgurl=cx[0])

