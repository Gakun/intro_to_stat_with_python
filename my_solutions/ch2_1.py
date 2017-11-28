"""
Solution to CH2 Exercise "Data Input"
"""


import pandas as pd
import numpy as np
import urllib2
import zipfile
import io


def getDataDobson(url, infile):
    '''Extract data from a zipped-archive'''

    # get the zip-archive
    req = urllib2.Request(url)
    GLM_archive = urllib2.urlopen(req).read()

    # make the archive available as a byte-stream
    zipdata = io.BytesIO()
    zipdata.write(GLM_archive)

    # extract the requested file from the archive, as a pandas XLS-file
    myzipfile = zipfile.ZipFile(zipdata)
    xlsfile = myzipfile.open(infile)

    # read the xls-file into Python, using Pandas, and return the extracted data
    df_ = pd.read_excel(xlsfile, skiprows=2)
    print df_.tail()


if __name__ == '__main__':
    # Read in a CSV file, and show the top:
    path = r'../data/swim100m.csv'
    df = pd.read_csv(path, header=0)
    print df.head()

    # Read in an excel file, and show the bottom
    xls = r'../data/Table 2.8 Waist loss.xls'
    df2 = pd.read_excel(xls, skiprows=2)
    print df2.tail(5)
    url = 'http://cdn.crcpress.com/downloads/C9500/GLM_data.zip'

    # Read in a zipped data-file from the WWW
    url = r'http://cdn.crcpress.com/downloads/C9500/GLM_data.zip'
    inFile = r'GLM_data/Table 2.8 Waist loss.xls'
    getDataDobson(url, inFile)

