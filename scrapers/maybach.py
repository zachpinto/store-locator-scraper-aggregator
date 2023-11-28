import pandas as pd

# Text data provided
text_data = """
ARIZONA
_______
PARIS OPTIQUE
7135 E. Camelback Rd. Suite 152
Scottsdale, AZ 85251
United States
P +1 480 945 1855
 
PARIS OPTIQUE
15147 N. Scottsdale Rd., Suite 140
Scottsdale, AZ 85254
United States
P +1 480 585 8500
 
CALIFORNIA
_______
DESERT VISION
555 S Sunrise Way #401
Palm Springs, CA 92264
United States
P +1 760 321 8528
 
EUROCOLLECTIVE
563 Newport Center Dr.
Newport Beach, CA 92660
United States
P +1 949 301 8001
 
EYE STRUCTURE
1232 Prospect St.
La Jolla, CA 92037
United States
P +1 858 551 7959
 
GOLDEN VISION
140 W. Valley Blvd, #115
San Gabriel, CA 91776
United States
P +1 626 288 8023
 
GOOD SEE CO.
801 Ocean Front Walk, Suite 1
Venice, CA 90291
United States
P +1 310 452 5357
 
HALL OF FRAMES
453 N. Fairfax Ave.
Los Angeles, CA 90036
United States
P +1 323 651 5976
 
OPTICA SOUTH COAST PLAZA
3333 Bristol Street, Suite 1613
Costa Mesa, CA 92626
United States
P +1 714 662 1222
 
OPTOMETRIX
375 N. Beverly Dr.
Beverly Hills, CA 90210
United States
P +1 310 273 8290
 
COLORADO
_______
EYE PIECES OF VAIL
122 E. Meadow Dr. Unit 1
Vail, CO 81657
United States
P +1 970 476 1947
 
MORGENTHAL FREDERICS
553 E. Cooper
Aspen, CO 81611
United States
P +1 970 925 2007
 
THE GLASS HOUSE OPTICAL
3000 E. 1st Ave. #254
Denver, CO 80206
United States
P +1 303 591 8385
 
CONNECTICUT
_______
SPECS OF WESTPORT
115 Post Road East
Westport, CT 06880
United States
P +1 203 226 8380
 
WASHINGTON DC
_______
GEORGETOWN OPTICIAN
1307 Wisconsin Ave NW
Washington, DC 20007
United States
P +1 202 337 8310
 
MORGENTHAL FREDERICS
941 H Street NW
Washington, DC 20007
United States
P +1 202 204 3393
 
FLORIDA
_______
EDWARD BEINER
Aventura Mall, 19501 Biscayne Boulevard
Aventura, FL 33180
United States
P +1 305 935 8771
 
EDWARD BEINER
6000 Glades Rd.
Boca Raton, FL 33431
United States
P +1 561 391 0011
 
OPTICA BAL HARBOUR SHOPS
9700 Collins Ave.
Bal Harbour, FL 33154
United States
P +1 305 866 2020
 
GROVE OPTICIANS
5250 Town Center Circle #139
Boca Raton, FL 33486
United States
P +1 561 394 5551
 
I-TOPIAN OPTICAL
15245 S. Tamiami Trail, Suite 6
Fort Myers, FL 33908
United States
P +1 239 689 6551
 
ICONS MIAMI EYEWEAR
900 Ocean Drive, Suite A
Miami Beach, FL 33139
United States
P +1 305 534 2550
 
LAVISH EYEWEAR
2001 Collins Avenue
Miami Beach, FL 33139
United States
P +1 305 520 6956
 
COUTURE OPTIQUE
11701 Lake Victoria Gardens Dr.
Palm Beach Gardens, FL 33410
United States
P +1 561 624 0474
 
MORGENTHAL FREDERICS
311 Worth Ave
Palm Beach, FL 33480
United States
P +1 305 866 2020
 
MORGENTHAL FREDERICS
9700 Collins Ave. #244
Bal Harbour, FL 33154
United States
P +1 561 655 3937
 
OBERLE OPTICIANS
9552 Harding Ave
Surfside, FL 33154
United States
P +1 305 861 1010
 
SEE AND SUN OPTICAL
3762 SE Ocean Blvd.
Sewalls Point, FL 34996
United States
P +1 772 247 7573
 
THE EYE PLACE
7828 Winter Garden Vineland Rd., #128
Windermere, FL 34786
United States
P +1 407 876 1200
 
LEXOR MIAMI
2371 NW 20th St
Miami, FL 33142
United States
P +1 305 633 0950
 
MOON & CO EYEWEAR
105 S Lemon Ave
Sarasota, FL 34326
United States
P +1 941 260 8523
 
GEORGIA
_______
SALLE OPTICIANS
3500 Peachtree Rd
Atlanta, GA 30326
United States
P +1 404 816 6266
 
HAWAII
_______
HI-TREND
Hilton Hawaiian Village, 2005 Kalia Road
Honolulu, HI 96815
United States
P +1 808 922 8838
 
ILLINOIS
_______
MORGENTHAL FREDERICS
129 East Oak Street
Chicago, IL 60611
United States
P +1 312 642 2550
 
INDIANA
_______
REVOLUTION EYES
14250 Clay Terrace Blvd., Suite 160
Carmel, IN 46032
United States
P +1 317-844-2020
 
MASSACHUSETTES
_______
EDGE LUXURY EYEWEAR
219 Newbury St.
Boston, MA 02116
United States
P +1 617 331 3687
 
MICHIGAN
_______
BIRMINGHAM VISION CARE
4114 West Maple Road
Bloomfield Twp, MI 48301
United States
P +1 248 539 4800
 
HI-TREND 2.0 OPTICS
23400 Greenfield Road
Oak Park, MI 48237
United States
P
 
OPTICA TROY
2801 W. Big Beaver E132
Troy, MI 48084
United States
P +1 248 643 6220
 
MINNESOTA
_______
ART OF OPTIKS
4999 France Ave. South, Suite 140
Minneapolis, MN 55410
United States
P +1 612 440 2020
 
ART OF OPTIKS
747 Lake Street East
Wayzata, MN 55391
United States
P +1 952 404 2020
 
NORTH CAROLINA
_______
THE SPECTACLE
4209 Lassiter Mill Rd., Suite 110
Raleigh, NC 27609
United States
P +1 919 783 5863
 
NEW JERSEY
_______
ARTIFACT VISIONS
112 Monticello Ave.
Jersey City, NJ 04304
United States
 
BENJAMIN OPTICAL
1 American Dream Way, #A160
East Rutherford, NJ 07073
United States
P +1 201 482 9444
 
EYEDESIGN
90 Broad St
Red Bank, NJ 07701
United States
P +1 732 530 6865
 
GEFEN OPTICAL
6780 U.S 9
Howell, NJ 07731
United States
P +1 732 363 7505
 
NEVADA
_______
OPTICA ARIA
3730 Las Vegas Blvd S.
Las Vegas, NV 89158
United States
P +1 702 479 1043
 
OPTICA BELLAGIO
3600 Las Vegas Blvd S.
Las Vegas, NV 89109
United States
P +1 702 262 5748
 
SUNGLASS OPTIC STUDIO
10300 W Charleston Blvd
Las Vegas, NV 89135
United States
P +1 702 822 2199
 
NEW YORK
_______
ALFA VISION
1402 Sheepshead Bay Rd.
Brooklyn, NY 11235
United States
P +1 718 934 1155
 
E.B. MEYROWITZ AND DELL
19 W. 44th Street
New York, NY 10036
United States
P +1 646 867 3600
 
ENVISION OPTICAL
505 Flushing Ave.
Brooklyn, NY 11205
United States
P +1 718 522 3332
 
EYECRAFTERS OPTICAL
340 Jay St.
Brooklyn, NY 11201
United States
P +1 718 858 5000
 
EYES & OPTICS
2922 Ave L
Brooklyn, NY 11210
United States
P +1 718 758 2020
 
EYES EXCLUSIVE
846 Main St., Suite R4
Buffalo, NY 14202
United States
P +1 716 300 8482
 
FABULOUS OPTICAL
200 West 125th Street
New York, NY 10027
United States
P +1 212 665 5051
 
FABULOUS OPTICAL – JAMAICA
161-11 Jamaica Ave
Jamaica, NY 11432
United States
P +1 646 321 5802
 
FABULOUS OPTICAL – NOSTRAND
546 Nostrand ave
Brooklyn, NY 11216
United States
P +1 212 665 5051
 
J&J PREMIUM EYE CARE
1304 Grand Ave.
Baldwin, NY 11510
United States
P +1 516 442 1570
 
JEWELZ FOR THE FACE
31 W 47TH ST #905
New York, NY 10036
United States
P +1 646 245 5702
 
MICHAEL ALLEN OPTICIANS
7948 Jericho Turnpike
Woodbury, NY 11797
United States
P +1 516 364 1288
 
MORGENTHAL FREDERICS
399 W. Broadway
New York, NY 10012
United States
P +1 212 966 0099
 
MORGENTHAL FREDERICS
944 Madison Ave.
New York, NY 10021
United States
P +1 212 744 9444
 
MORGENTHAL FREDERICS
680 Madison Ave.
New York, NY 10065
United States
P +1 212 838 3090
 
MORGENTHAL FREDERICS AMERICANA
2110-H Northern Blvd
Manhasset, NY 11030
United States
P +1 516 627 6620
 
MORGENTHAL FREDERICS TIME WARNER
10 Columbus Circle
New York, NY 10019
United States
P +1 212 956 6402
 
MS OPTICAL
5202 16th Ave.
Brooklyn, NY 11204
United States
P +1 718 436 5900
 
OCEAN VIEW OPTICAL
254 Brighton Beach Ave.
Brooklyn, NY 11235
United States
P +1 718 769 9800
 
SUPREME VISION CENTER
691 COOP CITY Blvd.
Bronx, NY 10475
United States
P +1 917 642 1035
 
THE LENS CENTER
5511 New Utrecht Ave
Brooklyn, NY 11219
United States
P +1 929 210 3268
 
PENNSYLVANIA
_______
BLINK OPTICAL
415 South Street
Philadelphia PA 19107
United States
P +1 610 570 4655
 
OMNI VISION
1230 Chestnut St
Philadelphia, PA 19107
United States
P +1 215 977 7700
 
SOUTH CAROLINA
_______
JACKSON DAVENPORT
372 King St.
Charleston, SC 29401
United States
P +1 843 722 4416
 
TEXAS
_______
ADAIR EYEWEAR
3550 West 7th Street
Fort Worth, TX 76107
United States
P +1 817 377 3500
 
CARE OPTICAL
7500 Bellaire Blvd., Suite F02
Houston, TX 77036
United States
P +1 713 773 2020
 
OPTICA HOUSTON
The Galleria, 5085 Westheimer, Suite 2805
Houston, TX 77056
United States
P +1 713 621 4225
 
20/20 VISION CARE
1313 South 10th St.
McAllen, TX 78501
United States
P +1 956 630 2020
 
VIRGINIA
_______
GEORGETOWN OPTICIAN – TYSON’S GALLERIA
2001 International Dr
McLean, VA 22102
United States
P +1 703 442 3130
"""

# Split the text into lines
lines = text_data.split("\n")

# Variables to hold the current store's data
current_store_name = ""
current_address = ""
store_data = []

# Iterate over the lines and process each one
for line in lines:
    line = line.strip()
    if not line or line in ["United States", "_______"] or line.startswith("P +"):
        continue

    if line.isupper():  # Assuming store names are in uppercase
        # Save the previous store if present
        if current_store_name:
            store_data.append({'Name': current_store_name, 'Address': current_address})
        current_store_name = line
        current_address = ""
    else:
        current_address += line + " "

# Don't forget to add the last store
if current_store_name:
    store_data.append({'Name': current_store_name, 'Address': current_address})

# Convert to DataFrame and save to CSV
df = pd.DataFrame(store_data)
csv_file_path = '/Users/pintoza/Desktop/dev/python-development/python_store_locator_web_scraper/data/maybach_store_locations.csv'  # Specify your path here
df.to_csv(csv_file_path, index=False)