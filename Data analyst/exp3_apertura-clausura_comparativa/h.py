#!/usr/bin/python

from ROOT import TGraph
#import sys
import csv
from datetime import date
import array as arr
from ROOT import TCanvas, gROOT, TGraph, TH1F, TFile, gStyle, TLegend

savefile = TFile("x.root","update")

n = 1
hcpuPerEvent1T = TH1F("hcpuPerEvent1T", "ssim en diferente iteraciones y tam de imagenes en apertura;Iteraciones;ssim", n, 0, n)
hcpuPerEvent4T = TH1F("hcpuPerEvent4T", "CPU time per event;config;CPU time (sec)", n, 0, n)
hcpuPerEvent1AT = TH1F("hcpuPerEvent1AT", "CPU time per event;config;CPU time (sec)", n, 0, n)
hcpuPerEvent1CT = TH1F("hcpuPerEvent1CT", "CPU time per event;config;CPU time (sec)", n, 0, n)
hcpuPerEvent1DT = TH1F("hcpuPerEvent1DT", "CPU time per event;config;CPU time (sec)", n, 0, n)
hcpuPerEvent1ET = TH1F("hcpuPerEvent1ET", "CPU time per event;config;CPU time (sec)", n, 0, n)

class Job:
    """ Job information
    """
 
    def __init__(self, iname, itime,iflag):
        """ constructor creates the data series"""
        self.name = iname
        self.time = itime
        self.flag = iflag


