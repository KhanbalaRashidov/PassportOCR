import base64
import os
import re
from datetime import date
from PIL import Image
from mrz_reader import mrz_reader

mrz_reader = mrz_reader()
mrz_reader.load()


countries={
    "AFG":"Afghanistan",
    "ALB":"Albania",
    "DZA":"Algeria",
    "ASM":"American Samoa",
    "AND":"Andorra",
    "AGO":"Angola",
    "AIA":"Anguilla",
    "ATA":"Antarctica",
    "ATG":"Antigua and Barbuda",
    "ARG":"Argentina",
    "ARM":"Armenia",
    "ABW":"Aruba",
    "AUS":"Australia",
    "AUT":"Austria",
    "AZE":"Azerbaijan",
    "BHS":"Bahamas",
    "BHR":"Bahrain",
    "BGD":"Bangladesh",
    "BRB":"Barbados",
    "BLR":"Belarus",
    "BEL":"Belgium",
    "BLZ":"Belize",
    "BEN":"Benin",
    "BMU":"Bermuda",
    "BTN":"Bhutan",
    "BOL":"Bolivia",
    "BIH":"Bosnia and Herzegovina",
    "BWA":"Botswana",
    "BVT":"Bouvet Island",
    "BRA":"Brazil",
    "IOT":"British Indian Ocean Territory",
    "BRN":"Brunei Darussalam",
    "BGR":"Bulgaria",
    "BFA":"Burkina Faso",
    "BDI":"Burundi",
    "KHM":"Cambodia",
    "CMR":"Cameroon",
    "CAN":"Canada",
    "CPV":"Cape Verde",
    "CYM":"Cayman Islands",
    "CAF":"Central African Republic",
    "TCD":"Chad",
    "CHL":"Chile",
    "CHN":"China",
    "CXR":"Christmas Island",
    "CCK":"Cocos (Keeling) Islands",
    "COL":"Colombia",
    "COM":"Comoros",
    "COG":"Congo",
    "COK":"Cook Islands",
    "CRI":"Costa Rica",
    "CIV":"Côte d'Ivoire",
    "HRV":"Croatia",
    "CUB":"Cuba",
    "CYP":"Cyprus",
    "CZE":"Czech Republic",
    "PRK":"Democratic People's Republic of Korea",
    "COD":"Democratic Republic of the Congo",
    "DNK":"Denmark",
    "DJI":"Djibouti",
    "DMA":"Dominica",
    "DOM":"Dominican Republic",
    "TMP":"East Timor",
    "ECU":"Ecuador",
    "EGY":"Egypt",
    "SLV":"El Salvador",
    "GNQ":"Equatorial Guinea",
    "ERI":"Eritrea",
    "EST":"Estonia",
    "ETH":"Ethiopia",
    "FLK":"Falkland Islands (Malvinas)",
    "FRO":"Faeroe Islands",
    "FJI":"Fiji",
    "FIN":"Finland",
    "FRA":"France",
    "FXX":"France, Metropolitan",
    "GUF":"French Guiana",
    "PYF":"French Polynesia",
    "GAB":"Gabon",
    "GMB":"Gambia",
    "GEO":"Georgia",
    "D":"Germany",
    "GHA":"Ghana",
    "GIB":"Gibraltar",
    "GRC":"Greece",
    "GRL":"Greenland",
    "GRD":"Grenada",
    "GLP":"Guadeloupe",
    "GUM":"Guam",
    "GTM":"Guatemala",
    "GIN":"Guinea",
    "GNB":"Guinea-Bissau",
    "GUY":"Guyana",
    "HTI":"Haiti",
    "HMD":"Heard and McDonald Islands",
    "VAT":"Holy See (Vatican City State)",
    "HND":"Honduras",
    "HKG":"Hong Kong",
    "HUN":"Hungary",
    "ISL":"Iceland",
    "IND":"India",
    "IDN":"Indonesia",
    "IRN":"Iran, Islamic Republic",
    "IRQ":"Iraq",
    "IRL":"Ireland",
    "ISR":"Israel",
    "ITA":"Italy",
    "JAM":"Jamaica",
    "JPN":"Japan",
    "JOR":"Jordan",
    "KAZ":"Kazakhstan",
    "KEN":"Kenya",
    "KIR":"Kiribati",
    "KWT":"Kuwait",
    "KGZ":"Kyrgyzstan",
    "LAO":"Lao People's Democratic Republic",
    "LVA":"Latvia",
    "LBN":"Lebanon",
    "LSO":"Lesotho",
    "LBR":"Liberia",
    "LBY":"Libyan Arab Jamahiriya",
    "LIE":"Liechtenstein",
    "LTU":"Lithuania",
    "LUX":"Luxembourg",
    "MDG":"Madagascar",
    "MWI":"Malawi",
    "MYS":"Malaysia",
    "MDV":"Maldives",
    "MLI":"Mali",
    "MLT":"Malta",
    "MHL":"Marshall Islands",
    "MTQ":"Martinique",
    "MRT":"Mauritania",
    "MUS":"MYT",
    "MEX":"Mexico",
    "FSM":"Micronesia, Federated States of",
    "MCO":"Monaco",
    "MNG":"Mongolia",
    "MNE":"Montenegro",
    "MSR":"Montserrat",
    "MAR":"Morocco",
    "MOZ":"Mozambique",
    "MMR":"Myanmar",
    "NAM":"Namibia",
    "NRU":"Nauru",
    "NPL":"Nepal",
    "NLD":"Netherlands, Kingdom of the",
    "ANT":"Netherlands Antilles",
    "NTZ":"Neutral Zone",
    "NCL":"New Caledonia",
    "NZL":"New Zealand",
    "NIC":"Nicaragua",
    "NER":"Niger",
    "NGA":"Nigeria",
    "NIU":"Niue",
    "NFK":"Norfolk Island",
    "MNP":"Northern Mariana Islands",
    "NOR":"Norway",
    "OMN":"Oman",
    "PAK":"Pakistan",
    "PLW":"Palau",
    "PSE":"Palestine",
    "PAN":"Panama",
    "PNG":"Papua New Guinea",
    "PRY":"Paraguay",
    "PER":"Peru",
    "PHL":"Philippines",
    "PCN":"Pitcairn",
    "POL":"Poland",
    "PRT":"Portugal",
    "PRI":"Puerto Rico",
    "QAT":"Qatar",
    "KOR":"Republic of Korea",
    "MDA":"Republic of Moldova",
    "REU":"Réunion",
    "ROU":"Romania",
    "RUS":"Russian Federation",
    "RWA":"Rwanda",
    "SHN":"Saint Helena",
    "KNA":"Saint Kitts and Nevis",
    "LCA":"Saint Lucia",
    "SPM":"Saint Pierre and Miquelon",
    "VCT":"Saint Vincent and the Grenadines",
    "WSM":"Samoa",
    "SMR":"San Marino",
    "STP":"Sao Tome and Principe",
    "SAU":"Saudi Arabia",
    "SRB":"Serbia",
    "SEN":"Senegal",
    "SYC":"Seychelles",
    "SLE":"Sierra Leone",
    "SGP":"Singapore",
    "SVK":"Slovakia",
    "SVN":"Slovenia",
    "SLB":"Solomon Islands",
    "SOM":"Somalia",
    "ZAF":"South Africa",
    "SGS":"South Georgia and the South Sandwich Island",
    "SSD":"South Sudan",
    "ESP":"Spain",
    "LKA":"Sri Lanka",
    "SDN":"Sudan",
    "SUR":"Suriname",
    "SJM":"Svalbard and Jan Mayen Islands",
    "SWZ":"Swaziland",
    "SWE":"Sweden",
    "CHE":"Switzerland",
    "SYR":"Syrian Arab Republic",
    "TWN":"Taiwan Province of China",
    "TJK":"Tajikistan",
    "TLS":"Timor Leste",
    "THA":"Thailand",
    "MKD":"The former Yugoslav Republic of Macedonia",
    "TGO":"Togo",
    "TKL":"Tokelau",
    "TON":"Tonga",
    "TTO":"Trinidad and Tobago",
    "TUN":"Tunisia",
    "TUR":"Turkey",
    "TKM":"Turkmenistan",
    "TCA":"Turks and Caicos Islands",
    "TUV":"Tuvalu",
    "UGA":"Uganda",
    "UKR":"Ukraine",
    "ARE":"United Arab Emirates",
    "GBR":"United Kingdom of Great Britain and Northern Ireland Citizen",
    "GBD":"United Kingdom of Great Britain and Northern Ireland Dependent Territories Citizen",
    "GBN":"United Kingdom of Great Britain and Northern Ireland National (oversees)",
    "GBO":"United Kingdom of Great Britain and Northern Ireland Oversees Citizen",
    "GBP":"United Kingdom of Great Britain and Northern Ireland Protected Person",
    "GBS":"United Kingdom of Great Britain and Northern Ireland Subject",
    "TZA":"United Republic of Tanzania",
    "USA":"United States of America",
    "UMI":"United States of America Minor Outlying Islands",
    "URY":"Uruguay",
    "UZB":"Uzbekistan",
    "VUT":"Vanuatu",
    "VEN":"Venezuela",
    "VNM":"Viet Nam",
    "VGB":"Virgin Islands (Great Britian)",
    "VIR":"Virgin Islands (United States)",
    "WLF":"Wallis and Futuna Islands",
    "ESH":"Western Sahara",
    "YEM":"Yemen",
    "ZAR":"Zaire",
    "ZMB":"Zambia",
    "ZWE":"Zimbabwe",
    "UNO":"United Nations Organization Official",
    "UNA":"United Nations Organization Specialized Agency Official",
    "XAA":"Stateless (per Article 1 of 1954 convention)",
    "XXB":"Refugee (per Article 1 of 1951 convention, amended by 1967 protocol)",
    "XXC":"Refugee (non-convention)",
    "XXX":"Unspecified / Unknown"
    
    
}

