#! /usr/bin/python

from FreeLing import *
import sys

## Modify this line to be your FreeLing installation directory
FREELINGDIR = "/usr"
DATA = FREELINGDIR+"/share/FreeLing/"

# create options set for maco analyzer. Default values are Ok, except for data files.
op=maco_options("en");
op.set_active_modules(True,True,True,True,True,True,True,True,0);
#print DATA+"en/locucions.dat"
op.set_data_files(DATA+"en/locucions.dat", DATA+"en/quantities.dat", 
                  DATA+"en/afixos.dat",
                  DATA+"en/probabilitats.dat", 
                  DATA+"en/maco.db", DATA+"en/np.dat",  
                  DATA+"common/punct.dat")

# create analyzers
tk=tokenizer(DATA+"en/tokenizer.dat")
sp=splitter(DATA+"en/splitter.dat")

mf=maco(op);
tg=hmm_tagger("en",DATA+"en/tagger.dat",1,2);
sen=senses(DATA+"en/senses16.db",0);
DATA = """I feel for Google \u2013 Steve Jobs threatened to sue me, too.\nIn 2003, after I unveiled a prototype Linux desktop called Project Looking Glass *, Steve called my office to let me know the graphical effects were \u201cstepping all over Apple\u2019s IP.\u201d (IP = Intellectual Property = patents, trademarks and copyrights.) If we moved forward to commercialize it, \u201cI\u2019ll just sue you.\u201d\nMy response was simple. \u201cSteve, I was just watching your last presentation, and Keynote looks identical to Concurrence \u2013 do you own that IP?\u201d Concurrence was a presentation product built by Lighthouse Design, a company I\u2019d help to found and which Sun acquired in 1996. Lighthouse built applications for NeXTSTEP, the Unix based operating system whose core would become the foundation for all Mac products after Apple acquired NeXT in 1996. Steve had used Concurrence for years, and as Apple built their own presentation tool, it was obvious where they\u2019d found inspiration . \u201cAnd last I checked, MacOS is now built on Unix. I think Sun has a few OS patents, too.\u201d Steve was silent.\nAnd that was the last I heard on the topic. Although we ended up abandoning Looking Glass, Steve\u2019s threat didn\u2019t figure into our decision (the last thing enterprises wanted was a new desktop \u2013 in hindsight, exactly the wrong audience to poll (we should\u2019ve been asking developers, not CIO\u2019s)).\nBluster and Threat (Often Credible)\nAs in life, bluster and threat are commonplace in business \u2013 especially the technology business. So that interaction was good preparation for a later meeting with Bill Gates and Steve Ballmer. They\u2019d flown in over a weekend to meet with Scott McNealy, Sun\u2019s then CEO \u2013 who asked me and Greg Papadopoulos (Sun\u2019s CTO) to accompany him. As we sat down in our Menlo Park conference room, Bill skipped the small talk, and went straight to the point, \u201cMicrosoft owns the office productivity market, and our patents read all over OpenOffice.\u201d OpenOffice is a free office productivity suite found on tens of millions of desktops worldwide. It\u2019s a tremendous brand ambassador for its owner \u2013 it also limits the appeal of Microsoft Office to businesses and those forced to pirate it. Bill was delivering a slightly more sophisticated variant of the threat Steve had made, but he had a different solution in mind. \u201cWe\u2019re happy to get you under license.\u201d That was code for \u201cWe\u2019ll go away if you pay us a royalty for every download\u201d \u2013 the digital version of a protection racket.\nRoyalty bearing free software? Jumbo shrimp. (Oxymoron.)\nBut fearing this was on the agenda, we were prepared for the meeting. Microsoft is no stranger to imitating successful products, then leveraging their distribution power to eliminate a competitive threat \u2013 from tablet computing to search engines, their inspiration is often obvious (I\u2019m trying to like Bing, I really am). So when they created their web application platform, .NET, it was obvious their designers had been staring at Java \u2013 which was exactly my retort. \u201cWe\u2019ve looked at .NET, and you\u2019re trampling all over a huge number of Java patents. So what will you pay us for every copy of Windows?\u201d Bill explained the software business was all about building variable revenue streams from a fixed engineering cost base, so royalties didn\u2019t fit with their model\u2026 which is to say, it was a short meeting.\nI understand the value of patents \u2013 offensively and, more importantly, for defensive purposes. Sun had a treasure trove of some of the internet\u2019s most valuable patents \u2013 ranging from search to microelectronics \u2013 so no one in the technology industry could come after us without fearing an expensive counter assault. And there\u2019s no defense like an obvious offense.\nBut for a technology company, going on offense with software patents seems like an act of desperation, relying on the courts instead of the marketplace. See Nokia\u2019sse2"""
DATA2 = """By John Timmer | Last updated March 19, 2010 6:38 AM\nEarlier this year, Amazon found itself in a showdown over e-book pricing with publisher Macmillan, which wanted the ability to set pricing for its works. Amazon initially pulled all of Macmillan's titles off its virtual shelves but, a few days later, conceded there was little it could do \u2014Macmillan's works went back on sale, and Amazon apparently gave up on trying to force its prices on the company. Despite that rousing lack of success, reports are now indicating that several other publishers may get the same treatment, as Amazon is threatening to stop selling their works as well.\nIndications of an ongoing fight between Amazon and book publishers were apparent almost as soon as the Macmillan matter was settled . Amazon had been purchasing e-books from publishers at a wholesale rate, which allowed it to set the retail prices; rumor had it that the company was selling works at a loss in order to push Kindle sales. Publishers, which have an obvious interest in keeping prices for their work higher, were certainly not pleased with this approach.\nThe impending entry of Apple into the e-book field seems to have brought matters to a head. Apple apparently offered publishers an agency model, in which they get to set prices for their works and simply provide Apple with its (apparently standard) 30 percent cut. In essence, Apple did to Amazon what Amazon had done to it in the music business, where the labels have now been granted the ability to set their own prices by both companies after Amazon pioneered that deal.\nBoth The New York Times and Publisher's Marketplace ( paywall-free excerpt available ) now indicate that Amazon has accepted the agency model, but is seeking to burden it with terms that the publishers are not anxious to go along with. But, should they refuse, the retailer is threatening to give them the Macmillan treatment and stop selling their books.\nFor starters, Amazon wants to lock the publishers into three-year contracts. With several new Kindle competitors either released or very close to market, the e-book economy is likely to experience a time of significant flux, so the publishers would rather reserve the right to keep their options open to adapt to any changes that occur.\nThe other sticking point appears to be a price lock-in: both Apple and Amazon are looking for contracts in which both are guaranteed the lowest price being offered. That would eliminate the ability of publishers to favor one or the other e-book store by offering it better prices. Again, the publishers have probably learned from the record labels' experience that wielding this sort of favoritism can be an extremely powerful lever, and are unlikely to be happy about giving it up.\nThe surprise, however, is that Amazon is even bothering to try this with the major publishers after its failure to bring Macmillan to heel. One of its weaknesses here is the success of its programs for affiliates and used books; even if Amazon pulls its own sales of a major work, it's often easy to use the company's Web interface to pick it up used or from a retailer that uses Amazon's storefront.\nAs The Times points out, the threat is likely to carry a lot more weight with smaller publishers, who don't have a large presence in the retail market, meaning Amazon is their primary outlet for\u00a0Web\u00a0sales. As usual, the little guys are most likely to be trampled as the retailing and publishing giants scuffle.\nUser comments\nDon't Miss : Promos & Insight\n-1\ncenturies\n"""

lin="Mary had a little lamb. Is it really a lost cause."
print type(DATA)
l = tk.tokenize(DATA);
#print l
ls = sp.split(l,False);
#print ls
ls = mf.analyze(ls);
#ls = tg.analyze(ls);
print ls
    #sen.analyze(ls);

for s in ls :
    ws = s.get_words();
    for w in ws :
        if w.get_parole() == 'NNP':
            print w.get_form(), w.get_span_start(), w.get_span_finish()
        #print w.get_form()+" "+w.get_lemma()+" "+w.get_parole()+" "+w.get_senses_string();
        #print w.get_form(), w.get_parole()
        #print;



l = tk.tokenize(DATA2);
#print l
ls = sp.split(l,False);
#print ls
ls = mf.analyze(ls);
#ls = tg.analyze(ls);
print ls
    #sen.analyze(ls);

for s in ls :
    ws = s.get_words();
    for w in ws :
        if w.get_parole() == 'NNP':
            print w.get_form(), w.get_span_start(), w.get_span_finish()
        #print w.get_form()+" "+w.get_lemma()+" "+w.get_parole()+" "+w.get_senses_string();
        #print w.get_form(), w.get_parole()
        #print;