def fillWithPrefix(job) :

    """ Fills histograms with a prefixed label """
    #y = job.cputime #nstep
    hcpuPerEvent1T.Fill(" ", 0)
    hcpuPerEvent1AT.Fill(" ", 0)
    hcpuPerEvent1CT.Fill(" ", 0)
    hcpuPerEvent1DT.Fill(" ", 0)
    hcpuPerEvent1ET.Fill(" ", 0)
    hcpuPerEvent4T.Fill(" ", 0) 
    hcpuPerEvent1T.Fill(" ", 0)
    hcpuPerEvent1AT.Fill(" ", 0)
    hcpuPerEvent1CT.Fill(" ", 0)
    hcpuPerEvent1DT.Fill(" ", 0)
    hcpuPerEvent1ET.Fill(" ", 0)
    hcpuPerEvent4T.Fill(" ", 0) 
    hcpuPerEvent1T.Fill(" ", 0)
    hcpuPerEvent1AT.Fill(" ", 0)
    hcpuPerEvent1CT.Fill(" ", 0)
    hcpuPerEvent1DT.Fill(" ", 0)
    hcpuPerEvent1ET.Fill(" ", 0)
    hcpuPerEvent4T.Fill(" ", 0) 
    hcpuPerEvent1T.Fill(" ", 0)
    hcpuPerEvent1AT.Fill(" ", 0)
    hcpuPerEvent1CT.Fill(" ", 0)
    hcpuPerEvent1DT.Fill(" ", 0)
    hcpuPerEvent1ET.Fill(" ", 0)
    hcpuPerEvent4T.Fill(" ", 0) 
    hcpuPerEvent1T.Fill(" ", 0)
    hcpuPerEvent1AT.Fill(" ", 0)
    hcpuPerEvent1CT.Fill(" ", 0)
    hcpuPerEvent1DT.Fill(" ", 0)
    hcpuPerEvent1ET.Fill(" ", 0)
    hcpuPerEvent4T.Fill(" ", 0) 
    hcpuPerEvent1T.Fill(" ", 0)
    hcpuPerEvent1AT.Fill(" ", 0)
    hcpuPerEvent1CT.Fill(" ", 0)
    hcpuPerEvent1DT.Fill(" ", 0)
    hcpuPerEvent1ET.Fill(" ", 0)
    hcpuPerEvent4T.Fill(" ", 0) 

    
    hcpuPerEvent1T.Fill(" ", 0)
    hcpuPerEvent1AT.Fill(" ", 0)
    hcpuPerEvent4T.Fill(" ", 0)
    hcpuPerEvent1AT.Fill(" ", 0)
    hcpuPerEvent1CT.Fill(" ", 0)
    hcpuPerEvent1DT.Fill(" ", 0)
    hcpuPerEvent1ET.Fill(" ", 0)
 
    hcpuPerEvent1T.Fill(" ", 0)
    hcpuPerEvent1AT.Fill(" ", 0)
    hcpuPerEvent4T.Fill(" ", 0) 
    hcpuPerEvent1CT.Fill(" ", 0)
    hcpuPerEvent1DT.Fill(" ", 0)
    hcpuPerEvent1ET.Fill(" ", 0)

    #.. make sure all labels exist in all histograms
    
    if job.flag== "102":
	hcpuPerEvent1T.Fill(" ", 0)
	hcpuPerEvent1AT.Fill(" ", 0)
	hcpuPerEvent4T.Fill(" ", 0) 
    	hcpuPerEvent1CT.Fill(" ", 0)
    	hcpuPerEvent1DT.Fill(" ", 0)
    	hcpuPerEvent1ET.Fill(" ", 0)
        hcpuPerEvent1T.Fill(job.name, job.time)
    	hcpuPerEvent1AT.Fill(job.name, 0)
        hcpuPerEvent4T.Fill(job.name, 0)
    	hcpuPerEvent1CT.Fill(job.name, 0)
    	hcpuPerEvent1DT.Fill(job.name, 0)
    	hcpuPerEvent1ET.Fill(job.name, 0)

    elif job.flag== "256":
	hcpuPerEvent1T.Fill(" ", 0)
	hcpuPerEvent1AT.Fill(" ", 0)
	hcpuPerEvent4T.Fill(" ", 0)
    	hcpuPerEvent1CT.Fill(" ", 0)
    	hcpuPerEvent1DT.Fill(" ", 0) 
    	hcpuPerEvent1ET.Fill(" ", 0)
        hcpuPerEvent1T.Fill(job.name, 0)
    	hcpuPerEvent1AT.Fill(job.name, job.time)
        hcpuPerEvent4T.Fill(job.name, 0)
    	hcpuPerEvent1CT.Fill(job.name, 0)
    	hcpuPerEvent1DT.Fill(job.name, 0)
    	hcpuPerEvent1ET.Fill(job.name, 0)

    elif job.flag== "128":
	hcpuPerEvent1T.Fill(" ", 0)
	hcpuPerEvent1AT.Fill(" ", 0)
	hcpuPerEvent4T.Fill(" ", 0) 
    	hcpuPerEvent1CT.Fill(" ", 0)
    	hcpuPerEvent1DT.Fill(" ", 0)
    	hcpuPerEvent1ET.Fill(" ", 0)
        hcpuPerEvent1T.Fill(job.name, 0)
    	hcpuPerEvent1AT.Fill(job.name, 0)
        hcpuPerEvent4T.Fill(job.name, job.time)
    	hcpuPerEvent1CT.Fill(job.name, 0)
    	hcpuPerEvent1DT.Fill(job.name, 0)
    	hcpuPerEvent1ET.Fill(job.name, 0)

    elif job.flag== "1128":
	hcpuPerEvent1T.Fill(" ", 0)
	hcpuPerEvent1AT.Fill(" ", 0)
	hcpuPerEvent4T.Fill(" ", 0) 
    	hcpuPerEvent1ET.Fill(" ", 0)
        hcpuPerEvent1T.Fill(job.name, 0)
    	hcpuPerEvent1AT.Fill(job.name, 0)
        hcpuPerEvent1CT.Fill(job.name, job.time)
    	hcpuPerEvent4T.Fill(job.name, 0)
    	hcpuPerEvent1DT.Fill(job.name, 0)
    	hcpuPerEvent1ET.Fill(job.name, 0)

    elif job.flag== "1256":
	hcpuPerEvent1T.Fill(" ", 0)
	hcpuPerEvent1AT.Fill(" ", 0)
	hcpuPerEvent4T.Fill(" ", 0) 
    	hcpuPerEvent1ET.Fill(" ", 0)
        hcpuPerEvent1T.Fill(job.name, 0)
    	hcpuPerEvent1AT.Fill(job.name, 0)
        hcpuPerEvent1DT.Fill(job.name, job.time)
    	hcpuPerEvent4T.Fill(job.name, 0)
    	hcpuPerEvent1CT.Fill(job.name, 0)
    	hcpuPerEvent1ET.Fill(job.name, 0)


    elif job.flag== "1102":
	hcpuPerEvent1T.Fill(" ", 0)
	hcpuPerEvent1AT.Fill(" ", 0)
	hcpuPerEvent4T.Fill(" ", 0) 
    	hcpuPerEvent1DT.Fill(" ", 0)
        hcpuPerEvent1T.Fill(job.name, 0)
    	hcpuPerEvent1AT.Fill(job.name, 0)
        hcpuPerEvent1ET.Fill(job.name, job.time)
    	hcpuPerEvent4T.Fill(job.name, 0)
    	hcpuPerEvent1CT.Fill(job.name, 0)
    	hcpuPerEvent1DT.Fill(job.name, 0)



    return