def removeJunk(txt):
        return txt.replace('<', '').replace(' ', '')

def fixDigits(txt):
        data = [('A','-'),('B',8),('C','-'),('D',0),('E',3),('F',7),('G',6),('H',8),('I',1),('J','-'),('K',8),('L','-'),('M','-'),('N','-'),('O',0),('P',9),('Q',2),('R','-'),('S',5),('T',7),('U',0),('V','-'),('W','-'),('X','-'),('Y',5),('Z',2)]
        for  t in data:
              txt=txt.replace(t[0], t[1])
        return txt 

def fixLettera(txt):
        data = [(0,'O'),(1,'I'),(2,'Z'),(3,'-'),(4,'A'),(5,'S'),(6,'G'),(7,'T'),(8,'B'),(9,'-')]
        for t in data:
            txt=txt.replace(str(t[0]),t[1])
        return txt

def getDate(txt):
    today=int(str(date.today())[2:4])+15
    year=txt[0:2]
    month=txt[2:4]
    day=txt[4:]
    
    print(today)
    
    if today<=int(txt[0:2]):
       year='19'+txt[0:2]
    else:
      year='20'+txt[0:2]
    return day+'-'+month+'-'+year

def getPortire(img):
    image_name='portire.jpg'
    image=Image.open(img).convert('RGB')
    portire= image.crop((20,60,180,260))
    portire.save(image_name)
    
    data=getImage(image_name)
    
    os.remove(image_name)
        
    return data

