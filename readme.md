# Name-Letter-Effect in Co-Authorship Networks

Do researchers prefer to collaborate with people who share the first letter of their surname?


### Methods

This is a repository to a Python-script that reads in a database of metadata about scientific publications: Co-Authorship-Networks.

For every combination of first letters of the surname, it counts the occurence of co-authorship.
{'AA': 2394, 'AB':1923, ....., 'ZY':131, 'ZZ': 226}

### Results

The results are plotted with plotly: http://theilemail.de/authorship_dblp_0.html
On the x-Axis you see the expected times of co-authorship of a given pair of first-letter-of-author-surnames (calculated with the absolute number of edges with a first-letter-of-author-surname like this).
On the y-Axis you see the actual Number of co-authorship.



## Data-Sources (and possible data-sources)

 * small sample:
   * cond-mat-2005.xgml (90 MB XML)
   * ?? number of Authors, ?? papers, ?? edges
   * I lost the original source, here is something similar: http://snap.stanford.edu/data/#canets
   
 * big sample (466 MB JSON): 
   * tmp_dblp_coauthorship.json
   * original source:
     * https://dblp.uni-trier.de/xml/
     * https://dblp.uni-trier.de/faq/1474679
   
   * I used the preprocessed json from: https://projects.csail.mit.edu/dnd/DBLP/
   
   ´´´
    dblp.xml.gz (263MB) is a copy of the raw DBLP data from http://dblp.uni-trier.de/xml/dblp.xml.gz
        39,206,851 lines and 1,481,239,034 characters (uncompressed)
        License: Open Data Commons Attribution License (ODC-BY 1.0).
        Format: gzipped XML 
    dblp.json.gz (91MB) is a computed, more succinct version consisting of (paper-key, [author list], year) triples
        4,215,613 papers
        9,086,030 edges between papers and authors
        Format: gzipped JSON
        Sample line format:

        ["conf/www/DemaineHMMRSZ14", ["Erik D. Demaine", "MohammadTaghi Hajiaghayi", "Hamid Mahini", "David L. Malec", "S. Raghavan", "Anshul Sawant", "Morteza Zadimoghaddam"], 2014],

    dblp_coauthorship.json.gz (88MB) is a computed coauthorship graph (half-square) consisting of (author1, author2, year) triples
        1,482,029 unique authors
        10,615,809 timestamped coauthorship edges between authors
        Format: gzipped JSON
        Sample line format:

        ["Erik D. Demaine", "MohammadTaghi Hajiaghayi", 2014],
  ´´´