def beautify(histo, icolor, pos, style) :

    ### setup space inside histograms
    histo.SetStats(0)
    histo.SetMinimum(0)
    histo.SetMaximum(1.2)
    histo.LabelsOption("au","X")
    histo.SetLineColor(1)
    histo.SetFillColor(icolor)
    histo.SetBarWidth(0.15);
    histo.SetBarOffset(0.05*pos)
    histo.SetFillStyle(style)
    return

def readData(fileName):
    # Open file for reading
    file = open(fileName, "r")

    reader = csv.reader(file)
    first=True

    jobs = []
    for row in reader :
        if not first :
            #print 'read: <%s>' % row
            name = row[0]
            ntime = float(row[1])
            nflag = row[2]


            jobs.append( Job(name,ntime,nflag) )
            #print len(jobs)

        else :
            #.. just skip reading header line in file
            first=False
            pass

    file.close()
    return jobs


### Entry point

if __name__ == "__main__":

    ### these are the full series (without normalization)
    jobs = readData("h.csv")
    print("jobs: %i" % len(jobs))

    for job in jobs:
	fillWithPrefix(job)
    beautify(hcpuPerEvent1T, 95, 1,3004)
    beautify(hcpuPerEvent4T, 62, 4,3016)
    beautify(hcpuPerEvent1AT, 92,7,3001)
    beautify(hcpuPerEvent1ET, 97,10,3005)
    beautify(hcpuPerEvent1CT, 52,13,3020)
    beautify(hcpuPerEvent1DT, 80,16,3021)


    gStyle.SetErrorX(0.);
    gStyle.SetOptFit(1)

    ### setup canvas
    c1 = TCanvas('c1','c1', 900, 600 )
    #c1.Divide(1,5)
    c1.SetGrid()


    hcpuPerEvent1T.Draw('histbar')
    hcpuPerEvent1AT.Draw('histbar same')
    hcpuPerEvent4T.Draw('histbar same')


    hcpuPerEvent1ET.Draw('histbar same')
    hcpuPerEvent1CT.Draw('histbar same')
    hcpuPerEvent1DT.Draw('histbar same')

    legend = TLegend(0.1,0.7,0.28,0.9)
    legend.AddEntry(hcpuPerEvent1T,"102x102 Lenna","f")
    legend.AddEntry(hcpuPerEvent4T,"128x128 Lenna","f")
    legend.AddEntry(hcpuPerEvent1AT,"256x256 Lenna","f")
    legend.AddEntry(hcpuPerEvent1ET,"102x102 Baboon","f")
    legend.AddEntry(hcpuPerEvent1CT,"128z128 Baboon","f")
    legend.AddEntry(hcpuPerEvent1DT,"156x156 Baboon","f")
    #legend.AddEntry(hcpuPerEvent4AT,"4 thread and single track in 1","f")
    legend.Draw()
    #c1.cd(5)
    c1.SaveAs("Iteracionesxssim_apertura.png")

    savefile.Write()
    savefile.Close()