def getSignature(img):
    image_name='signature.jpg'
    image=Image.open(img).convert('RGB')
    signature=image.crop((405,227,580,295))
    signature.save(image_name)
    
    data=getImage(image_name)
    os.remove(image_name)
    return data
    
def getImage(img):
     with open(img, "rb") as image_file:
        data = base64.standard_b64encode(image_file.read())   
     return "data:image/jpg;base64," + data.decode('utf-8')        

def getPaasportText(img):
        txt,face=mrz_reader.predict(img)
        indices=[0,44]
        lines=[txt[index:] for index in indices]
        if  len(lines[0])<35:
            return ({},0)
        lines[1]=lines[1].replace('\n', '')
        if len(lines[1])<28:
            return({},0)
        
        doucumentType=lines[0][0]
        
        passportType= removeJunk(lines[0][0:2])
        
        countryCode=lines[0][2:5]
        
        temp= re.findall(r'\w+',lines[0][5:])
        
        surname=fixLettera(temp[0])
        
        name_index=lines[0].find('<<')+2
        givenName= lines[0][name_index:44]
        givenIndex=givenName.find('<')
        firstName=removeJunk(givenName[0:givenIndex]) + ' ' +removeJunk(givenName[givenIndex:])
        
        passportNo= removeJunk(lines[1][:9])
        
        nationality=countries[lines[1][10:13]]
        
        dateOfBirty=lines[1][13:19]
        
        gender=fixLettera(lines[1][20])
        
        expiryDate=lines[1][21:27]
        
        personalNumber=removeJunk(lines[1][28:42])
        
        personData={
            "documentType":doucumentType,
            "passportType":passportType,
            "countryCode":countryCode,
            "surname":surname,
            "firstName":firstName,
            "passportNo":passportNo,
            "nationality":nationality,
            "dateOfBirth": getDate(dateOfBirty),
            "gender":gender,
            "expiryDate": getDate(expiryDate),
            "mrz": txt,
            "personalNumber":personalNumber,
            "portire":getPortire(img=img),
            "passport":getImage(img=img),
           # "signature":getSignature(img=img)
        }
        
        return personData